# Prompt 08: Audit third-party SDKs and embeds

````text
<context>
The Privacy Policy (Prompt 01) must name every service that receives visitor or client data. An audit of the code on 2026-09-28 found:
- no third-party scripts, iframes, fonts or stylesheets;
- CSP default-src 'self' (netlify.toml:17);
- one outbound link, https://grisha.studio/ (public/index.html:108, in the showcase frame's address bar), with rel="noopener" and "(opens in a new tab)" text; Referrer-Policy strict-origin-when-cross-origin, so only the origin is sent.

Data still reaches third parties outside the page code: Netlify (hosting logs, Forms, form spam filtering), the mailbox provider for info@tech-savvies.com, and the domain registrar.
</context>

<inputs>
docs/business-facts.md, docs/compliance-log.md, docs/legal-compliance.md, netlify.toml, public/
</inputs>

<deliverables>
1. docs/third-parties.md, containing:
   - a table with the columns Service | Purpose | Data received | Triggered by (every visit / form submit / email / link click) | Where stored | Privacy policy URL | DPA available | How to delete data there;
   - a section "Loaded by the browser automatically";
   - a checklist "Adding a third party": update this file, /privacy/, /cookies/, the CSP and EXPECTED_CSP, and follow fix-prompts/05-cookie-consent.md if the service sets cookies or tracks.
   For Netlify, record from Netlify's current docs, with each URL cited:
   - the fields and metadata stored per form submission (for example IP, user agent, referrer) and how long they're kept;
   - whether form spam filtering sends submissions to another service, and whether that can be turned off;
   - what request logs contain;
   - whether Netlify Analytics is server-side and cookieless;
   - where data is stored.
2. A check named third-party-allowlist in tools/check_site.py: every external origin in an href must be in ALLOWED_LINK_ORIGINS, which starts as ["https://grisha.studio"].
3. The confirmed Netlify facts added to docs/business-facts.md, and item 8 updated in docs/compliance-log.md.
4. One commit, "Fix #08: document third-party data flows and enforce an outbound-link allowlist", pushed.
5. A final message of at most 8 bullets.
</deliverables>

<constraints>
- Leave the set of third parties unchanged. This prompt only documents it.
- Base the "Loaded by the browser automatically" section on observed requests: visit every HTML page at 375px and 1280px with the mobile menu both closed and open. If https://tech-savvies.com is reachable, also observe it and record any Set-Cookie header or injected script. If it isn't reachable, say so.
- Take the mailbox provider and registrar from docs/business-facts.md, asking the owner if they're missing.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- A temporary copy of public/ with <a href="https://example.com"> makes third-party-allowlist fail.
</acceptance_criteria>

<if_uncertain>
When a setting can only be seen in the Netlify dashboard, write "unverified: owner to check in Netlify → Site → <area>" in the table.
</if_uncertain>

<task>
Document every third party that receives Tech-Savvies visitor or client data in docs/third-parties.md, and make the checker reject unlisted outbound origins.
</task>
````

## Assumptions
- Prompts 00 and 24 have run.
- Netlify's documentation is reachable with WebFetch.

## Parameters
- Reasoning effort: medium.

## What to test
- The observed-requests section lists only the site's own origin, for localhost and for production if reachable.
- Check the Netlify Forms metadata row against Netlify's submissions API docs.
- Add a link to an unlisted site and confirm the checker fails.
