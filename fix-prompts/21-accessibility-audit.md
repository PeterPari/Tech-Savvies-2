# Prompt 21: Fix accessibility (full WCAG 2.2 AA audit and statement)

````text
<context>
Website accessibility claims arise under ADA Title III, the NY State Human Rights Law and the NYC Human Rights Law (see docs/legal-compliance.md). The business's audience includes people who don't feel confident with technology, including older adults (see /our-story/).

Prompts 13, 14, 15 and 25 fixed alt text, contrast, keyboard access and labels, and recorded their results in docs/accessibility-audit.md. This prompt covers the rest of WCAG 2.2 AA across the finished site, including every legal page, and adds an accessibility statement.
</context>

<inputs>
docs/accessibility-audit.md, docs/business-facts.md, docs/legal-compliance.md, docs/compliance-log.md, public/, public/privacy/index.html (template)
</inputs>

<deliverables>
1. An "Automated" section in docs/accessibility-audit.md: axe-core results with the tags wcag2a, wcag2aa, wcag21a, wcag21aa, wcag22aa and best-practice, for every HTML page. Matrix: 320px, 375px, 768px and 1280px, crossed with default, mobile menu open, contact form errors shown, prefers-reduced-motion: reduce, and forced-colors: active. Record results before and after fixes.
2. A "Manual" section, giving pass or fail with evidence for:
   - 1.3.1/1.3.2: one h1 per page, headings, lists, tables with caption and th scope, landmarks;
   - 1.3.5: autocomplete;
   - 1.4.4/1.4.10: 200% zoom and 320px width with no page-level horizontal scroll;
   - 1.4.12: the WCAG text-spacing overrides clip nothing, including the kern-dot/kern-apos headlines and buttons;
   - 1.4.13: content on hover or focus;
   - 2.2.2/2.3.1: motion and flashing;
   - 2.4.2: titles are unique;
   - 2.5.8: target size;
   - 3.1.1: page language;
   - 3.2.3/3.2.4/3.2.6: consistent navigation, labels and help location;
   - 3.3.7/3.3.8: redundant entry and accessible authentication;
   - 4.1.2: name, role and value;
   - 4.1.3: status messages (whether the error state or "Sending…" needs a live region);
   - reading order and names from the Chromium accessibility tree for /, /contact/ and /privacy/.
3. Fixes for every failure in public/, with header and footer changes applied to every page.
4. public/accessibility/index.html, built from the /privacy/ template:
   - title "Accessibility | Tech-Savvies", a unique description, canonical, og tags;
   - article.prose, at most 350 words, covering:
     - the goal of WCAG 2.2 AA;
     - the measures taken (automated and keyboard testing, zoom, reduced motion, high contrast);
     - known limitations, or "none known as of <date>";
     - how to report a barrier: a mailto link with subject "Accessibility", the reply time from docs/business-facts.md, and an offer to provide the information another way;
     - the last review date;
     - the technologies relied on (HTML and CSS; JavaScript optional).
   - "Accessibility" added to the footer Legal column on every page, the sitemap, the README, and REQUIRED_FOOTER_LINKS.
5. Item 21 updated in docs/compliance-log.md, including the owner action of a real VoiceOver or NVDA pass.
6. One commit, "Fix #21: full WCAG 2.2 AA audit, fixes and accessibility statement", pushed.
7. A final message of at most 8 bullets.
</deliverables>

<constraints>
- Keep the visual design and tokens. Fix semantics and behaviour.
- Word the statement as "we aim to meet WCAG 2.2 AA". Leave out "fully compliant".
- Install axe-core in a scratch directory outside the repo.
</constraints>

<acceptance_criteria>
- axe reports 0 violations across the whole matrix after fixes.
- Every manual criterion listed has a pass, or a fixed failure, with evidence.
- The checker exits 0.
</acceptance_criteria>

<if_uncertain>
Where automated tools can't decide a criterion and the accessibility tree doesn't settle it, mark it "needs manual screen-reader check" and add it to the owner action.
</if_uncertain>

<task>
Bring every page in public/ to WCAG 2.2 AA and publish /accessibility/ with a way to report barriers.
</task>
````

## Assumptions
- Every other prompt except the Prompt 24 final pass has run.

## Parameters
- Reasoning effort: high.

## What to test
- Re-run the axe matrix independently after the commit and expect 0 violations.
- Apply the text-spacing overrides and zoom to 200% on `/`, `/solutions/` and `/refunds/`, and check that nothing clips.
- A human does a 10-minute VoiceOver or NVDA pass on the contact form.
