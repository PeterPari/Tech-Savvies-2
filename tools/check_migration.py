#!/usr/bin/env python3
# Checks a deployed copy of the site against migration-plan.md: every old-site URL redirects (301) to its
# new page, every sitemap page is indexable, kept URLs still answer, /sw.js is served and missing pages 404.
# Standard library only. Run from the repo root:
#   python3 tools/check_migration.py https://tech-savvies-2.netlify.app     before the domain moves
#   python3 tools/check_migration.py https://tech-savvies.com --production  after it moves
# --production also checks that http:// and www redirect to https://tech-savvies.com/, that the
# tech-savvies-2.netlify.app address redirects to the domain, and that the email (iCloud) and Search
# Console DNS records survived the move. Exits 1 and prints each problem if anything fails.
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True  # no tools/__pycache__ in the repo
from check_site import LEGACY_REDIRECTS, SITE_ORIGIN  # noqa: E402

NETLIFY_APP = "https://tech-savvies-2.netlify.app"

# Old-site URLs that keep working without a rule: the new site has a file at the same path.
KEPT_URLS = ["/", "/index.md", "/contact.md", "/llms.txt", "/site.webmanifest", "/robots.txt", "/sitemap.xml"]

# DNS records in the tech-savvies.com zone that the move must not touch (public DNS, 2026-09-30).
# (name, type, text the answer must contain). Update this list if the email provider changes.
EXPECTED_DNS = [
    ("tech-savvies.com", "MX", "mx01.mail.icloud.com"),
    ("tech-savvies.com", "MX", "mx02.mail.icloud.com"),
    ("tech-savvies.com", "TXT", "v=spf1 include:icloud.com"),
    ("tech-savvies.com", "TXT", "apple-domain="),
    ("tech-savvies.com", "TXT", "google-site-verification="),
    ("sig1._domainkey.tech-savvies.com", "CNAME", "icloudmailadmin.com"),
]


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


OPENER = urllib.request.build_opener(NoRedirect)


