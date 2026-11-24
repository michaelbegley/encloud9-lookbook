# Brian's 43 questions: what changes on the site for each answer

Tue 24 Nov 2026, about 12:40 AM Central. Claude, #17 Facilitator, at the Compass's ask (relayed by Michael, 24 Nov, 12:07 AM). Nothing here is applied. Staging is unchanged (plugin 0.5.74).

**Purpose:** when Brian replies, each answer turns into a change list in minutes. Find his number, read the row, apply the "after" that matches his answer, rebuild, verify, upload.

**Numbering:** this follows the 43-question version Michael sent on 23 Nov (about 8:55 PM). Question 1 is the launch date. Questions 2 to 43 are Draft1A's questions 1 to 42, each moved down by one. The exact wording of question 1 as sent: could not determine (it is in the Compass's version, not in any file here). It is taken as "Does launch stay Wed 9 Dec, or move to Wed 16 Dec?" (the open proposal in HANDOFF-Facilitator-17).

**Where the lines were read:** the built page data, wp-theme-fable/content/pages.json at plugin 0.5.74 (commit a578393), measured 24 Nov. Page paths are the new-site addresses.

**How to apply a change (learned 23 Nov):** build.py rebuilds pages.json from the site HTML. So edit the source, never pages.json alone:
- site/<path>/index.html (the page as built);
- pages/nine-*.html (the template copy), when the page has one;
- stories-data/<client>.json, for a story page.

Then run build.py, copy pages.json into encloud9-site/data/, run tools/verify.py, bump the plugin version, zip, upload and import. Search all three sources for the exact old text before editing. A line that appears on many pages is listed with its count.

**Launch blockers:** a question marked **BLOCKER** clears at least one open placeholder in LAUNCH-BLOCKERS-23-NOV.md (64 open after the 23 Nov recount). Do those first. The blocker counts by question are Claude's mapping of that report's lines to the 43 numbers. Where a mapping is a guess, it says "inferred".

## Order to work his reply
1. BLOCKERS first: 1, 2, 3, 4, 5, 7, 9, 16, 30, 32, 35, 38 and 42. Also 29, which is not a placeholder but fixes a page that contradicts itself.
2. Then the wording, price and menu questions: 6, 8, 10 to 15, 17 to 28, 31, 33, 34, 36, 37 and 41.
3. No site change: 39, 40 and 43. File them only.

---

## Launch date

### 1. Launch date: stays 9 Dec, or moves to 16 Dec? **BLOCKER** (clears 10 of Claude's launch-day placeholders)
- **Pages:** /blog/ ([publish date], [Showing count at launch], [count at launch], [author]); /how-microsoft-updates-dynamics-365/, /power-platform-dynamics-365/ (3 price captions), /blog/whats-new-in-dynamics-365-november-2026/ ([publish date]); /accessibility/ ([Date of last review.], [Date published.]); /privacy-policy/ and /terms-of-use/ ([Effective date.]).
- **Answer "9 Dec":** every date bracket becomes 9 December 2026, filled in on launch day. No change before then.
- **Answer "16 Dec":** the same, with 16 December 2026. Also move every dated step in the launch runbook and the site roadmap one week later: go or no-go Fri 4 Dec becomes Fri 11 Dec. Check Bing's 15 Dec date in the runbook against the new day.
- **Other answer:** use his date. Go or no-go is the Friday before.

## Privacy Policy

### 2. How long do we keep leads, form data and analytics? **BLOCKER** (1)
- **Page:** /privacy-policy/
- **Now:** "[Retention periods for leads, form data, analytics and chat transcripts, Brian and the lawyer decide.]"
- **Answer with periods** (for example "leads 3 years, analytics 14 months"): "We keep leads and form entries for [his period] after our last contact with you, and analytics data for [his period]. Chat transcripts: [his period, or the line is dropped if the chat assistant is not live]." The lawyer reads it before the DRAFT bar comes off.
- **Answer "ask the lawyer":** no change. The line stays a blocker under the lawyer.

### 3. State privacy rights: may Claude draft them? **BLOCKER** (1; the lawyer still reviews)
- **Page:** /privacy-policy/
- **Now:** "[State privacy rights that apply, including the Nebraska Data Privacy Act, and how to use them; lawyer.]"
- **Answer "yes, draft it":** Claude writes the section from the Nebraska Data Privacy Act and the states in our client stories. It lists the rights, how to make a request (privacy@encloud9.com) and our reply time. It is marked draft until the lawyer clears it. The bracket clears when the lawyer signs off, not when Claude drafts.
- **Answer "I'll write it":** no change until his text arrives.

