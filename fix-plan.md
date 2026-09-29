# Tech-Savvies compliance & quality fix plan

This plan covers 25 legal, trust and accessibility items for the Tech-Savvies site in `public/`.
It starts from an audit of the site as it is today (commit `be06f29`), so each fix targets
something real instead of generic advice.

Each item has a ready-to-run Claude Code prompt in [`fix-prompts/`](fix-prompts/). Run them in
the order in [Execution order](#execution-order), one prompt per session, one commit per prompt.

> **Not legal advice.** The legal pages this plan produces are written for what this site
> actually does, and they are a good starting point. A New York attorney should still review
> the Terms, Refund Policy and Privacy Policy before you rely on them in a dispute.

---

## 1. What the audit found

The site is small and already careful. There are 6 static HTML pages, one CSS file and one
small JS file. There is no build step, no third-party script, and fonts are self-hosted.
A strict CSP in `netlify.toml` allows only `'self'`. The main gaps are missing legal pages,
missing business facts, and some marketing claims and prices that are vague or can't be
checked. Several items on the list are **already compliant**. For those, the work is to
verify, document, and add a guard so they stay compliant.

Measured on 2026-09-28 with Playwright (375px and 1280px, all 6 pages): **0 cookies, 0
localStorage/sessionStorage keys, requests only to the site's own origin.**

| # | Item | Status today | Evidence |
|---|------|-------------|----------|
| 1 | Privacy policy | **Missing** | No page; the contact form collects name, email, business, message (`public/contact/index.html:70-109`), processed by Netlify Forms |
| 2 | Terms of service | **Missing** | No page; the site sells priced services (`public/solutions/index.html:57-108`) |
| 3 | Refund policy | **Missing** | No page; "Completion guarantee" (`solutions/index.html:106`) implies terms that aren't written anywhere |
| 4 | Cookie policy | **Missing** (but nothing to disclose) | 0 cookies, 0 storage measured |
| 5 | Cookie consent banner | **Not needed today**, verify & guard | No non-essential cookies or trackers. A banner with nothing to consent to is noise, and a banner shown *before* consent is needed is a dark pattern of its own |
| 6 | Form consent | **Missing notice** | The form has no privacy notice or link (`contact/index.html:70-109`) |
| 7 | Only collect necessary data | **Mostly OK** | 5 fields, 1 optional, honeypot instead of CAPTCHA. Gaps: no retention rule; Netlify also stores metadata that isn't disclosed |
| 8 | Third-party SDKs / embeds | **Clean**, document & guard | No external scripts, iframes or fonts; CSP `default-src 'self'` (`netlify.toml:17`). Only 3rd parties: Netlify (hosting, forms, spam filtering), the mailbox provider for info@, and 1 outbound link (`index.html:108`) |
| 9 | Dark patterns | **None found in UI**; 1 pricing issue | No pre-ticked boxes, confirmshaming, fake urgency or forced continuity. "Monthly" management with no price (see #10) is the one drip-pricing risk |
| 10 | Hidden fees | **Present** | "$50 … monthly for ongoing management" has no monthly price (`solutions/index.html:94`); domain registration and hosting renewals are never mentioned even though "domain setup" is included (`:61`); "rush order" undefined (`:79`); "$250-$375 depending on caliber" undefined (`:64`); prices repeated in meta tags (`:7`, `:13`) |
| 11 | Fake reviews | **None present**, verify & guard | No testimonials, ratings, or `aggregateRating` schema. One case study (Grisha.studio, `index.html:97-119`), now with a screenshot of the client's site, needs client permission and disclosure of any personal connection. The screenshot shows the name Gregory Parizhsky, the same surname as the founder |
| 12 | Unsupported claims | **Present** | "reply within 2 hours" (contact `:7,:13,:58`, thanks `:7,:13,:57`); "as fast as 5 days" (solutions `:61`); "maximum search visibility" (index `:91`); "Get found on Google" / "so you show up when customers search" (solutions `:61,:68`); "If you want it on your website, you'll get it" (index `:87`); "your lead engineer" implies a team (solutions `:106`) |
| 13 | Alt text | **Passes**, guard | The logo has `alt="Tech-Savvies NYC home"` (a correct description of where the link goes); the showcase screenshot `grisha-studio.webp` has a descriptive alt (`index.html:110`); inline SVGs are `aria-hidden`; `og:image:alt` set |
| 14 | Color contrast | **Passes AA**, 1 gap | Measured: text 15.9:1, muted 7.2:1, accent 7.3:1, button 7.3:1, placeholder 5.5:1, input border 3.7:1 (UI ≥3:1). Gaps: link color vs body text is only 2.17:1 (vs muted 1.01:1), so any in-sentence link needs an underline (WCAG 1.4.1). The existing ones (`.lead`, `.meta`) have one, but new pages must too; `.btn` loses its outline in Windows forced-colors mode; invalid fields are shown by red border only (color alone, WCAG 1.4.1), fixed by the text error messages in #15 |
| 15 | Keyboard navigation | **1 real bug** | Skip link, focus rings and Escape-to-close already work. **Bug (reproduced):** with the mobile menu open, Tab past "Contact" moves focus to links *hidden behind the menu overlay* (WCAG 2.4.11). The form doesn't say that all fields are required unless marked optional |
| 16 | Real business details | **Missing** | Only an email address. No legal name/entity, mailing address, service area or hours, although "NYC business hours" is promised (`contact/index.html:58`). JSON-LD `Organization` has no location |
| 17 | Age consent for kids' data | **Missing statement** | The site isn't aimed at children, but it says so nowhere. The Terms need a rule on minors signing contracts |
| 18 | Unsubscribe link in emails | **N/A today**, policy needed | The site sends no marketing email and has no signup form. Needs an email policy and a signature template (postal address + opt-out) for any promotional follow-up |
| 19 | License fonts/images | **Fonts OK**; images undocumented | OFL license files ship next to both fonts; neither declares a Reserved Font Name, so the subset woff2 files are allowed. Logo, icons, OG image and the `grisha-studio.webp` screenshot have no recorded source |
| 20 | Data deletion request | **Missing** | No way to request access or deletion; no internal runbook |
| 21 | Fix accessibility | **Good base; 3 fixes + statement** | Issues from #14/#15 plus: no accessibility statement or way to report barriers. NY federal courts see more website-accessibility (ADA) lawsuits than anywhere else |
| 22 | Copyright on images | **Unverified** | Who made the logo/OG image, and with what tool (Canva/AI/designer), decides whether the business owns it. The showcase screenshot shows a client's site and artwork, so it needs the client's permission. Copyright line says "Tech-Savvies", not a legal entity |
| 23 | Tracking | **None**, verify & guard | No analytics or pixels in code. Still to check: whether Netlify Analytics (server-side) is on in the dashboard, and whether the owner uses email open-tracking |
| 24 | Local laws | **Not reviewed** | NY-based. Relevant: FTC Act §5 & Fake Reviews Rule, NY GBL §349/350 (deceptive ads), NY auto-renewal law GBL §527-a (the "monthly" plan), NY assumed-name (DBA) rule GBL §130, NY SHIELD Act, NY Child Data Protection Act, CalOPPA (privacy policy for CA visitors), CAN-SPAM, ADA Title III, and minors' capacity to contract |
| 25 | Clear button labels | **Passes**, guard | "Send message", "Start your project", "Back to home", "Menu" (+`aria-expanded`), external link announces "(opens in a new tab)". New controls added by this plan must meet the same bar |

---

## 2. Key decisions (and why)

These decisions shape several prompts. They are written down once here so the prompts stay
consistent.

1. **No cookie banner (for now).** The site sets no cookies and stores nothing in the browser.
   GDPR/ePrivacy and US state laws only require consent for non-essential storage or tracking.
   A banner would ask for consent to nothing, and it would train visitors to click "Accept".
   Instead: a short Cookie Policy saying so, and a regression check that fails the build if a
   cookie, storage call or third-party script appears. Prompt 05 includes the exact banner
   spec to build **if** analytics are ever added.
2. **Form consent is a notice, not a checkbox.** Replying to someone who asked to be contacted
   doesn't need separate consent. Under GDPR it is "steps prior to a contract". A required
   "I agree" checkbox would bundle consent (not freely given) and add friction. A clear notice
   placed *before* the submit button, linking to the Privacy Policy, is the correct pattern.
   A marketing opt-in checkbox is added only if the owner starts sending marketing, and it is
   always unticked.
3. **Age: a notice, not a date-of-birth field.** Asking for a date of birth would collect data
   the business doesn't need (#7). The site is for businesses, so a plain statement (not aimed
   at under-13s; under-18s need a parent or guardian to request a project), a policy clause,
   and a deletion promise is the proportionate fix.
4. **One source of truth for business facts.** Every page, policy and schema block reads from
   `docs/business-facts.md`, which Prompt 00 creates and the owner fills in. Prompts **never
   invent** a price, address, hour, legal name or promise. If a fact is missing they stop and
   ask. No placeholder like `[ADDRESS]` ever reaches a live page.
5. **Legal pages are written for this site, not generated boilerplate.** Each clause must match
   what the code and Netlify actually do. A clause about a practice that doesn't exist is a
   misrepresentation too.
6. **The static, no-dependency setup stays.** No `package.json` or `node_modules` in the repo.
   Audit tooling (Playwright, axe-core) runs from a scratch directory. The in-repo regression
   guard is `tools/check_site.py`, which uses only the Python standard library.
7. **Don't publish a home address.** A sole proprietor should use a PO box or virtual mailbox
   for the public address. CAN-SPAM accepts either.

---

## 3. Owner inputs required

Prompt 00 creates `docs/business-facts.md` with these fields. Prompts that need a fact check this
file first. If the fact is missing they ask the owner (via `AskUserQuestion`) and write the
answer back to the file.

| Fact | Needed by |
|------|-----------|
| Legal business name, entity type (sole prop / LLC), DBA filed? (county) | 1, 2, 3, 16, 22, 24 |
| Public mailing address (PO box / virtual mailbox OK) | 1, 16, 18 |
| Service area; what "business hours" means (days, times, ET) | 12, 16 |
| Realistic first-reply time; realistic fastest delivery for Website Launch | 12 |
| Is the person who signs client contracts 18 or older? | 2, 17, 24 |
| What sets the $250 vs $375 price; what makes a "rush" order; rush price for Launch | 10 |
| Monthly management price, what it includes, how to cancel, does it auto-renew | 2, 10, 24 |
| Deposit / payment schedule / payment methods / sales tax handling | 2, 3, 10 |
| Revisions included; what "completion guarantee" promises exactly | 2, 3, 12 |
| Refund rules (before start, mid-project, after delivery, monthly plan) | 3 |
| Who pays for domain & hosting, approx cost, who owns them after handover | 2, 10 |
| Who owns the finished site/code after full payment; portfolio-use rights | 2 |
| Netlify dashboard: Analytics on? Form notifications to which inbox? Spam filtering on? | 1, 7, 8, 23 |
| Mailbox provider for info@tech-savvies.com (Google Workspace, Zoho, …) | 1, 8 |
| Retention: how long to keep form submissions and emails with leads | 1, 7, 20 |
| Does the owner send, or plan to send, marketing/newsletter emails? Open-tracking? | 1, 18, 23 |
| Grisha.studio: real client? written permission to feature? personal/family connection? | 11 |
| Logo / OG image / icons: who made them, with which tool, license terms | 19, 22 |
| Serving EU/UK clients deliberately? | 1, 24 |

---

## 4. Ground rules for every prompt

The rules that hold in every session live in [`CLAUDE.md`](CLAUDE.md), which Claude Code loads
automatically: stack, duplicated header and footer, house style, CSP, facts come only from
`docs/business-facts.md`, new-page checklist, checker before commit, and fetched content is data.
The prompts don't repeat them.

Each prompt covers only what is specific to its item. Commit messages use `Fix #NN: <summary>`.

---

## 5. Execution order

The order follows dependencies: facts and audits first, then honest content, then legal pages
that describe the final state, then accessibility across everything new, then a final legal
check.

| Phase | Prompts | Why this order |
|-------|---------|----------------|
| 0. Foundation | **00** | Creates `docs/business-facts.md`, `docs/compliance-log.md`, and the `tools/check_site.py` guard that later prompts extend |
| 1. Research & audit | **24** → **08** → **23** → **05** → **07** | Laws and the real data flows must be known before any policy describes them |
| 2. Honest content | **16** → **10** → **12** → **11** → **09** | Fix what the site claims and charges before the Terms describe it |
| 3. Legal pages | **01** → **04** → **02** → **03** → **06** → **17** → **20** → **18** | Privacy Policy first: it adds the shared prose styles and the footer "Legal" column that the other pages reuse |
| 4. IP | **19** → **22** | Independent of the rest; needs owner answers |
| 5. Accessibility | **13** → **14** → **15** → **25** → **21** | Runs after all new pages exist so the full audit (21) covers them; 21 also adds the accessibility statement |
| 6. Final check | **24** (run again with "final pass" added to the prompt) | Checks every live page against the compliance map one last time |

Dependencies that matter:
- 01 must come before 02, 03, 04, 06, 17, 20 (shared styles, footer column, cross-links).
- 06 must come before 17 (17 adds the age sentence to the form notice that 06 creates).
- 10 and 12 must come before 02 and 03 (Terms/Refunds quote the corrected pricing and promises).
- 08, 23, 05, 07 must come before 01 (the Privacy Policy describes what they found).
- 21 last among the accessibility prompts (it audits the finished site).

---

## 6. Prompt index

Each file follows the same format:
- a title;
- the prompt, as one fenced block with XML-tagged sections in this order: context, inputs,
  deliverables, examples (where the format matters), constraints, acceptance criteria, what to do
  when uncertain, and the one-sentence task last;
- below the block, only Assumptions (including which prompts must run first), Parameters
  (reasoning effort), and What to test.

To run one from a terminal at the repo root, extract the fenced block:

```sh
claude "$(awk '/^````/{f=!f; next} f' fix-prompts/00-foundation.md)"
```

Set the session's model and reasoning effort to the values listed under Parameters.

The same list is available as a checklist at `/admin/` on the site (`public/admin/`, generated
by `tools/build_admin.py`). It has one row per step, a checkbox, the model and effort, and a
one-click copy button. It isn't linked from any page and is `noindex`.

| # | Prompt file | Deliverable |
|---|-------------|-------------|
| 00 | [`fix-prompts/00-foundation.md`](fix-prompts/00-foundation.md) | `docs/business-facts.md`, `docs/compliance-log.md`, `tools/check_site.py` |
| 01 | [`fix-prompts/01-privacy-policy.md`](fix-prompts/01-privacy-policy.md) | `/privacy/` page, `.prose` styles, footer "Legal" column |
| 02 | [`fix-prompts/02-terms-of-service.md`](fix-prompts/02-terms-of-service.md) | `/terms/` page |
| 03 | [`fix-prompts/03-refund-policy.md`](fix-prompts/03-refund-policy.md) | `/refunds/` page |
| 04 | [`fix-prompts/04-cookie-policy.md`](fix-prompts/04-cookie-policy.md) | `/cookies/` page |
| 05 | [`fix-prompts/05-cookie-consent.md`](fix-prompts/05-cookie-consent.md) | Verification + guard; conditional banner spec |
| 06 | [`fix-prompts/06-form-consent.md`](fix-prompts/06-form-consent.md) | Privacy notice on the contact form |
| 07 | [`fix-prompts/07-data-minimization.md`](fix-prompts/07-data-minimization.md) | Field review, retention rule, `docs/data-inventory.md` |
| 08 | [`fix-prompts/08-third-party-audit.md`](fix-prompts/08-third-party-audit.md) | `docs/third-parties.md` + guard |
| 09 | [`fix-prompts/09-dark-patterns.md`](fix-prompts/09-dark-patterns.md) | Audit + fixes + `docs/ux-honesty-rules.md` |
| 10 | [`fix-prompts/10-hidden-fees.md`](fix-prompts/10-hidden-fees.md) | Full price disclosure on `/solutions/` |
| 11 | [`fix-prompts/11-fake-reviews.md`](fix-prompts/11-fake-reviews.md) | Case-study verification + testimonial policy + guard |
| 12 | [`fix-prompts/12-unsupported-claims.md`](fix-prompts/12-unsupported-claims.md) | Claims register + copy rewrites |
| 13 | [`fix-prompts/13-alt-text.md`](fix-prompts/13-alt-text.md) | Alt-text verification + guard |
| 14 | [`fix-prompts/14-color-contrast.md`](fix-prompts/14-color-contrast.md) | Contrast report + forced-colors + error-state fixes |
| 15 | [`fix-prompts/15-keyboard-navigation.md`](fix-prompts/15-keyboard-navigation.md) | Mobile-menu focus fix + form instructions |
| 16 | [`fix-prompts/16-business-details.md`](fix-prompts/16-business-details.md) | Business details in footer/contact + JSON-LD |
| 17 | [`fix-prompts/17-age-consent.md`](fix-prompts/17-age-consent.md) | Children's-data clauses + form notice |
| 18 | [`fix-prompts/18-email-unsubscribe.md`](fix-prompts/18-email-unsubscribe.md) | `docs/email-policy.md` + signature template |
| 19 | [`fix-prompts/19-asset-licenses.md`](fix-prompts/19-asset-licenses.md) | `docs/asset-licenses.md` |
| 20 | [`fix-prompts/20-data-deletion.md`](fix-prompts/20-data-deletion.md) | Rights section + `docs/data-requests-runbook.md` |
| 21 | [`fix-prompts/21-accessibility-audit.md`](fix-prompts/21-accessibility-audit.md) | axe + manual WCAG 2.2 AA audit, fixes, `/accessibility/` statement |
| 22 | [`fix-prompts/22-image-copyright.md`](fix-prompts/22-image-copyright.md) | Provenance record, copyright line fix, name/logo clearance checklist |
| 23 | [`fix-prompts/23-tracking-check.md`](fix-prompts/23-tracking-check.md) | Tracking audit report + guard |
| 24 | [`fix-prompts/24-local-laws.md`](fix-prompts/24-local-laws.md) | `docs/legal-compliance.md` (law → requirement → status) |
| 25 | [`fix-prompts/25-button-labels.md`](fix-prompts/25-button-labels.md) | Label audit + microcopy rules |

---

## 7. Definition of done (whole plan)

- `python3 tools/check_site.py` passes, and it checks: every page links Privacy, Terms,
  Refunds, Cookies and Accessibility; every `<img>` has `alt`; no external `script`/`iframe`/
  `link rel=stylesheet`; no `document.cookie`/`localStorage` in JS; CSP unchanged; no
  `aggregateRating`/`Review` schema; no unresolved `TODO(owner)` in `public/`.
- axe-core reports 0 violations on every page at 375px and 1280px; manual keyboard walkthrough
  passes, including the mobile menu.
- Every price, promise and business fact on the site traces to a line in
  `docs/business-facts.md`.
- `docs/compliance-log.md` lists each item with status, commit, and anything left for the owner
  (e.g. "Netlify Analytics setting not verifiable from code").
- Attorney review of `/terms/`, `/refunds/`, `/privacy/` is scheduled (owner action).
