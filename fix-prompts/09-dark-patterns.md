# Prompt 09: Remove dark patterns

Phase 2 (after 11). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md`, `docs/compliance-log.md`, and
`docs/claims-register.md` if it exists.

## Goal

Audit every page and flow for manipulative design, fix whatever you find, and write rules that
keep the prompts that follow (legal pages, form notices, and any future consent banner) from
introducing new ones.

## Why

The FTC's staff report "Bringing Dark Patterns to Light" (2022) and its enforcement actions
treat manipulative interfaces as unfair or deceptive under FTC Act §5. NY's auto-renewal law
(GBL §527-a) specifically targets hard-to-cancel subscriptions. The first audit found no
classic UI dark patterns: no pre-ticked boxes, confirmshaming, countdown timers, fake scarcity,
or disguised ads. It did find one pricing problem: a "$50" headline for a service whose monthly
plan had no price. That's drip pricing and a bait risk, fixed in Prompt 10.

A lot of UI is about to be added (legal pages, a form notice, a rights-request flow, maybe a
cancellation path), so it's the right time to set the rules.

## Task

1. **Walk every page and flow** in a real browser (Playwright, 375px and 1280px): home,
   solutions, our-story, contact, the form submit, thanks, 404, and every legal page that
   exists. Check each of these categories and record pass or fail with evidence in the table
   below:
   - false urgency or scarcity;
   - confirmshaming;
   - pre-selected options;
   - hidden costs or drip pricing (re-check Prompt 10's result);
   - bait-and-switch (headline offer vs. real terms);
   - forced continuity or hard cancellation: is cancelling the monthly plan as easy as starting
     it (same channel, email)?
   - obstruction: is a data-deletion request as easy as sending the enquiry?
   - misleading visual hierarchy: the primary vs. secondary actions in any choice;
   - trick wording or double negatives;
   - nagging or interruptive overlays;
   - disguised ads or undisclosed relationships (re-check Prompt 11);
   - privacy defaults that favour the business;
   - fake social proof;
   - forced registration or unnecessary fields (re-check Prompt 07).

2. **Fix what you find**, within this prompt's scope:
   - Copy and markup fixes on existing pages: do them now.
   - If Prompt 10 hasn't been run and the unpriced "monthly" is still there, stop and tell the
     user to run Prompt 10 first. Don't duplicate its work.
   - If cancelling the monthly plan isn't explained anywhere, add one plain sentence next to its
     price on `/solutions/` ("Cancel any time by emailing info@tech-savvies.com"), matching the
     owner's facts. The Terms (Prompt 02) will give the details.

3. **Write `docs/ux-honesty-rules.md`**:
   - the audit table: category, pass/fail, evidence, fix, commit;
   - "Rules for new UI":
     - choices of equal weight look equal;
     - no pre-ticked consent;
     - declining never costs more clicks than accepting;
     - cancelling or deleting uses the same channel as signing up;
     - every price is shown with its recurring terms;
     - no countdowns or "only N spots left" unless literally true and automatically enforced;
     - no guilt-trip wording on decline options;
     - disclosures sit next to the claim, not in a footnote.

   Link it from the README "Editing" section.

4. Update item 9 in `docs/compliance-log.md`.

## Constraints

- Don't redesign pages. Make the smallest change that removes the manipulation.
- Keep existing classes and tokens.

## Verify

- `python3 tools/check_site.py` passes.
- Screenshots of any changed page at 375px and 1280px.

## Commit

`Fix #09: audit for dark patterns and add honest-UI rules`. Push to the current branch.
