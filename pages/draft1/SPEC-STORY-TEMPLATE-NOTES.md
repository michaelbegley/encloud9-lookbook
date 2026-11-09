# Client story template (T5), first instance Hogan Assessments: sources and choices (9 Nov 2026)

Template spec (SITE-STRUCTURE.md T5): breadcrumb Home > Client stories > story; H1 with the client name; key-facts strip (industry, state, products, timeline, work type); stat tiles in plain HTML, only real numbers, else time or scope facts; Key outcomes list; Challenge, Solution, Results as question H2s; client quote only if one exists and is approved (none exists today); "Packages used" cells linking to product and package pages; next and previous story; CTA band. 23 stories at /blog/success_stories/{slug}/, addresses kept.

Facts used, all from the live Hogan story (WebFetch 9 Nov 2026) and FACTCHECK-SALES.md row 23 (4 Nov 2026):
- Title on the live page: "Hogan's CRM Rescue Story: A Fresh Start with Dynamics 365". Published May 28, 2025, by Kristin Caniglia.
- Hogan Assessments, Tulsa, OK. Global provider of personality assessments for talent acquisition and development, plus certifications and professional training. Company size not stated.
- Products listed: Microsoft Dynamics 365 Sales Hub; HubSpot integration. Services listed: implementation, sales team training, mailbox configuration.
- Challenge: so heavily customized it became "virtually unusable"; reps avoided it; management lacked pipeline visibility.
- Solution: removed unnecessary customizations; out-of-the-box Sales Hub; standard lead-to-opportunity process.
- Results: "Within just three months" a clean, simplified system; "The project finished on time and under budget"; activities and follow-ups trackable; pipeline visibility.
- Next: Hogan plans to implement Sales Sequences.
- No quote from Hogan staff in the story.

Choices (Claude, Draft 1):
1. Copy rewritten in our voice from the facts above; the long article body is not carried over word for word. Whether to keep the full original article text below the template is open (it is the indexed content today).
2. Stat tiles: "3 months", "On time" (and under budget), "Standard" (Sales Hub). No invented metrics.
3. A visible line "No client quote is published for this story yet." so the quote slot shows; Brian may prefer to hide it.
4. Previous and next: Milestone Leasing and PriceMDs (World Import Distributors, the next card on the hub, is a Business Central story and is skipped).
5. Page title "Hogan Assessments: Dynamics 365 Rescue | enCloud9" (49 characters); H1 "Hogan Assessments: a usable CRM again in three months".
6. "Mailbox setup" in key facts paraphrases "mailbox configuration"; the HubSpot integration is listed as the story lists it, with no claim about who built it.
7. JSON-LD: BreadcrumbList and Article (author, datePublished). No dateModified until content is approved.

## Story data sheet (Draft 2): what every story fills in
Required: file/slug (keep the live /blog/success_stories/{slug}/ address), client, work_type (hub wording: New build, Rescue or fix, Upgrade, Integration, Add-on, Support), title (60 characters or fewer), meta (120 to 160), h1 (2 short lines), answer (40 to 60 words, who, what was wrong, what we did, result), facts (Client, Location, Industry, Starting point, Products, Services: in the story's own words), outcomes (2 to 5, each traceable to the story), chapters (What was wrong, What did we change, What changed day to day), author, published date, prev and next.
Optional, and the block disappears when empty: timeline (adds a Timeline row), tiles (0 to 3, real numbers or plain facts only; the grid sizes itself to 1, 2 or 3), quote (text, name, title; only when approved in writing), next_steps (an extra chapter), packages (0 to 3 related links; a package is labeled "Package for work like this", never as something the client bought).
Rules: every fact traces to the published story; no "again", "back to" or causes the story does not state; no Business Central stories (World Import Distributors waits on Brian).
Instances built: Hogan Assessments (timeline, 3 tiles, next steps), Milestone Leasing (no timeline, 2 tiles, no next steps).
