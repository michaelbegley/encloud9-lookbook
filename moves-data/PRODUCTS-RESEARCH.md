# PRODUCTS RESEARCH: enCloud9 product, app and add-on pages

Researched 9 Nov 2026 by a read-only research agent for the encloud9.com rebuild.

## How this was gathered (read first)

- Every page was opened with WebFetch. Direct HTML download (curl) was blocked by the agent proxy (CONNECT 403), so no raw HTML was read. WebFetch returns quotes through a summarizer capped at about 125 characters per quote. Quotes below were requested "character for character" and are short, but they were **not checked against raw HTML**. Treat every quote as "measured through WebFetch", and re-check any quote that will be reused word for word on the new site.
- Where a sentence was longer than the cap, the quote is split into fragments joined with " / ".
- Labels used: **measured** (seen on the page via WebFetch), **inferred** (my reasoning from what was seen), **opinion** (my judgment).
- Business Central appears on **every one of the six pages**, but only in the site navigation and footer, never in the body copy (measured). That nav and footer will be replaced on the new site, so no page body needs a Business Central fix. Flagged per page anyway.
- AppSource: **no enCloud9 listing found** (details in section 7).

---

## 1. Email Verifier

URL: https://www.encloud9.com/email-verifier/

### Facts

| Fact | Exact quote | URL |
|---|---|---|
| Page title | "Email Verifier \| enCloud9 \| Dynamics 365 CRM & Copilot Experts" | https://www.encloud9.com/email-verifier/ |
| H1 | "Email Verifier for Dynamics 365" | same |
| Opening line | "Verify every email address in your CRM in real time." | same |
| What it is | "Email Verifier is a Dynamics 365 add-on from enCloud9 that checks every email address in your CRM for deliverability." | same |
| Who makes it | "a Dynamics 365 add-on from enCloud9" (only statement of origin; no "built by" line) | same |
| Trial | H3 "Start free with 100 verifications"; page says first 100 verifications free, "no credit card required" (summarized wording) | same |
| Trial form | Fields First Name, Last Name, Email (required), Phone (optional); button text "Contact Us Today" | same |
| H2s, in order | "What is Email Verifier for Dynamics 365?"; "How Email Verifier works"; "Email Verifier features"; "Why do emails go to spam?"; "How much does Email Verifier cost?"; "Frequently asked questions"; "Make every email in Dynamics 365 count" | same |
| How it works H3s | "Verify at the point of entry"; "Clean what you already have"; "Act on the results" | same |
| Feature: real time | "Every email address is checked as it is entered, keeping bad data out of your CRM from the start." | same |
| Feature: bulk | "Verify entire marketing lists, leads, and contacts in one pass before launching a major campaign." | same |
| Feature: Sendex | "Each address gets a score that ranks its quality, so marketers can prioritize high-value prospects." | same |
| Feature: results | "See exactly why an address failed: disposable, role-based, defunct, or undeliverable." | same |
| Feature: deliverability | "Fewer bounces and fewer spam traps mean a stronger sender reputation and more email in the inbox." | same |
| Feature: built for D365 | "Runs inside your environment and works with Power Apps, so verification fits your existing workflow." | same |
| Runs inside D365 (FAQ) | "Yes. Email Verifier is built for Dynamics 365 and runs in your environment." | same |
| Versus built-in validation (FAQ) | "Built-in validation catches basic problems like bad syntax." Rest of answer (summarized): Email Verifier checks whether an address can receive mail, scores it with Sendex, cleans lists in bulk. | same |
| ClickDimensions / Customer Insights (FAQ) | Answer says verifying lists before sends reduces bounces in any email platform, "including ClickDimensions and Dynamics 365 Customer Insights" (summarized; short fragment) | same |
| Price: Essentials | "$240 USD / year" / "12,000 email verifications per year" / "2.0 cents per verification" | same |
| Price: Premium | "$1,080 USD / year" / "60,000 email verifications per year" / "1.8 cents per verification"; marked "Most popular" | same |
| Price: Enterprise | "$1,920 USD / year" / "120,000 email verifications per year" / "1.6 cents per verification" | same |
| All plans | include real time and bulk verification; each lists "Add verification packs anytime" | same |
| Proof callout | "B&G Landholdings strengthened their Dynamics 365 data quality with Email Verifier." Links to https://www.encloud9.com/about-encloud9/microsoft-dynamics-365-success/ | same |
| CTAs | "Schedule a call with an expert", "Get started" (each plan), "Talk to an expert": all to https://www.encloud9.com/lp/schedule-a-meeting/ ; "Start free with 100 verifications" to on-page anchor #ev9-start | same |
| Third-party engine | None named on the page. "Sendex" has no trademark notice or owner. | same |
| Partner badges | "Microsoft Solutions Partner", "Click Gold Partner" (footer) | same |
| Business Central | Footer and nav only. **FLAG** | same |
| HubSpot / AppSource | Not mentioned | same |

