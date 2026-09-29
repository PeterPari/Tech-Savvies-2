# Accessibility Audit: Images and alt text

WCAG 1.1.1 (Level A) requires a text alternative for every non-text element. This audit documents every image, icon, and SVG on the site.

## Images

| Page | Element | Role | Current alternative | Correct? | Notes |
|------|---------|------|----------------------|----------|-------|
| public/index.html:51 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Linked logo, alt names destination |
| public/index.html:114 | `<img src="grisha-studio.webp">` | Meaningful (case study) | alt="The Grisha.studio home page, showing the name Gregory Parizhsky beside a photo of a tall green ceramic tower sculpture" | ✓ | 110 characters, describes content |
| public/index.html:141 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Footer logo link |
| public/404.html:35 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Header logo link |
| public/404.html:68 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Footer logo link |
| public/contact/index.html:35 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Header logo link |
| public/contact/index.html:129 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Footer logo link |
| public/contact/thanks/index.html:35 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Header logo link |
| public/contact/thanks/index.html:68 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Footer logo link |
| public/cookies/index.html:35 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Header logo link |
| public/cookies/index.html:90 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Footer logo link |
| public/our-story/index.html:35 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Header logo link |
| public/our-story/index.html:68 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Footer logo link |
| public/privacy/index.html:35 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Header logo link |
| public/privacy/index.html:242 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Footer logo link |
| public/refunds/index.html:35 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Header logo link |
| public/refunds/index.html:179 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Footer logo link |
| public/solutions/index.html:35 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Header logo link |
| public/solutions/index.html:149 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Footer logo link |
| public/terms/index.html:35 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Header logo link |
| public/terms/index.html:210 | `<img src="logo.png">` | Linked logo | alt="Tech-Savvies NYC home" | ✓ | Footer logo link |

## SVG Icons

All inline SVGs are decorative (menu, close, external-link, send icons) and use `aria-hidden="true" focusable="false"`.

| Page | Element | Classes | Role | ARIA attributes | Correct? |
|------|---------|---------|------|-----------------|----------|
| Every page | Menu icon | icon-menu | Decorative | aria-hidden="true" focusable="false" | ✓ |
| Every page | Close icon | icon-close | Decorative | aria-hidden="true" focusable="false" | ✓ |
| Every page | External link icon | icon-inline | Decorative, alongside visible "(opens in a new tab)" text | aria-hidden="true" focusable="false" | ✓ |
| public/index.html + contact | Send icon | (inline in button) | Decorative, button label is "Send message" | aria-hidden="true" focusable="false" | ✓ |

## Open Graph Images

All pages include og:image and og:image:alt (social card preview). Most also include twitter:image:alt for Twitter/X.

| Page | og:image | og:image:alt | twitter:image:alt | Correct? |
|------|----------|--------------|-------------------|----------|
| Every public page | /assets/img/og-image.png | "Tech-Savvies: Websites done fast. Websites done right." | Now added | ✓ |

## Summary

- **21 `<img>` elements:** 1 meaningful (case study), 20 linked logos
- **7+ inline SVGs (icons):** all decorative with aria-hidden and focusable attributes
- **12 pages:** all have og:image:alt, all now have twitter:image:alt
- **Status:** ✓ All non-text elements have appropriate alternatives

# Accessibility Audit: Contrast

WCAG 2.2 AA: 1.4.3 needs 4.5:1 for body text and 3:1 for large text, 1.4.11 needs 3:1 for UI boundaries and focus indicators, and 1.4.1 says color can’t be the only signal. Audited 2026-09-29 against the `:root` tokens in `public/assets/css/styles.css`. Every token is unchanged.

## Ratios

Transparent colors are composited over their real background first: the header `rgba(15,20,25,.88)` becomes #0f1419 over `--bg` (#2c3035 in the worst case, over white), and the showcase frame’s `rgba(255,255,255,.05/.1/.14)` fills are composited over `--field-bg`.

