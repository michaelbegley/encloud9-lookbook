# Seed data notes (condensed 10 Nov 2026 from claude/genpages-demo/SEED-README.md, Agent 18, 4 Nov 2026)

All companies, people, emails (example.com) and phones (555) are fictional. No enCloud9 client appears.

Make the CSVs for the demo day first: `python3 make-seed.py YYYY-MM-DD` (it also prints the badge each account and open opportunity should show). Load the day before the demo or the morning of it; activity times are 08:00.

Load order (parents first; lookups match the parent's primary name):
1. 01-accounts.csv, Account, 10 rows
2. 02-contacts.csv, Contact, 20 (Company Name -> Account)
3. 03-opportunities.csv, Opportunity, 15 (Account, Contact). All load open; then close 3 as Won (Driver onboarding forms $12,000, Hygiene recall reminders $18,000, Supplier portal $54,000; Actual Revenue = Est. Revenue; Actual Close Date = the CSV date) and 2 as Lost (Seasonal staffing tracker, Energy usage dashboard).
4. 04-opportunity-products.csv, Opportunity Product, 20 write-in lines (Opportunity)
5. 05-quotes.csv, Quote, 8 (Potential Customer -> Account, Opportunity, Price List). Replace the price list placeholder with a real price list name read from the environment. Approval Status needs the new column.
6. 06-quote-products.csv, Quote Product, 16 (Quote)
7. 07-cases.csv, Case, 5, all open (Customer -> Account). Needs the Case table.
8. 08-tasks.csv, Task, 10 regarding opportunities: 7 Completed with an Actual End, 3 Open (one 2 days overdue: Shop floor scheduling).
9. 09-phone-calls.csv, Phone Call, 10 regarding accounts: 9 Completed, 1 Open. Harbor Lane Bakery has none on purpose.

After loading, check: one completed call and one completed task show Activity Status Completed and Actual End on the CSV date, not today (otherwise every badge is wrong).

Expected on the demo day: Account 360 on Ironwood Fabrication shows Strong (5 days, 0 High), win rate 100% (1 of 1), lifetime won $54,000. Opportunity command center on Shop floor scheduling shows $132,000 (= its two product lines), 50%, Healthy, one open task 2 days overdue in red. Approvals shows 8 Pending quotes, about $420,800 waiting.

Removing the seed data after the demo is a delete: it needs Michael's yes first.