### Supporting sources

| Fact | Exact quote | URL |
|---|---|---|
| Blog post title | "Improve Email Deliverability with enCloud9 Email Verifier" | https://www.encloud9.com/blog/improve-email-deliverability-with-encloud9-email-verifier/ |
| Blog byline and date | "By Brian Begley", "May 3, 2026" | same |
| Blog feature | "Built specifically for Dynamics 365 and Power Apps"; lists "Sendex Score analysis" | same |
| Blog pricing / AppSource | None | same |
| Client story (data file) | Products: "Dynamics 365 Sales / Click Marketing Automation / enCloud9 Email Verifier" | /home/claude/lb/stories-data/bgland.json |
| Client story solution | "B&G Landholdings partnered with enCloud9 to implement our Email Verifier solution within Microsoft Dynamics 365." | same |
| Client story features | "Real-time email validation during lead and contact creation."; "Bulk verification capabilities for existing CRM records."; "Automated identification of invalid and high-risk email addresses." | same |
| Client story outcomes | "Improved accuracy of contact information within Dynamics 365."; "Reduced risk of sending campaigns to invalid email addresses."; "Reduced manual effort required to identify problematic records." | same |
| Client story numbers | None. Data file notes: "No numbers on the page, so no tiles and no timeline." Quote has no named person. | same |
| Client story meta | author "Kristin Caniglia", published "2026-04-10", live slug bg-landholdings-strengthens-data-quality-and-email-deliverability-with-encloud9-email-verifier | same |

### Unsupported or wrong claims

1. **Pricing model conflicts with the EULA** (measured on both pages). Product page: annual plans priced per verification volume. EULA: "THE PRICE FOR THE SOLUTION(S) IS PER USER", "Users must subscribe to the service each month." If the EULA governs Email Verifier, one of the two is wrong. Needs Brian's decision before the new page ships prices.
2. **"Sendex" is used with no owner.** Inferred, not measured on any page: Sendex is the name Emailable uses for its own quality score, which would mean Email Verifier calls Emailable behind the scenes. If so, the name may need a trademark credit or a rename to "quality score". Could not determine from the pages. Ask Michael or Brian which engine the product uses.
3. "Fewer bounces and fewer spam traps mean ... more email in the inbox" and "stronger sender reputation": reasonable outcome claims, but no figure or client measurement backs them (B&G story has no numbers).
4. Trial form button says "Contact Us Today" while the heading promises a free start. Small mismatch; the copy says the team "sets it up", so the trial is not self-serve (inferred).
5. Callout link goes to the general success stories page, not the B&G story itself (measured).
6. Client story spells the city "Fort Meyers" on the live page; real city is Fort Myers (from bgland.json notes).

### Worth-it read (opinion)

Keep and promote. This is the only page in the set that sells something real, priced and owned by enCloud9 today: a named product, three published prices, a free 100-verification start, a FAQ that answers real buyer questions, and one client story (B&G Landholdings) behind it. It is already close to the target page pattern. Two things block it from going live as-is: the per-user/monthly EULA versus per-verification/annual pricing conflict, and the unexplained Sendex name. Proof is thin: one client, no numbers.

### Suggested page content (new site)

