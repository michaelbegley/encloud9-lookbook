import json, re, sys
OUT = "/home/claude/lb/stories-data/"
stories = []

def S(claim, quote): return {"claim": claim, "quote": quote}

stories.append({
 "key": "bgland",
 "slug": "bg-landholdings-strengthens-data-quality-and-email-deliverability-with-encloud9-email-verifier",
 "client": "B&G Landholdings",
 "work_type": "Add-on",
 "title": "B&G Landholdings: Email Verifier for Dynamics 365 | enCloud9",
 "meta": "How enCloud9 added its Email Verifier to B&G Landholdings' Dynamics 365 to catch invalid emails, verify existing records and clean up marketing lists.",
 "h1": ["B&G Landholdings:", "Cleaner email data in Dynamics 365"],
 "answer": "B&G Landholdings, based in Fort Meyers, FL, relies on Dynamics 365, and email accuracy mattered more as its contact volume grew. Invalid and outdated addresses were entering the CRM, raising bounce risk and manual cleanup. We implemented our Email Verifier in Dynamics 365 with real-time and bulk verification. Contact data is now more accurate and marketing lists are cleaner.",
 "facts": [["Client", "B&G Landholdings"], ["Location", "Fort Meyers, FL"], ["Starting point", "Dynamics 365 in place, with invalid email addresses entering the CRM"], ["Products", "Dynamics 365 Sales; Click Marketing Automation; enCloud9 Email Verifier"], ["Services", "Implementation Services, Data Quality, Marketing Consulting"]],
 "timeline": None,
 "tiles": [],
 "outcomes": [
  "Contact information in Dynamics 365 is more accurate.",
  "There is less risk of sending campaigns to invalid email addresses.",
  "Cleaner marketing lists support a better sender reputation.",
  "The team has more confidence in CRM data quality.",
  "Less manual effort is needed to find problem records."],
 "chapters": [
  ["What was wrong with B&G Landholdings' email data?", [
   "B&G Landholdings manages a growing portfolio of business operations and relies on Dynamics 365. As the volume of contacts increased, the accuracy and reliability of email data became more important.",
   "Invalid email addresses were entering the CRM, and outdated contact information was reducing marketing effectiveness. Bounces put sender reputation at risk, finding and fixing bad email data by hand took time, and the team had limited visibility into which addresses posed deliverability risks."]],
  ["What did we change?", [
   "We implemented our Email Verifier inside B&G Landholdings' existing Dynamics 365 environment, without disrupting user workflows.",
   "It validates email addresses in real time when leads and contacts are created, automatically flags invalid and high-risk addresses, and verifies existing CRM records in bulk. The team also gained visibility into email quality and deliverability risks."]],
  ["What changed day to day?", [
   "Contact records in Dynamics 365 are more accurate, marketing lists are cleaner, and less manual effort goes into finding problem records. The team has more confidence in its CRM data and is better prepared for marketing automation and customer engagement work."]]],
 "next_steps": None,
 "quote": None,
 "author": "Kristin Caniglia", "published": "2026-04-10", "published_h": "April 10, 2026",
 "sources": [
  S("Client overview", "B&G Landholdings manages a growing portfolio of business operations and relies on Dynamics 365"),
  S("Contact volume", "As the volume of contacts increased, ensuring the accuracy and reliability of email data became increasingly important"),
  S("Location", "Fort Meyers, FL"),
  S("Products", "Dynamics 365 Sales / Click Marketing Automation / enCloud9 Email Verifier"),
  S("Challenge: invalid emails", "Invalid email addresses entering the CRM."),
  S("Challenge: outdated data", "Outdated contact information reducing marketing effectiveness."),
  S("Challenge: bounces", "Increased risk of email bounces impacting sender reputation."),
  S("Challenge: manual effort", "Time-consuming manual efforts to identify and correct bad email data."),
  S("Challenge: visibility", "Limited visibility into which email addresses posed deliverability risks."),
  S("Solution", "B&G Landholdings partnered with enCloud9 to implement our Email Verifier solution within Microsoft Dynamics 365."),
  S("No disruption", "B&G was able to improve data quality without disrupting user workflows."),
  S("Real-time validation", "Real-time email validation during lead and contact creation."),
  S("Risky addresses flagged", "Automated identification of invalid and high-risk email addresses."),
  S("Bulk verification", "Bulk verification capabilities for existing CRM records."),
  S("Visibility", "Improved visibility into email quality and deliverability risks."),
  S("Existing environment", "Seamless integration within the existing Dynamics 365 environment."),
  S("Outcome: accuracy", "Improved accuracy of contact information within Dynamics 365."),
  S("Outcome: fewer invalid sends", "Reduced risk of sending campaigns to invalid email addresses."),
  S("Outcome: sender reputation", "Enhanced sender reputation through cleaner marketing lists."),
  S("Outcome: confidence", "Increased confidence in CRM data quality."),
  S("Outcome: less manual effort", "Reduced manual effort required to identify problematic records."),
  S("Outcome: readiness", "Better readiness for marketing automation and customer engagement initiatives.")],
 "notes": "Location is spelled 'Fort Meyers, FL' on the page; the real city is Fort Myers, FL. Kept the page spelling in facts and answer; fix the page or this file once Michael confirms. Product list on the page says 'Click Marketing Automation', not 'Click (formerly ClickDimensions)' as on the hub. Page title uses 'B&G Landholdings' while the slug says 'bg-landholdings'. No industry stated, so that row is dropped. No numbers on the page, so no tiles and no timeline. The only quote ('High-quality data is the foundation of effective customer engagement.') has no named person, so quote is null. Page ends with a contact call to action only, so next_steps is null. Business Central appears only in site navigation and footer, not in the story. WebFetch returns summaries; quotes above were requested as exact and are short, but were not checked against raw HTML."
})

