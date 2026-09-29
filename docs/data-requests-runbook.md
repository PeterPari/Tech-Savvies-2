# Data requests runbook

How the owner (Peter Parizhsky) completes a request from `/privacy/#your-rights` to see, correct or
delete personal data, or to stop marketing. Not legal advice. Facts come from
[`business-facts.md`](business-facts.md), [`data-inventory.md`](data-inventory.md),
[`third-parties.md`](third-parties.md) and [`legal-compliance.md`](legal-compliance.md).

Vendor steps were checked against the vendor docs on 2026-09-29. A step marked "unverified: confirm in
<vendor> UI" is one the docs don’t describe.

## Deadlines

| Step | Deadline | Basis |
|------|----------|-------|
| Acknowledge | Within 1 business day of the email | Reply time in business-facts.md; promised on /privacy/#your-rights |
| Verify | Ask in the acknowledgement; the clock keeps running | Same |
| Complete (copy, correction, deletion, marketing stop) | Within 10 business days of the email | The only period in legal-compliance.md (CAN-SPAM opt-outs, “within 10 business days”), used for every request |
| Child’s or minor’s data, parent or guardian request | Within 30 days at most | business-facts.md, /privacy/#children |
| Invoices and payment records | Kept as required by law (see accountant), then deleted | legal-compliance.md; period not settled |

If a request can’t be finished in time, write to the person before the deadline and say why and when.

## 1. Log it

Record the date received, the request type (copy, correction, deletion, marketing stop) and the dates
you acknowledged and finished. Use a private tracker outside the repo, such as a password-protected
sheet. Don’t put names, email addresses or request details in this repo, and don’t log more than
dates, type and outcome.

## 2. Acknowledge

Send template A the same business day.

## 3. Verify

Reply to the email address on file for the person (the address on their form message or earlier emails),
not to a different address in the request. Send template B. A reply from that address is enough for
simple requests. Don’t ask for ID documents. If you have no address on file, ask them to write from
the address they used with us.

- **Parent or guardian:** for a child’s data, confirm by reply from the parent’s address and with the details of the child’s original message.
- **Authorised agent:** they write from their own address, with the person’s written permission. Also confirm with the person at the address on file before acting.

## 4. Search everywhere

Search for the person’s name, email address and business name in each place. Note where you found
data in the private tracker.

1. **Netlify Forms.** Netlify → Site → Forms → `contact`. Check **Verified submissions**, then switch to **Spam submissions** with the menu above the list. Search or read each list. Source: https://docs.netlify.com/manage/forms/submissions/
2. **Inbox (iCloud Mail, info@tech-savvies.com).** Search Inbox, Archive, Sent, Trash and Junk, including form notification emails from formresponses@netlify.com and reply threads. Source: https://support.apple.com/guide/icloud/welcome/icloud. That guide doesn’t describe searching across all folders: unverified: confirm in iCloud Mail UI that the search covers every folder.
3. **Notes and project folders.** The invoices folder, project files, meeting notes, and the password manager for shared logins.
4. **Client accounts we manage.** Google Business Profile, social media and any other account where we hold a manager role or a login for this person.
5. **Vendors in [`third-parties.md`](third-parties.md).** Netlify (hosting logs and Forms), iCloud Mail, Squarespace Domains II (registrant data), Claude and ChatGPT (the owner enters no enquiry or client personal details, per business-facts.md, so expect nothing), and Akismet, whose handling of form fields is unverified. Netlify’s hosting logs and analytics aren’t searchable by person; Netlify keeps service logs online 90 days and offline 1 year (https://www.netlify.com/pdf/netlify-dpa.pdf). For anything else at Netlify write to privacy@netlify.com.

## 5. Copy (access request)

1. Netlify: open the `contact` form and select **Download as CSV** (https://docs.netlify.com/manage/forms/submissions/). The CSV holds every submission, so delete every other person’s row from your copy before you send anything.
2. Email: forward or export the person’s own messages. Don’t include other people’s data.
3. Client records: copy their contact details, invoices and project notes.
4. Send the collected material only to the verified address, in one reply. Say where the data sits and how long you keep it.

Correction: fix the data in each place found, and say what you changed. Marketing stop: we send none, so
say so, and note the person in the private tracker so they’re never added.

## 6. Delete

Delete everything found in step 4, except what step 7 says to keep.

- **Netlify dashboard:** in `contact`, tick each of the person’s submissions (both tabs), select the red **Delete submission** button and confirm. Deletion is permanent. Source: https://docs.netlify.com/manage/forms/submissions/
- **Netlify API (option):** `DELETE https://api.netlify.com/api/v1/submissions/{submission_id}` returns 204 on success and needs a Netlify personal access token in an `Authorization: Bearer` header. Source: https://open-api.netlify.com/ (operation `deleteSubmission`). Keep the token in your shell session or password manager. Never put a token, or a script that holds one, in this repo. The docs I read don’t say how to filter spam submissions through the API: unverified: confirm in Netlify UI.
- **Inbox:** delete every matching email, including form notifications, from Inbox, Archive, Sent and Junk, then empty Trash. Apple’s guide says the steps are in its “Delete email” article (https://support.apple.com/guide/icloud/welcome/icloud). third-parties.md says Trash keeps mail 30 days unless emptied; unverified: confirm in iCloud Mail UI.
- **Notes and project folders:** delete the files and notes; remove any stored login from the password manager.
- **Client accounts:** remove our manager role (or ask the client to), and note it.
- **Vendors:** for a registrant record, write to privacy@squarespace.com (the registration data must be kept while the domain is registered). For other vendors follow the “How to delete” column in third-parties.md.
- **Backups:** if any device or drive backs up the folders above, delete the person’s files from those copies at the next backup, and say so in the private tracker.

## 7. What to keep

Keep invoices and payment records (Venmo, bank transfer) for as long as the law requires (see
accountant). Keep them only for tax and accounting, and delete them when the period ends. The period
isn’t settled: legal-compliance.md cites 3 years as a floor. Once the accountant confirms it, record
it in business-facts.md. Also keep a minimal note in the private tracker (date, type, outcome, no
personal details) so we can show we did it. If you keep the person’s name or email on an invoice, use template D.

## 8. Confirm

Send template C to the verified address, listing where you deleted and what you kept. Mark the request
finished in the private tracker with the date.

## Email templates

Each is at most 80 words. Replace the bracketed parts before sending.

### A. Acknowledgement

> Subject: Re: Data request
>
> Hi [name],
>
> Thanks for your data request. We’ve got it and will finish it within 10 business days. There’s no charge. First we need to check it’s you; see our next email. If anything is unclear, reply here.
>
> Peter
> Tech-Savvies

### B. Verification

> Subject: Please confirm your data request
>
> Hi [name],
>
> To protect your data, please reply “Yes, this is me” to this email, from this address. Then we’ll [send you a copy / correct / delete] your data. We don’t need any ID. If someone else sent this request for you, reply “No” and we’ll stop.
>
> Peter
> Tech-Savvies

### C. Completion

> Subject: Your data request is done
>
> Hi [name],
>
> We’ve finished your request. We [sent you a copy / corrected / deleted] your data from our contact form records, email, notes and project files. [We kept: invoices and payment records, if any.] If you think we missed something, reply and we’ll check.
>
> Peter
> Tech-Savvies

### D. Records we must keep

> Subject: What we’re keeping
>
> Hi [name],
>
> We deleted your data except your invoices and payment records. The law requires us to keep those for tax purposes for as long as the law requires (see accountant). We use them only for that, and delete them when the period ends. Reply if you have questions.
>
> Peter
> Tech-Savvies
