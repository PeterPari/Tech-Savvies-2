# Prompt 19: License fonts and images

````text
<context>
Audit findings:
- Fonts: public/assets/fonts/plus-jakarta-sans-latin-wght-normal.woff2 and jetbrains-mono-latin-500-normal.woff2 are under SIL OFL 1.1. The full licence texts ship beside them (LICENSE-PlusJakartaSans.txt, LICENSE-JetBrainsMono.txt), and neither declares a Reserved Font Name, so the latin subsets can keep their names. The filenames follow Fontsource's naming.
- Images: logo.png, og-image.png, icon-192.png, icon-512.png, favicon-64.png, favicon.ico and apple-touch-icon.png carry no embedded metadata, so their origin must come from the owner. og-image.png looks like the logo composed with the two OFL fonts.
- Inline SVG icons in the HTML (menu, close, arrow "M4 10h12M11 5l5 5-5 5", external link "M5 11l6-6M6 5h5v5") and the checkmark SVG in styles.css have no recorded source. If one comes from an icon set (Heroicons, Lucide, Feather, etc.), it carries a licence notice requirement.
- design/Tech-Savvies_Website_Mockup.pdf was printed from Chromium.
</context>

<inputs>
docs/business-facts.md, docs/compliance-log.md, public/, design/
</inputs>

<deliverables>
1. docs/asset-licenses.md, containing:
   - one row per non-code asset in public/ and design/, per inline SVG shape, and per CSS data-URI image, with the columns Asset | Path(s) | Creator | Source / upstream URL | Licence | Obligations | Evidence (location of the proof, outside the repo for contracts) | Status;
   - a section "Adding an asset" with 4 rules: a row before the asset is added; prefer self-made, OFL, CC0 or MIT; no hotlinking; keep licence files beside assets when the licence requires it.
2. For any SVG matching an icon set: the set's notice added where its licence requires it (for example public/assets/LICENSES.md).
3. A "Credits & licences" section in the README, of at most 5 lines, linking docs/asset-licenses.md.
4. A check named asset-inventory in tools/check_site.py: every file in public/assets/img/, public/assets/fonts/, and the root icon files is named in docs/asset-licenses.md.
5. The owner's answers recorded in docs/business-facts.md. Item 19 updated in docs/compliance-log.md, with any asset of unknown origin listed as an owner action.
6. One commit, "Fix #19: document asset licences", pushed.
7. A final message of at most 6 bullets.
</deliverables>

<constraints>
- Ask the owner in AskUserQuestion calls, starting with the logo, skipping anything already in the facts:
  - who made each image (you / designer / logo maker / Canva / AI tool / other);
  - whether the source file exists;
  - for designer-made images, whether a written rights transfer exists.
- Confirm font origin and version from the Fontsource package page or upstream repository, citing the URL.
- Leave every asset in place. Prompt 22 decides on ownership risks.
</constraints>

<acceptance_criteria>
- The checker exits 0.
- A temporary copy of the repo with an extra public/assets/img/x.png makes asset-inventory fail.
</acceptance_criteria>

<if_uncertain>
Set Status to "origin unknown: owner action" for any asset the owner can't account for.
</if_uncertain>

<task>
Record the creator and licence of every font, image and icon in the repo in docs/asset-licenses.md, meeting any licence obligations that are unmet.
</task>
````

## Assumptions
- Prompt 00 has run.
- The owner knows where the logo came from, or can find out.

## Parameters
- Reasoning effort: medium.

## What to test
- Every file under `public/assets/img` and `public/assets/fonts` has a row.
- Compare at least one SVG path against Heroicons and Lucide sources, and check the recorded conclusion.
- A seeded extra image fails the checker.
