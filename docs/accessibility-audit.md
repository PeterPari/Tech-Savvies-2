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
| All pages | `<a>` footer legal | Terms of Service, Refund Policy, Privacy Policy, Cookie Policy, Accessibility (added in Prompt 21) | (page-specific) | Navigate to policy pages | ✓ |

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

# Accessibility Audit: WCAG 2.2 AA

Prompt 21, 2026-09-29. It covers the rest of WCAG 2.2 AA across all 12 HTML files in `public/`, including every legal page and the new /accessibility/ page. Everything was tested in Chromium (Playwright 1.56, headless) against `python3 -m http.server`. “Before” is commit `0b5b2b7`, served from a scratch worktree; “after” is this commit. axe-core 4.13.0 was installed in a scratch directory outside the repo.

## Automated

**Setup.** axe-core ran with the tags `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, `wcag22aa` and `best-practice` on every HTML page. Each page ran at 320, 375, 768 and 1280px wide (800px tall), in five states:

- **default:** page as loaded.
- **menu open:** the menu toggle clicked. This state only exists at 320 and 375px; at 768px and up the toggle is hidden (the menu becomes the desktop nav at 48em). /admin/ has no menu.
- **form errors:** on /contact/, “bob” typed in Email and the form submitted empty otherwise, so all four text errors show. Other pages have no form.
- **reduced motion:** `prefers-reduced-motion: reduce` emulated.
- **forced colors:** `forced-colors: active` emulated.

That makes 156 runs before and 170 after; the 70 page/state/width combinations that don’t exist are marked n/a. Each cell below is violation nodes summed over the widths, before → after.

| Page | default | menu open | form errors | reduced motion | forced colors (raw axe) | forced colors (painted color) |
|---|---|---|---|---|---|---|
| / | 0 → 0 | 0 → 0 | n/a | 0 → 0 | 124 → 128 | 0 → 0 |
| /solutions/ | 0 → 0 | 0 → 0 | n/a | 0 → 0 | 268 → 272 | 0 → 0 |
| /our-story/ | 0 → 0 | 0 → 0 | n/a | 0 → 0 | 72 → 76 | 0 → 0 |
| /contact/ | 0 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 146 → 150 | 0 → 0 |
| /contact/thanks/ | 0 → 0 | 0 → 0 | n/a | 0 → 0 | 82 → 86 | 0 → 0 |
| /privacy/ | 0 → 0 | 0 → 0 | n/a | 0 → 0 | 398 → 402 | 0 → 0 |
| /terms/ | 0 → 0 | 0 → 0 | n/a | 0 → 0 | 442 → 446 | 0 → 0 |
| /refunds/ | 0 → 0 | 0 → 0 | n/a | 0 → 0 | 270 → 274 | 0 → 0 |
| /cookies/ | 0 → 0 | 0 → 0 | n/a | 0 → 0 | 114 → 118 | 0 → 0 |
| /404.html | 0 → 0 | 0 → 0 | n/a | 0 → 0 | 78 → 82 | 0 → 0 |
| /admin/ | 0 → 0 | n/a | n/a | 0 → 0 | 692 → 692 | 0 → 0 |
| /accessibility/ | new → 0 | new → 0 | n/a | new → 0 | new → 130 | new → 0 |

**Totals.** Outside forced colors, there are 0 violations before and after. The raw forced-colors column is 2,686 → 2,856 nodes, all `color-contrast`. It rises only because of the new footer link and the new page. Measured on the painted color, it is 0 → 0.

**Why the raw forced-colors count is not a real failure.** Under forced colors, Chromium paints text in the forced system color, and `getComputedStyle().color` reports that color. The computed `-webkit-text-fill-color`, however, keeps the author color. axe reads `-webkit-text-fill-color` before `color` (axe.js line 25340), so it measures, for example, `#94a3b8` on the forced white Canvas. To check what is actually drawn, element screenshots were decoded under forced colors: 31 elements on /, /contact/, /privacy/ and /accessibility/, covering `.lead`, `.line.accent`, `.eyebrow`, `.meta`, `.nav-link`, `.btn`, footer links, `.prose p`, `.contact-label` and `.form-note`. In every one, the ink was the forced color: black `0,0,0`, or navy `0,0,159` for links, on white `255,255,255`. It was never the author color axe reports.

