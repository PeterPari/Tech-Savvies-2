# Asset licences

Every font, image, icon and design file in `public/` and `design/`, with who made it, where it came
from and what the licence requires. Owner answers are dated in [`business-facts.md`](business-facts.md)
(Brand assets). `python3 tools/check_site.py` (check `asset-inventory`) fails if a file in
`public/assets/img/`, `public/assets/fonts/` or the root icon files is not named here.

Contracts, permissions and source files stay outside the repo. The Evidence column says where.

## Inventory

| Asset | Path(s) | Creator | Source / upstream URL | Licence | Obligations | Evidence | Status |
|-------|---------|---------|-----------------------|---------|-------------|----------|--------|
| Plus Jakarta Sans (latin, variable weight, v5.3.0 npm package) | `public/assets/fonts/plus-jakarta-sans-latin-wght-normal.woff2` | The Plus Jakarta Sans Project Authors (Tokotype, Gumpita Rahayu) | https://fontsource.org/fonts/plus-jakarta-sans, npm `@fontsource-variable/plus-jakarta-sans@5.3.0` (https://www.npmjs.com/package/@fontsource-variable/plus-jakarta-sans), upstream https://github.com/tokotype/PlusJakartaSans | SIL OFL 1.1 | Ship the copyright notice and licence text with the font; no Reserved Font Name is declared, so the latin subset keeps its name; don’t sell the font on its own | Byte-identical (SHA-256 `153fc85b…5e79`) to `files/plus-jakarta-sans-latin-wght-normal.woff2` in the 5.3.0 package, checked 2026-09-29 | Documented, obligations met |
| Plus Jakarta Sans licence | `public/assets/fonts/LICENSE-PlusJakartaSans.txt` | The Plus Jakarta Sans Project Authors | Same package | SIL OFL 1.1 (full text) | Stays beside the font | In repo | Documented, obligations met |
| JetBrains Mono (latin, weight 500, v5.3.0 npm package) | `public/assets/fonts/jetbrains-mono-latin-500-normal.woff2` | The JetBrains Mono Project Authors (JetBrains) | https://fontsource.org/fonts/jetbrains-mono, npm `@fontsource/jetbrains-mono@5.3.0` (https://www.npmjs.com/package/@fontsource/jetbrains-mono), upstream https://github.com/JetBrains/JetBrainsMono | SIL OFL 1.1 | Same as above; no Reserved Font Name declared | Byte-identical (SHA-256 `cb182fee…553a`) to `files/jetbrains-mono-latin-500-normal.woff2` in the 5.3.0 package, checked 2026-09-29 | Documented, obligations met |
| JetBrains Mono licence | `public/assets/fonts/LICENSE-JetBrainsMono.txt` | The JetBrains Mono Project Authors | Same package | SIL OFL 1.1 (full text) | Stays beside the font | In repo | Documented, obligations met |
| Logo | `public/assets/img/logo.png` | Peter Parizhsky, drawn in Procreate | None (original work) | Owned by the owner; no third-party licence | None | Owner answer 2026-09-29. The Procreate source file no longer exists; the PNG is the only master | Documented; source file lost (keep the PNG safe) |
| Social share image (OG) | `public/assets/img/og-image.png` | Claude Code, coded from the owner’s logo (uses the two OFL fonts above) | None | Owner’s logo plus OFL fonts; no other third-party material known | Follows the logo and font terms above | Owner answer 2026-09-29 | Documented |
| App icon 192 | `public/assets/img/icon-192.png` | Claude Code, coded from the owner’s logo | None | As the logo | None | Owner answer 2026-09-29 | Documented |
| App icon 512 | `public/assets/img/icon-512.png` | Claude Code, coded from the owner’s logo | None | As the logo | None | Owner answer 2026-09-29 | Documented |
| Favicon 64 | `public/assets/img/favicon-64.png` | Claude Code, coded from the owner’s logo | None | As the logo | None | Owner answer 2026-09-29 | Documented |
| Favicon | `public/favicon.ico` | Claude Code, coded from the owner’s logo | None | As the logo | None | Owner answer 2026-09-29 | Documented |
| Apple touch icon | `public/apple-touch-icon.png` | Claude Code, coded from the owner’s logo | None | As the logo | None | Owner answer 2026-09-29 | Documented |
| Grisha.studio screenshot (client’s website and artwork) | `public/assets/img/grisha-studio.webp` | Screenshot by the owner; the site and artwork belong to the client (Gregory Parizhsky) | https://grisha.studio | Client’s rights; used under the client’s written permission covering the name, the link and this screenshot | Keep the disclosure next to the case study; remove the image if the client withdraws permission | Client’s written message, kept outside the repo (owner, 2026-09-29; see business-facts, Case study) | Permission on file. Prompt 22 decides on ownership risk |
| Website mockup | `design/Tech-Savvies_Website_Mockup.pdf` | Owner and Claude Code (printed from Chromium) | None | Owner’s; not served to visitors | None | Owner answer 2026-09-29 | Documented |
| Menu icon (three lines) | Inline SVG, path `M4 7h16M4 12h16M4 17h16`, in the header of every page | Claude Code | None | Written for this site; no icon set | None | Owner answer 2026-09-29 | Documented |
| Close icon (cross) | Inline SVG, path `M6 6l12 12M18 6L6 18`, in the header of every page | Claude Code | None | As above | None | Owner answer 2026-09-29 | Documented |
| Arrow icon | Inline SVG, path `M4 10h12M11 5l5 5-5 5`, in buttons | Claude Code | None | As above | None | Owner answer 2026-09-29 | Documented |
| External-link icon | Inline SVG, path `M5 11l6-6M6 5h5v5`, on links that open a new tab | Claude Code | None | As above | None | Owner answer 2026-09-29 | Documented |
| Green checkmark (CSS data-URI, viewBox 1124×1156, one `path`) | `public/assets/css/styles.css`, `.checklist li::before` | Pasted by the owner from a Claude chat reply; no icon set or website named | None known | Unknown; no icon-set match claimed | If it turns out to come from an icon set, add that set’s notice to `public/assets/LICENSES.md` | Owner answer 2026-09-29 | origin unknown: owner action (find the chat, or replace with a self-made check) |
| Select-box chevron (CSS data-URI, viewBox 12×8, path `M1 1.5l5 5 5-5`) | `public/assets/css/styles.css`, `select.input` | Claude Code (part of the site’s form styles) | None | Written for this site | None | Same page as the form styles | Documented (owner has not been asked separately) |

Not listed, because they are code or data rather than assets: `site.webmanifest`, `robots.txt`,
`sitemap.xml`, the CSS and JS. The `public/admin/` checklist has no images.

## Adding an asset

1. Add a row to this table before the asset goes into the repo, with creator, source, licence and where the proof is kept.
2. Prefer self-made work, then SIL OFL, CC0 or MIT material. Anything else needs the owner’s approval and a written licence.
3. No hotlinking: host every font, image and icon in `public/assets/`. The CSP and `no-external-resources` check enforce this.
4. Keep the licence file beside the asset when the licence requires it (as for the OFL fonts), and add an icon set’s notice to `public/assets/LICENSES.md` when its licence asks for one.
