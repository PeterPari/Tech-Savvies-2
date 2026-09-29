# Tech-Savvies website

The Tech-Savvies site, built from the mockup in [`design/Tech-Savvies_Website_Mockup.pdf`](design/Tech-Savvies_Website_Mockup.pdf).
It is plain HTML, CSS and a little JavaScript, with no build step and no dependencies.

## Pages

| URL | File | Content |
| --- | --- | --- |
| `/` | `public/index.html` | Hero, What we offer, Featured Showcase, Start Your Project |
| `/solutions/` | `public/solutions/index.html` | Core Services and pricing |
| `/our-story/` | `public/our-story/index.html` | Our Story |
| `/contact/` | `public/contact/index.html` | Contact info and the contact form |
| `/contact/thanks/` | `public/contact/thanks/index.html` | Shown after the form is sent (not indexed by Google) |
| `/terms/` | `public/terms/index.html` | Terms of Service (linked from every footer’s Legal column and the /solutions/ Payment block) |
| `/refunds/` | `public/refunds/index.html` | Refund Policy (linked from every footer’s Legal column, the /solutions/ Payment block and the refund wording in /terms/) |
| `/privacy/` | `public/privacy/index.html` | Privacy Policy (linked from every footer’s Legal column) |
| `/cookies/` | `public/cookies/index.html` | Cookie Policy (linked from every footer’s Legal column) |
| `/accessibility/` | `public/accessibility/index.html` | Accessibility statement: WCAG 2.2 AA aim, what was tested, known limitations, how to report a barrier (linked from every footer’s Legal column) |
| any missing page | `public/404.html` | Page not found |
| `/admin/` | `public/admin/index.html` | Internal prompt checklist (not linked, not indexed; generated, see below) |

Everything the site serves lives in `public/`:

```
public/
  assets/css/styles.css   all styles; colors, fonts and sizes are variables at the top
  assets/js/main.js       mobile menu (inert page behind it), focus clearance, footer year, form errors and double-submit guard
  assets/fonts/           Plus Jakarta Sans + JetBrains Mono (self-hosted, OFL licensed)
  assets/img/             logo, icons, social share image
  robots.txt, sitemap.xml, site.webmanifest, favicon.ico, apple-touch-icon.png
docs/                     business-facts.md (owner fills in), data-inventory.md (personal data and retention), data-requests-runbook.md (how to complete a data request), compliance-log.md (status of the 25 items), claims-register.md (evidence for every claim)
tools/                    check_site.py (regression checker), build_admin.py
```

## Checks

`python3 tools/check_site.py` (standard library only, run from the repo root) exits 1 and prints
`path:line: [check-name] message` for each problem. It guards image alt text, external resources,
client-side storage, the CSP, review schema, unsupported claims, placeholder text, internal links, new-tab links,
the shared header and footer, and that every price and the completion guarantee on `/solutions/` match `/terms/`.
Changing a price, promise or refund rule? Change `/solutions/`, `/terms/`, `/refunds/` and `docs/business-facts.md` together. GitHub Actions runs it, and `python3 tools/build_admin.py --check`,
on every push and pull request. To add a check, see the comment at the top of the script.

Adding analytics or any cookie? Read fix-prompts/05-cookie-consent.md first.

## Credits & licences

Fonts: Plus Jakarta Sans and JetBrains Mono, SIL Open Font License 1.1, self-hosted with their licence texts in `public/assets/fonts/`.
Logo: drawn by the owner. Icons and the share image: made for this site from the logo.
The Grisha.studio screenshot is used with the client’s written permission.
Every asset, its creator, source and licence: [`docs/asset-licenses.md`](docs/asset-licenses.md).
Adding an image, font or icon? Add its row there first; `check_site.py` (`asset-inventory`) checks it.

## Preview locally

