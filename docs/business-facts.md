# Business facts

The single source of truth for every name, price, address, hour, promise and legal term on the
site. Prompts read from this file and never invent a value. If a row says `TODO(owner)`, the
prompt that needs it asks the owner and records the answer here with the date.

Source column: who confirmed the value and when. "(from site, confirm)" means the repo
establishes it but the owner hasn't confirmed it yet.

## Identity

| Fact | Value | Source |
|------|-------|--------|
| Brand name | Tech-Savvies (logo reads "Tech-Savvies NYC") | (from site, confirm) |
| Founder | Peter Parizhsky | (from site, confirm) |
| History | Founded 2020, paused 2023, relaunched 2026 | (from site, confirm) |
| Domain | tech-savvies.com | (from site, confirm) |
| Hosting and contact form | Netlify, Netlify Forms | (from site, confirm) |
| Contact email | info@tech-savvies.com | (from site, confirm) |
| Legal business name | Peter Parizhsky | Owner, 2026-09-29 |
| Entity type | Sole proprietorship | Owner, 2026-09-29 |
| DBA (assumed name) filed? | No | Owner, 2026-09-29 |
| DBA county | Not applicable until a DBA is filed | Owner, 2026-09-29 |
| Public mailing address (PO box / virtual mailbox OK) | None. Online-only business with no physical location; use email only | Owner, 2026-09-29 |
| Person who signs client contracts is 18 or older | No, under 18 | Owner, 2026-09-29 |

## Service area and hours

| Fact | Value | Source |
|------|-------|--------|
| Service area | Anywhere (remote) | Owner, 2026-09-29 |
| What "business hours" means (days, times, ET) | No fixed hours. Work happens when there are clients and time after school | Owner, 2026-09-29 |
| Realistic first-reply time | Within 1 business day | Owner, 2026-09-29 |
| Realistic fastest delivery for Website Launch | 5 days, only as a rush order for a relatively simple site | Owner, 2026-09-29 |
| Serving EU/UK clients deliberately | No | Owner, 2026-09-29 |

## Prices

Current published prices are from `public/solutions/index.html`.

| Fact | Value | Source |
|------|-------|--------|
| Website Launch | $250-$375 (depending on website caliber and time frame) | (from site, confirm) |
| Website Rescue | $200 flat fee, "up to $250 rush order" | (from site, confirm) |
| Google Business Profile and Social Media Presence | $50 flat fee for a one-time fix; "monthly for ongoing management" | (from site, confirm) |
| What sets the $250 vs $375 Launch price | Features/complexity and turnaround time. Maximum complexity is charged the maximum price, with no rush option | Owner, 2026-09-29 |
| What makes an order a "rush" order | A 5-day delivery is a rush order | Owner, 2026-09-29 |
| Rush price for Website Launch | $375 | Owner, 2026-09-29 |

## Monthly management

| Fact | Value | Source |
|------|-------|--------|
| Monthly management price | $50/month | Owner, 2026-09-29 |
| What monthly management includes | Google Business Profile and social media upkeep | Owner, 2026-09-29 |
| How to cancel monthly management | Nothing to cancel: the plan covers one month at a time and continues only if the client re-books (earlier answer “email info@tech-savvies.com before the next month starts” superseded) | Owner, 2026-09-29 |
| Auto-renews until cancelled | No, manual (client re-books each month) | Owner, 2026-09-29 |

## Payment

| Fact | Value | Source |
|------|-------|--------|
| Deposit | 50% upfront | Owner, 2026-09-29 |
| Payment schedule | 50% upfront, 50% on delivery | Owner, 2026-09-29 |
| Accepted payment methods | Venmo, bank transfer | Owner, 2026-09-29 |
| Sales tax handling | Prices currently do not include tax; whether tax applies is not yet determined (owner needs advice, e.g. NY Dept. of Taxation and Finance or an accountant). TODO(owner) | Owner, 2026-09-29 |

## Scope, guarantee and refunds

| Fact | Value | Source |
|------|-------|--------|
| Revisions included | Unlimited within the agreed scope | Owner, 2026-09-29 |
| What the "completion guarantee" promises exactly | No extra billing if a project takes longer than expected (current site wording) | Owner, 2026-09-29 |
| Refund rule: before work starts | Full refund | Owner, 2026-09-29 |
| Refund rule: mid-project | Pro-rated for work done | Owner, 2026-09-29 |
| Refund rule: after delivery | Refund only if an issue can’t be fixed | Owner, 2026-09-29 |
| Refund rule: monthly plan | No refund for the current month; a next month happens only if the client re-books | Owner, 2026-09-29 |

