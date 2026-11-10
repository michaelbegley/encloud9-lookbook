import json,re
D='2026-11-09'
PR='https://monday.com/crm/pricing'
LIVE='https://www.encloud9.com/lp/monday-to-dynamics-365-migration/'
v=dict(
 file="nine-move-monday.html", url=LIVE, name="Monday.com", crumb="Move from Monday.com", unit="monday.com account",
 title="Move from monday.com to Dynamics 365 Sales | enCloud9",
 meta="We move growing US businesses from monday.com to Dynamics 365 Sales, with boards mapped and checked before go-live, and support from $500 a month.",
 answer="We move growing US businesses from monday CRM to Dynamics 365 Sales: your leads, contacts, accounts, deals and activities, with item counts checked against monday.com before go-live. Moving data from your old CRM or spreadsheets is part of a full implementation. Microsoft licenses are a separate cost, and support plans start at $500 a month.",
 inc_lead="Your monday.com boards, items and columns move to Dynamics 365 Sales, mapped column by column and tested in a trial run before the full move. Automations, integrations and apps in monday.com do not move on their own; we review them first and quote any rebuild separately.",
 inc=["A written review of your monday.com account: boards, groups, columns, automations, integrations and apps",
      "Your monday.com boards and columns mapped to Dynamics 365 Sales",
      "Your monday.com users mapped to Dynamics 365 users and security roles",
      "Your Microsoft licenses assigned to each user",
      "A trial run first, then the full move, with item counts checked against monday.com",
      "Up to [Brian sets] records moved","[Brian sets] training sessions","[Brian sets] days of help after go-live"],
 noinc=["Rebuilding monday.com automations, integrations and apps, quoted separately",
        "Boards outside your CRM, such as project or task boards, quoted separately",
        "Integrations with other systems, quoted separately",
        "Microsoft licenses and Copilot Credits",
        "Ending your monday.com subscription, which stays between you and monday.com"],
 grid=[["Reviewed","Your account","A written review of your monday.com account"],
       ["Mapped","Boards and columns","Your monday.com boards and columns mapped to Dynamics 365 Sales"],
       ["Mapped","Users and roles","Your monday.com users mapped to Dynamics 365 users and security roles"],
       ["Assigned","Licenses","Your Microsoft licenses assigned to each user"]],
 price_h="What do Dynamics 365 Sales and monday CRM cost per user?",
 price_lead="Microsoft lists Dynamics 365 Sales at $65, $105 or $150 per user per month, paid yearly. For monday CRM, monday.com lists Basic at $12 and Pro at $28 per seat per month, billed annually, with plans from 3 users; Enterprise is priced by quote from its sales team.",
 col5="Automation actions on the vendor's page",
 rows=[["Microsoft","Dynamics 365 Sales Professional","$65","Paid yearly","None listed"],
       ["Microsoft","Dynamics 365 Sales Enterprise","$105","Paid yearly","None listed"],
       ["Microsoft","Dynamics 365 Sales Premium","$150","Paid yearly","None listed"],
       ["monday.com","monday CRM Basic","$12 per seat","Billed annually","None listed"],
       ["monday.com","monday CRM Pro","$28 per seat","Billed annually","25,000 automation actions and 25,000 integration actions per month"],
       ["monday.com","monday CRM Enterprise","Quote from monday.com","Not shown","250,000 automation and integration actions per month"]],
 price_note2="On its pricing page, monday.com says yearly billing saves 18% and monthly plans are not discounted, but it shows no separate monthly price. Plans start from 3 users, and the free option is a 14-day trial.",
 fit_lead="A move fits a sales team on monday CRM whose boards hold mostly standard records, such as leads, contacts, accounts and deals, and who already work in Outlook and Teams. It is a weaker fit if your monday.com account runs many automations and integrations, or if you need other systems connected on day one.",
 fit_yes=["Most of your monday CRM setup is standard boards: leads, contacts, accounts and deals.",
          "Your monday.com renewal date is coming and you want a plan before it arrives."],
 fit_no="Your monday.com account runs many automations and integrations. We review them first and scope that rebuild separately.",
 q4=["Do our monday.com automations and integrations move across?","Not on their own. Automations, integrations and apps are rebuilt in Dynamics 365 rather than copied. We review them first and quote any rebuild separately."],
 q5=["Does Microsoft have a tool for moving from monday.com?","Not a dedicated one. Microsoft's own migration tool, Dynamics 365 Activate, covers moves from Salesforce. For other systems, Microsoft's guidance points to data import, dataflows and data migration tools such as Azure Data Factory."],
 checklist="monday.com to Dynamics 365 Checklist",
 other=["nine-move-salesforce.html","Move from Salesforce"],
)
S=lambda fact,url,quote: dict(fact=fact,url=url,quote=quote,date=D)
GS='https://support.monday.com/hc/en-us/articles/4409464697618'
v['sources']=[
 S("monday CRM plans shown: Basic, Pro, Enterprise (no Standard or Free card)",PR,"Basic ... Pro ... Enterprise"),
 S("Basic price",PR,"$12 seat / month ... Billed annually"),
 S("Pro price",PR,"$28 seat / month ... Billed annually"),
 S("Enterprise has no listed price",PR,"If you want to sign up more than 40 users, you can request a quote from our sales team to get an exact price."),
 S("Billing toggle and discount",PR,"Yearly SAVE 18% | Monthly; monthly plans are not discounted"),
 S("Yearly paid upfront",PR,"Payment is made in one upfront installment (if you purchase a plan for one year, you will pay for one year upfront)."),
 S("Minimum seats",PR,"Plans start from 3 users."),
 S("Free option",PR,"Your first option to use monday CRM for free is a 14-day trial."),
 S("Pro automation and integration actions",PR,"Custom CRM automations (25,000 actions per month) / Custom CRM integrations (25,000 actions per month)"),
 S("Enterprise automation and integration actions",PR,"Includes 250K automation & integration actions per month."),
 S("No onboarding fee or AI credits on the CRM pricing page",PR,"No onboarding fee, AI, AI credits or AI agents appear on the page (as read through WebFetch)"),
 S("Core CRM boards: Leads",GS,"To get started using monday CRM, import your leads into your Leads board."),
 S("Core CRM boards: Accounts",GS,"From the Accounts board, you will be able to see how many contacts are associated with each company."),
 S("Core CRM boards: Deals",GS,"With the Deals board, you have the power to track the progress of every deal your sales team is currently working on."),
 S("Core CRM boards: Activities",GS,"Each activity created will automatically be added to the Activities board."),
 S("Core boards fixed",GS,"The core boards and columns of monday CRM (cannot be deleted or duplicated, per the article)"),
 S("Integrations feed leads",GS,"automatically through integrations with specific tools such as Facebook, Hubspot, Pipedrive"),
 S("Items, groups, boards","https://support.monday.com/hc/en-us/articles/115005319105","An item is an individual row (or line item) in a group. ... Your monday.com boards are made up of groups of items."),
 S("Excel export limits","https://support.monday.com/hc/en-us/articles/26989749858578-Export-a-board-to-Excel","You may only export a board with up to 10,000 items at a time. ... The Auto Number Column is not supported when exporting to Excel."),
 S("Microsoft guidance for moving from other CRMs (no monday.com tool found)","https://learn.microsoft.com/dynamics365/guidance/implementation-guide/data-management-product-specific-ce#migrate-data","For more complex migrations, such as moving all the data from an old CRM system, manual import from flat files isn't efficient and can cause errors. Instead, use ETL tools like SSIS or Azure Data Factory."),
 S("Live page title",LIVE,"Migrate from Monday.com to Dynamics 365 | enCloud9"),
 S("Live page hero",LIVE,"Ready to Replace monday.com? Choose Dynamics 365."),
 S("Live page download",LIVE,"monday.com to Dynamics 365 Checklist ... Get My Free Download!"),
 S("PriceMDs started on Monday CRM","/home/claude/lb/stories-data/pricemds.json (slug how-price-mds-transformed-healthcare-operations-with-dynamics-365; live URL not opened)","Before partnering with enCloud9, PriceMDs was using Monday CRM."),
]
v['live_page_notes']=("Read 9 Nov 2026 via WebFetch (curl blocked by proxy, so wording comes through a summarizer; short quotes were requested exactly). Title 'Migrate from Monday.com to Dynamics 365 | enCloud9'; no author or date. Hero H2 'Ready to Replace monday.com? Choose Dynamics 365.' Intro opens 'You've outgrown monday.com' with an em dash. "
 "Feature H4s: Tailored to Fit Your Business; Data That Drives Decisions; Transparent Pricing; Full Ownership of Your Data; Seamless Microsoft Integration; Actionable Insights at a Glance; Customizable Workflows; Advanced Automation. Closing H4 'Ready to get more from Dynamics 365?'. "
 "CTAs: 'Speak to an Expert' (Microsoft Bookings), download form (First Name, Last Name, Work Email, consent) with button 'Get My Free Download!' for 'monday.com to Dynamics 365 Checklist' (image file named 'Migration Readiness Checklist'). Links to /dynamics-365-sales/ and microsoft.com/en-us/dynamics-365. "
 "Errors and unsourced claims: an 11-row 'Monday.com vs. Dynamics 365' table marks monday.com with a cross for Advanced Customization, Scalable CRM Capabilities, Full Data Ownership, AI-Powered Sales Tools, Real CRM Functionality, Multi-Entity Support, Centralized Customer Records and Migration Support, and 'Limited/Basic/Add-ons' for Microsoft 365 Integration, Workflow Automation and Enterprise-Grade Reporting, with no source; monday.com sells monday CRM with Leads, Contacts, Accounts and Deals boards and lists automations and integrations on its own pricing page, so 'Real CRM Functionality' and 'Centralized Customer Records' crosses contradict the vendor's pages. 'Get the insights monday.com lacks', 'no templates, no fluff', 'free from platform lock-in', 'Avoid surprise fees' and 'Connect effortlessly' are unsupported. "
 "Capitalization is mixed (Monday.com in title, table header and metadata; monday.com in hero, body and download). Em dashes throughout. A stray 'Δ' near the form. No prices, figures or client story on the page.")
