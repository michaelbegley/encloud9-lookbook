# Look 9 build kit (read fully before building)

Repo working copy: /home/claude/lb (GitHub Pages lookbook). Pages live in /home/claude/lb/pages/.
Shared files, DO NOT EDIT: pages/nine.css, pages/nine.js, pages/nine-home.html, pages/nine-dynamics-365-sales.html.
If you need a style that nine.css lacks, put it in ONE <style> block in your own page's <head>, prefixed with a page class (e.g. body.p-stories .x{}). Keep it small.

## Start every page from the template
Copy /home/claude/lb/pages/nine-dynamics-365-sales.html as your starting file. Keep exactly:
- the <head> pattern (fonts.css, nine.css, nine.js defer, noindex), title and meta set for your page
- the lookbook bar (#lbbar) with the font buttons; change which link has class="on" (none of Home/Sales page if your page is neither; you may add your page's name as plain text in the .t span)
- the header and footer: after writing your page, run
  `python3 /home/claude/dec/n9kit/chrome.py pages/YOURPAGE.html SECTION`
  SECTION = d365 | marketing | copilot | packages | stories | about. This rewrites header and footer to the shared version and marks the current nav item.
- the final dark band (section.final with .inner, footer, and the 9-colour .scale strip)
- JSON-LD: BreadcrumbList matching the visible crumb; FAQPage only if the page has an FAQ, word for word.

## Components available in nine.css (see nine-home.html and nine-dynamics-365-sales.html for markup)
- .crumb breadcrumb (Home / Section / Page). Hubs: Home / Hub.
- .hero two columns (.copy left with .mono eyebrow, .h1 with .ln>span lines that animate, .lead, .acts buttons, .phone-note). Right column: a signature visual. Use the 3x3 cube grid idea (Brian loves "the cubes", the grid and its bounce): .grid9 with 9 .cell (dark to light blues, var(--b1)..var(--b9), .cell.lt for light ones with dark text, .cell.core for the outlined centre), or .lic 3 cells, or a .mock window. Each page should have its own take on the cubes, not a copy of home's.
- .proof 4-cell fact row (.pf, a.pf with <small> link line)
- .sec sections with .sec-head (h2.h2 + p.lead)
- .rows of a.row (glyph .g with 9 <i>, .nm, .ds, .go)
- .band dark section with .ai-top, .aigrid (9 .aic, one .on), .three blocks, .band-foot, .tbl.dark
- .gp + .mock (browser-window mock with .mock-bar, .mock-body, .kpi, .mock-wide, .mock-line, .badge .r/.g). Label any mock "Example data" in a .mock-cap figcaption; use Microsoft sample names (Contoso, Fabrikam, Northwind, Litware) only.
- .jobs (4 .job cards with .bar colour strip), .stages (4 .stg with .g glyph using style="--k:n"), .tbl table in .tbl-wrap, .plans-grid, .stories (.story cards; .stories.two), .posts, .fit (.yes/.no lists), .cards/.card (.facts), .check/.qbox readiness widget, .faq details/summary, .fine small print
- Motion: add class "rev" to blocks that should reveal on scroll; .rise with style="--d:n" in the hero. Everything is gated by prefers-reduced-motion in nine.css already.

## Hard content rules (Brian's decisions and house rules)
1. Never invent a fact, URL, price, number, date, client or quote. Use only the copy file you are given and facts in it. Where a value is missing, keep the bracket exactly, e.g. [Brian sets].
2. NO package prices anywhere (Brian, 4 Nov: package rows show scope and time, not price). Replace any package price line with "Quoted in writing after a short call" or drop the Price row. Support plan prices STAY (On-Demand $200 an hour; Stability $500 a month, 4 hours, minimum plan; Optimization $1,500 a month, 20 hours, up to 50 users; Partnership $2,000 a month, 35 hours, 50 users and up). Microsoft list prices stay.
3. The words "Business Central" must not appear on any page (including story product lists). No orange. No cloud images or cloud puns. No em dashes or en dashes anywhere (use commas, colons, "to").
4. Say "Free checkups, no obligation" (not "free checks"). Say "23 client stories" (never "written up"). Do not use "two thirds of projects come from returning clients". No "Solutions Partner" claim. Partner line: "Microsoft partner since [2008], specializing in Dynamics 365".
5. Cut filler captions. Every heading says a plain thing a buyer asks. Prefer question H2s where the copy file has them.
6. Links: only URLs that appear in your copy file, SITE-STRUCTURE.md, or these concept pages: nine-home.html, nine-dynamics-365.html, nine-dynamics-365-sales.html, nine-customer-service.html, nine-marketing.html, nine-copilot.html, nine-packages.html, nine-stories.html, nine-about.html. Booking: https://www.encloud9.com/lp/schedule-a-meeting/ . Phone tel:+18442640729 shown as 1-844-264-0729. Support plans: https://www.dynamics365support.com/#plans . Readiness check: nine-dynamics-365-sales.html#check .
7. "Click (formerly ClickDimensions)" is how we name Click the first time on a page; "Click" after that.

## Quality bar
Michael: "a nice looking standout website, way better than anything we had before. Be creative and exciting." Be bold within the look: big confident type, the blue scale, the cubes, generous space, one signature interactive or animated moment per page (built in plain JS inside the page, gated by prefers-reduced-motion, no loops, no libraries). Never cram.

## Checks you must run before reporting
1. `node /tmp/claude-0/-home-claude/560b35a6-e00c-5990-89dc-05dfaaa63f19/scratchpad/shot.js` is for the two old pages; instead write your own small Playwright check (require('playwright'), chromium.launch()) that loads file:///home/claude/lb/pages/YOURPAGE.html at widths 1440, 390 and 360, scrolls through with behavior:'instant', waits, and prints document.documentElement.scrollWidth (must equal the width) and any page errors (must be none). Save full-page screenshots at 1440 and 390 to /home/claude/dec/shots/ and LOOK at them (Read the image, cropped into parts), fix anything ugly or broken.
2. grep your page for: Business Central, written up, em dash (U+2014), en dash (U+2013), "free check" (lowercase without "up"), "$[" in package rows. Zero hits (except brackets you were told to keep).
3. Every href="#x" has a matching id; every relative link points to a file that exists or to one of the nine concept page names listed in rule 6.

## Copy voice (Brian's decision, Teams, 6 Nov 2026 00:31 Central)
"set up is very passive" / "we build" / "strong words, just use that as a guide". enCloud9 builds; it does not "set up". Use strong, active verbs for what we do (build, fix, move, run, support). "Set up" stays only for describing a configured thing (users and security roles set up).