The “painted color” column re-runs axe in the same page, with `-webkit-text-fill-color` hidden from axe so it reads the painted color. This is a test-harness correction, not a site change; the site sets `-webkit-text-fill-color` only on autofilled inputs. Changing the CSS just to satisfy the tool would risk the real system colors, so it was left as is.

**Incomplete.** 116 `color-contrast` nodes, the same before and after, come back “needs review” outside forced colors. They are on /contact/ (the `select`’s background image), and on the /privacy/ and /refunds/ tables inside the horizontally scrolling region, where axe can’t see the background. Those pairs are in the Contrast section’s computed ratios.

## Manual

Probes were Playwright scripts run on every page. The accessibility tree came from `ariaSnapshot()` and the CDP `Accessibility.getFullAXTree`. “All pages” means the 11 visitor pages; /admin/ is the owner’s internal checklist and is covered by axe only.

| Criterion | Result | Evidence |
|---|---|---|
| 1.3.1 / 1.3.2 One h1, headings | **Fail → fixed** | Every page has exactly one `h1` and no skipped heading levels. The footer column labels “Pages”, “Contact” and “Legal” looked like headings but were `<p class="eyebrow footer-heading">`, so the tree read them as “paragraph: Pages”. They are now `<h2 class="eyebrow footer-heading">` on every page. The computed font, size, weight, spacing, color, position and box are identical at 375 and 1280px. |
| 1.3.1 Lists | Pass | Nav, footer, offer grid, checklists and legal lists are `ul`/`li`. Lists with `list-style: none` carry `role="list"`, and the tree shows `list`/`listitem`. |
| 1.3.1 Tables | **Fail → fixed** | The /privacy/ data-sharing table had no `<caption>` and was exposed as an unnamed “table”. It now has a visually hidden caption, matching /refunds/, and the tree reads `table "Services that handle data for us, what each gets and its privacy policy"`. Every `th` on both tables has `scope`: 13 of 13 on /privacy/, 8 of 8 on /refunds/. |
| 1.3.1 Landmarks | Pass | Every page has banner, `nav "Main"`, main, contentinfo, `nav "Footer"` and `nav "Legal"`. The home sections, the contact form and the scrollable table regions are named by their headings or labels. No visible text lies outside a landmark except the skip link. |
| 1.3.2 Reading order | Pass | The DOM order matches the visual order at every width. The accessibility-tree order for /, /contact/ and /privacy/ is below. |
| 1.3.5 Autocomplete | Pass | Name `name`, Email `email`, Business or current website `organization`. Service and Message have no matching input purpose. The honeypot is `off`. |
| 1.4.4 / 1.4.10 Resize, reflow | Pass | No page-level horizontal scroll on any page at 320×800, 640×400 (1280 at 200%) or 320×200 (1280 at 400%), including with the menu open. Wide tables scroll inside `.table-scroll` (allowed for data tables). The showcase frame’s tab title “grisha.studio - Artist \| NYC Artist Portfolio” is cut off with an ellipsis at 320 and 375px, as it was before, because it imitates a browser tab. The full title is its link’s accessible name, and the site name and link are shown in full in the “Client: Grisha.studio” line above. |
| 1.4.12 Text spacing | Pass | Injected `line-height: 1.5`, `letter-spacing: .12em`, `word-spacing: .16em` and `p { margin-bottom: 2em }`, all `!important`, at 320 and 1280px on every page. No element with `overflow: hidden/clip` cuts text, and no button, input, menu toggle or skip-link content leaves its box. Kerned punctuation (`kern-dot`, `kern-apos` on the /, /contact/, /contact/thanks/ and 404 headlines): each glyph’s box starts exactly its negative margin (0.1em, 0.07em) inside the previous glyph’s box, which now includes the added 0.12em letter spacing. So the dot or apostrophe sits 0.02–0.06em clear of its neighbours, on the same line; nothing overlaps. The showcase tab title is cut off at 320/375px with or without the overrides, and shows in full at 768px and up even with them. |
| 1.4.13 Content on hover or focus | **Fail → fixed** | No tooltips, `title` attributes, hover menus or focus pop-ups. The skip link showing on focus is the focused control itself. A stray selector from Prompt 14 (`.meta a:hover, .icon-inline { width: .75em; … }`) gave the “Grisha.studio” link on / the icon’s 0.75em box on hover. Sampled every 30ms with the pointer at rest on it, the link flipped between 88px and 11px wide and in and out of `:hover`, so it flickered and was hard to click. The rule is now split: hover only darkens the underline, and 8 of 8 samples stay 88px and hovered. |
| 2.2.2 / 2.3.1 Motion, flashing | Pass | No `@keyframes`, `animation`, autoplay, video, GIF, carousel or timer in `public/` (the /solutions/ “animations” is a tier description). Only 0.15s color/transform transitions, which `prefers-reduced-motion: reduce` cuts to 0.01ms. Nothing flashes. |
| 2.4.2 Page titled | Pass | 12 titles, 12 unique, each “Topic \| Tech-Savvies” (the home page leads with the brand). |
| 2.5.8 Target size | Pass | Every link, button and field was measured at 320 (menu closed and open) and 1280px. Buttons, the toggle and fields are ≥ 40px. Smaller targets (footer and desktop nav links) pass the spacing exception: a 24px circle on each touches no other target or circle. In-sentence links are exempt. 0 failures on every page, including the new footer link. |
| 3.1.1 Language | Pass | `<html lang="en">` on all 12 files. |
| 3.2.3 / 3.2.4 / 3.2.6 Consistency | Pass | Header and footer links (href and text) are in the same order on every page (compared to /). Names match the glossary in `microcopy.md`. The help mechanisms (header Contact button, footer email, footer Contact link) sit in the same place on every page. |
| 3.3.7 Redundant entry | Pass | The only process is the one-step contact form; nothing is asked twice. |
| 3.3.8 Accessible authentication | Pass | No login, password or CAPTCHA anywhere (the honeypot is invisible and needs nothing from people). |
| 4.1.2 Name, role, value | **Fail → fixed** | Menu toggle `button "Menu"` with `expanded` false/true. Every field has a label; required text fields are `required=true`. The Service `select` (a required select with an empty first option) was exposed as `invalid=true` on page load, before anything was entered. It now has `aria-invalid="false"`, and `main.js` sets `"false"` rather than removing the attribute when an error clears; the tree shows `invalid="false"` on load and `"true"` only with an error. |
| 4.1.2 Required state of the select | **Needs manual screen-reader check** | Chromium’s tree doesn’t report `required` for the combobox, even with `aria-required` (tested in isolation). “All fields are required unless marked (optional).” is stated in text above the form, so 3.3.2 is met either way. |
| 4.1.3 Status messages | **Fail → fixed** | *Errors on submit* need no live region. Focus moves to the first invalid field, and its accessible description is the error (the tree shows `textbox "Name" … desc="Error: Enter your name." focused`). A live region would announce twice. *Errors on leaving a field* did need one. The `change` check shows the error after focus has moved on (for example, focus on Business while “Error: Enter an email address like name@example.com.” appears under Email), and nothing was announced. *“Sending…”* also needed one: the button text changes and the button is disabled, with no focus change. Fix: an empty `<p class="visually-hidden" id="form-status" role="status">` in the form (tree: `status`, `live="polite"`). `main.js` puts the error text there on `change` and “Sending your message…” on a valid submit, and clears it on submit errors, on a fixed field and on `pageshow`. Verified: leaving Email as “bob” → status carries the error while focus is on Business; empty submit → status empty, focus on Name; valid submit → button “Sending…” disabled, status “Sending your message…”. |

