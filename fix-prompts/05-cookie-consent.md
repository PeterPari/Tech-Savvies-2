# Prompt 05: Cookie consent (decide, guard, conditional banner)

````text
<context>
Consent laws (EU ePrivacy/GDPR, UK PECR, US state opt-out laws) are triggered by non-essential cookies, device storage or tracking. docs/tracking-audit.md records 0 cookies, 0 browser storage and no third-party requests.

A banner on this site would ask for consent to nothing, which misleads. It would also add a keyboard and screen-reader obstacle to every first visit, and it would need a cookie of its own to remember the choice. The planned outcome is therefore: no banner, a recorded decision, and a guard. Branch B below applies only when a non-essential cookie or tracker exists, or the owner explicitly asks for analytics.
</context>

<inputs>
docs/tracking-audit.md, docs/third-parties.md, docs/business-facts.md, docs/compliance-log.md, public/assets/js/main.js
</inputs>

<branch_a>
Applies when there are no non-essential cookies, storage or trackers.
1. A "Cookie consent" section in docs/tracking-audit.md recording the decision, the evidence and the date.
2. A check named consent-required in tools/check_site.py that fails when both are true:
   - any page outside public/admin/ has a <script src> other than /assets/js/main.js, or inline or linked JS that uses cookies, Web Storage or a TRACKER_SIGNATURES entry;
   - no element has data-consent-banner.
   The failure message is "Non-essential storage or tracking added without consent. See fix-prompts/05-cookie-consent.md". The check must pass on the current main.js.
3. One line in the README "Checks" section: "Adding analytics or any cookie? Read fix-prompts/05-cookie-consent.md first."
</branch_a>

<branch_b>
Applies when a non-essential cookie or tracker exists, or the owner explicitly asks for analytics. First offer a cookieless server-side option, such as Netlify Analytics, which needs disclosure but no banner. Build a banner only if the owner still chooses a cookie-based tool. The banner must meet all of the following:
- The tracker loads only after "Accept analytics". Nothing is preloaded, and the tracker origin is added to the CSP and EXPECTED_CSP.
- "Accept analytics" and "Reject analytics" are the same size and style, in the same row. A "Cookie settings" link goes to /cookies/. No pre-ticked options, and no "by continuing you agree".
- navigator.globalPrivacyControl === true counts as Reject, and the banner isn't shown.
- The choice is stored in one first-party cookie, ts_consent (6 months, SameSite=Lax, Secure), listed on /cookies/.
- A "Cookie settings" link in every footer reopens the choice.
- The banner is a non-modal <section role="region" aria-label="Cookie choices" data-consent-banner> at the end of <body>. It doesn't trap focus. While it's shown, body gets bottom padding so it never covers focused content. It uses existing .btn styles and meets AA contrast.
- With JavaScript off, no tracker loads.
- /cookies/, /privacy/, docs/third-parties.md and docs/tracking-audit.md are updated in the same commit.
</branch_b>

<deliverables>
1. The branch A or branch B output.
2. Item 5 updated in docs/compliance-log.md, naming the branch taken and the evidence.
3. One commit, "Fix #05: record cookie consent decision and guard against unconsented tracking" (branch A) or "Fix #05: add analytics consent banner" (branch B), pushed.
4. A final message of at most 6 bullets.
</deliverables>

<constraints>
- In branch A, leave all page markup unchanged.
- If docs/tracking-audit.md is older than the latest commit touching public/, re-measure cookies and storage before deciding, and update the audit.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- Branch A: a temporary copy of public/ with <script>document.cookie="x=1"</script> makes consent-required fail.
- Branch B: with JavaScript on and before any choice, the page makes no tracker request; with GPC on, no tracker request ever.
</acceptance_criteria>

<task>
Decide from the tracking evidence whether the site needs cookie consent, and implement the matching branch.
</task>
````

## Assumptions
- Prompts 08 and 23 have run.
- The expected result is branch A.

## Parameters
- Model: sonnet.
- Reasoning effort: medium.

## What to test
- Branch A on the current site: no markup changes, and the seeded cookie write fails the checker.
- Tell the session "the owner wants Google Analytics" and confirm it offers the cookieless option before building branch B.
