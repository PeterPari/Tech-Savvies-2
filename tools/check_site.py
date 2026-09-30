#!/usr/bin/env python3
# To add a check: write `def check_x(site)` that yields (path, line, message) tuples,
# then append ("check-name", check_x) to CHECKS below. `site.pages` holds the parsed HTML
# files (tags, anchors, scripts); `site.text_files()` lists the other text files.
# Run from the repo root: python3 tools/check_site.py [--public DIR] [--netlify FILE]
# Keep checks strict. Record real problems in docs/compliance-log.md; never loosen a check.
import json
import os
import re
import sys
from html import unescape
from html.parser import HTMLParser

SITE_ORIGIN = "https://tech-savvies.com"

EXPECTED_CSP = (
    "default-src 'self'; img-src 'self' data:; font-src 'self'; style-src 'self'; "
    "script-src 'self'; form-action 'self'; frame-ancestors 'none'; base-uri 'self'; "
    "object-src 'none'"
)

# Outbound link origins that are documented in docs/third-parties.md. Add one only after updating that file.
ALLOWED_LINK_ORIGINS = [
    "https://grisha.studio",
    # Privacy policies of the services listed on /privacy/#sharing
    "https://www.netlify.com", "https://automattic.com", "https://www.apple.com",
    "https://www.squarespace.com", "https://www.anthropic.com", "https://openai.com",
]

# Legal name of the business (sole proprietor). Every footer copyright line and the JSON-LD legalName must match.
LEGAL_NAME = "Peter Parizhsky"

# Footer hrefs every page must contain. Later prompts append here, e.g. "/privacy/".
REQUIRED_FOOTER_LINKS = ["/terms/", "/refunds/", "/privacy/", "/cookies/", "/accessibility/"]

# URLs of the old site (before the 2026 relaunch) and the page each one 301-redirects to in netlify.toml.
# Search engines and old links know these, so keep them for good (see migration-plan.md). legacy-redirects
# fails if a rule is missing or changed, if a file in public/ shadows one (Netlify then serves the file
# and skips the rule), if a target doesn't exist, or if public/sw.js (removes the old service worker) is gone.
LEGACY_REDIRECTS = {
    "/services": "/solutions/",
    "/services.html": "/solutions/",
    "/services.md": "/solutions.md",
    "/content/services.md": "/solutions.md",
    "/about": "/our-story/",
    "/about.html": "/our-story/",
    "/about.md": "/our-story.md",
    "/content/about.md": "/our-story.md",
    "/who-is-tech-savvies": "/our-story/",
    "/contact.html": "/contact/",
    "/content/contact.md": "/contact.md",
    "/content/index.md": "/index.md",
    "/assets/logo.png": "/assets/img/logo.png",
    "/assets/logo.webp": "/assets/img/logo.png",
    "/assets/favicon.png": "/assets/img/favicon-64.png",
    "/assets/icon-192.png": "/assets/img/icon-192.png",
    "/assets/icon-512.png": "/assets/img/icon-512.png",
    "/assets/icon-512-maskable.png": "/assets/img/icon-512.png",
}

# Substrings that mark a tracker, pixel or analytics tool. no-trackers fails on any of them in public/
# HTML or JS (case-insensitive). Adding a tracker means a consent banner first: see
# fix-prompts/05-cookie-consent.md, and update docs/tracking-audit.md and the Privacy/Cookie policies.
TRACKER_SIGNATURES = [
    "gtag", "googletagmanager", "google-analytics", "analytics.js", "fbq", "connect.facebook",
    "doubleclick", "hotjar", "clarity.ms", "segment", "mixpanel", "plausible", "umami",
    "cloudflareinsights", "tiktok", "snap.licdn", "sendBeacon", "<noscript><img",
]

# Claims the business can't back up. claims fails on any of them in public/ (case-insensitive, straight
# or curly apostrophe). A new objective claim (a time, number, result, guarantee or fact about the
# business) needs a row in docs/claims-register.md, with its evidence, before it goes on the site.
BANNED_PHRASES = [
    "within 2 hours", "maximum search visibility", "guaranteed ranking", "#1 on Google",
    "lead engineer", "you'll get it",
]

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "param", "source", "track", "wbr"}
TEXT_EXTS = (".html", ".css", ".js", ".txt", ".xml", ".webmanifest", ".json", ".svg")


