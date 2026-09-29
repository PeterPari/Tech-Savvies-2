# Email policy

How the owner (Peter Parizhsky, sole proprietor, trading as Tech-Savvies) writes email. The
website sends no email and has no newsletter signup. Netlify form notifications go only to the
owner. This policy covers the owner's own inbox.

Facts used (from [`business-facts.md`](business-facts.md), owner, 2026-09-29): no marketing or
newsletter email planned; no open-tracking; EU/UK clients not served deliberately; no public
mailing address. `/privacy/` and the `p#form-privacy` note say "no marketing emails, no mailing
list", and that stays true under this policy. If any fact above changes, update this file,
`/privacy/` and the form note together.

Rules source: FTC, [CAN-SPAM Act: A Compliance Guide for Business](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business).

## Email types

| Email type | Category | Requirements |
|------------|----------|--------------|
| Enquiry reply | Transactional/relationship | Honest From, Reply-To and subject. Standard signature. No opt-out needed. Don't add promotion. |
| Project update | Transactional/relationship | Same as above. Only about the work the client asked for. |
| Invoice | Transactional/relationship | Same as above. Amounts and terms come from `business-facts.md`. |
| Follow-up offer (upsell, "still need a site?", past-client promo) | Commercial | Every commercial rule below. Commercial signature. Check the suppression list first. |
| Newsletter | Commercial | Every commercial rule below, plus a double opt-in signup. None exists today, and the site must not add one without Prompt 06 deliverable 3. |

A message mixing a reply with an offer is judged by its primary purpose. If unsure, treat it as
commercial.

## Rules for commercial email

Each rule follows the [FTC guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business).

1. **Honest subject and from-name.** The From name is "Peter at Tech-Savvies" or "Tech-Savvies". The subject says what the email is. No misleading header data. Say it's an ad where the recipient wouldn't otherwise know.
2. **Postal address.** Include a valid postal address (street address, PO box or private mailbox). None is confirmed yet. **Don't send commercial email until one is.**
3. **Clear opt-out.** Every commercial email tells the reader, in plain words, how to stop getting them.
4. **Honour it within 10 business days.** Aim for the next working day.
5. **No fee or extra steps.** No charge, no login, no form, no more than a reply or one email.
6. **Opt-out works for 30 days after sending.** Keep the reply address and mailbox working for at least 30 days after each send.
7. **Never transfer opted-out addresses.** Don't sell, share or give them to anyone, except a service helping you comply.

## Suppression list

- Keep a list of everyone who opted out, **outside this repo** (password manager notes or a private spreadsheet). Never commit addresses.
- Add an address the day the request arrives. Keep it permanently.
- Check it before **every** promotional send, one-off or bulk.

## Email service (only if one is ever used)

- Put the physical address in the service's settings.
- Keep the built-in unsubscribe footer on. Don't remove or hide it.
- Use double opt-in (confirm by email) for any future signup form.

## EU/UK recipients

Not applicable. `business-facts.md` says EU/UK clients aren't served deliberately, so no
marketing email goes to them. If that changes, add a section on consent under PECR and GDPR
first.

## Open tracking

[`tracking-audit.md`](tracking-audit.md) records no open-tracking or read receipts, and
`business-facts.md` agrees. Send plain email with no tracking pixels, tracked links or read
receipts. If a service is added later, keep open tracking off and update `/privacy/`.

## Signatures

### Standard (all email)

Plain text:

```
Peter Parizhsky
Tech-Savvies (Peter Parizhsky, sole proprietor)
https://tech-savvies.com
info@tech-savvies.com
```

HTML:

```html
<p>
  Peter Parizhsky<br>
  Tech-Savvies (Peter Parizhsky, sole proprietor)<br>
  <a href="https://tech-savvies.com">tech-savvies.com</a><br>
  <a href="mailto:info@tech-savvies.com">info@tech-savvies.com</a>
</p>
```

### Commercial (offers, newsletters)

Plain text:

```
Peter Parizhsky
Tech-Savvies (Peter Parizhsky, sole proprietor)
https://tech-savvies.com
info@tech-savvies.com
postal address required before sending commercial email

Don't want emails like this? Reply 'unsubscribe' or email info@tech-savvies.com with the subject 'Unsubscribe', and we'll stop within 10 business days.
```

HTML:

```html
<p>
  Peter Parizhsky<br>
  Tech-Savvies (Peter Parizhsky, sole proprietor)<br>
  <a href="https://tech-savvies.com">tech-savvies.com</a><br>
  <a href="mailto:info@tech-savvies.com">info@tech-savvies.com</a><br>
  postal address required before sending commercial email
</p>
<p>
  Don't want emails like this? Reply 'unsubscribe' or email
  <a href="mailto:info@tech-savvies.com?subject=Unsubscribe">info@tech-savvies.com</a>
  with the subject 'Unsubscribe', and we'll stop within 10 business days.
</p>
```

When an address is confirmed, record it in `business-facts.md` (with the date) and replace the
"postal address required" line in both commercial versions.

## Owner actions

- Get a postal address (PO box or virtual mailbox) before any commercial email. Record it in `business-facts.md`.
- Create the suppression list outside the repo.
- Wanting a newsletter or marketing signup later: see Prompt 06 deliverable 3.
