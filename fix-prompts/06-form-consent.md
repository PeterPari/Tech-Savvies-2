# Prompt 06: Form consent

````text
<context>
The contact form (public/contact/index.html:70-109) collects name, email, business and message, with no notice of how they're used. A just-in-time notice where data is collected meets GDPR Art. 13 (where relevant) and the FTC's notice principle, and points to /privacy/.

A notice is the right pattern here, not a required "I agree" checkbox. Replying to the person is the form's purpose. A mandatory consent box would bundle consent with the service, so it wouldn't be freely given under GDPR, and it would add friction.

An optional, unticked marketing checkbox is right only if the owner sends marketing. docs/business-facts.md records whether they do.

The site's pattern for opening a link in a new tab is the showcase frame link (public/index.html:108): target="_blank" rel="noopener", the inline arrow SVG, and <span class="visually-hidden"> (opens in a new tab)</span>. In-sentence links need an underline, because accent against text is 2.17:1.
</context>

<inputs>
docs/business-facts.md, docs/data-inventory.md, docs/ux-honesty-rules.md, docs/compliance-log.md, public/contact/index.html, public/assets/css/styles.css
</inputs>

<deliverables>
1. <p class="form-note" id="form-privacy"> placed inside the form, directly above the submit button:
   - at most 2 sentences and at most 40 words, accurate to docs/data-inventory.md and the owner's email practice;
   - ends with a link to /privacy/ using the new-tab pattern, so typed input isn't lost;
   - the submit button gets aria-describedby="form-privacy".
2. .form-note styles in the Contact section of styles.css: font-size 0.8125rem, color var(--muted), line-height about 1.55, and spacing from the message field. Text contrast on its actual background is at least 4.5:1.
3. Only if docs/business-facts.md says the owner will send marketing: an unticked optional checkbox below the notice, with its own name and <label for>, plus matching updates to docs/data-inventory.md and /privacy/.
4. A check named form-notice in tools/check_site.py: every <form> in public/ contains a link to /privacy/, and no checkbox has the checked attribute.
5. Item 6 updated in docs/compliance-log.md.
6. One commit, "Fix #06: add privacy notice to the contact form", pushed.
7. A final message of at most 5 bullets.
</deliverables>

<examples>
<example index="1">We'll only use these details to reply to you about your project, and we won't add you to a mailing list. Read our Privacy Policy (opens in a new tab).</example>
<example index="2">We use your details to reply and, if you hire us, to run your project. We never sell them. Read our Privacy Policy (opens in a new tab).</example>
<example index="3">We'll use these details to reply to you. We may follow up once about your enquiry; just ask us to stop. Read our Privacy Policy (opens in a new tab).</example>
</examples>

<constraints>
- Add no required consent checkbox and no pre-ticked box.
- Leave the other fields' markup and styling unchanged.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- At 375px and 1280px the notice renders above the button, and keyboard focus reaches the notice link before the submit button.
- The submit button's accessible description is the notice text.
</acceptance_criteria>

<task>
Add an accurate privacy notice, with a link to the Privacy Policy, directly above the contact form's submit button.
</task>
````

## Assumptions
- Prompts 07 and 01 have run.

## Parameters
- Model: sonnet.
- Reasoning effort: low.

## What to test
- The notice text matches the owner's email practice. Run once with "sends follow-ups: yes" and expect wording like example 3.
- Check the accessible description in the Chromium accessibility tree.
- Check that no checkbox is added when marketing is "no".
