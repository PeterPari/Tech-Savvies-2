# Claims register

Every objective claim on the site: a time, number, result, guarantee or fact about the business
that a visitor could check. Under FTC Act §5 and NY GBL §349/§350 the business needs a
reasonable basis for each one before publishing it. Puffery (“affordable”, “Websites done fast.
Websites done right.”) needs none and is listed at the end only so it isn’t re-audited.

A new objective claim needs a row here, with its evidence, before it goes on the site. The
`claims` check in `tools/check_site.py` fails on the phrases in `BANNED_PHRASES`.

Evidence comes from [`business-facts.md`](business-facts.md). Locations are as of Prompt 12
(2026-09-29). “Owner to confirm” means the wording is qualified until the owner supplies the fact.

## Claims from the initial audit

| Claim | Location | Issue | Evidence / owner confirmation | Decision | New wording |
|-------|----------|-------|-------------------------------|----------|-------------|
| “We typically reply within 2 hours during NYC business hours” | /contact/ meta, og, lead and Replies block; /contact/thanks/ meta, og and lead | Specific and measurable; hard to keep as a one-person business | Owner, 2026-09-29: realistic first reply is within 1 business day; no fixed hours | Qualify (done in Prompt 16) | “We typically reply within 1 business day.” and “No fixed hours.” |
| “Custom site built in as fast as 5 days” | /solutions/ Launch (replaced by the rush tier in Prompt 10): headline note (line 64) and Rush row (line 71) | Needs a real delivery in that time, and its conditions | Owner, 2026-09-29: no site delivered in 5 days yet (two clients so far, both Tier 3, neither rushed). 5 days is the owner’s estimate for a relatively simple site. Owner to confirm when the 5 days start and what happens if a rush runs late | Qualify: a target, not a delivery promise | “a rush on a Tier 1–3 site (5-day target) costs $375” and “Rush: we aim to deliver a Tier 1, 2 or 3 site within 5 days; Tiers 4 and 5 can’t be rushed.” |
| “basic SEO so you show up when customers search for your services” | Formerly /solutions/ Launch description | Implies a ranking outcome | None | Remove (done in Prompt 10) | None: the Launch description now lists what the service does |
| “SEO Setup (Get found on Google)” | /solutions/ Launch checklist (line 74) | Outcome claim | Tier SEO work is listed in business-facts (titles, meta, schema, sitemap, Search Console); no ranking can be promised | Qualify | “SEO Setup on every tier (so Google can find your site)” |
| “fix your social media for maximum search visibility” | / What we offer, Google & Social Presence (line 94) | “Maximum” can’t be proven | The $50 service sets up or refreshes the Google Business Profile and social media (business-facts, Prices) | Qualify | “We set up or refresh your Google Business Profile and your social media profiles.” |
| “Get found by locals and tourists.” | / What we offer, Google & Social Presence (line 94) | Outcome claim, same sentence as above | As above | Qualify | “Make it easier for locals and tourists to find you.” |
| “If you want it on your website, you’ll get it.” | / What we offer, New Websites (line 90) | Absolute promise that conflicts with fixed prices | Prices are fixed by tier (business-facts, Prices) | Qualify | “Tell us what you want on your site. We’ll build it, or tell you upfront if it’s outside the quoted price.” |
| “you reach your lead engineer, not a ticketing system” | /solutions/ Every Project Includes (line 138) | Implies a team; the business is one person | Owner, 2026-09-29: Peter does the work himself, using Claude and ChatGPT as tools; no staff or subcontractors | Qualify | “you talk directly to Peter, who builds your site, not a ticketing system” |
| “Security Patching” | /solutions/ Rescue checklist (line 95) | Scope undefined | Owner, 2026-09-29: updating the site’s platform, theme and plugins to current versions and making sure HTTPS is on. No audit or ongoing monitoring | Qualify | “Security Updates (platform, theme and plugins updated; HTTPS on)” |
| Case-study facts (“secured his preferred domain”, “created his Instagram page”, “worked with him from the beginning”, “Over the next few weeks”, checklist: New Website Build, Social Channel Streamlining, New Website Domain) | / Featured Showcase (lines 105–118) | Accuracy and the family connection | Owner, 2026-09-29: real client, written permission, the owner’s brother. Narrative accuracy is Prompt 11’s | Left to Prompt 11 | Unchanged here |

## Further objective claims in public/

