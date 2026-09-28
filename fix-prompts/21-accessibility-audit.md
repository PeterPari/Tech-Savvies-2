# Prompt 21: Fix accessibility (full WCAG 2.2 AA audit and statement)

Phase 5, last. It audits the finished site. Paste everything below the line into a new Claude
Code session opened at the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/accessibility-audit.md` (built up by Prompts 13, 14,
15 and 25), `docs/business-facts.md`, `docs/legal-compliance.md` (ADA / NYS / NYC Human Rights
Law entries) and `docs/compliance-log.md`.

## Goal

Bring every page to WCAG 2.2 Level AA. That means automated checks, a manual review of what
automation can't catch, and fixes for everything found. Then publish an honest accessibility
statement with a way to report barriers.

## Why

New York's federal courts see more website accessibility lawsuits under ADA Title III than
anywhere else, and NYS and NYC human rights laws add state-level exposure. Beyond the legal
risk, this business exists to help people who "don't feel tech-savvy". Many of them are older
adults (the original Tech-Savvies mission, per Our Story), for whom accessibility is everyday
usability. The site started from a good base: semantic landmarks, a skip link, focus styles,
reduced-motion support, and labelled fields. Prompts 13–15 and 25 fixed specific issues. This
prompt is the complete sweep over the finished site, including all the new legal pages.

## Task

1. **Automated audit.** Install `axe-core` in your scratchpad (not the repo). Use Playwright to
   run axe with the tags `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, `wcag22aa` and
   `best-practice` on **every** HTML page in `public/`, at 320px, 375px, 768px and 1280px, in
   these states:
   - default;
   - mobile menu open;
   - contact form showing errors;
   - `prefers-reduced-motion: reduce`;
   - `forced-colors: active`.

   Save the results as a table in `docs/accessibility-audit.md` (Automated section).

2. **Manual review**, following the WCAG 2.2 AA success criteria that automation misses. Record
   pass or fail with evidence for each:
   - **1.3.1 / 1.3.2 structure:** one `h1` per page; heading levels don't skip in meaning (the
     solutions page uses `h2.h4` styled small, which is fine semantically); lists are real lists;
     tables have `caption` and `th scope`; landmarks: header, nav "Main", main, nav "Footer",
     nav "Legal", footer.
   - **1.3.5:** input purpose (`autocomplete`) on name, email and organization.
   - **1.4.4 / 1.4.10 resize and reflow:** 200% zoom, and a 320px viewport with no horizontal
     scroll, except the table scroll regions, which must be keyboard-focusable.
   - **1.4.12 text spacing:** inject the WCAG text-spacing CSS (line-height 1.5, paragraph
     spacing 2em, letter-spacing .12em, word-spacing .16em). Nothing clips, especially the
     display headlines with the `kern-dot`/`kern-apos` spans and the buttons.
   - **1.4.13:** hover or focus content (none expected).
   - **2.1.1 / 2.1.2 / 2.4.3 / 2.4.7 / 2.4.11:** a full keyboard pass on every page (Prompt 15's
     work plus the legal pages).
   - **2.2.2 / 2.3.1:** no motion or flashing beyond `transition`s, which reduced motion removes.
   - **2.4.2:** unique, descriptive `<title>` on every page.
   - **2.4.4 / 2.5.3:** see Prompt 25.
   - **2.5.8:** target size.
   - **3.1.1:** `lang="en"`.
   - **3.2.3 / 3.2.4 / 3.2.6:** consistent navigation, consistent labels, and help (the contact
     email) in the same place on every page.
   - **3.3.1 / 3.3.2 / 3.3.3:** errors and instructions (Prompt 15).
   - **3.3.7 / 3.3.8:** redundant entry and accessible authentication. Expected N/A; confirm.
   - **4.1.2:** name, role and value for the toggle (`aria-expanded`), form controls and errors
     (`aria-invalid`).
   - **4.1.3:** status messages. Decide whether the error summary or "Sending…" needs a live
     region.
   - **Screen-reader smoke test:** read `page.accessibility.snapshot()` for home, contact and
     privacy, and check that the reading order and names make sense. Note in the doc that a real
     VoiceOver/NVDA pass is a recommended owner step.

3. **Fix** every failure in the HTML, CSS and JS, following the house style. Apply header and
   footer changes to every file.

4. **Accessibility statement: `public/accessibility/index.html`** (from the privacy page
   template, `.prose`). Content:
   - our commitment (WCAG 2.2 AA as the target);
   - what we've done (a short list: tested with automated tools and keyboard, supports zoom,
     reduced motion and high-contrast mode);
   - known limitations (be honest, or say "none known as of <date>");
   - how to report a problem: email with a prefilled subject "Accessibility"; we reply within N
     business days (from the facts file) and offer the information another way, such as by email
     or phone if one exists;
   - date of last review;
   - the technologies relied on (HTML, CSS, JavaScript is optional).

   Unique title and meta, canonical, `og:` tags. Add it to the footer Legal column on every page
   ("Accessibility"), the sitemap, the README, and `REQUIRED_FOOTER_LINKS`.

5. **Re-run** the full automated audit after the fixes: 0 violations on every page, state and
   viewport. Update `docs/accessibility-audit.md` with before and after results, and update item
   21 in `docs/compliance-log.md` (plus any owner step, such as a real screen-reader test).

## Constraints

- Keep the visual design and tokens. Fix the semantics and behaviour, not the brand.
- Don't claim "fully compliant" in the statement. Say "we aim to meet WCAG 2.2 AA" and give the
  review date.

## Verify

- axe: 0 violations across the whole matrix.
- `python3 tools/check_site.py` passes.
- Screenshots of `/accessibility/` at 375px and 1280px.

## Commit

`Fix #21: full WCAG 2.2 AA audit, fixes and accessibility statement`. Push to the current branch.
