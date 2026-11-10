import json, re, sys

OUT = "/home/claude/lb/stories-data/"
S = lambda c, q: {"claim": c, "quote": q.replace("'", "\u2019")}
stories = []

stories.append({
 "key": "jasco",
 "slug": "jasco-modernizes-operations-with-dynamics-365-sales-and-customer-service",
 "client": "JASCO, Inc.",
 "work_type": "Upgrade",
 "title": "JASCO: Modern CRM in three months | enCloud9",
 "meta": "How enCloud9 moved JASCO off an outdated on-premises Dynamics 365 system to Dynamics 365 Sales with over 900 automated lead assignment rules.",
 "h1": ["JASCO:", "Modern CRM in three months"],
 "answer": "JASCO, Inc. is an analytical instruments maker in Easton, MD that operates in 57 countries. It was held back by an outdated on-premises Dynamics 365 system. We implemented Dynamics 365 Sales with a Lead Assignment Rule Table of over 900 rules and updated form captures. In three months, sales and lead management became centralized and automated.",
 "facts": [["Client", "JASCO, Inc."], ["Location", "Easton, MD"], ["Industry", "Analytical instruments (chromatography and molecular spectroscopy)"], ["Starting point", "Outdated on-premises Dynamics 365 system"], ["Products", "Dynamics 365 Sales Enterprise; Dynamics 365 Customer Service; ClickDimensions"], ["Services", "Cloud Migration, Marketing Services, Support Contract, Customization and Development"]],
 "timeline": "Within three months",
 "tiles": [["3 months", "to complete the project"], ["900+", "lead assignment rules"], ["57", "countries JASCO operates in"]],
 "outcomes": ["The project was completed in three months.", "Sales and lead management now run in one centralized, automated system.", "Lead assignments are automated and data management improved.", "Efficiency and customer interaction have greatly improved."],
 "chapters": [
  ["What was wrong with JASCO's CRM?", ["JASCO, Inc. makes analytical instruments, specializing in chromatography and molecular spectroscopy. It operates in 57 countries and serves manufacturers and research labs.", "JASCO was struggling with an outdated on-premises Dynamics 365 system. It needed a modern CRM to improve efficiency and streamline its processes."]],
  ["What did we change?", ["We implemented Dynamics 365 Sales, including a Lead Assignment Rule Table with over 900 rules, and updated JASCO's form captures.", "This automated lead assignments and improved data management."]],
  ["What changed day to day?", ["JASCO now has a centralized, automated system for sales and lead management, which has greatly improved efficiency and customer interaction."]]
 ],
 "next_steps": ["What comes next for JASCO?", "JASCO continues to work with us on ongoing enhancements, including potential integrations such as Adobe Sign and international lead management."],
 "quote": None,
 "author": "Kristin Caniglia", "published": "2023-10-30", "published_h": "October 30, 2023",
 "sources": [
  S("Client and location", "JASCO,Inc / Easton, MD"),
  S("Industry", "JASCO Inc., a global leader in analytical instruments, specializes in chromatography and molecular spectroscopy."),
  S("57 countries, who it serves", "Operating in 57 countries, they provide advanced solutions to manufacturers and research labs."),
  S("Starting point", "Jasco struggled with an outdated On-Premises Dynamics 365 system"),
  S("Need", "They needed a modern CRM solution to improve efficiency and streamline processes"),
  S("What we did, 900 rules", "enCloud9 implemented Dynamics 365 Sales, including a Lead Assignment Rule Table with over 900 rules"),
  S("Form captures", "updated form captures"),
  S("Automation result", "This solution automated lead assignments and improved data management"),
  S("Timeline", "Completed in three months"),
  S("Centralized system result", "providing a centralized, automated system for sales and lead management."),
  S("Efficiency result", "This has greatly improved efficiency and customer interaction."),
  S("Next steps", "Jasco continues to work with enCloud9 for ongoing enhancements"),
  S("Next steps detail", "potential integrations like Adobe Sign and international lead management"),
  S("Products", "Dynamics 365 Sales Enterprise / Dynamics 365 Customer Service / ClickDimensions"),
  S("Services", "Cloud Migration / Marketing Services / Support Contract / Customization and Development")
 ],
 "notes": "Off-limits ERP product: the page's Products Used list names a fourth product, the Microsoft ERP product we must not use; it is left out of every field. The services list also includes 'ERP Integration', which ties to that product; dropped from Services for the same reason (exact page list has five services). Hub product 'Click' is ClickDimensions on the page. Dynamics 365 Customer Service appears only in Products Used and tags; the body describes only a Sales implementation, so no Customer Service work is claimed. Page calls the old system 'On-Premises Dynamics 365' (odd wording, kept as on-premises Dynamics 365). Client written as 'JASCO,Inc', 'JASCO Inc.' and 'Jasco'; I used 'JASCO, Inc.' / 'JASCO'. Page H1 is 'Jasco Boosts Sales and Service with Dynamics 365'. Header image alt text reads 'Elmwood Reclaimed Timber' (leftover from another story). Page shows a modified date of August 13, 2026. Work type kept as Upgrade (on-premises to modern Dynamics 365 Sales). WebFetch would not return full verbatim text; quotes are short excerpts it returned."
})

