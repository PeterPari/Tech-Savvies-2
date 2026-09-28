# Prompt 12: Remove unsupported claims

````text
<context>
Under FTC Act §5 and NY GBL §349/§350, an advertiser needs a reasonable basis for an objective claim before making it. Obvious puffery ("affordable", "Websites done fast. Websites done right.") needs none.

Claims found in the initial audit:

| Claim | Location | Issue |
|-------|----------|-------|
| "We typically reply within 2 hours during NYC business hours" | contact/index.html:7,13,59; contact/thanks/index.html:7,13,58 | Specific and measurable; hard to keep as a one-person business |
| "Custom site built in as fast as 5 days" | solutions/index.html:62 | Needs a real delivery in that time, and its conditions |
| "basic SEO so you show up when customers search for your services" | solutions/index.html:62 | Implies a ranking outcome |
| "SEO Setup (Get found on Google)" | solutions/index.html:69 | Outcome claim |
| "fix your social media for maximum search visibility" | index.html:92 | "Maximum" can't be proven |
| "If you want it on your website, you'll get it." | index.html:88 | Absolute promise that conflicts with fixed prices |
| "you reach your lead engineer, not a ticketing system" | solutions/index.html:107 | Implies a team; the business is one person (Our Story) |
| "Security Patching" | solutions/index.html:85 | Scope undefined |
| Case-study facts ("secured his preferred domain", "created his Instagram page") | index.html:98-116 | Accuracy confirmed in Prompt 11 |

Line numbers may have shifted after Prompts 10 and 16.
</context>

<inputs>
docs/business-facts.md, docs/compliance-log.md, all HTML in public/ (including titles, meta and og tags, and JSON-LD)
</inputs>

<deliverables>
1. docs/claims-register.md: the table above, plus any further objective claims in public/, with added columns Evidence / owner confirmation | Decision (keep / qualify / remove) | New wording.
2. Every occurrence of each qualified or removed claim rewritten in public/, including meta and og copies. Keep the kern-dot and kern-apos spans in any headline you edit.
3. A check named claims in tools/check_site.py with a BANNED_PHRASES list: "within 2 hours" (omit it if the owner confirmed that claim), "maximum search visibility", "guaranteed ranking", "#1 on Google", "lead engineer", "you'll get it". Include a comment stating that a new objective claim needs a row in docs/claims-register.md.
4. The confirmed facts recorded in docs/business-facts.md, and item 12 updated in docs/compliance-log.md.
5. One commit, "Fix #12: replace unsupported claims with verifiable wording", pushed.
6. A final message of at most 8 bullets.
</deliverables>

<examples>
<example index="1">
Before: We typically reply within 2 hours during NYC business hours.
After: We usually reply within one business day (Monday–Friday, 9am–5pm ET).
</example>
<example index="2">
Before: Custom site built in as fast as 5 days.
After: Custom site built in as little as 5 days once we have your text and photos.
</example>
<example index="3">
Before: SEO Setup (Get found on Google)
After: SEO Setup (so Google can find your site)
</example>
<example index="4">
Before: If you want it on your website, you'll get it.
After: Tell us what you want on your site. We'll build it, or tell you upfront if it's outside the quoted price.
</example>
<example index="5">
Before: you reach your lead engineer, not a ticketing system
After: you talk directly to Peter, who builds your site, not a ticketing system
</example>
</examples>

<constraints>
- Before rewriting, ask the owner in one AskUserQuestion call, skipping anything the facts already answer:
  - realistic first-reply time: within one business day (recommended) / within 4 business hours / within 2 business hours;
  - whether a Launch site has been delivered in 5 days, and under what conditions;
  - who does the work;
  - what "Security Patching" covers.
- Keep claims specific when they're true. Replace an unsupported number with a supported one rather than with vague wording.
- Leave the case-study narrative to Prompt 11, apart from recording it in the register.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- Every objective claim in public/ has a row in docs/claims-register.md.
- Changed pages have no layout breaks at 375px and 1280px.
</acceptance_criteria>

<if_uncertain>
Mark a claim "owner to confirm" in the register and choose the qualify or remove wording until it's confirmed.
</if_uncertain>

<task>
Replace every objective claim on the Tech-Savvies site that lacks owner-confirmed support with accurate wording, and record each decision in docs/claims-register.md.
</task>
````

## Assumptions
- Prompts 00, 16 and 10 have run.
- Prompt 16 has defined the business hours.

## Parameters
- Reasoning effort: high. It needs judgment on what counts as puffery and what counts as an objective claim.

## What to test
- Run with the owner choosing "within 2 business hours (I can consistently hit this)". That claim should stay, and it should be dropped from `BANNED_PHRASES`.
- `grep -rn "maximum\|lead engineer" public/` returns nothing.
- Check that the meta and og copies match the page text.
