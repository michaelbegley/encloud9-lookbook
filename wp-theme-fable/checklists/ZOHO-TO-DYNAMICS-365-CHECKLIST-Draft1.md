# Zoho CRM to Dynamics 365 Migration Readiness Checklist
Draft 1 · 23 Nov 2026 · Claude, #17 Facilitator · for review by Michael and Brian before it becomes the download on /zoho-to-dynamics-365/
What to gather and decide before a move to Dynamics 365. Tick each line, then bring it to a short call.

## 1. What you have today
- [ ] How many users log in each week, and who owns each record type.
- [ ] Rough record counts: accounts or companies, contacts, leads, deals or opportunities, activities, cases or tickets.
- [ ] Total data size, if your current CRM shows it.
- [ ] Every system connected to your CRM: email, calendar, accounting, forms, phone, marketing tools.
- [ ] Reports and dashboards people use every week. Mark the ones you would miss on day one.

## 2. Clean before you move
- [ ] Duplicates: pick the rule (same email, same company name) and merge before the move.
- [ ] Old records: decide a cut-off date. Records older than that stay in an export, not in Dynamics 365.
- [ ] Empty or unused fields: list them so they are left behind.
- [ ] Owners: every record has an owner who still works with you.

## 3. Zoho-specific
- [ ] Your Zoho CRM edition and how many users.
- [ ] Modules: the standard ones you use (Leads, Contacts, Accounts, Deals, Activities) and any custom modules.
- [ ] Blueprints and workflow rules: list them. These are rebuilt in Dynamics 365, not copied across.
- [ ] Other Zoho apps tied to your CRM (Books, Desk, Campaigns) and what each one does for you.

## 4. Decide before the move
- [ ] Which Dynamics 365 app: Sales, Customer Service, or both.
- [ ] Who signs off that the moved data is right, and how: spot checks of named records, plus record counts per table.
- [ ] Cut-over: the day the old CRM goes read-only, and how long you keep it after.
- [ ] Training: who learns first, and who answers questions in week one.

## 5. How the data moves
Microsoft sizes CRM data moves like this [M1]:
- Up to 1 GB or fewer than 50,000 records: export to Excel or CSV and use the Dataverse import wizard.
- 1 GB to 50 GB or 50,000 to 500,000 records: an ETL tool such as Azure Data Factory, in batches, tested in a separate environment first.
- More than 50 GB or more than 500,000 records: phased moves with tools such as Azure Data Factory or SSIS, with checks at each phase.

---
Internal, not part of the download:
Sources
- A Microsoft tool for Zoho moves: could not determine one on Microsoft Learn (searched 23 Nov 2026). Moves use the import and ETL routes in M1.
- [M1] Microsoft Learn, "Data migration approaches" (power-platform/architecture/key-concepts/data-migration/data-migration-approaches), checked 23 Nov 2026.
- Zoho module names: Zoho developer docs (zoho.com/crm/developer/docs/api/v8/modules-api.html), from MOVES-ZOHO-MONDAY-NOTES.md, read 9 Nov 2026, not rechecked 23 Nov.
Open
- The download file format (PDF from a doc, or a page) and the form's destination: Michael (launch blocker, the "[Form: ...]" line on the page).
- Wording is Claude's (proposed). Nothing here promises a price, a timeline or what enCloud9 includes; scope stays on the call.