## Team and About

### 4. Who is listed on the Team page? **BLOCKER** (1, plus 1 inferred)
- **Page:** /about-encloud9/team/
- **Now:** "[Brian confirms who is listed.]" Listed today: Brian Begley, Kristin Caniglia, Jodie Henry, Michael Begley.
- **Also (inferred):** "[One line, Brian confirms: what the team does and how it works with clients.]"
- **Answer with names:** remove the bracket. Add or remove a person card for each name (photo spot, name, title, two-line bio). Each new person approves their own bio (Brian's rule). The /about-encloud9/ people row mirrors the list.
- **Answer "as is":** remove the bracket only.

### 5. What is Jodie's title? **BLOCKER** (2)
- **Pages:** /about-encloud9/ ("Jodie Henry Consultant [role Brian confirms]"); /about-encloud9/team/ (the same, plus "[Title, matches LinkedIn; Brian and Michael set it]").
- **Answer with a title:** "Jodie Henry, [title]". Remove both brackets. It must match her LinkedIn (Brian's rule, 11 Nov).
- **Kristin, same rows:** her title is open and Michael's to name (Brian list item 45). Her "[role Brian confirms]" stays until Michael names it.

### 6. Team page line: "It depends on the project. An experienced enCloud9 consultant leads it..." OK?
- **Pages (4 places):** /about-encloud9/how-we-work/ ("Who works on our project?"); /about-encloud9/team/ ("Who will work on our project?"); /faq/ (both).
- **Now:** "It depends on the project. An experienced enCloud9 consultant leads it, and the same people stay with you from the plan through go-live and support."
- **Answer "OK":** no change. Mark it answered in the Brian list.
- **Answer with changes:** replace the sentence in all 4 places (site/ and pages/ copies of each). The /faq/ copies are checked by verify's FAQ copy-drift check, so all must match.

### 7. Can Claude draft the Meet Brian intro and bio from his LinkedIn? **BLOCKER** (2)
- **Page:** /about-encloud9/team/brian-begley/
- **Now:** "[Two lines, Brian confirms: his background, what he works on today, and why he started enCloud9.]" and "[Bio, Brian writes or approves: background, how enCloud9 started, the kind of clients he works with.]"
- **Answer "yes":** Claude drafts both from his LinkedIn and the facts doc: Founder and CEO, founded 2008, a CPA, chairs the Nebraska CRM user group since 2012. Brian reads the draft before it goes on staging. The brackets clear on his yes to the text.
- **Answer "I'll write it":** no change until his text arrives.

### 8. Book a Call: does every first call go to him?
- **Page:** /lp/schedule-a-meeting/. Now: the booking button opens Brian's Microsoft Bookings page ("Book an hour with Brian Begley"). The FAQ says "You tell Brian..." and the page reads "Meet Brian on Teams" and "Meet Brian Begley →".
- **Answer "yes":** no change.
- **Answer "no, it depends" or someone else:** change "Pick a day and time on Brian's Microsoft Bookings page" to "Pick a day and time on our booking page". Change "Meet Brian on Teams" to "Meet an enCloud9 consultant on Teams". Change "You tell Brian" to "You tell us". Swap in the shared Bookings link (Michael gives it; never guessed). Then check /contact-us/ and the call prep pages for the same names.

### 9. The 21 placeholder answers in the attached file. **BLOCKER** (inferred: most of the Team, About and Privacy lines above)
- **Source:** PLACEHOLDER-ANSWERS-TEAM-ABOUT-PRIVACY-19-NOV.md, the file Michael attached. It is not in the project list today; look in the blue-stratus-clients or blue-stratus backups before applying.
- **For each yes:** apply that row's proposed text to its page and remove the bracket.
- **For each no:** leave the bracket and add the row to the Brian list with his note.
- Count the cleared lines with `verify.py --launch` before and after.

## Packages

### 10. Sales Accelerator becomes "Quick Start": exact name? Do Service and Marketing get new names?
- **Scale:** "Sales Accelerator" appears 76 times on 20 pages. "Service Accelerator" appears 82 times on 28 pages. "Marketing Accelerator" appears 6 times on 4 pages. The page address /dynamics-365-sales-accelerator/ also carries the name.
- **Answer "Quick Start" for Sales only:** replace "Sales Accelerator" with his exact name in every source. Do not touch the 11 lowercase "sales accelerator" hits in the sequences blog post: that is Microsoft's own feature name. Keep the address (or add a 301 if he wants a new address, through the redirect map, never as a hand-made redirect).
- **Answer with names for all three:** the same, for each.
- **Answer "keep the names":** no change.
- **Before applying:** list every hit, so no Microsoft product name is caught. Run the copy-drift check after.

### 11. Move price: "Quoted in writing after a short call" (Packages) or "From $20,000, quoted after a short call" (move pages)?
- **Now:** /packages/ shows "Price Quoted in writing after a short call" on the move package cards (the Salesforce, HubSpot, Zoho and monday.com moves; 2 hits). "From $20,000, quoted after a short call" appears on 4 pages (the /faq/ Salesforce answer and the move pages).
- **Answer "From $20,000":** /packages/ move cards: "Price From $20,000, quoted after a short call".
- **Answer "Quoted":** on the 4 pages, "From $20,000, quoted after a short call" becomes "Quoted in writing after a short call". The /faq/ answer changes with its source page.
- Facts doc: full implementation is from $20,000 (Brian, 9 Nov). A move without a price stays consistent with that only if he says so.

### 12. New tile "Build a custom application": a priced package or quoted? Which page does it open?
- **Now:** no such tile exists on staging. Searched for "Build a custom application", "custom application" and "custom app": 0 tiles. The only hits are Power Apps and licensing text.
- **Answer "priced":** a new package card on /packages/ and a tile on the home grid: name, price, weeks, users, a "See the package" link to the page he names. Then a package page (built to the package template) or a link to /dynamics-365-power-apps/.
- **Answer "quoted":** the same tile with "Quoted in writing after a short call", linking to /dynamics-365-power-apps/ (Claude's proposal) or the page he names.
- This is a build, not a line change: about an hour. It needs a version bump and the full verify.

### 13. Full implementation shows "Set in your written plan", no weeks. Keep?
- **Pages (6 hits on 5 pages):** /packages/ (Full Implementation and Rescue cards); /dynamics-365-sales/; /dynamics-365-customer-service/; /microsoft-dynamics-365-implementation/; the Rescue and Repair page.
- **Now:** "Time Set in your written plan".
- **Answer "keep":** no change. Item 13 on the waiting-for-yes list closes.
- **Answer with a range** (for example "6 to 12 weeks"): "Time [his range]" on the Full Implementation rows only. Rescue keeps "Set in your written plan" unless he names it too. The /faq/ Salesforce answer already says "usually 6 to 12 weeks"; make it agree with his answer.

### 14. Support plan terms: all still right?
- **Scale:** 130 hits on 22 pages (the support plan table and its notes repeat sitewide).
- **The lines:** "12-month agreement. Onboarding fee up to one month's charge. Support hours 7:00am to 5:00pm Central, Monday to Friday." "1-hour response on monthly plans." "Optimization $1,500 a month 20 hours a month Up to 50 users." "Partnership From $2,000 a month 35 hours a month 50 users and up."
- **Answer "all right":** no change.
- **Answer with a change:** change that one value in the shared support plan block (theme pattern or the site/ copies), rebuild, and count the hits before and after. They must move together. The facts doc gets the new value, with the old one in brackets.

### 15. Sales Accelerator: data beyond the 500-record import, and Power Automate flows: included or quoted?
- **Pages (3):** /dynamics-365-sales-accelerator/, /dynamics-365-service-accelerator/, /dynamics-365-sales/. Under "Not included": "Data migration beyond the 500-record import", "Custom tables", "Power Automate flows".
- **Answer "quoted":** no change.
- **Answer "included" (either item):** move that line from "Not included" to "Included" on the 3 pages, with his limit if he gives one (for example "Up to 3 Power Automate flows").

### 16. Service Accelerator: how many queues? **BLOCKER** (2)
- **Page:** /dynamics-365-service-accelerator/
- **Now:** "[Brian sets]" twice (the queues line in Included and in the package table; inferred from the page's layout).
- **Answer with a number:** "Up to [N] queues" in both places. Remove both brackets. /dynamics-365-customer-service/ says "Cases, queues and SLAs set up". Add his number there too only if he wants it.

### 17. Do the 4-week accelerators get weekly project meetings and UAT too?
- **Now:** the home page and implementation stages say "weekly project meetings" (Stage A) and "User acceptance testing (UAT) and fixes" (Stage C). The accelerator pages do not mention either.
- **Answer "yes":** add to "Included" on /dynamics-365-sales-accelerator/ and /dynamics-365-service-accelerator/: "Weekly project meetings" and "User acceptance testing before go-live".
- **Answer "no":** add nothing.
- **Answer "meetings only" or "UAT only":** add just that one line.

### 18. Implementation, Not included: "Agents and Copilot Studio work, scoped separately." Right?
- **Pages (3):** /microsoft-dynamics-365-implementation/, /dynamics-365-sales/, /dynamics-365-customer-service/.
- **Answer "right":** no change.
- **Answer "included":** move the line to "Included" as "Copilot and agents switched on" (the Stage C wording already on the home page). Remove it from "Not included" on all 3.

### 19. Five Microsoft phases vs our four rows (Discover and Initiate share one). Clear enough?
- **Pages:** /microsoft-dynamics-365-implementation/ (the table row "Stage A. Plan | Discover and Initiate", and the sentence "Microsoft's Success by Design framework uses five phases..."); /faq/ (the same sentence).
- **Answer "clear":** no change.
- **Answer "split it":** add a fifth row so each Microsoft phase has its own row. The stages stay four (A Plan, B Build, C Go live, D Run). Change the sentence "Our four stages, ..." on both pages to match.

## Contact, booking and menu

### 20. Does the street address stay on Contact?
- **Pages:** /contact-us/ (the address block "enCloud9 LLC 2915 Lynnwood Dr. Bellevue, NE 68123" and the FAQ "Our office is at ..."). The address also appears on /faq/, /microsoft-dynamics-365-partner-omaha/, /privacy-policy/ and /terms-of-use/.
- **Answer "stays":** no change. This matches Michael's 14 Nov "show it everywhere".
- **Answer "remove from Contact":** remove the address block on /contact-us/ only. Keep the FAQ answer, the Omaha page, the privacy and terms pages, and the schema (Michael's 14 Nov rule). Tell Michael, since it reverses part of his call.

### 21. Contact form: add a phone field?
- **Now:** /contact-us/ form fields are Your name, Company name, Work email, then "What do you...".
- **Answer "keep it short":** no change.
- **Answer "add phone":** add an optional "Phone" field after Work email. Map it in the ClickDimensions form capture (the clickdimensions-forms skill). Run one test submit to Dynamics and delete the test lead. It is a form change, so it waits for a staging test, not just a build.

### 22. Menu: keep, or regroup as Packages, Move to Dynamics 365 and Support? Does Contact stay under About?
- **Now:** the menu is in the theme header part (header.html, built from the site home page).
- **Answer "keep":** no change.
- **Answer "regroup":** a theme change, so the theme version goes up. Move the items into the three groups he names. Contact goes where he says. Run the phone and tablet check after.

### 23. On a 750 px screen, fit all 7 items on one row and drop the header Book a call button?
- **Answer "yes":** theme CSS. At up to 800 px wide, show all 7 items at smaller type and hide the header Book a call button. The page's own Book a call buttons stay. Theme version goes up. Michael's real-phone check (tracker row A20) runs after.
- **Answer "no":** no change.

## Look and wording

### 24. Headings: title case for short headings and names, sentence case for questions. His call too?
- **Now:** live on staging. Michael confirmed it as his and Brian's (23 Nov). The record is wp-theme-fable/reports/headings-title-case-23-nov.csv.
- **Answer "yes":** no change.
- **Answer "no":** revert using headings-title-case-23-nov.csv, which lists each heading before and after.

### 25. Home headline "Dynamics 365, Driven by Copilot". OK?
- **Page:** / (the hero heading).
- **Answer "OK":** no change.
- **Answer "the old one":** "Copilot AI-Driven Dynamics 365".
- **Answer with new words:** his words. Check the page title and meta description on / still agree.

### 26. "Complimentary" instead of "free": Fit Check only, or everywhere?
- **Scale:** "Free checkups" appears 121 times on 92 pages (the final call-to-action block on almost every page). "free Health Check" and "free License Check" appear 6 times on 4 pages. "free Fit Check" appears on 5 pages. "Is the first call free? Yes. The first call is free" appears on 5 pages.
- **Answer "Fit Check only":** "a free Fit Check" becomes "a complimentary Fit Check" on its 5 pages (/faq/ follows its sources).
- **Answer "everywhere":** the same, plus "Free checkups, no obligation" becomes "Complimentary checkups, no obligation" in the shared final block, and "free Health Check" and "free License Check" change to match.
- **Check:** the button "Book the free check" and the page /free-guides-and-checks/ (its address stays). Prices and headings that say "Free" as a label stay unless he says otherwise. Plain-copy note: "complimentary" is longer and reads less plainly. Say so once, then do what he says.

### 27. Keep the name "Fit Check"?
- **Scale:** 19 hits on 5 pages.
- **Answer "keep":** no change.
- **Answer with a new name:** replace "Fit Check" in all 19 hits. That includes the /faq/ question "What is the Fit Check?" and the Rescue and Repair "First step" row.

### 28. "Client stories" becomes "success stories" everywhere?
- **Scale:** 195 hits on 57 pages (breadcrumbs, the "All 23 client stories" links, the stories hub, the About counters, and "Client story · ..." labels on the 23 stories).
- **Answer "yes":** replace "client stories" with "success stories" and "Client story" with "Success story", in every case. The hub address stays /about-encloud9/microsoft-dynamics-365-success/ (it already says success). The /stories/ addresses stay. Rebuild and recount: it must be 0 "client stor" afterwards, except inside quotes from clients.
- **Answer "no":** no change.

## Free checks

### 29. Are the one-hour first call and the one-to-two-hour Health Check the same offer?
- **Found while mapping:** the Health Check page disagrees with itself.
  - /crm-health-check/ says "Up to one hour, no obligation" and "The session takes up to one hour."
  - Its own FAQ says "One to two hours of free consulting time with an enCloud9 consultant" (Brian's 17 Nov audio; waiting-for-yes item 6).
  - /free-guides-and-checks/ says "A check is a session of up to one hour on your own system."
  - The home page says "the first hour-long call is free".
- **Answer "same offer":** one length everywhere. Use his length. If he says one to two hours: "Up to one hour" becomes "One to two hours" on /crm-health-check/ (2 places) and /free-guides-and-checks/. If the License Check stays one hour, /free-guides-and-checks/ needs "Each check takes one to two hours (Health Check) or up to one hour (License Check)".
- **Answer "different offers":** keep the first call at one hour. Make the Health Check say one to two hours in all 3 places on its own page. Add one line to the Health Check FAQ: "This is separate from the free first call."
- **Either way:** fix the self-contradiction on /crm-health-check/ before launch. If Brian does not answer, bring it to Michael (it is a promise about free time).

### 30. Does the Health Check look at customizations, security roles, data quality and automation? **BLOCKER** (1)
- **Page:** /crm-health-check/
- **Now:** "[What we look at, Brian confirms: for example customizations, security roles, data quality, automation.]"
- **Answer "yes":** "We look at your customizations, security roles, data quality and automation." Remove the bracket.
- **Answer with his list:** his list, in the same sentence.

### 31. Sample findings marked "Not a real client": the kind we really find?
- **Pages (2):** /crm-health-check/ ("Sample findings, CRM Health Check. Not a real client." and its table); /dynamics-365-license-check/ (the same, with the February 2027 row sourced to Microsoft Learn).
- **Answer "yes":** no change.
- **Answer "change rows":** edit the named rows. A row about licensing must keep a Microsoft source.
- **Answer "drop them":** remove the sample table and its caption on both pages.

### 32. A follow-up email from a real person a few days after a guide download? **BLOCKER** (5)
- **Pages (5):** /lp/copilot-guide-dynamics-365-crm/, /crm-cleanup-checklist/, /dynamics-365-sales-management-guide/ ("[Follow-up email wording, Brian approves.]"); /faq/ and /free-guides-and-checks/ ("[Follow-up email from a real person a few days later, per the lead magnet plan; Brian approves t...]").
- **Answer "yes":** on the 3 guide pages, "A few days later, someone from enCloud9 emails to ask if the guide helped. No sales pitch." The FAQ and the checks page get the same sentence. Claude drafts the email itself (educational, no pitch, his 11 Nov answer 32) for his approval. The email is built in ClickDimensions only after his yes to its wording.
- **Answer "no":** remove the 5 brackets. Say nothing about a follow-up.

### 33. On the free check and guide pages the menu highlights About, but they sit under Packages. Change it?
- **Now:** a theme menu-state rule, not page text.
- **Answer "yes":** theme change so these pages highlight Packages: /free-guides-and-checks/, /crm-health-check/, /dynamics-365-license-check/ and the 3 guide pages. Theme version goes up.
- **Answer "no":** no change.

## Blog

### 34. Author line for every post: "Brian Begley is the founder and CEO of enCloud9, a Microsoft Dynamics 365 partner since 2008." plus his LinkedIn
- **Scale:** 16 hits on 16 posts.
- **Answer "OK":** no change.
- **Answer with changes:** replace the line in the blog post pattern (theme patterns/post-layout.php and the site/ copies) and all 16 posts. The 2 Kristin posts keep their own line (Brian list 45).

### 35. The generative pages post and the November 2026 post: keep or drop each? **BLOCKER** (4)
- **Pages:** /blog/generative-pages-dynamics-365/ ([Publish date], [Author], [Author's role...]); /blog/whats-new-in-dynamics-365-november-2026/ ([publish date]).
- **Answer "keep":** the publish date is launch day (question 1). The author is Brian with the standard author line (question 34), unless he names someone else. The brackets clear.
- **Answer "drop":** remove the page from pages.json and from the blog index (the count on /blog/ drops by one). Add its address to the redirect map: 301 to /microsoft-copilot-for-business/#genpages for the generative pages post, or 410 for the November post (Claude's proposal).

### 36. The blog standard on all 16 posts. OK?
- **Answer "OK":** no change.
- **Answer with exceptions:** follow "Blog standard (living).md" for the parts he names. Apply them to all 16 posts.

### 37. Two FAQ answers that are Claude's, not his: "at least once a year, and after any big change" and "weekly". Keep?
- **Pages:**
  - /blog/what-a-healthy-dynamics-365-system-actually-looks-like/ ("How often should we check system health? At least once a year, and after any big change: new team, new process, or a new app.");
  - /blog/how-to-stop-leads-from-falling-through-the-cracks-in-dynamics-365/ ("How often should we review stalled leads? Weekly. Use a view of open leads with no recent activity.").
- **Answer "keep":** no change.
- **Answer with his words:** replace the answer sentence only. The FAQ schema on each post follows its visible text.

### 38. encloud9demo tenant licenses: partner benefit or bought? **BLOCKER** (12 screenshot spots)
- **Pages:** the 7 "[Screenshot from the marketing sandbox: ...]" spots (sequences x2, Sales Qualification Agent, data quality, lead management, healthy system, customizations). Also the 5 later found (sequences, generative pages, stop-leads, last activity, storage posts).
- **Answer either way:** no page text changes. It decides where Claude takes the screenshots. Once that environment exists, each spot gets a real screenshot with alt text and the bracket clears. If the licenses are bought and he will not add more, the fallback is Microsoft Learn's own images, linked, not copied.

### 39. CRM Software Blog: weekly or 2 a month, and the short version?
- No site change. It goes to the marketing playbook and the CRM Software Blog notes.

### 40. Two new posts a month, 2nd and 4th Tuesday, from the second week of January?
- No site change. It goes to the marketing playbook calendar.

### 41. Data quality, Activate and 2024 posts: a real client result, or general?
- **Pages:** /blog/how-to-improve-dynamics-365-data-quality-garbage-in-garbage-out/, /blog/how-dynamics-365-activate-makes-leaving-salesforce-easier/, and the 2024 sales usage post.
- **Answer with a result:** add one sentence with the client and the number he gives. Use only a client with a published story (his 11 Nov rule). Link to that story.
- **Answer "general":** no change.

## Other pages

### 42. Distribution page: which clients should it name? **BLOCKER** (1)
- **Page:** /dynamics-365-distribution/
- **Now:** "[Brian names the distribution clients to show here.]"
- **Answer with names:** one card per client, linking to its /stories/ page, with the story's own one-line summary. Remove the bracket. Only clients with a published story (his 11 Nov rule). Claude's earlier guess was World Import Distributors and MSA Source; that is a guess, never filed as his answer.

### 43. Logo book: when can we meet?
- No site change. A calendar item for Michael.

---

## Not on the 43 but blockers Brian also holds (for the next message)
- The lawyer: the warranty and liability wording, governing law (/terms-of-use/), the Nebraska fit (/privacy-policy/), and both DRAFT bars with their "[bracket]" lines.
- Whether the chat assistant goes live at launch: /accessibility/ ("[the chat assistant]") and /privacy-policy/ ("[if the chat assistant goes live: ...]").
- Brian list item 43 (go or no-go: AI crawlers and Bing defaults) and item 46 (Compana live at check 3).

## After each answer
- Answer filed: DECISIONS (business facts, with his words and date), the facts doc, and the Brian list item struck.
- Blocker count: `python3 -I tools/verify.py --launch` before and after, with the number in the commit message.
- Staging: one plugin build per batch of answers, uploaded and read back on the changed pages.