## Domain, hosting and ownership

| Fact | Value | Source |
|------|-------|--------|
| Who pays for the client's domain and hosting | Client pays for the domain. Tech-Savvies guides them through buying it. Hosting is on Tech-Savvies’ own Netlify account | Owner, 2026-09-29 |
| Approximate domain and hosting cost | Domain cost depends on the domain the client chooses (paid by the client to the registrar). No separate hosting charge recorded | Owner, 2026-09-29 |
| Who owns the domain and hosting after handover | Tech-Savvies until paid in full, then the client | Owner, 2026-09-29 |
| Who owns the finished site and code after full payment | The client | Owner, 2026-09-29 |
| Portfolio-use rights | Only with the client’s written permission | Owner, 2026-09-29 |

## Data handling and tools

| Fact | Value | Source |
|------|-------|--------|
| Netlify Analytics on | Yes, on | Owner, 2026-09-29 |
| Netlify form notifications go to which inbox | info@tech-savvies.com | Owner, 2026-09-29 |
| Netlify spam filtering on | Owner says no, off (honeypot field only); Netlify’s docs say Akismet screens all submissions, so unconfirmed | Owner, 2026-09-29 |
| Mailbox provider for info@tech-savvies.com | iCloud | Owner, 2026-09-29 |
| Domain registrar for tech-savvies.com | Squarespace Domains II LLC (formerly Google Domains) | Owner, 2026-09-29 |
| Netlify Forms stored fields | Submission fields, IP address (`data.ip`), created-at; user agent and referrer unverified. Source: https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api/ (read 2026-09-28) | Netlify docs |
| Netlify submission retention | None documented; submissions stay until deleted. The 6-month rule is enforced by the owner. Source: https://docs.netlify.com/manage/forms/submissions/ | Netlify docs |
| Netlify spam filtering | Docs say Akismet filters all submissions and give no off switch, which conflicts with the owner’s “off”. Owner to check the dashboard. Source: https://docs.netlify.com/manage/forms/spam-filters/ | Netlify docs, conflict open |
| Netlify Analytics | Server-side from CDN logs, cookieless per Netlify; counts unique visitors by IP. Source: https://docs.netlify.com/manage/monitoring/web-analytics/overview/ | Netlify docs |
| Netlify data location | No region stated; AWS among sub-processors, transfers outside EEA under DPF/SCCs. Source: https://www.netlify.com/pdf/netlify-dpa.pdf | Netlify docs |
| Domain expiry | tech-savvies.com expires 2026-11-11; nameservers NS1, not Netlify DNS (RDAP) | Research, 2026-09-28 |
| Retention: form submissions | 6 months | Owner, 2026-09-29 |
| Retention: emails with leads | 12 months (all emails, leads and past clients) | Owner, 2026-09-29 |
| Sends or plans to send marketing/newsletter emails | No | Owner, 2026-09-29 |
| Uses email open-tracking | No | Owner, 2026-09-29 |
| Holds client account logins (Google Business Profile, social media) | Sometimes: some clients add Tech-Savvies as a manager; others who can’t or don’t want to share their login details | Owner, 2026-09-29 |

## Case study (Grisha.studio)

| Fact | Value | Source |
|------|-------|--------|
| Real client | Yes | Owner, 2026-09-29 |
| Written permission to feature | Yes, in writing | Owner, 2026-09-29 |
| Personal or family connection | Yes: the owner’s brother (Gregory Parizhsky). The owner asked that it not be on the homepage; a disclosure still has to sit with the case study or be easy to find (see compliance log #11) | Owner, 2026-09-29 |

## Brand assets

| Fact | Value | Source |
|------|-------|--------|
| Logo: who made it, with which tool, license terms | Drawn by the owner in Procreate | Owner, 2026-09-29 |
| OG image: who made it, with which tool, license terms | Coded by Claude Code from the owner’s logo | Owner, 2026-09-29 |
| Icons: who made them, with which tool, license terms | Favicon and app icons coded by Claude Code from the owner’s logo | Owner, 2026-09-29 |
