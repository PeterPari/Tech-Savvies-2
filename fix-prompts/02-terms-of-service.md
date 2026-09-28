# Prompt 02: Terms of Service

Phase 3 (after 01, 04, and after 10 and 12). Paste everything below the line into a new Claude
Code session opened at the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md`, `docs/legal-compliance.md`,
`docs/claims-register.md`, `docs/ux-honesty-rules.md` and `docs/compliance-log.md`. Read the
current `public/solutions/index.html`: its prices and promises are what these Terms must match.
If Prompt 10 or 12 hasn't been run, stop and say so.

## Goal

Publish `/terms/`, plain-English Terms covering (a) use of the website and (b) how
Tech-Savvies projects and the monthly plan work: quotes, payment, timelines, revisions,
ownership, cancellation and liability. Every term must be consistent with `/solutions/`.

## Why

The site sells services with published prices and promises ("Completion guarantee", a monthly
plan, rush orders, domain setup), but nothing defines them. Undefined terms lead to disputes,
and when the business is small, disputes are expensive. Specific legal hooks:
- **NY GBL §527-a** requires clear auto-renewal terms and a cancellation method for the monthly
  plan;
- the "completion guarantee" and "no surprise invoices" claims need concrete, enforceable
  meaning (FTC Act §5 / NY GBL §349);
- minors can generally void contracts in NY (GOL §3-101), which matters for clients under 18
  and, depending on the facts file, for the business side too.

## Content (with `id`s)

1. **About these terms** (`#about`): who "we" are (legal name, dba, address, email), effective
   date, and how the Terms apply (browsing the site; hiring us).
2. **Using this website** (`#website`): content is general information; prices can change, but a
   quote you accepted won't; links to other sites aren't endorsements; don't misuse the site or
   form.
3. **Quotes and scope** (`#quotes`): work starts after a written quote (email is fine) is
   accepted; the quote defines scope; changes outside scope are quoted before we do them. Never
   bill without agreement, which keeps "no surprise invoices" true.
4. **Prices and payment** (`#payment`): mirror `/solutions/` exactly (tiers, rush definition,
   deposit, due dates, methods, sales tax), taking values from `docs/business-facts.md`.
   Late payment terms only if the owner wants them.
5. **Timelines** (`#timelines`): estimates, not guarantees; "as little as N days" depends on
   receiving content and feedback; client delays move the schedule.
6. **Revisions** (`#revisions`): how many rounds are included, and what counts as one.
7. **Completion guarantee** (`#completion-guarantee`): the owner's exact definition, for
   example "we don't charge more than the quoted price if the agreed scope takes us longer than
   estimated". Use identical wording on `/solutions/`.
8. **Your responsibilities** (`#client-responsibilities`): accurate content; rights to the
   text, photos and logos you give us; timely feedback; account access you choose to share.
9. **Domains, hosting and third-party services** (`#third-party-costs`): who registers the
   domain and in whose name (recommend the client's name); who pays renewals; that third-party
   services have their own terms and prices; that we're not responsible for their outages or
   price changes.
10. **Ownership** (`#ownership`): after full payment, the client owns the final site content and
    design made for them. We keep ownership of our pre-existing tools and code and grant a
    licence to use them in the site. Portfolio use: we may show the finished work unless the
    client says no (use the owner's preference).
11. **Monthly management plan** (`#monthly-plan`): price, what's included, billing date,
    **"renews automatically each month until you cancel"**, how to cancel (email, same channel
    used to sign up), when it takes effect, no cancellation fee, and whether there's a refund for
    a partial month (link to `/refunds/` once it exists; Prompt 03). Include a price-change
    notice period. Verify each element against the current §527-a text cited in
    `docs/legal-compliance.md`.
12. **Search and social results** (`#results`): we can't guarantee rankings, traffic,
    followers or sales, because Google and social platforms decide those.
13. **Warranty and fixes** (`#fixes`): for example "we fix bugs in our work reported within N
    days of launch at no charge". Use the owner's number, or leave the section out.
14. **Limitation of liability** (`#liability`): a plain, reasonable cap (for example, the
    amount paid for the project) and exclusions for indirect loss, "to the extent the law
    allows". Mark this section for attorney review in the compliance log.
15. **Age** (`#age`): you must be 18 or older, or have a parent or guardian agree to these Terms
    and act as the client (Prompt 17 refines this). **If `docs/business-facts.md` says the
    person signing for Tech-Savvies is under 18**, don't draft around it. Tell the owner in your
    summary that a parent or guardian should co-sign client agreements, and that an attorney
    should confirm the setup.
16. **Ending a project** (`#termination`): either side can end it; what's paid for work done;
    handover of files.
17. **Disputes and governing law** (`#law`): talk to us first (email; we'll respond within N
    days); New York law; courts in the county from the facts file. **Don't** add mandatory
    arbitration or a class-action waiver. Note in the compliance log that an attorney can
    advise on those.
18. **Changes to these terms** (`#changes`), and **Contact** (`#contact`).

Writing rules: same as the Privacy Policy (plain English, "we"/"you", facts from docs only, no
placeholders on the page).

## Build

1. `public/terms/index.html` from the privacy page template. Title "Terms of Service |
   Tech-Savvies", unique description, canonical, `og:` tags.
2. **Footer, every HTML page:** add "Terms of Service" to the Legal column (order: Terms, Privacy,
   Cookies; Refunds will come after Terms). Confirm with `grep -L`.
3. **`/solutions/`:** replace Prompt 10's comment marker with a sentence in the Payment block,
   "See our <a href="/terms/">Terms of Service</a> for full details.", using an underlined
   in-text link. Make the completion guarantee wording identical in both places.
4. Add `/terms/` to the sitemap, README pages table, and `REQUIRED_FOOTER_LINKS`.
5. Add a `terms-consistency` check to `tools/check_site.py`: each price string in the
   `.price-amount` elements on `/solutions/` must also appear in `/terms/`, or `/terms/` must link
   to `/solutions/` for prices. Pick one approach and document it in the check's comment.
6. Update item 2 in `docs/compliance-log.md`, and flag sections 11, 14 and 17 for attorney review.

## Verify

- `python3 tools/check_site.py` passes.
- Playwright screenshots at 375px and 1280px; keyboard tab-through.
- A side-by-side read of `/solutions/` and `/terms/`: list every price and promise and confirm
  they match. Include the list in your summary.

## Commit

`Fix #02: add terms of service matching published prices and promises`. Push to the current
branch.
