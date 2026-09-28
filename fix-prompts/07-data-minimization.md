# Prompt 07: Only collect necessary data

Phase 1 (after 05). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md`, `docs/compliance-log.md`,
`docs/third-parties.md` and `docs/legal-compliance.md`.

## Goal

Make sure the site and business collect only the personal data they need, keep it only as long
as needed, and document every piece of it in `docs/data-inventory.md`. The Privacy Policy and
the deletion runbook will be built from that inventory.

## Why

Data minimisation is a core privacy principle (GDPR Art. 5(1)(c), the FTC's data-security
guidance, and NY SHIELD's "reasonable safeguards"). Data you don't collect can't leak and
doesn't need deleting. The contact form (`public/contact/index.html:71-105`) is already lean:

| Field | Required | Needed? |
|-------|----------|---------|
| `name` | yes | Yes, to address the reply |
| `email` | yes | Yes, to reply |
| `business` (business or current website) | no | Useful for quoting; already optional |
| `service` | yes | Routes the enquiry; has a "Not sure yet" escape hatch |
| `message` | yes | Yes |
| `bot-field` (honeypot) | hidden | Spam protection without a CAPTCHA vendor |

The gaps are outside the form: there is no retention period, and Netlify Forms stores more than
the visible fields. It keeps technical metadata (verify exactly what in `docs/third-parties.md`)
and emails a copy of every submission to an inbox.

## Task

1. **Review each field.** Confirm the table above, or argue for a change. Specifically:
   - Should `service` stay required? Keep it if "Not sure yet" makes it non-blocking. Otherwise
     make it optional.
   - Is `autocomplete="organization"` right for a field that may hold a URL? Keep it unless you
     find a concrete autofill problem.
   - Don't add fields such as phone, budget or date of birth. Prompt 17 deliberately avoids an
     age field.

2. **Check for hidden collection.** No query-string capture, no hidden fields besides
   `form-name` and the honeypot, no echo of submitted data on `/contact/thanks/`, and the form
   `method="POST"` over HTTPS (Netlify serves HTTPS; confirm the production site redirects HTTP
   to HTTPS if reachable).

3. **Retention.** Read the retention answer in `docs/business-facts.md`. If it's missing, ask the
   owner with `AskUserQuestion`, offering these options:
   - enquiries that don't become projects are deleted after 12 months (recommended);
   - after 6 months;
   - after 24 months.

   Client project records are kept for the engagement plus whatever tax and record-keeping law
   requires. Take that period from `docs/legal-compliance.md`, and don't invent a number.

   Record the answer. Then write a short "Retention routine" section in the inventory: how often
   (for example, the first Monday of each quarter), where to delete (Netlify → Forms → contact,
   including the Spam tab; the notification emails in the inbox; sent replies), and who does it.

4. **Write `docs/data-inventory.md`**: a table with `Data`, `Source`, `Purpose`, `Legal basis`
   (for EU/UK visitors; plain words otherwise), `Where stored` (Netlify Forms, inbox, invoices,
   project files), `Who can access`, `Retention`, `How to delete`. Include the Netlify metadata
   and the email copies. Link to `docs/third-parties.md` for vendor details.

5. **Apply field changes, if any.** Edit `public/contact/index.html` using the existing markup
   patterns (`.field`, `.optional`). Keep labels explicit and the `autocomplete` values valid.

6. Update item 7 in `docs/compliance-log.md`, and write the retention rule into
   `docs/business-facts.md`.

## Constraints

- Don't write the Privacy Policy here (that's Prompt 01). This prompt produces its input.
- Don't set up automated deletion scripts that need Netlify API tokens in the repo. Document the
  manual routine and mention the Netlify API as an option, with no secrets.

## Verify

- `python3 tools/check_site.py` passes.
- If the form changed: Playwright check at 375px and 1280px that it renders and that native
  validation still blocks an empty submit.

## Commit

`Fix #07: document collected data, set retention, confirm form minimality`. Push to the current
branch.
