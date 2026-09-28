# Prompt 13: Add alt text to images

Phase 5. Paste everything below the line into a new Claude Code session opened at the
repository root.

---

You're working in the Tech-Savvies website repo (static site in `public/`, hosted on Netlify).
Read `fix-plan.md` §2 and §4, then `docs/compliance-log.md`.

## Goal

Every image and icon on every page, including the legal pages added by Phases 3–4, should have
the right text alternative: meaningful images described, decorative ones hidden, and linked
images named by where they go. Keep it that way with a stronger check and a short guide.

## Why

Missing or poor alt text fails WCAG 1.1.1 and is one of the most common claims in website
accessibility lawsuits, which are frequent in NY. The initial audit found the site in good
shape:
- The only `<img>` is the logo, used twice per page (header and footer). Both have
  `alt="Tech-Savvies NYC home"`, which is correct for a linked logo because it says where the
  link goes and includes the visible logo text.
- All inline `<svg>` icons have `aria-hidden="true"`, and each sits next to visible text or
  visually-hidden text ("Menu", "(opens in a new tab)").
- The checklist ticks are CSS background images. They're decorative, and the list text carries
  the meaning.
- `og:image:alt` is set on every page.

So this prompt is mostly verification and prevention. New pages or images may have been added
since the audit, though, so re-check everything.

## Task

1. **Audit** every HTML file in `public/`:
   - every `<img>`, `<svg>`, `<picture>`, `<input type="image">`, `role="img"`, and CSS
     `background-image` that carries content;
   - for each: is it meaningful, decorative, or a link or button? Is the current alternative
     right? Use the W3C alt decision tree: `WebFetch`
     https://www.w3.org/WAI/tutorials/images/decision-tree/.
   - Record the results in a table in `docs/accessibility-audit.md` (create it; Prompt 21 extends
     it).

2. **Fix** anything wrong. Expected: nothing, unless later prompts added images.
   - Meaningful: describe the content or function concisely, with no "image of".
   - Decorative `<img>`: `alt=""`. Decorative `<svg>`: `aria-hidden="true"` and
     `focusable="false"`.
   - A linked image that's the link's only content gets alt text describing the destination.
   - Check that `og:image:alt` exists on every page, including new ones. Add
     `<meta name="twitter:image:alt">` with the same text for completeness.

3. **Strengthen the `img-alt` check** in `tools/check_site.py`:
   - fail if `alt` is a filename (`\.(png|jpe?g|svg|webp|gif)$`), or is "image", "photo",
     "picture", "logo" or "icon" on its own;
   - fail if an inline `<svg>` has neither `aria-hidden="true"` nor (`role="img"` and an
     accessible name via `aria-label` or `<title>`);
   - fail if a page lacks `og:image:alt`.

4. **Guide.** Add "Images and alt text" to the README "Editing" section: 4–5 rules with one
   example each, plus a link to the decision tree.

5. Update item 13 in `docs/compliance-log.md`.

## Verify

- `python3 tools/check_site.py` passes. In a temp copy, `alt="logo.png"` and an un-hidden `<svg>`
  both fail.
- Run axe-core's `image-alt`, `svg-img-alt` and `role-img-alt` rules on every page with
  Playwright. Install `axe-core` in your scratchpad (`npm i axe-core` there, not in the repo) and
  inject it with `page.addScriptTag({ path })`.

## Commit

`Fix #13: verify image text alternatives and tighten alt-text checks`. Push to the current
branch.