stories.append({
 "key": "rlh",
 "slug": "investment-firm-uses-dynamics-365-mobile-to-stay-connected",
 "client": "RLH (Riordan, Lewis, and Haden)",
 "work_type": "Upgrade",
 "title": "RLH: Dynamics 365 on the go | enCloud9",
 "meta": "How enCloud9 moved RLH, a Los Angeles private equity firm, from on-premises CRM to cloud Dynamics 365 and customized the mobile app for meetings.",
 "h1": ["RLH:", "Client data on the go"],
 "answer": "RLH (Riordan, Lewis, and Haden) is a private equity firm headquartered in Los Angeles. It needed strong client communication and efficient information flow to a global client base. We migrated its on-premises CRM to cloud-based Dynamics 365 and customized the mobile app. End-user engagement rose, and staff now get instant access to vital data.",
 "facts": [["Client", "RLH (Riordan, Lewis, and Haden)"], ["Location", "Los Angeles, CA"], ["Industry", "Private equity (business services, healthcare, and government services)"], ["Starting point", "On-premises CRM system"], ["Products", "Dynamics 365 Mobile"], ["Services", "Implementation Services"]],
 "timeline": None,
 "tiles": [["40+ years", "in private equity"]],
 "outcomes": ["End-user engagement has risen significantly.", "Staff have instant access to vital data for client interactions.", "Management has better insight into employee activities.", "Creating and accessing meeting notes and follow-up information is more efficient."],
 "chapters": [
  ["What did RLH need?", ["RLH (Riordan, Lewis, and Haden) is a private equity firm headquartered in Los Angeles, with a history of over four decades. It invests across business services, healthcare, and government services.", "RLH needed to maintain strong client communication and efficient information flow to a global client base."]],
  ["What did we change?", ["We migrated RLH's on-premises CRM system to cloud-based Dynamics 365.", "We customized the Dynamics 365 mobile app to deliver key information on the go, supporting client interactions and meetings."]],
  ["What changed day to day?", ["End-user engagement has risen significantly. Staff have instant access to vital data, management has better insight into employee activities, and meeting notes and follow-up information are faster to create and find."]]
 ],
 "next_steps": None,
 "quote": None,
 "author": "Kristin Caniglia", "published": "2018-05-01", "published_h": "May 1, 2018",
 "sources": [
  S("Client, industry, location", "RLH (Riordan, Lewis, and Haden), a renowned private equity firm headquartered in Los Angeles"),
  S("Location line", "Los Angeles, CA"),
  S("Four decades", "With a rich legacy spanning over four decades,"),
  S("Sectors", "business services, healthcare, and government services"),
  S("Challenge", "maintaining robust client communication channels"),
  S("Global client base", "Ensuring seamless connectivity and efficient information flow to a global client base became a strategic imperative."),
  S("Mobile customization", "We meticulously customized the Dynamics 365 mobile app to deliver mission-critical information on the go"),
  S("Meetings", "facilitating client interactions and strategic meetings"),
  S("Migration", "migration of RLH's on-premises CRM system to Dynamics 365's agile cloud-based platform"),
  S("Engagement result", "End-user engagement has surged significantly"),
  S("Data access result", "instant access to vital data"),
  S("Management insight result", "RLH's management now enjoys enhanced insights into employee activities"),
  S("Meeting notes result", "the efficiency of creating and accessing meeting notes and follow-up information has soared"),
  S("Products", "Dynamics 365 Mobile"),
  S("Services", "Implementation Services")
 ],
 "notes": "Page H1: 'RLH Boosts Productivity and Engagement with Dynamics 365'. Product 'Dynamics 365 Mobile' is the page's own label (Microsoft does not sell a product by that name; it is the Dynamics 365 mobile app). Work type kept as Upgrade: the page describes an on-premises CRM migrated to cloud Dynamics 365, which fits; the listed service is 'Implementation Services'. The 40+ years tile is a fact about the firm, not a project result; drop it if tiles should be project-only. No timeline, numbers or named quote on the page. WebFetch would not return full verbatim text."
})