stories.append({
 "key": "cfc",
 "slug": "collaborative-for-children-success-story",
 "client": "Collaborative for Children",
 "work_type": "New build",
 "title": "Collaborative for Children: Custom CRM and Portal | enCloud9",
 "meta": "How enCloud9 built a custom Dynamics 365 CRM and portal for Collaborative for Children to manage students, teachers, classrooms and large data imports.",
 "h1": ["Collaborative for Children:", "A CRM built for complex data"],
 "answer": "Collaborative for Children is a Houston-based nonprofit improving early childhood education across Greater Houston. It needed more than a traditional CRM to manage students, teachers, classrooms and large data imports. We built a custom Dynamics 365 solution with a portal for external users and custom plugins. It now handles large datasets with more consistent data and validation.",
 "facts": [["Client", "Collaborative for Children"], ["Location", "Houston, TX"], ["Industry", "Nonprofit, early childhood education"], ["Products", "Dynamics 365 Sales; Dataverse; Power Pages Portal"], ["Services", "Portal Design, Implementation Services, Data Migration/ Integration, Plugin Development, System Logic, CRM Optimization, Ongoing Support"]],
 "timeline": None,
 "tiles": [["100+", "fields in some of the data imports"], ["35 years", "serving early childhood education in Greater Houston"]],
 "outcomes": [
  "Collaborative for Children has a custom CRM designed around complex data relationships.",
  "External users can enter data through a working portal.",
  "Large and complex datasets are handled better.",
  "Data structure and validation are more consistent.",
  "The system can keep adapting as needs change."],
 "chapters": [
  ["What did Collaborative for Children need?", [
   "Collaborative for Children is a Houston-based nonprofit dedicated to improving the quality of early childhood education and care throughout Greater Houston. Working with educators, families and community partners, it delivers programs that strengthen early learning systems.",
   "It needed more than a traditional CRM. The system had to manage complex relationships between students, teachers and classrooms, handle large data imports including assessments and attendance records, let external users enter and update data through a portal, and keep data accurate across multiple sources.",
   "There were real-world problems too: data inconsistencies and missing identifiers, imports with 100+ fields in some datasets, and requirements that kept changing."]],
  ["What did we build?", [
   "We designed and built a custom Dynamics 365 solution around Collaborative for Children's data model, with custom tables, forms and fields structured around students, teachers and classrooms.",
   "We added a custom portal so external users could work with the data securely, handled complex, large-scale data integrations, and wrote custom plugins to automate processes and enforce data integrity.",
   "We kept improving the solution through ongoing updates, imports and refinements, following a build, test, refine and improve approach."]],
  ["What changed day to day?", [
   "Collaborative for Children now works in a CRM designed around its data relationships, with a portal for external data entry, better handling of large datasets and more consistent data structure and validation. The system can keep adapting as its needs change."]]],
 "next_steps": None,
 "quote": None,
 "author": "Kristin Caniglia", "published": "2026-06-16", "published_h": "June 16, 2026",
 "sources": [
  S("Client", "Collaborative for Children is a Houston‑based nonprofit organization"),
  S("Mission", "dedicated to improving the quality of early childhood education and care throughout Greater Houston."),
  S("Programs", "Working with educators, families, and community partners, the organization delivers programs"),
  S("35 years", "Their mission for the past 35 years has been to be “The” trusted nonprofilt resource"),
  S("Location", "Houston, TX"),
  S("More than a CRM", "Collaborative for Children needed more than a traditional CRM."),
  S("Need: relationships", "Managing complex relationships between students, teachers, and classrooms"),
  S("Need: imports", "Handling large volumes of data imports, including assessments and attendance records"),
  S("Need: portal", "Allowing external users to enter and update data through a portal"),
  S("Need: accuracy", "Maintaining data accuracy across multiple sources"),
  S("Problem: data", "Data inconsistencies and missing identifiers"),
  S("100+ fields", "Complex imports involving 100+ fields in some datasets"),
  S("Changing needs", "Ongoing updates and evolving requirements"),
  S("Custom build", "enCloud9 designed and built a custom Dynamics 365 solution tailored to Collaborative for Children’s data model."),
  S("Tables and forms", "Creating custom tables, forms, and fields"),
  S("Entities", "Structuring the system around key entities (students, teachers, classrooms)"),
  S("Portal", "enabled secure collaboration with external users through a custom portal"),
  S("Integrations", "The team handled complex, large-scale data integrations,"),
  S("Plugins", "implemented custom plugins to automate processes and enforce data integrity"),
  S("Ongoing work", "continued to enhance the solution through ongoing updates, imports, and refinements"),
  S("Approach", "following a consistent build → test → refine → improve approach"),
  S("Outcome: custom CRM", "A custom-built CRM designed around complex data relationships"),
  S("Outcome: portal", "A functional portal enabling external data input"),
  S("Outcome: datasets", "Improved handling of large and complex datasets"),
  S("Outcome: consistency", "More consistent data structure and validation"),
  S("Outcome: flexibility", "Ongoing flexibility to adapt the system as needs change")],
 "notes": "Page H1 is 'How Collaborative for Children Managed Complex Student and Classroom Data with Dynamics 365'. Page has a typo 'nonprofilt' in the 35-year mission sentence. Industry is not a labeled field; 'Nonprofit, early childhood education' is from the overview wording. No starting system is named, so the Starting point row is dropped. Services list on the page writes 'Data Migration/ Integration' with that spacing; kept exactly. The 35 years tile is the client's mission age, not a project figure; drop it if the template wants project numbers only. No timeline stated. The only quote ('Most Dynamics 365 projects don't fail...') is unattributed and reads as enCloud9's own line, so quote is null. Page uses em dashes in its own text; none copied into fields except where quoted in sources (the em dash quote was left out). Next steps: only ongoing enhancements as part of the solution plus a contact call to action, so null. Business Central appears only in site navigation and footer."
})

