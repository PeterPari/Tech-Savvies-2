# Third parties

Every service that receives visitor or client data, as of 2026-09-29. Prompt 08 only documents
the set; it does not change it. The Privacy Policy (`/privacy/`) must match this file.

Sources were read on 2026-09-28 by a research agent (Netlify docs, Netlify DPA, RDAP, Apple and
Squarespace help pages). "unverified" means the source did not state it or could not be read. Items
marked "(summary)" came back from a fetch tool as a paraphrase, not a verbatim quote. Where the
owner’s statement and Netlify’s docs disagree, both are shown.

| Service | Purpose | Data received | Triggered by | Where stored | Privacy policy URL | DPA available | How to delete data there |
|---------|---------|---------------|--------------|--------------|--------------------|---------------|--------------------------|
| Netlify (hosting, request logs) | Serves the site | IP address, user agent, referrer, URL, method, status, country and timestamp are the fields Netlify’s traffic logs carry (per its log-drain field list). Whether the site’s own request logs keep them, and for how long: unverified: owner to check in Netlify → Site → Logs. Netlify’s DPA says its own service logging is kept online 90 days and offline 1 year | Every visit | Netlify and its sub-processors (includes AWS); may be processed outside the EEA, UK and Switzerland. Region: unverified: ask privacy@netlify.com | https://www.netlify.com/privacy/ | Yes, https://www.netlify.com/pdf/netlify-dpa.pdf; incorporated into Netlify’s self-serve terms, no separate signature documented | Not per visitor. Account-owner requests: privacy@netlify.com |
| Netlify Forms | Contact form at `/contact/` | Every field the visitor submits, plus IP address (docs show `data.ip`) and a created-at timestamp. User agent and referrer as stored fields: unverified | Form submit | Netlify’s user database (“securely stored”). Retention: Netlify documents none | https://www.netlify.com/privacy/ | Yes, same DPA. For submitters, Netlify acts as processor and the owner is the controller | Netlify → Site → Forms → tick submissions → Delete submission (permanent), or API `DELETE /api/v1/submissions/{submission_id}`; “Delete form” removes all of a form’s submissions |
| Netlify form spam filtering (Akismet) | Screens submissions | Netlify’s docs say “All form submissions are filtered for spam using Akismet”. What fields go to Akismet: unverified. Owner confirmed in the dashboard that it’s on, with the honeypot field as extra spam prevention (2026-09-29) | Form submit | Akismet’s systems: unverified | https://automattic.com/privacy/ (Akismet’s operator; not read) | unverified | Deleting a Netlify spam submission is as for Netlify Forms; anything Akismet keeps: unverified |
| Netlify notification emails | Send each submission to info@tech-savvies.com | The submission content, sent from formresponses@netlify.com | Form submit | Netlify’s mail systems, then the iCloud mailbox below | https://www.netlify.com/privacy/ | Same DPA | Netlify → Site → Forms → Form notifications to remove the recipient; delete the email in iCloud |
| Netlify Web Analytics | Traffic statistics | Built from CDN server logs, no client script. Netlify says it is cookieless and anonymous. It counts unique visitors by IP address per day and shows top pages, sources, locations and bandwidth. Owner confirms it is on (2026-09-29). Whether IPs are hashed or stored raw: unverified | Every visit | Netlify. Chart window 30 days; storage duration: unverified | https://www.netlify.com/privacy/ | Same DPA | Not per person. Turn off: Netlify → Analytics & metrics → Analytics → Danger zone → Cancel Web Analytics service |
| iCloud Mail (Apple), mailbox for info@tech-savvies.com | Receives form notifications and emails from leads and clients | Sender address, message content, attachments | Email, form submit | Apple and third-party data centers; region unverified. Not end-to-end encrypted | https://www.apple.com/legal/privacy/en-ww/ | unverified: no DPA found for a personal iCloud account | Deleted mail stays in Trash 30 days, then is erased; emptying Trash erases at once. Owner rule: emails kept 12 months |
| Squarespace Domains II LLC (registrar for tech-savvies.com) | Domain registration | Registrant name or organization, email, phone, postal address, country (summary). Squarespace says free domain privacy is automatic for most domains; whether it is on for this one: unverified: owner to check in the registrar dashboard | Domain registration and renewal, not visits | Squarespace. Retention: unstated | https://www.squarespace.com/privacy (returned 429, not read) | unverified: no DPA found | privacy@squarespace.com (summary). Registration data must be kept while the domain is registered |
| Claude (Anthropic) | AI tool the owner uses to help build client sites | Only details that are on the client’s public website; no enquiry or client personal details otherwise (owner, 2026-09-29) | Owner’s use while building a site, not visits | Anthropic: unverified | https://www.anthropic.com/legal/privacy (opened 2026-09-29) | unverified | unverified |
| ChatGPT (OpenAI) | AI tool the owner uses to help build client sites | Same as Claude (owner, 2026-09-29) | Owner’s use while building a site, not visits | OpenAI: unverified | https://openai.com/policies/privacy-policy/ (returned 403, not read) | unverified | unverified |
| Grisha.studio (outbound link) | Case-study link on the homepage | Visitor’s IP and the origin `https://tech-savvies.com` as referrer (Referrer-Policy strict-origin-when-cross-origin) | Link click | Grisha.studio’s own systems | Not checked (a client site) | Not applicable | Visitor contacts that site |

