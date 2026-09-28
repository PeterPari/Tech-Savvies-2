# Prompt 05: Cookie consent (verify, guard, and conditional banner)

Phase 1 (after 23). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 (especially Decision 1) and §4, then `docs/business-facts.md`,
`docs/compliance-log.md`, `docs/tracking-audit.md` and `docs/third-parties.md`.

## Goal

Decide, based on evidence, whether the site needs a cookie consent banner. Today the expected
answer is **no**. Record that decision, make it enforceable, and leave an exact spec for the day
the answer changes.

## Why

Consent laws (the EU ePrivacy Directive and GDPR, UK PECR, and US state opt-out regimes) are
triggered by **non-essential** cookies, device storage or tracking. Tech-Savvies sets 0 cookies,
stores nothing in the browser, and loads nothing from other origins (measured 2026-09-28; see
`docs/tracking-audit.md`).

A banner here would:
- ask for consent to nothing, which is misleading in its own right;
- train visitors to click "Accept" without reading, which regulators criticise;
- add a keyboard and screen-reader obstacle to every first visit;
- need JavaScript and storage to remember the choice, which itself adds a cookie.

The right fix is to confirm, document, and guard. Build a banner only if a non-essential
cookie or tracker actually exists or is being added.

## Task

1. **Re-verify.** Read `docs/tracking-audit.md`. If it's older than the latest change in
   `public/`, re-run its cookie and storage probe with Playwright (script in your scratchpad).
   Also verify that Netlify's own platform sets no cookies on this site in production, if
   reachable.

2. **Branch on the result.**

   **A. No non-essential cookies, storage or trackers (expected).**
   - Don't add a banner.
   - Add a `## Cookie consent` section to `docs/tracking-audit.md` that records the decision,
     the evidence, and the date.
   - Extend `tools/check_site.py` with a `consent-required` check. If any page contains a
     `<script>` with `src`, or inline JS containing `cookie`, `Storage`, or a tracker signature,
     and the site has no `data-consent-banner` element, fail with the message: "Non-essential
     storage or tracking added without a consent mechanism. See fix-prompts/05-cookie-consent.md
     §B." Make sure this doesn't trip on `main.js` as it is today.
   - Add a line to the README "Checks" section: "Adding analytics or any cookie? Read
     `fix-prompts/05-cookie-consent.md` first."

   **B. A non-essential cookie or tracker exists, or the owner explicitly asks for analytics.**
   First recommend a cookieless, server-side option such as Netlify Analytics, which needs
   disclosure but usually no banner. Build a banner only if the owner still chooses a
   cookie-based tool. The banner must meet all of these requirements:
   - Nothing non-essential loads before consent. The tracker script is injected by JS only after
     "Accept". Nothing is preloaded, and the tracker's origin is added to the CSP.
   - The first layer shows **"Accept analytics"** and **"Reject analytics"** as equally
     prominent buttons: same size, same style, same row. There is a "Cookie settings" link to
     `/cookies/`. No pre-ticked options, no "by continuing to browse you agree".
   - A Global Privacy Control signal (`navigator.globalPrivacyControl === true`) counts as Reject
     and skips the banner.
   - The choice is stored in one first-party, strictly necessary cookie (`ts_consent`, 6 months,
     `SameSite=Lax; Secure`) and listed in the Cookie Policy.
   - A persistent "Cookie settings" link in every page footer reopens the choice. Withdrawing
     must be as easy as giving consent.
   - Accessibility: a non-modal `<section role="region" aria-label="Cookie choices"
     data-consent-banner>` at the end of `<body>`. It doesn't trap focus, doesn't cover focused
     content (WCAG 2.4.11; add bottom padding to `body` while it's shown), is reachable by
     keyboard, has visible focus, and meets AA contrast. It uses existing `.btn` styles and design
     tokens.
   - Works with the site's no-JS baseline: without JS, no tracker ever loads.
   - Update `/cookies/`, `/privacy/`, `docs/third-parties.md`, `EXPECTED_CSP`, and
     `docs/tracking-audit.md`.

3. Update item 5 in `docs/compliance-log.md` with the branch taken and the evidence.

## Constraints

- In branch A, change no page markup.
- Don't add a banner "just in case". The owner has to ask for analytics explicitly for branch B.

## Verify

- `python3 tools/check_site.py` passes. Adding `<script>document.cookie="x=1"</script>` to a temp
  copy makes `consent-required` fail.

## Commit

Branch A: `Fix #05: confirm no cookie banner is needed and guard against unconsented tracking`.
Push to the current branch.