stories.append({
 "key": "pricemds",
 "slug": "how-price-mds-transformed-healthcare-operations-with-dynamics-365",
 "client": "PriceMDs",
 "work_type": "New build",
 "title": "PriceMDs: Dynamics 365 for Healthcare Operations | enCloud9",
 "meta": "How enCloud9 moved PriceMDs from Monday CRM to Dynamics 365, then added a pharmacist portal, Tive and Ship 24 integrations and electronic signatures.",
 "h1": ["PriceMDs:", "A CRM built around healthcare work"],
 "answer": "PriceMDs, a healthcare company in Clearwater, FL, was using Monday CRM and needed to manage patient and prescription data with custom business logic. We implemented Dynamics 365 with custom entities, workflows and plugins, then added a pharmacist portal, Tive and Ship 24 integrations and electronic signatures. Patient onboarding is faster and reporting is clearer.",
 "facts": [["Client", "PriceMDs"], ["Location", "Clearwater, FL"], ["Industry", "Healthcare"], ["Starting point", "Monday CRM"], ["Products", "Dynamics 365 Sales and Customer Service; Dataverse; Power Pages (Portal); Document Core Pack"], ["Services", "Dynamics 365 Implementation, Custom Development and Plugin Enhancements, Ongoing Support and optimization, API Integration (with Tive and Ship 24), Data Management and Reporting"]],
 "timeline": None,
 "tiles": [],
 "outcomes": [
  "What started as a simple migration grew into a full CRM overhaul.",
  "A pharmacist portal replaced managing orders through informal messaging apps.",
  "Electronic signatures through Document Core Pack and Adobe Sign significantly sped up patient onboarding.",
  "PriceMDs reports better visibility into operations and reporting.",
  "The CRM is aligned with real-world healthcare processes."],
 "chapters": [
  ["What did PriceMDs need?", [
   "PriceMDs offers healthcare solutions that help organizations reduce costs while improving access to medications and patient services. Its operations rely on accurate data, efficient workflows and visibility across multiple processes. Before working with enCloud9, PriceMDs was using Monday CRM.",
   "It needed a system to manage patient and prescription data across multiple processes, support custom business logic that out-of-the-box CRM does not handle, improve visibility into operations and reporting, and keep data consistent and reliable.",
   "As the business grew, new needs appeared: more workflows and integrations, more data volume, and more functionality without losing stability."]],
  ["What did we build?", [
   "We implemented Dynamics 365 and configured it around how PriceMDs actually works, with custom entities, workflows, plugins and data structures.",
   "Once PriceMDs saw what Dynamics 365 could do, the scope expanded. We supported the development of a medication Pricing Portal, enabled integration with external systems like Tive and Ship 24, and improved data management, reporting and automation.",
   "We built a pharmacist portal and set up electronic signatures through Document Core Pack and Adobe Sign."]],
  ["What changed day to day?", [
   "The pharmacist portal ended the chaos of managing orders through informal messaging apps, and electronic signatures significantly sped up patient onboarding. The team works with greater ease and confidence, and PriceMDs reports better visibility into operations and reporting."]]],
 "next_steps": None,
 "quote": None,
 "author": "Kristin Caniglia", "published": "2026-06-05", "published_h": "June 5, 2026",
 "sources": [
  S("Client overview", "PriceMDs offers win-win healthcare solutions to help organizations reduce costs"),
  S("Industry", "reduce costs while improving access to medications and patient services"),
  S("Operations", "Their operations rely heavily on accurate data, efficient workflows, and visibility across multiple processes."),
  S("Implementation", "To support this, PriceMDs implemented Dynamics 365 with enCloud9 as their partner."),
  S("Starting point", "Before partnering with enCloud9, PriceMDs was using Monday CRM."),
  S("Need: patient data", "Managing patient and prescription data across multiple processes"),
  S("Need: custom logic", "Supporting custom business logic not handles by out-of-the-box CRM"),
  S("Need: visibility", "Improving visibility into operations and reporting"),
  S("Need: consistency", "Ensuring data consistency and reliability"),
  S("Growth needs", "As the business grew, new needs emerged:"),
  S("Growth: workflows", "Supporting additional workflows and integrations"),
  S("Growth: volume", "Handling increasing data volume"),
  S("Growth: stability", "Expanding system functionality while maintaining stability."),
  S("Build", "configured the system to support their core operations, including custom entities, workflows, plugins"),
  S("Fit to process", "From the start, the focus was on aligning the system with how PriceMDs actually works"),
  S("Pricing Portal", "supporting the development of a medication Pricing Portal"),
  S("Integrations", "enabling integration with external systems like Tive and Ship 24"),
  S("Scope expanded", "Once Price MDs saw the potential of Dynamics 365, the project scope expanded."),
  S("Outcome: overhaul", "What started as a simple migration grew into a full CRM overhaul"),
  S("Outcome: pharmacist portal", "One of the most impactful outcomes was the creation of the pharmacist portal."),
  S("Outcome: orders", "This enabled global coordination and eliminated the chaos of managing orders through informal messaging apps."),
  S("Outcome: e-signatures", "the implementation of electronic signatures through Document Core Pack and Adobe Sign"),
  S("Outcome: onboarding", "which significantly accelerated the patient onboarding process."),
  S("Outcome: team", "The client’s team now works with greater ease and confidence"),
  S("Outcome: aligned CRM", "PriceMDs now has a CRM system that is aligned with real-world healthcare processes."),
  S("Outcome: visibility", "PriceMDs has reported better visibility into operations and reporting")],
 "notes": "Page H1 is 'How PriceMDs Improved Healthcare Operations with Dynamics 365'; slug says 'transformed'. Page writes both 'PriceMDs' and 'Price MDs'; used PriceMDs. Published June 5, 2026 with a modified date of August 13, 2026 in metadata. Page mentions both a 'medication Pricing Portal' (enCloud9 supported its development) and a 'pharmacist portal' (named as an outcome); not clear if they are the same thing, so both are kept as the page words them. Location Clearwater, FL taken from the page's details as reported by WebFetch; I did not get a separate exact quote for it. Industry is not a labeled field; 'Healthcare' is from the page's wording. Page has typos: 'PriceMDs need a system', 'accuracty', 'not handles by', and a garbled sentence 'continually adapting CRM to continuously adapting it'. No numbers or timeline, so tiles are empty. Conclusion calls it a long-term partnership focused on continuous improvement but states no specific next steps, so next_steps is null. No named client quote. Business Central appears only in site navigation and footer. Memory notes a separate PriceMDs client file exists; not used, all facts are from the page."
})

