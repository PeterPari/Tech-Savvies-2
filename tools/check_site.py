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
REQUIRED_FOOTER_LINKS = ["/terms/", "/refunds/", "/privacy/", "/cookies/"]

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
    for page in site.pages:
        for tag in page.tags:
            if tag.name == "img" and "alt" not in tag.attrs:
                yield page.path, tag.line, "<img> has no alt attribute"
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


CHECKS = [
    ("img-alt", check_img_alt),
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