Pages link to files with paths like `/assets/...`, so open the site through a local web server
(double-clicking the HTML files won't load the styles):

```sh
python3 -m http.server 8080 --directory public
# or: npx serve public
```

Then visit <http://localhost:8080>.

## Editing

- **Text:** edit the HTML file for that page. On the two big headlines, the periods and
  apostrophes are wrapped in `<span class="kern-dot">` / `<span class="kern-apos">` to tuck
  them in tighter, like in the mockup. Keep those spans if you change the wording.
- **Header and footer:** repeated in every HTML file except `/admin/` (9 files). Change all of them together.
- **Business details:** the legal name (Peter Parizhsky) appears in the footer copyright line
  of every page, the `legalName` in the JSON-LD in `public/index.html`, the `LEGAL_NAME` constant
  in `tools/check_site.py`, and one sentence on `/our-story/`. "New York, NY" appears in every
  footer, the JSON-LD `address`, and the `.contact-info` block on `/contact/`, which also holds the
  service area and reply time. Source of truth: `docs/business-facts.md`. There is no mailing
  address or fixed hours to show; add them everywhere above if that changes.
- **New UI:** follow the honest-UI rules in [`docs/ux-honesty-rules.md`](docs/ux-honesty-rules.md).
- **Images and alt text:** every image and icon must have a text alternative for accessibility (WCAG 1.1.1). 
  1. *Linked logos* (a logo that links to a page): `alt="Tech-Savvies NYC home"` names the destination.
     Example: `<a href="/"><img alt="Tech-Savvies NYC home" …></a>`
  2. *Meaningful images* (screenshots, case studies): describe content in ≤125 characters, no "image of" prefix.
     Example: `alt="The Grisha.studio home page, showing the name Gregory Parizhsky beside a photo…"`
  3. *Decorative SVGs* (icons in buttons, menu toggles): mark as `aria-hidden="true" focusable="false"`.
     Example: `<svg aria-hidden="true" focusable="false">…</svg>`
  4. *Social cards* (og:image): both `og:image:alt` and `twitter:image:alt` must describe the card image.
     Example: `<meta property="og:image:alt" content="…"><meta name="twitter:image:alt" content="…">`
  Reference: [W3C alt decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/).
- **Colors, fonts, spacing:** the variables at the top of `public/assets/css/styles.css`.
- **Domain:** links for Google and social sharing use `https://tech-savvies.com`
  (the `canonical` and `og:` tags in each page, `sitemap.xml` and `robots.txt`).
  Update them if the site ends up on a different domain.

## Deploy on Netlify

1. In Netlify, choose **Add new site** (newer accounts: **Add new project**) → **Import an existing project**,
   and pick this repository.
2. Leave the build command empty. `netlify.toml` already tells Netlify to publish the `public/` folder.
3. Add the custom domain under **Domain management**. Netlify sets up HTTPS automatically.

`netlify.toml` also adds security headers, including a Content Security Policy that only allows
files from this site. If you later add a third-party script, font, video embed or analytics tool,
add its domain to that policy or the browser will block it.

## Contact form (Netlify Forms)

The form on `/contact/` is a Netlify form named `contact`. It works without any server code, but
two settings have to be switched on in the Netlify dashboard once the site is deployed:

1. **Turn on form detection:** open the site's **Forms** page and enable form detection (if it isn't
   already on), then redeploy. Netlify finds the form in `contact/index.html` during the deploy.
2. **Get submissions by email:** in the site's configuration, open **Notifications → Emails and webhooks**
   and add a *form submission notification* sent to `info@tech-savvies.com`.

Submissions also appear on the **Forms** page in Netlify. A hidden honeypot field (`bot-field`)
filters out simple spam bots. After sending, visitors land on `/contact/thanks/`.
The form can't be tested with a local server, so test it after deploying to Netlify.

## Prompt checklist (`/admin/`)

`/admin/` lists the compliance fix prompts from `fix-prompts/` in run order. Each row has a
checkbox, the model and effort to use, a one-click copy button, and the full prompt text. It
isn't linked from any page and is marked `noindex`, but anyone with the URL can open it.
Checkmarks are saved in your browser only.

The page is generated. After editing a prompt or the tables in `fix-plan.md`, rebuild it:

```sh
python3 tools/build_admin.py          # rewrite public/admin/index.html
python3 tools/build_admin.py --check  # fail if it's out of date
```