- **H1:** Email Verifier for Dynamics 365
- **Answer (49 words):** Email Verifier is enCloud9's Dynamics 365 add-on that checks every email address in your CRM for deliverability. It verifies new leads and contacts as they are entered, cleans existing lists in bulk, and scores each address. Annual plans start at $240 for 12,000 verifications, and your first 100 are free.
- **What is included:** real time verification on lead and contact creation; bulk verification of contacts, leads and marketing lists; a quality score on each record; detailed failure reasons (disposable, role-based, defunct, undeliverable); results stored on the Dynamics 365 record; works with Power Apps; setup by the enCloud9 team; verification packs can be added anytime.
- **Plans:** Essentials $240 per year, 12,000 verifications; Premium $1,080 per year, 60,000; Enterprise $1,920 per year, 120,000. (Hold until the EULA conflict is settled.)
- **Who it fits:** Dynamics 365 teams that send email campaigns, including ClickDimensions (Click) or Customer Insights users, and teams with growing contact volume where bad addresses are entering the CRM (the B&G Landholdings situation).
- **Proof:** B&G Landholdings (Fort Myers, FL), Dynamics 365 Sales plus Click Marketing Automation plus Email Verifier. Outcomes as listed in the story, no numbers.
- **FAQ questions:** How do I start with Email Verifier? Does Email Verifier run inside Dynamics 365? What is the quality score? What kinds of bad addresses does it catch? How is this different from the built-in email validation in Dynamics 365 Sales? Does it help with ClickDimensions or Customer Insights campaigns? What does Email Verifier cost?

---

## 2. Email Verifier EULA (product facts only)

URL: https://www.encloud9.com/email-verifier-eula/

### Facts

| Fact | Exact quote | URL |
|---|---|---|
| Page title | "Email Verifier EULA \| enCloud9 \| Dynamics 365 CRM & Copilot Experts" | https://www.encloud9.com/email-verifier-eula/ |
| H1 | "enCloud9 LLC End User License Agreement" "(EULA)" | same |
| Licensor | "ENCLOUD9, LLC" | same |
| Product name | Not defined. Text says "the solution(s)" and "enCloud9's solutions". The word "Email Verifier" appears only in the page title and nav. | same |
| What is licensed | "THE RIGHT TO ACCESS AND USE ENCLOUD9'S SOLUTION(S) THAT ARE SUBSCRIBED TO" | same |
| Price basis | "THE PRICE FOR THE SOLUTION(S) IS PER USER AND MUST BE LICENSED FOR ALL INDIVIDUALS WHO HAVE ACCESS TO THE SOLUTIONS." | same |
| Term | "Users must subscribe to the service each month." | same |
| Payment | "The charge is paid at the beginning of each month and will be paid electronically only." | same |
| Renewal | "Renewal of monthly subscription will be automatic until User communicates in writing" | same |
| Failed payment | "If the credit card transaction fails, the solutions will expire." | same |
| Cancellation | "A User may terminate this Agreement at any time by notifying enCloud9 electronically prior to the 1st of the month" | same |
| Trial | Not mentioned | same |
| Dates | No effective or last updated date found | same |
| Third-party engine | None named | same |
| Business Central | Nav and footer only. **FLAG** | same |

### Unsupported or wrong claims

1. Per user, monthly, credit card terms contradict the product page's annual, per-verification plans and "no credit card required" trial (measured on both pages).
2. Generic text: it reads as a shared EULA for all "solutions", not one written for Email Verifier (inferred from "solution(s)").
3. No effective date, which weakens it as a contract page (measured absence).

### Worth-it read (opinion)

Needed as a legal page, not a sales page. It must be rewritten or confirmed by Brian to match how Email Verifier is actually sold before the new product page goes live. Not a marketing priority, but a real risk if left contradicting the prices.

### Suggested page content (new site)

Not a sales page. Keep the URL, carry the legal text as given by Brian, add an effective date, name the product, and state the billing model that matches the product page. No answer block or FAQ.

---

## 3. enCloud9 Apps

URL: https://www.encloud9.com/encloud9-apps/

### Facts

