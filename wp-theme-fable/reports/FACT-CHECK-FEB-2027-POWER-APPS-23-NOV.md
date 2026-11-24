# Fact check: the February 2027 Power Apps licensing claim (23 Nov 2026)

Checked Mon 23 Nov 2026, about 11:25 PM Central, on Microsoft Learn (Compass via Michael, 10:15 PM). Result: **confirmed. Microsoft says it.** No page edits needed; none made.

## What Microsoft says (measured, Microsoft Learn, read 23 Nov 2026)
- **Power Apps licensing FAQs**, section "Licensing compliance for Power Apps": https://learn.microsoft.com/power-platform/admin/powerapps-licensing-faq#licensing-compliance-for-power-apps
  - Starting February 2027, three areas that were applied leniently need an appropriate premium licence: apps in managed environments, model-driven apps, and custom apps used outside a Dynamics 365 environment context. Users without one can't open the app.
  - Dynamics 365 licences include Power Apps use rights only in the context of, and in the same environment as, the licensed Dynamics 365 app.
- **Licensing requirements for managed environments**, FAQ: https://learn.microsoft.com/power-platform/admin/managed-environment-licensing#faq
  - In-app notices began June 2026; from February 2027 users without an appropriate licence are blocked from opening apps in a managed environment.

## Pages that carry the claim, and how they read against Microsoft
| Page | Our wording (paraphrase) | Against Microsoft |
|---|---|---|
| /dynamics-365-licensing/ | Apps outside the licensed Dynamics 365 context need Power Apps licensing; enforced more strictly from Feb 2027; "From Feb 2027 Stricter checks" tile | Matches |
| /faq/ | Same two answers (licensing and "What changes in February 2027?") | Matches |
| /dynamics-365-power-apps/ | FAQ "What changes in February 2027?": enforcement for apps in managed environments | Matches, but names one of Microsoft's three areas |
| /dynamics-365-license-check/ | The check covers "what Microsoft's stricter Power Apps checks from February 2027 mean for you"; same FAQ; sample finding about custom apps | Matches |
| /free-guides-and-checks/ | License check tile "Before February 2027" | Matches |

## Optional, Claude's call, not done
The "What changes in February 2027?" answer (Power Apps, FAQ and License Check pages) names managed environments only. Microsoft's FAQ lists three areas: managed environments, model-driven apps, and apps used outside a Dynamics 365 environment. A fuller answer would be: "Microsoft starts enforcing Power Apps licensing for apps in managed environments, model-driven apps, and apps used outside a Dynamics 365 environment." That is a wording change on three pages, so it waits for Michael's yes.
