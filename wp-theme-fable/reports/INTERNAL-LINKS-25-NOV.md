# Internal links on the new site, first count (report only)

Wed 25 Nov 2026, 12:50 AM Central (tool clock), #18 Facilitator. Roadmap step 10 (internal-linking pass), started early because it needs no answer from anyone. Nothing changed on staging or in the source.

Source: wp-theme-fable/encloud9-site/data/pages.json at commit b08a010 (plugin 0.5.81), 107 pages. Counted: links inside each page's body to another page of the 107. Not counted: the menu, the footer and links into the 138 blog posts (those are not in pages.json).

## Pages with 2 or fewer body links pointing to them
```
pages 107
inbound from page bodies (menus and footer not counted):
  0 in |   4 out | noindex=True | /404/ | Page Not Found | enCloud9
  0 in |   3 out | noindex=False | /accessibility/ | Accessibility Statement | enCloud9
  0 in |  10 out | noindex=True | /call-prep-received/ | Answers Received | enCloud9
  0 in |   8 out | noindex=False | /lp/best-crm-partner/ | Best CRM Partner for Small Businesses | enCloud9
  0 in |   7 out | noindex=False | /lp/dynamics-365-consulting-youtube/ | Dynamics 365 Help and Videos | enCloud9
  0 in |   6 out | noindex=False | /lp/dynamics-365-consulting/ | Dynamics 365 Consulting for Growing Businesses | enCloud9
  0 in |  10 out | noindex=True | /newsletter-signup-successful/ | Thanks for Subscribing | enCloud9
  0 in |  10 out | noindex=True | /request-received/ | Request Received | enCloud9
  0 in |   3 out | noindex=False | /terms-of-use/ | Website Terms of Use | enCloud9
  0 in |  10 out | noindex=True | /thank-you-contact/ | Message Received | enCloud9
  0 in |  10 out | noindex=True | /thank-you/ | Thank You | enCloud9
  1 in |   8 out | noindex=False | /blog/generative-pages-dynamics-365/ | Generative Pages in Dynamics 365: 12 Ways to Use Them
  1 in |   2 out | noindex=True | /call-prep/ | Call Preparation | enCloud9
  1 in |   5 out | noindex=False | /crm-cleanup-checklist/ | Dynamics 365 CRM Cleanup Checklist for Admins | enCloud9
  1 in |   5 out | noindex=False | /dynamics-365-sales-management-guide/ | Dynamics 365 Sales Management Guide | enCloud9
  1 in |   9 out | noindex=False | /how-microsoft-updates-dynamics-365/ | How Microsoft Updates Dynamics 365 After Release Waves
  1 in |   6 out | noindex=False | /lp/copilot-guide-dynamics-365-crm/ | Copilot Guide for Dynamics 365 CRM Users | enCloud9
  1 in |  12 out | noindex=False | /microsoft-dynamics-365-partner-omaha/ | Dynamics 365 Partner in Omaha, Nebraska | enCloud9
  1 in |   8 out | noindex=False | /stories/hogan-assessments/ | Hogan Assessments: Dynamics 365 Rescue | enCloud9
  1 in |   8 out | noindex=False | /stories/msa-source/ | MSA Source: Better Reporting and Seed Money Math | enCloud9
  2 in |  10 out | noindex=False | /about-encloud9/how-we-work/ | How We Work on Dynamics 365 Projects | enCloud9
  2 in |   9 out | noindex=False | /about-encloud9/team/ | The enCloud9 Team | Dynamics 365 Partner
  2 in |  11 out | noindex=False | /blog/how-to-improve-dynamics-365-data-quality-garbage-in-garbage-out/ | How to Improve Dynamics 365 Data Quality
  2 in |   9 out | noindex=False | /blog/whats-new-in-dynamics-365-november-2026/ | What Changed in Dynamics 365 in November 2026
  2 in |  11 out | noindex=False | /document-core-pack/ | Document Core Pack for Dynamics 365 | enCloud9
  2 in |  13 out | noindex=False | /dynamics-365-healthcare/ | Dynamics 365 for Healthcare Companies | enCloud9
  2 in |  14 out | noindex=False | /dynamics-365-professional-services/ | Dynamics 365 for Professional Services Firms | enCloud9
  2 in |  10 out | noindex=False | /dynamics-365-vs-salesforce-vs-hubspot/ | Dynamics 365 vs Salesforce vs HubSpot Compared | enCloud9
  2 in |  10 out | noindex=False | /encloud9-dynamics-365-crm-services/microsoft-dynamics-365-crm-accelerators/ | Dynamics 365 Accelerators, Fixed-Scope Packages | enCloud9
  2 in |  13 out | noindex=False | /monday-to-dynamics-365/ | Move from monday.com to Dynamics 365 Sales | enCloud9
  2 in |  12 out | noindex=False | /zoho-to-dynamics-365/ | Move from Zoho CRM to Dynamics 365 Sales | enCloud9
pages with 0 body links out to other pages: []
```

