# Prompt 17: Age consent for kids' data

Phase 3 (after 06). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 (especially Decision 3) and §4, then `docs/business-facts.md`,
`docs/legal-compliance.md` (the COPPA, NY Child Data Protection Act and minors' contract
entries), `docs/data-inventory.md` and `docs/compliance-log.md`. `/privacy/`, `/terms/` and the
contact form notice (Prompt 06) must exist.

## Goal

Handle children's and minors' data properly for a business-facing site. That means clear
statements, a sensible rule for under-18 clients, and a deletion promise, all **without**
collecting ages or birth dates.

## Why

- **COPPA** applies to sites directed to children under 13, or with actual knowledge of
  collecting their data. Tech-Savvies isn't directed to children, but the policy should say so
  and say what happens if a child's data arrives anyway.
- **NY Child Data Protection Act:** check its scope in `docs/legal-compliance.md`. For a general
  audience site without actual knowledge of minor users, it likely doesn't impose consent
  duties, but processing that's strictly necessary to answer a request is the safe footing.
- **Contracts:** minors can generally void contracts in NY (GOL §3-101). A 16-year-old artist
  could fill in the form. The business should have a parent or guardian as the contracting
  party in that case.
- **Why no age field or checkbox:** asking every visitor for a birth date would collect data the
  business doesn't need (Prompt 07's minimisation principle). An "I'm over 18" checkbox adds
  friction, provides no real assurance, and creates a false record. A clear statement plus a
  real process is the proportionate control.

## Task

1. **Privacy Policy `#children`** (`public/privacy/index.html`). Make sure it states:
   - our services and site are for businesses and adults, not directed to children under 13;
   - we don't knowingly collect personal information from children under 13;
   - if a parent or guardian believes their child sent us information, they can email us, and
     we'll delete it (give the timeframe from the facts, for example within 7 days);
   - if we learn we've received a child's information, we delete it and don't use it;
   - anyone under 18 who wants a project should ask a parent or guardian to contact us. We'll
     only use a minor's details to reply and to put them in touch with their parent or guardian.

   Align this with the NY CDPA finding in `docs/legal-compliance.md`.

2. **Terms `#age`** (`public/terms/index.html`): "To hire us you must be 18 or older. If you're
   under 18, a parent or guardian must agree to these Terms, and they'll be our client for the
   project (including payment)." Adjust it if the attorney guidance or facts say otherwise.

3. **Contact form notice** (`#form-privacy` from Prompt 06): add one short sentence, for example
   "Under 18? Please ask a parent or guardian to get in touch with us." Keep the notice to 2–3
   sentences in total.

4. **Owner-side minor question.** If `docs/business-facts.md` shows that the person signing
   client contracts for Tech-Savvies is under 18, don't put that on the site. Record an owner
   action in `docs/compliance-log.md` and `docs/legal-compliance.md`: get attorney advice on
   having a parent or guardian co-sign or run the business entity.

5. **Internal process.** Add a "Minors" subsection to `docs/data-inventory.md` covering what to
   do when an enquiry seems to come from a child: reply once asking for a parent or guardian,
   don't collect more, and delete within the stated timeframe if no parent or guardian follows up.

6. **Guard.** Add a `no-age-fields` check to `tools/check_site.py` that fails if any input `name`
   or `id` matches `dob|birth|age\b|birthday`. Adding one should be a deliberate decision.

7. Update item 17 in `docs/compliance-log.md`.

## Verify

- `python3 tools/check_site.py` passes.
- Playwright screenshot of the form at 375px, to check the notice length still reads well.

## Commit

`Fix #17: add children's data and under-18 client rules`. Push to the current branch.