stories.append({
 "key": "jwc",
 "slug": "manufacturer-integrates-website-with-crm-to-automate-lead-assignment",
 "client": "JWC Environmental",
 "work_type": "Integration",
 "title": "JWC Environmental: Web leads auto-assigned | enCloud9",
 "meta": "How enCloud9 connected JWC Environmental's website leads to Dynamics 365 Sales and assigned them automatically by customer interest and geography.",
 "h1": ["JWC Environmental:", "Website leads assigned automatically"],
 "answer": "JWC Environmental, based in Santa Ana, has made municipal wastewater equipment since 1973. Dozens of website leads arrived daily and needed a more sophisticated lead management system. We worked with JWC's web development team to connect web leads to Dynamics 365 and assign them automatically. The team saves time and responds faster to opportunities.",
 "facts": [["Client", "JWC Environmental"], ["Location", "Santa Ana"], ["Industry", "Municipal wastewater equipment"], ["Starting point", "Dozens of daily website leads; ClickDimensions Marketing Automation already in place"], ["Products", "Dynamics 365 Sales"], ["Services", "Implementation Service"]],
 "timeline": None,
 "tiles": [["Since 1973", "making wastewater equipment"]],
 "outcomes": ["The team saves substantial time managing leads and contacts.", "Automated lead distribution and assignment improved responsiveness to business opportunities.", "Efficiency and productivity increased."],
 "chapters": [
  ["What did JWC need?", ["JWC Environmental has made municipal wastewater equipment since 1973, offering waste reduction and screening solutions.", "Leads arrived through its website every day, often in the dozens. JWC had already integrated ClickDimensions Marketing Automation, but it needed a more sophisticated lead management system."]],
  ["What did we build?", ["We worked closely with JWC Environmental's web development team to connect web-generated leads to Microsoft Dynamics 365.", "Leads are assigned automatically based on factors such as customer interests and geography."]],
  ["What changed day to day?", ["JWC manages leads and contacts with far less effort, saving substantial time so the team can focus on high-value work. Automated lead distribution and assignment made the team more responsive to new business opportunities."]]
 ],
 "next_steps": None,
 "quote": None,
 "author": "Kristin Caniglia", "published": "2018-05-01", "published_h": "May 1, 2018",
 "sources": [
  S("Client, industry, since 1973", "JWC Environmental, a trailblazer in municipal wastewater equipment since its inception in 1973,"),
  S("Location", "Santa Ana"),
  S("Solutions", "reliable and high-performance waste reduction and screening solutions"),
  S("Daily leads", "a daily surge of leads through their website, often numbering in dozens"),
  S("ClickDimensions in place", "had previously integrated ClickDimensions Marketing Automation"),
  S("Need", "it became apparent that a more sophisticated lead management system was imperative"),
  S("Web team", "collaborated closely with JWC Environmental's web development team"),
  S("Integration", "establish a seamless integration between web-generated leads and Microsoft Dynamics 365"),
  S("Assignment rules", "intelligently assigning leads based on factors such as customer interests and geographic parameters"),
  S("Time savings result", "the company has unlocked substantial time savings,"),
  S("High-value work", "empowering their team to concentrate on high-value activities."),
  S("Responsiveness result", "The automation of lead distribution and assignment has significantly improved responsiveness"),
  S("Efficiency result", "JWC experiences a surge in efficiency and productivity"),
  S("Products", "Dynamics 365 Sales"),
  S("Services", "Implementation Service")
 ],
 "notes": "Page gives no state for Santa Ana; left as 'Santa Ana' (not adding CA). Page has a typo 'wnCloud9' in the results sentence. Services list is singular 'Implementation Service' on the page. Page H1: 'JWC Transforms Lead Management with Dynamics 365'. The 'Since 1973' tile is a company fact, not a project result. Work type Integration matches the page (website to CRM integration). No timeline, figures or named quote. WebFetch would not return full verbatim text."
})

