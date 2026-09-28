# Prompt 19: License fonts and images

Phase 4. Paste everything below the line into a new Claude Code session opened at the
repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/business-facts.md` and `docs/compliance-log.md`.

## Goal

Record, for every font, image, icon and design file in the repo, who made it, under what
licence it's used, and whether that licence is being followed. Put it in
`docs/asset-licenses.md`, fix any licence gap, and make new assets impossible to add without an
entry.

## Why

Using a font or image outside its licence can lead to takedown demands and damages claims, and
a web designer's own site is the first place clients and competitors look. What the audit
found:
- **Fonts:** `public/assets/fonts/plus-jakarta-sans-latin-wght-normal.woff2` and
  `jetbrains-mono-latin-500-normal.woff2` are SIL Open Font License 1.1, and the full licence
  texts ship alongside them (`LICENSE-PlusJakartaSans.txt`, `LICENSE-JetBrainsMono.txt`). That
  satisfies OFL's requirement to distribute the licence with the font. Neither licence declares a
  Reserved Font Name, so the latin-subset woff2 files (a "Modified Version" under OFL) can keep
  their names. **Compliant; document it.**
- **Images:** `logo.png`, `og-image.png`, `icon-192.png`, `icon-512.png`, `favicon-64.png`,
  `favicon.ico` and `apple-touch-icon.png` have no embedded metadata (it was probably stripped
  during optimisation), so their origin can't be read from the files. **Owner must supply
  provenance.**
- **Inline SVG icons** (menu, close, arrows, external-link) in the HTML, and the checkmark SVG in
  `styles.css`: simple paths. Check whether they were hand-drawn or copied from an icon set
  (Heroicons, Lucide, Feather, etc.), which would carry a licence with attribution or notice
  terms.
- **`design/Tech-Savvies_Website_Mockup.pdf`:** printed from Chromium; the author is presumably
  the owner.

## Task

1. **Inventory:** `find public design -type f` for every non-code asset, plus every inline
   `<svg>` and every `url(data:image/svg…)` in CSS. Compare the SVG path data against the common
   open icon sets (search their repos with `WebFetch` if a shape looks familiar, for example the
   arrow `M4 10h12M11 5l5 5-5 5` or the external-link `M5 11l6-6M6 5h5v5`). If one matches, note
   the set and its licence (MIT/ISC), and add the required notice.

2. **Fonts:** confirm each woff2's origin. The filenames match Fontsource's naming, so check the
   Fontsource package page and upstream repo with `WebFetch`. Confirm the licence files are the
   complete OFL 1.1 text with the correct copyright lines, and that they're publicly reachable
   next to the fonts (they are, under `public/assets/fonts/`). Record the upstream URL and
   version if you can determine them.

3. **Images:** ask the owner (`AskUserQuestion`, skipping anything already in
   `docs/business-facts.md`), for the logo and then the other images:
   - who made it (you / a designer / an online logo maker / Canva / an AI tool / other)?
   - do you have the source file?
   - if a designer made it, did they sign over the rights in writing?

   Record the answers. `og-image.png` looks like it was composed from the logo plus the two OFL
   fonts. If so, it's owner-made, and the OFL allows fonts to be used in images.

4. **Write `docs/asset-licenses.md`:** a table with `Asset`, `Path(s)`, `Creator`,
   `Source / upstream`, `Licence`, `Obligations` (for example "ship licence text", "keep
   copyright notice"), `Evidence` (where the proof lives, off-repo if it's a contract), `Status`.
   Add a section, "Adding an asset": no asset without a row; prefer self-made or OFL/CC0/MIT;
   never hotlink; keep licence files next to the asset if the licence requires it.

5. **Fix gaps:** add missing licence notices (for example, an icon-set MIT notice as
   `public/assets/LICENSES.md`, or a comment near the SVG, whichever the licence requires).
   Anything with unknown provenance becomes an owner action in `docs/compliance-log.md`, and
   Prompt 22 digs into copyright ownership.

6. **README:** add a short "Credits & licences" section linking `docs/asset-licenses.md`, and
   keep the existing "OFL licensed" note accurate.

7. **Guard.** Add an `asset-inventory` check to `tools/check_site.py`: every file under
   `public/assets/img/`, `public/assets/fonts/` and the root icon files must be mentioned in
   `docs/asset-licenses.md`.

8. Update item 19 in `docs/compliance-log.md`.

## Verify

- `python3 tools/check_site.py` passes. Adding a dummy `public/assets/img/x.png` to a temp copy
  fails the inventory check.

## Commit

`Fix #19: document asset licences and require an entry for new assets`. Push to the current
branch.