class Tag:
    def __init__(self, name, attrs, line, in_nav, in_footer):
        self.name = name
        self.attrs = {k: (v or "") for k, v in attrs}
        self.line = line
        self.in_nav = in_nav
        self.in_footer = in_footer


class Anchor:
    def __init__(self, tag):
        self.tag = tag
        self.children = []
        self.has_text = False
        self.hidden_text = ""


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.tags = []
        self.anchors = []
        self.scripts = []  # (line, type, src, content)
        self._stack = []  # (name, hidden, nav, footer)
        self._anchor_stack = []
        self._script = None
        with open(path, encoding="utf-8") as f:
            self.feed(f.read())
        self.close()

    def _ctx(self, attr_name):
        return any(e[attr_name] for e in self._stack)

    def handle_starttag(self, name, attrs):
        line = self.getpos()[0]
        a = dict((k, v or "") for k, v in attrs)
        in_nav = self._ctx(2) or (name == "nav" and a.get("aria-label") == "Main")
        in_footer = self._ctx(3) or name == "footer"
        tag = Tag(name, attrs, line, in_nav, in_footer)
        self.tags.append(tag)
        for anchor in self._anchor_stack:
            anchor.children.append(name)
        if name == "a":
            anchor = Anchor(tag)
            self.anchors.append(anchor)
            self._anchor_stack.append(anchor)
        if name == "script":
            self._script = [line, a.get("type", ""), a.get("src"), ""]
        if name not in VOID:
            hidden = "visually-hidden" in a.get("class", "").split()
            self._stack.append({"name": name, 0: hidden, 2: name == "nav" and a.get("aria-label") == "Main",
                                3: name == "footer"})

    def handle_startendtag(self, name, attrs):
        self.handle_starttag(name, attrs)
        if name not in VOID:
            self.handle_endtag(name)

    def handle_endtag(self, name):
        if name == "script" and self._script:
            self.scripts.append(tuple(self._script))
            self._script = None
        if name in VOID:
            return
        for i in range(len(self._stack) - 1, -1, -1):
            if self._stack[i]["name"] == name:
                del self._stack[i:]
                break
        if name == "a" and self._anchor_stack:
            self._anchor_stack.pop()

    def handle_data(self, data):
        if self._script is not None:
            self._script[3] += data
            return
        if not data.strip():
            return
        for anchor in self._anchor_stack:
            anchor.has_text = True
        if self._ctx(0):
            for anchor in self._anchor_stack:
                anchor.hidden_text += " " + data


class Site:
    def __init__(self, public, netlify):
        self.public = public
        self.netlify = netlify
        self.pages = []
        for path in self._walk(".html"):
            self.pages.append(Page(path))

    def _walk(self, *exts):
        found = []
        for root, _dirs, names in os.walk(self.public):
            for n in names:
                if n.endswith(exts):
                    found.append(os.path.join(root, n))
        return sorted(found)

    def is_admin(self, path):
        return os.path.relpath(path, self.public).split(os.sep)[0] == "admin"

    def text_files(self, *exts):
        return self._walk(*(exts or TEXT_EXTS))

    def read(self, path):
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def is_external(url):
    u = url.strip()
    if u.startswith(SITE_ORIGIN + "/") or u == SITE_ORIGIN:
        return False
    return bool(re.match(r"(?i)(https?:)?//", u))


# --- checks ---------------------------------------------------------------

def check_img_alt(site):
    # Generic alt text that provides no useful info
    generic_patterns = [
        re.compile(r"(?i)^[a-z0-9_\-\.]+\.(png|jpg|jpeg|webp|gif|svg)$"),  # filenames
        re.compile(r"(?i)^image$|^photo$|^picture$|^icon$|^logo$"),  # generic words only
    ]

    for page in site.pages:
        for tag in page.tags:
            if tag.name == "img" and "alt" not in tag.attrs:
                yield page.path, tag.line, "<img> has no alt attribute"
            elif tag.name == "img" and "alt" in tag.attrs:
                alt = tag.attrs["alt"]
                # Check for filename or generic-only alt text
                for pattern in generic_patterns:
                    if pattern.match(alt):
                        yield page.path, tag.line, "alt text %r is a filename or generic word without context" % alt
        for anchor in page.anchors:
            if anchor.children == ["img"] and not anchor.has_text:
                img = next(t for t in page.tags if t.name == "img" and t.line >= anchor.tag.line)
                if not img.attrs.get("alt", "").strip():
                    yield page.path, img.line, "<img> is the only content of a link, so its alt must not be empty"