| Fact | Exact quote | URL |
|---|---|---|
| Page title | "enCloud9 Apps \| enCloud9 \| Dynamics 365 CRM & Copilot Experts" | https://www.encloud9.com/encloud9-apps/ |
| H1 | "enCloud9 Apps" | same |
| Intro | "Effortlessly connect your tools with custom Dynamics 365 apps." | same |
| H2s | "Law Pro 365", "Email Verifier", "EasySMS", "Wealth Builder" (no H3s) | same |
| Law Pro 365 | "Law Pro 365 is a dynamic, cloud-based solution designed specifically for law firms to streamline operations" / "and enhance client service." Summary: case management, documents, time tracking, billing, Office 365 integration, Power BI, mobile. | same |
| Email Verifier | "Email Verifier for Dynamics 365 is a powerful tool designed to enhance your email accuracy and deliverability." | same |
| EasySMS | "EasySMS for Dynamics 365 is a powerful SMS integration solution" / "that transforms the way businesses communicate with their clients." Summary: two-way messaging, triggers, bulk, templates, delivery tracking, compliance tools. | same |
| Wealth Builder | "Wealth Builder is a comprehensive solution designed specifically for wealth and asset management firms," / "private banks, and family offices." | same |
| Superlatives | "Law Pro 365 is the ultimate tool for modern law firms"; "EasySMS for Dynamics 365 is the ultimate tool for businesses"; "Wealth Builder is the ultimate tool for modern wealth management firms"; "Email Verifier is a must-have for maintaining effective and efficient email outreach." | same |
| Who built them | Not stated for any app. Grouped under "enCloud9 Apps" only. | same |
| Prices, trials | None | same |
| CTAs | Each "Learn more about ..." link goes to a Microsoft Bookings calendar (outlook.office.com/bookwithme/...), not a product page. "Schedule a Call with an Expert" and "Let's talk" go to the same Bookings service. | same |
| Client names / numbers | None | same |
| Business Central | Nav and footer only. **FLAG** | same |
| Other vendors | ClickDimensions (nav, Click Gold badge), Document Core Pack, Tibco/Scribe, Zap Copy Record (footer); Office 365, Power BI in Law Pro copy | same |
| HubSpot / AppSource | Not mentioned | same |

### Unsupported or wrong claims

1. "The ultimate tool" three times and "must-have" once: unsupported superlatives with no proof.
2. "custom Dynamics 365 apps": no app says who built it, whether it is installable today, or what it costs. Only Email Verifier has its own page, prices and a client (measured).
3. Law Pro 365, EasySMS and Wealth Builder: no product page, no price, no client, no AppSource listing found. Could not determine whether these are live products, past projects, or plans.
4. "Learn more" links that open a booking calendar mislead the reader (they expect product detail).

### Worth-it read (opinion)

Weak as it stands. One of four apps (Email Verifier) is clearly real and sold. The other three may be real but nothing on the site proves it. The page should not carry products enCloud9 cannot sell today. Ask Brian which of Law Pro 365, EasySMS and Wealth Builder are live and supported. If only Email Verifier is, this page collapses into the Email Verifier page plus a short line on custom apps (which overlaps with custom development services).

**Overlap with Add-On Products (opinion):** both are "things you bolt onto Dynamics 365" pages with no prices and Bookings CTAs. The difference is ownership: Apps are enCloud9's own (claimed), Add-Ons are other vendors' products (DocumentsCorePack, TIBCO, Zap Copy Record). **Recommendation: merge into one hub, "Apps and add-ons for Dynamics 365", with two clearly labeled groups: "Built by enCloud9" (Email Verifier, plus any app Brian confirms) and "Partner products we implement" (only ones Brian confirms enCloud9 actually implements or resells).** One hub is easier to keep honest and gives Email Verifier a parent page. Keep both old URLs redirecting to it.

### Suggested page content (new site, merged hub)

- **H1:** Apps and add-ons for Dynamics 365
- **Answer (44 words):** enCloud9 builds its own Dynamics 365 apps and implements selected add-ons from other vendors. Our main product is Email Verifier, which checks every CRM email address for deliverability, with plans from $240 a year. We can also help you choose and set up document and integration add-ons.
- **What is included:** Built by enCloud9: Email Verifier (link to its page). Other enCloud9 apps only if Brian confirms they are live: Law Pro 365 (law firms), EasySMS (SMS for Dynamics 365), Wealth Builder (wealth and asset management firms, private banks, family offices). Partner products: see section 4.
- **Who it fits:** Dynamics 365 customers who need a specific capability Dynamics 365 does not do out of the box.
- **FAQ questions:** Which apps does enCloud9 build? Do these apps run inside Dynamics 365? How much does Email Verifier cost? Does enCloud9 resell the partner add-ons or just set them up? Can enCloud9 build a custom app for us?

---

## 4. Add-On Products

URL: https://www.encloud9.com/add-on-products/

### Facts

