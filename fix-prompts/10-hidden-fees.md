# Prompt 10: Remove hidden fees (full price disclosure)

Phase 2 (after 16). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md`, `docs/compliance-log.md` and
`docs/legal-compliance.md`.

## Goal

A visitor reading `/solutions/` should be able to work out the total they'll pay, now and
later, for each service before they get in touch. That means every mandatory cost, every
recurring cost, and every cost paid to someone else.

## Why

The page says "Transparent pricing (no surprise invoices)" (`public/solutions/index.html:107`),
but several costs are missing or vague:

| Where | Problem |
|-------|---------|
| `:95` "$50 (flat fee, for a one-time fix; monthly for ongoing management)" | The monthly price isn't stated. A recurring charge with no price is classic drip pricing, and if it auto-renews, NY GBL §527-a requires clear disclosure of the renewal terms and how to cancel. |
| `:62` "Includes your domain setup" | The domain registration itself (and any renewal) costs money every year, and so may hosting. The page never says who pays, roughly how much, or whose name the domain is in. |
| `:80` "up to $250 rush order" | "Rush" is undefined, and so is what determines the $200–$250 range. |
| `:65` "$250-$375 (depending on website caliber and time frame)" | "Caliber" isn't defined, so the visitor can't tell which price applies. |
| none | Deposit, payment schedule, accepted payment methods, card surcharges, and sales tax are never mentioned. |
| `:7`, `:13` meta/og descriptions | They repeat the headline prices, so they must stay consistent with the full terms. |

Deceptive pricing is actionable under FTC Act §5 and NY GBL §349/§350, and it undermines the
page's own "no surprise invoices" promise.

## Task

1. **Gather facts** from `docs/business-facts.md`: what separates the $250 and $375 tiers; the
   rush definition and prices for both Launch and Rescue; the monthly management price, what it
   includes, billing date, auto-renewal, how to cancel, and any minimum term; deposit and
   payment schedule; payment methods and fees; how sales tax is handled (an accountant's answer,
   per `docs/legal-compliance.md`); domain and hosting costs, who pays, and in whose name;
   revisions included. Ask with `AskUserQuestion` for anything that's `TODO(owner)`, and write
   the answers back. **Don't invent a number.** If the owner hasn't decided the monthly price,
   remove the word "monthly" from the page until they do. Don't publish an unpriced recurring
   service.

2. **Rewrite each service's offer block** in `public/solutions/index.html`, keeping the existing
   structure (`.service`, `.service-info`, `.service-offer`, `.price`, `.price-amount`,
   `.price-note`, `.checklist`):
   - **Website Launch:** replace "depending on website caliber and time frame" with the concrete
     rule, for example "$250 for up to N pages; $375 for N+ pages or delivery within N days". Use
     the owner's actual rule.
   - **Website Rescue:** "$200 flat fee. Rush (done within N days): $250."
   - **Google Business Profile & Social Media:** separate the one-time fix and the monthly plan
     as two clearly priced lines. The monthly line states "$X/month, billed <when>, renews
     monthly until you cancel. Cancel any time by email, effective at the end of the current
     month." Adjust to the owner's actual terms.

3. **Add a "Costs outside our fee" block** after the services, before "Every Project Includes".
   Use an `h2.h3` heading and a short list: domain registration (approximate yearly cost, paid
   directly to the registrar and registered in the client's name, if that's the policy), hosting
   (cost, or "free on Netlify's starter plan" only if true), paid themes, plugins or stock
   images (only with the client's approval, at cost). Only list what the facts support.

4. **Add a "Payment" block**: deposit, when the balance is due, accepted methods, whether there
   are card fees, and how sales tax works. Link "Terms of Service" and "Refund Policy" here once
   those pages exist. Prompts 02 and 03 add the links if they come later, so leave a comment
   marker `<!-- links to /terms/ and /refunds/ added by prompts 02/03 -->`.

5. **Make "Every Project Includes" true.** Keep "Transparent pricing (no surprise invoices)"
   only if, after this change, every cost is listed. Make "Completion guarantee (we don't bill
   extra if a project takes longer)" match exactly what the owner confirmed. Prompt 12 handles
   the other claims in that paragraph.

6. **Update the meta description and `og:description`** (`:7`, `:13`) so any price shown there
   is accurate and not misleading. For example, drop "$50" if it now reads as cheaper than the
   real monthly offer.

7. **Styling.** Reuse existing classes. If you need a definition list or a small table, add
   minimal CSS next to the Solutions section in `public/assets/css/styles.css`, using existing
   tokens. It must look right at 375px, 768px and 1280px.

8. **Record every published price and term** in `docs/business-facts.md`, marked as the source
   for the Terms (Prompt 02) and Refunds (Prompt 03). Update item 10 in `docs/compliance-log.md`.

## Constraints

- No "starting at" or "from $X" unless the page also explains what moves the price up.
- No asterisks leading to fine print. Disclose the terms next to the price.
- Keep the copy plain and short. The audience "doesn't feel tech-savvy yet".

## Verify

- `python3 tools/check_site.py` passes.
- Playwright screenshots of `/solutions/` at 375px, 768px and 1280px.
- Read the page as a customer and total up each service, including year-one domain and hosting.
  Put that total in your summary so the owner can sanity-check it.

## Commit

`Fix #10: disclose all prices, recurring charges and third-party costs`. Push to the current
branch.
