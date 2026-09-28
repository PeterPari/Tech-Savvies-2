# Prompt 03: Refund policy

````text
<context>
Clients pay up to a few hundred dollars upfront. The site promises a completion guarantee and sells an auto-renewing monthly plan, and neither has written refund or cancellation rules. docs/legal-compliance.md covers NY GBL §218-a (refund policy posting) and §527-a (auto-renewal cancellation). The refund rules must agree with /solutions/ and /terms/.
</context>

<inputs>
docs/business-facts.md, docs/legal-compliance.md, docs/ux-honesty-rules.md, docs/compliance-log.md, public/solutions/index.html, public/terms/index.html, public/privacy/index.html (template)
</inputs>

<deliverables>
1. public/refunds/index.html, built from the /privacy/ template:
   - title "Refund Policy | Tech-Savvies", a unique description, canonical, og tags, "Last updated <time>";
   - article.prose containing a summary table with one row per service (Website Launch, Website Rescue, Google & Social one-time, Monthly plan) and the columns Before work starts | During the project | After delivery. The table has a <caption>, th scope attributes, and the .prose scroll wrapper;
   - h2 sections #before-work-starts, #during-a-project, #after-delivery, #rush-orders, #monthly-plan, #third-party-costs;
   - #how-to-ask, with a mailto link, subject "Refund request", asking for the project name or invoice number;
   - #timing;
   - #if-we-miss-a-promise, covering how the completion guarantee and missed rush deadlines are honoured;
   - #chargebacks: at most 2 sentences asking the client to contact us first, with a response time;
   - #contact.
2. On /terms/, refund mentions link to /refunds/, with any conflicting wording removed. On /solutions/, a "Refund Policy" link next to the Terms link in the Payment block.
3. "Refund Policy" after "Terms of Service" in the footer Legal column on every HTML page.
4. /refunds/ added to the sitemap, the README, and REQUIRED_FOOTER_LINKS. The final rules recorded in docs/business-facts.md. Item 3 updated in docs/compliance-log.md and flagged for attorney review.
5. One commit, "Fix #03: add refund and cancellation policy", pushed.
6. A final message of at most 6 bullets.
</deliverables>

<constraints>
- Take the rules from docs/business-facts.md. For gaps, ask the owner in AskUserQuestion calls, with the recommended option listed first:
  - cancel before work starts: full deposit refund (recommended) / deposit non-refundable / refund minus a fixed admin amount;
  - cancel mid-project: pay for work done, refund the rest (recommended) / no refund;
  - after delivery: free bug fixes within N days, no refund (recommended) / satisfaction refund within N days;
  - rush fee: refunded if the deadline is missed (recommended) / non-refundable;
  - monthly plan: cancel any time, effective at the end of the paid month, no partial refund (recommended) / prorated refund;
  - refund method and timing: same payment method, within N business days.
- Cancelling the monthly plan uses the same channel as signing up.
- Leave out wording that discourages refund requests.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- /refunds/ renders at 320px, 375px and 1280px with no page-level horizontal scroll. The table scrolls inside its focusable wrapper.
- No refund or cancellation statement on /solutions/, /terms/ or /refunds/ contradicts another.
</acceptance_criteria>

<task>
Publish /refunds/, a refund and cancellation policy for each Tech-Savvies service that agrees with /solutions/ and /terms/.
</task>
````

## Assumptions
- Prompts 01 and 02 have run.
- The owner chooses the refund rules during the session if they aren't already in the facts file.

## Parameters
- Reasoning effort: high.

## What to test
- Run with all refund facts missing. There should be exactly one question per rule, each with the recommended option first.
- Grep `/terms/` for "refund". Every mention should link to `/refunds/`.
- Screenshot the table at 320px.
