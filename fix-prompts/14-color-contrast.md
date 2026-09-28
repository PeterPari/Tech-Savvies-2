# Prompt 14: Check and fix color contrast

Phase 5 (after 13). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/compliance-log.md` and `docs/accessibility-audit.md`.

## Goal

Every text, icon, link and control on every page should meet WCAG 2.2 AA contrast, and stay
usable in Windows forced-colors (high contrast) mode. Record the measured ratios.

## Why

WCAG 1.4.3 requires 4.5:1 for body text (3:1 for large text), 1.4.11 requires 3:1 for UI
component boundaries and focus indicators, and 1.4.1 says color can't be the only way to tell
things apart. Ratios measured in the audit from the tokens in `public/assets/css/styles.css`
`:root`:

| Pair | Ratio | Needs |
|------|-------|-------|
| `--text` #e8eef7 on `--bg` #0f1419 | 15.87 | 4.5 ✅ |
| `--muted` #94a3b8 on `--bg` | 7.22 | 4.5 ✅ |
| `--accent` #10b981 on `--bg` | 7.30 | 4.5 ✅ |
| `--bg` on `--accent` (button text) | 7.30 | 4.5 ✅ |
| `--bg` on `--accent-hover` #34d399 | 9.63 | 4.5 ✅ |
| placeholder #8391a5 on `--field-bg` #131a20 | 5.48 | 4.5 ✅ |
| `--field-border` #64748b on `--field-bg` | 3.69 | 3.0 ✅ |
| `--error` #f87171 on `--bg` | 6.69 | 4.5 ✅ |
| **`--accent` link vs `--text` body** | **2.17** | 3.0 ❌ if the link has no underline |
| **`--accent` link vs `--muted` body** | **1.01** | 3.0 ❌ if the link has no underline |

The tokens pass. The problems are:
1. **In-sentence links without underline.** `.lead a` and `.meta a` are underlined, but the Our
   Story "Contact Peter: info@tech-savvies.com" link (`public/our-story/index.html:58`,
   `.story-contact`) is color-only. Check links inside `.body-muted`, `.story`, `.contact-info`,
   the new `.prose` pages, `.form-note`, and the contact info block from Prompt 16.
2. **Forced-colors mode.** `.btn` is drawn with a background color and no border. In Windows
   High Contrast the background is removed, so the button becomes plain text with no visible
   boundary. Check the `.input:focus` box-shadow too, since box-shadows are removed in forced
   colors; the transparent outline on `.input` already covers that case.
3. **Error state.** Invalid fields are shown by a red border only (`.input:user-invalid`).
   Prompt 15 adds text error messages, which fixes this. Make sure the error text color passes on
   the form background.

## Task

1. **Measure everything,** with no guessing. Write a small script in your scratchpad (Node or
   Python) that computes WCAG contrast for every color pair, including rgba colors composited
   over their real background (for example `rgba(15,20,25,.88)` for the header, and the
   `rgba(255,255,255,.1)` lines if they separate anything interactive). Also run axe-core's
   `color-contrast` and `link-in-text-block` rules on every page at 375px and 1280px with
   Playwright: install axe-core in your scratchpad, not the repo. Include hover, focus,
   `aria-current`, disabled ("Sending…" at `opacity: .75`; disabled controls are exempt, but note
   the ratio) and `::selection` states.

2. **Fix in-text links.** Add underline styling for links inside running text. Either extend the
   `.lead a` rule into a shared selector (for example
   `.lead a, .story-contact a, .prose a, .form-note a, .body-muted a`), or add a small `.link`
   utility. Keep the existing look: underline in `rgba(16,185,129,.5)`, solid on hover. Don't
   underline nav, footer lists, buttons or the `.contact-email` feature link, since those aren't
   inside sentences.

3. **Forced colors.** Add a `@media (forced-colors: active)` block: `.btn { border: 1px solid
   ButtonText; }` (or `border: 1px solid transparent` on `.btn` by default, which forced colors
   turn visible). Make sure `.nav-link[aria-current]` keeps its underline, the skip link is
   visible, and focus outlines use `Highlight`. Test with Playwright:
   `page.emulateMedia({ forcedColors: 'active' })` and screenshots.

4. **Error text contrast.** Once Prompt 15 has added error messages, confirm they pass on their
   background. If Prompt 15 hasn't run yet, note it in the audit doc.

5. **Record** the full ratio table and the axe results in `docs/accessibility-audit.md`
   (Contrast section). Add a comment above `:root` in `styles.css`: "All color pairs meet WCAG AA;
   ratios in docs/accessibility-audit.md. Re-check when changing a token."

6. Update item 14 in `docs/compliance-log.md`.

## Constraints

- Keep the visual design. Don't change the brand colors, since they already pass.

## Verify

- axe `color-contrast` and `link-in-text-block`: 0 violations on every page and viewport.
- Forced-colors screenshots of the home page, contact form and mobile menu show visible button
  boundaries and focus.
- `python3 tools/check_site.py` passes.

## Commit

`Fix #14: underline in-text links, support forced colors, record contrast ratios`. Push to the
current branch.