## Read (Claude's, proposed)
- Thank-you, 404, call-prep and signup pages are noindex and reached by forms: 0 inbound is expected.
- /accessibility/ and /terms-of-use/: reached from the footer (not counted here). Nothing to do.
- The three /lp/ pages with 0 inbound (best CRM partner, YouTube, consulting) are campaign landing pages; whether they should get body links is a choice, not a fault.
- Worth a link or two from related pages: the Omaha page, the sales management and Copilot guides, the CRM cleanup checklist, How Microsoft updates Dynamics 365, the Hogan and MSA Source stories, How We Work and Team.
- Next, waiting on nothing: a proposed list of exact links to add (from page, sentence, to page), for Michael's yes before anything goes on staging. Best done after Brian's answers land, so the wording they hang on is final.

## Proposed links for the 24 indexed pages (proposals only, Claude's picks)

Added Wed 25 Nov 2026, about 2:15 AM Central (#18). Each line: the page that would carry the link, the section, the sentence as it stands (measured in pages.json at 0.5.81), and the words that would carry the link. Nothing is on staging. A link that depends on one of Brian's 43 questions is marked with the question number (numbering as sent, as on the check 3 read sheet). Candidates were found by script (keyword match in page bodies), then picked by hand.

**No link proposed (5):**
- /accessibility/ and /terms-of-use/: reached from the footer. Terms also rides on Q3 (privacy wording).
- /lp/best-crm-partner/, /lp/dynamics-365-consulting/, /lp/dynamics-365-consulting-youtube/: campaign landing pages, reached from ads, YouTube and email. Linking them from the main pages would compete with the service pages they repeat. Michael's call if he wants them linked.

**CRM cleanup checklist** (/crm-cleanup-checklist/)
- From the data quality post, section "How do you manage duplicate records before they damage data", sentence "Make duplicate detection and review a routine part of CRM administration, not an occasional cleanup." Link: "cleanup".
- From /dataverse-storage-analysis/, section "Dataverse Storage Questions", sentence starting "It depends which storage type is over and what is using it." Link: "a cleanup often pays for itself". The same sentence is on /faq/; one of the two is enough.

**Sales management guide** (/dynamics-365-sales-management-guide/)
- From the lead management post, section "How can enCloud9 help with lead management?", sentence starting "enCloud9 has been a Microsoft Partner since 2008. It helps small and medium-sized businesses set up lead scoring, assignment and follow-up". Add after it: a link on "sales management guide" (new words, no facts).
- From /dynamics-365-sales/, section "A Good Fit If", line "You want one pipeline view and a forecast your managers believe." Link: "pipeline view".

**How Microsoft updates Dynamics 365** (/how-microsoft-updates-dynamics-365/)
- From How We Work, section "During a Project", line "Health checks and updates are logged after go-live, so you always know what changed." Link: "updates".
- From the November 2026 post: a link back to this page. **Rides on Q35** (keep or drop that post).

**Copilot guide** (/lp/copilot-guide-dynamics-365-crm/)
- From the adoption post, section "Why does it matter if people work outside the CRM?", sentence "Copilot and other AI tools need complete, accurate and current data." Add after it a link on "Copilot guide" (new words, no facts).
- From Brian's page, section "What has Brian written?": add the guide to the list. **Rides on Q7** (the Meet Brian page may be rewritten).

**Omaha partner page** (/microsoft-dynamics-365-partner-omaha/)
- From the Team page, section "Questions About the Team", sentence "Our office is in Bellevue, Nebraska, in the Omaha metro." Link: "Omaha metro". **Rides on Q4** (who and what the Team page shows).
- From How We Work, section "Who does the work, and how do we stay in touch?", sentence "Mostly remote, through Teams and screen sharing, with on-site visits for Omaha-area clients when the work needs it." Link: "Omaha-area clients".
- From the BG Peterson story, sentence starting "BG Peterson is a long-standing mechanical services company based in Omaha, Nebraska". Link: "Omaha, Nebraska".

**Hogan Assessments story** (/stories/hogan-assessments/)
- From About, section "What do we believe about Dynamics 365 projects?", point 04 "Standard features first", sentence ending "the ones we most often get called in to rescue." Link: "rescue".
- From the data quality post, section "How do you build long-term Dynamics 365 data quality?", sentence "Some systems need more than routine care." Link: "more than routine care".
- Not proposed: a mention on the HubSpot move page. Whether Hogan may be named there is an open ask for Brian in the move-page notes (not one of the 43).

**MSA Source story** (/stories/msa-source/)
- Weak fits only. Best one: the sales usage reports post, in "The short answer", which points to a Power BI report; a "for example" link on "Power BI report" to this story. No other page body talks about reporting results for a client. Could also wait for the internal pass after launch.

**How We Work** (/about-encloud9/how-we-work/)
- From About, Dynamics 365 Sales, Customer Service, Sales Accelerator and Service Accelerator, the four-stage sections, sentence "Four stages, every time." Link: "Four stages". **Rides on the written-plan sentence** that follows it on all five pages (check 3 list; Brian has not confirmed it; not one of the 43).

**Team** (/about-encloud9/team/)
- From How We Work, section "During a Project", sentence "An experienced enCloud9 consultant leads your project, and the same people stay with you from the plan through support." Link: "the same people". **Rides on Q4 and Q6** (who is listed; the who-leads wording).
- From About, point 09 "The team that builds it supports it". Link: "The team". **Rides on Q4.**

**Data quality post** (/blog/how-to-improve-dynamics-365-data-quality-garbage-in-garbage-out/)
- From the lead management post, section "How do leads get into Dynamics 365?", line "Turn on duplicate lead detection so the same person isn’t entered twice." Link: "duplicate lead detection".
- From the healthy system post, section "2. Reports Are Trusted": add a link beside the duplicate detection video line.
- From the B&G Landholdings story, section "What changed for B&G Landholdings?", line "The team has more confidence in CRM data quality." Link: "CRM data quality".

**Generative pages post** (/blog/generative-pages-dynamics-365/) **All ride on Q35** (keep or drop the post).
- From /dynamics-365-power-apps/, Power Apps Questions, "See generative pages." (check where it points today before changing it).
- From /microsoft-copilot-for-business/, section "Describe the Screen. Watch the Page Build.", sentence starting "Generative pages let you describe a screen in plain English". Link: "Generative pages".

**November 2026 post** (/blog/whats-new-in-dynamics-365-november-2026/) **Rides on Q35.**
- From How Microsoft updates Dynamics 365: a link to it as the latest example.

**Document Core Pack** (/document-core-pack/)
- From the Milestone Leasing story, section "What did enCloud9 change?", line "Reps now create standard quotes directly from the CRM with Document Core Pack." Link: "Document Core Pack". Strongest fit on the list.

**Healthcare** (/dynamics-365-healthcare/)
- From the PriceMDs story, opening sentence "PriceMDs, a healthcare company in Clearwater, FL, ..." Link: "healthcare company".
- From the CRL story, opening sentence "Clinical Reference Lab (CRL), a laboratory testing provider in Lenexa, KS, ..." Link: "laboratory testing provider".

**Professional services** (/dynamics-365-professional-services/)
- From /dynamics-365-project-operations/, section "When does a business need Project Operations?", sentence starting "When you sell time and expertise: consulting, engineering, agencies or professional services." Link: "professional services".
- From the CRM Software Blog post, "The short answer", "the only partner in the Professional Services focus area". Link: "Professional Services".

**Comparison page** (/dynamics-365-vs-salesforce-vs-hubspot/)
- From Packages, section "Which Dynamics 365 package fits my business?", line "You are moving from Salesforce, HubSpot or another CRM." Add a "compare them" link. Rides on the move-page choice (options A and B on the read sheet; Michael's and Brian's call, not one of the 43).
- From the Activate post, "The short answer". Link: "Salesforce".

**Accelerators** (/encloud9-dynamics-365-crm-services/microsoft-dynamics-365-crm-accelerators/) **All ride on Q10** (Sales Accelerator may become "Quick Start").
- From Home, Common Questions, sentence starting "Microsoft list prices for Dynamics 365 Sales are $65, $105 or $150". Link: "Sales and Service Accelerators".
- From the sequences post, sentence "Its Sales Accelerator package sets up Dynamics 365 Sales for your pipeline for $7,500." Link: "Sales Accelerator package".

**monday.com move page** (/monday-to-dynamics-365/)
- From the PriceMDs story, opening sentence, words "was using monday CRM". Link: "monday CRM". Rides on the move-page choice (option B folds this page into one).

**Zoho move page** (/zoho-to-dynamics-365/)
- Its 2 inbound links come from Packages and FAQ, the only other pages that name Zoho (measured). Nothing more to propose. Rides on the move-page choice.

**Count:** 19 pages get at least one proposal, 5 get none. 11 of the 19 have at least one link that rides on a Brian answer or the move-page choice.

## Applied on staging (item 20, Michael's yes 25 Nov 2026, 2:38 AM)
Plugin 0.5.82 (source commit a02693e), uploaded and imported by Claude: "Done: 0 created, 107 updated." Verify before: FAIL 0, WARN 64 (0.5.81); after: FAIL 0, WARN 64 (0.5.82). Read back on staging, 25 Nov about 2:49 to 2:50 AM Central, abba Chrome, read only: each link's address read from the page, each target opened and its heading read.

| Page | Result | Links |
|---|---|---|
| CRM cleanup checklist | pass | data quality post "cleanup"; Dataverse storage analysis "a cleanup often pays for itself" |
| Sales management guide | pass | lead management post "follow-up"; Dynamics 365 Sales "pipeline view" |
| Hogan Assessments story | pass | About "rescue"; data quality post "more than routine care" |
| MSA Source story | not added | the only proposed spot is Microsoft's sample Power BI report; a link there needs new words, which the yes did not cover |
| Data quality post | pass (1 of 3) | B&G Landholdings "CRM data quality". Not added: the lead post's "duplicate lead detection" already links to Microsoft; the healthy-system line needs new words |
| Document Core Pack | pass | Milestone Leasing "Document Core Pack" |
| Healthcare | pass | PriceMDs "healthcare company"; CRL "laboratory testing provider" |
| Professional services | pass | Project Operations "professional services"; CRM Software Blog post "Professional Services" |

Smoke pages: home, /contact-us/ and the sitemap load with no PHP error. Phone width (V7) not checked: DevTools is out of the tool's reach; the change adds links only.
