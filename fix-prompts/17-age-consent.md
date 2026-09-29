# Prompt 17: Age consent for kids' data

````text
<context>
Three rules shape this:
- COPPA applies to sites directed to children under 13, or with actual knowledge of collecting their data. This site is aimed at businesses.
- The NY Child Data Protection Act's scope for a general-audience site is recorded in docs/legal-compliance.md.
- Minors can void contracts in NY (GOL §3-101), and a teenage artist could fill in the form.

Asking every visitor for a birth date would collect unneeded data. An "I'm over 18" checkbox adds friction and gives no real assurance. So the control is written statements plus a process, with no age field.

Existing pieces:
- /privacy/#children (Prompt 01);
- /terms/#age (Prompt 02);
- the form notice p#form-privacy (Prompt 06).
</context>

<inputs>
docs/business-facts.md, docs/legal-compliance.md, docs/data-inventory.md, docs/compliance-log.md, public/privacy/index.html, public/terms/index.html, public/contact/index.html
</inputs>

<deliverables>
1. /privacy/#children stating:
   - the service isn't directed to under-13s;
   - we don't knowingly collect their data;
   - parents can email us, and we delete the data within the timeframe in docs/business-facts.md;
   - discovered data is deleted and not used;
   - under-18s should have a parent or guardian contact us, and a minor's details are used only to reply and to reach that parent or guardian.
   The wording is consistent with the NY CDPA finding.
2. /terms/#age: "To hire us you must be 18 or older. If you're under 18, a parent or guardian must agree to these Terms and will be our client for the project, including payment."
3. One sentence added to p#form-privacy, of at most 12 words, for example "Under 18? Please ask a parent or guardian to contact us." The whole notice stays at 3 sentences or fewer.
4. A "Minors" section in docs/data-inventory.md: reply once asking for a parent or guardian, collect nothing more, and delete within the stated timeframe if no parent or guardian follows up.
5. A check named no-age-fields in tools/check_site.py: fails when an input name or id matches dob|birth|birthday|\bage\b.
6. Item 17 updated in docs/compliance-log.md.
7. One commit, "Fix #17: add children's data and under-18 client rules", pushed.
8. A final message of at most 5 bullets.
</deliverables>

<constraints>
- Add no age, birth-date or age-confirmation field.
- If docs/business-facts.md says the person signing client contracts for Tech-Savvies is under 18, keep that off the site. Record an owner action to get attorney advice on parent or guardian co-signing, in docs/compliance-log.md and docs/legal-compliance.md.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- The form notice renders on at most 4 lines at 375px.
</acceptance_criteria>

<task>
Add children's and under-18 data rules to the Privacy Policy, Terms and contact form notice, without collecting anyone's age.
</task>
````

## Assumptions
- Prompts 01, 02 and 06 have run.

## Parameters
- Model: sonnet.
- Reasoning effort: medium.

## What to test
- A seeded `<input name="dob">` fails the checker.
- The form notice at 375px fits in 4 lines or fewer.
- Set the signer age fact to "under 18". There should be no site change and an owner action in both docs.
