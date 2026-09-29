# Prompt 09: Remove dark patterns

````text
<context>
The FTC staff report "Bringing Dark Patterns to Light" (2022) and FTC enforcement treat manipulative interfaces as unfair or deceptive under FTC Act §5. NY GBL §527-a targets subscriptions that are hard to cancel.

The initial audit found no UI dark patterns: no pre-ticked boxes, confirmshaming, countdowns, fake scarcity or disguised ads. It found one pricing risk, the unpriced "monthly" plan behind a "$50" headline, which Prompt 10 addresses. The remaining prompts add legal pages, a form notice, a data-request flow and possibly a cancellation path, so this prompt also sets the rules that UI must follow.

Categories to check:
- false urgency and false scarcity;
- confirmshaming;
- pre-selected options;
- hidden costs and drip pricing;
- bait-and-switch;
- forced continuity (is cancelling as easy as signing up?);
- obstruction (is requesting deletion as easy as sending an enquiry?);
- misleading visual hierarchy;
- trick wording;
- nagging overlays;
- disguised ads and undisclosed relationships;
- privacy-unfriendly defaults;
- fake social proof;
- forced registration and unnecessary fields.
</context>

<inputs>
docs/business-facts.md, docs/claims-register.md, docs/compliance-log.md, public/
</inputs>

<deliverables>
1. docs/ux-honesty-rules.md, containing:
   - an audit table with the columns Category | Pages and flows checked | Result (pass/fail) | Evidence (file:line or screenshot description) | Fix. It covers every page in public/ and the contact form submit flow, at 375px and 1280px;
   - "Rules for new UI", each rule stated in at most 20 words:
     - choices of equal weight look equal;
     - no pre-ticked consent;
     - declining takes no more steps than accepting;
     - cancelling or deleting uses the same channel as signing up;
     - every price is shown with its recurring terms;
     - no countdowns or "only N left" unless true and enforced automatically;
     - no guilt-trip decline wording;
     - disclosures sit next to their claim.
2. Fixes for every failure in public/, using existing classes. If no cancellation path for the monthly plan is stated anywhere, add one sentence next to its price on /solutions/, using the cancellation method in docs/business-facts.md.
3. A link to docs/ux-honesty-rules.md in the README "Editing" section, and item 9 updated in docs/compliance-log.md.
4. One commit, "Fix #09: audit for dark patterns and add honest-UI rules", pushed.
5. A final message of at most 6 bullets.
</deliverables>

<constraints>
- If /solutions/ still shows "monthly" without a price, stop and report that Prompt 10 must run first. Leave pricing changes to Prompt 10.
- Make the smallest markup or copy change that removes each manipulation. Leave page layouts unchanged.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- Every category above has a row in the audit table.
- Changed pages have no layout breaks at 375px and 1280px.
</acceptance_criteria>

<task>
Audit every Tech-Savvies page and flow for dark patterns, remove any you find, and write the honest-UI rules that new UI must follow.
</task>
````

## Assumptions
- Prompts 10, 12 and 11 have run.

## Parameters
- Model: sonnet.
- Reasoning effort: medium.

## What to test
- Run before Prompt 10 on purpose. The session should stop at the "monthly" check.
- Every one of the 14 categories appears in the audit table with evidence.