v['notes']=("Naming: the vendor writes 'monday.com' and 'monday CRM' in lowercase. Per instructions name='Monday.com' and crumb='Move from Monday.com' are kept as given, but all running text uses the vendor's lowercase and avoids starting sentences with it. The shared FAQ template in gen_moves.py builds 'How much does a move from Monday.com cost?' from name, so those two FAQs and the crumb will show 'Monday.com'; Brian or the builder should pick one form (I recommend 'monday.com' to match the title, the vendor and the live hero). "
 "Pricing: read through WebFetch only (curl blocked). The page showed three cards (Basic $12, Pro $28, Enterprise by quote), all 'Billed annually', no Standard plan and no monthly price figure despite a Monthly toggle; monday.com has sold a Standard tier before, so a browser check of the live pricing page (and the monthly toggle) is worth doing before publish. No AI features or AI credits were listed on the CRM pricing page, so col5 uses automation actions instead of AI; Microsoft rows read 'None listed' there because Microsoft's price page does not list automation caps, which could read oddly; Brian may prefer the HubSpot page's onboarding-fee column (monday.com lists none). "
 "Microsoft tooling: no monday.com-specific Microsoft tool or guide found on Learn; q5 reuses the HubSpot wording, supported by the Learn implementation guide (Get data from Excel, dataflows, ETL such as Azure Data Factory). "
 "'Automations, integrations and apps do not move on their own' is our process statement, not a monday.com quote; no monday.com page found saying automations export. The Excel export page says up to 10,000 items per export and no Auto Number Column, which matters for scoping. "
 "Some businesses run their CRM on monday.com work management boards rather than monday CRM; the copy says 'monday.com account' and 'boards' so it covers both, but fit_yes names monday CRM boards. "
 "Client story: PriceMDs (stories-data/pricemds.json) says 'Before partnering with enCloud9, PriceMDs was using Monday CRM' and 'What started as a simple migration grew into a full CRM overhaul.' It names the move but measures nothing about it (no record counts, timeline or figures), so it is not a measured move story. Proposed optional story card, using only the story's wording: client 'PriceMDs', line 'PriceMDs was using Monday CRM before we implemented Dynamics 365. What started as a simple migration grew into a full CRM overhaul, with a pharmacist portal, Tive and Ship 24 integrations and electronic signatures.', link to the story slug how-price-mds-transformed-healthcare-operations-with-dynamics-365. Brian decides whether a story card goes on this page (the sister pages have none). Note the story writes 'Monday CRM' with a capital M. "
 "Open for Brian: weeks, records, training sessions, days of help ([Brian sets]); whether the checklist PDF content matches the new page; retire the live page's comparison table.")
p='/home/claude/lb/moves-data/monday.json'
json.dump(v,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
w=lambda s:len(s.split())
print(len(v['title']),len(v['meta']),w(v['answer']))
blob=json.dumps({k:x for k,x in v.items() if k not in('sources','live_page_notes','notes')},ensure_ascii=False)
print('dash',bool(re.search('[–—]',blob)),'BC','Business Central' in blob, 'cheaper' in blob.lower(),'better than' in blob.lower(),'licence' in blob.lower())
