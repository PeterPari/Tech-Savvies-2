# Prompt 25: Use clear button labels

````text
<branch>
Do all work on the git branch claude-fix-plan. Before changing anything, run git fetch origin claude-fix-plan, check the branch out, and pull, so you start from the commit the previous prompt pushed. Commit and push only to claude-fix-plan. This is explicit permission to use it instead of the session's default branch. Leave main unchanged.
</branch>

<context>
WCAG criteria covered:
- 2.4.4: link purpose;
- 2.4.6: labels;
- 2.5.3: label in name;
- 3.2.4: consistent identification.

The original controls pass: "Send message", "Start your project", "Back to home", "Contact", the menu toggle named "Menu" with aria-expanded, "(opens in a new tab)" on external links, and the logo link "Tech-Savvies NYC home". Prompts 01–21 added controls that haven't been checked: legal-page links, "Email a data request", the form-notice link, error states, the refund mailto.
</context>

<inputs>
docs/accessibility-audit.md, docs/ux-honesty-rules.md, docs/compliance-log.md, public/
</inputs>

<deliverables>
1. A "Labels" section in docs/accessibility-audit.md, with one row per <a>, <button>, input[type=submit|button], <summary> and [role=button] on every page: Page | Element | Visible text | Accessible name (computed) | Action or destination | Verdict.
2. Fixes in public/, so that every control meets these rules:
   - it names the action or destination;
   - its accessible name starts with its visible text;
   - the same destination or action uses the same key words everywhere;
   - mailto links show the address or begin "Email";
   - links that open a new tab say so;
   - icon-only controls have a text name;
   - after a failed JS validation the submit button reads "Send message".
3. docs/microcopy.md: the rules above, each in at most 15 words, plus a glossary of canonical labels ("Start your project", "Send message", "Privacy Policy", "Terms of Service", "Refund Policy", "Cookie Policy", "Accessibility", "Email a data request", "Back to home"). Linked from the README "Editing" section.
4. A check named link-text in tools/check_site.py. Visible text is the text after removing tags and visually hidden spans. The check fails when visible text equals click here, here, learn more, read more, more, submit or go (case-insensitive), and when an <a> or <button> has no accessible name.
5. Item 25 updated in docs/compliance-log.md.
6. One commit, "Fix #25: audit control labels and add microcopy rules", pushed.
7. A final message of at most 5 bullets.
</deliverables>

<examples>
<example index="1">Weak: "Click here" · Clear: "Read our Privacy Policy"</example>
<example index="2">Weak: "Submit" · Clear: "Send message"</example>
<example index="3">Name mismatch: visible "Contact", aria-label "Get in touch" · Clear: visible "Contact", no aria-label</example>
<example index="4">Weak: "info@…" opening a form · Clear: "info@tech-savvies.com" as a mailto link</example>
</examples>

<constraints>
- Keep the toggle's name as "Menu". aria-expanded already conveys its state.
- Change a label only when it breaks one of the rules above.
</constraints>

<acceptance_criteria>
- axe button-name, link-name and label-content-name-mismatch report 0 violations on every page.
- The checker exits 0, and a temporary copy of public/ with <a href="/">click here</a> makes link-text fail.
</acceptance_criteria>

<task>
Make every button and link on the Tech-Savvies site name exactly what it does, consistently across pages, and make the checker reject vague labels.
</task>
````

## Assumptions
- Prompts 01–21, except 21, have run, so all new controls exist.

## Parameters
- Model: haiku.
- Reasoning effort: low.

## What to test
- The Labels table row count equals the number of interactive elements Playwright counts across all pages.
- The seeded vague link fails the checker.
