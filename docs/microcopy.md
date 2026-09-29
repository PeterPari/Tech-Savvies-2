# Microcopy Rules

Microcopy is the text that labels controls (buttons, links, form fields). Clear labels help both keyboard users and people using assistive technology. Follow these rules for every control.

## Rules

Each rule fits in one line. Every new label must follow all of them before going on the site.

| # | Rule | Example |
|---|------|---------|
| 1 | Name the action or destination | "Download report" not "Click here" |
| 2 | Start the accessible name with the visible text | visible "Contact", aria-label "Get in touch" ✗ (rename to visible "Get in touch", no aria-label) |
| 3 | Use the same words for the same destination everywhere | "Terms of Service" everywhere, not "Terms" or "T&C" |
| 4 | Show the email address or start with "Email" | "info@tech-savvies.com" or "Email our support team", not just "Contact us" |
| 5 | Tell the user external links open in a new tab | visible "Privacy Policy", visually hidden " (opens in a new tab)" |
| 6 | Give icon-only controls a text name | `<button><svg>...</svg></button>` needs `<span class="visually-hidden">Menu</span>` |
| 7 | Name the action after error states | Submit button text stays "Send message" even after form validation fails |

## Canonical Labels Glossary

Use these exact labels for recurring controls and destinations. If a page or section renames one, update the glossary.

### Primary navigation

- **Home:** homepage, always navigate to /
- **Solutions:** services page, always navigate to /solutions/
- **Our Story:** about page, always navigate to /our-story/
- **Contact:** contact form page, always navigate to /contact/
- **Menu:** mobile menu toggle button (aria-label not needed)
- **Skip to content:** skip link to #main

### Policies and legal

- **Terms of Service:** legal page at /terms/
- **Refund Policy:** cancellation and refund page at /refunds/
- **Privacy Policy:** privacy page at /privacy/
- **Cookie Policy:** cookies and tracking page at /cookies/
- **Accessibility:** accessibility statement at /accessibility/ (footer Legal column)

### Contact and data

- **Send message:** submit button on the contact form
- **Email a data request:** mailto link to request user data (subject line includes "request")
- **info@tech-savvies.com:** direct email address (always shown in full)

### Navigation within pages

- **Back to home:** link from /contact/thanks/ to /
- **Contact Peter:** link to /contact/ from /our-story/
- **Read our Cookie Policy:** link from /privacy/ to /cookies/

### External links

- **Grisha.studio:** showcase client's site (always includes "(opens in a new tab)" visually hidden text)

## Checking Your Work

Before posting a label:

1. **Is it clear?** Would someone know what happens if they click it?
2. **Is it consistent?** Does the same destination use the same words on every page?
3. **Is it complete?** Does it name the action, destination or both?
4. **Is it accessible?** Can a screen reader read it? Does the visible text match the start of the accessible name?

## Linked from README

This file is linked from the README "Editing" section under "Microcopy and labels".
