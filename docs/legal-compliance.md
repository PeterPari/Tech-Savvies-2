# Legal compliance map

> **Not legal advice.** This map shows which laws may apply and where the site handles them. A New York attorney and an accountant should confirm it.

## Summary

Tech-Savvies is a one-person sole proprietorship in New York. It trades as “Tech-Savvies” with no
DBA filed and serves business clients remotely, anywhere. Going by `docs/business-facts.md`, these
laws apply: FTC Act §5 and NY GBL §349/§350 (all advertising and prices), the FTC Endorsement Guides
(the Grisha.studio case study features the owner’s brother), GBL §130 (trading under a name other
than the owner’s), GOL §3-101 (the contract signer is under 18), and tax record-keeping. The monthly
plan is re-booked each month, so automatic-renewal rules don’t apply while that stays true. EU/UK
rules don’t apply because those clients aren’t targeted. Most other rows depend on definitions or
thresholds this session couldn’t read. The network policy blocked every official source, so no
requirement is quoted yet. [`legal-sources-prompt.md`](legal-sources-prompt.md) collects the text for a re-run.

## Sources: status on 2026-09-29

Every official host tried was blocked by this session’s network policy: nysenate.gov, ftc.gov,
ecfr.gov, federalregister.gov, uscode.house.gov, govinfo.gov, ada.gov, oag.ca.gov and tax.ny.gov
(law.cornell.edu too). A web search confirmed that each URL below exists on an official site. Search
summaries aren’t statute text, so nothing from them is used as a requirement, threshold, date or
legal status. The Checked column records that only the URL was confirmed.

## Map

Page anchors are the ones the named prompt is told to create. The final-pass run checks each against the live page.

