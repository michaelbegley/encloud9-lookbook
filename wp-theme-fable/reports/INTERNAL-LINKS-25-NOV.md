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
