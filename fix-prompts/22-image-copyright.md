# Prompt 22: Check copyright on images

````text
<branch>
Do all work on the git branch claude-fix-plan. Before changing anything, run git fetch origin claude-fix-plan, check the branch out, and pull, so you start from the commit the previous prompt pushed. Commit and push only to claude-fix-plan. This is explicit permission to use it instead of the session's default branch. Leave main unchanged.
</branch>

<context>
Prompt 19 recorded what each asset is. Rights to an image depend on how it was made:
- Owner-made: owned by the owner.
- Freelance designer: in the US the designer usually keeps copyright unless there's a written assignment; work-for-hire rarely covers a contractor-made logo.
- Logo maker or template tool (Canva, Looka, etc.): terms vary; templates may be non-exclusive, and some tools prohibit trademarking template-based logos.
- AI generator: the US Copyright Office treats material without human authorship as not copyrightable.

The footer copyright line must name the legal owner, per docs/business-facts.md. Prompt 16 may already have done this.
</context>

<inputs>
docs/asset-licenses.md, docs/business-facts.md, docs/legal-compliance.md, docs/testimonials-policy.md, docs/compliance-log.md
</inputs>

<deliverables>
1. For each image in docs/asset-licenses.md, a rights finding in its Evidence and Status columns, by creation method:
   - designer: whether an assignment exists, and if not, the owner action "get a signed copyright assignment";
   - tool: a summary of at most 60 words of the tool's current licence (commercial use, exclusivity, trademark registration), citing the URL;
   - AI: the tool's terms plus the current USCO guidance, citing both;
   - owner-made: recorded, with a recommendation to keep the source files.
2. In docs/legal-compliance.md, under "Owner actions":
   - reverse image search steps for logo.png (Google Lens, TinEye);
   - a USPTO trademark search for "TECH SAVVIES" / "TECH-SAVVIES" in classes 35 and 42, and a NY DOS entity search;
   - a list of same-name web design businesses found by web search, with URLs.
3. Every page footer reading "© <span data-year>2026</span> <legal name>. All rights reserved.", enforced by the business-details check.
4. A rights finding for public/assets/img/grisha-studio.webp, a screenshot of the client's site showing their name and artwork, tied to the permission answer recorded by Prompt 11. Also a "Showing client work" section in docs/asset-licenses.md: client screenshots only with recorded permission; no copying of client-owned photos; photographer credit where the client's licence requires it.
5. Item 22 updated in docs/compliance-log.md, with owner actions.
6. One commit, "Fix #22: verify image rights and copyright notice", pushed.
7. A final message of at most 6 bullets.
</deliverables>

<constraints>
- Leave every image in place. Report risks for the owner to decide on.
- Summarise sources rather than stating legal conclusions, and mark "attorney to confirm" where ownership is unclear.
- Leave the reverse image search to the owner as a written step.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- Every image row in docs/asset-licenses.md has a non-empty Evidence and Status.
</acceptance_criteria>

<if_uncertain>
When the creation method is unknown, set Status to "ownership unverified: owner action" and state what evidence would settle it.
</if_uncertain>

<task>
Establish whether Tech-Savvies owns or is licensed to use each image on the site, correct the copyright notice, and record the owner's clearance actions.
</task>
````

## Assumptions
- Prompts 19 and 16 have run.

## Parameters
- Model: sonnet.
- Reasoning effort: medium.

## What to test
- Run with the logo marked "Canva". The finding should cite Canva's current licence URL.
- Run with "designer, no contract". It should produce the assignment owner action.
- Check that the footer copyright line matches `LEGAL_NAME` on every page.
