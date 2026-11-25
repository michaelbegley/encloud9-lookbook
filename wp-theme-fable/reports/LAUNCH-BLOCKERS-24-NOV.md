# Launch-blocker recount, 24 Nov 2026

Tue 24 Nov 2026, about 10:55 PM Central. Claude, #18 Facilitator. Measured with `python3 -I tools/verify.py --launch` on encloud9-lookbook wp-theme-fable, commit 4db5d79 (plugin 0.5.81, the build on staging). Same method as the 23 Nov count: verify's placeholder rule catches brackets of 3 to 300 characters (tools/verify.py line 83). The plugin's data files are not in git, so the run used the ones shipped in encloud9-site-0.5.81.zip (from Michael's Downloads); its pages.json is byte for byte the same as a fresh build of content/pages.json at 4db5d79.

**Result: 64 open placeholders, the same as 23 Nov at 0.5.74.** Nothing between 0.5.74 and 0.5.81 opened or closed one. Split by who unblocks each, using the 23 Nov report's groups (LAUNCH-BLOCKERS-23-NOV.md):

| Who unblocks | Count |
|---|---|
| Brian (his answers, the legal lines, sandbox licenses, the chat assistant) | 40 |
| Claude (10 need the launch date; 4 need the live setup: provider list, cookie list, accessibility gaps, cookie banner line) | 14 |
| Michael (3 photos, the Clarity project ID, 4 move-page download forms) | 8 |
| Kristin (her author line, twice) | 2 |
| Total | 64 |

Note on "the lawyer": 7 of Brian's 40 sit on the privacy and terms pages and name "the lawyer". Brian's newest word on an attorney is 17 Nov: "That's our attorney, Dr. Copilot." So these wait on Brian, not on an outside lawyer.