stories.append({
 "key": "aureon",
 "slug": "encloud9-helps-professional-employer-organization-peo-rescue-a-failed-crm",
 "client": "Aureon",
 "work_type": "Rescue or fix",
 "title": "Aureon: A failed CRM rescued | enCloud9",
 "meta": "How enCloud9 audited and rebuilt Aureon's self-implemented Dynamics CRM in Des Moines so staff could rely on Dynamics 365 for real-time information.",
 "h1": ["Aureon:", "A failed CRM rescued"],
 "answer": "Aureon is a business support services firm headquartered in Des Moines, IA. Years earlier it implemented Dynamics CRM without professional guidance, which led to underuse and reliability issues. We ran a systems audit and process review with Aureon and built a CRM enhancement plan. For the first time, staff can rely on Dynamics 365.",
 "facts": [["Client", "Aureon"], ["Location", "Des Moines, IA"], ["Industry", "Business support services"], ["Starting point", "Dynamics CRM implemented without professional guidance; underused and unreliable"], ["Products", "Dynamics 365"], ["Services", "Dynamics 365 Optimization, Rescue and Repair"]],
 "timeline": None,
 "tiles": [],
 "outcomes": ["For the first time in its history, Aureon can rely on Dynamics 365 for real-time, relevant information.", "Staff can manage client relationships in Dynamics 365.", "The work improved operational efficiency and client engagement potential."],
 "chapters": [
  ["What was wrong with Aureon's CRM?", ["Aureon is a business support services firm headquartered in Des Moines, IA. It was founded in 1986 as Iowa Network Services to connect independent telephone companies, and rebranded in 2016.", "Several years earlier, Aureon implemented Dynamics CRM without professional guidance. The system struggled to meet its requirements, which led to underuse and reliability issues."]],
  ["What did we change?", ["We started with a thorough systems audit and a process review, done together with Aureon.", "From that work we built a CRM enhancement plan aimed at Aureon's specific challenges."]],
  ["What changed day to day?", ["For the first time in its history, Aureon and its staff can rely on Dynamics 365 for real-time, relevant information, and use it to manage client relationships."]]
 ],
 "next_steps": None,
 "quote": None,
 "author": "Kristin Caniglia", "published": "2018-05-01", "published_h": "May 1, 2018",
 "sources": [
  S("Client, industry, location", "Aureon, a prominent Business Support services firm headquartered in Des Moines"),
  S("Location line", "Des Moines, IA"),
  S("Founded as", "Founded originally as Iowa Network Services"),
  S("Founded year", "since its establishment in 1986"),
  S("Original mission", "primary mission was to facilitate connectivity among independent telephone companies (ITCs)"),
  S("Rebrand", "a strategic rebranding initiative in 2016 marked the beginning"),
  S("Starting point", "Several years ago, they implemented Dynamics CRM without the guidance of professional expertise."),
  S("Requirements not met", "struggled to meet their intricate requirements"),
  S("Underuse and reliability", "resulting in underutilization and issues of reliability."),
  S("Audit and review", "a thorough systems audit and a comprehensive process review"),
  S("Enhancement plan", "construct a comprehensive CRM enhancement plan"),
  S("First time result", "For the first time in their history, Aureon and its dedicated workforce can confidently rely on Dynamics 365"),
  S("Real-time result", "deliver real-time, pertinent information"),
  S("Client relationships result", "effectively manage client relationships"),
  S("Efficiency result", "operational efficiency and client engagement potential"),
  S("Products", "Dynamics 365"),
  S("Services", "Dynamics 365 Optimization / Rescue and Repair")
 ],
 "notes": "The slug says 'professional employer organization (PEO)', but the page body never mentions PEO; it calls Aureon a 'Business Support services firm'. Industry follows the page, not the slug. Page H1: 'enCloud9 Helps Aureon Rescue a Failed CRM'. The page does not say the original CRM 'failed' in the body beyond underuse and reliability issues; 'failed CRM' comes from the H1. No timeline, figures, next steps or named quote. 'Client engagement potential' outcome is page wording; paraphrased mildly. WebFetch would not return full verbatim text."
})

