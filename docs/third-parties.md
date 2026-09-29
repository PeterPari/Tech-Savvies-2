# Third parties

Every service that receives visitor or client data, as of 2026-09-29. Prompt 08 only documents
the set; it does not change it. The Privacy Policy (`/privacy/`) must match this file.

Legend: "unverified: owner to check…" means the value can only be confirmed from the provider’s
current documentation or dashboard. On 2026-09-29 the session’s network policy still blocked
`docs.netlify.com` (checked twice), so no Netlify documentation could be read and no
Netlify claim below is cited. Nothing here is guessed.

| Service | Purpose | Data received | Triggered by | Where stored | Privacy policy URL | DPA available | How to delete data there |
|---------|---------|---------------|--------------|--------------|--------------------|---------------|--------------------------|
| Netlify (hosting, request logs) | Serves the site | IP address and request details (URL, user agent, referrer) as a normal web request. Exact log fields: unverified, see Netlify section | Every visit | unverified: owner to check in Netlify → Site → Logs / Analytics | https://www.netlify.com/privacy/ | unverified: owner to check with Netlify | unverified: owner to check in Netlify → Team settings → Support / privacy contact |
| Netlify Forms | Contact form at `/contact/` | Every form field the visitor types, plus per-submission metadata (fields and retention unverified) | Form submit | unverified: owner to check in Netlify → Site → Forms. Owner’s own retention rule: delete after 6 months | https://www.netlify.com/privacy/ | unverified: owner to check with Netlify | Netlify → Site → Forms → Submissions → delete a submission (owner to confirm in the dashboard) |
| Netlify Analytics | Traffic statistics | Owner confirms it is on (2026-09-29). Server-side/cookieless: unverified | Every visit | unverified: owner to check in Netlify → Site → Analytics | https://www.netlify.com/privacy/ | unverified: owner to check with Netlify | Not per person; unverified: owner to check in Netlify → Site → Analytics |
| Netlify form spam filtering | — | Owner confirms it is off; only the `bot-field` honeypot is used (2026-09-29), so submissions are not sent for spam scoring by this setting | Form submit | Not applicable while off | — | — | Not applicable; re-check Netlify → Site → Forms → Spam filters if it is ever turned on |
| iCloud Mail (Apple), mailbox for info@tech-savvies.com | Receives form notifications and emails from leads and clients | Sender address, message content, attachments; form notification contents | Email, form submit | Apple’s servers; location unverified: owner to check with Apple | https://www.apple.com/legal/privacy/ | unverified: owner to check with Apple | Delete the message and empty Trash in iCloud Mail. Owner rule: emails kept 12 months |
| Google Domains / Squarespace Domains (registrar for tech-savvies.com) | Domain registration and DNS | Owner’s registrant contact details (name, email, and any address or phone entered at registration) | Domain registration or renewal, not visits | Registrar’s systems | https://www.squarespace.com/privacy | unverified: owner to check with Squarespace | Not deletable while the domain is registered; owner can ask the registrar to update contact details or close the account |
| Grisha.studio (outbound link) | Case-study link on the homepage | Visitor’s IP and the origin `https://tech-savvies.com` as referrer (Referrer-Policy strict-origin-when-cross-origin) | Link click | Grisha.studio’s own systems | Not checked (a client site) | Not applicable | Visitor contacts that site |

## Netlify: facts to confirm

Each item needs a current Netlify docs URL before the Privacy Policy states it. Confirmed by the
owner (see `docs/business-facts.md`): Analytics on, spam filtering off, retention 6 months.

| Question | Status |
|----------|--------|
| Fields and metadata stored per form submission (IP, user agent, referrer) and how long Netlify keeps them | unverified: owner to check in Netlify → Site → Forms, and Netlify’s Forms docs (`docs.netlify.com`, submissions and API pages) |
| Does spam filtering send submissions to another service, and can it be turned off | Owner reports it is off. Whether Netlify’s filter uses another service: unverified, see Netlify’s Forms spam-filter docs |
| What request logs contain | unverified: owner to check in Netlify → Site → Logs, and Netlify’s log docs |
| Is Netlify Analytics server-side and cookieless | unverified. Prompt 05 and 23 need this; check Netlify’s Analytics docs |
| Where data is stored | unverified: owner to check Netlify’s docs or DPA |

## Loaded by the browser automatically

Observed 2026-09-29 with Playwright and Chromium against `python3 -m http.server 8080 --directory public`.
All 7 HTML pages (including `/admin/`, `/contact/thanks/` and `404.html`) at 375px and 1280px, mobile menu
closed and open: 176 requests, all to `http://localhost:8080` (the site’s own origin). No other
origin, no third-party script, font, stylesheet, frame or image, and no cookies set in the browser.

The new site is currently live at `https://tech-savvies-2.netlify.app/` and will move to `tech-savvies.com`
later. Its homepage (curl, 2026-09-29) returns `HTTP/2 200`, `server: Netlify`, the same CSP as
`netlify.toml`, no `Set-Cookie` header, and only same-origin scripts (`/assets/js/main.js` and inline
JSON-LD). The only external URL in the HTML is `https://grisha.studio/`.

The old site currently at `https://tech-savvies.com` is a different codebase and is being replaced.
Its headers and HTML (2026-09-29) show Microsoft Clarity, Google Fonts and a CSP allowing `formsubmit.co`.
Those do not belong to the new site and must not be copied into the Privacy Policy, but they receive data
until the domain moves. Browser-level requests and cookies were not observed on either production host:
Chromium could not load them through the session proxy (`ERR_CERT_AUTHORITY_INVALID`). Owner to re-run
the browser check on `tech-savvies-2.netlify.app` and again after the move.

The CSP in `netlify.toml` (`default-src 'self'`) blocks any other origin from loading. The
`third-party-allowlist` check in `tools/check_site.py` limits outbound `href` origins to
`ALLOWED_LINK_ORIGINS` (currently `https://grisha.studio`).

## Adding a third party

- [ ] Add a row to the table in this file.
- [ ] Update `/privacy/` (and name it in the data-sharing text).
- [ ] Update `/cookies/`.
- [ ] Update the CSP in `netlify.toml` and `EXPECTED_CSP` in `tools/check_site.py`, and describe the change here.
- [ ] Add outbound link origins to `ALLOWED_LINK_ORIGINS` in `tools/check_site.py`.
- [ ] If the service sets cookies or tracks, follow `fix-prompts/05-cookie-consent.md`.
- [ ] Record the provider in `docs/business-facts.md` and re-run `python3 tools/check_site.py`.
