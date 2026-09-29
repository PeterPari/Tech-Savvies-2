# Prompt 13: Add alt text to images

````text
<context>
WCAG 1.1.1 requires a text alternative for every non-text element. The initial audit found:
- The logo appears twice per page with alt="Tech-Savvies NYC home". That's correct for a linked logo: it names the destination and contains the visible logo text.
- The showcase screenshot (public/index.html:110, grisha-studio.webp) has a descriptive alt of about 130 characters.
- Every inline <svg> has aria-hidden="true" and sits beside visible or visually hidden text.
- The checklist ticks are decorative CSS backgrounds.
- og:image:alt is set on every original page.

Prompts 01–22 added pages, so every HTML file in public/ needs checking.
</context>

<inputs>
docs/compliance-log.md, public/
</inputs>

<deliverables>
1. docs/accessibility-audit.md (create it, or add an "Images" section), with a table: Page | Element | Role (meaningful / decorative / link or button) | Current alternative | Correct? | Fix.
2. Fixes in public/:
   - meaningful images described in at most 125 characters, without "image of";
   - decorative <img> alt="";
   - decorative <svg> aria-hidden="true" focusable="false";
   - a link's only image given alt naming the destination;
   - og:image:alt, plus <meta name="twitter:image:alt"> with the same text, on every page.
3. The img-alt check in tools/check_site.py extended to fail on:
   - alt that is a filename, or only "image", "photo", "picture", "logo" or "icon";
   - an <svg> with neither aria-hidden="true" nor (role="img" plus aria-label or <title>);
   - a page without og:image:alt.
4. An "Images and alt text" item in the README "Editing" section: 4 rules, each with one example, plus the W3C alt decision tree URL.
5. Item 13 updated in docs/compliance-log.md.
6. One commit, "Fix #13: verify image text alternatives and tighten checks", pushed.
7. A final message of at most 5 bullets.
</deliverables>

<examples>
<example index="1">Linked logo: alt="Tech-Savvies NYC home"</example>
<example index="2">Decorative divider image: alt=""</example>
<example index="3">Screenshot in a case study: alt="Grisha.studio homepage showing a gallery of paintings"</example>
<example index="4">Icon inside a labelled button: <svg aria-hidden="true" focusable="false">…</svg></example>
</examples>

<acceptance_criteria>
- The checker exits 0.
- axe-core rules image-alt, svg-img-alt and role-img-alt report 0 violations on every page.
- A temporary copy of public/ with alt="logo.png", or with an un-hidden <svg>, makes img-alt fail.
</acceptance_criteria>

<task>
Give every image and icon on every page in public/ a correct text alternative, and make the checker reject missing or meaningless ones.
</task>
````

## Assumptions
- Phases 1–4 have run, so all new pages exist.

## Parameters
- Reasoning effort: low.

## What to test
- axe results across all pages show 0 violations for the three rules.
- Both seeded failures make the checker fail.
