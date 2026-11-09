# Move from Salesforce and Move from HubSpot pages: copy source and deliberate changes (9 Nov 2026)

Source: project docs claude/site-build/PAGE-SALESFORCE-MOVE.md and PAGE-HUBSPOT-MOVE.md (4 Nov 2026, Agent 18), stage 4 copy. Agents cannot read project docs, so the key facts and every deliberate change are listed here. Both pages are built on the Sales Accelerator Draft 2 shell by one script, so they share structure.

## Spec facts (read 4 Nov 2026)
- Microsoft: Dynamics 365 Sales $65 / $105 / $150 per user per month, paid yearly; Copilot in Enterprise and Premium; Premium 1,000 Copilot Credits per user per month.
- Microsoft Dynamics 365 Activate (preview) assesses a Salesforce org and moves data to Sales and Customer Service; "doesn't convert or migrate flows, Process Builder, workflow rules, and Apex"; preview features "aren't meant for production use". Activate covers Salesforce only. No dedicated Microsoft HubSpot tool found (Learn search).
- Salesforce Sales Cloud (salesforce.com/sales/pricing, 4 Nov): Starter $25 (monthly or annual), Pro $100, Core $195, Advanced $395, Max $550 (billed annually); Agentforce for Sales add-on from $125.
- HubSpot Sales Hub (hubspot.com/pricing/sales, 4 Nov): Starter from $7, Professional from $90, Enterprise from $150 per seat per month; onboarding $1,500 (Pro) and $3,500 (Enterprise), required; page shows two prices for Starter and Pro without saying which billing goes with which.
- Proof: no published client story measures a move from Salesforce or HubSpot. Hogan has a HubSpot integration, not a move. So no story card.
- Checklists: live pages offer a "Migration Readiness Checklist" download form; the file and form destination are not yet supplied.

## Deliberate changes from the spec
1. No package prices (kit rule): price row "Fixed, quoted in writing after a short call"; FAQ Q1 the same.
2. US spelling: licenses. "As part of the move" in the licenses FAQ (spec "As part of setup").
3. Proof strip: no "written up"; spec had 2 cells, page has 4 factual cells ($65 Microsoft list price, 4 stages, 23 stories, $500 support).
4. Stage C uses the accelerator Draft 2 wording ("Copilot is switched on if your plan includes it; agents are scoped as a separate pilot") instead of the spec's older line that promised Copilot and agents. Stage B "We build" (voice rule).
5. "Get the migration checklist" goes to an on-page #checklist section with a bracketed form placeholder until Michael supplies the file and form.
6. The price-table date is written as "checked 4 Nov 2026; we check them again before this page goes live" instead of "[publish date]".
7. Hero cube grid of the included items; mono label "Move" (the hub calls these Package 05 and 06; Brian's package numbers cover 01 to 04 only).
8. Other packages strip in Brian's order (Full implementation, Rescue and Repair, Sales Accelerator, Service Accelerator), then the other move, then Support plans. Links to concept pages.
9. FAQPage JSON-LD leaves out the two answers that still have brackets.
10. The live HubSpot page's outbound link to hubspot.com is dropped (spec).
