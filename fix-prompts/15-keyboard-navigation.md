# Prompt 15: Keyboard navigation and keyboard-friendly forms

Phase 5 (after 14). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/compliance-log.md` and `docs/accessibility-audit.md`.
The relevant code is `public/assets/js/main.js`, the header/nav CSS in
`public/assets/css/styles.css` (around `.nav-toggle` and `@media (max-width: 47.99em)`), and
the form in `public/contact/index.html`.

## Goal

Everything should be operable with a keyboard alone, with visible focus that's never hidden.
The contact form should explain its requirements and report errors in text that screen readers
announce.

## Why

Keyboard access is WCAG 2.1.1 / 2.4.3 / 2.4.7 / 2.4.11. Form errors and instructions are
3.3.1 / 3.3.2. Many things already work: a skip link, `:focus-visible` outlines, a real
`<button>` menu toggle with `aria-expanded`, Escape to close with focus returned, and native
form controls with labels.

**Bug, reproduced 2026-09-28 in Playwright at 375px:** open the mobile menu and press Tab. After
"Contact", focus moves to "Grisha.studio", "Start your project" and so on. Those are links in
`<main>`, **hidden behind the full-screen menu overlay** (`.js .site-nav.is-open` covers the
viewport under the header). A keyboard user loses sight of focus entirely (2.4.11 Focus Not
Obscured).

**Form gaps:**
- Required fields aren't explained ("optional" is marked, but nothing says the rest are
  required).
- Errors are only the browser's native bubble plus a red border. The bubble disappears, and the
  border is color-only (1.4.1).

## Task

1. **Fix the menu focus leak** in `initMobileNav()` in `main.js`:
   - in `setOpen(open)`, set `inert` on everything outside the header while open:
     `document.querySelectorAll("body > :not(.site-header)")`. Take care not to make the skip
     link inert in a way that breaks it; the skip link can be inert while the menu is open.
   - clear `inert` on close (Escape, link click, outside click, resize to desktop, which are
     all existing paths through `setOpen`).
   - keep the current behaviour: focus stays on the toggle when opening, and Escape returns focus
     to the toggle.
   - `inert` is supported in all current browsers. If it's unsupported, the menu still works, so
     no polyfill is needed. Add a one-line comment in the file's style.

2. **Form instructions** (`public/contact/index.html`): add
   `<p class="form-note" id="form-required">All fields are required unless marked
   (optional).</p>` at the top of the form, after the honeypot. Reuse `.form-note` from Prompt 06,
   or add it if missing.

3. **Accessible inline errors**, as progressive enhancement in `initContactForm()`. Without JS,
   the native validation stays.
   - In JS only, set `form.noValidate = true` so the site controls the messages. On submit, run
     `form.checkValidity()`; if it's invalid, `preventDefault()`, show the messages, and focus
     the first invalid field.
   - For each required field, add an error element right after the control in the HTML:
     `<p class="field-error" id="name-error" hidden></p>`. When a field is invalid, fill it in,
     remove `hidden`, set `aria-invalid="true"`, and add the error id to the field's
     `aria-describedby`, keeping any existing ids. Clear everything on `input`/`change` once the
     field is valid.
   - Friendly, specific messages:
     - Name: "Enter your name."
     - Email, empty: "Enter your email address."
     - Email, bad format: "Enter an email address like name@example.com."
     - Service: "Choose what you need, or pick “Not sure yet”."
     - Message: "Tell us a little about your project."
   - Don't disable the submit button to block submission. The existing double-submit guard
     should only run when the form is valid, so move its logic after the validity check.
   - Style `.field-error`: `color: var(--error)`, `font-size: 0.8125rem`, and start the message
     with a visually hidden "Error: " or an inline icon, so the meaning doesn't depend on color.
     Check that contrast on the form background is at least 4.5:1.

4. **Also check, and fix if needed:**
   - After activating the skip link, the next Tab goes to the first focusable element in
     `<main>`. If a browser doesn't do this, add `tabindex="-1"` to `<main>` on every page, with
     no visible outline on `main:focus`.
   - Tab order matches visual order on every page. There's no positive `tabindex` anywhere.
   - Sticky header: tabbing backwards through a long page, like `/privacy/`, never leaves the
     focused element hidden under the header. `scroll-padding-top` exists; verify it works for
     focus. If it doesn't, add `scroll-margin-top` to focusable elements in `main`.
   - Target size is at least 24×24 CSS px (2.5.8) for footer links, inline links and the menu
     toggle (the toggle is 44×44).
   - The honeypot is unreachable by keyboard and hidden from assistive tech (`display: none`
     already does this; confirm it).

5. **Record** the keyboard walkthrough per page in `docs/accessibility-audit.md` (Keyboard
   section). Update item 15 in `docs/compliance-log.md`.

## Verify (Playwright script in your scratchpad)

- At 375px on `/`: open the menu and press Tab 10 times. Every focused element is inside
  `.site-header`. Press Escape: focus is on the toggle, and `inert` has been removed (Tab now
  reaches `<main>`).
- On `/contact/`: submit empty. Focus goes to Name, the error text is visible, `aria-invalid`
  is set, and `aria-describedby` includes the error id. Type a valid name: its error clears.
- With JavaScript disabled (`javaScriptEnabled: false`), an empty submit is still blocked by
  native validation.
- `python3 tools/check_site.py` passes.

## Commit

`Fix #15: keep focus out of content behind mobile menu; add accessible form errors`. Push to the
current branch.