stories.append({
 "key": "rei",
 "slug": "manufacturing-company-upgrades-to-dynamics-365-transforms-sales-process",
 "client": "Radio Engineering Industries, Inc. (REI)",
 "work_type": "Upgrade",
 "title": "REI: From Dynamics 2011 to Dynamics 365 | enCloud9",
 "meta": "How enCloud9 moved Omaha manufacturer REI from on-premises Dynamics 2011 to Dynamics 365 Online with sales processes for its five divisions.",
 "h1": ["REI:", "Sales moved into Dynamics 365"],
 "answer": "Radio Engineering Industries (REI) in Omaha, NE makes audio, video and safety systems for the school and tour bus industry. Its on-premises Dynamics 2011 CRM had grown outdated and user acceptance was low. We migrated REI to Dynamics 365 Online, built sales processes for its five divisions and added dashboards. User acceptance and productivity increased.",
 "facts": [["Client", "Radio Engineering Industries, Inc. (REI)"], ["Location", "Omaha, NE"], ["Industry", "Manufacturing (audio, video, and safety systems for the school and tour bus industry)"], ["Starting point", "Outdated on-premises Dynamics 2011 CRM"], ["Products", "Dynamics 365 Sales"], ["Services", "Implementation Services"]],
 "timeline": None,
 "tiles": [["5", "divisions with their own sales processes"]],
 "outcomes": ["Workflows are streamlined and more efficient.", "Accessibility improved across the organization.", "User acceptance and productivity increased.", "Management gained insight into sales trends through dashboards."],
 "chapters": [
  ["What was wrong with REI's CRM?", ["Radio Engineering Industries, Inc. (REI) is headquartered in Omaha and manufactures audio, video, and safety systems for the school and tour bus industry.", "REI's on-premises Dynamics 2011 CRM had grown outdated, which led to low user acceptance. REI wanted to move to Dynamics 365 Online and shift from mostly offline processes to a CRM-centered approach."]],
  ["What did we change?", ["We migrated REI to Dynamics 365 Online.", "We designed and implemented structured sales processes in Dynamics 365 Sales to fit the needs of REI's five divisions, and built dashboards that give management insight into sales trends."]],
  ["What changed day to day?", ["REI's sales work now runs on streamlined, more efficient workflows, with better accessibility across the organization and higher user acceptance and productivity."]]
 ],
 "next_steps": None,
 "quote": None,
 "author": "Kristin Caniglia", "published": "2018-05-01", "published_h": "May 1, 2018",
 "sources": [
  S("Client and location", "Radio Engineering Industries, Inc. (REI), headquartered in Omaha"),
  S("Location line", "Omaha, NE"),
  S("Industry", "foremost manufacturer specializing in cutting-edge audio, video, and safety systems"),
  S("Market", "meticulously tailored for the school and tour bus industry"),
  S("Starting point", "Their existing Dynamics 2011 on-premise CRM system, once a cornerstone of their operations, had grown outdated"),
  S("Low acceptance", "This unfortunate circumstance led to suboptimal user acceptance"),
  S("Goal", "REI embarked on a mission to transition to Dynamics 365 Online"),
  S("Offline to CRM", "shift from predominantly offline processes to a CRM-centric approach"),
  S("Migration", "executing a meticulous migration"),
  S("Sales processes", "design and implement structured sales processes"),
  S("Five divisions", "cater to the distinct needs and intricacies of REI's five distinct divisions"),
  S("Dashboards", "These dashboards provided REI's management team with valuable insights into sales trends"),
  S("Workflow result", "The implementation of Dynamics 365 has ushered in a new era of streamlined, highly efficient workflows."),
  S("Accessibility result", "significantly improved accessibility across the organization"),
  S("Acceptance result", "The end result has been a notable increase in user acceptance and productivity."),
  S("Products", "Dynamics 365 Sales"),
  S("Services", "Implementation Services")
 ],
 "notes": "Page H1: 'REI Transforms Sales Process with Dynamics 365' (meta title 'REI Streamlines Sales Process with Dynamics 365 CRM'). Page says 'on-premise' (no s); written as on-premises. Page shows a modified date of August 13, 2026. The '5 divisions' tile is a count stated on the page. No timeline, figures or named quote. Work type Upgrade matches (Dynamics 2011 to Dynamics 365 Online). WebFetch would not return full verbatim text."
})

