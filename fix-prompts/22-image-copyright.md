# Prompt 22: Check copyright on images

Phase 4 (after 19). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/asset-licenses.md`, `docs/business-facts.md`,
`docs/legal-compliance.md` and `docs/compliance-log.md`.

## Goal

Establish that Tech-Savvies actually owns, or is licensed to use, every image on the site, above
all the logo, which is its brand. Make the site's copyright notice name the right owner. Give
the owner a short clearance checklist for the name and logo.

## Why

Prompt 19 records what each asset *is*. This prompt checks the business's *rights* to it, which
depend on how it was made:
- **Made by the owner:** owned by the owner. Record it.
- **Made by a freelance designer:** in the US, the designer usually owns the copyright unless
  there's a **written assignment**. "Work made for hire" rarely applies to independent
  contractors for a logo.
- **Online logo maker or template tool** (Canva, Looka, Wix Logo Maker, etc.): the terms vary.
  Some templates are non-exclusive, and some tools forbid trademarking template-based logos.
  Read the tool's current licence.
- **AI image generator:** the US Copyright Office's position is that material without human
  authorship isn't copyrightable, so the business may not be able to stop others copying it.
  Check the current USCO guidance with `WebFetch`, and check the tool's terms.

Also, the footer says "© 2026 Tech-Savvies. All rights reserved." If Tech-Savvies isn't a legal
entity, the notice should name the legal owner (Prompt 16 may already have fixed this).

## Task

1. **Provenance review.** For each image in `docs/asset-licenses.md` (logo, OG image, icons,
   favicons), take the creation method from the owner's answers. If it's missing, ask with
   `AskUserQuestion`. Then:
   - **designer:** ask whether there's a signed assignment. If there isn't, make it an owner
     action: get a one-page copyright assignment signed.
   - **template or logo tool:** `WebFetch` the tool's current licence terms. Summarise what's
     allowed (commercial use, exclusivity, trademark registration) with a citation.
   - **AI tool:** summarise the tool's terms and the USCO position, with citations.
   - **owner-made:** record that, and recommend keeping the source files.

2. **Similarity check (owner step).** Automated reverse image search isn't reliably available
   from this environment, so give the owner steps: upload `public/assets/img/logo.png` to Google
   Lens and TinEye, and note any near-identical logos. Also do a `WebSearch` for "Tech-Savvies"
   and "Tech Savvies" web design businesses, especially in NY, and list any that look likely to
   conflict.

3. **Name and trademark checklist (owner step).** Add to `docs/legal-compliance.md` under
   "Owner actions": search USPTO trademark records for "TECH SAVVIES" / "TECH-SAVVIES" in web
   design classes (for example 42 and 35); check the NY DOS business entity database; and
   consider registering if the name is clear. Report findings from the web search only. Don't
   state legal conclusions.

4. **Copyright notice.** Make sure every page footer reads `&copy; <span data-year>2026</span>
   <Legal name>. All rights reserved.` If Prompt 16 already did this, verify it with the checker.
   Otherwise, apply it to every HTML file and confirm with `grep -L`.

5. **Client work rule.** Add a section to `docs/asset-licenses.md`, "Showing client work": use
   screenshots of client sites only with the client's permission (recorded, per
   `docs/testimonials-policy.md`), don't copy client-owned photos into this site, and credit
   photographers where the client's licence requires it.

6. **Update `docs/asset-licenses.md`:** fill in the `Evidence` and `Status` columns. Update item
   22 in `docs/compliance-log.md`, listing any owner actions (assignment, licence review,
   reverse image search).

## Constraints

- Don't replace the logo or any image. Report the risks and let the owner decide.
- Don't make trademark or copyright legal conclusions. Summarise sources and mark
  "attorney to confirm" where needed.

## Verify

- `python3 tools/check_site.py` passes (business-details / copyright line).

## Commit

`Fix #22: verify image rights and copyright notice; add clearance checklist`. Push to the
current branch.
