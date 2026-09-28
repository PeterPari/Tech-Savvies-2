# Prompt 08: Audit third-party SDKs and embeds

Phase 1. Paste everything below the line into a new Claude Code session opened at the
repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md`, `docs/compliance-log.md`, and
`docs/legal-compliance.md` if it exists.

## Goal

Produce a complete, verified inventory of every third party that receives visitor or client
data, in `docs/third-parties.md`. Make the checker enforce that no new third-party resource
sneaks in.

## Why

The Privacy Policy (Prompt 01) must name the services that process visitors' data. The audit in
`fix-plan.md` found no third-party scripts, iframes or fonts, and a strict CSP
(`default-src 'self'`, `netlify.toml:17`). But data still reaches third parties outside the
page code: Netlify (hosting logs, Forms, spam filtering), the mailbox provider for
`info@tech-savvies.com`, and the destination of one outbound link (`https://grisha.studio/`,
`public/index.html:101`). An inventory that only looks at HTML would miss these.

## Task

1. **Static scan.** Grep `public/` for every absolute URL and every `src`/`href`/`action`/
   `srcset`/`url(` value. Also cover `netlify.toml` and `site.webmanifest`. List each external
   origin and whether it is a resource the browser loads automatically or only a link the
   visitor chooses to follow.

2. **Runtime scan.** Serve `public/` (`python3 -m http.server 8080 --directory public`) and use
   Playwright (installed globally; put any script in your scratchpad, not the repo) to visit
   every HTML page at 375px and 1280px, with the mobile menu both open and closed. Record every
   request's origin. Expected result: only `localhost`. If the production site
   `https://tech-savvies.com` is reachable, repeat against it and note any request or response
   header that Netlify adds, such as `Set-Cookie` or analytics injection.

3. **Services outside the page code.** Use `WebFetch` on Netlify's docs to confirm, and cite:
   - what Netlify Forms stores per submission (fields, plus metadata such as IP address, user
     agent and referrer) and for how long;
   - whether Netlify's form spam filtering sends submissions to a third-party service (for
     example Akismet), and whether that can be turned off;
   - what request data Netlify keeps in logs, and whether Netlify Analytics is server-side and
     cookieless;
   - where Netlify stores data, and whether a DPA is available.

   Take the mailbox provider and domain registrar from `docs/business-facts.md`. If they're
   missing, ask the owner with `AskUserQuestion`.

4. **Write `docs/third-parties.md`**: a table with `Service`, `Purpose`, `Data it receives`,
   `Triggered by` (every visit / form submit / email / link click), `Where stored`,
   `Privacy policy URL`, `DPA`, `How to delete data there`. Add a section "Loaded by the browser
   automatically" (expected: none) and a section "Adding a new third party" with a checklist:
   update this file, the Privacy Policy, the Cookie Policy, the CSP in `netlify.toml`, and
   `EXPECTED_CSP` in `tools/check_site.py`, and get consent first if the service sets cookies or
   tracks (see Prompt 05).

5. **Outbound link.** `https://grisha.studio/` already uses `rel="noopener"` and the
   "(opens in a new tab)" text. `Referrer-Policy: strict-origin-when-cross-origin` means only the
   origin is sent. Leave it unless you find a problem, and record that it was reviewed.

6. **Extend `tools/check_site.py`.** Add a check `third-party-allowlist`. Collect every external
   origin in `href` attributes and compare it to an `ALLOWED_LINK_ORIGINS` list (currently
   `https://grisha.studio`). A new outbound link then needs a deliberate one-line change plus a
   docs update. The existing `no-external-resources` check already covers loaded resources;
   confirm it does.

7. Update item 8 in `docs/compliance-log.md`, and add the Netlify facts you confirmed to
   `docs/business-facts.md`.

## Constraints

- Don't add or remove any third party in this prompt. This is an audit.
- If you can't verify something (for example, a Netlify dashboard toggle), write
  "unverified: owner to check in Netlify → Site → Forms / Analytics" rather than assuming.

## Verify

- `python3 tools/check_site.py` passes.
- Add `<a href="https://example.com">` to a temp copy and confirm the allowlist check fails.

## Commit

`Fix #08: document third-party data flows and enforce an outbound-link allowlist`. Push to the
current branch.