stories.append({
 "key": "bsi",
 "slug": "dynamics-365-implementation-allows-sales-and-management-teams-to-work-more-productively",
 "client": "Biometric Signature ID (BSI)",
 "work_type": "New build",
 "title": "BSI: One view of the sales pipeline | enCloud9",
 "meta": "How enCloud9 implemented Dynamics 365 Sales for Biometric Signature ID with custom process flows and real-time dashboards, from first lead to close.",
 "h1": ["BSI:", "One view from lead to close"],
 "answer": "Biometric Signature ID (BSI) is a biometric security software company in Lewisville, TX. It needed one system to track and improve its whole sales process, from first lead to closed deal. We implemented Microsoft Dynamics 365 with custom business process flows and real-time dashboards. BSI now has better pipeline management and less manual effort.",
 "facts": [["Client", "Biometric Signature ID (BSI)"], ["Location", "Lewisville, TX"], ["Industry", "Biometric security software"], ["Starting point", "No integrated system to track the sales process from lead to close"], ["Products", "Dynamics 365 Sales"], ["Services", "Implementation Services"]],
 "timeline": None,
 "tiles": [["15+ years", "in biometric security"]],
 "outcomes": ["Sales pipeline management improved.", "Manual effort dropped.", "Overall sales efficiency increased.", "Management has real-time insight into sales activities."],
 "chapters": [
  ["What did BSI need?", ["Biometric Signature ID (BSI) builds software tools for security and serves sectors such as education and finance. It is an emerging startup and a Microsoft partner with over 15 years in biometric security.", "BSI needed a way to track and improve its entire sales process, from initial lead generation to closing opportunities, and chose us to implement Microsoft Dynamics 365."]],
  ["What did we build?", ["We built customized business process flows in Dynamics 365.", "We also built dashboards that give BSI's management team real-time insight into sales activities."]],
  ["What changed day to day?", ["Lead management and opportunity tracking are simpler. BSI has better sales pipeline management, less manual effort, and higher overall sales efficiency."]]
 ],
 "next_steps": None,
 "quote": None,
 "author": "Kristin Caniglia", "published": "2018-05-01", "published_h": "May 1, 2018",
 "sources": [
  S("Client", "Biometric Signature ID (BSI)"),
  S("Location line", "Lewisville, TX"),
  S("Industry", "specializing in innovative software tools designed to revolutionize security measures"),
  S("Sectors", "across sectors such as Education, Finance, and more"),
  S("Startup and partner", "As an emerging startup and a trusted Microsoft partner,"),
  S("15 years", "a rich legacy of over 15 years in the field of biometric security solutions"),
  S("Need", "a comprehensive solution to meticulously track and optimize the entire sales process"),
  S("Lead to close", "spanning from initial lead generation to the successful closure of opportunities"),
  S("Chose enCloud9", "BSI chose enCloud9 to implement Microsoft Dynamics 365, the ideal foundation for their vision."),
  S("Process flows", "the meticulous crafting of customized business process flows"),
  S("Dashboards", "These dashboards provide BSI's management team with real-time insights into sales activities"),
  S("Simpler tracking", "By simplifying lead management and opportunity tracking, BSI has achieved improved sales pipeline management,"),
  S("Manual effort and efficiency", "reduced manual effort, and increased overall sales efficiency."),
  S("Products", "Dynamics 365 Sales"),
  S("Services", "Implementation Services")
 ],
 "notes": "Page H1: 'Dynamics 365 Enhances Productivity for BSI Sales and Management Teams' (meta title 'BSI Boosts Sale Productivity with Dynamics 365', typo 'Sale'). Body says 'Located in the thriving heart of Texas'; 'Lewisville, TX' appears only in the header block. Page also shows 'Tuesday, July 23, 2024 12:28 PM', which looks like a render timestamp; publish date used is May 1, 2018. The '15+ years' tile is a company fact, not a project result. Starting point is inferred from the stated need (page does not name a prior system). Work type New build kept (no prior CRM named). No timeline, figures or named quote. WebFetch would not return full verbatim text."
})

