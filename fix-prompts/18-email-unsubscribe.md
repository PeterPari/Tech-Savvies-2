# Prompt 18: Unsubscribe link in emails

````text
<context>
The website sends no email and has no newsletter signup. Netlify form notifications go to the owner, so there's no unsubscribe link to add in code. The risk is the owner's own email:
- CAN-SPAM covers any email whose primary purpose is commercial, including B2B follow-ups to leads. Such emails need an honest header and subject, identification as an ad where applicable, a valid postal address, and a working opt-out honoured within 10 business days at no cost.
- Transactional and relationship emails (enquiry replies, project updates, invoices) are largely exempt from the opt-out requirement.

/privacy/ and the form notice state the owner's email practice, and those statements must stay true.
</context>

<inputs>
docs/business-facts.md, docs/legal-compliance.md, docs/data-inventory.md, docs/tracking-audit.md, docs/compliance-log.md, public/privacy/index.html, public/contact/index.html
</inputs>

<deliverables>
1. docs/email-policy.md, containing:
   - a table of email types (enquiry reply, project update, invoice, follow-up offer, newsletter) with the columns Category (transactional/relationship or commercial) | Requirements;
   - rules for commercial email, each citing the FTC CAN-SPAM guide URL:
     - honest subject and from-name;
     - postal address;
     - clear opt-out;
     - honour it within 10 business days;
     - no fee or extra steps;
     - opt-out works for 30 days after sending;
     - never transfer opted-out addresses;
   - an EU/UK section (consent under PECR/GDPR), only if docs/business-facts.md says EU/UK recipients are emailed;
   - a suppression list kept outside the repo, checked before every promotional send;
   - an email-service section: physical address in settings, keep the built-in unsubscribe footer, double opt-in for any future signup form;
   - an open-tracking section based on docs/tracking-audit.md.
2. Two signatures in docs/email-policy.md, each in plain text and HTML:
   - Standard: name, Tech-Savvies, legal name if different, website, email.
   - Commercial: the standard signature plus the postal address, plus "Don't want emails like this? Reply 'unsubscribe' or email info@tech-savvies.com with the subject 'Unsubscribe', and we'll stop within 10 business days." The HTML version links mailto:info@tech-savvies.com?subject=Unsubscribe.
3. /privacy/ email statements and p#form-privacy updated only if they no longer match the owner's practice.
4. Item 18 updated in docs/compliance-log.md: "No website email; owner email policy and signatures documented".
5. One commit, "Fix #18: add email policy and unsubscribe-ready signatures", pushed.
6. A final message of at most 5 bullets.
</deliverables>

<constraints>
- Ask the owner in one AskUserQuestion call, skipping anything the facts already answer:
  - do you send or plan promotional emails;
  - from your inbox or from an email service;
  - do you email EU or UK recipients for marketing.
- Add no newsletter signup or email-service integration to the site. If the owner wants a marketing opt-in, point them to Prompt 06 deliverable 3.
- Keep email addresses and suppression lists out of the repo.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- The commercial signature contains the postal address from docs/business-facts.md and a mailto unsubscribe link.
</acceptance_criteria>

<if_uncertain>
If no postal address is confirmed, write "postal address required before sending commercial email" in the commercial signature, and list it as an owner action.
</if_uncertain>

<task>
Write docs/email-policy.md, classifying each kind of email Tech-Savvies sends and giving CAN-SPAM-compliant signatures with a working unsubscribe for commercial email.
</task>
````

## Assumptions
- Prompts 16, 23, 01 and 06 have run.
- The site has no newsletter, so there's nothing to change in its code.

## Parameters
- Reasoning effort: low.

## What to test
- Run with "sends follow-ups: yes". The `/privacy/` and form notice wording should change to match.
- Run with the address `TODO(owner)`. The signature should show the required-address note, not an invented address.
