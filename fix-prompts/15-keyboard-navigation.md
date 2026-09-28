# Prompt 15: Keyboard navigation and keyboard-friendly forms

````text
<context>
Already working: the skip link, :focus-visible outlines, a <button> menu toggle with aria-expanded, Escape to close with focus returned, and labelled native form controls.

Failures:
1. Reproduced on 2026-09-28 at 375px: with the mobile menu open, Tab past "Contact" moves focus to links in <main>, which sit hidden behind the full-screen overlay (.js .site-nav.is-open). This fails WCAG 2.4.11 Focus Not Obscured. Menu state is handled by setOpen() in initMobileNav() in public/assets/js/main.js; every close path calls it.
2. The form doesn't say that unmarked fields are required (3.3.2).
3. Errors show only as the browser bubble plus a red border (.input:user-invalid). The bubble disappears and the border is color-only (3.3.1, 1.4.1).

The double-submit guard lives in initContactForm() in main.js. .form-note exists from Prompt 06.
</context>

<inputs>
docs/accessibility-audit.md, docs/compliance-log.md, public/assets/js/main.js, public/assets/css/styles.css, public/contact/index.html, public/
</inputs>

<deliverables>
1. In setOpen(open), inert set on every child of <body> except .site-header while the menu is open, and cleared on every close path. Opening leaves focus on the toggle, and Escape still returns focus to it.
2. <p class="form-note" id="form-required">All fields are required unless marked (optional).</p> at the top of the form, after the honeypot.
3. Inline errors as a JavaScript enhancement:
   - JS sets form.noValidate = true, so browsers without JS keep native validation;
   - on an invalid submit, JS shows messages and focuses the first invalid field;
   - each required field has <p class="field-error" id="<field>-error" hidden> right after it, filled in when the field is invalid, with aria-invalid="true" and the error id added to aria-describedby alongside existing ids;
   - errors clear when the field becomes valid;
   - the double-submit guard runs only for valid submissions.
   Messages:
   - Name: "Enter your name."
   - Email, empty: "Enter your email address."
   - Email, bad format: "Enter an email address like name@example.com."
   - Service: "Choose what you need, or pick “Not sure yet”."
   - Message: "Tell us a little about your project."
4. .field-error styles: color var(--error), font-size 0.8125rem, a visually hidden "Error: " prefix, and contrast of at least 4.5:1 on its background.
5. Fixes for any of these that fail:
   - after the skip link, the next Tab lands inside <main> (add tabindex="-1" to <main> on every page if needed, with no outline on main:focus);
   - DOM order matches visual order, with no positive tabindex;
   - focused elements are never hidden under the sticky header when tabbing backwards on /privacy/;
   - targets are at least 24×24 CSS px;
   - the honeypot is unreachable by keyboard and hidden from assistive technology.
6. A "Keyboard" section in docs/accessibility-audit.md with the result for each page. Item 15 updated in docs/compliance-log.md.
7. One commit, "Fix #15: keep focus out of content behind mobile menu; add accessible form errors", pushed.
8. A final message of at most 6 bullets.
</deliverables>

<constraints>
- Add no inert polyfill. The menu works without inert where it's unsupported.
- Leave the submit button enabled for invalid submissions.
- Match main.js's existing style: ES5 functions, var, and one-line comments.
</constraints>

<acceptance_criteria>
- At 375px on /, with the menu open, 10 consecutive Tab presses keep focus inside .site-header. After Escape, focus is on the toggle and Tab reaches <main>.
- On /contact/, an empty submit focuses Name, shows its error text, and sets aria-invalid and aria-describedby. Entering a valid name clears the error.
- With JavaScript disabled, an empty submit is blocked by native validation.
- The checker exits 0.
</acceptance_criteria>

<task>
Make every Tech-Savvies page fully keyboard-operable without focus going behind the mobile menu, and give the contact form stated requirements and announced text errors.
</task>
````

## Assumptions
- Prompts 06 and 14 have run.

## Parameters
- Reasoning effort: high. It changes interactive JS on the only form.

## What to test
- The three keyboard and form acceptance scenarios, scripted in Playwright, run twice.
- Browsers with and without JavaScript.
- A real Netlify deploy preview: a valid submission still reaches `/contact/thanks/`.
