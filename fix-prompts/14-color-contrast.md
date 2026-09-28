# Prompt 14: Check and fix color contrast

````text
<context>
WCAG requirements that apply:
- 1.4.3: 4.5:1 for body text, 3:1 for large text;
- 1.4.11: 3:1 for UI boundaries and focus indicators;
- 1.4.1: color can't be the only signal.

Ratios measured from the :root tokens in public/assets/css/styles.css:

| Pair | Ratio | Needs |
|------|-------|-------|
| --text #e8eef7 on --bg #0f1419 | 15.87 | 4.5 |
| --muted #94a3b8 on --bg | 7.22 | 4.5 |
| --accent #10b981 on --bg | 7.30 | 4.5 |
| --bg on --accent (button text) | 7.30 | 4.5 |
| --bg on --accent-hover #34d399 | 9.63 | 4.5 |
| placeholder #8391a5 on --field-bg #131a20 | 5.48 | 4.5 |
| --field-border #64748b on --field-bg | 3.69 | 3.0 |
| --error #f87171 on --bg | 6.69 | 4.5 |
| --accent link vs --text body | 2.17 | 3.0, or an underline |
| --accent link vs --muted body | 1.01 | 3.0, or an underline |

Known failures:
1. The .story-contact link on /our-story/ (public/our-story/index.html:58) sits in running text with no underline. .lead a and .meta a are already underlined.
2. .btn has a background and no border, so in forced-colors mode it loses its boundary. .input:focus uses a box-shadow, which forced colors removes; the transparent outline on .input covers that case.

Prompt 15 adds text error messages, which fixes the color-only invalid-field border.
</context>

<inputs>
docs/accessibility-audit.md, docs/compliance-log.md, public/assets/css/styles.css, public/
</inputs>

<deliverables>
1. A "Contrast" section in docs/accessibility-audit.md: a ratio table for every foreground/background pair in use (rgba colors composited over their real background, including the rgba(15,20,25,.88) header), covering hover, focus, aria-current, disabled (opacity .75; exempt but recorded), ::selection, and elements added by later prompts (.prose, .form-note, .field-error if present); plus axe results.
2. In-sentence links underlined with the .lead a treatment, via a shared selector or a .link utility, covering .story-contact, .prose, .form-note, .body-muted and the /contact/ info block. Nav links, footer lists, buttons and .contact-email stay unchanged.
3. An @media (forced-colors: active) block: .btn keeps a visible border, .nav-link[aria-current] keeps its underline, and focus outlines stay visible.
4. A comment above :root: "All color pairs meet WCAG AA; ratios in docs/accessibility-audit.md. Re-check when changing a token."
5. Item 14 updated in docs/compliance-log.md.
6. One commit, "Fix #14: underline in-text links, support forced colors, record contrast ratios", pushed.
7. A final message of at most 5 bullets.
</deliverables>

<constraints>
- Keep every color token unchanged. They already pass.
- Install axe-core in a scratch directory outside the repo.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- axe color-contrast and link-in-text-block report 0 violations on every page at 375px and 1280px.
- In forced-colors emulation, the home page, contact form and open mobile menu show button boundaries and focus outlines.
</acceptance_criteria>

<task>
Make every text, link, control and focus indicator on every page meet WCAG 2.2 AA contrast and remain visible in forced-colors mode.
</task>
````

## Assumptions
- Prompt 13 has run. Prompt 15 may not have run yet.

## Parameters
- Reasoning effort: medium.

## What to test
- axe across all pages at both widths.
- Forced-colors screenshots (Playwright `emulateMedia({ forcedColors: 'active' })`).
- Confirm by pixel inspection that the /our-story/ email link has an underline.
