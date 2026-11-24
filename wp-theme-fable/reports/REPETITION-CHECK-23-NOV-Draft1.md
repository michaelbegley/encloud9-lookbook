# Repetition check (Changes row 33), report only, Draft 1

Mon 23 Nov 2026, about 9:00 PM Central. Claude, #17 Facilitator. Nothing changed on the site. Source: michaelbegley/encloud9-lookbook, branch wp-theme-fable, commit 7b009b9, content/pages.json (107 pages), read by script (page text with tags stripped). Counts are measured on that file; staging was not opened.

## 1. Prices kept in one place
Every package price is typed into each page that shows it. No page pulls from one shared list. Pages carrying each price (measured):

| Price | Pages |
|---|---|
| Support from $500 a month | 39 |
| Full implementation from $20,000 | 35 |
| Rescue and Repair $500 to $10,000 | 29 |
| Sales or Service Accelerator $7,500 | 24 |
| On-Demand $200 an hour | 21 |
| Partnership $2,000 a month | 21 |
| Optimization $1,500 a month | 18 |
| Marketing Accelerator $5,000 | 4 |

- No page shows a different amount for the same package (measured for the eight prices above).
- The wording around the same price varies: "From $20,000", "From $20,000, quoted in writing", "starts at $20,000", "From $20,000 · quoted" (client stories).
- Microsoft list prices ($65, $105, $150 for Sales; $50, $105, $195 for Customer Service, and others) sit on up to 18 pages each.
- Risk: one price change means editing up to 39 pages by hand, and a missed page shows an old price.
- Proposed fix (Claude's call, needs Michael's yes): one price list in the plugin that every page reads, so a price is changed once. Build after Brian answers the open price questions, since several of them would change these numbers.

## 2. Moves: two different price lines
- Packages page, move tiles: "Quoted in writing after a short call".
- Move pages (Salesforce, HubSpot, Zoho, monday.com) and others: "From $20,000".
- Already on Brian's list (question 11 in the 43-question version Michael sent; 10 in Draft 1A). No change until he answers.

## 3. "Six steps" against four stages
- /lp/dynamics-365-consulting/ says: "How does enCloud9 run a Dynamics 365 project? In six steps, from the first assessment to support after go-live." Its list numbers 01 to 06.
- Every other page that says how a project runs (15 pages, measured) says four stages: Plan, Build, Go live and Run. The FAQ and the Implementation page also map these to Microsoft's five Success by Design phases.
- Proposed fix (Claude's call): rewrite the landing page's section to the four stages, using the same lines as the Implementation page. Not a price or a promise, so it does not need Brian; it needs Michael's yes.

## 4. FAQ page copies
- The FAQ page repeats answers and prices from the package and service pages, on purpose: search engines and AI answers read it.
- Since a2643c3, verify fails a build when an FAQ copy differs from its page's answer, or when the FAQ search data differs from the visible answer. #16 reported verify FAIL 0 at 7b009b9 (not re-run here: the plugin's data files are built at zip time and are not in the repo).
- Nothing to change now. If the one price list in item 1 is built, the FAQ reads from it too.

## 5. Repeated lines
- "Microsoft licenses are not part of the package price." under the price box: cut on Implementation, Sales Accelerator, Service Accelerator and Rescue in #16 (export, 23 Nov afternoon). Not re-counted here.
- The 71 "You get a straight answer on ..." call-box lines: row 32, on hold until Michael says go (Compass).

## What needs a yes
1. Michael: the one price list (item 1), to build after Brian's price answers.
2. Michael: the consulting landing page rewritten to four stages (item 3).
