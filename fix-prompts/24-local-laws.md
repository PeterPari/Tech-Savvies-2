# Prompt 24: Check local laws (compliance map)

Run in Phase 1 (right after Prompt 00), and again at the very end for the "Final pass" section.
Paste everything below the line into a new Claude Code session opened at the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 (Key decisions) and §4 (Ground rules), then `docs/business-facts.md` and
`docs/compliance-log.md`.

Tech-Savvies is a small web-design business run by one person in New York City. It sells
website builds, website repairs, and Google Business Profile / social media help, with prices
published on `/solutions/`. It collects enquiries through a Netlify contact form.

## Goal

Create `docs/legal-compliance.md`, a map of which laws apply to this site and business, what
each one requires, and which prompt or page handles it. Every legal page in this plan will be
written against this map, so it must be accurate and current.

## Why

Laws change, and model memory lags. The plan's other prompts make concrete promises about
privacy, pricing, refunds and accessibility. If they are built on a stale or wrong reading of
the law, the site gets confidently wrong legal pages, which is worse than none. This prompt
makes the legal basis explicit, sourced and reviewable.

## Task

1. **Research each candidate law with `WebSearch`/`WebFetch`.** Confirm its current status and
   requirements from a primary or authoritative source: statute text, FTC.gov, ag.ny.gov,
   dos.ny.gov, tax.ny.gov, ada.gov, the California AG. Cite the URL and the date you checked.
   Don't rely on memory for thresholds, effective dates, or whether a rule was vacated.

   Candidates to assess:
   - **FTC Act §5** (unfair/deceptive practices): marketing claims and pricing.
   - **FTC Trade Regulation Rule on Consumer Reviews and Testimonials (16 CFR Part 465)** and the
     **FTC Endorsement Guides (16 CFR Part 255)**: case studies and testimonials.
   - **FTC negative-option / "click-to-cancel" rule**: check its current legal status.
   - **NY General Business Law §349/§350**: deceptive acts and false advertising.
   - **NY GBL §527-a** (automatic renewal): the "monthly for ongoing management" plan.
   - **NY GBL §130** (assumed name / DBA): trading as "Tech-Savvies" rather than the owner's
     legal name.
   - **NY SHIELD Act** (GBL §899-aa, §899-bb): what counts as "private information", and whether
     contact-form data triggers it.
   - **NY Child Data Protection Act**: scope, and whether a general-audience B2B site with no
     knowledge of minor users is covered.
   - **Minors' capacity to contract in NY** (General Obligations Law §3-101). This matters if the
     business owner or a client is under 18.
   - **CalOPPA** (Cal. Bus. & Prof. Code §22575–22579): requires a posted privacy policy, including
     a statement on Do Not Track, for any site collecting PII from California residents.
   - **CCPA/CPRA thresholds**: expected answer is "not applicable", but show the thresholds.
   - **Other US state comprehensive privacy laws**: thresholds; expected not applicable.
   - **GDPR / UK GDPR**: only if `docs/business-facts.md` says EU/UK clients are deliberately
     targeted.
   - **COPPA**: site not directed to children; still state that in the policy.
   - **CAN-SPAM Act**: any promotional email.
   - **ADA Title III, NY State Human Rights Law, NYC Human Rights Law**: website accessibility,
     and the level of NY accessibility litigation.
   - **NY sales tax on web design / hosting / domain resale**: find the relevant tax.ny.gov
     guidance, then route the conclusion to an accountant. Don't state a tax position on the site.
   - **NYC Consumer and Worker Protection rules** relevant to service pricing and advertising, if any.
   - **Record-retention requirements** for invoices and tax records (for the deletion policy in #20).

2. **Write `docs/legal-compliance.md`** with:
   - A summary of the laws that apply and the top 5 owner actions.
   - A table: `Law` | `Applies?` (Yes / No / Only if …) | `Why` | `What it requires of this site` |
     `Handled by` (prompt # and page) | `Source (URL, checked date)`.
   - An "Owner actions outside the website" section: DBA filing, attorney review of Terms,
     Refunds and Privacy, accountant on sales tax, and contract co-signing if the signer is
     under 18. Base these on the facts file, and don't make assumptions about the owner.
   - A "Not legal advice" note at the top.

3. **Check for plan conflicts.** If any finding changes a decision in `fix-plan.md` §2 (for
   example, a law requires a consent mechanism the plan decided against), say so prominently in
   your final message and add a note under §2. Don't silently rewrite other prompts.

4. Update item 24 in `docs/compliance-log.md`.

## Final pass (run again after every other prompt is done)

Re-open `docs/legal-compliance.md` and check every "Handled by" entry against the live pages in
`public/`: open the page, find the clause or feature, and confirm it matches. Record the result
in a "Final pass (date)" section, listing any gaps, and fix small gaps directly. Refresh any
source whose checked date is more than 6 months old.

## Constraints

- Don't edit `public/` in the first run. This prompt produces documentation only.
- Say "unclear, ask an attorney" rather than guessing.
- Keep the owner's personal details out of the doc unless they're already in the facts file.

## Commit

`Fix #24: add legal compliance map for NY-based web design business` (final pass:
`Fix #24: final compliance pass`). Push to the current branch.
