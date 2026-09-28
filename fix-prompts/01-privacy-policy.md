# Prompt 01: Privacy policy

````text
<context>
The site collects personal data in two ways: the contact form (name, email, business, service, message) and Netlify's request logs and form metadata. CalOPPA requires a conspicuously posted privacy policy for commercial sites that collect personal information from California residents. A policy that misdescribes actual practice is deceptive under FTC Act §5 and NY GBL §349.

Generic boilerplate ("we may use cookies and share data with partners") would therefore be false here. The site sets no cookies, runs no analytics and has no ad partners, and every statement in the policy must come from the input documents.

This is the first legal page. It also creates two shared pieces the other legal pages reuse: .prose styles and a footer "Legal" column.

Two CSS facts matter here:
- The reset removes bullets only from ul[role="list"].
- Accent link color against body text is 2.17:1, so a link inside running text needs an underline (WCAG 1.4.1). The .lead a rule already has that treatment.
</context>

<inputs>
docs/business-facts.md, docs/data-inventory.md, docs/third-parties.md, docs/tracking-audit.md, docs/legal-compliance.md, docs/compliance-log.md, public/our-story/index.html (page template)
</inputs>

<deliverables>
1. public/privacy/index.html:
   - head, header and footer copied from public/our-story/index.html;
   - title "Privacy Policy | Tech-Savvies", a unique meta description, canonical https://tech-savvies.com/privacy/, and og tags;
   - body structure: main#main > section.section.section--first > .container > p.eyebrow "Legal" > h1.display-md "Privacy Policy" > p.meta "Last updated <time datetime>" > article.prose.
   Sections, each an h2 with the given id:
   - #summary: 4–5 bullets;
   - #what-we-collect;
   - #how-we-use-it, including what we don't do: no sale or "sharing" in the CCPA sense, no targeted advertising, no marketing email without separate opt-in;
   - #sharing: one entry per processor in docs/third-parties.md, each linking to its privacy policy;
   - #cookies: the conclusion from docs/tracking-audit.md, plus one sentence on Do Not Track and Global Privacy Control;
   - #retention;
   - #your-rights: access, correction, deletion and marketing opt-out via a mailto link with subject "Data request", identity confirmed by replying to the address on file, the response time supported by docs/legal-compliance.md, no charge;
   - #security: only measures confirmed in docs/business-facts.md;
   - #children: not directed to under-13s; delete on discovery; parents can contact us;
   - #international: legal bases and the right to complain if EU/UK clients are served; otherwise one sentence saying data is processed in the US;
   - #changes;
   - #contact, with legal name, dba, mailing address and email.
2. A "Legal pages" block in public/assets/css/styles.css:
   - .prose with max-width var(--measure);
   - h2 and h3 spacing;
   - paragraph and list spacing, with visible bullets;
   - links underlined like .lead a;
   - a table style with var(--line) borders, and a scroll wrapper (tabindex="0", role="region", aria-label) for tables wider than 320px.
3. A fourth footer block on every HTML page, after "Contact": <nav aria-label="Legal"> containing p.eyebrow.footer-heading "Legal" and ul.footer-links[role=list] with "Privacy Policy". .footer-grid gets four columns at 48em; if they don't fit at 768px, the brand spans a full row at 48em and four columns start around 64em.
4. /privacy/ added to public/sitemap.xml, the README pages table, and REQUIRED_FOOTER_LINKS.
5. Item 1 updated in docs/compliance-log.md, marked "attorney review recommended".
6. One commit, "Fix #01: add privacy policy, legal page styles and footer legal links", pushed.
7. A final message of at most 8 bullets, listing any section left out for lack of source facts.
</deliverables>

<constraints>
- Every factual statement comes from the input documents. Leave out any practice the inputs don't document.
- Writing level: Flesch-Kincaid grade 8 or lower, average sentence length at most 20 words, "we" and "you". Don't write "may" for practices that never happen.
- Publish no TODO or placeholder text. Ask the owner for any missing fact.
- If any of data-inventory.md, third-parties.md, tracking-audit.md or legal-compliance.md is missing, stop and name the prompt that creates it (07, 08, 23, 24).
</constraints>

<acceptance_criteria>
- The checker exits 0, including shared-chrome and required-footer-links.
- /privacy/ and the footer render without overflow at 375px, 768px and 1280px.
- Keyboard focus is visible on every link on the page.
</acceptance_criteria>

<if_uncertain>
If an input document marks a fact "unverified", word the policy so it's true either way, and list the fact in the final message.
</if_uncertain>

<task>
Publish /privacy/, a privacy policy that describes exactly what Tech-Savvies collects, why, who processes it, how long it's kept and how to have it deleted, together with the shared legal-page styles and footer Legal column.
</task>
````

## Assumptions
- Prompts 00, 24, 08, 23, 05, 07, and Phase 2 have run.
- An attorney will review the page before anyone relies on it.

## Parameters
- Reasoning effort: high.

## What to test
- Every processor in `docs/third-parties.md` appears in `#sharing`, and no others.
- Remove `docs/tracking-audit.md` in a scratch branch. The session should stop and name Prompt 23.
- Run a readability check (for example the textstat package in a scratch venv) and confirm grade 8 or lower.
- Check the footer layout at 768px.
