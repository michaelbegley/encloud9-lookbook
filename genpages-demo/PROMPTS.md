# Generative pages demo: the three pages Brian asked for (call with Brian, 9 Nov 2026, 21:29 to 22:23 in the recording)

Brian: "You need to create pages like this. In Dynamics." Then: build "the versions of what your little friend created" in the enCloud9 demo CRM, because "I can't demo this in enCloud9 [production]. It would show client information."
"These three" are the three requests in the generative pages demo on the new Copilot page (https://michaelbegley.github.io/encloud9-lookbook/site/microsoft-copilot-for-business/#genpages): Account 360, Opportunity command center, Approvals. The real pages should match what that demo shows, on fictional seed data (make-seed.py).

Sources for the Microsoft facts: Microsoft Learn "Generate a page using natural language" (generative-pages, last updated 28 Sep 2026) and "Create and edit generative pages with AI code generation tools" (generative-page-external-tools, 18 Sep 2026); Microsoft's power-platform-skills model-apps plugin (/genpage). Re-check both before building; they change.

`<PREFIX>` is the demo environment's publisher prefix. Read it from the environment; never guess it.

## Build order: 3, then 2, then 1
Page 3 is simplest and proves writes; page 2 proves recordId and form embedding; page 1 uses six tables, the in-browser limit.

## Page 3: Approvals (app navigation)
Matches the website demo: "List the quotes waiting for a manager, so I can tick the ones I am happy with and approve them together." Refinement shown on the site: "Sort by days waiting, longest first."

Needs three new columns on Quote in the demo environment only: `<PREFIX>_approvalstatus` (Choice, labels exactly Pending, Approved, Rejected; default Pending), `<PREFIX>_approvedby` (Lookup to User), `<PREFIX>_approvedon` (Date and time).

```
Build an "Approvals" generative page for the app navigation.

Use these Dataverse tables: quote, account, opportunity, systemuser.

Show quotes where <PREFIX>_approvalstatus is Pending in a selectable table with a checkbox on every row and a "select all" checkbox in the header. Columns: quote number, quote name, customer, opportunity, total amount (currency), discount percent (amber over 10 percent, red over 20 percent), and days waiting. Sort by days waiting, longest first.

Above the table: a count of items waiting, the total value waiting, and filters for owner and customer.

Command bar: "Approve" and "Reject" buttons, disabled until at least one row is ticked, showing how many are selected ("Approve 3").
When Approve is selected: ask for confirmation in a non-modal panel inside the page, then for each ticked quote call updateRow on the quote table to set <PREFIX>_approvalstatus to Approved, <PREFIX>_approvedby to the current user, and <PREFIX>_approvedon to now. Run the updates one after another, show progress, and when finished show a success message with the count, and list any rows that failed with the error. Remove approved rows from the list without reloading the whole page.
Reject works the same way but sets <PREFIX>_approvalstatus to Rejected and asks for an optional reason shown in the message.

Clicking a quote number opens the quote record. Friendly empty state "Nothing waiting for approval". Accessible: keyboard selection, visible focus, labelled checkboxes.
```

## Page 2: Account 360 (a tab on the Account main form)
Matches the website demo: "Add a tab to the account form with relationship health and the reason for it, win rate, open pipeline by month, contacts and open cases." Refinement shown on the site: "Put the open cases at the top."

```
Build an "Account 360" generative page to embed on the Account form.
Set up the page to accept an account recordId. When the page loads, use it to fetch the account and its related records. Show a loading state from the first frame.

Use these Dataverse tables: account, opportunity, contact, incident, activitypointer.

Sections, fluid width, light theme that matches Dynamics 365:
1. "Open cases" first: case number, title, priority badge, status, age in days. High priority first. Clicking opens the case.
2. "Customer intelligence" band: account logo, name, industry, city and state, employees, annual revenue. Next to it, four computed tiles:
   - Relationship health: Strong, Steady or At risk, with the reason in one line. At risk if there is no completed activity, the last completed activity is over 45 days ago, or there are 2 or more open High-priority cases; Strong if the last completed activity is under 14 days ago and there are no open High-priority cases; otherwise Steady.
   - Win rate: won opportunities divided by all closed opportunities for this account, with the count.
   - Lifetime won revenue: sum of actualvalue on won opportunities.
   - Last touch: date and subject of the most recent completed activity.
3. "Open pipeline": total estimated value of open opportunities, weighted value (estimatedvalue times closeprobability), and a bar chart of open estimated value by estimated close month for the next 6 months.
4. "Open opportunities" table: name, estimated value, probability, estimated close date (red if past). Sort by close date. Clicking a row opens the opportunity.
5. "Contacts" cards: full name, job title, email, phone, with the primary contact marked. Clicking opens the contact.

Only show active contacts. Select only the columns needed. Read every page of results, never compute totals from the first page alone. Friendly empty states for every section, and "Save the account to see its 360 view." on an unsaved account. Accessible, and readable both on a wide screen and in a narrow form tab.
```

## Page 1: Opportunity command center (the first tab on the Opportunity main form)
Matches the website demo: "Make the first tab on a deal: revenue, a probability ring, stage, products, the activity timeline with overdue follow-ups in red, and the quote." Refinement shown on the site: "Add a risk flag when follow-ups are overdue."

```
Build an "Opportunity command center" generative page for the Opportunity form.
Set up the page to accept an opportunity recordId. When the page loads, use it to fetch the opportunity and its related records. Show a loading state from the first frame.

Use these Dataverse tables: opportunity, account, contact, opportunityproduct, activitypointer, quote.

Layout, top to bottom, fluid width, light theme that matches Dynamics 365:
1. Header band: opportunity name, account name with its logo, status badge, a risk flag, and four large KPI tiles: Estimated revenue (estimatedvalue, currency), Probability (closeprobability as a ring gauge), Days to close (estimatedclosedate minus today, red if past due), and Stage (current sales stage).
   Risk flag: "At risk" with the reason when follow-ups are overdue (open activities past their due date: say how many and the oldest by how many days) or a quote is still waiting for approval; otherwise no flag.
2. A horizontal stage tracker showing the sales stages with the current stage highlighted.
3. Left column: "Deal health" card: green if an activity was completed in the last 14 days and the close date is in the future, amber if the last completed activity was 15 to 30 days ago, red if none in over 30 days, no completed activity, or the close date has passed. Show the reason in one line.
4. Left column: "Products" table from opportunityproduct (product, quantity, price per unit, extended amount) with a total row, and a small bar chart of extended amount by product.
5. Right column: "People" card listing contacts at the account (name, job title, email, phone), each clickable to open the contact record.
6. Right column: "Activity timeline": the 10 most recent activities regarding this opportunity, newest first, with an icon per activity type and overdue open activities in red.
7. Bottom: "Quotes" strip showing each quote for this opportunity with total amount and status.

Every record name is a link that opens the record. Select only the columns needed. Show friendly empty states when a section has no data, and "Save the opportunity to see its command center." on an unsaved opportunity. Accessible, and readable at 1280 px and on a narrow form tab.
```

## Rules that trip people up (from the plugin's rules and troubleshooting, as read 4 Nov 2026; re-read the current versions)
- The host mounts the page twice on open: de-dupe and cache each load per page and per record. All hooks above every early return, or the page crashes on the first open of a record (React error #310).
- Lookup writes use `_<field>_value: "/systemuser(<id>)"`, never `@odata.bind` (silently ignored).
- `ownerid` and `createdon` are left out of the generated RuntimeTypes; the prompts do not use them.
- `activitypointer` through queryTable is untested here: test it first; fall back to task and phonecall.
- Never run the plugin's teardown in an environment where a form embeds a page: it deletes the page.
