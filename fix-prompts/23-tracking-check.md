# Prompt 23: Check tracking

Phase 1 (after 08). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md`, `docs/compliance-log.md` and
`docs/third-parties.md`.

## Goal

Prove, with evidence, whether Tech-Savvies tracks visitors or email recipients in any way.
Write the result to `docs/tracking-audit.md` and add guards so tracking can't be added without
a deliberate decision.

## Why

The Privacy Policy and Cookie Policy will state "we don't track you". That must be verifiably
true, because a false privacy claim is a deceptive practice (FTC Act §5, NY GBL §349). A code
audit found no analytics, pixels or tag managers. A 2026-09-28 Playwright probe measured 0
cookies, 0 storage keys and only same-origin requests. Tracking can still exist outside the
code, though:
- **Netlify Analytics:** server-side log analysis, switched on in the dashboard, invisible in
  the HTML.
- **Netlify split testing:** can set an `nf_ab` cookie.
- **Email open-tracking:** tracking pixels added by the owner's mail client or extensions
  (Mailtrack, HubSpot, Superhuman read receipts, etc.).

## Task

1. **Code scan.** Search `public/` for known tracker signatures, including: `gtag`,
   `googletagmanager`, `google-analytics`, `analytics.js`, `fbq`, `connect.facebook`,
   `doubleclick`, `hotjar`, `clarity.ms`, `segment`, `mixpanel`, `plausible`, `umami`,
   `cloudflareinsights`, `tiktok`, `linkedin insight`, `sendBeacon`, 1×1 images, `data:image/gif`
   beacons, and `<noscript><img`.

2. **Runtime scan.** Use Playwright (script in your scratchpad) on every page at 375px and
   1280px. Submit the contact form locally: the Python server will return 501 on POST, which is
   fine, because you're only watching network calls. Record requests, cookies (`context.cookies()`),
   localStorage, sessionStorage, IndexedDB databases, and service worker registrations.

3. **Production scan.** If `https://tech-savvies.com` is reachable, fetch each page with `curl -sI`
   and in Playwright. Look for `Set-Cookie`, for scripts Netlify injects (snippet injection,
   analytics), and for any `nf_ab` cookie. If it isn't reachable, say so.

4. **Owner questions** (use `AskUserQuestion`, and skip any already answered in
   `docs/business-facts.md`):
   - Is Netlify Analytics enabled for this site?
   - Is Netlify split testing or snippet injection enabled?
   - Do you use read receipts or open-tracking in your email?
   - Do you plan to add analytics in the next 6 months? If yes, send them to Prompt 05's
     conditional section.

5. **Write `docs/tracking-audit.md`**: the date, method, results table (page × viewport ×
   requests/cookies/storage), production results, owner answers, and a conclusion in one sentence
   that the Privacy Policy can quote. Suggested wording if everything is clean: "Tech-Savvies
   doesn't use analytics, advertising or tracking tools, and doesn't set cookies." If Netlify
   Analytics is on, the conclusion must say so and describe it: server-side, no cookies, based on
   request logs.

6. **Extend `tools/check_site.py`.** Add a `no-trackers` check that fails on any of the
   signatures above in HTML/JS. Keep the list in one `TRACKER_SIGNATURES` constant with a comment
   pointing to Prompt 05 for the consent requirements before any tracker is added.

7. Update item 23 in `docs/compliance-log.md`, and add the answers to `docs/business-facts.md`.

## Constraints

- Don't add or remove any analytics in this prompt.
- If email open-tracking is on, don't change it yourself. Note it as an owner action, and note
  that the Privacy Policy must disclose it or it must be turned off.

## Verify

- `python3 tools/check_site.py` passes; inserting `gtag(` into a temp copy makes it fail.

## Commit

`Fix #23: audit tracking and block tracker scripts in site checks`. Push to the current branch.
