# Prompt 11: Remove fake reviews

````text
<context>
The FTC Rule on Consumer Reviews and Testimonials (16 CFR 465) allows civil penalties for fake or misrepresented reviews and testimonials, undisclosed insider reviews, and suppressing negative reviews. The FTC Endorsement Guides (16 CFR 255) require disclosure of material connections: family, friends, free or discounted work. NY GBL §349 also applies.

The initial audit found no reviews, ratings, testimonials or aggregateRating schema. It found one case study, "Featured Showcase" (public/index.html:98-116). The case study names Grisha.studio, links to it, states specific facts ("secured his preferred domain", "created his Instagram page"), and presents the relationship as an ordinary client engagement.
</context>

<inputs>
docs/business-facts.md, docs/claims-register.md, docs/third-parties.md, docs/compliance-log.md, public/
</inputs>

<deliverables>
1. A scan result for public/, covering quotes, testimonials, ratings, ★ or ⭐ characters, "clients say", "trusted by", client logos, client counts, and review schema, recorded in docs/testimonials-policy.md.
2. The case study updated according to the owner's answers:
   - inaccurate facts corrected;
   - if there's no permission to name the client: the name and link removed and the client described as "a local artist" (or the section removed, if the owner prefers), with ALLOWED_LINK_ORIGINS and docs/third-parties.md updated;
   - if there's a personal connection or free or discounted work: a disclosure in the same .meta line as the client name.
3. docs/testimonials-policy.md: rules for future endorsements, each citing the FTC source URL, covering:
   - real customers only, quoted verbatim;
   - written permission stored outside the repo;
   - a date on each quote;
   - disclosed incentives and relationships;
   - no written, bought or AI-generated reviews;
   - no suppression of negative reviews;
   - rating schema only for genuine reviews shown on the page.
4. A check named testimonial-source in tools/check_site.py: any <blockquote>, or any element whose class contains "testimonial" or "review", must have a data-source attribute. Confirm that no-review-schema catches nested aggregateRating and Review.
5. The owner's answers recorded in docs/business-facts.md, and item 11 updated in docs/compliance-log.md.
6. One commit, "Fix #11: verify case study and add testimonial rules", pushed.
7. A final message of at most 6 bullets.
</deliverables>

<examples>
<example index="1">Grisha.studio (opens in a new tab) - Local Artist</example>
<example index="2">Grisha.studio (opens in a new tab) - Local Artist (a friend of the founder; our first project, at a reduced rate)</example>
<example index="3">A local artist - New website build and social presence</example>
</examples>

<constraints>
- Ask the owner in one AskUserQuestion call, after showing them the case-study paragraph:
  - whether it was a real engagement with accurate facts;
  - whether the client gave permission to be named (written is preferred);
  - whether there's a personal connection or the work was free or discounted.
- Add no testimonials to fill the space.
- Leave contacting the client to the owner.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- A temporary copy of public/ with a <blockquote> lacking data-source makes testimonial-source fail.
- If the case study changed, / renders without layout breaks at 375px and 1280px.
</acceptance_criteria>

<if_uncertain>
If the owner can't confirm permission, anonymise the case study (example 3) and list getting permission as an owner action.
</if_uncertain>

<task>
Correct or remove any endorsement on the Tech-Savvies site that is not genuine, permitted and disclosed, and add rules and a check that keep it that way.
</task>
````

## Assumptions
- Prompts 00, 08 and 12 have run.

## Parameters
- Reasoning effort: medium.

## What to test
- Run 3 times with the owner answering (a) permission and no connection, (b) permission and a friend, (c) no permission. The page should match examples 1, 2 and 3 respectively.
- Check that the outbound-link allowlist changes in case (c).