def check_no_external_resources(site):
    for page in site.pages:
        for tag in page.tags:
            a = tag.attrs
            urls = []
            if tag.name in ("script", "iframe", "img", "video", "audio", "source", "embed", "track") and "src" in a:
                urls.append(a["src"])
            if tag.name in ("img", "source") and "srcset" in a:
                urls += [p.strip().split()[0] for p in a["srcset"].split(",") if p.strip()]
            if tag.name == "video" and "poster" in a:
                urls.append(a["poster"])
            if tag.name == "object" and "data" in a:
                urls.append(a["data"])
            if tag.name == "link":
                rel = a.get("rel", "").lower().split()
                if {"stylesheet", "preload", "modulepreload"} & set(rel) and "href" in a:
                    urls.append(a["href"])
            for u in urls:
                if is_external(u):
                    yield page.path, tag.line, "<%s> loads %s from another origin" % (tag.name, u)
    for path in site.text_files(".css"):
        text = site.read(path)
        for m in re.finditer(r"(?i)url\(\s*['\"]?((?:https?:)?//[^)'\"\s]+)|@import\s+['\"]?((?:https?:)?//[^'\";\s]+)", text):
            u = m.group(1) or m.group(2)
            if is_external(u):
                yield path, line_of(text, m.start()), "CSS loads %s from another origin" % u


STORAGE_RE = re.compile(r"document\s*\.\s*cookie|localStorage|sessionStorage|indexedDB|navigator\s*\.\s*sendBeacon")


def check_no_client_storage(site):
    for path in site.text_files(".js"):
        if site.is_admin(path):
            continue
        text = site.read(path)
        for m in STORAGE_RE.finditer(text):
            yield path, line_of(text, m.start()), "uses %s" % re.sub(r"\s+", "", m.group(0))
    for page in site.pages:
        if site.is_admin(page.path):
            continue
        for line, typ, src, content in page.scripts:
            if src or "json" in typ.lower():
                continue
            for m in STORAGE_RE.finditer(content):
                yield page.path, line + content.count("\n", 0, m.start()), \
                    "inline script uses %s" % re.sub(r"\s+", "", m.group(0))


def check_csp_unchanged(site):
    text = site.read(site.netlify)
    found = re.findall(r'Content-Security-Policy\s*=\s*"([^"]*)"', text)
    if len(found) != 1:
        yield site.netlify, 1, "expected exactly one Content-Security-Policy, found %d" % len(found)
        return
    if found[0] != EXPECTED_CSP:
        m = re.search(r"Content-Security-Policy", text)
        yield site.netlify, line_of(text, m.start()), \
            "CSP differs from EXPECTED_CSP in tools/check_site.py (update both, and docs/third-parties.md)"


def _find_key(node, hits):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "aggregateRating":
                hits.append("aggregateRating")
            if k == "@type" and (v == "Review" or (isinstance(v, list) and "Review" in v)):
                hits.append('"@type": "Review"')
            _find_key(v, hits)
    elif isinstance(node, list):
        for v in node:
            _find_key(v, hits)


def check_no_review_schema(site):
    for page in site.pages:
        for line, typ, src, content in page.scripts:
            if typ.lower() != "application/ld+json":
                continue
            try:
                data = json.loads(content)
            except ValueError as e:
                yield page.path, line, "JSON-LD does not parse: %s" % e
                continue
            hits = []
            _find_key(data, hits)
            for h in hits:
                yield page.path, line, "JSON-LD contains %s" % h


def check_testimonial_source(site):
    for page in site.pages:
        for tag in page.tags:
            classes = tag.attrs.get("class", "").lower()
            if tag.name == "blockquote" or "testimonial" in classes or "review" in classes:
                if not tag.attrs.get("data-source", "").strip():
                    yield page.path, tag.line, \
                        "<%s> is a quote, testimonial or review without a data-source attribute (see docs/testimonials-policy.md)" % tag.name


