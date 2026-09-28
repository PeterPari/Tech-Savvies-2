# Prompt 06: Form consent (privacy notice at the point of collection)

Phase 3 (after 01). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 (especially Decision 2) and §4, then `docs/business-facts.md`,
`docs/data-inventory.md`, `docs/ux-honesty-rules.md` and `docs/compliance-log.md`. `/privacy/`
must exist.

## Goal

Tell people, right where they type their details, what the contact form data is used for, and
link to the Privacy Policy. Do it without a checkbox that isn't needed.

## Why

The contact form (`public/contact/index.html:71-105`) collects name, email, business and
message with no notice at all. Privacy law and good practice call for a "just-in-time" notice at
the point of collection: GDPR Art. 13 if EU visitors are relevant, the FTC's notice principles,
and the Privacy Policy we just published.

Why a notice and not an "I agree" checkbox: replying to someone who asked to be contacted is the
reason the form exists. A mandatory consent box would bundle consent with the service, which
means it isn't freely given under GDPR. It would also add friction and a false sense that
agreement is legally needed. The honest pattern is a clear notice. A separate, **unticked,
optional** checkbox is only right if the business wants to send marketing, and per
`docs/business-facts.md` it doesn't (confirm).

## Task

1. **Write the notice** as one or two plain sentences that match `docs/data-inventory.md` and the
   owner's email practice. Draft:
   > We'll only use these details to reply to you about your project. We won't add you to a
   > mailing list or share your details for marketing. <a>Read our Privacy Policy</a>.

   Adjust it if the facts differ. It must be true.

2. **Place it inside the form, directly above the submit button**, so screen-reader and keyboard
   users meet it before submitting:
   - `<p class="form-note" id="form-privacy">…</p>`;
   - add `aria-describedby="form-privacy"` to the submit `<button>`, so it's announced when the
     button gets focus.

3. **Link behaviour.** Clicking a same-tab link would throw away what the visitor has typed.
   Open the Privacy Policy in a new tab using the site's existing pattern (see the showcase link
   in `public/index.html:101`): `target="_blank" rel="noopener"`, the inline arrow icon, and
   `<span class="visually-hidden"> (opens in a new tab)</span>`. The link is underlined, because
   in-text link color alone fails 1.4.1.

4. **Style** `.form-note` in the Contact section of `styles.css`: `font-size: 0.8125rem`,
   `color: var(--muted)`, `line-height` about 1.55, and `margin-top` to separate it from the
   message field. Check that muted text on the form background still meets 4.5:1 (it's 6.85:1 on
   `--field-bg`, and about 7.2:1 on `--bg`; verify which background applies).

5. **Marketing opt-in: only if the facts file says the owner will send marketing.** Add an
   optional checkbox, **unticked**, below the notice: "Send me occasional tips and offers by
   email (optional)". Give it its own `name` and a proper `<label for>`. Then update
   `docs/data-inventory.md`, the Privacy Policy and `docs/email-policy.md` (Prompt 18).
   Otherwise, don't add it.

6. **Thanks page** (`public/contact/thanks/index.html`): no change needed, unless the notice
   promised something the thanks page contradicts.

7. **Guards** in `tools/check_site.py`: a `form-notice` check that every `<form>` in `public/`
   contains a link to `/privacy/`, and that no `<input type="checkbox">` has the `checked`
   attribute.

8. Update item 6 in `docs/compliance-log.md`.

## Constraints

- No required consent checkbox, and no pre-ticked box.
- Don't move or restyle the other fields.

## Verify

- `python3 tools/check_site.py` passes.
- Playwright at 375px and 1280px: a screenshot of the form, and a keyboard tab-through showing
  the notice link gets focus before the submit button.
- Check the accessibility tree (`page.accessibility.snapshot()` or an axe run): the submit button
  has the notice as its description.

## Commit

`Fix #06: add privacy notice to the contact form`. Push to the current branch.
