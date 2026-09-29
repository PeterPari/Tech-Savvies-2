# Migration plan: moving tech-savvies.com to the new site

This plan moves `tech-savvies.com` from the old site (repo
[PeterPari/Tech-Savvies](https://github.com/PeterPari/Tech-Savvies), on its own Netlify site) to this
repo's site, which already runs at `https://tech-savvies-2.netlify.app/`. The goal is to keep the search
rankings and recognition the old site has built up.

The findings below come from the live site, the old repo, public DNS and a web search, all checked on
2026-09-29. Work happens on the branch `migration`.

---

## In short

- **The domain stays the same, so most SEO carries over automatically.** Google ties rankings to URLs, and
  on this domain almost every page URL changes (`/services` → `/solutions/`, `/about` → `/our-story/`).
  Every old URL gets a permanent (301) redirect to its new page, and the redirects stay for good. That is
  the main SEO work.
- **The domain expires on 2026-11-11.** If it lapses, the rankings, the website and the
  `info@tech-savvies.com` mailbox all go with it. Renew it first (Phase 0).
- **Email and Search Console live in the same DNS zone as the website.** The move must not touch the
  iCloud mail records or the Google verification record. The recommended cutover changes no DNS records.
- **Recommended cutover:** move the domain from the old Netlify site to the `tech-savvies-2` Netlify site.
  That site already deploys this repo and already has the contact form, spam filter and notifications set
  up. The move takes about 15 minutes, plus a few minutes while Netlify issues the HTTPS certificate.
- **What to expect:** a small wobble in rankings for 2 to 6 weeks, and searches for the brand name should
  recover within days to a couple of weeks. Rankings for things the new site no longer offers (IT support,
  ecommerce, brand kits, automation, "Upper West Side") will fade. That comes from the new positioning,
  not from the migration, and no redirect can keep it.

---

## 1. What's there today

### Hosting, DNS and search engines

| Item | Finding | Evidence |
|------|---------|----------|
| Old site | Netlify, published from the root of PeterPari/Tech-Savvies. Serves `tech-savvies.com`; `www` and `http://` 301 to `https://tech-savvies.com/` | `server: Netlify` header; old repo `netlify.toml` |
| New site | Netlify site `tech-savvies-2`, deploying `main` of this repo | `https://tech-savvies-2.netlify.app/` serves this repo's `public/` |
| DNS | **Netlify DNS** (Netlify runs it on NS1 servers) | Nameservers `dns1-4.p06.nsone.net`; SOA contact `domains+netlify.netlify.com`; apex and `www` answer with Netlify's flattened A records instead of a CNAME. This corrects the earlier note in `docs/business-facts.md` that it is "not Netlify DNS" |
| Other records in the zone | iCloud mail: 2 MX records, SPF TXT, `apple-domain` TXT. Google Search Console: `google-site-verification` TXT | Public DNS lookup |
| Registrar, expiry | Squarespace Domains, **expires 2026-11-11** | `docs/business-facts.md` (RDAP) |
| Google Search Console | Verified by the DNS TXT record, so verification survives the move as long as that record stays | TXT record above |
| Bing | No verification tag found | Old HTML |
| Analytics on the old site | Microsoft Clarity. The new site has none, and its CSP blocks it; Netlify Analytics is on | Old HTML; `docs/tracking-audit.md` |
| Old Netlify build plugins | Probably installed in the Netlify UI: the live `sitemap.xml` has the format of a sitemap plugin (lists `/404`, `priority 0.8` everywhere), and the live HTML is minified although the repo's isn't. Not a problem for the recommended cutover; important for Option A (Phase 3) | Live `sitemap.xml` and HTML against the old repo |

### Every old URL and where it goes

Google has probably indexed the `.html` versions of the inner pages, because their canonical tags point
there, while the old sitemap lists the extensionless ones. Both get redirects.

| Old URL | Live today | Notes | New URL |
|---------|-----------|-------|---------|
| `/` | 200 | | `/` (same URL) |
| `/services`, `/services.html` | 200 | Canonical is `/services.html`; `/services` is in the old sitemap | `/solutions/` |
| `/about`, `/about.html` | 200 | Canonical is `/about.html` | `/our-story/` |
| `/contact` | 200 | Canonical is `/contact.html` | `/contact/` (Netlify adds the slash itself, checked on the new site) |
| `/contact.html` | 200 | | `/contact/` |
| `/about/`, `/services/`, `/contact/` | 301 to no slash | Netlify matches redirect rules with or without the slash, so the rules above cover them | as above |
| `/index.html` | 200 | Canonical `/` | No rule: the new site serves it with canonical `/` |
| `/services.md`, `/about.md` | 200 | Markdown copies for AI crawlers, listed in the old `llms.txt` | `/solutions.md`, `/our-story.md` |
| `/index.md`, `/contact.md`, `/llms.txt` | 200 | The new site has files at the same paths | No rule |
| `/content/*.md` | 404 on the live build, present in the old repo | | Matching new `.md` file |
| `/404` | 200 with `noindex`, listed in the old sitemap by mistake | | No rule; the new site returns a real 404 |
| `/who-is-tech-savvies` | 404 already | From an older generation of the site; a web search still lists `www.tech-savvies.com/who-is-tech-savvies` with a "discontinued" notice | `/our-story/` |
| `/assets/logo.png` | 200 | Old share image, logo in the old structured data and image sitemap | `/assets/img/logo.png` |
| `/assets/logo.webp` | 200 | | `/assets/img/logo.png` |
| `/assets/favicon.png` | 200 | | `/assets/img/favicon-64.png` |
| `/assets/icon-192.png` | 200 | | `/assets/img/icon-192.png` |
| `/assets/icon-512.png`, `/assets/icon-512-maskable.png` | 200 | | `/assets/img/icon-512.png` |
| `/assets/showcase-farm.webp` | 200 | Nothing equivalent on the new site | No rule (404) |
| `/humans.txt`, `/security.txt` | 200 | Not used for search | No rule (404) |
| `/sw.js` | 200 | The old site's service worker, see below | Served as a file (see below), not redirected |
| `/site.webmanifest` | 200 | Same path on the new site | No rule |

Phase 0 checks this list against Google's own data (Search Console) before cutover, in case Google
knows a URL that neither the old repo nor the live site shows.

### Something the old site left in visitors' browsers

The old site registers a service worker (`/sw.js`) that caches pages in the browser. Browsers that
visited the old site keep it after the move. If `/sw.js` then returns 404, the old worker stays installed
and can serve old pages to anyone offline or on a flaky connection. A browser won't accept a worker
script that redirects, so the new site must serve a small `/sw.js` that deletes the old caches and
unregisters itself. It only runs in browsers that already have the old worker. It adds no storage, and
the CSP already allows it (`script-src 'self'`).

### SEO differences between the two sites

| Page | Old title | New title |
|------|-----------|-----------|
| Home | Tech-Savvies \| Rapid Web Development & IT Support in New York City | Tech-Savvies \| Websites done fast. Websites done right. |
| Solutions | Solutions & Pricing \| Tech-Savvies - NYC Web Development & IT Services | Solutions & Pricing \| Tech-Savvies |
| Our Story | Our Story \| Tech-Savvies - NYC Web Development by Peter Parizhsky | Our Story \| Tech-Savvies |
| Contact | Contact Us \| Tech-Savvies - NYC Web Development & IT Services | Contact \| Tech-Savvies |

- **Titles:** the new titles drop the words people search for ("web development", "website", the
  founder's name). Titles are the strongest on-page signal, so this is the biggest content-side risk.
  Decision D2.
- **Structured data:** the new home page already has `ProfessionalService` with a New York address,
  which covers most of what the old `LocalBusiness` block did. It has no `WebSite` block, which Google
  uses to choose the site name shown in results (the old site had one). The old block also listed the
  misspellings "Tech Savvies", "Tech-Savvys" and "Tech Savvys" as `alternateName`.
- **Services:** the old site sold Ecommerce Setup, Brand Kit, Social Asset Batch, IT Automation and
  Concierge IT, and targeted the Upper West Side (10025). `docs/business-facts.md` now says the business
  is online-only and serves anyone remotely. Rankings for those services and that neighbourhood won't
  carry over.
- **Improvements the new site already brings:** a real 404 instead of a `200` page listed in the sitemap,
  one URL per page instead of `/about` and `/about.html` both returning 200, legal pages, and faster pages
  with no third-party scripts.

---

## 2. Redirect map

Added at the end of `netlify.toml`, outside the generated `BEGIN/END plain-text mirrors` block. Targets
are relative, so the same rules work on `tech-savvies-2.netlify.app` for testing and on
`tech-savvies.com` after cutover.

```toml
# Old site (before the 2026 relaunch): send every URL search engines know to the matching new page.
# Keep these for good. Removing one turns old links and search results into 404s. A rule stops working
# if a file with the same path is added to public/ (check_site.py `legacy-redirects` guards this).
[[redirects]]
  from = "/services"
  to = "/solutions/"
  status = 301
```

The full list, one `[[redirects]]` entry each, all `status = 301`:

| From | To |
|------|----|
| `/services`, `/services.html` | `/solutions/` |
| `/about`, `/about.html`, `/who-is-tech-savvies` | `/our-story/` |
| `/contact.html` | `/contact/` |
| `/services.md`, `/content/services.md` | `/solutions.md` |
| `/about.md`, `/content/about.md` | `/our-story.md` |
| `/content/contact.md` | `/contact.md` |
| `/content/index.md` | `/index.md` |
| `/assets/logo.png`, `/assets/logo.webp` | `/assets/img/logo.png` |
| `/assets/favicon.png` | `/assets/img/favicon-64.png` |
| `/assets/icon-192.png` | `/assets/img/icon-192.png` |
| `/assets/icon-512.png`, `/assets/icon-512-maskable.png` | `/assets/img/icon-512.png` |

Rules deliberately left out:

- `/contact` → `/contact/`: Netlify already does this, and an explicit rule would loop, because Netlify
  treats `/contact` and `/contact/` as the same path when matching rules.
- A catch-all to the home page: Google treats a mass redirect to `/` as a soft 404, so unknown URLs
  should get the real 404 page.
- `force = true`: none of the old paths exist in `public/`, so no rule needs it.

---

## 3. Step by step

### Phase 0: Before anything changes (owner, about an hour, this week)

1. **Renew `tech-savvies.com`** at Squarespace Domains and turn on auto-renew. It expires 2026-11-11.
   Do this even if the cutover waits.
2. **Search Console baseline.** In the `tech-savvies.com` property:
   - Performance → last 16 months → Export (Pages and Queries tabs).
   - Indexing → Pages → export the indexed URLs.
   - Links → Top linked pages → export.

   Send the three exports to Claude. Any URL with impressions or external links that's missing from
   the redirect map gets a rule before cutover.
3. **Netlify readouts:**
   - Which team holds the old site, the `tech-savvies-2` site and the `tech-savvies.com` DNS zone
     (Netlify → Domains). The recommended cutover needs all three in the same team.
   - Which site Netlify Analytics is on.
   - The old site's name (`<name>.netlify.app`), for rollback.
4. **Back up the DNS zone:** screenshot or export every record in Netlify → Domains →
   `tech-savvies.com`. At minimum: 2 MX, the SPF TXT, the `apple-domain` TXT and the
   `google-site-verification` TXT.
5. **Decide D1 to D4** (section 4).

### Phase 1: Code on the `migration` branch (Claude, one session)

1. Add the redirect map (section 2) to `netlify.toml`.
2. Add `public/sw.js`, the self-removing service worker, with a comment saying why it exists and to keep
   it. Test it locally with Playwright:
   - serve the old repo on `localhost:8080` and load it, so its worker registers;
   - serve `public/` on the same port and reload;
   - confirm no service worker is registered and Cache Storage is empty.
3. Add a `legacy-redirects` check to `tools/check_site.py`. It fails if a rule from the map is missing
   from `netlify.toml`, if a file in `public/` shadows a rule's path, or if `public/sw.js` is missing.
4. Add `tools/check_migration.py`, standard library only: `python3 tools/check_migration.py <base-url>`.
   It checks against a live deploy:
   - every old URL returns a 301 to the right target, and the target returns 200;
   - every sitemap URL returns 200, its canonical path matches, and it has no `noindex`;
   - `/contact` ends up at `/contact/`;
   - `/sw.js` returns 200 as JavaScript;
   - with `--production` also: `http://` and `www` redirect to `https://tech-savvies.com/`,
     `tech-savvies-2.netlify.app` redirects to the domain, and the MX and verification TXT records still
     resolve.
5. Add a `WebSite` JSON-LD block to the home page (`name` "Tech-Savvies", `url`), plus `alternateName`
   if the owner approves it in D2.
6. Apply the title and description changes the owner approves in D2, then rerun
   `python3 tools/build_markdown.py`.
7. If D4 is yes, delete the stale copy of the site at the repo root (see D4).
8. Documentation:
   - a Migration row in the README;
   - the DNS correction in `docs/business-facts.md` and `docs/third-parties.md`.
9. `python3 tools/check_site.py`, `python3 tools/build_admin.py --check` and
   `python3 tools/build_markdown.py --check` must all exit 0. Commit and push to `migration`.

### Phase 2: Test on tech-savvies-2.netlify.app

1. Merge `migration` into `main`. This is safe before cutover: `main` only deploys to
   `tech-savvies-2.netlify.app`, not to the live domain.
2. Run `python3 tools/check_migration.py https://tech-savvies-2.netlify.app`. It must pass.
3. Send one real message through the contact form on `tech-savvies-2.netlify.app` and confirm it
   reaches `info@tech-savvies.com` and lands on `/contact/thanks/`.

### Phase 3: Cutover (owner in Netlify, about 15 minutes, at a quiet time such as a weekday evening ET)

**Recommended (Option B): move the domain to the `tech-savvies-2` site.**

1. In `tech-savvies-2` → Deploys, confirm the latest `main` deploy is published and includes the
   redirects.
2. Old site → Domain management: remove `www.tech-savvies.com`, then `tech-savvies.com`. **If Netlify
   offers to delete the DNS zone or its records, say no.** It holds the email and Search Console records.
3. `tech-savvies-2` → Domain management → Add a domain → `tech-savvies.com`. Netlify detects the Netlify
   DNS zone. Make it the primary domain and confirm `www.tech-savvies.com` is listed as redirecting to it.
4. Domain management → HTTPS: wait for "Your site has HTTPS enabled", usually within minutes. Until
   then, returning visitors see a certificate warning. The old site sent a one-year HSTS header, so
   their browsers won't fall back to `http://`.
5. Compare the DNS zone with the Phase 0 backup: the MX and TXT records must all still be there.
6. Run `python3 tools/check_migration.py https://tech-savvies.com --production`. It must pass.
7. Send one real message through the form on `https://tech-savvies.com/contact/`.

**Rollback:** remove the domain from `tech-savvies-2` and add it back to the old site (about 10 minutes
plus HTTPS). Leave the old Netlify site untouched for at least 8 weeks.

**Option A, if the three items in Phase 0 step 3 aren't in one team:** relink the old Netlify site to
this repo (Site configuration → Build & deploy → Continuous deployment → Manage repository → Link to a
different repository). There's no HTTPS gap, and rollback is one click (Deploys → an old deploy →
Publish deploy). But first:

- clear the old site's build command;
- remove its UI-installed build plugins (a sitemap plugin would overwrite `public/sitemap.xml` with
  `/404`, `/admin/` and `/contact/thanks/` in it);
- turn on form detection, the `info@` notification and Analytics there;
- afterwards, delete the `tech-savvies-2` site so its `netlify.app` copy doesn't stay online as a
  duplicate.

### Phase 4: Same day, tell search engines (owner, about 20 minutes)

1. **Google Search Console:**
   - Sitemaps: submit `https://tech-savvies.com/sitemap.xml` again. The address is the same, but the
     contents are new.
   - URL Inspection: for `/`, `/solutions/`, `/our-story/` and `/contact/`, run Test live URL, then
     Request indexing.
   - URL Inspection: run a live test on `https://tech-savvies.com/services.html` and confirm it
     reports the redirect.
2. **Bing Webmaster Tools:** sign in, import the site from Google Search Console and submit the sitemap.
   Bing also feeds DuckDuckGo and several AI search tools.
3. **Update links you control**, so they skip the redirect: Google Business Profile website field (if
   there is one), social profile bios, email signature, directory listings, and the old repo's README.
   Point each at the new URLs (`/solutions/`, not `/services.html`).
4. **Retire Microsoft Clarity:** delete the Clarity project and its recordings.
5. **Claude, follow-up commit:**
   - remove the "older build loads Clarity" sentences from `/cookies/` and `/privacy/`, as
     `docs/compliance-log.md` asks after go-live;
   - rerun the tracking audit against the live domain, as `docs/tracking-audit.md` asks.

### Phase 5: Watch (weeks 1 to 12)

| When | Check |
|------|-------|
| Day 1 and day 3 | `check_migration.py --production` passes. Search Console → Pages shows no new 404s among the old URLs |
| Weekly, weeks 1–4 | Pages report: old URLs move to "Page with redirect", which is expected and good. Any old URL under "Not found (404)" gets a redirect rule. Performance: compare clicks and impressions for "tech-savvies" / "tech savvies" with the baseline |
| Week 8 | If traffic has settled: delete the old Netlify site, so its `netlify.app` copy stops serving the old pages, and archive (don't delete) the old GitHub repo |
| Week 12 | Compare with the Phase 0 export. Rankings for services the site still offers should be back. Queries for dropped services are expected to be gone |

Keep the redirects and `/sw.js` permanently. Google recommends keeping redirects at least a year, and
they cost nothing.

---

## 4. Decisions for the owner

| # | Decision | Recommendation |
|---|----------|----------------|
| D1 | Cutover method: Option B (move the domain to `tech-savvies-2`) or Option A (relink the old site to this repo) | **B**, unless Phase 0 shows the sites and DNS zone are in different Netlify teams |
| D2 | Titles, descriptions and `alternateName`: keep the slogan titles, or add the words people search for | Put what you sell in the Home and Solutions titles, and your name in Our Story, using only wording already in `docs/business-facts.md`. For example, Home: "Tech-Savvies \| Affordable websites for small businesses and creators". Our Story: "Our Story: Peter Parizhsky \| Tech-Savvies". Also confirm whether "Tech Savvies", "Tech-Savvys" and "Tech Savvys" may be listed as alternate names |
| D3 | Cutover date | First half of October 2026, after Phase 0 step 1 (renewal) and Phase 2 pass. Not in the days just before 2026-11-11 unless the domain is already renewed |
| D4 | Delete the stale copy of the site at the repo root (`index.html`, `assets/`, `privacy/` and more). It was committed by accident in `2141dee` ("Fix #06") and no longer matches `public/` | **Yes.** Netlify serves only `public/`, so visitors never see it, but it's easy to edit by mistake, and it would go live if the publish folder ever changed |

---

## 5. Things that would hurt SEO (don't)

- Let the domain expire, or delete or recreate the DNS zone.
- Use 302 (temporary) redirects, or send every old URL to the home page.
- Block old URLs in `robots.txt`. Google has to crawl them to see the redirects.
- Use Search Console's Removals tool on old URLs, or its Change of Address tool. That tool is only for
  moving to a different domain.
- Switch the preferred domain to `www`. Canonical tags, the sitemap and the old site all use
  `https://tech-savvies.com`.
- Remove the redirects later, or add a page in `public/` at an old path such as `/about/` without also
  removing its redirect rule.
- Publish with `noindex` on any page in the sitemap. `check_migration.py` checks this.
