# Review: Full implementation page, Draft 1 to Draft 2 (9 Nov 2026)

Page: pages/nine-full-implementation.html (Look 9 concept). Copy source: project doc claude/site-build/PAGE-FULL-IMPLEMENTATION.md.
Frozen Draft 1: pages/draft1/nine-full-implementation-D1.html, sha256 d631edb6... (unchanged through review).

## Scores
- Draft 1: 22/32, independent reviewer. Failed (bar 28).
- Draft 2: 30/32, Claude's re-score on the same rubric (not independent).

## Fixed in Draft 2
1. Layout bug: a stray closing div ended the page container after the hero, so every later section ran to the screen edge. Removed; sections now sit at 20 px (390) and 72 px (1440), same as the Sales page (measured).
2. FAQPage JSON-LD added: 8 of 9 questions word for word; the time question is left out while it holds a [Brian sets] bracket.
3. Integrations contradiction: the data FAQ said integrations are "quoted separately" while Included lists them. Now: integrations you name are part of the written scope and its fixed price per phase.
4. Final band no longer promises "a price" from a free call (the page sells a paid Fit Check): "You get a straight answer on which package fits, whether or not you work with us."
5. Story facts tightened to the sources (fact check): KBG "for a business that ran on QuickBooks alone"; Tension Packaging "for a division whose pipeline lived in Excel" (the story is an expansion, not a first system); section lead "each a Dynamics 365 Sales build".
6. One placeholder style for time: "[Brian sets] to [Brian sets] months" in the hero and the FAQ; On-Demand bracket now "[Brian sets: ...]".
7. Voice: "As part of setup" became "As part of the build".
8. Contrast: the Licenses cube (step 6) now uses dark text (5.3:1).
9. Centre cube reads "Full implementation" on phones without a hyphen break.
10. "Go live" cube matches Stage C: Copilot on, agents only where data is ready.
11. Removed "brand: Microsoft" from the Service schema.
12. US spelling: license, licenses (Michael, 9 Nov: "we are in the US").

## Not changed, and why
- Proof does not show an integration project: no published story states integrations (spec 2.4). Needs a story from Brian.
- Support plans tile in "Other packages" repeats the support section: kept as the route to dynamics365support.com.

## Checks
- Confirmed against Microsoft (fact check): five Success by Design phases, "does not guarantee outcomes", license plus security role, Sales list prices $65/$105/$150.
- Could not determine (support site blocked to the agent): support plan prices; they are word for word from the spec (round 8 wording).
- No sideways scroll at 1440, 390, 360; 0 page or console errors; 0 bad anchors; 1 H1; 0 dashes, 0 "Business Central", 0 package prices.

## Still open for Brian
Time range; Fit Check price and credit rule; On-Demand eligibility; naming KBG and Tension Packaging; "The quote is yours to keep"; the four stage names.

## Process note
The review agents could not read project docs (no Projects tool in agent sessions). For the next pages, the copy spec is saved to disk before review.
Other Look 9 pages still use British "licences": nine-blog-post, nine-copilot, nine-customer-service, nine-dynamics-365-sales, nine-dynamics-365, nine-packages.
