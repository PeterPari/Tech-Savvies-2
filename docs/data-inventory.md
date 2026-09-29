# Data inventory

Every piece of personal data Tech-Savvies collects, why, where it sits and when it goes. The
Privacy Policy (Prompt 01) and the deletion runbook (Prompt 20) are built from this file. Facts come
from [`business-facts.md`](business-facts.md) and [`third-parties.md`](third-parties.md). Not legal advice.

Legal basis uses EU/UK terms with plain words. The owner is not deliberately serving EU/UK clients
(business-facts, 2026-09-29), so these terms are a labelling aid, not a claim that GDPR applies.
"unverified" means Netlify’s docs don’t confirm it.

## Inventory

| Data | Source | Purpose | Legal basis | Where stored | Who can access | Retention | How to delete |
|------|--------|---------|-------------|--------------|----------------|-----------|---------------|
| Name | Contact form | Address the reply | Legitimate interests (Art. 6(1)(f)): answering someone who wrote to us; or steps before a contract (6(1)(b)) | Netlify Forms; inbox copy (iCloud) | Owner; Netlify and Apple as processors | Non-converted enquiry: 6 months. Converted client: see client records | Netlify → Site → Forms → Verified submissions → tick → Delete submission; delete the email in iCloud, then empty Trash |
| Email address | Contact form | Reply, quote | Same as name | Netlify Forms; inbox copy | Same | Same | Same |
| Business or current website (optional) | Contact form | Scope and quote the work | Same as name | Netlify Forms; inbox copy | Same | Same | Same |
| Service wanted | Contact form (select) | Route the enquiry | Same as name | Netlify Forms; inbox copy | Same | Same | Same |
| Message | Contact form | Understand the request | Same as name | Netlify Forms; inbox copy | Same | Same | Same |
| Honeypot `bot-field` | Contact form (hidden) | Block bots, no CAPTCHA vendor | Legitimate interests: keeping the form usable | Not stored: a filled honeypot is quietly rejected and not listed as spam (Netlify docs) | Nobody | None | Nothing to delete |
| IP address (`data.ip`) and created-at time | Netlify, on submit | Netlify’s own record of the submission | Legitimate interests: security and abuse handling | Netlify Forms, with the submission | Owner (dashboard and API); Netlify | Deleted with the submission: 6 months | Delete the submission (as above) |
| User agent, referrer on submissions | Netlify | Not documented as stored | Legitimate interests | Netlify Forms: **unverified** | Owner; Netlify | Deleted with the submission | Delete the submission |
| Spam-tab submissions | Netlify (Akismet or honeypot flagged) | Kept for review of false positives | Legitimate interests | Netlify Forms → Spam submissions. Akismet is on, plus the honeypot (owner checked the dashboard, 2026-09-29). Which fields Akismet receives: **unverified** | Owner; Netlify; Akismet (**unverified**) | 6 months, same routine | Netlify → Forms → Spam submissions → delete (or "Delete all spam") |
| Notification email copy of each submission | Netlify (from formresponses@netlify.com) | Alert the owner | Legitimate interests | iCloud Mail, info@tech-savvies.com | Owner; Apple | 12 months (owner rule for all emails). See the gap under "Retention routine" | Delete in iCloud; Trash keeps 30 days unless emptied |
| Emails with leads and clients | Direct email | Correspondence | Steps before a contract / contract (6(1)(b)) | iCloud Mail | Owner; Apple | 12 months | Delete in iCloud, empty Trash |
| Client project records: contact details, invoices, payment records (Venmo, bank transfer) | Client, payment apps | Deliver the work, get paid, keep tax records | Contract (6(1)(b)); legal obligation (6(1)(c)) for invoices and tax records | Invoices folder, payment apps, project files | Owner; payment providers | Per accountant (legal-compliance.md cites 3 years as a floor; not settled) | Delete the folder or file once the period ends; ask the payment provider for its own records if needed |
| Client project records: site files, content, and account access (Google Business Profile manager role, social media, logins some clients share) | Client | Do the work | Contract | Project files; client’s own accounts (a manager role is removed by the client or by the owner on request) | Owner | Per accountant for the records. Shared passwords: kept in a password manager and deleted when the work ends (owner, 2026-09-29). Manager roles: the client removes them, or the owner on request | Remove manager role; delete files and stored logins; confirm to the client |

## Decision per form field

| Field | Decision | Why |
|-------|----------|-----|
| name | Keep (required) | Needed to address the reply |
| email | Keep (required) | Needed to reply |
| business | Keep, already optional | Helps quoting and is not required |
| service | Keep (required) | Routes the enquiry; "Not sure yet" avoids forcing a guess |
| message | Keep (required) | The enquiry itself |
| bot-field | Keep (hidden honeypot) | Stops bots without a CAPTCHA vendor and stores nothing |

No field was added, removed or changed, so `public/contact/index.html` is unchanged. The thanks page
(`/contact/thanks/`) shows no submitted data.

## Minors

Applies when an enquirer says, or the message shows, that they are under 18 or under 13. No age is ever
asked for: the contact form has no age or birth-date field, and the `no-age-fields` check keeps it that way.

1. Reply once, asking them to have a parent or guardian contact info@tech-savvies.com. Say nothing else
   about the project and quote no price.
2. Collect nothing more. Use the minor’s name and email only to send that reply and to reach the parent or
   guardian. Don’t add them to any list or use the details for anything else.
3. If a parent or guardian follows up, they become the client (Terms #age) and the record moves under
   client records.
4. If none does, delete the Netlify submission (Verified and Spam tabs), the notification email and the
   sent reply within 30 days of learning the person is a minor (business-facts, 2026-09-29). Empty the
   iCloud Trash.
5. A parent or guardian who asks for deletion, or data found from a child under 13: delete within the same
   30 days and don’t use it. Confirm by email.
6. Note the date and outcome in the log below without the child’s name.

| Date | Action | Deleted by |
|------|--------|------------|

## Retention routine

For a request from a person, follow [`data-requests-runbook.md`](data-requests-runbook.md).

- **Rule:** form submissions 6 months; emails 12 months (owner, 2026-09-29); client records per accountant.
- **Schedule:** first Monday of each quarter (January, April, July, October).
- **Who:** the owner, Peter Parizhsky. Tick the run in the log below.
- **Steps, all manual:**
  1. Netlify → Site → Forms → **Verified submissions**: delete anything older than 6 months, unless it became a client (keep it under client records).
  2. Netlify → Forms → **Spam submissions** tab: delete everything older than 6 months.
  3. iCloud Mail (info@tech-savvies.com): delete mail older than 12 months, then empty Trash.
  4. Client records: delete what the accountant’s period no longer requires.
  5. Note the date here.
- **Known gap:** a notification email is kept up to 12 months while the Netlify copy goes at 6. To match, delete
  form notification emails from non-clients at step 3 after 6 months. Owner to confirm.
- **Option:** Netlify’s API (`DELETE /api/v1/submissions/{submission_id}`) could automate step 1 and 2. Tokens
  and scripts that use them stay out of this repo. Manual is the documented routine.

| Date run | Done by | Notes |
|----------|---------|-------|
|  |  |  |
