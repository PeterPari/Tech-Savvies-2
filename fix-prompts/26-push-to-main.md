# Prompt 26: Push the finished fix plan to main

````text
<branch>
Start from the git branch claude-fix-plan: run git fetch origin, check out claude-fix-plan, and pull. This prompt is the only one with explicit permission to push to main, and only by fast-forwarding main to claude-fix-plan.
</branch>

<context>
Prompts 00–25, plus the Prompt 24 final pass, have each committed to claude-fix-plan. Netlify deploys main to tech-savvies.com, so pushing to main publishes every change on the branch. Main may have gained commits since claude-fix-plan was created. docs/compliance-log.md records each item's status and owner follow-ups. docs/legal-compliance.md holds the final-pass results.
</context>

<inputs>
docs/compliance-log.md, docs/legal-compliance.md, tools/check_site.py, tools/build_admin.py
</inputs>

<deliverables>
1. claude-fix-plan with origin/main merged in:
   - a merge commit, not a rebase;
   - conflicts resolved per the constraints below;
   - public/admin/index.html rebuilt with python3 tools/build_admin.py if the merge changed fix-prompts/ or fix-plan.md;
   - pushed to origin claude-fix-plan.
2. main fast-forwarded to claude-fix-plan with git push origin claude-fix-plan:main.
3. A final message of at most 10 bullets:
   - the commit range pushed to main;
   - the pages added or changed;
   - every item in docs/compliance-log.md that isn't done, with its owner follow-ups;
   - the legal pages flagged for attorney review.
</deliverables>

<constraints>
- Push to main only when all of these hold on the merged tree:
  - python3 tools/check_site.py exits 0;
  - python3 tools/build_admin.py --check exits 0;
  - docs/legal-compliance.md has a "Final pass" section;
  - public/ contains no TODO(owner).
  If any fails, stop before pushing and report which one failed, naming the prompt that owns the fix.
- When both sides of a merge conflict can be kept, keep both. When both sides changed the same copy or legal text and choosing one loses content, stop and ask the owner with AskUserQuestion, showing both versions.
- Don't force-push, rebase or rewrite history on claude-fix-plan or main. If the fast-forward is rejected because main moved again, fetch and merge again, at most 2 more times, then stop and report.
- Leave the claude-fix-plan branch in place after pushing.
</constraints>

<acceptance_criteria>
- After the push, git rev-parse origin/main equals git rev-parse origin/claude-fix-plan.
- Both checks exit 0 on that commit.
</acceptance_criteria>

<if_uncertain>
If docs/compliance-log.md shows any item not done, list those items and ask the owner with AskUserQuestion, offering "Push anyway" or "Stop", before pushing.
</if_uncertain>

<task>
Fast-forward main to the finished claude-fix-plan branch once the site checks pass, so the completed fix plan goes live on tech-savvies.com.
</task>
````

## Assumptions
- Every other prompt, including the Prompt 24 final pass, has run and pushed to `claude-fix-plan`.
- The owner is present to answer merge-conflict or open-item questions.

## Parameters
- Model: sonnet.
- Reasoning effort: medium.

## What to test
- Run once with a failing check on `claude-fix-plan` (for example a seeded `TODO(owner)`). The session should stop before pushing and name the owning prompt.
- Add a commit to main first, then run. The session should merge main in, then fast-forward.
- After a real run, confirm the Netlify deploy finished and that `https://tech-savvies.com/privacy/` returns 200.
