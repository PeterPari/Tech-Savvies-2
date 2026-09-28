# Prompt 02: Terms of Service

````text
<context>
/solutions/ sells services with prices and promises, but nothing defines the terms: completion guarantee, monthly plan, rush orders, domain setup. The Terms must match /solutions/ and docs/business-facts.md exactly. Relevant law, detailed in docs/legal-compliance.md:
- NY GBL §527-a: auto-renewal disclosure and cancellation for the monthly plan;
- FTC Act §5 and NY GBL §349: the "completion guarantee" and "no surprise invoices" promises need concrete meaning;
- NY GOL §3-101: minors can void contracts.

/privacy/ provides the page template, the .prose styles and the footer Legal column. Prompt 10 left the comment <!-- links to /terms/ and /refunds/ added by prompts 02/03 --> in the /solutions/ Payment block.
</context>

<inputs>
docs/business-facts.md, docs/legal-compliance.md, docs/claims-register.md, docs/ux-honesty-rules.md, docs/compliance-log.md, public/solutions/index.html, public/privacy/index.html (template)
</inputs>

<deliverables>
1. public/terms/index.html:
   - title "Terms of Service | Tech-Savvies", a unique description, canonical, og tags, "Last updated <time>";
   - article.prose with one h2 per section, ids as listed:
     - #about: parties (legal name, dba, address, email) and when the Terms apply;
     - #website: content is information only; prices can change but an accepted quote won't; links aren't endorsements;
     - #quotes: work starts after a written quote (email counts) is accepted; out-of-scope work is quoted and agreed before it's done;
     - #payment: tiers, rush, deposit, due dates, methods, sales tax, exactly as on /solutions/;
     - #timelines: estimates depend on receiving content and feedback;
     - #revisions: rounds included, and what one round is;
     - #completion-guarantee: the owner's definition, in words identical to /solutions/;
     - #client-responsibilities: accurate content, rights to supplied material, timely feedback;
     - #third-party-costs: who registers the domain and in whose name, who pays renewals, vendors' own terms;
     - #ownership: the client owns the final deliverables on full payment; we keep pre-existing tools under a licence; portfolio use per the owner's preference;
     - #monthly-plan: price, inclusions, billing date, "renews automatically each month until you cancel", cancellation by the same channel as sign-up, when cancellation takes effect, no fee, partial-month rule, price-change notice period;
     - #results: no guarantee of rankings, traffic, followers or sales;
     - #fixes: free bug fixes within N days of launch, if the owner provides N;
     - #liability: a cap of fees paid, and an exclusion of indirect loss "to the extent the law allows";
     - #age: 18 or older, or a parent or guardian agrees and acts as the client;
     - #termination: either side may end a project; payment for work done; file handover;
     - #law: contact us first, with a stated response time; New York law; courts of the county in docs/business-facts.md;
     - #changes;
     - #contact.
2. "Terms of Service" as the first entry in the footer Legal column on every HTML page.
3. The Prompt 10 comment on /solutions/ replaced with "See our Terms of Service for full details." (underlined in-text link), and the completion guarantee wording identical on both pages.
4. A check named terms-consistency in tools/check_site.py: each .price-amount string on /solutions/ appears in /terms/, or /terms/#payment links to /solutions/. Pick one rule and state it in the check's comment.
5. /terms/ added to the sitemap, the README, and REQUIRED_FOOTER_LINKS. Item 2 updated in docs/compliance-log.md, with #monthly-plan, #liability and #law flagged for attorney review.
6. One commit, "Fix #02: add terms of service matching published prices and promises", pushed.
7. A final message of at most 8 bullets, including a two-column list of each price or promise on /solutions/ beside its clause in /terms/.
</deliverables>

<constraints>
- If /solutions/ still has an unpriced "monthly" plan or banned claims, stop and report that Prompts 10 and 12 must run first.
- Take every number and term from docs/business-facts.md, and ask the owner for missing ones. Drop #fixes if no N is given.
- Leave out mandatory arbitration and class-action waivers. Note in the compliance log that an attorney can advise on them.
- If docs/business-facts.md says the person signing for Tech-Savvies is under 18, keep that off the site. Report in the final message that a parent or guardian should co-sign and an attorney should confirm the arrangement.
- Writing level: Flesch-Kincaid grade 9 or lower, average sentence length at most 22 words.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- /terms/ renders without overflow at 375px and 1280px, and focus is visible on every link.
</acceptance_criteria>

<if_uncertain>
Where the law's requirement for a clause is unclear in docs/legal-compliance.md, write the plainest fair version, and flag the clause for attorney review in the compliance log.
</if_uncertain>

<task>
Publish /terms/, Terms of Service for website use and for Tech-Savvies projects and the monthly plan, consistent with every price and promise on /solutions/.
</task>
````

## Assumptions
- Prompts 10, 12, 01 and 04 have run.
- An attorney will review the page before anyone relies on it.

## Parameters
- Reasoning effort: high.

## What to test
- Compare the price and promise table in the final message with `/solutions/` by hand.
- Run with `/solutions/` still containing "lead engineer". The session should stop.
- Set the signer age fact to "under 18". There should be no site change and an owner action in the final message.
