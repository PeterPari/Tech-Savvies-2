# Prompt 10: Remove hidden fees

````text
<context>
public/solutions/index.html promises "Transparent pricing (no surprise invoices)" (:107), but leaves these costs undisclosed or vague:

| Location | Problem |
|----------|---------|
| :95 "$50 (flat fee, for a one-time fix; monthly for ongoing management)" | The monthly price is missing. An unpriced recurring charge is drip pricing, and NY GBL §527-a requires clear auto-renewal terms. |
| :62 "Includes your domain setup" | The yearly domain registration fee, hosting costs, who pays, and whose name the domain is in are all unstated. |
| :80 "up to $250 rush order" | "Rush" is undefined. |
| :65 "$250-$375 (depending on website caliber and time frame)" | "Caliber" is undefined. |
| nowhere | Deposit, payment schedule, payment methods, card fees and sales tax are missing. |
| :7 and :13 meta and og descriptions | Both repeat headline prices. |

Deceptive pricing is actionable under FTC Act §5 and NY GBL §349/§350.
</context>

<inputs>
docs/business-facts.md, docs/legal-compliance.md, docs/compliance-log.md, public/solutions/index.html, public/assets/css/styles.css
</inputs>

<deliverables>
1. Each service block on /solutions/, rewritten within the existing .service / .price / .price-amount / .price-note / .checklist markup, stating:
   - the rule that sets each price;
   - the rush definition and its price;
   - for the monthly plan: price per month, billing date, "renews monthly until you cancel", and how to cancel.
2. A "Costs outside our fee" block (h2 styled with .h3), before "Every Project Includes", listing each third-party cost the facts support: domain registration (approximate yearly cost, paid to the registrar, whose name it's registered in), hosting, and paid plugins or images (only with the client's approval).
3. A "Payment" block covering deposit, balance due date, accepted methods, card fees, and sales tax handling, ending with the comment <!-- links to /terms/ and /refunds/ added by prompts 02/03 -->.
4. "Every Project Includes", with each claim true under the new pricing. The completion guarantee wording must match docs/business-facts.md exactly.
5. Meta description and og:description (:7, :13) consistent with the new prices.
6. Any new CSS placed next to the Solutions section, using existing tokens.
7. Every published price and term recorded in docs/business-facts.md as the source for Prompts 02 and 03. Item 10 updated in docs/compliance-log.md.
8. One commit, "Fix #10: disclose all prices, recurring charges and third-party costs", pushed.
9. A final message of at most 8 bullets, including the year-one total a customer pays for each service (including domain and hosting).
</deliverables>

<examples>
<example index="1">$250 for a site of up to 5 pages · $375 for 6–10 pages or delivery within 7 days</example>
<example index="2">$200 flat fee · Rush (finished within 3 business days): $250</example>
<example index="3">$40/month, billed on the 1st. Renews monthly until you cancel. Cancel any time by emailing info@tech-savvies.com; it stops at the end of that month.</example>
</examples>

<constraints>
- Take every number and term from docs/business-facts.md. Ask the owner for any that are TODO(owner).
- If the monthly price is still undecided after asking, remove "monthly" from the page rather than publishing an unpriced recurring service.
- Put each condition next to its price. Don't use asterisks or footnotes, and don't write "starting at" or "from $X" unless the page also states what raises the price.
- Keep each price note to one sentence of at most 25 words.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- /solutions/ has no overflow at 375px, 768px and 1280px.
- Every price, and every price condition shown on the page, appears in docs/business-facts.md.
</acceptance_criteria>

<if_uncertain>
List any cost you believe exists but that the facts don't cover in the final message, as a question for the owner.
</if_uncertain>

<task>
Rewrite /solutions/ so a visitor can see every cost of each service before contacting Tech-Savvies: upfront, recurring, and paid to third parties.
</task>
````

## Assumptions
- Prompts 00, 24 and 16 have run.
- The owner has decided their prices, or can decide during the session.

## Parameters
- Reasoning effort: high. Pricing copy has legal consequences.

## What to test
- Run with the monthly price as `TODO(owner)` and the owner declining to answer. "Monthly" should disappear from the page.
- Check the year-one totals in the final message against the facts by hand.
- Check the page at 375px for price-note wrapping.
