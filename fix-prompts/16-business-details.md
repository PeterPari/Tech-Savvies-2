# Prompt 16: Add real business details

````text
<context>
The only business detail on the site is info@tech-savvies.com. Four problems follow from that:
- The Terms and Privacy Policy must name the contracting party and the data controller.
- CAN-SPAM requires a postal address in commercial email (Prompt 18).
- Trading as "Tech-Savvies" rather than the owner's legal name may need a NY assumed-name filing (see docs/legal-compliance.md).
- /contact/ promises replies "during NYC business hours" (public/contact/index.html:59) without defining the hours.

The current JSON-LD (public/index.html:28-40) is an Organization with name, url, logo, email, foundingDate, founder and description, and no location. The footer copyright line reads "© <span data-year>2026</span> Tech-Savvies. All rights reserved." on every page.
</context>

<inputs>
docs/business-facts.md, docs/legal-compliance.md, docs/compliance-log.md
</inputs>

<deliverables>
1. The /contact/ .contact-info block, below the email, using the existing .contact-label and body text styles:
   - business name;
   - "Based in New York, NY" and the service area;
   - hours with time zone;
   - the mailing address inside an <address> element.
   The block reflows cleanly beside the form at 768px and 1280px.
2. Every page's footer:
   - "New York, NY" under the email in the Contact column;
   - the copyright line reads "© <span data-year>2026</span> <legal name>. All rights reserved."
3. If the legal name differs from "Tech-Savvies", one sentence on /our-story/: "Tech-Savvies is the trading name of <legal name>."
4. JSON-LD in public/index.html:
   - @type ProfessionalService, keeping the existing properties;
   - legalName and areaServed;
   - address as a PostalAddress containing only the parts the owner approved (at minimum addressLocality "New York", addressRegion "NY", addressCountry "US");
   - openingHoursSpecification if hours are confirmed;
   - sameAs only with owner-provided, active profile URLs.
5. A check named business-details in tools/check_site.py: every footer contains a LEGAL_NAME constant, and the JSON-LD legalName equals it.
6. An "Editing → Business details" bullet in the README, listing every place these details appear.
7. Item 16 updated in docs/compliance-log.md, including the DBA filing as an owner action if it's still needed.
8. One commit, "Fix #16: show legal name, location, hours and mailing address", pushed.
9. A final message of at most 6 bullets.
</deliverables>

<examples>
<example index="1">Business: Jane Doe Web Services LLC (doing business as Tech-Savvies)</example>
<example index="2">Business: Tech-Savvies · Based in New York, NY · Serving New York City and remote clients</example>
<example index="3">Hours: Monday–Friday, 9am–5pm ET · Mail: PO Box 123, New York, NY 10001</example>
</examples>

<constraints>
- Publish only values confirmed in docs/business-facts.md.
- If the owner offers a home address, recommend a PO box or virtual mailbox and use whichever they confirm. If they decline to publish any address, show "New York, NY" only, and note in the compliance log that commercial email still needs a postal address.
- Leave out a phone number unless the owner asks for one to be published. Leave out telephone, priceRange, aggregateRating and review in the JSON-LD.
- Use no map embed. It would add a third-party iframe that the CSP blocks.
</constraints>

<acceptance_criteria>
- The checker exits 0, and the JSON-LD parses with python3 -m json.tool.
- /contact/ and a footer render without overflow at 375px, 768px and 1280px.
</acceptance_criteria>

<if_uncertain>
Omit any detail the owner hasn't confirmed, and list it in the final message.
</if_uncertain>

<task>
Add Tech-Savvies' confirmed legal name, location, service area, hours and mailing address to the contact page, every footer, and the JSON-LD.
</task>
````

## Assumptions
- Prompts 00 and 24 have run.
- The owner decides whether to publish an address.

## Parameters
- Reasoning effort: medium.

## What to test
- Run with the address set to `TODO(owner)`. The session should ask, and publish nothing until answered.
- Run with a home address offered. It should recommend a PO box.
- The JSON-LD validates with the schema.org validator.
