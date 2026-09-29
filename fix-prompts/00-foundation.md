# Prompt 00: Foundation (facts file, compliance log, site checker)

````text
<branch>
Do all work on the git branch claude-fix-plan. Before changing anything, run git fetch origin claude-fix-plan, check the branch out, and pull, so you start from the commit the previous prompt pushed. Commit and push only to claude-fix-plan. This is explicit permission to use it instead of the session's default branch. Leave main unchanged.
</branch>

<context>
The fix prompts in fix-prompts/ publish prices, promises, addresses and legal terms. They can do that safely only with three shared artifacts in place:
- a single facts file the owner fills in;
- a status log for the 25 items;
- a regression checker. The repo has no tests and no CI, so nothing currently stops a later edit from adding a tracker or dropping a footer link.

Facts the repo already establishes:
- brand "Tech-Savvies" (logo reads "Tech-Savvies NYC");
- email info@tech-savvies.com;
- founder Peter Parizhsky; founded 2020, paused 2023, relaunched 2026;
- domain tech-savvies.com, hosted on Netlify, contact form via Netlify Forms;
- the prices currently published in public/solutions/index.html.

The owner-input fields are the rows of the table in fix-plan.md §3. The starting status of each item is the "Status today" column in fix-plan.md §1.
</context>

<deliverables>
1. docs/business-facts.md:
   - one table per topic, with columns Fact | Value | Source (who confirmed it, and the date);
   - one row per field in fix-plan.md §3;
   - the repo-established facts above filled in and marked "(from site, confirm)";
   - every other value set to TODO(owner), except answers the owner gives during this session.
2. docs/compliance-log.md: a 25-row table with columns # | Item | Status | Prompt | Commit | Owner follow-ups.
3. tools/check_site.py:
   - Python 3 standard library only, run from the repo root;
   - exits 1 on any failure and prints `path:line: [check-name] message`;
   - checks are functions registered in a CHECKS list, with a header comment of at most 5 lines explaining how to add one.
   Initial checks:
   - img-alt: every <img> has an alt attribute; an <img> that is a link's only content has non-empty alt.
   - no-external-resources: no script, iframe, stylesheet or preload link, img, video, audio or source loaded from another origin. Plain <a href> links are allowed.
   - no-client-storage: no document.cookie, localStorage, sessionStorage, indexedDB or navigator.sendBeacon in public/**/*.js or in inline scripts, excluding public/admin/.
   - csp-unchanged: the CSP in netlify.toml equals an EXPECTED_CSP constant.
   - no-review-schema: every JSON-LD block parses and contains no aggregateRating or "@type": "Review".
   - no-placeholders: no TODO(owner), [PLACEHOLDER, lorem ipsum, XXX or [ADDRESS in public/.
   - internal-links: every root-relative href/src resolves to a file in public/ (/x/ maps to public/x/index.html). Ignore fragments, mailto: and tel:.
   - new-tab-links: every target="_blank" link has rel containing noopener, plus visually hidden text "(opens in a new tab)".
   - shared-chrome: every page's main-nav and footer href sets equal those in public/index.html, excluding public/admin/.
   - required-footer-links: every page's footer (excluding public/admin/) contains each entry of REQUIRED_FOOTER_LINKS. The list starts empty; later prompts append to it.
4. .github/workflows/site-checks.yml: runs the checker and `python3 tools/build_admin.py --check` on push and pull_request, on ubuntu-latest, with no install step.
5. README.md: a "Checks" section of at most 8 lines, and docs/ added to the file tree.
6. One commit, "Fix #00: add business facts file, compliance log and site checker", pushed.
7. A final message of at most 8 bullets, followed by the list of free-text facts still set to TODO(owner).
</deliverables>

<constraints>
- Leave public/ unchanged. public/admin/ is the owner's generated prompt checklist (see CLAUDE.md).
- Ask about choice-type facts (entity type, yes/no questions, auto-renewal, whether the contract signer is 18 or older) with AskUserQuestion, at most 4 questions per call. List free-text facts (address, prices, hours, refund rules) in the final message instead of asking them one at a time.
- If a check finds a real existing problem, record it in docs/compliance-log.md and keep the check strict. Don't loosen it.
</constraints>

<acceptance_criteria>
- The checker exits 0 on the current tree.
- For each check, a temporary copy of public/ outside the repo, seeded with one violation of that check, makes the checker exit 1 with that check's name.
</acceptance_criteria>

<if_uncertain>
Leave a value as TODO(owner) when the repo doesn't establish it and the owner hasn't answered.
</if_uncertain>

<task>
Create the shared compliance foundation (facts file, compliance log, and site checker with CI) that the prompts in fix-prompts/ build on.
</task>
````

## Assumptions
- This is the first prompt run, on a branch that contains `fix-plan.md` and `CLAUDE.md`.
- The owner is available to answer questions during the session.

## Parameters
- Model: sonnet.
- Reasoning effort: medium.
- Output schema and temperature: none, and default. The output is repo changes plus the final message.

## What to test
- Run on a clean checkout. The checker exits 0, and each seeded violation fails with the right check name.
- Run once without answering any questions. `docs/business-facts.md` should contain `TODO(owner)` values, never guessed ones.