Domain facts (RDAP, 2026-09-28): registered 2020-11-11, **expires 2026-11-11**, nameservers `DNS1-4.P06.NSONE.NET`.
Those are the NS1 servers that Netlify DNS runs on: the zone's SOA contact is `domains+netlify.netlify.com`, so DNS
is hosted in Netlify DNS (corrected 2026-09-29; the zone also holds the iCloud MX, SPF and Google verification records).

## Netlify facts and sources

| Question | Answer | Source |
|----------|--------|--------|
| Fields stored per form submission | `id`, `number`, `title`, `email`, `name`, `first_name`, `last_name`, `company`, `summary`, `body`, `data` (the fields plus `ip`), `created_at`, `site_url`. User agent and referrer: unverified | https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api/ (Forms section) |
| Submission retention | Not stated. “Form submission data is securely stored in our user database … we recommend that you actively manage the data by exporting form submissions and deleting them regularly.” The owner’s 6 months must be enforced by the owner | https://docs.netlify.com/manage/forms/submissions/ |
| Does spam filtering send data to another service | “All form submissions are filtered for spam using Akismet.” No off switch is documented. A honeypot-caught submission is “quietly reject[ed]” and not listed as spam | https://docs.netlify.com/manage/forms/spam-filters/ |
| Deleting submissions | Dashboard Delete submission, or API `DELETE /api/v1/submissions/{submission_id}` | https://docs.netlify.com/manage/forms/submissions/ |
| Notification emails | Sent from formresponses@netlify.com | https://docs.netlify.com/manage/forms/notifications/ |
| Request logs | Traffic-log fields: `client_ip`, `user_agent`, `referrer`, `url`, `method`, `status_code`, `country`, `timestamp`, `request_id`. Log drains are Enterprise only. Function logs 7 days (the site has no functions) | https://docs.netlify.com/manage/monitoring/log-drains/ and https://docs.netlify.com/manage/monitoring/logs/ |
| Netlify’s own service-log retention | Online 90 days, offline 1 year | https://www.netlify.com/pdf/netlify-dpa.pdf (Exhibit II) |
| Analytics server-side and cookieless | “Data for Web Analytics comes from our Content Delivery Network (CDN) server logs … no client-side code”; “tracked anonymously without cookies or personally identifying information” (Netlify’s claim). It still counts by IP address | https://docs.netlify.com/manage/monitoring/web-analytics/overview/ and https://docs.netlify.com/manage/monitoring/web-analytics/how-web-analytics-works/ |
| Where data is stored | Sub-processors include AWS, Datadog, WorkOS, Fivetran, CrowdStrike. Processing may occur outside the EEA, UK and Switzerland (EU-US DPF, with SCCs as fallback). No region is stated | https://www.netlify.com/pdf/netlify-dpa.pdf (§6, §14) and https://trust-center.netlify-corp.com/ |

## Loaded by the browser automatically

Observed twice. Both runs found only same-origin requests and no cookies.

- Local copy of the repo (2026-09-29, Playwright and Chromium): all 7 HTML pages at 375px and 1280px, mobile
  menu closed and open. 176 requests, all to `http://localhost:8080`. No cookies.
- Deployed new site `https://tech-savvies-2.netlify.app/` (2026-09-28, research agent): `/`, `/solutions/`,
  `/our-story/`, `/contact/`, `/contact/thanks/` and a 404 URL, 375px and 1280px, menu closed and open.
  The only request origin was the site itself (HTML, 2 woff2 fonts, CSS, `main.js`, logo, and the
  self-hosted Grisha.studio image). No cookies, no `Set-Cookie` header, no script injected by Netlify. At
  1280px the menu toggle is hidden, so "menu open" was not tested there.
- Provisional: that run went through a TLS-intercepting proxy. Repeat it from a clean machine, and again
  after the move to `tech-savvies.com`.
- The old `https://tech-savvies.com` is a different build that still loads Microsoft Clarity and Google
  Fonts and allows `formsubmit.co` (headers and HTML, 2026-09-29). It is being replaced and is not part
  of this document’s table.

Response headers on the deployed new site match `netlify.toml`, including the CSP
(`default-src 'self'` …). The `third-party-allowlist` check in `tools/check_site.py` limits outbound `href`
origins to `ALLOWED_LINK_ORIGINS`: `https://grisha.studio`, plus the privacy-policy origins that
`/privacy/#sharing` links to (Netlify, Automattic, Apple, Squarespace, Anthropic, OpenAI; added 2026-09-29).

## Open items for the owner

1. ~~Spam filtering~~: done 2026-09-29. Akismet is on, and the honeypot is an extra layer. /privacy/ already names Akismet.
2. Retention: Netlify keeps submissions until deleted. Delete after 6 months by hand or script, or reword the policy.
3. Netlify dashboard readouts (Deploys, Forms, Analytics, Domain management, add-ons) are still needed.
4. Rerun the browser check from a clean machine.
5. Renew the domain before 2026-11-11. DNS stays in Netlify DNS at cutover; see [`../migration-plan.md`](../migration-plan.md).
6. Canonical tags already point to `https://tech-savvies.com/`; fine after the move.

## Adding a third party

- [ ] Add a row to the table in this file.
- [ ] Update `/privacy/` (and name it in the data-sharing text).
- [ ] Update `/cookies/`.
- [ ] Update the CSP in `netlify.toml` and `EXPECTED_CSP` in `tools/check_site.py`, and describe the change here.
- [ ] Add outbound link origins to `ALLOWED_LINK_ORIGINS` in `tools/check_site.py`.
- [ ] If the service sets cookies or tracks, follow `fix-prompts/05-cookie-consent.md`.
- [ ] Record the provider in `docs/business-facts.md` and re-run `python3 tools/check_site.py`.