| Fact | Exact quote | URL |
|---|---|---|
| Page title | "Add-On Products \| enCloud9 \| Dynamics 365 CRM & Copilot Experts" | https://www.encloud9.com/add-on-products/ |
| H1 | "Add-On Products" | same |
| Intro | "Explore solutions that simplify document management, automate workflows, and improve overall efficiency" (sentence continues: in your Dynamics 365 environment) | same |
| H2s | "DocumentsCorePack", "TIBCO", "Zap Copy Record" (no H3s) | same |
| DocumentsCorePack | "DocumentsCorePack is a comprehensive solution for Microsoft Dynamics 365 that simplifies document creation, management," ... | same |
| DocumentsCorePack signatures | "DocumentsCorePack supports digital signatures through integration with platforms like DocuSign and Adobe Sign," | same |
| DocumentsCorePack link | link text "DocumentsCorePack" to https://www.mscrm-addons.com/language/de-DE/Solutions/DocumentsCorePack (German-language URL) | same |
| TIBCO | "TIBCO is a leading integration and analytics platform that enhances CRM systems by enabling seamless data integration" | same |
| TIBCO connectors | "With over 200 pre-built connectors, it allows businesses to connect CRM platforms like Microsoft Dynamics 365" | same |
| TIBCO link | https://www.tibco.com/ ; nav label "Tibco/Scribe" | same |
| Zap Copy Record | "Zap Copy Record is a powerful app for Microsoft Dynamics 365 designed to streamline the process of duplicating records." | same |
| Zap link | https://zapobjects.com/apps/zap-copy-record/ | same |
| enCloud9 role | Not stated for any of the three. Only partner lines on the page: "enCloud9 is a Microsoft Solutions Partner", "enCloud9 is a Click Gold Partner". | same |
| Prices, trials, clients | None | same |
| CTAs | "Schedule a Call with an Expert", "Let's talk": Microsoft Bookings; "Contact Us": https://www.encloud9.com/contact-us | same |
| Business Central | Nav and footer only. **FLAG** | same |
| HubSpot / AppSource | Not mentioned | same |

### Unsupported or wrong claims

1. "over 200 pre-built connectors" is TIBCO's claim, not enCloud9's, and the page gives no source or date for it.
2. "a leading integration and analytics platform": vendor superlative with no source.
3. The page never says whether enCloud9 resells, implements or merely recommends these products. Visitors cannot tell what they would buy from enCloud9.
4. TIBCO Scribe (the Dynamics integration tool the nav label points at) has been rebranded and reorganized by its owner over the years (inferred from general knowledge, not checked in this run); the page links to the TIBCO home page, not a Dynamics integration product. Could not determine whether enCloud9 still uses Scribe.
5. DocumentsCorePack link goes to a German-language page (/language/de-DE/) on an English site (measured URL).
6. Three outbound "learn more" links send buyers to other companies' sites, which leaks visitors with no enCloud9 offer attached.

### Worth-it read (opinion)

Thin. It is a list of other vendors' products with no enCloud9 offer, no price and no proof. Worth keeping only if enCloud9 actually implements these add-ons for clients today, in which case each entry should say what enCloud9 does (for example "we set up DocumentsCorePack templates for quotes and invoices"). Merge into the hub described in section 3. Ask Brian which of the three are still sold or implemented, and whether there is a partner agreement for any of them.

### Suggested page content (new site)

Becomes the "Partner products we implement" group on the merged hub (section 3), not its own page. For each confirmed product, one block:
- **DocumentsCorePack:** generates documents such as quotes, invoices and contracts from Dynamics 365 data; supports e-signature through DocuSign and Adobe Sign. Add one line on what enCloud9 does (to be confirmed by Brian).
- **TIBCO (Scribe):** integration platform for connecting Dynamics 365 to other systems. Keep only if confirmed in use.
- **Zap Copy Record:** duplicates records such as quotes, orders and opportunities, including related data.
- **FAQ questions (on the hub):** Does enCloud9 sell these add-ons or set them up? Which add-on creates quotes and invoices from Dynamics 365? Can Dynamics 365 copy a quote with its line items?

---

## 5. Dynamics 365 Marketing Accelerator

URL: https://www.encloud9.com/dynamics-365-marketing-accelerator/

### Facts