stories.append({
 "key": "tensionpa",
 "slug": "tension-pa-tension-packaging-expands-collaboration-with-encloud9-across-multiple-divisions",
 "client": "Tension Packaging and Automation",
 "work_type": "New build",
 "title": "Tension Packaging: Dynamics 365 Sales Rollout | enCloud9",
 "meta": "How enCloud9 moved a Tension Packaging division from spreadsheets to Dynamics 365 Sales in six months, with data migrated and a full view of the pipeline.",
 "h1": ["Tension Packaging:", "Spreadsheets to Dynamics 365 in six months"],
 "answer": "Tension Packaging and Automation, a Kansas City, MO packaging equipment and automation company, tracked a division's sales pipeline in Excel spreadsheets and individual storage. After an earlier project with one division, we implemented Dynamics 365 Sales for another and migrated its data to the cloud. The project was completed in six months, with better pipeline visibility and reporting.",
 "facts": [["Client", "Tension Packaging and Automation"], ["Location", "Kansas City, MO"], ["Industry", "Packaging equipment and automation"], ["Starting point", "Excel spreadsheets and individual desktop or cloud storage"], ["Products", "Dynamics 365 Sales"], ["Services", "Data Migration, Implementation Services"]],
 "timeline": "Completed in six months",
 "tiles": [["6 months", "to complete the project"]],
 "outcomes": [
  "The project was completed in six months.",
  "Productivity rose and management reporting improved.",
  "The team has a full view of the sales pipeline and related product interests.",
  "Product interests can now be connected to sales opportunities."],
 "chapters": [
  ["What did Tension Packaging need?", [
   "Tension Packaging and Automation is a leader in packaging equipment and automation systems, serving the eCommerce and Pharmacy markets. Its services include manufacturing, installation, packaging automation, consumables and robotics.",
   "Following a previous project with one division, Tension Packaging engaged enCloud9 for another project in a different division.",
   "That division was using Excel spreadsheets and individual desktop or cloud storage to manage its sales pipeline and documents. This led to inefficiencies and limited visibility into the overall pipeline. It needed a cloud-based way to manage leads, accounts, opportunities and contacts."]],
  ["What did we build?", [
   "We implemented Dynamics 365 Sales and migrated the division's data to the cloud. The system gives easy access to records and detailed tracking of market, industry and product interests.",
   "The implementation streamlined processes, improved reporting and increased overall productivity."]],
  ["What changed day to day?", [
   "The team now has a full view of the sales pipeline and related product interests, which makes sales opportunities easier to manage and track. Management gets better reporting. The client team's professionalism and engagement were key to the project's success and user adoption."]]],
 "next_steps": ["What comes next for Tension Packaging?", "Tension Packaging continues to work with enCloud9 for ongoing support and future enhancements."],
 "quote": None,
 "author": "Kristin Caniglia", "published": "2024-07-24", "published_h": "July 24, 2024",
 "sources": [
  S("Client name", "Tension Packaging and Automation"),
  S("Industry", "Tension Packaging and Automation is a leader in packaging equipment and automation systems,"),
  S("Markets", "catering to the eCommerce and Pharmacy markets."),
  S("Services offered", "They offer a wide range of services, including manufacturing, installation, packaging automation, consumables, and robotics"),
  S("Previous division", "Following the success of a previous project with one division,"),
  S("New division", "Tension Packaging decided to engage enCloud9 for another project in a different division of the company."),
  S("Starting point", "Tension Packaging was using Excel spreadsheets and individual desktop or cloud storage"),
  S("Problem", "This setup led to inefficiencies and limited visibility into their overall sales pipeline."),
  S("Need", "The company needed a more efficient, cloud-based solution to manage leads, accounts, opportunities, and contacts,"),
  S("Build", "enCloud9 implemented Dynamics 365 Sales to address Tension Packaging’s needs."),
  S("Migration", "The solution involved migrating their data to the cloud,"),
  S("Tracking", "providing easy access and detailed tracking of market, industry, and product interests."),
  S("Process gains", "This implementation streamlined their processes, improved reporting capabilities, and increased overall productivity."),
  S("Timeline / tile", "The project was successfully completed in six months,"),
  S("Outcome: productivity", "leading to a significant boost in productivity and better reporting for management."),
  S("Outcome: pipeline view", "The new system provided a comprehensive view of the sales pipeline and related product interests,"),
  S("Outcome: product to opportunity", "particularly the enhanced ability to connect product interests with sales opportunities."),
  S("Adoption", "The professionalism and engagement of the client team were key to the project’s success and user adoption."),
  S("Next steps", "Tension Packaging continues to collaborate with enCloud9 for ongoing support and future enhancements.")],
 "notes": "Page H1 is 'Tension Packaging Expands Dynamics 365 Collaboration Across Divisions'. The page does not say which division this was, or what the earlier project delivered. It says the company (not the division) used spreadsheets; I wrote 'a division's' in the answer because the project was for a different division; reword to 'the company' if that reads as going past the page. Industry is not a labeled field; taken from the overview. Location Kansas City, MO taken from the page details as reported by WebFetch, not a separate quote. Published July 24, 2024, the same date as the Schiff and MSA stories (likely a bulk upload date). No named client quote. Business Central appears only in site navigation and footer."
})

