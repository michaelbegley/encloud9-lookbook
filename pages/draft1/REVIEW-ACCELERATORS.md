# Review: Sales Accelerator and Service Accelerator pages, Draft 1 to Draft 2 (9 Nov 2026)

Pages: pages/nine-sales-accelerator.html, pages/nine-service-accelerator.html. Copy: project docs PAGE-SALES-ACCELERATOR.md and PAGE-SERVICE-ACCELERATOR.md (4 Nov), changes listed in SPEC-*-NOTES.md here.
Frozen Draft 1: nine-sales-accelerator-D1.html (25978c9d...), nine-service-accelerator-D1.html (793d90a1...).

## Scores (Draft 1 independent reviewer; Draft 2 Claude's re-score, not independent)
- Sales Accelerator: 28 to 31 of 32.
- Service Accelerator: 21 to 30 of 32.

## Fact check (agents, 9 Nov)
Confirmed and unchanged since 4 Nov: Sales $65/$105/$150; Copilot in Sales Enterprise and Premium only; Premium 1,000 Copilot Credits; Microsoft's own "sales accelerator" feature; Customer Service $50/$105/$195; Copilot in Customer Service Enterprise and Premium only; plan split; Azure Communication Services separate; four service agents; Premium base credit capacity (no amount); Case Management and Customer Intent agents need pay-as-you-go on Azure; license plus security role; Schiff (Rockville MD, one month); KBG (Memphis TN, within two months, QuickBooks before); Compana (St. Louis, Sales, Customer Service, Copilot Studio, Shopify work); PriceMDs (Clearwater FL, replaced Monday CRM).
Corrected: Compana "in early testing" is not in the story (removed). PriceMDs story does not describe case or queue work (card claims only the products).
New on Microsoft's pricing page (could not determine if new since 4 Nov): Copilot Credits "require an Azure subscription to use agents".

## Fixed in Draft 2
1. Service page: a splicing error left two duplicate proof cells and a stray closing div, so sections lost their side margins (same bug as Full implementation D1). Removed. Cause: replacing a block by searching for the first closing div inside nested markup. Fix to the process: the page check script now fails if section left edges differ.
2. Stage C on all three build packages (Full implementation, both accelerators): "Training and cut-over day. Copilot is switched on if your plan includes it; agents are scoped as a separate pilot" (agents are Not included; Professional plans have no Copilot).
3. Support plan cube labelled "After the package" (it is not included).
4. Story meta and leads: city and state on both cards; the lead names both stories.
5. Proof numbers no longer wrap or overflow on phones (all four package pages).
6. "Other packages" strips in the home page order on all four pages: Full implementation, Rescue and Repair, Sales Accelerator, Service Accelerator, then moves and support.
7. Service: hero cube labels "Built" (voice rule); H1 wraps cleanly on phones.

## Not changed
- "Free checkups, no obligation" keeps linking to the Copilot readiness check (KIT rule 6); a first-time buyer check would be better (reviewer); idea for Brian.
- Final band line stays "a straight answer on which package fits" (no price promised from a free call).

## Open for Brian
Package numbers (weeks, users, limits); knowledge base and email to case in the Service Accelerator; whether we do voice and chat work; a first Customer Service build story; naming Compana and PriceMDs; the four stage names.