PLACEHOLDER_RES = [
    re.compile(r"TODO\(owner\)"),
    re.compile(r"(?i)\[PLACEHOLDER"),
    re.compile(r"(?i)lorem ipsum"),
    re.compile(r"XXX"),
    re.compile(r"\[ADDRESS"),
]


def check_no_placeholders(site):
    for path in site.text_files():
        if site.is_admin(path):  # the owner's prompt checklist quotes these strings
            continue
        text = site.read(path)
        for rx in PLACEHOLDER_RES:
            for m in rx.finditer(text):
                yield path, line_of(text, m.start()), "placeholder text %r" % m.group(0)


def check_third_party_allowlist(site):
    for page in site.pages:
        for tag in page.tags:
            u = tag.attrs.get("href", "").strip()
            if tag.name not in ("a", "link", "area") or not is_external(u):
                continue
            m = re.match(r"(?i)(?:(https?):)?//([^/?#]+)", u)
            origin = "%s://%s" % ((m.group(1) or "https").lower(), m.group(2).lower())
            if origin not in ALLOWED_LINK_ORIGINS:
                yield page.path, tag.line, \
                    "href %s goes to %s, which is not in ALLOWED_LINK_ORIGINS (document it in docs/third-parties.md first)" % (u, origin)


def check_internal_links(site):
    for page in site.pages:
        for tag in page.tags:
            for attr in ("href", "src", "action"):
                u = tag.attrs.get(attr)
                if not u or not u.startswith("/") or u.startswith("//"):
                    continue
                path = re.split(r"[?#]", u)[0]
                target = os.path.join(site.public, path.lstrip("/"))
                if path.endswith("/") or os.path.isdir(target):
                    target = os.path.join(target, "index.html")
                if not os.path.isfile(target):
                    yield page.path, tag.line, "%s=%s does not resolve to a file in public/" % (attr, u)


def check_new_tab_links(site):
    for page in site.pages:
        for anchor in page.anchors:
            a = anchor.tag.attrs
            if a.get("target", "").lower() != "_blank":
                continue
            if "noopener" not in a.get("rel", "").lower().split():
                yield page.path, anchor.tag.line, 'target="_blank" link needs rel containing noopener'
            hidden = re.sub(r"\s+", " ", anchor.hidden_text).lower()
            if "(opens in a new tab)" not in hidden:
                yield page.path, anchor.tag.line, 'target="_blank" link needs visually hidden text "(opens in a new tab)"'


def _chrome(page, attr):
    return {t.attrs["href"] for t in page.tags if t.name == "a" and "href" in t.attrs and getattr(t, attr)}


def check_shared_chrome(site):
    home = os.path.join(site.public, "index.html")
    ref = next((p for p in site.pages if p.path == home), None)
    if ref is None:
        yield home, 1, "reference page not found"
        return
    for page in site.pages:
        if site.is_admin(page.path) or page is ref:
            continue
        for attr, label in (("in_nav", "main-nav"), ("in_footer", "footer")):
            want, have = _chrome(ref, attr), _chrome(page, attr)
            if want != have:
                msg = "%s hrefs differ from public/index.html" % label
                if want - have:
                    msg += "; missing %s" % sorted(want - have)
                if have - want:
                    msg += "; extra %s" % sorted(have - want)
                yield page.path, 1, msg


def check_business_details(site):
    for page in site.pages:
        if site.is_admin(page.path):
            continue
        with open(page.path, encoding="utf-8") as f:
            html = f.read()
        m = re.search(r"<footer\b.*?</footer>", html, re.S)
        if not m or LEGAL_NAME not in m.group(0):
            yield page.path, 1, "footer must contain LEGAL_NAME %r" % LEGAL_NAME
        elif not re.search(r"(?:&copy;|©) <span data-year>\d{4}</span> %s\. All rights reserved\." % re.escape(LEGAL_NAME), m.group(0)):
            yield page.path, 1, "footer must read '© <span data-year>YYYY</span> %s. All rights reserved.'" % LEGAL_NAME
    home = os.path.join(site.public, "index.html")
    with open(home, encoding="utf-8") as f:
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', f.read(), re.S)
    names = []
    for b in blocks:
        try:
            names.append(json.loads(b).get("legalName"))
        except ValueError:
            yield home, 1, "JSON-LD does not parse"
    if LEGAL_NAME not in names:
        yield home, 1, "JSON-LD legalName must equal LEGAL_NAME %r" % LEGAL_NAME


