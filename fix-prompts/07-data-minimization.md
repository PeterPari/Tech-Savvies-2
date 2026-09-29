# Prompt 07: Only collect necessary data

````text
<branch>
Do all work on the git branch claude-fix-plan. Before changing anything, run git fetch origin claude-fix-plan, check the branch out, and pull, so you start from the commit the previous prompt pushed. Commit and push only to claude-fix-plan. This is explicit permission to use it instead of the session's default branch. Leave main unchanged.
</branch>

<context>
The contact form (public/contact/index.html:70-109) collects:

| Field | Required | Assessment |
|-------|----------|-----------|
| name | yes | Needed to address the reply |
| email | yes | Needed to reply |
| business ("Business or current website") | no | Useful for quoting |
| service (select) | yes | Routes the enquiry; "Not sure yet" option exists |
| message | yes | Needed |
| bot-field | hidden | Honeypot, used instead of a CAPTCHA vendor |

Gaps outside the form:
- no retention period;
- Netlify Forms stores technical metadata alongside the fields (see docs/third-parties.md);
- Netlify emails a copy of every submission to the inbox.

The Privacy Policy (Prompt 01) and the deletion runbook (Prompt 20) are built from the inventory this prompt writes.
</context>

<inputs>
docs/business-facts.md, docs/third-parties.md, docs/legal-compliance.md, docs/compliance-log.md, public/contact/index.html, public/contact/thanks/index.html
</inputs>

<deliverables>
1. docs/data-inventory.md, containing:
   - a table with the columns Data | Source | Purpose | Legal basis (EU/UK terms plus plain words) | Where stored (Netlify Forms, inbox, invoices, project files) | Who can access | Retention | How to delete. It covers the form fields, the Netlify metadata, the email copies, and client project records;
   - a "Retention routine" section: the schedule (for example the first Monday of each quarter), each place to delete from (including Netlify's Spam submissions tab), and who does it.
2. A decision for each form field (keep / make optional / remove), with one line of justification, recorded in the inventory. Apply any change to public/contact/index.html using the existing .field and .optional markup.
3. The retention rule written into docs/business-facts.md, and item 7 updated in docs/compliance-log.md.
4. One commit, "Fix #07: document collected data and set retention", pushed.
5. A final message of at most 6 bullets.
</deliverables>

<constraints>
- Add no fields. Prompt 17 deliberately avoids an age field.
- Take the retention period for non-converted enquiries from docs/business-facts.md. If it's missing, ask the owner with the options 6 / 12 (recommended) / 24 months.
- Take the retention period for client records from docs/legal-compliance.md, and write "per accountant" if it isn't settled there.
- Document deletion as a manual routine, and mention the Netlify API as an option. Keep API tokens and scripts that need them out of the repo.
- Leave the Privacy Policy to Prompt 01.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- The form still posts with method="POST", has no hidden fields other than form-name and bot-field, and /contact/thanks/ shows no submitted data.
- If the form changed, it renders correctly at 375px and 1280px, and an empty submit is still blocked.
</acceptance_criteria>

<if_uncertain>
Mark any metadata field that Netlify's docs don't confirm as "unverified" in the inventory.
</if_uncertain>

<task>
Record every piece of personal data Tech-Savvies collects in docs/data-inventory.md, with a retention period, and remove any collection that isn't needed.
</task>
````

## Assumptions
- Prompts 08, 23 and 05 have run.

## Parameters
- Model: sonnet.
- Reasoning effort: medium.

## What to test
- Every row in the inventory has a retention value and a deletion method.
- Run with the retention fact missing. The session should ask using the three options, not choose one itself.
