# Compliance log

One row per item in [`fix-plan.md`](../fix-plan.md). Status starts as the "Status today" from
plan §1 (audit of 2026-09-28). Each prompt updates its row: status, commit hash, and anything
left for the owner.

| # | Item | Status | Prompt | Commit | Owner follow-ups |
|---|------|--------|--------|--------|------------------|
| 1 | Privacy policy | Missing | [01](../fix-prompts/01-privacy-policy.md) | | Mailing address, retention, mailbox provider. Netlify Analytics is on (owner, 2026-09-29), so the policy must disclose it |
| 2 | Terms of service | Missing | [02](../fix-prompts/02-terms-of-service.md) | | Payment, ownership and monthly-plan facts. Contract signer is under 18 (see #17). The monthly plan does not auto-renew; clients re-book each month (owner, 2026-09-29), so #monthly-plan must not say “renews automatically” (see docs/legal-compliance.md) |
| 3 | Refund policy | Missing | [03](../fix-prompts/03-refund-policy.md) | | Refund rules and what the completion guarantee promises |
| 4 | Cookie policy | Missing (nothing to disclose) | [04](../fix-prompts/04-cookie-policy.md) | | |
| 5 | Cookie consent banner | Not needed today, verify and guard | [05](../fix-prompts/05-cookie-consent.md) | | Confirm Netlify Analytics (on) sets no cookies; it is server-side |
| 6 | Form consent | Missing notice | [06](../fix-prompts/06-form-consent.md) | | |
| 7 | Only collect necessary data | Mostly OK | [07](../fix-prompts/07-data-minimization.md) | | Retention rule. Netlify spam filtering is off (honeypot only) |
| 8 | Third-party SDKs / embeds | Clean, document and guard | [08](../fix-prompts/08-third-party-audit.md) | | Mailbox provider |
| 9 | Dark patterns | None found in UI; 1 pricing issue | [09](../fix-prompts/09-dark-patterns.md) | | Monthly price (see #10) |
| 10 | Hidden fees | Present | [10](../fix-prompts/10-hidden-fees.md) | | Sales tax: prices exclude tax and the owner needs advice on whether it applies |
| 11 | Fake reviews | None present, verify and guard | [11](../fix-prompts/11-fake-reviews.md) | | Grisha.studio is a real client with written permission; the owner’s brother runs it (2026-09-29). The owner wants the connection kept off the homepage. It must still be disclosed next to the case study itself: the FTC sources require the disclosure to be “unavoidable”, so “easy to find” behind a link isn’t enough. If the owner keeps it off the homepage, the case study moves off the homepage (see docs/legal-compliance.md) |
| 12 | Unsupported claims | Present | [12](../fix-prompts/12-unsupported-claims.md) | | Replace “2 hours” with 1 business day, “5 days” with rush-only, and drop “NYC business hours” |
| 13 | Alt text | Passes, guard | [13](../fix-prompts/13-alt-text.md) | | |
| 14 | Color contrast | Passes AA, 1 gap | [14](../fix-prompts/14-color-contrast.md) | | |
| 15 | Keyboard navigation | 1 real bug | [15](../fix-prompts/15-keyboard-navigation.md) | | |
| 16 | Real business details | Missing | [16](../fix-prompts/16-business-details.md) | | No physical address (online-only), so the site shows email only. No fixed hours: the “NYC business hours” promise must go |
| 17 | Age consent for kids' data | Missing statement | [17](../fix-prompts/17-age-consent.md) | | Owner says the contract signer is under 18. Minors' capacity to contract is limited, so a parent/guardian or an adult signer is likely needed; get legal advice |
| 18 | Unsubscribe link in emails | N/A today, policy needed | [18](../fix-prompts/18-email-unsubscribe.md) | | No marketing email planned (owner, 2026-09-29) |
| 19 | License fonts/images | Fonts OK; images undocumented | [19](../fix-prompts/19-asset-licenses.md) | | Screenshot source (logo is owner-drawn in Procreate; OG image and icons were coded by Claude Code) |
| 20 | Data deletion request | Missing | [20](../fix-prompts/20-data-deletion.md) | | Retention periods |
| 21 | Fix accessibility | Good base; 3 fixes + statement | [21](../fix-prompts/21-accessibility-audit.md) | | |
| 22 | Copyright on images | Unverified | [22](../fix-prompts/22-image-copyright.md) | | Copyright line should name Peter Parizhsky (sole proprietor); name/logo clearance |
| 23 | Tracking | None in code; Netlify Analytics is on | [23](../fix-prompts/23-tracking-check.md) | | Netlify Analytics is on in the dashboard (owner, 2026-09-29); the audit and Privacy Policy must reflect it. No email open-tracking |
| 24 | Local laws | Mapped in [`docs/legal-compliance.md`](legal-compliance.md) with requirements quoted from [`docs/legal-sources.md`](legal-sources.md) (official pages opened 2026-09-28) | [24](../fix-prompts/24-local-laws.md) | `Fix #24: fill legal compliance map from official sources` | File a DBA with the county clerk: until it’s filed you can’t sue on contracts made under “Tech-Savvies” (GBL §130(9)). Parent or guardian co-signs contracts (signer under 18). Attorney: Terms, Refunds, Privacy, and the “Unclear” rows (endorsements, CalOPPA, ADA, NY State Human Rights Law). Accountant: sales tax, vendor registration, record retention. Client logins fall under the SHIELD Act; keep them in a password manager and delete them after the work ends. Final pass still to run |
| 25 | Clear button labels | Passes, guard | [25](../fix-prompts/25-button-labels.md) | | |

## Problems found by `tools/check_site.py`

None on the current tree.
