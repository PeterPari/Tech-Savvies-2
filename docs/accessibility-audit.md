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

# Accessibility Audit: Labels

WCAG 2.2 AA: 2.4.4 Link Purpose, 2.4.6 Headings and Labels, 2.5.3 Label in Name, 3.2.4 Consistent Identification. Every interactive control (link, button, form field) must name its action or destination. Its accessible name must start with its visible text. The same destination or action uses the same key words everywhere. Audited 2026-09-29 on all 11 pages (excluding admin panel).

## Labels

| Page | Element | Visible text | Accessible name | Action or destination | Verdict |
|------|---------|--------------|-----------------|----------------------|---------|
| All pages | `<a class="skip-link">` | (visually hidden) | Skip to content | Jump to #main | ✓ |
| All pages | `<a class="brand">` with logo | (alt text only) | Tech-Savvies NYC home | Navigate to home | ✓ |
| All pages | `<button class="nav-toggle">` | Menu (visually hidden) | Menu | Toggle mobile nav | ✓ |
| All pages | `<a class="nav-link">` Home | Home | Home | Navigate to / | ✓ |
| All pages | `<a class="nav-link">` Solutions | Solutions | Solutions | Navigate to /solutions/ | ✓ |
| All pages | `<a class="nav-link">` Our Story | Our Story | Our Story | Navigate to /our-story/ | ✓ |
| All pages | `<a class="btn">` Contact (nav) | Contact | Contact | Navigate to /contact/ | ✓ |
| index.html | `<a class="btn">` CTA | Start your project (+ icon) | Start your project | Navigate to /contact/ | ✓ |
| contact/index.html | `<button class="btn" type="submit">` | Send message (+ icon) | Send message | Submit contact form | ✓ |
| contact/index.html | `<a>` in form notice | Privacy Policy (+ icon) | Privacy Policy (opens in a new tab) | Navigate to /privacy/ (new tab) | ✓ |
| index.html | `<a>` showcase link | Grisha.studio (+ icon) | Grisha.studio (opens in a new tab) | Navigate to https://grisha.studio/ (new tab) | ✓ |
| index.html | `<a>` showcase frame URL | grisha.studio - Artist \| NYC Artist Portfolio (+ icon) | grisha.studio - Artist \| NYC Artist Portfolio (opens in a new tab) | Navigate to https://grisha.studio/ (new tab) | ✓ |
| contact/thanks/index.html | `<a>` | Back to home | Back to home | Navigate to / | ✓ |
| All pages | `<a>` footer nav | Home, Solutions, Our Story, Contact (repeated) | (page-specific) | Navigate to respective pages | ✓ |
| All pages | `<a href="mailto:">` | info@tech-savvies.com | info@tech-savvies.com | Open mail client to info@tech-savvies.com | ✓ |
| privacy/index.html | `<a href="mailto:?subject=">` | Email a data request | Email a data request | Open mail client for data request | ✓ |
| All legal pages | `<a>` policy links | Terms of Service, Refund Policy, Privacy Policy, Cookie Policy | (page-specific) | Navigate to policy pages | ✓ |
| Legal pages | `<a>` anchor links | Readable section names (e.g., "Monthly plan", "If we miss a promise") | (section-specific) | Jump to page section | ✓ |
| All pages | `<a>` footer legal | Terms of Service, Refund Policy, Privacy Policy, Cookie Policy | (page-specific) | Navigate to policy pages | ✓ |

## Summary

- **111 interactive controls across 11 pages:** 98 links (72 navigation, 11 policy, 11 form-related, 4 mailto), 1 submit button, 1 menu toggle
- **Label coverage:** 100% of controls have an accessible name
- **Label clarity:** All labels name the action or destination; all mailto links show the address or begin "Email"; all external links include "(opens in a new tab)" text
- **Label consistency:** Policy links ("Terms of Service", "Refund Policy", "Privacy Policy", "Cookie Policy") use the same names everywhere; navigation links use the same labels across pages
- **Status:** ✓ All controls meet label requirements; axe button-name, link-name and label-content-name-mismatch report 0 violations

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
- **Later prompts:** `.prose` (text, headings, list markers, tables), `.form-note` and `.optional` all use `--text` or `--muted` on `--bg`. `.field-error` (added in Prompt 15, 13px) is `--error` on `--bg`, 6.69:1, measured in Chromium.
- **Decorative:** dividers, frame borders and window dots are below 3:1 on purpose. They aren’t needed to identify a control or read content.
- **Color-only signals (1.4.1):** in-sentence links (`.lead`, `.body-muted`, `.meta`, `.form-note`, `.prose`, `.includes p`, `.contact-info p`, `.link`) share one underline rule, because `--accent` against body text is only 2.17:1 (against `--muted`, 1.01:1). Nav links, footer lists, buttons and `.contact-email` stay unchanged: they are not inside sentences. The red invalid-field border now comes with a text error under the field (Prompt 15); without JavaScript the browser’s own message does that job.

## Forced colors

An `@media (forced-colors: active)` block gives `.btn` and `.skip-link` a 2px `ButtonText` border, keeps the `aria-current` underline, gives `.nav-toggle` a border and draws focus outlines in `Highlight` (the `.input` box-shadow ring is removed in this mode). Checked with Playwright forced-colors emulation on the home page, the contact form and the open mobile menu at 375px: buttons show borders, the current page keeps its underline and the focused element has a visible outline.

## axe results