stories.append({
 "key": "schiff",
 "slug": "streamlining-sales-processes-the-schiff-groups-transformation-with-dynamics-365-by-encloud9",
 "client": "The Schiff Group",
 "work_type": "New build",
 "title": "The Schiff Group: Dynamics 365 Sales in a Month | enCloud9",
 "meta": "How enCloud9 implemented Dynamics 365 Sales for The Schiff Group, a government contracting consultancy, and moved its data to the cloud in one month.",
 "h1": ["The Schiff Group:", "Cloud-based sales in one month"],
 "answer": "The Schiff Group, a Rockville, MD firm that guides contractors through government contracting, lacked a comprehensive sales app to track pipelines and opportunities. We implemented Dynamics 365 Sales Hub for accounts, contacts, opportunities, opportunity products and email, and migrated their data. In one month they moved to a cloud-based system with one central platform for sales.",
 "facts": [["Client", "The Schiff Group"], ["Location", "Rockville, MD"], ["Industry", "Government contracting consulting"], ["Starting point", "No comprehensive sales app"], ["Products", "Dynamics 365 Sales; Team Member"], ["Services", "Implementation Services, Data Migration"]],
 "timeline": "Within one month",
 "tiles": [["1 month", "to move to a cloud-based system"]],
 "outcomes": [
  "In one month, The Schiff Group moved to a cloud-based system.",
  "Sales processes and communications are managed from one central platform.",
  "Operational efficiency improved significantly.",
  "The Opportunity Product feature improved how they track and manage sales opportunities."],
 "chapters": [
  ["What did The Schiff Group need?", [
   "The Schiff Group guides contractors through securing contracts with federal, state and local governments, and provides strategic consulting to help clients navigate government procurement.",
   "It needed a more effective way to manage customer communications and data. Without a comprehensive sales app, it was limited in tracking critical business information, including sales pipelines and opportunity details."]],
  ["What did we build?", [
   "We implemented Dynamics 365 Sales Hub to manage accounts, contacts, opportunities, opportunity products and email communications.",
   "The work included data migration so all relevant information carried into the new system."]],
  ["What changed day to day?", [
   "Within one month The Schiff Group was working in a cloud-based system, managing sales processes and communications from one central platform. The firm was particularly pleased with the Opportunity Product feature, which improved how it tracks and manages sales opportunities."]]],
 "next_steps": ["What comes next for The Schiff Group?", "The Schiff Group is continuing its partnership with enCloud9 for ongoing support and is considering additional integrations, such as with SharePoint."],
 "quote": None,
 "author": "Kristin Caniglia", "published": "2024-07-24", "published_h": "July 24, 2024",
 "sources": [
  S("Client overview", "The Schiff Group specializes in guiding contractors through the process of securing contracts"),
  S("Government", "with federal, state, and local governments."),
  S("Consulting", "They provide strategic consulting services to help clients navigate the complexities of government procurement."),
  S("Need", "The Schiff Group needed a more effective way to manage communications and data related to customers"),
  S("Starting point", "They lacked a comprehensive Sales App, which limited their ability to track and manage critical business information"),
  S("Pipeline detail", "including sales pipelines and opportunity details."),
  S("Build", "enCloud9 implemented Dynamics 365 Sales Hub to meet The Schiff Group’s needs."),
  S("Scope", "This solution provided functionalities for managing Accounts, Contacts, Opportunities, Opportunity Products"),
  S("Migration", "The implementation also included data migration to ensure all relevant information was seamlessly integrated"),
  S("Timeline / tile / outcome", "In just one month, The Schiff Group transitioned to a cloud-based system"),
  S("Outcome: central platform", "The new system provided a centralized platform for tracking and managing sales opportunities"),
  S("Outcome: efficiency", "significantly improving their operational efficiency."),
  S("Outcome: Opportunity Product", "The Schiff Group was particularly pleased with the Opportunity Product feature"),
  S("Opportunity Product effect", "which has improved their ability to track and manage sales opportunities."),
  S("Next: support", "They are continuing their partnership with enCloud9 for ongoing support"),
  S("Next: SharePoint", "are considering additional integrations, such as with SharePoint.")],
 "notes": "Page H1 is 'How The Schiff Group Transformed Sales with Dynamics 365'. Body says 'Dynamics 365 Sales Hub' while the products list says 'Dynamics 365 Sales' and 'Team Member'. The page does not say what system they used before, only that they lacked a comprehensive sales app; Starting point reflects that. Industry is not a labeled field; taken from the overview. Location Rockville, MD from the page details as reported by WebFetch, not a separate quote. No named client quote. Business Central appears only in site navigation and footer."
})

