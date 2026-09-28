# Prompt 16: Add real business details

Phase 2. Paste everything below the line into a new Claude Code session opened at the
repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 (especially Decisions 4 and 7) and §4, then `docs/business-facts.md`,
`docs/compliance-log.md` and `docs/legal-compliance.md`.

## Goal

Show visitors who they're dealing with: the legal business name, where the business is based,
the area it serves, the hours behind the "business hours" promise, and a postal address for
correspondence. Keep the structured data (JSON-LD) consistent with what the page shows.

## Why

The only business detail on the site today is `info@tech-savvies.com`. That hurts trust: small
clients paying a few hundred dollars want to know there's a real, reachable business. It's also
a legal gap:
- the Terms and Privacy Policy must name the contracting party and controller;
- CAN-SPAM needs a postal address in any commercial email (Prompt 18);
- trading under "Tech-Savvies" instead of the owner's legal name generally requires an assumed
  name (DBA) filing in NY (see `docs/legal-compliance.md`);
- the contact page promises replies "during NYC business hours" (`public/contact/index.html:59`)
  but never says what those hours are.

## Task

1. **Gather facts.** From `docs/business-facts.md` you need: legal name and entity type, DBA
   status, public mailing address, service area, business hours with time zone. If any are
   `TODO(owner)`, ask with `AskUserQuestion` and write the answers back.
   - **Address privacy:** if the owner offers a home address, recommend a PO box or virtual
     mailbox instead (Decision 7), and use whichever they confirm. If they decline to publish
     any address, show "New York, NY" only, and note in the compliance log that CAN-SPAM
     commercial email still needs a postal address.
   - Never publish a value that isn't confirmed in the facts file.

2. **Contact page** (`public/contact/index.html`, the `.contact-info` block). Below the email,
   add, using existing typography classes (`.contact-label`, body text):
   - Business: `<legal name> (doing business as Tech-Savvies)` or just `Tech-Savvies` if the
     legal name matches;
   - Based in: New York, NY; Serving: `<service area>`;
   - Hours: `<days, times> ET`;
   - Mail: `<address>` in an `<address>` element.

   Keep it compact. It sits beside the form at desktop widths, so check that the grid still
   balances at 768px and 1280px.

3. **Footer, on every HTML page.** In the "Contact" column, add "New York, NY" under the email.
   Change the copyright line to `&copy; <span data-year>2026</span> <Legal name>. All rights
   reserved.` Keep `data-year` so `main.js` still updates it. Apply the change to every HTML file
   in `public/`, then confirm with `grep -L` that none were missed.

4. **Our Story** (`public/our-story/index.html`). No change needed unless the legal name differs
   from the brand. If it does, add one sentence such as "Tech-Savvies is the trading name of
   <legal name>."

5. **JSON-LD** (`public/index.html:28-40`). Change `@type` to `ProfessionalService` (a
   schema.org LocalBusiness subtype suited to service businesses). Keep `name`, `url`, `logo`,
   `email`, `founder` and `description`, and add:
   - `legalName`;
   - `areaServed` (a `City`/`State` or text, per the facts);
   - `address` as a `PostalAddress`, but only the parts the owner agreed to publish (at minimum
     `addressLocality: "New York"`, `addressRegion: "NY"`, `addressCountry: "US"`);
   - `openingHoursSpecification` if hours are confirmed;
   - `sameAs`, only if the owner provides real, active social profile URLs.

   Don't add `telephone`, `priceRange`, `aggregateRating` or `review` unless the facts file
   supports them. `aggregateRating` is banned by the checker. Check that the JSON parses.

6. **Checker.** Extend `tools/check_site.py` with `business-details`. Every page's footer must
   contain the legal name from a `LEGAL_NAME` constant, and `public/index.html` JSON-LD must have
   `legalName` equal to it.

7. **README.** Add an "Editing → Business details" bullet listing everywhere these appear:
   contact page, all footers, JSON-LD, and later the legal pages.

8. Update item 16 in `docs/compliance-log.md`, and mark the DBA filing as an owner action if
   it's still needed.

## Constraints

- No phone number unless the owner explicitly wants one published.
- No map embed: it would add a third-party iframe and break the CSP.

## Verify

- `python3 tools/check_site.py` passes.
- Playwright screenshots of `/contact/` and one footer at 375px, 768px and 1280px. Make sure
  nothing overflows and the address wraps cleanly.
- Paste the JSON-LD into a scratch file and parse it with `python3 -m json.tool`.

## Commit

`Fix #16: show legal name, location, hours and mailing address`. Push to the current branch.