| Pair | Ratio | Needs |
|------|-------|-------|
| body text `--text` on `--bg` | 15.87 | 4.5 |
| headings `--heading` on `--bg` | 18.51 | 4.5 |
| muted text (`.lead`, `.meta`, `.body-muted`, `.prose li::marker`, footer, `.optional`, `.contact-label`) on `--bg` | 7.22 | 4.5 |
| `--accent` text (`.eyebrow`, `.accent`, `.showcase` links, links on `--bg`) | 7.30 | 4.5 |
| `--accent` link hover `--accent` on `--bg` (footer links hover) | 7.30 | 4.5 |
| Header nav link `--muted` on header (rgba(15,20,25,.88) over `--bg`) | 7.22 | 4.5 |
| Header nav link `--muted` on header over white (worst case if page content scrolls behind) | 5.18 | 4.5 |
| Header nav hover / `aria-current` `--heading` on header (over `--bg`) | 18.51 | 4.5 |
| Header nav hover / `aria-current` `--heading` on header over white (worst case) | 13.28 | 4.5 |
| `aria-current` underline `--accent` on header (1.4.11 graphic) | 7.30 | 3.0 |
| Mobile menu panel `--muted` link on `--bg` | 7.22 | 4.5 |
| Footer link `--text` on `--bg` | 15.87 | 4.5 |
| Button text `--bg` on `--accent` | 7.30 | 4.5 |
| Button hover `--bg` on `--accent-hover` | 9.63 | 4.5 |
| Skip link `--bg` on `--accent` | 7.30 | 4.5 |
| Button boundary `--accent` vs `--bg` (1.4.11) | 7.30 | 3.0 |
| Disabled button text (opacity .75; exempt, recorded) | 3.40 | – |
| Input text `--heading` on `--field-bg` | 17.55 | 4.5 |
| Placeholder `#8391a5` on `--field-bg` | 5.48 | 4.5 |
| Field label `--text` on `--bg` | 15.87 | 4.5 |
| Input border `--field-border` vs `--field-bg` (1.4.11) | 3.69 | 3.0 |
| Input border `--field-border` vs page `--bg` (1.4.11) | 3.89 | 3.0 |
| Input hover border `--muted` vs `--field-bg` | 6.85 | 3.0 |
| Input focus border `--accent` vs `--field-bg` (1.4.11) | 6.92 | 3.0 |
| Focus ring `:focus-visible` `--accent` vs `--bg` (1.4.11) | 7.30 | 3.0 |
| Focus ring `--accent` vs `--field-bg` | 6.92 | 3.0 |
| Invalid border `--error` vs `--field-bg` (1.4.11) | 6.35 | 3.0 |
| Error text `--error` on `--bg` | 6.69 | 4.5 |
| Select option `--text` on `--bg` | 15.87 | 4.5 |
| Select arrow `#94a3b8` vs `--field-bg` (1.4.11) | 6.85 | 3.0 |
| `::selection` `--bg` on `--accent` | 7.30 | 4.5 |
| Check mark `--accent` vs `--bg` (decorative) | 7.30 | 3.0 |
| Table head `--heading` on `--field-bg` | 17.55 | 4.5 |
| Table cell `--text` on `--bg` | 15.87 | 4.5 |
| Showcase URL text `--muted` on rgba(255,255,255,.05) over `--field-bg` | 6.03 | 4.5 |
| Showcase URL hover `--heading` on rgba(255,255,255,.1) over `--field-bg` | 13.16 | 4.5 |
| Showcase frame focus outline `--heading` vs `--bg` | 18.51 | 3.0 |
| Showcase frame border rgba(255,255,255,.1) vs `--bg` (decorative) | 1.31 | – |
| Showcase frame hover border rgba(255,255,255,.2) vs `--bg` (decorative) | 1.86 | – |
| Showcase window dots rgba(255,255,255,.14) vs `--field-bg` (decorative) | 1.52 | – |
| Divider `--line` rgba(255,255,255,.1) vs `--bg` (decorative) | 1.31 | – |
| In-sentence link vs body text (`--accent` vs `--text`, needs underline) | 2.17 | 3.0 |
| In-sentence link vs muted body (`--accent` vs `--muted`, needs underline) | 1.01 | 3.0 |

Notes:

- **Hover, focus, `aria-current`:** nav hover and `aria-current="page"` use `--heading`, the underline is `--accent`. Link hover in the footer is `--accent` on `--bg`. `.btn:hover` is `--bg` on `--accent-hover`. All rows are above.
- **Disabled:** `.btn:disabled` uses opacity .75. Disabled controls are exempt from 1.4.3, so 3.40:1 is recorded, not required.
- **`::selection`:** `--bg` on `--accent`.
- **Later prompts:** `.prose` (text, headings, list markers, tables), `.form-note` and `.optional` all use `--text` or `--muted` on `--bg`. There is no `.field-error` yet; when Prompt 15 adds it, `--error` on `--bg` is 6.69:1.
- **Decorative:** dividers, frame borders and window dots are below 3:1 on purpose. They aren’t needed to identify a control or read content.
- **Color-only signals (1.4.1):** in-sentence links (`.lead`, `.body-muted`, `.meta`, `.form-note`, `.prose`, `.includes p`, `.contact-info p`, `.link`) share one underline rule, because `--accent` against body text is only 2.17:1 (against `--muted`, 1.01:1). Nav links, footer lists, buttons and `.contact-email` stay unchanged: they are not inside sentences. The invalid-field border is color-only until Prompt 15 adds text error messages.

## Forced colors

An `@media (forced-colors: active)` block gives `.btn` and `.skip-link` a 2px `ButtonText` border, keeps the `aria-current` underline, gives `.nav-toggle` a border and draws focus outlines in `Highlight` (the `.input` box-shadow ring is removed in this mode). Checked with Playwright forced-colors emulation on the home page, the contact form and the open mobile menu at 375px: buttons show borders, the current page keeps its underline and the focused element has a visible outline.

## axe results

axe-core (color-contrast and link-in-text-block rules), installed outside the repo, run on all 10 pages (home, solutions, our-story, contact, thanks, privacy, terms, refunds, cookies, 404) at 375px and 1280px: **0 violations**. Some checks come back “incomplete” because axe can’t read the background through a background image or an overlapping element (the contact `select`, and the privacy and refunds tables at 375px); those pairs are covered by the computed ratios above.
