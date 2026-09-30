# Tracking audit

Audit date: 2026-09-29. Owner answers dated 2026-09-29. Related: compliance log item 23,
[`business-facts.md`](business-facts.md), [`third-parties.md`](third-parties.md).

## Conclusion (for the Privacy Policy to quote)

> Tech-Savvies doesn’t use advertising or tracking tools, and this website doesn’t set cookies. Our host counts page visits from its server logs, without cookies.

This is true of the code in this repository. It is true of the public site only after `tech-savvies.com`
serves this build (see "Production" below: the old build there still loads Microsoft Clarity). Do not
publish the Privacy Policy sentence until that switch is done and re-checked.

## Method

1. Served `public/` locally (`python3 -m http.server 8080 --directory public`) and drove it with Playwright
   and Chromium.
2. For each visitor-facing page and each viewport (375 × 812 and 1280 × 800), used a fresh browser context
   with service workers allowed, loaded the page until the network was idle, then recorded: every request
   origin, `context.cookies()`, `document.cookie`, `localStorage` and `sessionStorage` key counts,
   `indexedDB.databases()` and service worker registrations.
3. On `/contact/`, filled in and submitted the form. The local server has no Netlify Forms, so the POST
   returns 501, as expected.
4. Static scan: `python3 tools/check_site.py` (new `no-trackers` check) looks for tracker signatures in
   `public/` HTML and JS.
5. Production: fetched the pages with curl (headers, `Set-Cookie`, HTML) and compared the scripts and
   external origins they reference. See "Production".

`public/admin/` is excluded: it is the owner’s internal checklist, and its `localStorage` holds only the
owner’s own checklist state.

## Results: this repository (local, 2026-09-29)

| Page | Viewport | Request origins | Cookies | localStorage keys | sessionStorage keys | IndexedDB databases | Service workers | Form submit |
|------|----------|-----------------|---------|-------------------|---------------------|---------------------|-----------------|-------------|
| `/` (Home) | 375 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | n/a |
| `/` (Home) | 1280 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | n/a |
| `/solutions/` (Solutions) | 375 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | n/a |
| `/solutions/` (Solutions) | 1280 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | n/a |
| `/our-story/` (Our story) | 375 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | n/a |
| `/our-story/` (Our story) | 1280 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | n/a |
| `/contact/` (Contact) | 375 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | Form filled and submitted: local POST returned 501 (expected); still 0 cookies and 0 storage after it |
| `/contact/` (Contact) | 1280 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | Form filled and submitted: local POST returned 501 (expected); still 0 cookies and 0 storage after it |
| `/contact/thanks/` (Contact thanks) | 375 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | n/a |
| `/contact/thanks/` (Contact thanks) | 1280 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | n/a |
| `/no-such-page/` (404 page) | 375 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | n/a |
| `/no-such-page/` (404 page) | 1280 px | `http://localhost:8080` only | 0 | 0 | 0 | 0 | 0 | n/a |

All 12 page × viewport runs: only the site’s own origin, no cookies, no storage, no service worker.

## Production

Chromium in this sandbox cannot trust the sandbox’s TLS-intercepting proxy, and disabling certificate
checks is not acceptable, so no browser run against production was possible. The checks below are
static (curl: response headers and HTML). They cannot show what scripts do at runtime, so treat them as
partial. The contact form was **not** submitted on production, to avoid creating a real submission and
email.

| Host | Pages fetched | Set-Cookie headers | Scripts and external origins referenced |
|------|---------------|--------------------|------------------------------------------|
| `https://tech-savvies-2.netlify.app` (new build) | `/`, `/solutions/`, `/our-story/`, `/contact/`, `/contact/thanks/`, 404 URL | 0 | No third-party scripts, pixels or fonts. Only the link to `grisha.studio` and canonical/`og:` URLs on `tech-savvies.com`. CSP matches `netlify.toml` |
| `https://tech-savvies.com` (old build) | `/` (the other new paths return its 404 page) | 0 | **Loads Microsoft Clarity** (`https://www.clarity.ms/tag/vwz3thl727`, inline script on `/` and on its 404 page), Google Fonts, and its CSP allows `clarity.ms`, `c.bing.com` and `formsubmit.co` |

Finding: the live domain runs a session-recording/analytics tool today. The new build has none. The
statement above is not true of `tech-savvies.com` until the new build replaces the old one. Rerun this
probe (in a browser from a clean machine) after the move.

## Owner answers (2026-09-29)

| Question | Answer |
|----------|--------|
| Netlify Analytics on? | Yes, on (server-side from CDN logs, cookieless per Netlify; counts by IP) |
| Netlify split testing (`nf_ab` cookie)? | No, off |
| Netlify snippet injection? | No, none |
| Email open-tracking or read receipts? | No |
| Plans for analytics, ads or pixels in the next 6 months? | Answered "Netlify Analytics are running". Read as: no further tools planned beyond Netlify Analytics. Confirm this if it was not the intent |

## Cookie consent

Decision (2026-09-29): **no cookie consent banner.**

Evidence:

- Results table above: 0 cookies, 0 `localStorage`/`sessionStorage` keys, no IndexedDB, no service workers
  and only first-party requests on every page and viewport. This audit is newer than the last commit
  touching `public/`, so no re-measurement was needed.
- `public/assets/js/main.js` (menu, footer year, form double-submit guard) uses no cookies or storage.
- `public/sw.js` is never registered by this site. It only runs in browsers that still have the old
  site’s service worker: it deletes that worker’s caches and unregisters it, so it removes storage and
  adds none (see [`../migration-plan.md`](../migration-plan.md)).
- Netlify Analytics is server-side and cookieless per Netlify (owner answers above); it needs disclosure in
  the Privacy Policy but no consent prompt.
- A banner would ask for consent to nothing, add an obstacle for keyboard and screen-reader users on
  every first visit, and need a cookie of its own to remember the choice.

Guard: the `consent-required` check in `tools/check_site.py` fails when a page outside `public/admin/`
loads a script other than `/assets/js/main.js`, or JS uses cookies, Web Storage or a tracker signature,
and no element has `data-consent-banner`. Tested with `<script>document.cookie="x=1"</script>` in a
temporary copy of `public/`. Adding a tracker or cookie later means following
`fix-prompts/05-cookie-consent.md` (branch B) first.

Owner should re-check this decision if a cookie-based tool is ever wanted.

## Owner actions

- Netlify Analytics is left on, as instructed. The Privacy Policy must disclose it.
- Retire the old Clarity build on `tech-savvies.com` when the new site goes live, and check the Clarity
  project for stored recordings to delete.
- Re-run this audit after go-live, and before adding any tracker (the `no-trackers` check will block it;
  see `fix-prompts/05-cookie-consent.md`).
