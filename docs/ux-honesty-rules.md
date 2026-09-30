# UX honesty rules

Audit of every page and flow for dark patterns (FTC Act §5; FTC staff report “Bringing Dark
Patterns to Light”, 2022; NY GBL §527-a on hard-to-cancel subscriptions), and the rules new UI
must follow. Audited 2026-09-29 on the tree after Prompts 10–12.

Scope: `/`, `/solutions/`, `/our-story/`, `/contact/` (and its submit flow),
`/contact/thanks/`, `/404.html`, at 375px and 1280px. The owner’s internal
checklist at `public/admin/` (removed 2026-09-30) was out of scope. Checks run in Chromium: no horizontal
overflow at either width on any page, and zero checkboxes, radios or dialogs in the markup.

## Audit

| Category | Pages and flows checked | Result | Evidence | Fix |
|----------|------------------------|--------|----------|-----|
| False urgency and false scarcity | All pages; contact submit flow | Pass | No timers, “limited”, “only N left” or deadline copy (`grep` across `public/`). The 5-day rush is stated as a target with a price, not a countdown (`solutions/index.html:71`) | None |
| Confirmshaming | All pages; form submit | Pass | No decline choices exist. The only actions are “Start your project”, “Contact Peter”, “Send message”, “Back to home” | None |
| Pre-selected options | `/contact/` form | Pass | Service `<select>` starts on the empty “Choose a service” (`contact/index.html:101`); no checkboxes or radios anywhere | None |
| Hidden costs and drip pricing | `/solutions/` (375px, 1280px) | Fail, fixed | Prices, rush, costs outside the fee and payment terms are all on one page (`solutions/index.html:64-133`). The “Hosting … ($0)” checklist item dropped its condition (`solutions/index.html:79`) | Added “while it fits Netlify’s free plan” beside the $0 |
| Bait-and-switch | `/solutions/`, `/` | Pass | Headline “$250–$375” is followed by the tier that sets it and the rush rule in the same line (`solutions/index.html:64`). Home says it will tell the visitor “upfront if it’s outside the quoted price” (`index.html:90`) | None |
| Forced continuity (cancelling as easy as signing up) | Monthly plan on `/solutions/` | Pass | “Paid in full when you book each month; it doesn’t renew on its own, so there’s nothing to cancel” sits beside the $50/month price (`solutions/index.html:106`). Matches business-facts.md “Monthly management”: no auto-renewal | None; no extra cancellation sentence needed |
| Obstruction (deleting as easy as enquiring) | `/contact/`, footer | Pass | The enquiry channel is the address `info@tech-savvies.com`, linked in every footer and on `/contact/`. No deletion flow exists yet; Prompt 20 must reuse that address | None yet; rule below binds Prompt 20 |
| Misleading visual hierarchy | All pages | Pass | One primary `.btn` per view; nav “Contact” is the only nav button. No choice pairs styled unequally | None |
| Trick wording | `/contact/`, `/solutions/` | Pass | Labels are plain: “(optional)” on the one optional field, “Send message”. No double negatives | None |
| Nagging overlays | All pages | Pass | No modals, popups, banners or toasts. The only fixed element is the sticky header (`styles.css:421`); the mobile menu is opened by the visitor and closes on Escape | None |
| Disguised ads and undisclosed relationships | `/` showcase | Pass | No ads or affiliate links. The case study’s family tie and reduced rate are disclosed in its `.meta` line (`index.html:107`) | None |
| Privacy-unfriendly defaults | `/contact/`, all pages | Pass | No cookies or storage (docs/tracking-audit.md). Form asks six fields; none pre-filled. A consent notice for the form is Prompt 06’s job | None |
| Fake social proof | `/` | Pass | No ratings, counts, logos or reviews; one real, disclosed case study (docs/testimonials-policy.md) | None |
| Forced registration and unnecessary fields | `/contact/` submit flow | Pass | No account or login. Name, email, service and message are required; business is optional (`contact/index.html:94`). See docs/data-inventory.md | None |

## Rules for new UI

1. Choices of equal weight look equal.
2. No pre-ticked consent.
3. Declining takes no more steps than accepting.
4. Cancelling or deleting uses the same channel as signing up.
5. Every price is shown with its recurring terms.
6. No countdowns or “only N left” unless true and enforced automatically.
7. No guilt-trip decline wording.
8. Disclosures sit next to their claim.
