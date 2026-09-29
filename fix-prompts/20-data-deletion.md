# Prompt 20: Data deletion requests

````text
<branch>
Do all work on the git branch claude-fix-plan. Before changing anything, run git fetch origin claude-fix-plan, check the branch out, and pull, so you start from the commit the previous prompt pushed. Commit and push only to claude-fix-plan. This is explicit permission to use it instead of the session's default branch. Leave main unchanged.
</branch>

<context>
Contact form data lives in several places:
- Netlify Forms, including the Spam tab;
- the notification emails Netlify sends to the inbox;
- reply threads;
- notes and project files.

A deletion promise that misses any of these is a deceptive claim. Invoices must be kept for the retention period in docs/legal-compliance.md, and the policy has to say so. docs/ux-honesty-rules.md requires that deleting data be as easy as sending it. /privacy/#your-rights exists from Prompt 01.
</context>

<inputs>
docs/business-facts.md, docs/data-inventory.md, docs/third-parties.md, docs/legal-compliance.md, docs/compliance-log.md, public/privacy/index.html
</inputs>

<deliverables>
1. /privacy/#your-rights covering:
   - the rights: copy, correction, deletion, and stopping marketing;
   - a link with the text "Email a data request" pointing to mailto:info@tech-savvies.com?subject=Data%20request;
   - verification by reply to the address on file, with no ID documents for simple requests;
   - what's deleted, and what's kept (invoices, for the documented period);
   - acknowledgement within N business days and completion within the period docs/legal-compliance.md supports;
   - no charge and no different treatment;
   - how a parent or an authorised agent makes a request.
   The #summary bullet about rights links to #your-rights.
2. docs/data-requests-runbook.md, with each vendor step checked against current vendor docs and the URLs cited, covering:
   - logging (date and request type, in a private tracker outside the repo);
   - acknowledgement;
   - verification;
   - where to search: Netlify → Forms → contact, including Spam; inbox, archive, sent and trash; notes and project folders; client accounts we manage; vendors in docs/third-parties.md;
   - deletion, with the Netlify API DELETE /api/v1/submissions/{id} as an option and no tokens in the repo;
   - what to keep;
   - confirmation;
   - access-request export;
   - a deadlines table;
   - 4 email templates (acknowledgement, verification, completion, records we must keep), each at most 80 words.
3. A link to the runbook from the "Retention routine" in docs/data-inventory.md.
4. A check in tools/check_site.py: /privacy/ contains id="your-rights" and a mailto link whose subject contains "request".
5. Item 20 updated in docs/compliance-log.md.
6. One commit, "Fix #20: add data request process and deletion runbook", pushed.
7. A final message of at most 5 bullets.
</deliverables>

<constraints>
- Take N and the retention periods from the input docs. If a period isn't settled, write "as required by law (see accountant)" rather than a number.
- Keep personal details and request logs out of the repo.
- Leave p#form-privacy unchanged. It already links to /privacy/.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- The "Email a data request" link's href equals mailto:info@tech-savvies.com?subject=Data%20request, and it shows visible keyboard focus.
</acceptance_criteria>

<if_uncertain>
Mark a vendor step "unverified: confirm in <vendor> UI" in the runbook when its docs don't describe the step.
</if_uncertain>

<task>
Give visitors a one-email way to request access to or deletion of their data, and give the owner a runbook that completes each request everywhere the data is stored.
</task>
````

## Assumptions
- Prompts 07, 08, 24, 01 and 17 have run.

## Parameters
- Model: sonnet.
- Reasoning effort: medium.

## What to test
- Each place listed in `docs/data-inventory.md` appears as a search location in the runbook.
- Run with the invoice retention period missing from `docs/legal-compliance.md`. The page should say "as required by law", not give a number.
