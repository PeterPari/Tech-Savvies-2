# Prompt 04: Cookie policy

````text
<context>
docs/tracking-audit.md records 0 cookies and 0 browser storage, and its "Cookie consent" section records the no-banner decision. Visitors expect a cookie policy. Its content must match what the audit found, so a generic list of "analytics and advertising cookies" would be false. If a consent mechanism is ever added (Prompt 05 branch B), this page will list its cookie.

/privacy/, the .prose styles and the footer Legal column already exist (Prompt 01). The unlinked owner page /admin/ is outside the policy's scope (see CLAUDE.md).
</context>

<inputs>
docs/tracking-audit.md, docs/third-parties.md, docs/business-facts.md, docs/compliance-log.md, public/privacy/index.html (template)
</inputs>

<deliverables>
1. public/cookies/index.html, built from the /privacy/ template:
   - title "Cookie Policy | Tech-Savvies", a unique description, canonical https://tech-savvies.com/cookies/, and og tags;
   - body: h1 "Cookie Policy", "Last updated <time>", and article.prose with these sections:
     - the short version: the audit conclusion, quoted;
     - what cookies are: at most 3 sentences;
     - how we checked: the test date and the fact that the site's automated checks run on every change;
     - other websites: linked sites have their own policies;
     - if this changes: we'll update this page first and ask permission before any cookie that isn't strictly necessary;
     - controlling cookies in your browser: settings described in words;
     - contact, with a link to /privacy/.
   The whole page is at most 400 words. Include a cookie table only if Prompt 05 took branch B.
2. "Cookie Policy" added to the footer Legal column after "Privacy Policy" on every HTML page.
3. A "Read our Cookie Policy" link added to /privacy/#cookies.
4. /cookies/ added to the sitemap, the README pages table, and REQUIRED_FOOTER_LINKS. Item 4 updated in docs/compliance-log.md.
5. One commit, "Fix #04: add cookie policy", pushed.
6. A final message of at most 5 bullets.
</deliverables>

<constraints>
- Describe browser settings in words rather than linking to browser help pages, so ALLOWED_LINK_ORIGINS stays unchanged.
- If docs/tracking-audit.md says Netlify Analytics is on, state that it counts visits from server logs without cookies.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- /cookies/ renders without overflow at 375px and 1280px, and focus is visible on every link.
</acceptance_criteria>

<task>
Publish /cookies/, a cookie policy that states what cookies and storage Tech-Savvies actually uses, and link it from every footer and from the Privacy Policy.
</task>
````

## Assumptions
- Prompts 05 (branch A) and 01 have run.

## Parameters
- Model: sonnet.
- Reasoning effort: low. The content is small and fully determined by the audit.

## What to test
- The page is at most 400 words and contains no cookie table.
- Its first statement matches the conclusion in `docs/tracking-audit.md` word for word.
- `grep -L 'href="/cookies/"'` over `public/**/*.html` returns nothing.
