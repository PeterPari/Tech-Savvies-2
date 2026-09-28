# Prompt 00: Foundation (facts file, compliance log, regression guard)

Run this first. Paste everything below the line into a new Claude Code session opened at the
repository root.

---

You're working in the Tech-Savvies website repo: plain HTML/CSS/JS in `public/`, hosted on
Netlify, with no build step and no dependencies. Read `fix-plan.md` in full first. It holds the
audit, the key decisions, and the ground rules that every later prompt relies on.

This prompt sets up three things that the 25 fix prompts depend on:

1. `docs/business-facts.md`: the one source of truth for every business fact the site states.
2. `docs/compliance-log.md`: status tracking for the 25 items.
3. `tools/check_site.py`: a standard-library-only regression checker. Later prompts add checks
   to it so fixed issues can't quietly come back.

## Why

The later prompts write prices, promises, addresses and legal terms. If each prompt guessed,
the site would contradict itself and could publish claims that aren't true, which is exactly
what items 10, 12 and 16 are fixing. A single facts file, filled in by the owner, stops that.
The checker matters because this site has no CI and no tests, so nothing currently prevents a
future edit from adding a tracking script or dropping a footer link.

## Task

### 1. `docs/business-facts.md`

Create it with one table per topic. Columns: `Fact`, `Value`, `Source` (who confirmed it, and
the date). Include every field listed in `fix-plan.md` §3 "Owner inputs required".

Pre-fill only what the repo already establishes, and mark each pre-filled value
`(from site, confirm)`: brand name "Tech-Savvies" (logo says "Tech-Savvies NYC"), email
`info@tech-savvies.com`, founder Peter Parizhsky, founded 2020, paused 2023, relaunched 2026,
domain `tech-savvies.com`, host Netlify, contact form handled by Netlify Forms, and the prices
exactly as currently published in `public/solutions/index.html`.

Leave every other value as `TODO(owner)`.

Then gather answers:
- For questions with a small set of answers (entity type, yes/no questions, "does the monthly
  plan auto-renew", "is the contract signer 18 or older", "Netlify Analytics on?"), use the
  `AskUserQuestion` tool, up to 4 questions per call, grouped by topic.
- For free-text facts (address, prices, hours, refund rules), list them clearly in your final
  message and ask the owner to reply with answers or edit the file.
- Write every answer you receive into the file with today's date. Never guess a value.

### 2. `docs/compliance-log.md`

A table with one row per item 1–25: `#`, `Item`, `Status` (copy the "Status today" column from
`fix-plan.md` §1), `Prompt`, `Commit`, `Owner follow-ups`. Later prompts update their row.

### 3. `tools/check_site.py`

Python 3 standard library only (`html.parser`, `json`, `re`, `pathlib`, `tomllib` if needed). Run
it as `python3 tools/check_site.py` from the repo root. It exits 1 on any failure and prints
`path:line: message`.

Structure it as a list of small check functions registered in one `CHECKS` list, so later
prompts add a check by writing a function and appending it. Keep a short comment at the top
explaining how to add one. Start with these checks:

- **img-alt:** every `<img>` has an `alt` attribute. Also, an `<img>` that is the only content
  of a link has a non-empty `alt`.
- **no-external-resources:** no `<script src>`, `<iframe>`, `<link rel="stylesheet">`,
  `<link rel="preload">`, `<img src>`, `<video>`, `<audio>` or `<source>` pointing to another
  origin. (Plain `<a href>` links to other sites are fine.)
- **no-client-storage:** no `document.cookie`, `localStorage`, `sessionStorage`, `indexedDB` or
  `navigator.sendBeacon` in `public/**/*.js` or in inline `<script>` blocks.
- **csp-unchanged:** the `Content-Security-Policy` value in `netlify.toml` equals an
  `EXPECTED_CSP` constant in the script. The constant's comment says: change it only together
  with the privacy, cookie and third-party docs.
- **no-review-schema:** JSON-LD blocks parse as JSON and contain no `aggregateRating` or
  `"@type": "Review"`.
- **no-placeholders:** no `TODO(owner)`, `[PLACEHOLDER`, `lorem ipsum`, `XXX` or `[ADDRESS` in
  `public/`.
- **internal-links:** every root-relative `href`/`src` (`/…`) resolves to a file in `public/`
  (`/x/` maps to `public/x/index.html`). Ignore `#fragment`, `mailto:` and `tel:`.
- **new-tab-links:** every `target="_blank"` link has `rel` containing `noopener` and contains
  visually-hidden text "(opens in a new tab)".
- **shared-chrome:** every HTML page's main nav links and footer links match `public/index.html`,
  as sets of `href`s. This catches the "header/footer are copy-pasted into every file" problem.
- **required-footer-links:** a `REQUIRED_FOOTER_LINKS` list, empty for now. Prompts 01, 02, 03,
  04 and 21 add `/privacy/`, `/terms/`, `/refunds/`, `/cookies/` and `/accessibility/`.

Run it on the current site. It should pass. If a check finds a genuine existing problem, don't
weaken the check. Report the problem in your summary and in the compliance log.

### 4. CI and docs

- Add `.github/workflows/site-checks.yml` that runs `python3 tools/check_site.py` on push and
  pull requests (ubuntu-latest, no dependencies to install).
- Add a short "Checks" section to `README.md` explaining how to run the script and what it guards.
- Add `docs/` to the README file tree.

## Constraints

- Don't change anything in `public/` in this prompt.
- No `package.json`, no pip dependencies.

## Verify

- `python3 tools/check_site.py` exits 0 on the current tree.
- Temporarily break each check (for example, add `<script src="https://example.com/x.js">` to a
  copy of a page in your scratchpad, or run the checker against a temp copy of `public/`) and
  confirm each one fails with a clear message. Don't commit the broken copies.

## Commit

`Fix #00: add business facts file, compliance log and site checker`. Push to the current branch.
