# Prompt 03: Refund policy

Phase 3 (after 02). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md`, `docs/legal-compliance.md`,
`docs/ux-honesty-rules.md` and `docs/compliance-log.md`. Read `public/solutions/index.html` and
`public/terms/index.html`; the refund rules must agree with both.

## Goal

Publish `/refunds/`, a clear refund and cancellation policy for each service: before work
starts, during the project, after delivery, rush fees, the monthly plan, and third-party costs.
Include how to ask and how fast the money comes back.

## Why

People paying a small business a few hundred dollars upfront want to know what happens if
things go wrong. The site promises a "completion guarantee" and sells a recurring monthly plan,
and both need matching refund and cancellation rules. Without a written policy, every
disagreement is a negotiation, and customers may go straight to a card chargeback. NY GBL
§218-a requires retailers to conspicuously post their refund policy for goods. It's aimed at
goods rather than services, so check its scope in `docs/legal-compliance.md`, but posting one is
best practice either way. NY §527-a also covers cancelling auto-renewing plans.

## Task

1. **Get the rules from the owner.** Use `docs/business-facts.md` first, then `AskUserQuestion`
   for gaps. Offer sensible options and mark a recommendation where one is fair to both sides:
   - **Cancel before work starts:** full refund of the deposit (recommended) / deposit
     non-refundable / refund minus a fixed admin amount.
   - **Cancel mid-project:** pay for work done so far at a stated rate or percentage, refund the
     rest (recommended) / no refund.
   - **After delivery:** no refund, but bugs are fixed free within N days (recommended) /
     satisfaction refund within N days.
   - **Rush fee:** refunded if the rush deadline is missed (recommended) / not refundable.
   - **Monthly plan:** cancel any time, effective end of the current paid month, no partial
     refund (recommended) / prorated refund.
   - **Third-party costs** (domains, paid plugins bought for the client): not refundable by us,
     but the domain stays the client's.
   - **Refund method and timing:** same payment method, within N business days of approval.

2. **Write `public/refunds/index.html`** from the privacy page template. Title "Refund Policy |
   Tech-Savvies", unique description, canonical, `og:` tags. Content:
   - `h1`, "Last updated";
   - a **summary table or list** per service (Website Launch, Website Rescue, Google & Social
     one-time, Monthly plan), in plain language;
   - sections: `#before-work-starts`, `#during-a-project`, `#after-delivery`, `#rush-orders`,
     `#monthly-plan`, `#third-party-costs`, `#how-to-ask` (a `mailto:` with a prefilled subject
     "Refund request"; include the project name or invoice number), `#timing`,
     `#if-we-miss-a-promise` (how the completion guarantee and missed rush deadlines are
     honoured), `#chargebacks` (a friendly note: please contact us first; we'll respond within N
     business days; no threats), and `#contact`.

   If you use a table, it needs a `<caption>` and `<th scope>`, and must reflow at 320px using
   the scroll-region pattern from `.prose table`.

3. **Consistency.** Where `/terms/` mentions refunds, link to `/refunds/` and remove any
   conflicting wording. On `/solutions/`, add "Refund Policy" next to the Terms link in the
   Payment block.

4. **Footer, every HTML page:** add "Refund Policy" after "Terms of Service" in the Legal column.
   Confirm with `grep -L`.

5. Add `/refunds/` to the sitemap, README pages table, and `REQUIRED_FOOTER_LINKS`.

6. Write the final refund rules into `docs/business-facts.md`. Update item 3 in
   `docs/compliance-log.md` and flag it for attorney review.

## Constraints

- The monthly plan's cancel path must be as easy as signing up (see `docs/ux-honesty-rules.md`).
- No wording that discourages refunds ("refunds are rarely granted").

## Verify

- `python3 tools/check_site.py` passes.
- Playwright screenshots at 320px, 375px and 1280px, since the table must not overflow.
- Read `/solutions/`, `/terms/` and `/refunds/` together and list any contradiction, which
  should be none.

## Commit

`Fix #03: add refund and cancellation policy`. Push to the current branch.