| Law | Applies? | Why | Requirement (quoted from the source) | Handled by | Source URL | Checked |
|-----|----------|-----|--------------------------------------|------------|------------|---------|
| FTC Act §5 (15 U.S.C. §45) | Yes | The site advertises paid services and their prices | Not fetched (blocked by network policy) | 09 site-wide + `docs/ux-honesty-rules.md`, 10 /solutions/, 12 /, /solutions/, /contact/ | https://uscode.house.gov/view.xhtml?req=%28title%3A15+section%3A45+edition%3Aprelim%29 | 2026-09-29, URL only |
| FTC Rule on Consumer Reviews and Testimonials (16 CFR 465) | Only if the site shows reviews or testimonials | None on the site today: no ratings, quotes or review schema (plan §1 #11) | Not fetched (blocked by network policy) | 11 `docs/testimonials-policy.md` + `tools/check_site.py` guard | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465 | 2026-09-29, URL only |
| FTC Endorsement Guides (16 CFR 255) | Yes | The home-page case study features a client run by the owner’s brother (business-facts, 2026-09-29) | Not fetched (blocked by network policy) | 11 / case study, disclosure next to it or one click away (compliance log #11) | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255 | 2026-09-29, URL only |
| FTC negative-option (“click-to-cancel”) rule: current status | Only if the monthly plan renews automatically | The owner confirmed on 2026-09-29 that clients re-book each month. Current legal status not confirmed: a search listed a Federal Register notice of 2026-02-12, “Revision of the Negative Option Rule … to Conform These Rules to Federal Court Decisions”, which is still unread | Not fetched (blocked by network policy) | 02 /terms/#monthly-plan, 10 /solutions/ (state that the plan is re-booked monthly) | https://www.federalregister.gov/documents/2026/02/12/2026-02866/revision-of-the-negative-option-rule-withdrawal-of-the-cars-rule-removal-of-the-non-compete-rule-to | 2026-09-29, URL only |
| NY GBL §349 / §350 | Yes | A New York business advertising prices, delivery times and results | Not fetched (blocked by network policy) | 09 site-wide, 10 /solutions/, 12 /, /solutions/, /contact/ | https://www.nysenate.gov/legislation/laws/GBS/349 and https://www.nysenate.gov/legislation/laws/GBS/350 | 2026-09-29, URL only (the GBS index was confirmed, not these two pages) |
| NY GBL §527-a (automatic renewal) | Only if the monthly plan renews automatically | Not today: clients re-book each month (owner, 2026-09-29). Prompt 02’s planned “renews automatically” wording would contradict this | n/a while the plan is re-booked; statute not fetched | 02 /terms/#monthly-plan, 10 /solutions/ | https://www.nysenate.gov/legislation/laws/GBS/527-A | 2026-09-29, URL only |
| NY GBL §130 (assumed name) | Yes | The sole proprietor trades as “Tech-Savvies”, not under their own name, and no DBA is filed (business-facts) | Not fetched (blocked by network policy) | Owner action (DBA filing, below); 16 footer + /contact/, 01 /privacy/#contact, 02 /terms/#about show the legal name | https://www.nysenate.gov/legislation/laws/GBS/130 and https://dos.ny.gov/instructions-completing-certificate-assumed-name-0 | 2026-09-29, URL only |
| NY GBL §218-a (refund policy posting) | Unclear; ask an attorney | Whether it covers a services-only online business wasn’t confirmed from the text | Not fetched (blocked by network policy) | 03 /refunds/ (posted regardless), 10 /solutions/ Payment block link | https://www.nysenate.gov/legislation/laws/GBS/218-A | 2026-09-29, URL only |
| NY SHIELD Act (GBL §899-aa, §899-bb) | Unclear; ask an attorney | Holds enquiry names and emails. Sometimes holds client Google Business Profile and social media logins (owner, 2026-09-29). Whether those count as “private information” turns on a definition not fetched | Not fetched (blocked by network policy) | 01 /privacy/#security, 07 `docs/data-inventory.md`, 20 `docs/data-requests-runbook.md`; owner action (client logins, below) | https://www.nysenate.gov/legislation/laws/GBS/899-AA, https://www.nysenate.gov/legislation/laws/GBS/899-BB, https://ag.ny.gov/resources/organizations/data-breach-reporting/shield-act | 2026-09-29, URL only |
| NY Child Data Protection Act (GBL §899-ee et seq.) | Unclear; ask an attorney | The site is aimed at businesses, not minors. How the Act treats a site that learns an enquirer is a minor wasn’t confirmed | Not fetched (blocked by network policy) | 17 /privacy/#children, /contact/ `p#form-privacy`, `docs/data-inventory.md` “Minors” | https://www.nysenate.gov/legislation/laws/GBS/A39-FF and https://ag.ny.gov/child-data-protection-act-guidance | 2026-09-29, URL only |
| NY General Obligations Law §3-101 (minors’ contracts) | Yes | The person who signs client contracts for Tech-Savvies is under 18 (business-facts). It also bears on under-18 clients | Not fetched (blocked by network policy) | Owner action (parent or guardian co-signing, below); 02 /terms/#age, 17 /contact/ `p#form-privacy` | https://www.nysenate.gov/legislation/laws/GOB/3-101 | 2026-09-29, URL only |
| CalOPPA (Cal. Bus. & Prof. Code §22575–22579) | Unclear; ask an attorney | The contact form collects names and emails from visitors anywhere, California included. Whether business enquirers count as “consumers” under §22577 wasn’t confirmed | Not fetched (blocked by network policy) | 01 /privacy/ (linked in every footer; #cookies covers Do Not Track; #changes) | https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=BPC&division=8.&title=&part=&chapter=22.&article= | 2026-09-29, URL only |
| CCPA/CPRA | Only if Tech-Savvies crosses a “business” threshold in Cal. Civ. Code §1798.140(d) | A one-person business that doesn’t sell or share data. The threshold figures weren’t fetched, so there’s no comparison yet | Not fetched (blocked by network policy) | 01 /privacy/#how-we-use-it (no sale or sharing), 20 /privacy/#your-rights | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.140. and https://oag.ca.gov/privacy/ccpa | 2026-09-29, URL only |
| Other US state privacy laws | Only if a state’s applicability test is met | Not researched state by state. No official source fetched, and no single official list exists | Not fetched | 01 /privacy/#how-we-use-it, 20 /privacy/#your-rights | None fetched (check each state’s statute or attorney general) | Not checked |
| GDPR / UK GDPR | Only if EU/UK clients are deliberately targeted | `docs/business-facts.md` says they aren’t (owner, 2026-09-29) | n/a unless that changes; Art. 3 not fetched | 01 /privacy/#international (one sentence: data is processed in the US) | https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng and https://www.legislation.gov.uk/eur/2016/679/article/3 | 2026-09-29, URL only |
| COPPA (16 CFR 312) | Only if the site is aimed at children under 13 or knowingly collects their data (scope text not fetched) | The site is for businesses. Decision 3 in fix-plan §2 says it isn’t aimed at under-13s | Not fetched (blocked by network policy) | 17 /privacy/#children | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312 | 2026-09-29, URL only |
| CAN-SPAM | Only if marketing (commercial) email is sent | No marketing email sent or planned, and no open-tracking (owner, 2026-09-29) | Not fetched (blocked by network policy) | 18 `docs/email-policy.md` + signatures | https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business | 2026-09-29, URL only |
| ADA Title III (website accessibility) | Unclear; ask an attorney | Online-only, with no physical premises (business-facts). No fetched source settles whether that makes it a public accommodation | Not fetched (blocked by network policy) | 13, 14, 15, 25 site-wide; 21 /accessibility/ | https://www.ada.gov/resources/web-guidance/ and https://www.ada.gov/topics/title-iii/ | 2026-09-29, URL only |
| NY State Human Rights Law (Exec. Law §296) | Unclear; ask an attorney | Same question for a New York business with no premises | Not fetched (blocked by network policy) | 21 /accessibility/ | https://www.nysenate.gov/legislation/laws/EXC/296 and https://dhr.ny.gov/public-accommodations | 2026-09-29, URL only |
| NYC Human Rights Law (Admin. Code §8-107) | Unclear; ask an attorney | Same question for an NYC-based provider of services | Not fetched | 21 /accessibility/ | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-219879 and https://www.nyc.gov/site/cchr/law/the-law.page | 2026-09-29, URL only |
| NY sales tax: web design, hosting, domain resale | Unclear; ask an accountant | Prices exclude tax and the owner hasn’t decided whether tax applies (business-facts). Hosting runs on Tech-Savvies’ own Netlify account, and clients pay for their own domains. No tax conclusion is drawn here | Not fetched (blocked by network policy) | Owner action (accountant, below); 10 /solutions/ Payment block, 02 /terms/#payment state the result | https://www.tax.ny.gov/pubs_and_bulls/tg_bulletins/st/quick_reference_guide_for_taxable_and_exempt_property_and_services.htm and https://www.tax.ny.gov/bus/st/register.htm | 2026-09-29, URL only |
| NYC consumer protection rules on service pricing (Admin. Code §20-700 et seq.) | Unclear; ask an attorney | NYC-based, but clients are businesses. Whether they buy “consumer” services under §20-701 wasn’t confirmed | Not fetched | 09 site-wide, 10 /solutions/, 12 /solutions/ | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-35314 and https://www.nyc.gov/site/dca/about/consumer-protection-and-licensing-laws.page | 2026-09-29, URL only |
| Record retention for invoices and tax records | Yes | Every sale creates invoices and payment records (Venmo, bank transfer). Emails are kept 12 months (business-facts), which may be shorter than the tax period; the period itself wasn’t fetched | Not fetched (blocked by network policy) | Owner action (accountant, below); 07 `docs/data-inventory.md` retention rule, 01 /privacy/#retention | https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records and https://www.tax.ny.gov/pubs_and_bulls/tg_bulletins/st/record-keeping_requirements_for_sales_tax_vendors.htm | 2026-09-29, URL only |

## Notes for other prompts

- **Prompt 02 (Terms), #monthly-plan.** Its deliverable says “renews automatically each month until
  you cancel”. The owner confirmed on 2026-09-29 that clients re-book each month. Write the clause to
  match the facts file, not the prompt’s example wording.
- **Prompts 01 and 20, response time for data requests.** This map doesn’t yet support any legal
  deadline, because no source was fetched. Promise only the reply time in `docs/business-facts.md`
  until the map is refreshed.
- **Prompts 01 and 07, retention.** Keep invoices and payment records apart from the 12-month email
  rule until an accountant confirms the tax retention period.
- **Prompts 01 and 07, security.** Client account logins are sometimes held. The inventory and
  /privacy/#security should describe how they’re stored, using only facts the owner confirms.

## Owner actions outside the website

1. **DBA filing.** Trading as “Tech-Savvies” rather than under your own legal name means GBL §130
   applies. File an assumed-name certificate with the county clerk where the business is conducted
   (see the Department of State instructions linked above), then record the county and date in
   `docs/business-facts.md`.
2. **Attorney review of Terms, Refunds and Privacy.** Have a New York attorney review /terms/,
   /refunds/ and /privacy/ before relying on them, along with every “Unclear; ask an attorney” row
   above.
3. **Accountant review of sales tax.** Ask an accountant, or the NY Department of Taxation and
   Finance, whether web design, repairs, profile management and hosting on your own Netlify account
   are taxable, and whether you need to register as a sales tax vendor. Ask them how long to keep
   invoices and payment records too. Record both answers in `docs/business-facts.md`.
4. **Parent or guardian co-signing.** `docs/business-facts.md` says the person who signs client
   contracts is under 18. Have a parent or guardian co-sign client contracts, or sign them as the
   contracting party, and ask the attorney which is right.
5. **Client logins.** Where a client can add you as a manager, prefer that to holding their password.
   Ask the attorney whether stored client logins bring the SHIELD Act’s duties into play.
6. **Refresh this map.** Run [`legal-sources-prompt.md`](legal-sources-prompt.md) in a session that
   can open official sites. Save its output as `docs/legal-sources.md`, then re-run Prompt 24 to fill
   in the Requirement column.