stories.append({
 "key": "ppc",
 "slug": "encloud9-enables-design-company-to-work-more-productively-and-efficiently-after-digitally-transforming-various-processes",
 "client": "PPC Flexible Packaging",
 "work_type": "New build",
 "title": "PPC Flex: Artwork jobs tracked in CRM | enCloud9",
 "meta": "How enCloud9 replaced PPC Flex's manual client artwork process with a Dynamics 365 tracking system for requests, estimates, design and artist schedules.",
 "h1": ["PPC Flex:", "Artwork jobs tracked in Dynamics 365"],
 "answer": "PPC Flexible Packaging is a flexible packaging manufacturer in Buffalo Grove, Illinois. Its manual process for managing client artwork had become outdated. We built a Dynamics 365 tracking system for client requests, job estimates and the full design process, with a dashboard and a due-date calendar. PPC expects to save hundreds of hours annually.",
 "facts": [["Client", "PPC Flexible Packaging (PPC Flex)"], ["Location", "Buffalo Grove, IL"], ["Industry", "Flexible packaging manufacturing"], ["Starting point", "Manual, outdated processes for managing client artwork"], ["Products", "Dynamics 365 Sales"], ["Services", "Implementation Services"]],
 "timeline": None,
 "tiles": [["Hundreds of hours", "expected to be saved each year"]],
 "outcomes": ["PPC manages all its jobs in Dynamics 365 through a dashboard.", "A calendar organizes jobs by due date and assigns them to the responsible artists.", "The system is expected to save hundreds of hours annually."],
 "chapters": [
  ["What did PPC Flex need?", ["PPC Flexible Packaging, formerly known as Packaging Products, makes flexible packaging in Buffalo Grove, Illinois, including consumer, cleanroom, and floral and gift packaging.", "PPC saw that some of its processes had become outdated and needed to digitize and streamline its manual processes to stay competitive. Many clients depend on PPC's design services, so a smooth system for client artwork was essential."]],
  ["What did we build?", ["We started with PPC's manual process for managing client artwork.", "Using Microsoft Dynamics 365, we built a tracking system that manages client requests, job estimates, and the entire design process."]],
  ["What changed day to day?", ["PPC now manages all its jobs in Dynamics 365 through a dashboard, with a calendar that organizes jobs by due date and assigns them to the responsible artists. The system is expected to save hundreds of hours annually."]]
 ],
 "next_steps": None,
 "quote": None,
 "author": "Kristin Caniglia", "published": "2018-05-01", "published_h": "May 1, 2018",
 "sources": [
  S("Client, location, industry", "Located in Buffalo Grove, Illinois, PPC Flexible Packaging is a leader in high-quality flexible packaging manufacturing."),
  S("Product lines", "PPC offers a wide range of products, including consumer packaging, cleanroom packaging, and floral/gift packaging."),
  S("Former name", "Formerly known as Packaging Products, PPC partnered with enCloud9"),
  S("Outdated processes", "PPC, always looking ahead, realized that some of their processes had become outdated."),
  S("Digitize to compete", "they knew they needed to digitize and streamline their manual processes to stay competitive."),
  S("Design services", "Many clients depend on PPC's design services, so a smooth and efficient system was essential."),
  S("Artwork first", "The first step was to overhaul their manual processes for managing client artwork"),
  S("Built with Dynamics 365", "Using Microsoft Dynamics 365, enCloud9 created a sophisticated tracking system."),
  S("System scope", "This system manages client requests, job estimates, and the entire design process"),
  S("Dashboard result", "PPC can now manage all their jobs through Dynamics 365, accessible via an intuitive dashboard."),
  S("Calendar result", "includes a calendar that organizes jobs by due date and assigns them to responsible artists."),
  S("Hours saved", "is expected to save hundreds of hours annually."),
  S("Products", "Dynamics 365 Sales"),
  S("Services", "Implementation Services")
 ],
 "notes": "Client is named three ways on the page: 'PPC Flex' (H1), 'PPC Flexible Packaging' (overview) and formerly 'Packaging Products'. Used PPC Flexible Packaging as client, PPC Flex in title and H1 to match the hub. Location: page writes 'Buffalo Grove, Illinois' in the body; written as IL in facts to match the City, ST format. Slug calls PPC a 'design company'; the page calls it a flexible packaging manufacturer. Page also says 'PPC Flex has enjoyed a long-standing partnership with enCloud9' (not used as an outcome). 'Hundreds of hours' is a projection, worded as expected. Page H1: 'PPC Flex Boosts Productivity and Efficiency with Dynamics 365'. No timeline, next steps or named quote. WebFetch would not return full verbatim text."
})

# validation
bad = False
for s in stories:
    blob = json.dumps(s, ensure_ascii=False)
    errs = []
    if "—" in blob or "–" in blob: errs.append("dash")
    if "Business Central" in blob: errs.append("BC")
    if len(s["title"]) > 60: errs.append(f"title {len(s['title'])}")
    if not 120 <= len(s["meta"]) <= 160: errs.append(f"meta {len(s['meta'])}")
    if not s["meta"].startswith("How enCloud9"): errs.append("meta start")
    wc = len(s["answer"].split())
    if not 40 <= wc <= 60: errs.append(f"answer {wc}")
    h = len(s["h1"][1].split())
    if not 2 <= h <= 7: errs.append(f"h1 {h}")
    if not 2 <= len(s["outcomes"]) <= 5: errs.append("outcomes")
    if len(s["tiles"]) > 3: errs.append("tiles")
    print(s["key"], len(s["title"]), len(s["meta"]), wc, h, errs)
    if errs: bad = True
    else:
        with open(OUT + s["key"] + ".json", "w", encoding="utf-8") as f:
            json.dump(s, f, ensure_ascii=False, indent=1)
print("BAD" if bad else "OK")
