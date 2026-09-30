# Testimonials and endorsements policy

Rules for any review, rating, quote, testimonial or case study on the site, and the scan that
shows what is there today. Sources: FTC Rule on Consumer Reviews and Testimonials (16 CFR 465) and
FTC Endorsement Guides (16 CFR 255). NY GBL §349 (deceptive acts) also applies. This is not legal
advice; the owner should ask an attorney about anything unclear.

## Scan of `public/` (2026-09-29)

| Looked for | Result |
|------------|--------|
| Quotes (`<blockquote>`, quotation-marked customer text) | None |
| Testimonials, reviews, “clients say”, “customers say”, “trusted by” | None. `/solutions/` names “testimonials” only as a feature a Tier 3 site can include; it claims none of its own |
| Ratings, stars, ★ or ⭐ characters | None |
| Client logos | None. The only logo is Tech-Savvies’ own |
| Client counts (“50+ clients”) | None |
| Review schema (`aggregateRating`, `"@type": "Review"`) | None. The `no-review-schema` check reads every JSON-LD block, including nested objects and arrays; a temporary copy with both nested in a `LocalBusiness` block made it fail |
| Case studies | Two: Grisha.studio (Featured Showcase on `/` and on `/showcases/`) and Eldunary (`/showcases/`) |

## Case study: Grisha.studio

Owner answers, 2026-09-29 (also in [`business-facts.md`](business-facts.md)): real engagement, all
facts accurate; written permission to name the client, link to the site and show its screenshot;
the client, Gregory Parizhsky, is the owner’s brother, and the work was at a reduced rate.

The disclosure “(the founder’s brother; our first project, at a reduced rate)” sits in the same
`.meta` line as the client name, so it is visible without a click (16 CFR 255.0(f): “unavoidable”).
The case study is not a customer quote, and no ratings or quotes are attached to it.

Owner actions: keep the written permission outside the repo (see rule 2); the owner asked for the
connection to stay off the home page, but the disclosure must stay wherever the case study
appears. If it is removed from the home page, the case study has to move with it. Do not ask a
relative for a Google review (rule 4).

## Case study: Eldunary

Owner answers, 2026-09-29 (also in [`business-facts.md`](business-facts.md), Case study (Eldunary)):
real engagement described in the owner’s own words; the client reached out, the site is around 100
pages, and the work continues. The client gave written permission to name the site, link to it and
show its screenshot. No family or other connection and no discount to disclose. No quotes or
ratings are attached to it.

Owner action: keep the written permission outside the repo (see rule 2).

## Rules for future endorsements

1. **Real customers only, quoted verbatim.** Show only words from a real customer who bought the
   service, unedited (cut only with an ellipsis that doesn’t change the meaning). Never attribute a
   quote to someone who did not write it, or to a person who does not exist.
   16 CFR 465 (fake or false consumer reviews and testimonials):
   https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465
   FTC Endorsement Guides, endorsements must reflect the honest opinions of the endorser (16 CFR 255.1):
   https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255
2. **Written permission, stored outside the repo.** Get the customer’s written permission to use
   their name, quote, logo or site screenshot before publishing. Keep the message in the owner’s
   email or files, never in the repo. Portfolio use also needs the client’s written permission
   ([`business-facts.md`](business-facts.md)). 16 CFR 255.1 (endorsements must be
   authorised and the advertiser is responsible for them):
   https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255
3. **A date on every quote.** Show when the customer said it, and remove it when it no longer holds.
   Give the quote’s source in a `data-source` attribute (see the check below).
   16 CFR 255.1 (an endorsement must not be misleading):
   https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255
4. **Disclose incentives and relationships.** Family, friends, employees, free or discounted work,
   discounts, gifts or payment for the endorsement are disclosed next to the endorsement, in
   plain words, without a click. Never solicit reviews from immediate relatives (spouse, parent,
   child, sibling) or from staff about the business. 16 CFR 255.5 and 255.0(f); 16 CFR 465
   (insider reviews, immediate relatives): https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255 and
   https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465
5. **No written, bought or AI-generated reviews.** Don’t write reviews yourself, have anyone write
   one for a non-customer, buy or trade for reviews or ratings, or generate one with AI.
   16 CFR 465 (fake reviews, including AI-generated, and buying reviews):
   https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465
6. **No suppression of negative reviews.** If reviews are shown, don’t hide, delete or threaten
   customers over honest negative reviews, and don’t pick only the positive ones from a
   collection presented as representative. 16 CFR 465 (review suppression):
   https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465
7. **Rating schema only for genuine reviews shown on the page.** Add `aggregateRating` or `Review`
   markup only for real reviews visible on that page, matching what is shown. Until then,
   `no-review-schema` fails the build on any of it. 16 CFR 465 (misrepresenting reviews):
   https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465

## Guard: `tools/check_site.py`

- `testimonial-source`: any `<blockquote>`, or any element whose class contains “testimonial” or
  “review”, must have a non-empty `data-source` attribute (where the words came from and the date).
- `no-review-schema`: fails on `aggregateRating` or `"@type": "Review"` at any depth in JSON-LD.
