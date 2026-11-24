# Staging redirect test, report only

Tue 24 Nov 2026, about 1:40 AM Central. Claude, #17 Facilitator, at the Compass's ask (relayed by Michael, 1:04 AM). Nothing was changed: no rule edited, added or removed.

## Result
- **383 rules tested; 383 behave as written.** 352 redirects each land on their own target with a 200. 31 gone rules each return 410.
- **Chains: 0. Loops: 0. Landing on a missing page (404 or other error): 0. Wrong target: 0.**
- **Rule codes in the Redirection plugin:** 352 set to 301 and 31 set to 410, read from the Tools > Redirection list (all 383 rows, 2 pages at 200 per page). The list view was put back to 25 rows per page afterwards; it shows 16 pages again (measured).

## How it was measured
- **Where:** Michael's Chrome, on the staging site itself (encloud9-new.flywheelsites.com). Neither the cloud container nor the shell on Michael's computer could reach staging (both returned no connection).
- **The rules:** the repo's redirection-import-301.csv (352) and redirection-410.txt (31), read from GitHub. That is the set imported to staging: the plugin shows 383 items, 352 at 301 and 31 at 410.
- **Each rule got two plain GET requests from the page:**
  1. With redirects not followed. This gives the first answer: a redirect, or the status.
  2. With redirects followed. This gives the final address and status.
  If a final address had differed from the rule's target, the target was to be requested too, to see whether it redirected on (a chain). None differed, so none was needed.
