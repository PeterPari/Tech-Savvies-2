# Compliance log

One row per item in [`fix-plan.md`](../fix-plan.md). Status starts as the "Status today" from
plan §1 (audit of 2026-09-28). Each prompt updates its row: status, commit hash, and anything
left for the owner.

| # | Item | Status | Prompt | Commit | Owner follow-ups |
|---|------|--------|--------|--------|------------------|
| 1 | Privacy policy | Missing | [01](../fix-prompts/01-privacy-policy.md) | | Mailing address, retention, mailbox provider. Netlify Analytics is on (owner, 2026-09-29), so the policy must disclose it |
| 2 | Terms of service | Missing | [02](../fix-prompts/02-terms-of-service.md) | | Payment, ownership and monthly-plan facts. Contract signer is under 18 (see #17) |
| 3 | Refund policy | Missing | [03](../fix-prompts/03-refund-policy.md) | | Refund rules and what the completion guarantee promises |
| 4 | Cookie policy | Missing (nothing to disclose) | [04](../fix-prompts/04-cookie-policy.md) | | |
| 5 | Cookie consent banner | Not needed today, verify and guard | [05](../fix-prompts/05-cookie-consent.md) | | Confirm Netlify Analytics (on) sets no cookies; it is server-side |
| 6 | Form consent | Missing notice | [06](../fix-prompts/06-form-consent.md) | | |
| 7 | Only collect necessary data | Mostly OK | [07](../fix-prompts/07-data-minimization.md) | | Retention rule. Netlify spam filtering is off (honeypot only) |
| 8 | Third-party SDKs / embeds | Clean, document and guard | [08](../fix-prompts/08-third-party-audit.md) | | Mailbox provider |
| 9 | Dark patterns | None found in UI; 1 pricing issue | [09](../fix-prompts/09-dark-patterns.md) | | Monthly price (see #10) |
| 10 | Hidden fees | Present | [10](../fix-prompts/10-hidden-fees.md) | | Rush price for Launch and the domain/hosting cost figure. Sales tax: prices exclude tax and the owner needs advice on whether it applies |
| 11 | Fake reviews | None present, verify and guard | [11](../fix-prompts/11-fake-reviews.md) | | Grisha.studio is a real client with written permission; the owner’s brother runs it (2026-09-29). The owner wants the connection kept off the homepage. It must still be disclosed clearly next to the case study, or be easy to find, so it doesn’t mislead |
| 12 | Unsupported claims | Present | [12](../fix-prompts/12-unsupported-claims.md) | | Replace “2 hours” with 1 business day, “5 days” with rush-only, and drop “NYC business hours” |
| 13 | Alt text | Passes, guard | [13](../fix-prompts/13-alt-text.md) | | |
| 14 | Color contrast | Passes AA, 1 gap | [14](../fix-prompts/14-color-contrast.md) | | |
| 15 | Keyboard navigation | 1 real bug | [15](../fix-prompts/15-keyboard-navigation.md) | | |
| 16 | Real business details | Missing | [16](../fix-prompts/16-business-details.md) | | Legal name (owner unsure; own full legal name for a sole proprietor). No physical address (online-only), so the site shows email only. No fixed hours: the “NYC business hours” promise must go |
| 17 | Age consent for kids' data | Missing statement | [17](../fix-prompts/17-age-consent.md) | | Owner says the contract signer is under 18. Minors' capacity to contract is limited, so a parent/guardian or an adult signer is likely needed; get legal advice |
| 18 | Unsubscribe link in emails | N/A today, policy needed | [18](../fix-prompts/18-email-unsubscribe.md) | | No marketing email planned (owner, 2026-09-29) |
| 19 | License fonts/images | Fonts OK; images undocumented | [19](../fix-prompts/19-asset-licenses.md) | | Which AI tool made the OG image and icons, and its terms; Canva license for the logo; screenshot source |
| 20 | Data deletion request | Missing | [20](../fix-prompts/20-data-deletion.md) | | Retention periods |
| 21 | Fix accessibility | Good base; 3 fixes + statement | [21](../fix-prompts/21-accessibility-audit.md) | | |
| 22 | Copyright on images | Unverified | [22](../fix-prompts/22-image-copyright.md) | | Creator and tool for logo/OG image; legal entity name for the copyright line |
| 23 | Tracking | None in code; Netlify Analytics is on | [23](../fix-prompts/23-tracking-check.md) | | Netlify Analytics is on in the dashboard (owner, 2026-09-29); the audit and Privacy Policy must reflect it. No email open-tracking |
| 24 | Local laws | Not reviewed | [24](../fix-prompts/24-local-laws.md) | | DBA not filed (NY GBL §130); minor contract signer |
| 25 | Clear button labels | Passes, guard | [25](../fix-prompts/25-button-labels.md) | | |

## Problems found by `tools/check_site.py`

None on the current tree.
