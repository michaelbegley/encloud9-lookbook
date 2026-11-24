# Check 3 prep, 24 Nov 2026 (report; nothing changed on staging)

Written about 2:50 AM Central, #17, from the Compass blocks of 2:11 and 2:14 AM. Every page read was on screen in Michael's Chrome; no scripts.

## 1. The "You get a straight answer on ..." lines
Measured in the site sources (build input): 68 lines on 66 pages. 65 are in the closing call box on 63 pages; 3 are FAQ answers to "What happens on the (first) call?" and are left as they are (they answer a question).

Proposal (Michael's yes needed): drop the repeated phrase "You get a straight answer on", keep the promise.

| # | Before (call box) | After | Pages |
|---|---|---|---|
| 1 | Tell us where your system is today. You get a straight answer on which package fits. | Tell us where your system is today, and we tell you which package fits. | 36 |
| 2 | Tell us where your system is today. You get a straight answer on what it would take. | Tell us where your system is today, and we tell you what it would take. | 23 |
| 3 | Tell us where your system is today. You get a straight answer on where to start. | Tell us where your system is today, and we tell you where to start. | 2 (Power Apps, Power BI) |
| 4 | Tell us where your system is today. You get a straight answer on which package fits and what it costs. | Tell us where your system is today, and we tell you which package fits and what it costs. | 1 (Home) |
| 5 | Tell us where your system is today. You get a straight answer on which plan fits. | Tell us where your system is today, and we tell you which plan fits. | 1 (Support Plans) |
| 6 | Tell us where your system is today. You get a straight answer on which tool fits. | Tell us where your system is today, and we tell you which tool fits. | 1 (Power Platform) |
| 7 | Something else on your mind? Ask us on a call. You get a straight answer on what your data is ready for and what it costs to run. | Something else on your mind? Ask us on a call, and we tell you what your data is ready for and what it costs to run. | 1 (Copilot and AI) |
Left as is (FAQ answers): Contact us and FAQ ("... You get a straight answer on what fits."), Book a Call ("You tell Brian ... You get a straight answer on what fits."), plus the same three in their FAQ search data.
Total changed on yes: 65 lines on 63 pages, plus each page's built copy.

## 2. Health Check duration
On screen, /crm-health-check/ (24 Nov, about 2:15 AM): hero "Up to one hour, no obligation."; booking line "The session takes up to one hour."; FAQ "One to two hours of free consulting time".
Both "up to one hour" lines describe the Health Check itself. Brian's 17 Nov audio (Brian list v7, Q5, closed): "I wouldn't say up to an hour ... I would say a one to two hour free consulting time".
Cause found: the same two lines were fixed on staging on 18 Nov ("One to two hours, free." and "The session takes one to two hours."), but the repo commit was refused and not retried (roadmap log, 19 Nov), so later uploads from the repo put "up to one hour" back.
Proposed fix: hero "One to two hours, no obligation."; booking line "The session takes one to two hours." Edited in the source this time.

## 3. Owed rows
- Row 56, Packages headline, three options for Brian: (a) "Ready-Made Dynamics 365 Packages, Tailored to Your Business" (Claude's pick: his words, keeps "Dynamics 365 Packages" for search); (b) "Dynamics 365 Packages, Ready-Made and Tailored to You"; (c) "Dynamics 365 Packages That Start Ready-Made and Fit Your Business". Today: "Dynamics 365, in Packages You Can Read Before You Buy".
- Row 55, Rescue and Repair name: partial. Ahrefs free keyword tool, US, on screen: "crm optimization" over 100 a month; "dynamics 365 optimization", "crm rescue", "dynamics crm rescue", "dynamics 365 crm rescue" under 100 each. The free tool gives buckets only, and after three searches it asked for a human check, which Claude does not get around. Could not check: exact volumes, "dynamics 365 rescue", "crm health check", "crm cleanup", or Google Search Console queries (no connector; needs Michael's sign-in on screen). Ahrefs in this session: no connector loaded.
- Row 26, Microsoft Sales prices: matched on microsoft.com Sales pricing, on screen: $65.00, $105.00, $150.00 user/month, paid yearly.

## 4. Tracker (revision 33)
Pages: "Covered desktop" (D), new "Covered phone" (E), "Brian OK" (F) all empty; the 22 Nov ticks kept in J. Start here counts all three. Changes row 12 (Bookings) Done. Questions: column H maps rows to Brian's 43 numbers; rows 72 to 80 add his Q1, Q25, Q37, Q43 and Brian list 42 to 46; rows 26, 60, 61 marked Answered; row 55 has the partial check. Rows 30, 31, 32, 33, 41, 43, 44, 56 are NOT closed yet (on Michael's tap card).

## 5. Read sheet
claude/site-build/CHECK3-READ-SHEET.md, rewritten 24 Nov (project doc, replaces the 18 to 19 Nov one).

## 6. Pre-flight, desktop (on screen)
16 pages in the running order: all load styled (header, fonts, layout; the hero animates in and settles within about 3 seconds).
Visible placeholders: 24 on 5 pages. Service Accelerator 2, About 7, Team 11, Brian Begley 3, CRM Health Check 1. Zero on Home, Packages, Contact, Book a Call, Implementation, Sales Accelerator, Rescue and Repair, Compana (text read line by line), and on Support Plans, Dynamics 365 Sales, Customer Service (checked by an on-page search only).
Also seen: About shows a counter reading "0 of 9" in the page text (likely a count-up that runs on scroll; not checked further).
Phone view: NOT done. Chrome's phone view lives in DevTools, which the Chrome extension cannot open (F12 and Ctrl + Shift + M went to the page, measured 24 Nov). A narrowed window does not count (Compass). So the 390-wide look is Michael's, in the meeting or before it, with the steps on the read sheet.

## 7. The four move-page download forms
On staging, each move page (Salesforce, HubSpot, Zoho, monday.com) shows: "[Form: the existing checklist download form (first name, last name, work email, consent). Michael supplies the checklist file and the form before this page goes live.]"
What each needs:
1. The checklist itself, approved: Draft 1 of all four is in the repo (wp-theme-fable/checklists/, 23 Nov), waiting on Michael and Brian.
2. A file to hand over (a PDF of each approved checklist).
3. The form: the same "guide" form the other guide pages use (first name, last name, work email, consent), posting to the ClickDimensions capture "24 - Download our Free Guide", with the checklist's name sent as the topic so the lead says which checklist.
4. The hand-over after submit: the guide form goes to /thank-you/. How that page hands over a particular file: could not determine in this pass; checked before the build.
Proposal: build all four the way the other five forms were built (the plugin's own form, no new plugin), once the checklists are approved; one test submit per form, test leads on the delete-before-launch list.