| Claim | Location | Issue | Evidence / owner confirmation | Decision | New wording |
|-------|----------|-------|-------------------------------|----------|-------------|
| “Rush: the Rescue finished within 5 days.” | /solutions/ Rescue (line 90) | Same as the Launch rush: no Rescue delivered yet | Owner, 2026-09-29: no rushed project yet. Owner to confirm when the 5 days start | Qualify: a target | “Rush: we aim to finish the Rescue within 5 days.” |
| Tier prices $250 / $275 / $300 / $330 / $375; Rescue $200, rush $250; $50 one-time; $50/month | /solutions/ meta, og and service cards | Prices | Owner, 2026-09-29; Tier 2 changed to $275 by the owner, 2026-09-30 (business-facts, Prices and Monthly management) | Keep | |
| Tier contents (pages, gallery, map, form, animations, CMS, store) | /solutions/ Launch tiers (lines 66–70) | Scope per price | Owner, 2026-09-29 (business-facts, Prices) | Keep | |
| “Tiers 4 and 5 can’t be rushed” | /solutions/ Rush row (line 71) | Limit | Owner, 2026-09-29 | Keep | |
| “Mobile Responsive (Phone Ready)”, “Custom Design from Tier 2”, “Contact Form from Tier 2” | /solutions/ Launch checklist (lines 75–77) | Feature claims | Tier contents in business-facts (Tier 1 is a template layout) | Keep | |
| “Domain Setup (registered in your name)” and the domain cost “about $10–$20 a year” | /solutions/ Launch checklist and Costs outside our fee | Ownership and cost | Owner, 2026-09-29 (business-facts, Domain, hosting and ownership) | Keep | |
| “Hosting on our account ($0)” | /solutions/ Launch checklist (line 79) | Free hosting | Owner, 2026-09-29: $0 while the site fits Netlify’s free plan; the condition is stated in Costs outside our fee on the same page | Keep | |
| Speed optimization, layout repairs, mobile fixes | /solutions/ Rescue (lines 86–94) | Work performed, not a result | Service description; no speed figure is promised | Keep | |
| “we can help you drive more engagement and potentially more customers” | /solutions/ Presence (line 102) | Outcome | Hedged (“can help”, “potentially”); no figure promised | Keep | |
| “Every cost listed, including domain.” | /solutions/ meta and og description | Completeness | Prompt 10 lists every fee and outside cost; sales tax is disclosed as “if it applies” | Keep | |
| “Transparent pricing (… so no surprise invoices)” | /solutions/ Every Project Includes (line 138) | Pricing promise | All prices and outside costs are on the page (Prompt 10) | Keep | |
| “Unlimited revisions within the agreed scope” | /solutions/ Every Project Includes | Guarantee | Owner, 2026-09-29 (business-facts, Scope) | Keep | |
| “Completion guarantee: no extra billing if a project takes longer than expected” | /solutions/ Every Project Includes | Guarantee | Owner, 2026-09-29 (business-facts, Scope) | Keep | |
| 50% deposit, Venmo or bank transfer, no payment fees, tax excluded | /solutions/ Payment | Payment terms | Owner, 2026-09-29 (business-facts, Payment) | Keep | |
| “We typically reply within 1 business day” and “No fixed hours” | /contact/ and /contact/thanks/, including meta and og | Reply time | Owner, 2026-09-29 | Keep | |
| “Based in New York, NY. Serving clients anywhere, remotely.”; footer “New York, NY”; JSON-LD `address` and `areaServed: Worldwide` | /contact/, every footer, / JSON-LD | Location and service area | Owner, 2026-09-29: service area anywhere (remote); New York from the original site and logo, published in Prompt 16 | Keep | |
| Founded 2020 by Peter Parizhsky to help older adults with technology; paused 2023 for school; relaunched 2026; JSON-LD `foundingDate`, `founder` | /our-story/ (line 57), meta and og; / JSON-LD | History | Owner, 2026-09-29: accurate | Keep | |
| “Peter continues to run the business and manage every project that comes through it himself.” | /our-story/ (line 57) | Who does the work | Owner, 2026-09-29: Peter, using Claude and ChatGPT as tools | Keep | |
| Legal name Peter Parizhsky, trading as Tech-Savvies | Every footer, /our-story/, / JSON-LD | Identity | Owner, 2026-09-29 (business-facts, Identity) | Keep | |

## Claims added by /terms/ (Prompt 02, 2026-09-29)

Prices, payment terms, outside costs and the completion guarantee on /terms/ repeat the /solutions/ rows
above word for word; the `terms-consistency` check keeps the prices and the guarantee in step.

