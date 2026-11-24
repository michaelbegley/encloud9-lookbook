# Outside links on staging, report only

Tue 24 Nov 2026, about 2:30 AM Central. Claude, #17 Facilitator, at the Compass's ask (relayed by Michael, 1:34 AM). Nothing was changed on staging or in the repo's pages.

## Result
- **104 outside links tested** (every distinct outside link in plugin 0.5.74's pages, commit a578393). **0 dead.**
- **3 cited figures not found on the page they cite**, all in /blog/dynamics-365-pricing-licensing-2025-guide/. **1 link lands on a different page.** **2 links redirect to a new address on the same subject.**
- **YouTube: 7 video links, 7 play** ("OK" from YouTube's own player status), all on the enCloud9 channel. The 2 channel links open the channel.

## Scope, and why it is all 104
The Compass asked for the links new since the 17 Nov link check (82 links then): the source links in the 16 rewritten posts, plus any link added in the wording pass. The site's page data is only tracked in git from 23 Nov, so the 17 Nov list cannot be rebuilt exactly. So all 104 current outside links were tested. 82 of them sit in the 18 blog posts (the 16 rewritten posts and the 2 unpublished ones). Links to encloud9.com and staging were left out (encloud9-verify covers inside links).

## How it was checked
- **Where:** each link was opened in Michael's Chrome. Neither the cloud workspace nor the shell on Michael's computer can reach outside sites; both were refused by the network allowlist.
- **For each link:** the final address and the page title were read. For a link to a heading (#anchor), the check also confirmed the heading still exists on the page. For YouTube, the player's own playability status was read, with the video ID and channel. For the links that carry a price or a number, the page text was searched for that figure.
- **Whether the page still says what we cite it for:** judged from the title, the heading anchor and, for numbers, the text search. A full reread of every page was not done; the 3 flags below come from the number searches.

## Flags

### Cited figure not found on the page (3), all on /blog/dynamics-365-pricing-licensing-2025-guide/
1. **"$21 per user per month"** (Microsoft 365 Copilot Business) links to learn.microsoft.com/partner-center/announcements/2025-december. The page is live and its 4 Dec 2025 item says the Copilot Business SKUs are live. It shows no $21; the only prices on it are $30 and $15 (measured). The figure needs another source (Microsoft's own pricing page), or a different line.
2. **"$18 on an annual subscription through 31 December 2026"** (the 15% promotion) links to .../announcements/2026-july. The page is live and covers Copilot Business ("Copilot in 30" trial). It shows no $18 and no 15% promotion; the prices on it are $15 and $10 (measured). Same fix.
3. **"Up to 20% off with an up-front commitment"** (Copilot Credit pre-purchase plan) links to learn.microsoft.com/azure/cost-management-billing/reservations/copilot-credit-p3. The page is live and describes tiered pre-purchase discounts ("The more you buy, the greater the discount"). Its only worked example is a 6% saving. "20%" is not in the page text (measured). The 20% may be in a tier table drawn as an image; could not determine.

### Lands on a different page (1)
4. **"5% more"** (monthly billing on an annual subscription since 1 April 2025) links to .../partner-center/announcements/2025-march. That page now redirects to the general Partner Center announcements index. Same finding as 17 Nov, left as is then. The line needs Microsoft's own page for the 5% change, or the link removed.

### Redirect to a new address, same subject (2; no action needed unless we want clean links)
5. learn.microsoft.com/en-us/dynamics365/sales/sales-qualification-agent-43 now goes to .../sales-qualification-agent ("Sales Qualification Agent overview"), on /blog/dynamics-365-sales-qualification-agent/.
6. microsoft.com/en-us/power-platform/products/power-bi/pricing now goes to microsoft.com/en-us/microsoft-fabric/features/power-bi/pricing ("Power BI: Pricing Plan"), on /microsoft-power-bi/ and /microsoft-power-platform/.

### Normal, not flagged
- 4 links written as microsoft.com without www, and Learn links without en-us, gain those on the way. Each lands on the same page.
- make.powerapps.com opens the Power Apps home for the signed-in user. It is a sign-in link, by design.
- The Bookings link was checked on 23 Nov ("Bookings with me - Brian Begley") and not reopened tonight.
- One YouTube title differs from our link text, but the subject is the same. 5Q-JYI6b-So is "How to Create Leads in Dynamics 365 from Outlook Emails with Sales Copilot"; our text says "How to Create a Lead from an Outlook Email in Copilot".

## Every link
Columns: the link; result.
- **Learn, guidance and implementation guide:**
  - change-management-transition-handover: live.
  - extend-your-solution#define-your-extension-strategy: live, heading found.
  - fit-to-standard-fit-gap-analysis #fit-gap-analysis and #fit-to-standard-analysis: live, both headings found.
- **Learn, Customer Insights:**
  - removed-deprecated-features #...november-2026: live, heading found.
  - whats-new-customer-insights: live.
  - journeys/whats-new-marketing: live.
- **Learn, Project Operations:** whats-new-nov-2026-lite: live.
- **Learn, Sales:** live, each on its own topic:
  - configure-predictive-lead-scoring, configure-sales-qualification-agent;
  - connect-a-sequence-to-records (and #through-power-automate, heading found);
  - create-and-activate-a-sequence, create-manage-sequences, delete-a-sequence, edit-a-sequence, edit-active-sequence;
  - digital-selling-scoring, enable-duplicate-lead-detection, qualify-lead-convert-opportunity-sales, sales-accelerator-intro;
  - view-sequence-details-connected-records, wa-create-and-activate-assignment-rule;
  - view-understand-sales-usage-reports, deprecations-sales#sales-usage-reports (heading found);
  - sales-qualification-agent-43: redirect, same subject (flag 5).
- **Learn, Activate:** dynamics-365-activate-overview: live. migrate-salesforce-to-dynamics-365-overview (and #automated-discovery): live, heading found.
- **Learn, Power Platform admin:**
  - capacity-storage (with and without en-us, and #manage-storage-overage): live, heading found.
  - delete-bulk-records, detect-duplicate-data, set-up-duplicate-detection-rules-keep-data-clean: live.
  - pay-as-you-go-meters: live, $48 found.
  - powerapps-flow-licensing-faq: live, $40 found.
  - general-availability-deployment: live, "April and October" found.
  - opt-in-early-access-updates, policies-communications: live.
- **Learn, important-changes-coming:** all 6 anchors found (AI-generated descriptions, copresence in Power Apps plans, Dataverse for Teams, record-level copresence, unmanaged developer environments, Describe it to design it).
- **Learn, Power Apps:** define-rollup-fields (and the Activity Party anchor, heading found), control-access-forms#set-security-roles-for-a-form (heading found), generative-pages, channel-overview: live.
- **Learn, other:**
  - power-automate/replace-workflows-with-flows, microsoft-365/admin/manage/roadmap, microsoft-copilot-studio/requirements-messages-management: live.
  - compliance/regulatory/offering-hipaa-hitech, business-central/marketing-integrate-dynamicscrm, get-started/release-schedule, training/modules/sales-sequence/4-disconnect: live.
- **Learn, Partner Center:**
  - 2025-december: live, figure not found (flag 1).
  - 2026-july: live, figure not found (flag 2).
  - 2026-september: live. It says Dynamics 365, Power Platform and Dataverse roadmap content moves to the AI at Work roadmap starting September 2026, which matches what we cite.
  - 2025-march: lands on the announcements index (flag 4).
- **Learn, Azure:** copilot-credit-p3: live, "20%" not found (flag 3).
- **microsoft.com pricing:** live, each on its own product:
  - Sales, Customer Service, Customer Insights, Field Service, Project Operations, Contact Center (each with and without www and en-us);
  - Power Apps, Power Automate, Power Pages;
  - Copilot Studio ($200 found).
  - Power BI: redirect, same subject (flag 6).
- **microsoft.com, other:** Copilot blog 8 Oct 2026, the Dynamics 365 Activate blog 9 Sep 2026, Microsoft 365 pricing and packaging updates 2026, Dynamics 365 licensing guidance: live.
- **ClickDimensions:** the 5 dashboard articles (Marketing Summary, Email, Forms, Surveys, Landing Pages) and clickdimensions.com: live.
- **CRM Software Blog:** Best Dynamics 365 CRM Partner List 2026: live, names enCloud9.
- **GitHub:** Sales Usage Reporting Sample.pbit: live.
- **YouTube:**
  - 0CkVJqdgPek, Hitn-q-mzok, 5Q-JYI6b-So, HUgUlEYomKM, XbWtfPzE2N0, mJ2Vf09tGng, pZdhwN6AIM4: all OK, all on the enCloud9 channel.
  - @enCloud9CRM and its subscribe link: open the channel.
  - 7 video links in all: 2 youtube.com watch links and 5 youtu.be links (the youtu.be links forward to youtube.com, as they should).
- **LinkedIn:** brianbegleydynamicscrm: "Brian Begley | LinkedIn".
- **make.powerapps.com:** opens Power Apps home (sign-in link).
- **Bookings:** checked 23 Nov.
