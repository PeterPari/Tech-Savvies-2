# Prompt 18: Unsubscribe link in emails

Phase 3 (last). Paste everything below the line into a new Claude Code session opened at the
repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md` (email practices, mailing address),
`docs/legal-compliance.md` (the CAN-SPAM entry), `docs/data-inventory.md`, `/privacy/` and
`docs/compliance-log.md`.

## Goal

Make sure every email Tech-Savvies sends is lawful. Commercial or promotional emails need a
working opt-out and a postal address. Document what counts as what, give the owner ready-to-use
signatures, and make sure the site's promises about email match reality.

## Why

The website itself sends no email and has no newsletter signup. Netlify form notifications go to
the owner, not the visitor. So there's no unsubscribe link to add in the code. The risk lies in
how the owner emails leads and clients:
- **CAN-SPAM** covers any email whose main purpose is commercial, including B2B follow-ups such
  as "Checking in, want to book your site this month?". Those need a clear way to opt out,
  honoured within 10 business days, a valid physical postal address, a non-deceptive subject
  line and "from" name, and identification as an ad where applicable.
- **Transactional and relationship emails** (replying to an enquiry, project updates, invoices)
  are largely exempt from the opt-out requirement, but must not be deceptive.
- The Privacy Policy and the form notice promise "no mailing list without opt-in". That has to
  stay true.

Verify these requirements against the FTC's CAN-SPAM compliance guide with `WebFetch`, and cite
it in the doc.

## Task

1. **Confirm the owner's practice** (`AskUserQuestion`, skipping anything already in
   `docs/business-facts.md`):
   - Do you send, or plan to send, any promotional emails: follow-ups to people who didn't book,
     newsletters, offers?
   - If so, from your normal inbox or from an email service (Mailchimp, Buttondown, etc.)?
   - Do you email anyone in the EU or UK for marketing?

2. **Write `docs/email-policy.md`**:
   - **Email types table:** enquiry reply, project update, invoice, follow-up offer, newsletter.
     For each, give its category (transactional/relationship vs. commercial) and what it
     requires.
   - **Rules for commercial emails:**
     - honest subject and from-name;
     - postal address from `docs/business-facts.md` (PO box / private mailbox is OK);
     - a clear opt-out line;
     - honour opt-outs within 10 business days and never email that address commercially again;
     - no charge or extra steps to opt out;
     - opt-outs must work for at least 30 days after sending;
     - never sell or transfer opted-out addresses.
   - **EU/UK:** marketing needs prior consent (PECR/GDPR). Include this only if relevant.
   - **Suppression list:** keep it in a private place, off-repo. Say how to check it before any
     promotional send.
   - **If using an email service:** set the physical address in its settings, keep its built-in
     unsubscribe footer, and turn on double opt-in if a signup form is ever added. Any signup
     form must use an unticked optional checkbox (see `docs/ux-honesty-rules.md`) and needs its
     own Privacy Policy and data inventory update.
   - **Open-tracking:** if the owner uses read receipts or tracking pixels, the Privacy Policy
     must disclose it, or it should be turned off. Take the answer from `docs/tracking-audit.md`.

3. **Signature templates** in the same doc, in plain text and simple HTML:
   - **Standard** (all emails): name, "Tech-Savvies", legal name if different, website,
     `info@tech-savvies.com`.
   - **Commercial** (add to any promotional email): the standard signature plus the postal
     address, plus "Don't want emails like this? Reply 'unsubscribe' or email
     info@tech-savvies.com with the subject 'Unsubscribe', and we'll stop within 10 business
     days." Include a `mailto:info@tech-savvies.com?subject=Unsubscribe` link in the HTML version.

4. **Check the site's promises.** Re-read the `/privacy/` email statements and the contact form
   notice. If the owner does send follow-ups, update both to say so accurately, for example "We
   may follow up once about your enquiry. You can ask us to stop at any time." If the owner wants
   a marketing opt-in, point them to Prompt 06 step 5 rather than building it here.

5. Update item 18 in `docs/compliance-log.md` (status: "No website emails; owner email policy and
   signatures documented").

## Constraints

- Don't add a newsletter signup or email service integration.
- Don't commit anyone's email addresses or a suppression list.

## Verify

- `python3 tools/check_site.py` passes (only relevant if the policy or notice changed).
- Proofread the templates: they have a postal address and a working `mailto` unsubscribe.

## Commit

`Fix #18: add email policy with CAN-SPAM rules and unsubscribe-ready signatures`. Push to the
current branch.