| Fact | Exact quote | URL |
|---|---|---|
| Page title | "Dynamics 365 Marketing Accelerator \| enCloud9 \| Dynamics 365 CRM & Copilot Experts" | https://www.encloud9.com/dynamics-365-marketing-accelerator/ |
| H1 | "Dynamics 365 Marketing Accelerator" | same |
| Subheading | "Accelerate Sales. Close Deals Faster. Drive Growth." | same |
| H2 | "Automate Marketing with Dynamics 365 Marketing Accelerator" | same |
| Intro | "enCloud9 helps businesses enhance their marketing efforts with the Dynamics 365 Marketing Accelerator," / "streamlining campaign management, lead nurturing, and audience targeting to improve engagement and conversions." | same |
| Insights claim | "Our intelligent insights" ... "provide data-driven recommendations," / "while real-time dashboards and analytics help optimize campaign performance, track customer interactions," | same |
| Services line | "We also enable automated follow-ups, email marketing, and CRM integration." | same |
| H2 | "enCloud9's Marketing Accelerator Features:" | same |
| Feature 1 | Automated Campaign Management: "Streamline marketing efforts with automated email sequences, lead nurturing, and multi-channel campaigns" | same |
| Feature 2 | Real-Time Marketing Dashboards & Analytics: "Gain actionable insights into campaign performance, audience behavior, and ROI" | same |
| Feature 3 | AI-Powered Audience Targeting: "Use predictive analytics to segment and target high-value leads based on behavior, demographics, and engagement patterns." | same |
| Feature 4 | Lead Scoring & Conversion Optimization: "Identify and prioritize high-potential leads with automated lead scoring," | same |
| Feature 5 | Event & Webinar Management: "Plan, promote, and track both online and in-person events seamlessly with integrated event marketing tools." | same |
| Feature 6 | Seamless CRM & Email Integration: "Sync customer interactions, track email engagement, and manage communications within Outlook" / "and Dynamics 365 for a unified marketing experience." | same |
| Platform named | None. Customer Insights, Dynamics 365 Marketing and ClickDimensions are not named as the platform. "Microsoft's official site" link goes to https://dynamics.microsoft.com/en-us/dynamics365/ | same |
| What enCloud9 delivers | Not stated: no hours, duration, setup steps, training or deliverables | same |
| Who it is for | "businesses" only | same |
| H2 | "Other enCloud9 Accelerators"; H3s "Service Accelerator", "Sales Accelerator" | same |
| Service Accelerator | "Improve service operations, automate workflows, and resolve issues faster" / "with enCloud9's Service Accelerator for Dynamics 365." | same |
| Sales Accelerator | "Track leads, automate sales processes, and close deals faster with enCloud9's Sales Accelerator for Dynamics 365." | same |
| Link bug | Sales Accelerator "Learn More" goes to /dynamics-365-sales-accelerator/, but the H3 title link goes to /dynamics-365-crm-solutions-rescue-repair/ | same |
| Prices, clients | None | same |
| CTAs | "Speak to an expert", "Let's talk": Microsoft Bookings; "Contact Us": /contact-us | same |
| Business Central | Nav and footer only. **FLAG** | same |
| HubSpot | Not mentioned | same |

### Unsupported or wrong claims

1. Subheading "Accelerate Sales. Close Deals Faster." is sales copy on a marketing page (looks copied from the Sales Accelerator).
2. "AI-Powered Audience Targeting", "predictive analytics", "intelligent insights", "data-driven recommendations": no platform, no example, no proof. These are capabilities of Microsoft or ClickDimensions products, not something the page shows enCloud9 adds.
3. "Event & Webinar Management" and "Real-Time Marketing Dashboards": no statement of which product provides them.
4. "Dynamics 365 Marketing" was renamed by Microsoft to Dynamics 365 Customer Insights (inferred from general knowledge, not checked in this run). Using "Dynamics 365 Marketing Accelerator" as a name may read as dated or be confused with a Microsoft product.
5. No client, no number, no deliverable list, no price or duration. Nothing distinguishes it from a product brochure.
6. Sales Accelerator title link points to the Rescue and Repair page (measured link bug).

### Worth-it read (opinion)

As written, it does not stand as a package. A package needs a defined scope (what is set up, how long, what it costs or how it is priced) and this page has none. It describes platform features rather than enCloud9 work. Whether it can sit next to the Sales and Service Accelerators depends on whether those pages define scope (not checked in this run; they were out of scope). enCloud9's real marketing story on the evidence found is ClickDimensions (Click Gold Partner, B&G Landholdings uses Click Marketing Automation) plus Email Verifier. **Recommendation: do not rebuild this page as-is. Either Brian defines a real Marketing Accelerator scope (platform, steps, duration, price basis), or fold it into a "Marketing automation for Dynamics 365" page built on ClickDimensions, Customer Insights and Email Verifier, with a 301 from this URL.**

### Suggested page content (new site, only if Brian defines the package)

