# Prompt 11: Remove fake reviews (and keep it that way)

Phase 2 (after 12). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md`, `docs/compliance-log.md` and
`docs/legal-compliance.md`.

## Goal

Confirm the site shows no fake, unverifiable or undisclosed endorsements. Make sure the one
case study is accurate, permitted, and discloses any connection. Set rules and a guard for any
testimonial added later.

## Why

The FTC's Rule on the Use of Consumer Reviews and Testimonials (16 CFR Part 465, in force since
October 2024) allows civil penalties for fake or misrepresented reviews and testimonials,
undisclosed insider reviews, and suppressing negative reviews. The FTC Endorsement Guides
(16 CFR Part 255) require disclosure of material connections (family, friends, free or
discounted work). NY GBL §349/§350 applies too.

Audit result: the site has **no** reviews, star ratings, testimonials, or `aggregateRating`
schema. It has one case study, the "Featured Showcase" of Grisha.studio
(`public/index.html:98-116`). That's the business describing its own work, not a customer
review. But it names a real person's business and makes specific claims ("secured his preferred
domain", "created his Instagram page"), and it presents the relationship as an ordinary client
engagement.

## Task

1. **Re-scan** all of `public/` for reviews, testimonials, quotes, ratings, star characters
   (★, ⭐), "clients say", "trusted by", logos of other businesses, client counts ("100+ happy
   clients") and review schema. Record what you find (expected: nothing besides the case study).

2. **Verify the case study with the owner** (`AskUserQuestion`, skipping anything already in
   `docs/business-facts.md`):
   - Was Grisha.studio a real client engagement, and are all the stated facts accurate? (Show the
     owner the paragraph from `public/index.html`.)
   - Do you have the client's permission, ideally in writing, to name and link them?
   - Is there a personal connection (family, friend) or was the work free or discounted?

   Apply the answers:
   - **Not accurate:** correct the text to what actually happened.
   - **No permission:** tell the owner to get it. Until they do, anonymise the case study ("a
     local artist") and remove the name and link, or remove the section if the owner prefers.
     Update `ALLOWED_LINK_ORIGINS` in `tools/check_site.py` and `docs/third-parties.md` if the
     link goes.
   - **Connection or free work:** add a short, clear disclosure right next to the client name,
     in the same `.meta` line, not a footnote. For example: "— Local Artist (a friend of the
     founder; our first project, done at a reduced rate)". Use the owner's facts.

3. **Write `docs/testimonials-policy.md`**. Rules for any future testimonial or review:
   - real customers only, quoted verbatim (trimming for length is fine as long as the meaning is
     kept);
   - written permission stored off-repo;
   - dated;
   - disclose any incentive, discount or relationship;
   - never write, buy or AI-generate reviews;
   - never cherry-pick by hiding negative reviews that exist elsewhere;
   - star ratings or `aggregateRating` schema only if the reviews are shown on the page and come
     from a verifiable source.

   Cite the FTC rule and guides with URLs verified via `WebFetch`.

4. **Guard.** Extend `tools/check_site.py`:
   - `no-review-schema` already exists. Confirm it catches `aggregateRating` and `Review` in
     nested JSON-LD.
   - Add a `testimonial-source` check. Any element with `class` containing `testimonial` or
     `review`, or any `<blockquote>`, must have a `data-source` attribute saying where the quote
     came from, for example `data-source="email 2026-05-02, permission on file"`.

5. Update item 11 in `docs/compliance-log.md`, and record the case-study answers in
   `docs/business-facts.md`.

## Constraints

- Don't add testimonials to "replace" anything.
- Don't contact the client yourself. That's the owner's job.

## Verify

- `python3 tools/check_site.py` passes. A temp copy with `<blockquote>` and no `data-source`
  fails.
- If the showcase text changed: Playwright screenshots of `/` at 375px and 1280px.

## Commit

`Fix #11: verify case study and add testimonial rules and guards`. Push to the current branch.