def check_no_trackers(site):
    patterns = [(sig, re.compile(re.escape(sig).replace(r"><", r">\s*<"), re.I)) for sig in TRACKER_SIGNATURES]
    for path in site.text_files(".html", ".js"):
        if site.is_admin(path):  # the owner's checklist quotes these names in prompt text
            continue
        text = site.read(path)
        for sig, rx in patterns:
            for m in rx.finditer(text):
                yield path, line_of(text, m.start()), "contains tracker signature %r" % sig


def check_required_footer_links(site):
    for page in site.pages:
        if site.is_admin(page.path):
            continue
        have = _chrome(page, "in_footer")
        for link in REQUIRED_FOOTER_LINKS:
            if link not in have:
                yield page.path, 1, "footer is missing link %s" % link


CONSENT_MESSAGE = "Non-essential storage or tracking added without consent. See fix-prompts/05-cookie-consent.md"


def check_consent_required(site):
    pages = [p for p in site.pages if not site.is_admin(p.path)]
    if any("data-consent-banner" in t.attrs for p in pages for t in p.tags):
        return
    sig_rx = re.compile("|".join(re.escape(s) for s in TRACKER_SIGNATURES if "<" not in s), re.I)

    def uses_tracking(text):
        return STORAGE_RE.search(text) or sig_rx.search(text)

    for page in pages:
        for line, typ, src, content in page.scripts:
            if "json" in typ.lower():
                continue
            if src is not None and re.split(r"[?#]", src.strip())[0] != "/assets/js/main.js":
                yield page.path, line, CONSENT_MESSAGE
            elif src is None and uses_tracking(content):
                yield page.path, line, CONSENT_MESSAGE
    for path in site.text_files(".js"):
        if site.is_admin(path):
            continue
        text = site.read(path)
        m = STORAGE_RE.search(text) or sig_rx.search(text)
        if m:
            yield path, line_of(text, m.start()), CONSENT_MESSAGE


def _phrase_re(phrase):
    parts = []
    for ch in phrase:
        if ch == "'":
            parts.append(r"(?:'|’|&rsquo;|&#8217;|&#39;)")
        elif ch == " ":
            parts.append(r"\s+")
        else:
            parts.append(re.escape(ch))
    return re.compile("".join(parts), re.I)


def check_claims(site):
    patterns = [(p, _phrase_re(p)) for p in BANNED_PHRASES]
    for path in site.text_files():
        if site.is_admin(path):  # the owner's checklist quotes the old claims in prompt text
            continue
        text = site.read(path)
        for phrase, rx in patterns:
            for m in rx.finditer(text):
                yield path, line_of(text, m.start()), \
                    "unsupported claim %r (see docs/claims-register.md)" % phrase


def _section_text(html_text, section_id):
    """Plain text of the <h2 id=section_id> section: from that heading to the next <h2>."""
    m = re.search(r'<h2\b[^>]*\bid="%s"[^>]*>(.*?)(?=<h2\b|</article>|$)' % re.escape(section_id), html_text, re.S)
    if not m:
        return None, 1
    text = unescape(re.sub(r"<[^>]+>", " ", m.group(1)))
    return re.sub(r"\s+", " ", text), line_of(html_text, m.start())