def fetch(url):
    """(status, headers, body) for one request, without following redirects."""
    req = urllib.request.Request(url, headers={"User-Agent": "tech-savvies-migration-check"})
    try:
        with OPENER.open(req, timeout=30) as r:
            return r.status, r.headers, r.read(2_000_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.headers, e.read(2_000_000).decode("utf-8", "replace")


class Head(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.canonical = None
        self.robots = ""
        self.feed(html)

    def handle_starttag(self, name, attrs):
        a = dict((k, v or "") for k, v in attrs)
        if name == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        if name == "meta" and a.get("name", "").lower() == "robots":
            self.robots += a.get("content", "").lower()


class Checker:
    def __init__(self):
        self.passed = 0
        self.problems = []

    def expect(self, ok, url, message):
        if ok:
            self.passed += 1
        else:
            self.problems.append("%s: %s" % (url, message))
        return ok

    def redirect(self, url, want):
        """url answers 301 with a Location that resolves to want."""
        try:
            status, headers, _ = fetch(url)
        except OSError as e:
            return self.expect(False, url, "request failed: %s" % e)
        location = headers.get("Location")
        location = urllib.parse.urljoin(url, location) if location else None
        return self.expect(status == 301 and location == want, url, "got %s%s, want 301 to %s"
                           % (status, " to " + location if location else "", want))

    def ok(self, url, noindex_ok=False):
        """url answers 200 directly; returns the body."""
        try:
            status, headers, body = fetch(url)
        except OSError as e:
            self.expect(False, url, "request failed: %s" % e)
            return None
        where = headers.get("Location")
        if not self.expect(status == 200, url, "got %s%s, want 200" % (status, " to " + where if where else "")):
            return None
        if not noindex_ok:
            self.expect("noindex" not in (headers.get("X-Robots-Tag") or "").lower(), url,
                        "X-Robots-Tag noindex on an indexable URL")
        return body


def check_site(c, base):
    for old, new in LEGACY_REDIRECTS.items():
        if c.redirect(base + old, base + new):
            c.ok(base + new)
        if not os.path.splitext(old)[1]:  # Netlify matches /about and /about/ with the same rule
            c.redirect(base + old + "/", base + new)

    for path in KEPT_URLS:
        c.ok(base + path)
    if c.redirect(base + "/contact", base + "/contact/"):
        c.ok(base + "/contact/")

    status, _, sitemap = fetch(base + "/sitemap.xml")
    locs = [loc.split("</loc>")[0].strip() for loc in sitemap.split("<loc>")[1:]]
    c.expect(status == 200 and locs, base + "/sitemap.xml", "no sitemap URLs found")
    for loc in locs:
        if not c.expect(loc.startswith(SITE_ORIGIN + "/"), base + "/sitemap.xml", "%s is not on %s" % (loc, SITE_ORIGIN)):
            continue
        url = base + loc[len(SITE_ORIGIN):]
        body = c.ok(url)
        if body is None:
            continue
        head = Head(body)
        c.expect(head.canonical == loc, url, "canonical is %s, want %s" % (head.canonical, loc))
        c.expect("noindex" not in head.robots, url, "meta robots is %r on a sitemap page" % head.robots)

    status, headers, body = fetch(base + "/sw.js")
    c.expect(status == 200 and "javascript" in (headers.get("Content-Type") or "") and "unregister()" in body,
             base + "/sw.js", "got %s %s, want 200 JavaScript that unregisters the old service worker"
             % (status, headers.get("Content-Type")))

    missing = base + "/migration-check-missing-page"
    status, _, body = fetch(missing)
    c.expect(status == 404 and "noindex" in Head(body).robots, missing, "got %s, want the 404 page with status 404" % status)

    robots = c.ok(base + "/robots.txt") or ""
    lines = [line.strip().lower() for line in robots.splitlines()]
    c.expect("disallow: /" not in lines, base + "/robots.txt", "blocks the whole site")
    c.expect("sitemap: %s/sitemap.xml" % SITE_ORIGIN in lines, base + "/robots.txt", "no Sitemap line")


def check_production(c):
    home = SITE_ORIGIN + "/"
    for url in ["http://tech-savvies.com/", "https://www.tech-savvies.com/"]:
        c.redirect(url, home)
    try:  # http://www may go through https://www first; it must end at the domain within 2 hops
        url, hops = "http://www.tech-savvies.com/", 0
        while hops < 2:
            status, headers, _ = fetch(url)
            if status not in (301, 308):
                break
            url, hops = urllib.parse.urljoin(url, headers.get("Location")), hops + 1
        c.expect(url == home, "http://www.tech-savvies.com/", "ends at %s, want %s" % (url, home))
    except OSError as e:
        c.expect(False, "http://www.tech-savvies.com/", "request failed: %s" % e)
    c.redirect(NETLIFY_APP + "/", home)
    c.redirect(NETLIFY_APP + "/solutions/", SITE_ORIGIN + "/solutions/")

    for name, rtype, want in EXPECTED_DNS:
        url = "https://dns.google/resolve?" + urllib.parse.urlencode({"name": name, "type": rtype})
        try:
            answers = [a.get("data", "") for a in json.loads(fetch(url)[2]).get("Answer", [])]
        except (OSError, ValueError) as e:
            c.expect(False, name, "DNS lookup failed: %s" % e)
            continue
        c.expect(any(want in a for a in answers), "%s %s" % (name, rtype),
                 "no record containing %r (found %s); restore it from the Phase 0 backup" % (want, answers or "none"))


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    flags = set(argv) - set(args)
    if len(args) != 1 or not args[0].startswith(("http://", "https://")) or flags - {"--production"}:
        print("usage: check_migration.py BASE_URL [--production]", file=sys.stderr)
        return 2
    base = args[0].rstrip("/")
    c = Checker()
    check_site(c, base)
    if "--production" in flags:
        check_production(c)
    for problem in c.problems:
        print(problem)
    if c.problems:
        print("%d problem(s) found, %d checks passed on %s" % (len(c.problems), c.passed, base), file=sys.stderr)
        return 1
    print("OK: %d checks passed on %s" % (c.passed, base))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