| Claim | Location | Issue | Evidence / owner confirmation | Decision | New wording |
|-------|----------|-------|-------------------------------|----------|-------------|
| The 5-day rush clock starts once the deposit and all content are in; a late rush drops to the normal price | /terms/#payment “Rush orders” | Defines the rush target | Owner, 2026-09-29 (business-facts, Service area and hours) | Keep | “If we take longer than 5 days, and we aren’t waiting on you, you pay the normal price instead.” |
| “For 30 days after your site launches, we fix bugs and make tweaks for free” | /terms/#fixes | Service promise | Owner, 2026-09-29 (business-facts, Scope): agreed work only; Launch and Rescue only (Prompt 03) | Qualify (Prompt 03) | “For 30 days after we deliver a Website Launch or a Website Rescue, we fix bugs and make tweaks for free” |
| Completion guarantee means the accepted quote is the most the client pays for that work; “no surprise invoices” lists everything a client can be charged | /terms/#completion-guarantee | Gives the /solutions/ promises a concrete meaning (FTC Act §5, GBL §349) | Owner, 2026-09-29 (business-facts, Scope and Payment) | Keep | |
| Monthly plan: 30 days per booking, no automatic renewal, nothing to cancel, no partial-month refund | /terms/#monthly-plan | Recurring terms | Owner, 2026-09-29 (business-facts, Monthly management and Refunds) | Keep | |
| “We reply within 1 business day” to disputes | /terms/#law | Reply time | Owner, 2026-09-29: first reply within 1 business day | Keep | |

## Claims added by /accessibility/ (Prompt 21, 2026-09-29)

| Claim | Location | Issue | Evidence / owner confirmation | Decision | New wording |
|-------|----------|-------|-------------------------------|----------|-------------|
| “We aim to meet WCAG 2.2 AA” | /accessibility/#goal | Conformance claim | Worded as an aim, never “fully compliant”; audit in accessibility-audit.md | Keep | |
| Tested with axe-core at 320–1280px, menu open and form errors showing; keyboard; 200% zoom and text spacing; reduced motion and high-contrast mode | /accessibility/#what-we-checked | Testing claims | accessibility-audit.md, Automated and Manual sections (Prompt 21) and Keyboard section (Prompt 15) | Keep | |
| “None known as of September 29, 2026. So far we’ve tested in Chrome-based browsers, not yet with a screen reader.” | /accessibility/#limitations | Limitations | Every manual criterion passes or was fixed; screen-reader pass is an owner action (compliance log #21) | Keep; update after the screen-reader pass | |
| “We typically reply within 1 business day” | /accessibility/#report | Reply time | Owner, 2026-09-29 (business-facts) | Keep | |
| “every page also has a plain-text version: add .md to the page’s name”, with links to /privacy.md, /index.md and /llms.txt | /accessibility/#report | Must stay true for every page | Mirrors generated by `tools/build_markdown.py`; `check_site.py` `markdown-mirrors` fails if a page has none or it’s stale | Keep | |
| “This site relies on HTML and CSS. JavaScript is optional” | /accessibility/#technologies | Technical fact | Without JavaScript the nav links wrap under the logo and the form posts with native validation (main.js header comment, Prompt 15 test) | Keep | |

## Puffery (no substantiation needed)

| Wording | Location |
|---------|----------|
| “Websites done fast. Websites done right.” | / headline, title, og, every footer tagline, og:image alt |
| “affordable technology solutions”, “Affordable website creation…” | / lead, meta, og, JSON-LD description; /our-story/ |
| “We focus on quality and customer satisfaction.” | / New Websites |
| “Custom-built websites to your specifications.” | / New Websites |
| “we are here to help”, “we’re here to help” | / lead and Start Your Project |
| “Let’s Upgrade Your Business.” | /contact/ headline |
| “That’s how we work.” | /solutions/ Every Project Includes |

## Claims added by /refunds/ (Prompt 03, 2026-09-29)

| Claim | Location | Issue | Evidence / owner confirmation | Decision | New wording |
|-------|----------|-------|-------------------------------|----------|-------------|
| Full refund if a project ends before work starts; pro-rated for work done mid-project, explained by email | /refunds/ summary table, #before-work-starts, #during-a-project; /terms/#termination | Refund promise | Owner, 2026-09-29 (business-facts, Scope, guarantee and refunds) | Keep | |
| After delivery, refund of the unfixable part within 30 days (Launch and Rescue); none for the one-time fix | /refunds/ summary table, #after-delivery; /terms/#fixes | Refund promise | Owner, 2026-09-29 (Prompt 03) | Keep | |
| A late rush is charged at the normal price, taken off the second payment (Tier 1 example: $187.50 deposit, $62.50 second payment) | /refunds/#rush-orders, #if-we-miss-a-promise; /terms/#payment | Rush remedy | Owner, 2026-09-29 (business-facts, Service area and hours); arithmetic from the 50/50 split | Keep | |
| Anything paid above the accepted quote is refunded | /refunds/#if-we-miss-a-promise; /terms/#completion-guarantee | Guarantee remedy | Follows from the completion guarantee (business-facts) | Keep; attorney to confirm | |
| Refund sent within 5 business days to the same Venmo or bank account; reply within 1 business day | /refunds/#timing, #chargebacks | Time promise | Owner, 2026-09-29 (Prompt 03); reply time from business-facts | Keep | |
