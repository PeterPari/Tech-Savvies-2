# Prompt 04: Cookie policy

Phase 3 (after 01). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 (Decision 1) and §4, then `docs/tracking-audit.md` (including its
"Cookie consent" section), `docs/third-parties.md`, `docs/business-facts.md` and
`docs/compliance-log.md`. `/privacy/` and the `.prose` styles must already exist (Prompt 01).

## Goal

Publish `/cookies/`, a short, honest Cookie Policy. Today it will mostly say "we don't use
cookies", and that's the point: it tells visitors and regulators clearly, with a date and an
explanation of how it was checked.

## Why

Visitors look for a cookie policy, and a missing one reads as "they're hiding something". Its
content must match reality, and the audit (`docs/tracking-audit.md`) measured 0 cookies and 0
browser storage. A generic cookie policy listing "analytics and advertising cookies" would be
false and deceptive. A dedicated page also gives Prompt 05 branch B a ready home if a consent
mechanism is ever added.

## Content

1. `h1` "Cookie Policy", `p.meta` "Last updated" with `<time>`.
2. **The short version:** "Tech-Savvies doesn't use cookies or similar technologies (like local
   storage or tracking pixels) on this website." Use the exact conclusion from
   `docs/tracking-audit.md`. If Netlify Analytics is on, add that it counts visits from server
   logs without cookies.
3. **What cookies are:** 2–3 plain sentences.
4. **How we checked:** "We tested every page on <date> in a standard browser and found no
   cookies or stored data. We re-check whenever the site changes." (This is true because of the
   `tools/check_site.py` guards; say so simply.)
5. **Other websites:** the site links to other sites (for example, the showcase link); they have
   their own cookie policies.
6. **If this changes:** "If we ever add a tool that uses cookies, we'll update this page first
   and ask for your permission before setting any cookie that isn't strictly necessary."
7. **Controlling cookies:** link to browser help pages (Chrome, Safari, Firefox, Edge). Verify
   the URLs with `WebFetch`. These are outbound links, so add their origins to
   `ALLOWED_LINK_ORIGINS` in `tools/check_site.py` and to `docs/third-parties.md` (links only,
   no data shared). If you'd rather avoid growing the allowlist, describe the setting in words
   instead of linking.
8. **Contact:** email, plus a link to `/privacy/`.

Add an empty-state table only if branch B of Prompt 05 has been taken. Otherwise, don't show a
table of zero cookies.

## Build

1. `public/privacy/index.html` is the template (header, footer, `.prose`). Give the new page a
   unique title, description, canonical `https://tech-savvies.com/cookies/`, and `og:` tags.
2. **Footer, every HTML page:** add "Cookie Policy" to the Legal column after "Privacy Policy".
   Confirm with `grep -L`.
3. **Privacy Policy `#cookies` section:** add a link, "Read our Cookie Policy".
4. Add `/cookies/` to `public/sitemap.xml`, the README pages table, and `REQUIRED_FOOTER_LINKS`.
5. Update item 4 in `docs/compliance-log.md`.

## Verify

- `python3 tools/check_site.py` passes.
- Playwright screenshot at 375px and 1280px. A keyboard tab-through shows visible focus on
  every link.

## Commit

`Fix #04: add cookie policy`. Push to the current branch.