- **H1:** Marketing Accelerator for Dynamics 365
- **Answer (45 words):** The Marketing Accelerator is enCloud9's package for getting marketing automation running inside Dynamics 365. We set up campaign automation, lead scoring and email tracking so marketing and sales work from the same CRM data. Talk to an expert to scope the platform and timeline that fit you.
- **What is included (only items the current page claims; Brian to confirm each):** automated email sequences and lead nurturing; campaign dashboards and reporting; lead scoring; event and webinar management; email engagement tracking in Outlook and Dynamics 365. Missing and needed: platform used, duration, deliverables, price basis.
- **Who it fits:** businesses already on Dynamics 365 that want marketing automation in the same system as sales. Needs a sharper fit from Brian.
- **FAQ questions:** What does the Marketing Accelerator include? Which marketing platform does it use: Customer Insights or ClickDimensions? How long does it take? How is it priced? How does it relate to the Sales and Service Accelerators? Do we need clean email data first? (link to Email Verifier)

---

## 6. ClickDimensions PowerPack

URL: https://www.encloud9.com/clickdimensions-powerpack/

### Facts

| Fact | Exact quote | URL |
|---|---|---|
| Page title | "ClickDimensions PowerPack - Powered by enCloud9" | https://www.encloud9.com/clickdimensions-powerpack/ |
| H1 | "Unify Sales and Marketing with ClickDimensions PowerPack" | same |
| Intro | "integrated tools for automation, engagement, and customer management inside Dynamics 365" (fragment of a longer intro sentence aimed at small and midsize businesses in the Microsoft ecosystem) | same |
| H2 | "Succeed with enCloud9 and ClickDimensions PowerPack:" | same |
| Benefit: conversions | "Update your sales and marketing strategy with today's customers." | same |
| Benefit: costs | "Get an affordable, easy-to-use, unified sales and marketing software solution." | same |
| Benefit: efficiency | "Unified Sales and Marketing processes mean your efforts have more impact." | same |
| Second H1 | "ClickDimensions PowerPack Delivers:" (a second H1 on the page) | same |
| Marketing Automation | "Automate multi-channel marketing campaigns aimed at your Target Account List." | same |
| CRM | "Manage Contacts, Accounts, & Opportunities." | same |
| Sales Engagement | "Automate email communications to reduce workloads and drive consistency" | same |
| Positioning line | "Discover the Only All-in-One CRM, Marketing Automation, and Sales Enablement Platform Designed Exclusively for SMBs and Leverage:" | same |
| Partner status | "enCloud9 is a Click Gold Partner" (image alt text); "Our certified experts work closely with small to medium-sized companies" | same |
| enCloud9 role | Not stated as reseller or builder. Title says "Powered by enCloud9"; outbound "Learn more about Click" to clickdimensions.com | same |
| Who it is for | Small and midsize businesses in the Microsoft ecosystem | same |
| Prices, clients | None. Links to "Success Stories" with no named client on the page. | same |
| CTAs | "Speak to an expert", "Let's talk": Microsoft Bookings; "Schedule a Call": no link found; "Contact Us": /contact-us | same |
| Business Central | Nav and footer only. **FLAG** | same |
| HubSpot | Not mentioned | same |

### Unsupported or wrong claims

1. "the Only All-in-One CRM, Marketing Automation, and Sales Enablement Platform Designed Exclusively for SMBs": an absolute claim ("Only") with no source; it reads as ClickDimensions' own marketing line. It also contradicts the intro's "inside Dynamics 365": a product that runs inside Dynamics 365 is not itself the CRM.
2. "Powered by enCloud9" in the title implies enCloud9 built or runs the product. Nothing on the page supports that; enCloud9 is a Click Gold Partner (measured).
3. "affordable" with no price.
4. "PowerPack" is never defined: could not determine whether it is a ClickDimensions edition, an enCloud9 bundle of ClickDimensions plus services, or a retired name. ClickDimensions now goes by "Click" (bgland.json notes the live story says "Click Marketing Automation"), so the page name may be out of date (inferred).
5. Two H1s on one page (measured; SEO issue, not a claim).
6. "Schedule a Call" CTA has no link (measured).

### Worth-it read (opinion)

The partnership is real and sellable (Click Gold Partner badge across the site; a client, B&G Landholdings, runs Click Marketing Automation). This page is the weakest way to sell it: undefined product name, a copied vendor superlative, no enCloud9 services listed, no client. Recommendation: replace with a "Click (ClickDimensions) for Dynamics 365" partner page that says what enCloud9 does (implementation, setup, marketing consulting, per the B&G services list), names Click Gold Partner status, links the B&G story, and cross-links Email Verifier. Ask Brian whether "PowerPack" is still a real offer; if not, 301 this URL to the new page. This page and the Marketing Accelerator overlap heavily and should probably become one marketing page (opinion).

