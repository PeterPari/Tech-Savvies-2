# Prompt 23: Check tracking

````text
<context>
The Privacy Policy and Cookie Policy will say whether Tech-Savvies tracks visitors, and a false statement there is a deceptive practice under FTC Act §5 and NY GBL §349.

A Playwright probe on 2026-09-28 (all 6 pages, 375px and 1280px) measured 0 cookies, 0 localStorage/sessionStorage keys, and requests only to the site's own origin. The code contains no analytics, pixels or tag managers.

Tracking can still exist outside the code:
- Netlify Analytics: server-side, switched on in the dashboard;
- Netlify split testing: sets an nf_ab cookie;
- Netlify snippet injection;
- email read receipts or open-tracking pixels in the owner's mail client.
</context>

<inputs>
docs/business-facts.md, docs/compliance-log.md, docs/third-parties.md, public/
</inputs>

<deliverables>
1. docs/tracking-audit.md, containing:
   - the method and date;
   - a results table with one row per visitor-facing page × viewport (public/admin/ is excluded: its localStorage holds only the owner's checklist; note that in one line), and columns for request origins, cookies, localStorage, sessionStorage, IndexedDB and service workers, including a contact-form submit (a local 501 response is expected);
   - production results, or "production not reachable";
   - the owner's answers about Netlify Analytics, split testing, snippet injection, email open-tracking, and plans for analytics in the next 6 months;
   - a one-sentence conclusion the Privacy Policy can quote.
2. A check named no-trackers in tools/check_site.py, failing on any entry in a TRACKER_SIGNATURES constant found in public/ HTML or JS. The constant covers at least: gtag, googletagmanager, google-analytics, analytics.js, fbq, connect.facebook, doubleclick, hotjar, clarity.ms, segment, mixpanel, plausible, umami, cloudflareinsights, tiktok, snap.licdn, sendBeacon, <noscript><img. Add a comment pointing to fix-prompts/05-cookie-consent.md.
3. The owner's answers added to docs/business-facts.md, and item 23 updated in docs/compliance-log.md.
4. One commit, "Fix #23: audit tracking and block tracker scripts", pushed.
5. A final message of at most 8 bullets.
</deliverables>

<examples>
<example index="1">Conclusion when everything is clean: "Tech-Savvies doesn't use analytics, advertising or tracking tools, and this website doesn't set cookies."</example>
<example index="2">Conclusion with Netlify Analytics on: "Tech-Savvies doesn't use advertising or tracking tools. Our host counts page visits from its server logs, without cookies."</example>
<example index="3">Conclusion with email open-tracking on: "This website doesn't set cookies or track you. Emails we send may include a read receipt that tells us when an email is opened."</example>
</examples>

<constraints>
- Leave analytics and tracking settings as they are. Record owner-side tracking (Netlify Analytics, email open-tracking) as an owner action, not something to change in this prompt.
- Ask the owner only the questions docs/business-facts.md doesn't already answer, in one AskUserQuestion call.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- A temporary copy of public/ containing "gtag(" makes no-trackers fail.
</acceptance_criteria>

<if_uncertain>
If the owner doesn't know whether a dashboard setting is on, record "unknown: owner to check" and word the conclusion so it stays true either way.
</if_uncertain>

<task>
Establish with evidence whether Tech-Savvies tracks website visitors or email recipients, record the result in docs/tracking-audit.md, and make the checker reject tracker code.
</task>
````

## Assumptions
- Prompt 08 has run.
- The owner can check their Netlify dashboard and email settings.

## Parameters
- Model: sonnet.
- Reasoning effort: medium.

## What to test
- The results table covers all 6 pages at both widths, plus the form submit.
- Run with the owner saying Netlify Analytics is "on". The conclusion should change to the example 2 pattern.
- A seeded tracker signature makes the checker fail.
