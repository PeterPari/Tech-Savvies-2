# Prompt 12: Remove unsupported claims

Phase 2 (after 10). Paste everything below the line into a new Claude Code session opened at
the repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md`, `docs/compliance-log.md` and
`docs/legal-compliance.md`.

## Goal

Every objective, checkable claim on the site should be true and backed by something the owner
can point to. Clear puffery ("Websites done right") can stay. Anything specific that the owner
can't back is qualified or removed.

## Why

Under FTC Act §5 and NY GBL §349/§350, an advertiser needs a reasonable basis for objective
claims *before* making them. The site makes several objective claims, and some of them sit
uneasily with other facts on the site. For example, one person runs every project (Our Story)
while the copy mentions "your lead engineer".

## Claims register (starting point, verify each against the files)

| Claim | Where | Issue |
|-------|-------|-------|
| "We typically reply within 2 hours during NYC business hours" | `contact/index.html:7,13,59`; `contact/thanks/index.html:7,13,58` | Specific, measurable, hard to keep as a one-person business. "Business hours" is undefined (Prompt 16 defines it). |
| "Custom site built in as fast as 5 days" | `solutions/index.html:62` | Needs at least one real delivery in 5 days, and conditions (for example, once content is supplied). |
| "…basic SEO so you show up when customers search for your services" | `solutions/index.html:62` | Implies a ranking outcome nobody controls. |
| "SEO Setup (Get found on Google)" | `solutions/index.html:69` | Same: an outcome claim. |
| "fix your social media for maximum search visibility" | `index.html:92` | "Maximum" is unprovable. |
| "If you want it on your website, you'll get it." | `index.html:88` | An absolute promise that contradicts fixed prices. |
| "you reach your lead engineer, not a ticketing system" | `solutions/index.html:107` | Implies a team; the business is one person. |
| "Completion guarantee (we don't bill extra if a project takes longer)" | `solutions/index.html:107` | Fine only if it matches the Terms exactly (Prompt 02). |
| "Transparent pricing (no surprise invoices)" | `solutions/index.html:7,13,107` | True only after Prompt 10. |
| "Security Patching" | `solutions/index.html:85` | Needs a defined scope: which software, and whether it's one-time. |
| Case study facts: "secured his preferred domain", "created his Instagram page" | `index.html:98-116` | Must be accurate (Prompt 11 confirms with the owner). |
| "drive more engagement and potentially more customers" | `solutions/index.html:91` | Already hedged. Keep. |
| "affordable", "Websites done fast. Websites done right." | several | Puffery. Keep. |

## Task

1. **Complete the register.** Re-read every HTML page, including `<title>`, meta and `og:` tags,
   JSON-LD, the OG image text (`public/assets/img/og-image.png` reads "Websites done fast.
   Websites done right." and "WEBSITES · GOOGLE · SOCIAL", which is fine), and the pages added by
   earlier prompts. Add anything objective that's missing from the table above.

2. **Ask the owner** (`AskUserQuestion`, and skip anything already in `docs/business-facts.md`):
   - What is your realistic first-reply time? Offer: "within one business day" (recommended),
     "within 4 business hours", "within 2 business hours (I can consistently hit this)".
   - Have you delivered a Launch site in 5 days, and under what conditions? Offer: yes, keep
     "as fast as 5 days once we have your content"; say "usually 1–2 weeks"; remove the timing.
   - Who does the work? Confirm it's the owner alone, or name the collaborators.
   - What does "Security Patching" cover?

3. **Write `docs/claims-register.md`**: the completed table plus columns `Evidence / owner
   confirmation`, `Decision` (keep / qualify / remove), `New wording`. This is the record the
   owner can show if a claim is ever challenged.

4. **Apply the rewrites** everywhere each claim appears, including meta and `og:` duplicates.
   Suggested wording, to adapt to the owner's answers and keep in the site's plain, friendly
   voice:
   - Reply time: "We usually reply within one business day (Mon–Fri, 9am–5pm ET)." Use the hours
     from the facts file.
   - Launch: "Custom site built in as little as 5 days once we have your content and photos."
   - SEO: "…and basic SEO setup so search engines can find and understand your site." Checklist
     item: "SEO Setup (so Google can find your site)".
   - Home, Google & Social: "…and tidy up your social media so it's easier for people to find
     you."
   - Home, New Websites: "Tell us what you want on your site. We'll build it, or tell you
     upfront if something is outside the quoted price."
   - Includes paragraph: "Direct communication (you talk to Peter, who builds your site, not a
     ticketing system)."
   - Security: "Security updates for your site's software" plus scope, if the owner confirms it.

   Keep the headline kerning spans (`kern-dot`, `kern-apos`) intact if you touch a headline. See
   README "Editing".

5. **Guard.** Add a `claims` check to `tools/check_site.py` with a `BANNED_PHRASES` list:
   `within 2 hours` (unless the owner confirmed it), `maximum search visibility`,
   `guaranteed ranking`, `#1 on Google`, `lead engineer`, `you'll get it`. Include a comment
   saying a new objective claim needs an entry in `docs/claims-register.md`.

6. Update item 12 in `docs/compliance-log.md`, and add the confirmed facts to
   `docs/business-facts.md`.

## Constraints

- Don't make copy vaguer than it needs to be. Specific and true beats vague.
- Leave the case-study narrative to Prompt 11, beyond flagging it.

## Verify

- `python3 tools/check_site.py` passes.
- `grep -rn "2 hours\|maximum\|lead engineer" public/` returns nothing, or only owner-confirmed
  wording.
- Playwright screenshots of changed pages at 375px and 1280px, to catch any line-length or
  layout change.

## Commit

`Fix #12: replace unsupported claims with verifiable wording`. Push to the current branch.