stories.append({
 "key": "msa",
 "slug": "msa-source-transforms-compliance-operations-with-encloud9s-tailored-solutions",
 "client": "MSA Source",
 "work_type": "Rescue or fix",
 "title": "MSA Source: Better Reporting and Seed Money Math | enCloud9",
 "meta": "How enCloud9 improved MSA Source's CRM after another partner's build, adding Document Core Pack reports, a Seed Money calculation and dashboards.",
 "h1": ["MSA Source:", "More accurate reporting, simpler tracking"],
 "answer": "MSA Source, a Brandon, FL company specializing in Medicare Secondary Payer compliance, had a CRM from another partner that relied heavily on Power Automate Flows and Word documents for reporting. We deployed Document Core Pack for reports and email templates, built a Seed Money Allocation calculation and added status dashboards. Reporting accuracy and data tracking improved.",
 "facts": [["Client", "MSA Source"], ["Location", "Brandon, FL"], ["Industry", "Medicare Secondary Payer compliance"], ["Starting point", "A previous CRM implementation by another partner, heavily reliant on Power Automate Flows"], ["Products", "Dynamics 365 Sales; Team Member; Click2Clone; Document Core Pack; MS CRM Add ons"], ["Services", "Enhanced Support for Specific Tasks"]],
 "timeline": None,
 "tiles": [["1 month", "typical length of each ongoing support project"]],
 "outcomes": [
  "Reporting accuracy improved.",
  "Data tracking is simpler.",
  "The team has clear insight into the status of its projects.",
  "The Seed Money Calculation and dashboards were particularly well received and significantly improved operational efficiency."],
 "chapters": [
  ["What was wrong with MSA Source's CRM?", [
   "MSA Source specializes in Medicare Secondary Payer compliance, helping clients navigate the claims process and manage their responsibilities efficiently and accurately.",
   "Its previous CRM implementation, built by another partner, relied heavily on Power Automate Flows and was inadequate for the company's complex reporting and data processing needs. Complex reports were built in Microsoft Word documents, which proved insufficient. The team struggled to calculate Seed Money Allocations accurately and needed help with templated emails and process flows."]],
  ["What did we change?", [
   "We deployed Document Core Pack for complex reports, replacing the Word-based system, and used it to create email templates for more consistent communication.",
   "We designed a precise solution for the complex Seed Money Allocation calculations, and built dashboards that group data by status stage."]],
  ["What changed day to day?", [
   "MSA Source has a more streamlined and efficient system. Reporting is more accurate, data tracking is simpler and the team can see the status of its projects clearly. The Seed Money Calculation and dashboards were particularly well received."]]],
 "next_steps": ["What comes next for MSA Source?", "MSA Source continues to work with enCloud9 for ongoing support and further enhancements, with projects typically spanning one month at a time. Budget may shape the scope of future work, and MSA Source sees room for continued improvement."],
 "quote": None,
 "author": "Kristin Caniglia", "published": "2024-07-24", "published_h": "July 24, 2024",
 "sources": [
  S("Client overview", "MSA Source is an innovative company specializing in Medicare Secondary Payer compliance"),
  S("Claims", "helping clients navigate the complex claims process with confidence"),
  S("Previous partner", "MSA Source faced several challenges with their previous CRM implementation by another partner."),
  S("Flows", "heavily reliant on Power Automate Flows"),
  S("Inadequate", "was inadequate for handling the company's complex reporting and data processing needs"),
  S("Word reporting", "They used Microsoft Word Documents for complex reporting, which proved insufficient."),
  S("Seed Money problem", "they struggled with accurately calculating Seed Money Allocations"),
  S("Templates need", "needed assistance with templated emails and process flow improvements"),
  S("Document Core Pack", "Document Core Pack: Deployed for creating complex reports, replacing the inadequate Microsoft Word-based system."),
  S("Seed Money fix", "Seed Money Calculation: Designed a precise solution for handling the complex Seed Money Allocation calculations"),
  S("Email templates", "Email Templates: Created efficient email templates using Document Core Pack, improving communication consistency."),
  S("Dashboards", "Dashboards: Developed dashboards to compartmentalize data in various status stages"),
  S("Outcome: streamlined", "The collaboration with enCloud9 resulted in a more streamlined and efficient system for MSA Source."),
  S("Outcome: accuracy and tracking", "The new tools and processes improved reporting accuracy, simplified data tracking"),
  S("Outcome: status insight", "provided clear insights into the status of various projects"),
  S("Outcome: well received", "The enhanced Seed Money Calculation and detailed dashboards were particularly well-received"),
  S("Outcome: efficiency", "significantly improving operational efficiency"),
  S("Next: ongoing", "The company continues to work with enCloud9 for ongoing support and further enhancements"),
  S("Tile: one month", "with projects typically spanning one month at a time"),
  S("Next: budget", "While budget considerations may influence the scope of future work"),
  S("Next: potential", "MSA Source recognizes the potential for continued improvements and values the partnership with enCloud9")],
 "notes": "Page H1 is 'MSA Source Transforms Compliance with Dynamics 365'. Rescue or fix fits: the page says the previous partner's implementation was inadequate. The 1 month tile is the typical length of each ongoing support project, not the original project; no project timeline is stated, so timeline is null. Drop the tile if the template wants project figures only. 'MS CRM Add ons' and 'Click2Clone' are in the products list but the story body never mentions them. The page does not explicitly name Dynamics 365 as the previous partner's platform in the challenge text; the H1 and products list say Dynamics 365. Location Brandon, FL from the page details as reported by WebFetch, not a separate quote. No named client quote. Business Central appears only in site navigation and footer."
})