### Accessibility tree: reading order and names

Read from Chromium after the fixes (375px for / and /contact/, where the menu is closed, so the Main nav is out of the tree until opened; 1280px for /privacy/).

- **/**: link “Skip to content” → banner (link “Tech-Savvies NYC home” with img of the same name, button “Menu”) → main: heading 1 “Websites done fast. Websites done right.” (the `.line` spans are joined by a space) → lead → region “What we offer” (h2, list of three items each with an h3) → region “Featured Showcase” (h2, h3, paragraph, “Client:” paragraph with link “Grisha.studio (opens in a new tab)”, figure with link “grisha.studio - Artist \| NYC Artist Portfolio (opens in a new tab)” and the described img, list of three) → region “Start Your Project” (h2, paragraph, link “Start your project”) → contentinfo: logo link, tagline, navigation “Footer” (heading 2 “Pages”, list), heading 2 “Contact” with email link and “New York, NY”, navigation “Legal” (heading 2 “Legal”, five links), copyright.
- **/contact/**: … main: heading 1 “Let’s Upgrade Your Business.” (the kern span doesn’t split the word) → lead → heading 2 “Contact Info”, then label/value paragraphs (“Direct Email:” then link “info@tech-savvies.com”, “Business:”, “Location:”, “Replies:”; the colon carries the relationship) → heading 2 “Contact Form” → form “Contact Form”: required-fields note, textbox “Name”, textbox “Email”, textbox “Business or current website (optional)”, combobox “What do you need?” with five options, textbox “Message”, privacy notice with link “Privacy Policy (opens in a new tab)”, button “Send message” (described by the privacy notice), status (empty). The honeypot is not in the tree.
- **/privacy/**: … main: heading 1 “Privacy Policy”, “Last updated” with time, then h2/h3 sections in document order. region “Services that handle data for us” (focusable) contains table “Services that handle data for us, what each gets and its privacy policy” with four columnheaders and nine rowheaders (Netlify … ChatGPT, run by OpenAI) → contentinfo as on /.

### Fixed in this prompt

1. Footer column labels are `h2` on every page (1.3.1).
2. Caption on the /privacy/ table (1.3.1).
3. `.meta a:hover` no longer collapses the link (the stray `.icon-inline` selector is split out).
4. The Service select is no longer announced as invalid before input (4.1.2).
5. A `role="status"` region announces errors that appear after focus has moved on, and “Sending your message…” (4.1.3).
6. /accessibility/ published and linked from every footer’s Legal column. Each page gains one Tab stop (the footer Accessibility link), so the Keyboard section’s counts rise by one. /accessibility/ itself has 15 stops at 375px and 18 at 1280px; each has a 2px outline and none is under the header.

### Not tested here (owner action)

A real screen reader: VoiceOver (Safari, macOS and iOS) or NVDA (Firefox or Chrome, Windows). Check that the menu’s expanded state is read, the Service select is read as required, errors are read on submit and on leaving a field, “Sending your message…” is read, and the footer headings and table captions are read. Also check Safari and Firefox, and real Windows High Contrast, since this audit used Chromium emulation.

## Plain-text mirrors

Added 2026-09-29, after the owner’s decision recorded in `business-facts.md`. /accessibility/ offers these as the “information another way”. `tools/build_markdown.py` builds `public/<page>.md` from each page’s `<main>` and footer; there is none for /admin/. It also builds `public/llms.txt` and the mirrors’ headers in `netlify.toml`. Each HTML page links to its mirror with `<link rel="alternate" type="text/markdown">`. `check_site.py` (`markdown-mirrors`) and CI fail when a mirror is missing or stale.

What the builder does, and why:

- **Readable as raw text.** The header, logo, icons, scripts and “(opens in a new tab)” text are dropped. Links keep their visible text and gain a full `https://` address. Each Contact Info label is joined to its value (“**Replies:** No fixed hours…”). The contact form becomes a note that it works on the web page only, the required-fields line, the list of questions (with the Service choices) and the privacy notice.
- **Tables become lists.** Each /privacy/ and /refunds/ table row becomes a list item named by its row header, with each cell labelled by its column header. A pipe table read as plain text gives a screen reader no headers. The table caption introduces the list.
- **Structure kept.** The page’s headings are kept in order, starting with its one `#` heading. After it come the page address and the meta description as a “Summary:”, for AI tools and skimming. Two lists in a row use different markers (`-`, then `*`) so Markdown doesn’t merge them. The home page image keeps its alt text.
- **Served as `text/plain; charset=utf-8`.** Without a charset, Chromium showed the curly quotes as “â€œ” (checked with the local server, which sends `text/markdown` with no charset). `text/plain` is shown inline by every browser. Indexable mirrors carry `Link: <HTML page>; rel="canonical"`; the 404 and thanks mirrors carry `X-Robots-Tag: noindex`, like their HTML pages.

Checked:

- **Rendered with markdown-it 14 (CommonMark):** each of the 11 mirrors has one h1, no skipped heading levels, the image with alt text, only absolute links, no generic link text and no stray escapes. axe on the rendered HTML reports only `target-size` on unstyled footer links, which depends on the Markdown viewer, not on the file.
- **Word comparison with the HTML:** every word of `<main>` and the footer is in the mirror. The exceptions are the tables’ first column header (“Service”), whose values start each list item, and the “(opens in a new tab)” text.
- **axe matrix re-run on the HTML pages after this change:** 0 violations outside forced colors. Forced colors: 2,868 raw nodes (12 more, from the three new links on /accessibility/ at four widths) and 0 on the painted color.