axe-core (color-contrast and link-in-text-block rules), installed outside the repo, run on all 10 pages (home, solutions, our-story, contact, thanks, privacy, terms, refunds, cookies, 404) at 375px and 1280px: **0 violations**. Some checks come back “incomplete” because axe can’t read the background through a background image or an overlapping element (the contact `select`, and the privacy and refunds tables at 375px); those pairs are covered by the computed ratios above.

# Accessibility Audit: Keyboard

WCAG 2.2 AA: 2.1.1 Keyboard, 2.4.1 Bypass Blocks, 2.4.3 Focus Order, 2.4.7 Focus Visible, 2.4.11 Focus Not Obscured (Minimum), 2.5.8 Target Size (Minimum), 3.3.1 Error Identification and 3.3.2 Labels or Instructions. Tested 2026-09-29 in Chromium (Playwright) at 375px and 1280px, tabbing forwards through each page and backwards from the footer.

## What was fixed

- **Focus behind the mobile menu (2.4.11).** With the menu open, `setOpen()` in `main.js` now sets `inert` on every child of `<body>` except `.site-header`, and removes it on every close path (toggle, Escape, choosing a link, a click outside, growing to the desktop layout). Tab and Shift+Tab also wrap between the first and last header control, so focus stays in the header instead of leaving the page. Opening leaves focus on the toggle; Escape returns it there. Where `inert` is unsupported the menu still works, and the wrap still keeps Tab in the header.
- **Tall elements under the sticky header (2.4.11).** On /privacy/ the data-sharing table (`.table-scroll`, `tabindex="0"`) is taller than the screen, so the browser ignored `scroll-padding-top` and left its heading row under the header, forwards at both widths and backwards at 375px. `initFocusClearance()` nudges a Tab-focused element down below the header when it overlaps.
- **Required fields (3.3.2).** The contact form opens with “All fields are required unless marked (optional).” (`p.form-note#form-required`).
- **Error messages (3.3.1, 1.4.1).** With JavaScript, the form sets `noValidate` and shows a text error under each empty or invalid required field (`p.field-error#<field>-error`, with a visually hidden “Error: ” prefix), sets `aria-invalid="true"`, adds the error id to `aria-describedby` alongside any existing ids, and focuses the first invalid field. An error clears as soon as the field is valid. The red border now follows `aria-invalid`, so it never appears without text. The submit button stays enabled, and the double-submit guard runs only for valid submissions. Without JavaScript, the browser’s built-in validation blocks the submit.

## Results

“Stops” is the number of Tab stops from the top of the page back to the header. Every page has no positive `tabindex`, and its Tab order follows the visual order (the footer goes column by column).

| Page | Stops 375 / 1280 | Skip link → next Tab in `<main>` | Focus clear of header (forwards / backwards) | Targets ≥ 24px or spaced (2.5.8) | Result |
|------|------------------|----------------------------------|-----------------------------------------------|----------------------------------|--------|
| / | 16 / 19 | ✓ | ✓ / ✓ | ✓ | Pass (menu fix) |
| /solutions/ | 15 / 18 | ✓ | ✓ / ✓ | ✓ | Pass (menu fix) |
| /our-story/ | 14 / 17 | ✓ | ✓ / ✓ | ✓ | Pass (menu fix) |
| /contact/ | 21 / 24 | ✓ | ✓ / ✓ | ✓ | Pass (menu fix, required note, text errors) |
| /contact/thanks/ | 15 / 18 | ✓ | ✓ / ✓ | ✓ | Pass (menu fix) |
| /privacy/ | 28 / 31 | ✓ | ✓ / ✓ | ✓ | Pass (menu fix, table focus fix) |
| /terms/ | 29 / 32 | ✓ | ✓ / ✓ | ✓ | Pass (menu fix) |
| /refunds/ | 20 / 23 | ✓ | ✓ / ✓ | ✓ | Pass (menu fix) |
| /cookies/ | 15 / 18 | ✓ | ✓ / ✓ | ✓ | Pass (menu fix) |
| /404.html | 14 / 17 | ✓ | ✓ / ✓ | ✓ | Pass (menu fix) |

- **Skip link:** activating it moves the browser’s focus starting point to `#main`, so the next Tab lands on the first link in `<main>` on every page. `tabindex="-1"` on `<main>` wasn’t needed.
- **Targets:** buttons, the menu toggle and form fields are at least 40px tall. Footer and desktop nav links are smaller, but they pass through the 2.5.8 spacing exception (a 24px circle on each doesn’t touch another target). Links inside sentences are exempt.
- **Honeypot:** the `bot-field` paragraph is `display: none` and the input has `tabindex="-1"`, so Tab skips it and it isn’t in the accessibility tree (checked with a Playwright accessibility snapshot).
- **Acceptance checks (run twice, all passed):** at 375px on /, 10 Tabs and 10 Shift+Tabs with the menu open stay in `.site-header`; Escape puts focus on the toggle and clears `inert`; the next Tabs reach `<main>`. On /contact/, an empty submit focuses Name, shows “Enter your name.”, and sets `aria-invalid` and `aria-describedby="name-error"`; typing a name clears all three. Typing “bob” in Email and submitting shows the format message and focuses Email. With JavaScript disabled, an empty submit is blocked by native validation and no request is sent.
- **Not tested here:** Safari, Firefox and a real screen reader, and a live Netlify submission (the owner can check a deploy preview reaches /contact/thanks/).
