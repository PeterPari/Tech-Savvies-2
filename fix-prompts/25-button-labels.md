# Prompt 25: Use clear button labels

Phase 5 (after 15). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/compliance-log.md`, `docs/accessibility-audit.md` and
`docs/ux-honesty-rules.md`.

## Goal

Every button and link should say exactly what happens when you use it, to sighted users and
screen-reader users alike, and use the same words for the same action everywhere.

## Why

Clear labels are WCAG 2.4.4 (link purpose), 2.4.6 (labels), 2.5.3 (label in name) and 3.2.4
(consistent identification), and they're the basis of honest UI (no misleading buttons). The
audience "doesn't feel tech-savvy yet", so vague labels cost real enquiries. The audit found the
original controls good:
- "Send message" (submit), "Start your project", "Back to home", "Contact";
- the menu toggle is named "Menu", with `aria-expanded` for its state;
- the external link says "(opens in a new tab)";
- the logo link is "Tech-Savvies NYC home".

Prompts 01–20 added new links and controls (legal pages, "Email a data request", the privacy
notice link, form errors, maybe a refund-request link), and those need the same bar.

## Task

1. **Inventory** every `<a>`, `<button>`, `<input type="submit|button">`, `<summary>`, and
   element with `role="button"` on every page. For each, get the computed accessible name with
   Playwright (`page.accessibility.snapshot()` or `locator.evaluate` + axe). Put the table in
   `docs/accessibility-audit.md` (Labels section): page, element, visible text, accessible name,
   destination or action, verdict.

2. **Check each against these rules:**
   - Starts with a verb or names the destination ("Send message", "Read our Privacy Policy",
     "Email a data request"). Never "Click here", "Learn more", "Submit", "Read more" or "Go".
   - The accessible name **contains the visible text**, starting with it (2.5.3). For example,
     don't add an `aria-label` that replaces the visible words.
   - The same destination or action uses the same label across pages (3.2.4). For example, the
     privacy link is "Privacy Policy" in the footer and "Read our Privacy Policy" in running text,
     which is fine because it's the same key words. It must not become "Data info" somewhere else.
   - `mailto:` links show the address or say "Email …". Links that open a new tab say so.
   - Icon-only controls have a text name (the toggle does). Decide whether the toggle should say
     "Close menu" when open. `aria-expanded` already conveys state, so keeping "Menu" is correct.
     Don't change it without a reason.
   - Loading state: when the submit label switches to "Sending…", confirm the page navigation
     makes an extra announcement unnecessary. If a JS validation failure (Prompt 15) keeps the
     user on the page, the button must return to "Send message".
   - Buttons that do the same thing look the same. Choices of equal weight look equal
     (`docs/ux-honesty-rules.md`).

3. **Fix** anything that fails, in every affected HTML file.

4. **Write `docs/microcopy.md`:** the rules above as a short checklist, plus a glossary of the
   site's canonical labels ("Start your project", "Send message", "Privacy Policy", "Terms of
   Service", "Refund Policy", "Cookie Policy", "Accessibility", "Email a data request", "Back to
   home"). Link it from the README "Editing" section.

5. **Guard.** Add a `link-text` check to `tools/check_site.py` that fails on link or button text
   (after stripping tags and visually hidden spans) equal to `click here`, `here`, `learn more`,
   `read more`, `more`, `submit` or `go`, case-insensitive, and on any `<a>`/`<button>` with an
   empty accessible name (no text, no `aria-label`, no `img[alt]`).

6. Update item 25 in `docs/compliance-log.md`.

## Verify

- axe `button-name`, `link-name` and `label-content-name-mismatch` show 0 violations on every page.
- `python3 tools/check_site.py` passes, and a temp copy with `<a href="/">click here</a>` fails.

## Commit

`Fix #25: audit control labels and add microcopy rules`. Push to the current branch.