# Rule: every .price-amount string on /solutions/ must appear, character for character and as a whole
# amount, in the text of /terms/#payment. (A link from /terms/#payment to /solutions/ is not enough on its own.) The
# "Completion guarantee: ..." sentence on /solutions/ must also appear word for word in
# /terms/#completion-guarantee.
def check_terms_consistency(site):
    solutions = os.path.join(site.public, "solutions", "index.html")
    terms = os.path.join(site.public, "terms", "index.html")
    for path in (solutions, terms):
        if not os.path.isfile(path):
            yield path, 1, "file is missing"
            return
    sol, ter = site.read(solutions), site.read(terms)
    payment, pay_line = _section_text(ter, "payment")
    guarantee, g_line = _section_text(ter, "completion-guarantee")
    if payment is None:
        yield terms, 1, 'no <h2 id="payment"> section'
    if guarantee is None:
        yield terms, 1, 'no <h2 id="completion-guarantee"> section'
    if payment is None or guarantee is None:
        return
    amounts = re.finditer(r'<span\b[^>]*\bclass="(?:[^"]*\s)?price-amount(?:\s[^"]*)?"[^>]*>(.*?)</span>', sol, re.S)
    for m in amounts:
        amount = re.sub(r"\s+", " ", unescape(m.group(1))).strip()
        # Whole amount only: "$50" must not match inside "$250" or "$50/month"
        if not re.search(r"(?<![\w$])%s(?![\d/.,]\d|/)" % re.escape(amount), payment):
            yield terms, pay_line, "price %r from /solutions/ (line %d) is not in /terms/#payment" % (
                amount, line_of(sol, m.start()))
    sol_text = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", sol)))
    m = re.search(r"Completion guarantee:[^.]*\.", sol_text)
    if not m:
        yield solutions, 1, 'no "Completion guarantee: ..." sentence'
    elif m.group(0) not in guarantee:
        yield terms, g_line, "completion guarantee on /solutions/ (%r) is not word for word in /terms/#completion-guarantee" % m.group(0)


def check_form_notice(site):
    for page in site.pages:
        text = site.read(page.path)
        for m in re.finditer(r"(?is)<form\b.*?</form>", text):
            if not re.search(r"""(?i)<a\b[^>]*\bhref=["']/privacy/(#[^"']*)?["']""", m.group(0)):
                yield page.path, line_of(text, m.start()), "form needs a link to /privacy/ (privacy notice)"
        for m in re.finditer(r"(?i)<input\b[^>]*>", text):
            tag = m.group(0)
            if re.search(r"""\btype=["']?checkbox""", tag, re.I) and re.search(r"\schecked\b", tag, re.I):
                yield page.path, line_of(text, m.start()), "checkbox must not be pre-ticked (remove checked)"


def check_no_age_fields(site):
    pattern = re.compile(r"(?i)dob|birth|birthday|\bage\b")
    for page in site.pages:
        text = site.read(page.path)
        for m in re.finditer(r"(?is)<(?:input|select|textarea)\b[^>]*>", text):
            for attr in re.finditer(r"""(?i)\b(?:name|id)=["']?([^"'\s>]+)""", m.group(0)):
                if pattern.search(attr.group(1)):
                    yield page.path, line_of(text, m.start()), "no age or birth-date fields (found %r)" % attr.group(1)


def check_data_request(site):
    """/privacy/ must have #your-rights and a mailto link whose subject contains "request"."""
    text = site.read(os.path.join(site.public, "privacy", "index.html"))
    if 'id="your-rights"' not in text:
        yield "privacy/index.html", 1, 'missing id="your-rights"'
    if not re.search(r"""(?i)<a\b[^>]*\bhref=["']mailto:[^"'?]+\?[^"']*subject=[^"'&]*request""", text):
        yield "privacy/index.html", 1, 'needs a mailto link whose subject contains "request"'


def check_svg_alt(site):
    """SVGs must either be aria-hidden="true" focusable="false" (decorative), or have role="img"
    with aria-label or <title> (meaningful)."""
    for page in site.pages:
        text = site.read(page.path)
        # Find all <svg> tags
        for m in re.finditer(r'<svg\b([^>]*)>', text):
            attrs_str = m.group(1)
            line = line_of(text, m.start())

            is_hidden = 'aria-hidden="true"' in attrs_str
            is_role_img = 'role="img"' in attrs_str
            has_focusable_false = 'focusable="false"' in attrs_str
            has_aria_label = 'aria-label=' in attrs_str

            # Check for <title> inside the SVG (look ahead until closing tag)
            close_match = re.search(r'</svg>', text[m.end():])
            has_title = False
            if close_match:
                svg_content = text[m.end():m.end() + close_match.start()]
                has_title = '<title' in svg_content

            # Rule: if aria-hidden, must have focusable="false"
            if is_hidden and not has_focusable_false:
                yield page.path, line, '<svg> with aria-hidden="true" must also have focusable="false"'

            # Rule: if role="img", must have aria-label or <title>
            if is_role_img and not has_aria_label and not has_title:
                yield page.path, line, '<svg role="img"> must have aria-label or <title>'

            # Rule: must be either decorative (aria-hidden) or meaningful (role="img")
            if not is_hidden and not is_role_img:
                yield page.path, line, '<svg> must either have aria-hidden="true" focusable="false" (decorative) or role="img" with aria-label/<title> (meaningful)'


