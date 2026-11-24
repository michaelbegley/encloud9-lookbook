# Pricing guide post: source fixes, change list (24 Nov 2026)

Page: /blog/dynamics-365-pricing-licensing-2025-guide/
Status: PROPOSED. Nothing changed on staging or in the repo sources. Waiting for Michael's yes.
How checked: each Microsoft page opened in Michael's Chrome and read on screen (address bar, page text, screenshot). No scripts.

All four figures are stated by Microsoft today. So every fix is a link swap; the wording stays, with one optional added clause in change 2.

## 1. $21 (Copilot Business list price)
- BEFORE: "...lists at [$21 per user per month](https://learn.microsoft.com/partner-center/announcements/2025-december)" (that page shows only $30 and $15)
- AFTER: same words, link to https://www.microsoft.com/en-us/copilot/pricing/business
- Seen on screen: "Microsoft 365 Copilot Business (add-on) ... Originally starting from $21.00 now starting from $18.00, user/month, paid yearly". (The old address microsoft.com/en-us/microsoft-365-copilot/pricing now lands on this one.)

## 2. $18 (the promotion, through 31 Dec 2026)
- BEFORE: "a 15% promotion brings it to [$18 on an annual subscription through 31 December 2026](https://learn.microsoft.com/partner-center/announcements/2026-july)" (that page shows only $15 and $10, no 15%)
- AFTER: "a 15% promotion brings it to [$18 on an annual subscription through 31 December 2026](https://www.microsoft.com/en-us/copilot/pricing/business), for the first year only"
- Seen on screen: $18.00; the Buy now button reads "save up to 15%"; the footnote says the offer runs 1 July 2026 to 31 December 2026, needs an annual commitment, and the promotional price applies to the first year only.
- The added clause "for the first year only" is optional. Claude's call: add it, since the footnote says so.

## 3. "Up to 20%" (Copilot Credit pre-purchase plan)
- BEFORE: table row "Pre-purchase plan | [Up to 20% off with an up-front commitment](https://learn.microsoft.com/azure/cost-management-billing/reservations/copilot-credit-p3)" (that page's only worked example is 6%)
- AFTER: same words, link to https://www.microsoft.com/licensing/guidance/CopilotCreditsGuide
- Seen on screen: "Copilot Credit Pre-Purchase Plan (P3) Pricing Tiers": tier 1, 300,000 credits, 5%, up to tier 9, 300,000,000 credits, 20%.

## 4. 5% (monthly billing on an annual subscription)
- BEFORE: "Since 1 April 2025, monthly billing on an annual subscription costs [5% more](https://learn.microsoft.com/partner-center/announcements/2025-march) than paying up front." (that address now lands on the general Partner Center announcements page)
- AFTER: same words, link to https://techcommunity.microsoft.com/blog/microsoft_365blog/flexible-billing-for-microsoft-365-copilot-pricing-updates-for-annual-subscripti/4288536
- Seen on screen (Microsoft 365 Blog, FAQ 2): starting 1 April 2025, monthly billing plans for annual term subscriptions across Buy Online, CSP and MCA-E are standardized with a price update of 5%; categories in scope include Microsoft Dynamics 365 Services.
- Note: this is Microsoft's own blog, not a Learn page. The Learn announcement addresses for March 2025 and November 2024 both now land on the general index.

## On yes
Edit site/blog/dynamics-365-pricing-licensing-2025-guide/index.html (the source), rebuild, verify, bump the plugin, upload to staging, then re-read the four links on screen.