DASH = re.compile("[–—]")
ok = True
for s in stories:
    t = s["title"]; m = s["meta"]; a = s["answer"]
    wc = len(a.split())
    print(s["key"], "title", len(t), "meta", len(m), "answer words", wc, "h1b words", len(s["h1"][1].split()))
    if len(t) > 60 or not (120 <= len(m) <= 160) or not (40 <= wc <= 60) or not m.startswith("How enCloud9"): ok=False; print("  FAIL")
    if not (2 <= len(s["h1"][1].split()) <= 7): ok=False; print("  FAIL h1")
    # dash check on non-source fields
    chk = {k:v for k,v in s.items() if k != "sources"}
    if DASH.search(json.dumps(chk, ensure_ascii=False)): ok=False; print("  DASH in fields")
    if DASH.search(json.dumps(s["sources"], ensure_ascii=False)): print("  note: dash in sources")
    if "Business Central" in json.dumps({k:v for k,v in s.items() if k!="notes"}): ok=False; print("  BC!")
if not ok: sys.exit(1)
if len(sys.argv) > 1 and sys.argv[1] == "write":
    for s in stories:
        with open(OUT + s["key"] + ".json", "w", encoding="utf-8") as f:
            json.dump(s, f, ensure_ascii=False, indent=1)
    print("written")