- **Proof the table below is what was measured:** each rule was reduced to "source | final address | final status | first answer", and the list was sorted and hashed with SHA-256.
  - Measured in the browser: e65dabbf68d3bb94 (first 16 hex characters).
  - Expected, built here from the repo lists with every redirect landing on its own target at 200 and every gone rule at 410: e65dabbf68d3bb94.
  - They match, so every row below is the measured result. The test ran twice (the first run's results were lost to a page reload), and both gave the same counts.
- **What a browser cannot see:** the code on the first hop. The page sees "a redirect", not 301 or 302. The 301 code comes from the plugin's own list. The number of hops is not visible either, but a chain would end somewhere other than the rule's target, and no rule did.
- **Run time:** 93 seconds, 6 requests at a time. No cookies, tokens or headers were read or reused.

## Not covered
- The live site (encloud9.com) still runs its old rules. This is staging only.
- Old addresses that are not in the 383 rules: the 31 LEAVE-404 rows in REDIRECT-MAP-Draft1-FULL.csv stay 404 by design and were not tested. The /security/ CHECK row is still open.
- Query strings: passing through is a plugin setting (waiting-for-yes item 11, kept). It was not re-tested here.

## Every rule (sorted by source)
| Source | Rule | Plugin code | Lands on | Final status | At its target |
|---|---|---|---|---|---|
| /13-signs-that-your-crm-sucks/ | 301 | 301 redirect | /blog/13-signs-that-your-crm-sucks/ | 200 | yes |
| /5-challenges-new-businesses-face-crm-can-help/ | 301 | 301 redirect | /blog/how-dynamics-365-solves-common-smb-challenges/ | 200 | yes |
| /5-simple-ways-to-step-up-your-marketing-2/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /6-killer-new-features-of-dynamics-365/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /6-strategies-for-great-customer-service/ | 301 | 301 redirect | /blog/10-strategies-for-great-customer-service/ | 200 | yes |
| /61-distribution-companies-using-crm/ | 301 | 301 redirect | /blog/61-distribution-companies-using-crm/ | 200 | yes |
| /70-insurance-companies-use-crm/ | 301 | 301 redirect | /dynamics-365-professional-services/ | 200 | yes |
| /about | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /about-encloud9-2/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /about-encloud9-2/microsoft-dynamics-365-success-2/ | 301 | 301 redirect | /about-encloud9/microsoft-dynamics-365-success/ | 200 | yes |
| /about-encloud9-2/microsoft-dynamics-365-success/ | 301 | 301 redirect | /about-encloud9/microsoft-dynamics-365-success/ | 200 | yes |
| /about-encloud9/events/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /about-us/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /begin-the-year-with-a-bang-with-our-marketing-checklist/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog-site/ | 301 | 301 redirect | /blog/ | 200 | yes |
| /blog/2020/02/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/2021/06/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/2022/02/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/2022/03/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/2022/08/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/2023/11/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/2023/12/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/2024/03/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/5-challenges-new-businesses-face-crm-can-help/ | 301 | 301 redirect | /blog/how-dynamics-365-solves-common-smb-challenges/ | 200 | yes |
| /blog/5-clickdimensions-updates-to-look-forward-to/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/5-must-have-microsoft-365-copilot-features-2025/ | 301 | 301 redirect | /microsoft-copilot-for-business/ | 200 | yes |
| /blog/5-of-the-most-common-tracked-sales-metrics/ | 301 | 301 redirect | /blog/measuring-crm-success-in-dynamics-365-metrics-kpis/ | 200 | yes |
| /blog/5-simple-ways-to-step-up-your-marketing-2/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/6-killer-new-features-of-dynamics-365/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /blog/a-basic-sales-training-outline-for-dynamics-365-sales/ | 301 | 301 redirect | /blog/getting-started-with-dynamics-365-sales/ | 200 | yes |
| /blog/accelerate-business-growth-with-the-microsoft-power-platform/ | 301 | 301 redirect | /microsoft-power-platform/ | 200 | yes |
| /blog/announcing-encloud9s-copilot-ai-practice-the-future-of-dynamics-365-sales/ | 301 | 301 redirect | /microsoft-copilot-for-business/ | 200 | yes |
| /blog/april-2020-new-feature-deep-dive-sales-forecasting-webinar/ | 301 | 301 redirect | /blog/boost-forecast-accuracy-with-product-catalog-and-quotes-in-dynamics-365/ | 200 | yes |
| /blog/april-2024-dynamics-365-release-enhances-ai-collaboration-with-microsoft-teams/ | 301 | 301 redirect | /microsoft-copilot-for-business/ | 200 | yes |
| /blog/august-webinar-case-management-in-dynamics-365-for-customer-service/ | 301 | 301 redirect | /blog/provide-seamless-customer-service-with-case-management-in-dynamics-365/ | 200 | yes |
| /blog/automated- | 301 | 301 redirect | /blog/automated-notifications-in-dynamics-365/ | 200 | yes |
| /blog/begin-the-year-with-a-bang-with-our-marketing-checklist/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/best-of-the-april-2020-power-apps-and-dynamics-365-update-webinar/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /blog/blog-ai-selling-dynamics-365-sales-2025/ | 301 | 301 redirect | /blog/ai-selling-dynamics-365-sales/ | 200 | yes |
| /blog/blog-hubspot-migration-guide-encloud9/ | 301 | 301 redirect | /hubspot-to-dynamics-365/ | 200 | yes |
| /blog/boosting-summer-sales-with-dynamics-365-10-easy-strategies-part-1/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/boosting-summer-sales-with-dynamics-365-10-easy-strategies-part-2/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/build-stronger-relationships-with-dynamics-365-sales-insights/ | 301 | 301 redirect | /blog/our-top-10-dynamics-365-sales-insights-features/ | 200 | yes |
| /blog/business-ca/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /blog/but-really-what-is-dynamics-365/ | 301 | 301 redirect | /power-platform-dynamics-365/ | 200 | yes |
| /blog/campaign-integration-between-dynamics-365-and-clickdimensions-social-engagement/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/can-business-benefit-crm/ | 301 | 301 redirect | /power-platform-dynamics-365/ | 200 | yes |
| /blog/click-product-update-2025-whats-new/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/clickdimensions-adds-a-microsoft-teams-integration-to-their-event-management-services/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/clickdimensions-product-update-offers-new-functionalities/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/close-more-deals-with-marketing-automation/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/december-2019-webinar-mobilize-your-business-processes-with-dynamics-365-mobile/ | 301 | 301 redirect | /blog/dynamics-365-sales-mobile-app/ | 200 | yes |
| /blog/dont-be-afraid-of-the-unified-interface-webinar/ | 301 | 301 redirect | /blog/basic-dynamics-365-navigation/ | 200 | yes |
| /blog/downloads_resources/microsoft-dynamics-365-for-sales-data-sheet/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /blog/downloads_resources/social-engagement-with-microsoft-dynamics-365/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/drive-your-business-to-success/ | 301 | 301 redirect | /packages/ | 200 | yes |
| /blog/driving-success-the-role-of-year-end-crm-reviews-in-dynamics-365/ | 301 | 301 redirect | /microsoft-dynamics-365-support-services/ | 200 | yes |
| /blog/dynamics-365-2019-wave2-early-opt-in-now-available/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /blog/dynamics-365-2026-release-wave-1-what-sales-and-service-teams-should-pay-attention-to/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /blog/dynamics-365-cure-for-team-chaos/ | 301 | 301 redirect | /power-platform-dynamics-365/ | 200 | yes |
| /blog/dynamics-365-customer-buying-journey/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /blog/dynamics-365-customization-for-growing-business-needs/ | 301 | 301 redirect | /blog/dynamics-365-customizations-worth-it/ | 200 | yes |
| /blog/dynamics-365-licensing-and-pricing-made-easy/ | 301 | 301 redirect | /blog/dynamics-365-pricing-licensing-2025-guide/ | 200 | yes |
| /blog/dynamics-365-new-features-visual-process-designer/ | 301 | 301 redirect | /blog/business-process-flows-purpose-modify-and-extend/ | 200 | yes |
| /blog/dynamics-365-now-more-than-ever/ | 301 | 301 redirect | /power-platform-dynamics-365/ | 200 | yes |
| /blog/dynamics-365-october-2018-release-overview/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /blog/dynamics-365-optimization/ | 301 | 301 redirect | /blog/dynamics-365-optimization-overbuilt-crm/ | 200 | yes |
| /blog/dynamics-365-pricing-changes-bring-an-opportunity-to-reduce-costs/ | 301 | 301 redirect | /blog/dynamics-365-pricing-licensing-2025-guide/ | 200 | yes |
| /blog/dynamics-365-sales-project-milestones/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /blog/dynamics-365-the-cure-for-team-chaos/ | 301 | 301 redirect | /power-platform-dynamics-365/ | 200 | yes |
| /blog/dynamics-365-unified-interface/ | 301 | 301 redirect | /blog/basic-dynamics-365-navigation/ | 200 | yes |
| /blog/easily-create-surveys-in-microsoft-forms-pro/ | 301 | 301 redirect | /blog/blog-customer-voice-survey-guide/ | 200 | yes |
| /blog/easily-create-surveys-microsoft-forms-pro/ | 301 | 301 redirect | /blog/blog-customer-voice-survey-guide/ | 200 | yes |
| /blog/eliminate-content-silos-with-a-custom-dynamics-365-content-management-system/ | 301 | 301 redirect | /dynamics-365-power-apps/ | 200 | yes |
| /blog/eliminate-the-guesswork-with-sales-forecasting-part-1/ | 301 | 301 redirect | /blog/boost-forecast-accuracy-with-product-catalog-and-quotes-in-dynamics-365/ | 200 | yes |
| /blog/eliminate-the-guesswork-with-sales-forecasting-part-2/ | 301 | 301 redirect | /blog/boost-forecast-accuracy-with-product-catalog-and-quotes-in-dynamics-365/ | 200 | yes |
| /blog/email-marketing-best-practices-2025-clickdimensions/ | 301 | 301 redirect | /blog/email-marketing-best-practices-clickdimensions/ | 200 | yes |
| /blog/encloud9-adds-another-microsoft-certification-to-their-toolbox/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /blog/encloud9-bridges-sales-marketing-gap-with-inogics-mailchimp-dynamics-365-crm-integration/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/encloud9-crm-consultants-earns-silver-cloud-customer-relationship-management-competency-for-seventh-year/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /blog/encloud9-helps-companies-return-to-work-safely/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/encloud9-helps-digital-transformation/ | 301 | 301 redirect | /packages/ | 200 | yes |
| /blog/encloud9-moves-into-elevator-coworking-space/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /blog/encloud9-partners-with-clickdimensions-to-launch-powerpack-revolutionizing-sales-and-marketing-for-smbs/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/encloud9-recognized-as-a-2024-top-member-by-crm-software-blog/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /blog/encloud9-socialcrm-consultants-achieves-silver-cloud-crm-competency-from-microsoft/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /blog/encloud9s-top-new-features-in-dynamics-365-sales-2024-release-wave-2/ | 301 | 301 redirect | /blog/ai-selling-dynamics-365-sales/ | 200 | yes |
| /blog/end-the-year-on-a-high-note-with-this-sales-checklist/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/enhanced-timeline-features-power-improvement-to-dynamics-365-customer-service/ | 301 | 301 redirect | /blog/learn-the-basics-of-the-customer-service-hub-in-dynamics-365/ | 200 | yes |
| /blog/exciting-ai-innovations-coming-to-dynamics-365-sales/ | 301 | 301 redirect | /microsoft-copilot-for-business/ | 200 | yes |
| /blog/february-webinar-three-flows-to-charge-up-your-sales/ | 301 | 301 redirect | /blog/an-introduction-to-the-microsoft-power-platform/ | 200 | yes |
| /blog/forgotten-features-of-dynamics-365-part-6-boost-reliability-in-dynamics-365-sales-with-quoting/ | 301 | 301 redirect | /blog/boost-forecast-accuracy-with-product-catalog-and-quotes-in-dynamics-365/ | 200 | yes |
| /blog/four-takeaways-microsoft-business-forward-event/ | 301 | 301 redirect | /blog/microsoft-ignite-2025-copilot-ai-agents-work-iq/ | 200 | yes |
| /blog/from-reactive-support-to-proactive-service-agentic-ai-in-dynamics-365-customer-service/ | 301 | 301 redirect | /blog/agentic-ai-dynamics-365-customer-service/ | 200 | yes |
| /blog/gdpr-dynamics-365-pathway-to-compliance/ | 301 | 301 redirect | /blog/anticipated-arrival-wave-1-2024-introduces-consent-management-in-dynamics-365-customer-insights/ | 200 | yes |
| /blog/get-paid-faster-and-sell-more-with-dynamics-365-credit-card-processing/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/get-started-quickly-with-dynamics-365-for-free/ | 301 | 301 redirect | /blog/getting-started-with-dynamics-365-sales/ | 200 | yes |
| /blog/harnessing-the-power-of-assignment-rules-in-dynamics-365-a-key-to-enhanced-lead-conversion/ | 301 | 301 redirect | /blog/mastering-assignment-rule-configuration-in-dynamics/ | 200 | yes |
| /blog/help-your-sales-team-stay-productive-anywhere-with-the-dynamics-365-sales-mobile-app/ | 301 | 301 redirect | /blog/dynamics-365-sales-mobile-app/ | 200 | yes |
| /blog/highlights-of-the-2021-dynamics-365-release-wave-1/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /blog/highlights-of-the-2021-microsoft-power-platform-release-wave-1/ | 301 | 301 redirect | /microsoft-power-platform/ | 200 | yes |
| /blog/highlights-of-the-2022-dynamics-365-release-wave-1/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /blog/highlights-of-the-power-platform-2022-release-wave-1/ | 301 | 301 redirect | /microsoft-power-platform/ | 200 | yes |
| /blog/how-encloud9-transformed-a-sales-team-with-iterative-dynamics-365-development/ | 301 | 301 redirect | /about-encloud9/microsoft-dynamics-365-success/ | 200 | yes |
| /blog/how-hubspot-dynamics-365-integration-solves-the-sales-marketing-disconnect/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/how-sales-copilot-can-boost-your-productivity-and-performance/ | 301 | 301 redirect | /microsoft-copilot-for-business/ | 200 | yes |
| /blog/how-to---use-customer-voice-for-a-contact-us-form/ | 301 | 301 redirect | /blog/how-to-use-customer-voice-for-a-contact-us-form/ | 200 | yes |
| /blog/how-to-clean-up-crm-data-with-bulk-delete-in-dynamics-365/ | 301 | 301 redirect | /blog/spring-cleaning-your-crm-a-guide-to-refreshing-data-in-dynamics-365/ | 200 | yes |
| /blog/importance-slas-choosing-crm/ | 301 | 301 redirect | /microsoft-dynamics-365-support-services/ | 200 | yes |
| /blog/increase-productivity-with-dynamics-365-app-for-outlook-webinar/ | 301 | 301 redirect | /blog/dynamics-365-app-for-outlook-basics/ | 200 | yes |
| /blog/increase-productivity-with-dynamics-365-for-outlook-app/ | 301 | 301 redirect | /blog/dynamics-365-app-for-outlook-basics/ | 200 | yes |
| /blog/increase-productivity-with-dynamics365-app-for-outlook-webinar/ | 301 | 301 redirect | /blog/dynamics-365-app-for-outlook-basics/ | 200 | yes |
| /blog/information-discovery-made-easier-with-new-search-experience-in-model-driven-apps/ | 301 | 301 redirect | /blog/dataverse-search-dynamics-365-tips/ | 200 | yes |
| /blog/is-your-dynamics-365-ready-for-q2-a-practical-dynamics-365-readiness-check/ | 301 | 301 redirect | /blog/dynamics-365-readiness-check/ | 200 | yes |
| /blog/its-time-to-embrace-the-unified-interface/ | 301 | 301 redirect | /blog/basic-dynamics-365-navigation/ | 200 | yes |
| /blog/january-webinar-increase-productivity-with-the-dynamics-365-app-for-outlook/ | 301 | 301 redirect | /blog/dynamics-365-app-for-outlook-basics/ | 200 | yes |
| /blog/july-webinar-enhanced-filtering-in-dynamics-365/ | 301 | 301 redirect | /blog/user-experience-made-easier-with-enhanced-filtering/ | 200 | yes |
| /blog/june-webinar-credit-card-processing-with-dynamics-365/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/last-call-for-on-prem-crm-why-the-ews-retirement-matters-more-than-you-think/ | 301 | 301 redirect | /blog/ews-retirement-on-premises-crm/ | 200 | yes |
| /blog/leveraging-dynamics-365-analytics-for-springtime-decision-making/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/main-takeaways-from-microsoft-inspire-2020/ | 301 | 301 redirect | /blog/microsoft-ignite-2025-copilot-ai-agents-work-iq/ | 200 | yes |
| /blog/managing-and-marketing-teams-live-events-part-2/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/managing-and-marketing-teams-live-events/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/mastering-the-dynamics-365-sales-cycle-part-2/ | 301 | 301 redirect | /blog/lead-to-opportunity/ | 200 | yes |
| /blog/maximize-your-social-roi-with-clickdimensions-social-engagement/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/may-webinar-sms-messaging-in-dynamics-365/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/meet-the-women-of-encloud9/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /blog/microsoft-announces-deprecation-of-the-dynamics365-outlook-com-add-in/ | 301 | 301 redirect | /blog/dynamics-365-app-for-outlook-basics/ | 200 | yes |
| /blog/microsoft-announces-the-release-of-three-sales-premium-capabilities-to-sales-enterprise-customers/ | 301 | 301 redirect | /blog/our-top-10-dynamics-365-sales-insights-features/ | 200 | yes |
| /blog/microsoft-flow-re-branded-to-power-automate/ | 301 | 301 redirect | /blog/an-introduction-to-the-microsoft-power-platform/ | 200 | yes |
| /blog/microsoft-ignite-2025-top-5-ai-agent-updates/ | 301 | 301 redirect | /blog/microsoft-ignite-2025-copilot-ai-agents-work-iq/ | 200 | yes |
| /blog/microsoft-inspire-2019-bring-dynamics-365-pricing-changes-and-new-features-for-teams/ | 301 | 301 redirect | /blog/dynamics-365-pricing-licensing-2025-guide/ | 200 | yes |
| /blog/microsoft-power-platform-low-code-leader-2025/ | 301 | 301 redirect | /microsoft-power-platform/ | 200 | yes |
| /blog/microsoft-releases-teams-changes-group-chat-forever/ | 301 | 301 redirect | /blog/microsoft-teams-chat-24-things-you-probably-didnt-know-you-can-do/ | 200 | yes |
| /blog/microsoft-teams-adds-new-virtual-experiences/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/microsoft-teams-pro-adds-advanced-webinar-features/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/microsoft-to-reveal-2022-release-wave-1-plans/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /blog/microsofts-new-focus-to-beat-salesforce/ | 301 | 301 redirect | /blog/10-game-changing-reasons-to-choose-microsoft-dynamics-365-over-salesforce/ | 200 | yes |
| /blog/mobilize-your-business-processes-with-dynamics-365-mobile/ | 301 | 301 redirect | /blog/dynamics-365-sales-mobile-app/ | 200 | yes |
| /blog/msps-looking-for-a-dynamics-365-partner | 301 | 301 redirect | /blog/msps-looking-for-a-dynamics-365-partner-2/ | 200 | yes |
| /blog/navigating-the-customer-service-hub-in-dynamics-365/ | 301 | 301 redirect | /blog/learn-the-basics-of-the-customer-service-hub-in-dynamics-365/ | 200 | yes |
| /blog/new-power-platform-features-coming-soon/ | 301 | 301 redirect | /microsoft-power-platform/ | 200 | yes |
| /blog/new-sequence-designer-in-dynamics-365-sales-is-now-available-for-early-access/ | 301 | 301 redirect | /blog/creating-and-managing-sequences-in-dynamics-365-sales-insights/ | 200 | yes |
| /blog/nurturing-customer-loyalty-dynamics-365-crm-essentials/ | 301 | 301 redirect | /dynamics-365-customer-service/ | 200 | yes |
| /blog/optimizing-personalized-engagement-with-dynamics-365/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/personalization-at-scale-with-ai-transforming-customer-engagement-with-dynamics-365/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/phase-2-when-crm-really-makes-an-impact/ | 301 | 301 redirect | /microsoft-dynamics-365-support-services/ | 200 | yes |
| /blog/power-apps-price-changes-signal-new-era-for-low-code-application-development/ | 301 | 301 redirect | /dynamics-365-power-apps/ | 200 | yes |
| /blog/quick-update-dynamics-365-plan-name-changes/ | 301 | 301 redirect | /dynamics-365-licensing/ | 200 | yes |
| /blog/recovering-from-a-failed-crm-project/ | 301 | 301 redirect | /encloud9-dynamics-365-crm-services/dynamics-365-crm-solutions-rescue-repair/ | 200 | yes |
| /blog/revolutionize-your-workflow-dynamics-365-and-microsoft-integration/ | 301 | 301 redirect | /microsoft-power-platform/ | 200 | yes |
| /blog/revolutionizing-sales-teams-how-microsoft-sales-copilot-is-changing-the-game/ | 301 | 301 redirect | /microsoft-copilot-for-business/ | 200 | yes |
| /blog/see-the-power-of-clickdimensions-campaign-automations/ | 301 | 301 redirect | /blog/everything-you-wanted-to-know-about-clickdimensions/ | 200 | yes |
| /blog/sell-smarter-with-dynamics-365-sales/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /blog/send-and-analyze-quizzes-surveys-in-microsoft-forms-pro/ | 301 | 301 redirect | /blog/blog-customer-voice-survey-guide/ | 200 | yes |
| /blog/september-webinar-10-dynamics-365-best-practices-and-hacks/ | 301 | 301 redirect | /blog/8-dynamics-365-tricks-to-skyrocket-your-productivity/ | 200 | yes |
| /blog/service-principal-profiles-in-power-bi-embedded-now-generally-available/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/six-reasons-need-crm-microsoft-dynamics-right-choice/ | 301 | 301 redirect | /blog/13-signs-that-your-crm-sucks/ | 200 | yes |
| /blog/smarter-lead-prioritization-ai-scoring-comes-to-dynamics-365-sales-in-2024-release-wave-2/ | 301 | 301 redirect | /blog/dynamics-365-sales-qualification-agent/ | 200 | yes |
| /blog/spring-renewal-dynamics-365-strategies-for-sales-pipeline-optimization/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /blog/spring-renewal-revitalizing-stale-leads-with-dynamics-365-insights/ | 301 | 301 redirect | /blog/mastering-lead-management-in-dynamics-365-igniting-your-sales-pipeline/ | 200 | yes |
| /blog/stop-making-these-dynamics-365-mistakes/ | 301 | 301 redirect | /blog/5-mistakes-we-keep-seeing-in-first-time-dynamics-365-implementations/ | 200 | yes |
| /blog/success_stories/bg-landholdings-strengthens-data-quality-and-email-deliverability-with-encloud9-email-verifier/ | 301 | 301 redirect | /stories/bg-landholdings/ | 200 | yes |
| /blog/success_stories/bg-peterson-ss/ | 301 | 301 redirect | /stories/bg-peterson/ | 200 | yes |
| /blog/success_stories/clinical-reference-laboratories-optimizes-processes-and-improves-efficiency-with-dynamics-365-customer-service/ | 301 | 301 redirect | /stories/clinical-reference-laboratories/ | 200 | yes |
| /blog/success_stories/collaborative-for-children-success-story/ | 301 | 301 redirect | /stories/collaborative-for-children/ | 200 | yes |
| /blog/success_stories/dynamics-365-implementation-allows-sales-and-management-teams-to-work-more-productively/ | 301 | 301 redirect | /stories/bsi/ | 200 | yes |
| /blog/success_stories/elmwood-reclaimed-timber-migrating-a-20-year-old-crm-to-the-cloud/ | 301 | 301 redirect | /stories/elmwood-reclaimed-timber/ | 200 | yes |
| /blog/success_stories/encloud9-enables-design-company-to-work-more-productively-and-efficiently-after-digitally-transforming-various-processes/ | 301 | 301 redirect | /stories/ppc-flex/ | 200 | yes |
| /blog/success_stories/encloud9-helps-professional-employer-organization-peo-rescue-a-failed-crm/ | 301 | 301 redirect | /stories/aureon/ | 200 | yes |
| /blog/success_stories/hogans-crm-rescue-story-a-fresh-start-with-dynamics-365/ | 301 | 301 redirect | /stories/hogan-assessments/ | 200 | yes |
| /blog/success_stories/how-compana-and-encloud9-expanded-customer-engagement-with-dynamics-365-and-copilot-studio/ | 301 | 301 redirect | /stories/compana/ | 200 | yes |
| /blog/success_stories/how-milestone-leasing-optimized-dynamics-365-to-support-sales-and-lease-renewals/ | 301 | 301 redirect | /stories/milestone-leasing/ | 200 | yes |
| /blog/success_stories/how-price-mds-transformed-healthcare-operations-with-dynamics-365/ | 301 | 301 redirect | /stories/pricemds/ | 200 | yes |
| /blog/success_stories/investment-firm-uses-dynamics-365-mobile-to-stay-connected/ | 301 | 301 redirect | /stories/rlh/ | 200 | yes |
| /blog/success_stories/iowa-braille-school/ | 301 | 301 redirect | /about-encloud9/microsoft-dynamics-365-success/ | 200 | yes |
| /blog/success_stories/jasco-modernizes-operations-with-dynamics-365-sales-and-customer-service/ | 301 | 301 redirect | /stories/jasco/ | 200 | yes |
| /blog/success_stories/kbg-technologies-enhances-sales-processes-with-dynamics-365-implementation-by-encloud9/ | 301 | 301 redirect | /stories/kbg-technologies/ | 200 | yes |
| /blog/success_stories/manufacturer-integrates-website-with-crm-to-automate-lead-assignment/ | 301 | 301 redirect | /stories/jwc/ | 200 | yes |
| /blog/success_stories/manufacturing-company-upgrades-to-dynamics-365-transforms-sales-process/ | 301 | 301 redirect | /stories/rei/ | 200 | yes |
| /blog/success_stories/miles-christi-encloud9-digitally-transforms-non-profit/ | 301 | 301 redirect | /stories/miles-christi/ | 200 | yes |
| /blog/success_stories/msa-source-transforms-compliance-operations-with-encloud9s-tailored-solutions/ | 301 | 301 redirect | /stories/msa-source/ | 200 | yes |
| /blog/success_stories/streamlining-sales-processes-the-schiff-groups-transformation-with-dynamics-365-by-encloud9/ | 301 | 301 redirect | /stories/schiff-group/ | 200 | yes |
| /blog/success_stories/tension-pa-tension-packaging-expands-collaboration-with-encloud9-across-multiple-divisions/ | 301 | 301 redirect | /stories/tension-packaging/ | 200 | yes |
| /blog/success_stories/tension-ss/ | 301 | 301 redirect | /stories/tension-operations/ | 200 | yes |
| /blog/success_stories/world-import-distributors/ | 301 | 301 redirect | /stories/world-import-distributors/ | 200 | yes |
| /blog/take-another-look-at-dynamics-365-mobile-webinar/ | 301 | 301 redirect | /blog/dynamics-365-sales-mobile-app/ | 200 | yes |
| /blog/take-the-plunge-into-the-unified-interface/ | 301 | 301 redirect | /blog/basic-dynamics-365-navigation/ | 200 | yes |
| /blog/the-1-most-important-sales-strategy-building-strong-relationships-with-customers/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/the-data-driven-path-to-crm-success-with-dynamics-365/ | 301 | 301 redirect | /blog/measuring-crm-success-in-dynamics-365-metrics-kpis/ | 200 | yes |
| /blog/the-microsoft-power-platform-powerful-alone-but-better-together/ | 301 | 301 redirect | /microsoft-power-platform/ | 200 | yes |
| /blog/the-microsoft-power-platform-powerful-alone-but-better-together/appid=0aaa3911-df1d-e811-a843-000d3a1bea77&pagetype=entityrecord&etn=en9_encloud9content&id=372f0ab3-fd0b-f011-9988-7c1e521664f7 | 301 | 301 redirect | /microsoft-power-platform/ | 200 | yes |
| /blog/three-flows-to-charge-up-your-sales-webinar/ | 301 | 301 redirect | /blog/an-introduction-to-the-microsoft-power-platform/ | 200 | yes |
| /blog/time-for-a-mid-year-check-on-your-marketing-goals/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/top-5-reasons-dynamics365support-com-is-the-right-managed-service-provider-for-you/ | 301 | 301 redirect | /microsoft-dynamics-365-support-services/ | 200 | yes |
| /blog/top-6-ways-crm-can-shorten-your-sales-cycle/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /blog/transform-your-sales-strategy-with-these-three-easy-habits/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/turn-prospects-into-business-relationships-with-dynamics-365-marketing/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/unifying-sales-and-marketing-with-dynamics-365/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/upcoming-webinar-dont-be-afraid-of-the-unified-interface/ | 301 | 301 redirect | /blog/basic-dynamics-365-navigation/ | 200 | yes |
| /blog/update-cd-today/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /blog/view-now-dynamics-365-for-outlook-app-webinar/ | 301 | 301 redirect | /blog/dynamics-365-app-for-outlook-basics/ | 200 | yes |
| /blog/view-now-dynamics-365-unified-interface-webinar/ | 301 | 301 redirect | /blog/basic-dynamics-365-navigation/ | 200 | yes |
| /blog/visual-solutions-the-power-of-visio-in-encloud9s-customization-approach/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /blog/webinar-april-2020-new-feature-deep-dive-sales-forecasting/ | 301 | 301 redirect | /blog/boost-forecast-accuracy-with-product-catalog-and-quotes-in-dynamics-365/ | 200 | yes |
| /blog/webinars-leads-new-teams-features/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /blog/what-makes-encloud9-different-a-dynamics-365-partner-that-puts-you-first/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /blog/what-the-heck-is-digital-transformation/ | 301 | 301 redirect | /packages/ | 200 | yes |
| /blog/whats-new-and-upcoming-in-dynamics-365-sales/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /blog/whats-new-in-dynamics-365-customer-service-2024-encloud9s-top-features/ | 301 | 301 redirect | /blog/blog-dynamics-365-customer-service-2025/ | 200 | yes |
| /blog/whats-new-in-microsoft-flow/ | 301 | 301 redirect | /blog/an-introduction-to-the-microsoft-power-platform/ | 200 | yes |
| /blog/which-dynamics-365-customizations-are-worth-it-and-which-ones-we-usually-advise-against/ | 301 | 301 redirect | /blog/dynamics-365-customizations-worth-it/ | 200 | yes |
| /blog/why-ongoing-dynamics-365-support-matters/ | 301 | 301 redirect | /microsoft-dynamics-365-support-services/ | 200 | yes |
| /blog/why-you-should-move-your-crm-to-the-cloud-now/ | 301 | 301 redirect | /blog/ews-retirement-on-premises-crm/ | 200 | yes |
| /can-business-benefit-crm/ | 301 | 301 redirect | /power-platform-dynamics-365/ | 200 | yes |
| /category/customer-service/ | 301 | 301 redirect | /dynamics-365-customer-service/ | 200 | yes |
| /clickdimensions-marketing-automation/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /company-need-dynamics-365-crm-administrator/ | 301 | 301 redirect | /blog/company-need-dynamics-365-crm-administrator/ | 200 | yes |
| /contact | 301 | 301 redirect | /contact-us/ | 200 | yes |
| /contacts-2/ | 301 | 301 redirect | /contact-us/ | 200 | yes |
| /copilot-studio/ | 301 | 301 redirect | /microsoft-copilot-studio/ | 200 | yes |
| /crm-2013/16017/ | 301 | 301 redirect | /blog/ | 200 | yes |
| /crm-2013/daily-cloud-news-fri-sept-22-2016/ | 301 | 301 redirect | /blog/ | 200 | yes |
| /crm-cloud-automation-solutions/ | 301 | 301 redirect | /packages/ | 200 | yes |
| /crm-quicktip-adding-global-search-site-map/ | 301 | 301 redirect | /blog/dataverse-search-dynamics-365-tips/ | 200 | yes |
| /divi_overlay/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /divi_overlay/product-service-page-contact-form-pop-up/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /dont-fall-bad-customer-service-trap-6-things-avoid/ | 301 | 301 redirect | /blog/dont-fall-bad-customer-service-trap-6-things-avoid/ | 200 | yes |
| /downloads/ | 301 | 301 redirect | /free-guides-and-checks/ | 200 | yes |
| /dynamics-365-2/ | 301 | 301 redirect | /power-platform-dynamics-365/ | 200 | yes |
| /dynamics-365-2/dynamics-365-for-field-service/ | 301 | 301 redirect | /dynamics-365-field-service/ | 200 | yes |
| /dynamics-365-2/dynamics-365-for-project-service-automation/ | 301 | 301 redirect | /dynamics-365-project-operations/ | 200 | yes |
| /dynamics-365-2/dynamics-365-for-sales/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /dynamics-365-2/dynamics-365-pricing/ | 301 | 301 redirect | /dynamics-365-pricing/ | 200 | yes |
| /dynamics-365-crm-gives-construction-companies-competitive-edge/ | 301 | 301 redirect | /blog/dynamics-365-crm-gives-construction-companies-competitive-edge/ | 200 | yes |
| /dynamics-365-crm-makes-managing-law-firm-easy/ | 301 | 301 redirect | /blog/dynamics-365-crm-makes-managing-law-firm-easy/ | 200 | yes |
| /dynamics-365-crm-quicktips-some-shortcomings-of-crm-calculated-fields/ | 301 | 301 redirect | /blog/ | 200 | yes |
| /dynamics-365-customer-buying-journey/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /dynamics-365-for-field-service/ | 301 | 301 redirect | /dynamics-365-field-service/ | 200 | yes |
| /dynamics-365-for-project-service-automation/ | 301 | 301 redirect | /dynamics-365-project-operations/ | 200 | yes |
| /dynamics-365-for-sales/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /dynamics-365-marketing-automation-with-clickdimensions/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /dynamics-365-marketing-services/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /dynamics-365-new-features-editable-grids/ | 301 | 301 redirect | /blog/managing-views-in-dynamics-365/ | 200 | yes |
| /dynamics-365-new-features-visual-process-designer/ | 301 | 301 redirect | /blog/business-process-flows-purpose-modify-and-extend/ | 200 | yes |
| /dynamics-365-old/ | 301 | 301 redirect | /power-platform-dynamics-365/ | 200 | yes |
| /dynamics-365-partner-fort-worth/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /dynamics-365-project-service-automation/ | 301 | 301 redirect | /dynamics-365-project-operations/ | 200 | yes |
| /dynamics-365-quicktip-use-competitors/ | 301 | 301 redirect | /blog/dynamics-365-quicktip-use-competitors/ | 200 | yes |
| /dynamics-365-rescue-repair/ | 301 | 301 redirect | /encloud9-dynamics-365-crm-services/dynamics-365-crm-solutions-rescue-repair/ | 200 | yes |
| /dynamics-365-services | 301 | 301 redirect | /packages/ | 200 | yes |
| /dynamics-365/ | 301 | 301 redirect | /power-platform-dynamics-365/ | 200 | yes |
| /dynamics-365/can-business-benefit-crm/ | 301 | 301 redirect | /power-platform-dynamics-365/ | 200 | yes |
| /dynamics-365/dynamics-365-business-central/ | 301 | 301 redirect | /dynamics-365-business-central/ | 200 | yes |
| /dynamics-365/dynamics-365-for-customer-service/ | 301 | 301 redirect | /dynamics-365-customer-service/ | 200 | yes |
| /dynamics-365/dynamics-365-for-field-service/ | 301 | 301 redirect | /dynamics-365-field-service/ | 200 | yes |
| /dynamics-365/dynamics-365-for-marketing/ | 301 | 301 redirect | /dynamics-365-customer-insights/ | 200 | yes |
| /dynamics-365/dynamics-365-for-project-service-automation/ | 301 | 301 redirect | /dynamics-365-project-operations/ | 200 | yes |
| /dynamics-365/dynamics-365-for-sales/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /dynamics-365/dynamics-365-new-feature-extending-crm-lob-apps-powerapps/ | 301 | 301 redirect | /dynamics-365-power-apps/ | 200 | yes |
| /dynamics-365/dynamics-365-pricing/ | 301 | 301 redirect | /dynamics-365-pricing/ | 200 | yes |
| /dynamics-365/dynamics-crm-personal-history/ | 301 | 301 redirect | /blog/ | 200 | yes |
| /dynamics-365/encloud9-implements-dynamics-365-small-businesses/ | 301 | 301 redirect | /blog/how-dynamics-365-solves-common-smb-challenges/ | 200 | yes |
| /dynamics-365/fix-crm-five-problems-lots-solutions/ | 301 | 301 redirect | /blog/13-signs-that-your-crm-sucks/ | 200 | yes |
| /dynamics-365/isnt-time-get-started-dynamics-365 | 301 | 301 redirect | /blog/a-simple-guide-to-microsoft-dynamics-365/ | 200 | yes |
| /dynamics-365/quicktip-personalizing-your-dynamics-365-crm-home-page/ | 301 | 301 redirect | /blog/configuring-personal-settings-in-dynamics-365-sales/ | 200 | yes |
| /email-marketing-dos-donts/ | 301 | 301 redirect | /blog/email-marketing-best-practices-clickdimensions/ | 200 | yes |
| /encloud9-dynamics-365-crm-services/ | 301 | 301 redirect | /packages/ | 200 | yes |
| /encloud9-dynamics-365-crm-services/microsoft-dynamic-365-crm-accelerators/ | 301 | 301 redirect | /encloud9-dynamics-365-crm-services/microsoft-dynamics-365-crm-accelerators/ | 200 | yes |
| /encloud9-dynamics-365-crm-services/microsoft-dynamics-365-crm-implementation/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /encloud9-dynamics-365-crm-services/microsoft-dynamics-365-support-services/ | 301 | 301 redirect | /microsoft-dynamics-365-support-services/ | 200 | yes |
| /encloud9-helps-digital-transformation/ | 301 | 301 redirect | /packages/ | 200 | yes |
| /encloud9-socialcrm-consultants-achieves-silver-cloud-crm-competency-from-microsoft/ | 301 | 301 redirect | /about-encloud9/ | 200 | yes |
| /encloud9/favorite-new-features-organizational-insights/ | 301 | 301 redirect | /blog/ | 200 | yes |
| /encloud9/keyboard-shortcuts-for-dynamics-365-editable-grids/ | 301 | 301 redirect | /blog/managing-views-in-dynamics-365/ | 200 | yes |
| /encloud9s-favorite-4-new-features-of-the-dynamics-365-july-2017-update/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /encloud9s-friday-5-march-3/ | 301 | 301 redirect | /blog/ | 200 | yes |
| /end-the-year-on-a-high-note-with-this-sales-checklist/ | 410 | 410 Gone | (none, stays on the address) | 410 | n/a |
| /fix-crm-five-problems-lots-solutions/ | 301 | 301 redirect | /blog/13-signs-that-your-crm-sucks/ | 200 | yes |
| /four-takeaways-microsoft-business-forward-event/ | 301 | 301 redirect | /blog/microsoft-ignite-2025-copilot-ai-agents-work-iq/ | 200 | yes |
| /gdpr-dynamics-365-pathway-to-compliance/ | 301 | 301 redirect | /blog/anticipated-arrival-wave-1-2024-introduces-consent-management-in-dynamics-365-customer-insights/ | 200 | yes |
| /highlights-dynamics-365-spring-2018-update/ | 301 | 301 redirect | /blog/dynamics-365-2026-release-wave-1/ | 200 | yes |
| /home/ | 301 | 301 redirect | / | 200 | yes |
| /how-accounting-firms-can-benefit-from-microsoft-dynamics-365-crm/ | 301 | 301 redirect | /blog/how-accounting-firms-can-benefit-from-microsoft-dynamics-365-crm/ | 200 | yes |
| /how-microsoft-dynamics-365-crm-can-benefit-the-healthcare-industry-or-boost-your-healthcare-services-with-dynamics-365-crm/ | 301 | 301 redirect | /blog/how-microsoft-dynamics-crm-benefits-healthcare/ | 200 | yes |
| /how-microsoft-dynamics-crm-benefits-healthcare/ | 301 | 301 redirect | /blog/how-microsoft-dynamics-crm-benefits-healthcare/ | 200 | yes |
| /how-microsoft-dynamics-crm-can-benefit-healthcare/ | 301 | 301 redirect | /blog/how-microsoft-dynamics-crm-benefits-healthcare/ | 200 | yes |
| /https/wwwencloud9com/blog/10-easy-ways-to-obtain-more-leads-without-doing-paid-ads/ | 301 | 301 redirect | /blog/10-easy-ways-to-obtain-more-leads-without-doing-paid-ads/ | 200 | yes |
| /hubspot-implementation/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /hubspot-support-services/ | 301 | 301 redirect | /microsoft-dynamics-365-support-services/ | 200 | yes |
| /hubspot/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /hubspot/commerce-hub/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /hubspot/content-hub/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /hubspot/marketing-hub/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /hubspot/operations-hub/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /hubspot/sales-hub/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /hubspot/service-hub/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /index.php | 301 | 301 redirect | / | 200 | yes |
| /lp/crm-for-professional-services/ | 301 | 301 redirect | /dynamics-365-professional-services/ | 200 | yes |
| /lp/dataverse-storage-analysis/ | 301 | 301 redirect | /dataverse-storage-analysis/ | 200 | yes |
| /lp/dynamics-365-crm-cleanup-checklist/ | 301 | 301 redirect | /crm-cleanup-checklist/ | 200 | yes |
| /lp/dynamics-365-sales-management-guide/ | 301 | 301 redirect | /dynamics-365-sales-management-guide/ | 200 | yes |
| /lp/healthcare-crm-software-dynamics-365/ | 301 | 301 redirect | /dynamics-365-healthcare/ | 200 | yes |
| /lp/microsoft-dynamics-365-hubspot-crm-migration/ | 301 | 301 redirect | /hubspot-to-dynamics-365/ | 200 | yes |
| /lp/microsoft-dynamics-365-partner-austin/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /lp/microsoft-dynamics-365-partner-boston/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /lp/microsoft-dynamics-365-partner-charlotte/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /lp/microsoft-dynamics-365-partner-san-antonio/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /lp/microsoft-dynamics-365-partner-seattle/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /lp/monday-to-dynamics-365-migration/ | 301 | 301 redirect | /monday-to-dynamics-365/ | 200 | yes |
| /lp/unleash-dynamics-365-sales/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /marketing-accelerator-now/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /marketing-accelerator-old/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /marketing-accelerator/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /microsoft-announces-integration-plans-linkedin/ | 301 | 301 redirect | /blog/ | 200 | yes |
| /microsoft-dynamic-365-crm-accelerators/ | 301 | 301 redirect | /encloud9-dynamics-365-crm-services/microsoft-dynamics-365-crm-accelerators/ | 200 | yes |
| /microsoft-dynamics-365-consulting-for-colorado/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-crm-licensing/ | 301 | 301 redirect | /dynamics-365-licensing/ | 200 | yes |
| /microsoft-dynamics-365-partner-akron-ohio/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-augusta/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-baltimore/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-cleveland-ohio/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-columbus-georgia/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-connecticut/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-dallas/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-dayton-ohio/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-denver/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-el-paso/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-for-springfield-businesses/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-georgia/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-houston/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-iowa/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-jacksonville/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-kansas/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-knoxville-tn/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-las-vegas/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-louisiana/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-macon-georgia/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-maryland/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-michigan/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-milwaukee/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-minneapolis/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-minnesota/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-missouri/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-nebraska/ | 301 | 301 redirect | /microsoft-dynamics-365-partner-omaha/ | 200 | yes |
| /microsoft-dynamics-365-partner-new-mexico/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-new-york/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-north-carolina/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-ohio/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-portland-maine/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-rochester/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-south-carolina/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-st-louis/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-toledo-ohio/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-virginia/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-partner-washington/ | 301 | 301 redirect | /microsoft-dynamics-365-implementation/ | 200 | yes |
| /microsoft-dynamics-365-salesforce-crm-migration/ | 301 | 301 redirect | /salesforce-to-dynamics-365/ | 200 | yes |
| /microsoft-dynamics-365-vs-salesforce/ | 301 | 301 redirect | /blog/10-game-changing-reasons-to-choose-microsoft-dynamics-365-over-salesforce/ | 200 | yes |
| /microsoft-dynamics-365-zoho-crm-migration/ | 301 | 301 redirect | /zoho-to-dynamics-365/ | 200 | yes |
| /microsoft-dynamics-crm/clickdimensions-october-release/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /microsoft-dynamics-crm/dynamics-365-new-features-editable-grids/ | 301 | 301 redirect | /blog/managing-views-in-dynamics-365/ | 200 | yes |
| /microsoft-dynamics-crm/importance-slas-choosing-crm/ | 301 | 301 redirect | /microsoft-dynamics-365-support-services/ | 200 | yes |
| /microsoft-dynamics-crm/six-reasons-need-crm-microsoft-dynamics-right-choice/ | 301 | 301 redirect | /blog/13-signs-that-your-crm-sucks/ | 200 | yes |
| /microsoft-dynamics-crm/survey-says-another-satisfied-customer/ | 301 | 301 redirect | /about-encloud9/microsoft-dynamics-365-success/ | 200 | yes |
| /ms-power-platform/ | 301 | 301 redirect | /microsoft-power-platform/ | 200 | yes |
| /multiple-account-salesperson-scenarios-dynamics-365/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /new-features-dynamics-365-data-storage/ | 301 | 301 redirect | /dataverse-storage-analysis/ | 200 | yes |
| /power-bi/ | 301 | 301 redirect | /microsoft-power-bi/ | 200 | yes |
| /products/ | 301 | 301 redirect | /packages/ | 200 | yes |
| /quick-update-dynamics-365-plan-name-changes/ | 301 | 301 redirect | /dynamics-365-licensing/ | 200 | yes |
| /quicktip-simple-personal-navigation-in-dynamics-365/ | 301 | 301 redirect | /blog/basic-dynamics-365-navigation/ | 200 | yes |
| /quicktip-updating-to-the-latest-dynamics-365-for-outlook-client/ | 301 | 301 redirect | /blog/dynamics-365-app-for-outlook-basics/ | 200 | yes |
| /sales-accelerator-get-started/ | 301 | 301 redirect | /dynamics-365-sales-accelerator/ | 200 | yes |
| /sales-accelerator/ | 301 | 301 redirect | /dynamics-365-sales-accelerator/ | 200 | yes |
| /service/dynamics-crm-for-sales-teams-2/ | 301 | 301 redirect | /packages/ | 200 | yes |
| /services-solutions/social-media-mananagement/ | 301 | 301 redirect | /marketing-services/ | 200 | yes |
| /services/crm-health-check/ | 301 | 301 redirect | /blog/what-a-healthy-dynamics-365-system-actually-looks-like/ | 200 | yes |
| /stories/ | 301 | 301 redirect | /about-encloud9/microsoft-dynamics-365-success/ | 200 | yes |
| /success-stories | 301 | 301 redirect | /about-encloud9/microsoft-dynamics-365-success/ | 200 | yes |
| /success_stories/ | 301 | 301 redirect | /about-encloud9/microsoft-dynamics-365-success/ | 200 | yes |
| /thank-you-customer-journey/ | 301 | 301 redirect | /dynamics-365-sales/ | 200 | yes |
| /thank-you-microsoft-dynamics-365-vs-salesforce/ | 301 | 301 redirect | /blog/10-game-changing-reasons-to-choose-microsoft-dynamics-365-over-salesforce/ | 200 | yes |
| /what-the-heck-is-digital-transformation/ | 301 | 301 redirect | /packages/ | 200 | yes |