def check_og_image_alt(site):
    """Every page must have og:image:alt and twitter:image:alt."""
    for page in site.pages:
        if site.is_admin(page.path):
            continue
        text = site.read(page.path)

        if 'property="og:image:alt"' not in text and 'property="og:image"' in text:
            yield page.path, 1, 'has og:image but missing og:image:alt'

        if 'property="og:image"' in text and 'name="twitter:image:alt"' not in text:
            yield page.path, 1, 'has og:image but missing twitter:image:alt'


def check_asset_inventory(site):
    doc = os.path.join(os.path.dirname(os.path.abspath(site.public)), "docs", "asset-licenses.md")
    if not os.path.exists(doc):
        yield "docs/asset-licenses.md", 1, "missing"
        return
    with open(doc, encoding="utf-8") as f:
        text = f.read()
    files = []
    for sub in ("assets/img", "assets/fonts"):
        base = os.path.join(site.public, sub)
        if os.path.isdir(base):
            files += [os.path.join(sub, n) for n in sorted(os.listdir(base))]
    for n in ("favicon.ico", "apple-touch-icon.png"):
        if os.path.exists(os.path.join(site.public, n)):
            files.append(n)
    for rel in files:
        if rel.replace(os.sep, "/") not in text:
            yield rel, 1, "not named in docs/asset-licenses.md (add a row before adding the asset)"


def check_link_text(site):
    """Check link and button text for clarity and accessibility. Fail when:
    - visible text is one of the banned generic phrases (case-insensitive)
    - <a> has no accessible name (links with only images inside are OK if img has alt)
    """
    banned_phrases = {"click here", "here", "learn more", "read more", "more", "submit", "go"}

    for page in site.pages:
        text = site.read(page.path)

        # Find all links with context
        for m in re.finditer(r'<a\b([^>]*)>(.*?)</a>', text, re.S | re.I):
            attrs_str = m.group(1)
            inner_html = m.group(2)
            link_line = line_of(text, m.start())

            # Extract aria-label
            aria_label_match = re.search(r'aria-label=["\']([^"\']*)["\']', attrs_str)
            aria_label = aria_label_match.group(1) if aria_label_match else ""

            # Extract visible text (remove tags and visually-hidden content)
            # Remove visually-hidden spans first
            visible_html = re.sub(r'<span[^>]*class="[^"]*visually-hidden[^"]*"[^>]*>.*?</span>', '', inner_html, flags=re.S | re.I)
            # Extract text by removing remaining tags
            visible_text = re.sub(r'<[^>]+>', '', visible_html)
            visible_text = re.sub(r'\s+', ' ', unescape(visible_text)).strip()

            # Check if there's an image inside
            has_img = '<img' in inner_html

            # Determine accessible name
            accessible_name = aria_label or visible_text

            # If no accessible name and has image, skip (img-alt check handles this)
            if not accessible_name and has_img:
                continue

            # Check if there's no accessible name
            if not accessible_name:
                yield page.path, link_line, "<a> has no visible text or aria-label"
                continue

            # Check if visible text is banned
            if visible_text and visible_text.lower() in banned_phrases:
                yield page.path, link_line, \
                    "link has vague text %r; use a label that names the destination or action" % visible_text


