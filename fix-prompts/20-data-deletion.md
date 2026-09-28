# Prompt 20: Data deletion requests

Phase 3 (after 17). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md`, `docs/data-inventory.md`,
`docs/third-parties.md`, `docs/legal-compliance.md` (record-retention entry) and
`docs/compliance-log.md`. `/privacy/` must exist.

## Goal

Make it easy for anyone to ask Tech-Savvies to show, correct or delete their data. Give the
owner a step-by-step runbook so every request is actually completed in every place the data
lives.

## Why

A promise to delete that isn't carried out everywhere is a deceptive claim. Contact form data
doesn't live in one place: it sits in Netlify Forms (including the Spam tab), in the
notification email Netlify sends to the inbox, in replies, and possibly in notes and project
files. Some records, such as invoices, have to be kept for tax purposes, and the policy must say
so honestly instead of promising to delete everything. Easy deletion is also an honest-UI rule:
removing your data must be as easy as sending it (`docs/ux-honesty-rules.md`).

## Task

1. **Privacy Policy `#your-rights`** (`public/privacy/index.html`). Make sure it covers:
   - **what you can ask for:** a copy of your data, a correction, deletion, and to stop any
     marketing;
   - **how:** a prominent link, "Email a data request", as
     `mailto:info@tech-savvies.com?subject=Data%20request`, with a note to say what you want and
     to email from the same address you used before;
   - **verification:** we'll reply to the email address we have on file to confirm it's you, and
     won't ask for ID documents for a simple request;
   - **what we delete:** your form submissions, emails and project notes;
   - **what we may have to keep:** invoices and payment records, for the period
     `docs/legal-compliance.md` supports (don't invent a number). We keep only what the law
     requires and delete the rest;
   - **timing:** we confirm receipt within N business days and complete within 30 days (or the
     period the compliance map supports). Use the owner's confirmed numbers;
   - **no charge, and no different treatment** for asking;
   - **authorised agents / parents:** how a parent (see `#children`) or an agent can make a
     request.

2. **Discoverability.** Keep the request path at most one click from anywhere:
   - the footer Legal column links `/privacy/`;
   - the Privacy Policy summary (`#summary`) bullet links to `#your-rights`;
   - optionally, the contact form notice (`#form-privacy`) already links to the policy. Don't
     make the notice longer.

3. **Write `docs/data-requests-runbook.md`** for the owner. Verify each vendor step with
   `WebFetch` against current Netlify and mailbox provider docs, and cite the URLs.
   - **Log it:** record the date received and the request type in a private tracker (off-repo;
     don't store personal details in git).
   - **Acknowledge** within N business days, using the template below.
   - **Verify:** reply to the address on file; if the request came from a different address, ask
     them to confirm from the original one.
   - **Find everything:**
     - Netlify → Site → Forms → `contact` → search by email, including the **Spam** submissions
       tab;
     - inbox: Netlify notification emails and threads with that address (inbox, archive, sent,
       trash);
     - local notes, documents, project folders, design files;
     - any client accounts we manage for them (hand over or remove our access);
     - any vendors from `docs/third-parties.md` that hold their data.
   - **Delete** each item, including the Netlify form submission. Mention the Netlify API
     (`DELETE /api/v1/submissions/{id}`) as an option, with **no tokens in the repo**. Then empty
     the mailbox trash.
   - **Keep** only the legally required records (invoices), and note that they're retained and
     why.
   - **Confirm** completion to the requester, using the template below.
   - **Access requests:** export what we hold (form submission, email threads summary) and send
     it to the verified address.
   - **Deadlines** table: acknowledge / complete / extension rules.
   - **Templates:** acknowledgement, verification, completion, and "we must keep invoices"
     wording. All plain and friendly.

4. **Tie in retention.** Link the runbook from `docs/data-inventory.md`'s "Retention routine"
   (Prompt 07), since the quarterly clean-up uses the same steps.

5. **Guard.** Add a check to `tools/check_site.py` that `/privacy/` contains `id="your-rights"` and
   a `mailto:` link whose subject includes "request".

6. Update item 20 in `docs/compliance-log.md`.

## Verify

- `python3 tools/check_site.py` passes.
- In Playwright, click the "Email a data request" link and assert its `href` is the expected
  `mailto:` with the subject. Tab to it and check that focus is visible.

## Commit

`Fix #20: add data request process and deletion runbook`. Push to the current branch.