### Suggested page content (new site)

- **H1:** Click (ClickDimensions) marketing automation for Dynamics 365
- **Answer (47 words):** enCloud9 is a Click Gold Partner that sets up Click (formerly ClickDimensions) marketing automation inside Dynamics 365 for small and midsize businesses. You get multi-channel campaigns, contact and opportunity tracking, and automated sales email in the same CRM your team already uses. Talk to an expert to scope it.
- **What is included:** marketing automation (multi-channel campaigns aimed at a target account list, engaging buying groups); CRM (contacts, accounts, opportunities, pipeline tracked by buying group, reports for sales leadership); sales engagement (outbound sequences by email, phone and social; automated email). enCloud9 services, per the B&G story: implementation services, data quality, marketing consulting.
- **Who it fits:** small and midsize businesses in the Microsoft ecosystem running Dynamics 365 that want marketing and sales in one system.
- **Proof:** B&G Landholdings (Dynamics 365 Sales, Click Marketing Automation, enCloud9 Email Verifier). Click Gold Partner status.
- **FAQ questions:** What is Click, formerly ClickDimensions? Does Click run inside Dynamics 365? What does enCloud9 do as a Click Gold Partner? What is PowerPack? (only if Brian confirms it exists) How does Email Verifier help Click campaigns? How is Click priced? (answer: talk to us; no price found)

---

## 7. AppSource / Microsoft Marketplace

| Check | Result | Source |
|---|---|---|
| Web search "enCloud9 Email Verifier AppSource Dynamics 365" | No enCloud9 listing. Results were other vendors' verifiers (Data8, Force Works "zbounce", MyEmailVerifier, Zapier integrations). | WebSearch, 9 Nov 2026 |
| Web search "appsource.microsoft.com encloud9" | No enCloud9 listing | WebSearch, 9 Nov 2026 |
| Extended search for enCloud9 apps on Microsoft marketplace | Only encloud9.com and crmsoftwareblog.com results; no marketplace listing | WebSearch, 9 Nov 2026 |
| marketplace.microsoft.com search page | Could not be fetched (robots_disallowed) | https://marketplace.microsoft.com/en-us/search/products?search=encloud9 |
| appsource.microsoft.com search page | Could not be fetched (client_error) | https://appsource.microsoft.com/en-us/marketplace/apps?search=encloud9 |
| PCF Gallery "Email Verifier" | Unrelated: author "Ramprasath Ramamurthi", "A control to validate an email address using PerfectValidation API." | https://search.pcf.gallery/email-verifier |

Result: **could not determine** that any enCloud9 app is listed on AppSource. No evidence of a listing; the marketplace search itself could not be read. Michael can confirm in Partner Center. Opinion: an AppSource listing for Email Verifier would be strong third-party proof for the new page and is worth considering.

---

## 8. Cross-page summary

| Page | Sells something real today? (opinion) | Price shown | Proof | Recommendation (opinion) |
|---|---|---|---|---|
| Email Verifier | Yes | Yes, three plans | B&G Landholdings, no numbers | Keep, fix EULA conflict and Sendex naming |
| Email Verifier EULA | Legal page | Per user, monthly | n/a | Rewrite to match product page |
| enCloud9 Apps | Partly (Email Verifier only proven) | No | None | Merge with Add-Ons into one hub |
| Add-On Products | Unclear (role not stated) | No | None | Merge into hub; keep only confirmed products |
| Marketing Accelerator | No defined package | No | None | Define scope or fold into one marketing page |
| ClickDimensions PowerPack | Partnership yes, "PowerPack" unclear | No | B&G uses Click | Replace with Click partner page |

Questions for Brian (none can be answered from the pages):
1. Is Email Verifier billed per verification yearly (product page) or per user monthly (EULA)?
2. Which engine does Email Verifier use, and can we say "Sendex"?
3. Are Law Pro 365, EasySMS and Wealth Builder live, supported products today?
4. Does enCloud9 resell or implement DocumentsCorePack, TIBCO/Scribe and Zap Copy Record today?
5. What exactly is in the Marketing Accelerator (platform, steps, duration, price basis)?
6. Is "ClickDimensions PowerPack" still a real offer?