## All 64, as verify lists them
```
/about-encloud9/: [photo]
/about-encloud9/: [role Brian confirms]
/about-encloud9/team/: [Photo: real, not AI]
/about-encloud9/team/: [Brian confirms who is listed.]
/about-encloud9/team/: [Title, matches LinkedIn; Brian and Michael set it]
/about-encloud9/team/: [role Brian confirms]
/about-encloud9/team/: [One line, Brian confirms: what the team does and how it works with clients.]
/about-encloud9/team/brian-begley/: [Photo of Brian: real, not AI]
/about-encloud9/team/brian-begley/: [Two lines, Brian confirms: his background, what he works on today, and why he started enCloud9.]
/about-encloud9/team/brian-begley/: [Bio, Brian writes or approves: background, how enCloud9 started, the kind of clients he works with.]
/accessibility/: [Known gaps found in testing, listed here with a date.]
/accessibility/: [Date published.]
/accessibility/: [the chat assistant]
/accessibility/: [Date of last review.]
/blog/: [count at launch]
/blog/: [author]
/blog/: [publish date]
/blog/: [Showing count at launch]
/blog/clickdimensions-dashboards-2025-update/: [One line on Kristin's role at enCloud9, Kristin confirms.]
/blog/creating-and-managing-sequences-in-dynamics-365-sales-insights/: [Screenshot from the marketing sandbox: Up next on a lead with a connected sequence]
/blog/creating-and-managing-sequences-in-dynamics-365-sales-insights/: [Screenshot from the marketing sandbox: Connect sequence on the leads list]
/blog/creating-and-managing-sequences-in-dynamics-365-sales-insights/: [Screenshot from the marketing sandbox: the sequence designer with three steps]
/blog/creating-and-managing-sequences-in-dynamics-365-sales-insights/: [One line on Kristin's role at enCloud9, Kristin confirms.]
/blog/dynamics-365-sales-qualification-agent/: [Screenshot from the marketing sandbox: a lead’s research page from the agent]
/blog/generative-pages-dynamics-365/: [Screenshot: Power Apps app designer, Add page, Generative page, Describe a page, with a prompt typed in. Take it in the demo environment.]
/blog/generative-pages-dynamics-365/: [Author's role at enCloud9, and one line on the Dynamics 365 work they do.]
/blog/generative-pages-dynamics-365/: [Author]
/blog/generative-pages-dynamics-365/: [Publish date]
/blog/how-to-improve-dynamics-365-data-quality-garbage-in-garbage-out/: [Screenshot from the marketing sandbox: a duplicate detection rule for leads]
/blog/how-to-stop-leads-from-falling-through-the-cracks-in-dynamics-365/: [Screenshot from the marketing sandbox: a view of open leads with no activity in 30 days]
/blog/how-to-track-the-last-activity-date-in-microsoft-dynamics-365-sales/: [Screenshot from the marketing sandbox: the rollup column editor set to the latest Actual End date]
/blog/mastering-lead-management-in-dynamics-365-igniting-your-sales-pipeline/: [Screenshot from the marketing sandbox: the lead score on a lead record]
/blog/microsoft-dataverse-storage-notifications/: [Screenshot from the marketing sandbox: the Dataverse capacity page in the Power Platform admin center]
/blog/what-a-healthy-dynamics-365-system-actually-looks-like/: [Screenshot from the marketing sandbox: the duplicate detection rules list]
/blog/whats-new-in-dynamics-365-november-2026/: [publish date]
/blog/dynamics-365-customizations-worth-it/: [Screenshot from the marketing sandbox: form settings with security roles assigned]
/crm-health-check/: [What we look at, Brian confirms: for example customizations, security roles, data quality, automation.]
/dynamics-365-distribution/: [Brian names the distribution clients to show here.]
/dynamics-365-service-accelerator/: [Brian sets]
/faq/: [Follow-up email from a real person a few days later, per the lead magnet plan; Brian approves the wording.]
/free-guides-and-checks/: [Follow-up email from a real person a few days later, per the lead magnet plan; Brian approves the wording.]
/how-microsoft-updates-dynamics-365/: [publish date]
/lp/copilot-guide-dynamics-365-crm/: [Follow-up email wording, Brian approves.]
/crm-cleanup-checklist/: [Follow-up email wording, Brian approves.]
/dynamics-365-sales-management-guide/: [Follow-up email wording, Brian approves.]
/hubspot-to-dynamics-365/: [Form: the existing checklist download form (first name, last name, work email, consent). Michael supplies the checklist file and the form before this page goes live.]
/monday-to-dynamics-365/: [Form: the existing checklist download form (first name, last name, work email, consent). Michael supplies the checklist file and the form before this page goes live.]
/salesforce-to-dynamics-365/: [Form: the existing checklist download form (first name, last name, work email, consent). Michael supplies the checklist file and the form before this page goes live.]
/zoho-to-dynamics-365/: [Form: the existing checklist download form (first name, last name, work email, consent). Michael supplies the checklist file and the form before this page goes live.]
/power-platform-dynamics-365/: [publish date]
/privacy-policy/: [Microsoft Clarity, if installed.]
/privacy-policy/: [bracket]
/privacy-policy/: [Confirm with the lawyer how this fits Nebraska and other state laws.]
/privacy-policy/: [Website host, email and chat providers, listed by name.]
/privacy-policy/: [Cookie list, after the cookie audit.]
/privacy-policy/: [Retention periods for leads, form data, analytics and chat transcripts, Brian and the lawyer decide.]
/privacy-policy/: [if the chat assistant goes live: what you type, and how long we keep it]
/privacy-policy/: [Once the cookie banner is built: you can decline non-essential cookies and change your choice at any time.]
/privacy-policy/: [State privacy rights that apply, including the Nebraska Data Privacy Act, and how to use them; lawyer.]
/privacy-policy/: [Effective date.]
/terms-of-use/: [bracket]
/terms-of-use/: [Warranty disclaimer and limitation of liability wording: the lawyer writes this.]
/terms-of-use/: [State law that governs these terms, and where disputes are heard: the lawyer and Brian decide.]
/terms-of-use/: [Effective date.]
```
