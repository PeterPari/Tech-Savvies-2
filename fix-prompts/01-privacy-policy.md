# Prompt 01: Privacy policy

Phase 3, the first legal page. Paste everything below the line into a new Claude Code session
opened at the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then these docs, which are this page's source material:
`docs/business-facts.md`, `docs/data-inventory.md`, `docs/third-parties.md`,
`docs/tracking-audit.md`, `docs/legal-compliance.md`, `docs/compliance-log.md`. If any of the
first five is missing, stop and tell the user which earlier prompt to run (07, 08, 23, 24).

## Goal

Publish `/privacy/`, a plain-English privacy policy that exactly describes what Tech-Savvies
collects, why, who processes it, how long it's kept, and how people can get it deleted. This
prompt also builds the shared pieces the other legal pages reuse: `.prose` styles and a footer
"Legal" column.

## Why

The site collects personal data through the contact form (name, email, business, message) and
through Netlify's request logs and form metadata. CalOPPA requires a conspicuously posted
privacy policy for any commercial site that collects personal information from California
residents, which includes this one. The FTC and NY GBL §349 treat a policy that misdescribes
practices as deceptive, so it must describe **this** site, not generic "we may use cookies and
share with partners" boilerplate. That boilerplate would be false here: there are no cookies,
no analytics and no ad partners.

## Content (in this order, with `id`s for deep links)

1. **Intro.** Who we are: legal name, "doing business as Tech-Savvies", mailing address, email.
   Effective date in a `<time datetime="YYYY-MM-DD">`.
2. **Summary** (`#summary`): 4–5 bullets a visitor can read in 20 seconds. For example: we only
   collect what you send us; we use it to reply and to do your project; we don't sell it or use
   it for ads; no cookies or tracking; email us to see or delete your data.
3. **What we collect** (`#what-we-collect`): the contact form fields; what you send by email;
   technical data Netlify records (take the exact list from `docs/third-parties.md`); client
   project information (content, logins you choose to share, invoices).
4. **How we use it** (`#how-we-use-it`): reply to enquiries; quote and deliver projects;
   invoicing and legal or tax obligations; spam prevention. State plainly what we **don't** do,
   using `docs/tracking-audit.md` and the owner's email answers: no marketing emails without a
   separate opt-in, no selling or sharing for targeted advertising (use the CCPA terms "sell"
   and "share" and say "we don't"), no profiling.
5. **Who we share it with** (`#sharing`): one row per processor from `docs/third-parties.md`
   (Netlify, including its spam filtering and the named third party if one exists; mailbox
   provider; payment processor if any), with a link to each one's privacy policy. Also: legal
   requests, and a business transfer.
6. **Cookies and tracking** (`#cookies`): a short statement taken from the conclusion in
   `docs/tracking-audit.md`. Include a **Do Not Track / Global Privacy Control** sentence, which
   CalOPPA requires: we don't track visitors across sites, so these signals don't change
   anything. Prompt 04 will add a link to `/cookies/` here.
7. **How long we keep it** (`#retention`): straight from `docs/data-inventory.md`.
8. **Your rights and choices** (`#your-rights`): access, correct, delete, and opt out of any
   future marketing. How to ask: a `mailto:` link with a prefilled subject. What we need from
   you (we reply to the email address on file to confirm it's you). Response time (use the
   figure `docs/legal-compliance.md` supports; 30 days is a safe default). No charge. Prompt 20
   refines this section and adds the internal runbook.
9. **Security** (`#security`): HTTPS, limited access, strong passwords and 2FA on the accounts
   that hold data. Only claim what the owner confirms in `docs/business-facts.md`.
10. **Children** (`#children`): not directed to children under 13; we don't knowingly collect
    their data; if we learn we have, we delete it; parents can contact us. Prompt 17 refines this.
11. **Visitors outside the US** (`#international`): include only if the facts file says EU/UK
    clients are served, with the legal bases (contract / legitimate interests / legal obligation)
    and the right to complain to a supervisory authority. Otherwise one sentence: data is stored
    and processed in the US.
12. **Changes to this policy** (`#changes`), and **Contact** (`#contact`).

Writing rules: short sentences, "we" and "you", roughly grade-8 reading level, no "may" for
things that never happen, and every fact traceable to a doc. No `TODO` or placeholder text on
the page. If a fact is missing, ask the owner.

## Build

1. **`public/privacy/index.html`.** Copy the full `<head>`, header and footer pattern from
   `public/our-story/index.html`. Give it a unique `<title>` ("Privacy Policy | Tech-Savvies"),
   meta description, canonical `https://tech-savvies.com/privacy/`, and `og:` tags. Structure:
   `<main id="main">` → `section.section.section--first` → `.container` → `p.eyebrow`
   ("Legal") → `h1.display-md` ("Privacy Policy") → `p.meta` with "Last updated" → an
   `<article class="prose">` holding h2/h3/p/ul.

2. **`.prose` styles** in `public/assets/css/styles.css`, in a new `/* ---------- Legal pages
   ---------- */` block using the existing tokens:
   - `max-width: var(--measure)`;
   - h2 using `--fs-h2`-like sizing with top spacing, h3 smaller;
   - paragraph and list spacing;
   - `ul`/`ol` restored to visible bullets (the reset only removes them for `ul[role="list"]`,
     so don't add `role="list"` inside `.prose`);
   - **links underlined.** Accent vs body text is only 2.17:1, so color alone fails WCAG 1.4.1.
     Reuse the `.lead a` underline treatment;
   - an optional `.prose table` style with borders using `var(--line)`, and horizontal scroll
     wrapped in a focusable `div` (`tabindex="0"`, `role="region"`, `aria-label`) if a table can
     exceed 320px.

3. **Footer "Legal" column, on every HTML page.** Add a fourth footer block after "Contact":
   `<nav aria-label="Legal">` with `p.eyebrow.footer-heading` "Legal" and
   `ul.footer-links[role=list]` containing "Privacy Policy". Update `.footer-grid` in
   `@media (min-width: 48em)` to four columns (`minmax(0, 1fr) auto auto auto`), and check that
   it still fits at 768px. If it doesn't, let the brand span a full row at 48em and use four
   columns from about 64em. Apply this to every HTML file in `public/`, and confirm with
   `grep -L 'aria-label="Legal"' $(find public -name '*.html')` that it returns nothing.

4. **Registration.** Add `/privacy/` to `public/sitemap.xml` and to the README pages table.
   Append `/privacy/` to `REQUIRED_FOOTER_LINKS` in `tools/check_site.py`.

5. Update item 1 in `docs/compliance-log.md`, and note "attorney review recommended".

## Verify

- `python3 tools/check_site.py` passes, including shared-chrome and required-footer-links.
- Playwright screenshots of `/privacy/` and a footer at 375px, 768px and 1280px. Tab through
  the page and check that focus is visible on every link.
- Cross-check every sentence against the source docs. List in your summary any statement you
  couldn't trace.

## Commit

`Fix #01: add privacy policy, legal page styles and footer legal links`. Push to the current
branch.
