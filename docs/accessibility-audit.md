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
