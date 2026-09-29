# Prompt 24: Check local laws (compliance map)

````text
<context>
Tech-Savvies is a one-person web-design business in New York City. It sells website builds, website repairs, and Google Business Profile and social media help, with prices on /solutions/, including a monthly management plan. It collects enquiries through a Netlify contact form. The Privacy Policy, Terms, Refund Policy, email policy and accessibility statement will all be written against the map this prompt produces.

Laws to assess:
- FTC Act §5; FTC Rule on Consumer Reviews and Testimonials (16 CFR 465); FTC Endorsement Guides (16 CFR 255); current legal status of the FTC negative-option ("click-to-cancel") rule.
- NY GBL §349/§350; NY GBL §527-a (automatic renewal); NY GBL §130 (assumed name); NY GBL §218-a (refund policy posting; confirm whether it covers services); NY SHIELD Act (GBL §899-aa/bb); NY Child Data Protection Act; NY General Obligations Law §3-101 (minors' contracts).
- CalOPPA (Cal. Bus. & Prof. Code §22575–22579); CCPA/CPRA and other US state privacy law thresholds; GDPR/UK GDPR (only if docs/business-facts.md says EU/UK clients are targeted); COPPA; CAN-SPAM.
- ADA Title III, NY State Human Rights Law, NYC Human Rights Law (website accessibility).
- NY sales tax guidance on web design, hosting and domain resale; NYC consumer protection rules on service pricing; record-retention periods for invoices and tax records.
</context>

<inputs>
docs/business-facts.md, docs/compliance-log.md
</inputs>

<deliverables>
1. docs/legal-compliance.md, containing:
   - a one-line "Not legal advice" note;
   - a summary of at most 150 words;
   - a table with the columns Law | Applies? (Yes / No / Only if …) | Why | Requirement (quoted from the source, at most 40 words) | Handled by (prompt # and page) | Source URL | Checked (date). One row per law above;
   - "Owner actions outside the website": DBA filing, attorney review of Terms, Refunds and Privacy, accountant review of sales tax, and parent/guardian co-signing if docs/business-facts.md says the contract signer is under 18.
2. A note under fix-plan.md §2 for any finding that contradicts a decision there, also reported in the final message.
3. Item 24 updated in docs/compliance-log.md.
4. One commit, "Fix #24: add legal compliance map", pushed.
5. A final message of at most 8 bullets.
</deliverables>

<examples>
<example index="1">
| NY GBL §527-a | Yes | The monthly management plan renews each month | "clear and conspicuous" disclosure of the automatic renewal terms before purchase, plus an easy cancellation method | 02 /terms/#monthly-plan, 10 /solutions/ | https://… | 2026-… |
</example>
<example index="2">
| CCPA/CPRA | No | Below every threshold (revenue, record count, data-sale share) | n/a | n/a | https://… | 2026-… |
</example>
<example index="3">
| GDPR | Only if EU clients are deliberately targeted | docs/business-facts.md says they aren't | n/a unless that changes | 01 /privacy/#international | https://… | 2026-… |
</example>
</examples>

<constraints>
- Take every requirement, threshold, effective date and legal status from a primary or official source fetched in this session (statute text, ftc.gov, ag.ny.gov, dos.ny.gov, tax.ny.gov, ada.gov, oag.ca.gov). If you can't fetch one, say so in that row rather than filling it from memory.
- Don't draw tax conclusions. Link the guidance and route the question to an accountant.
- Leave public/ unchanged.
- Leave the owner's personal details out, unless they're already in docs/business-facts.md.
</constraints>

<final_pass>
When the user's message says "final pass", do this instead of the deliverables above. For each "Handled by" entry, open the page in public/ and quote the clause or feature that satisfies the requirement. Add a "Final pass (date)" section listing each entry as met or gap. Fix gaps that need at most 3 lines of copy. Refresh any source whose checked date is more than 6 months old. Commit as "Fix #24: final compliance pass".
</final_pass>

<if_uncertain>
Write "Unclear; ask an attorney" in the Applies? column when the source doesn't settle whether the law applies.
</if_uncertain>

<task>
Write docs/legal-compliance.md, mapping each law listed above to whether it applies to Tech-Savvies, what it requires, and which prompt and page handles it.
</task>
````

## Assumptions
- Run in Phase 1, right after Prompt 00, and again with "final pass" added after every other prompt.
- WebSearch and WebFetch can reach official government sites from the session.

## Parameters
- Model: opus.
- Reasoning effort: high. Applicability depends on reading statutes against facts.
- Temperature: default.

## What to test
- Check 3 rows by hand against their sources: §527-a, CalOPPA, and the FTC negative-option rule's status.
- Run once with EU clients set to "no" and once set to "yes" in the facts file. The GDPR row and the Privacy Policy "Handled by" entry should change.
- In the final-pass run, every "met" entry should quote actual page text.