def check_markdown_mirrors(site):
    """Every page links to its plain-text mirror, and the mirrors, llms.txt and their netlify.toml
    block match what tools/build_markdown.py generates (/accessibility/ promises the mirrors)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.dont_write_bytecode = True  # no tools/__pycache__ in the repo
    import build_markdown
    if os.path.abspath(site.public) != str(build_markdown.PUBLIC):
        return
    for page in site.pages:
        if site.is_admin(page.path):
            continue
        want = "/" + build_markdown.mirror_path(build_markdown.Path(os.path.abspath(page.path))) \
            .relative_to(build_markdown.PUBLIC).as_posix()
        if not any(t.name == "link" and t.attrs.get("rel") == "alternate" and t.attrs.get("type") == "text/markdown"
                   and t.attrs.get("href") == want for t in page.tags):
            yield page.path, 1, 'needs <link rel="alternate" type="text/markdown" href="%s">' % want
    for path, text in build_markdown.outputs().items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            yield str(path), 1, "%s; run python3 tools/build_markdown.py" % ("missing" if current is None else "out of date")


def netlify_redirects(text):
    """[[redirects]] rules in netlify.toml as {from: (to, status, line)}."""
    rules = {}
    for m in re.finditer(r"^\[\[redirects\]\]\n((?:[ \t]+\w+[ \t]*=.*\n?)+)", text, re.M):
        values = dict(re.findall(r'^[ \t]+(\w+)[ \t]*=[ \t]*"?([^"\n]*)"?[ \t]*$', m.group(1), re.M))
        if "from" in values:
            rules[values["from"]] = (values.get("to"), values.get("status"), line_of(text, m.start()))
    return rules


def served_files(public, path):
    """Files in public/ that Netlify would serve at path, which stops a redirect rule for it from applying."""
    base = os.path.join(public, path.strip("/"))
    candidates = [base]
    if not os.path.splitext(path)[1]:
        candidates += [base + ".html", os.path.join(base, "index.html")]
    return [c for c in candidates if os.path.isfile(c)]


def check_legacy_redirects(site):
    text = site.read(site.netlify)
    rules = netlify_redirects(text)
    for old, new in LEGACY_REDIRECTS.items():
        to, status, line = rules.get(old, (None, None, 1))
        if to is None:
            yield site.netlify, 1, "no redirect rule for old URL %s (want 301 to %s)" % (old, new)
        elif to != new or status != "301":
            yield site.netlify, line, "redirect for %s goes to %s with status %s, want %s with 301" % (old, to, status, new)
        for path in served_files(site.public, old):
            yield path, 1, "shadows the redirect for old URL %s; remove the file or the rule" % old
        target = os.path.join(site.public, new.lstrip("/"))
        if new.endswith("/"):
            target = os.path.join(target, "index.html")
        if not os.path.isfile(target):
            yield site.netlify, line, "redirect target %s for %s does not exist in public/" % (new, old)
    sw = os.path.join(site.public, "sw.js")
    if not os.path.isfile(sw) or "unregister()" not in site.read(sw):
        yield sw, 1, "missing or no longer unregisters: browsers keep the old site's service worker without it"


CHECKS = [
    ("legacy-redirects", check_legacy_redirects),
    ("img-alt", check_img_alt),
    ("svg-alt", check_svg_alt),
    ("og-image-alt", check_og_image_alt),
    ("no-external-resources", check_no_external_resources),
    ("no-client-storage", check_no_client_storage),
    ("business-details", check_business_details),
    ("no-age-fields", check_no_age_fields),
    ("no-trackers", check_no_trackers),
    ("consent-required", check_consent_required),
    ("claims", check_claims),
    ("csp-unchanged", check_csp_unchanged),
    ("no-review-schema", check_no_review_schema),
    ("testimonial-source", check_testimonial_source),
    ("no-placeholders", check_no_placeholders),
    ("third-party-allowlist", check_third_party_allowlist),
    ("internal-links", check_internal_links),
    ("new-tab-links", check_new_tab_links),
    ("shared-chrome", check_shared_chrome),
    ("required-footer-links", check_required_footer_links),
    ("terms-consistency", check_terms_consistency),
    ("form-notice", check_form_notice),
    ("data-request", check_data_request),
    ("asset-inventory", check_asset_inventory),
    ("link-text", check_link_text),
    ("markdown-mirrors", check_markdown_mirrors),
]


def main(argv):
    public, netlify = "public", "netlify.toml"
    args = list(argv)
    while args:
        flag = args.pop(0)
        if flag == "--public" and args:
            public = args.pop(0)
        elif flag == "--netlify" and args:
            netlify = args.pop(0)
        else:
            print("usage: check_site.py [--public DIR] [--netlify FILE]", file=sys.stderr)
            return 2
    site = Site(public, netlify)
    problems = []
    for name, fn in CHECKS:
        for path, line, message in fn(site):
            problems.append((path, line, name, message))
    for path, line, name, message in sorted(problems):
        print("%s:%d: [%s] %s" % (path, line, name, message))
    if problems:
        print("%d problem(s) found" % len(problems), file=sys.stderr)
        return 1
    print("OK: %d checks passed on %d pages" % (len(CHECKS), len(site.pages)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
