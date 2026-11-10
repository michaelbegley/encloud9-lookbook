"""Power Apps and Power BI (licensing FAQ and Feb 2027 enforcement from Learn: powerapps-licensing-faq, pricing-billing-skus, read 9 Nov 2026) product pages, Draft 1. Microsoft prices from Microsoft's pricing pages, checked 9 Nov 2026.
Live pages (read 9 Nov) have no prices, FAQ or client proof. No story names Power Apps or Power BI, so proof links are Dynamics 365 builds, labeled as such."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from n9base import *
TCSS = ('@media(max-width:640px){#plans .tbl{min-width:0}#plans .tbl thead{position:absolute;left:-9999px}#plans .tbl tr{display:grid;grid-template-columns:1fr;padding:14px 0;border-bottom:1px solid var(--line)}'
        '#plans .tbl tbody th,#plans .tbl td{display:block;border:0;padding:2px 0}#plans .tbl td::before{content:attr(data-l) ": ";font-family:var(--label);font-size:13px;color:var(--muted)}}')
PAGES = {
'nine-power-apps.html': dict(
  url='https://www.encloud9.com/dynamics-365-power-apps/', name='Power Apps', h1=('Power Apps','for Dynamics 365'),
  title='Power Apps for Dynamics 365 | enCloud9', kicker='Power Platform &middot; Power Apps',
  meta='We build Power Apps on your Dynamics 365 data: screens, forms and approvals your team needs. Power Apps Premium is $20 per user per month, paid yearly.',
  answer=('Power Apps is Microsoft\'s tool for building business apps without heavy code. Dynamics 365 Sales and Customer Service are themselves Power Apps, so we build the extra screens, forms and approvals your team needs on the same data. '
          'Power Apps Premium is $20 per user per month, paid yearly.'),
  plans=[('Developer Plan','Free','For building and testing, not for running apps for your team'),('Premium','$20 per user per month','Run any number of apps; paid yearly'),
         ('Premium, 2,000 seats or more','$12 per user per month','Same plan at volume; paid yearly'),('Dataverse capacity add-on','$40 per GB per month','More database storage; paid yearly')],
  plan_h='How much does Power Apps cost?', plan_lead='Microsoft licenses Power Apps per user. A Dynamics 365 license already covers apps that extend that Dynamics 365 app in the same environment, so check before you buy more. Our build work is quoted in writing after a short call.',
  cells=[('b1','#plans','Price','$20','Per user per month, Premium','&#8600;',''),('b2','#fit','Builds','Screens','Forms your team fills in','&#8600;',''),('b3','#fit','Builds','Approvals','With Power Automate','&#8600;',''),
         ('b4','#fit','Builds','Mobile','Apps on phones and tablets','&#8600;',''),('b5','#plans','Power Apps','One data','Same data as Dynamics 365','','core'),
         ('b6','nine-power-platform.html','Family','Power Platform','All five tools','&#8599;','lt'),('b7','nine-power-bi.html','Pairs with','Power BI','Reports on the same data','&#8599;','lt'),
         ('b8','nine-story-ppc.html','Client story','PPC','A job tracking system in Dynamics 365','&#8599;','lt'),('b9','nine-copilot.html#genpages','New','Generative pages','Pages from a prompt','&#8599;','lt')],
  fit_h='When does a Dynamics 365 team need Power Apps?', fit_lead='When your team works around the CRM instead of in it: a spreadsheet for one process, a paper form, or a screen built for a different job. We build that piece on your Dynamics 365 data.',
  fit=['People keep a spreadsheet next to Dynamics 365 for one process.','Field staff need a simple phone app that writes back to the CRM.','A request goes around by email for approval.',
       'You need a screen that pulls together records from several tables. See how we built a job tracking system for <a class="lnk" href="nine-story-ppc.html">PPC</a>.'],
  faq=[("Has enCloud9 built Power Apps for clients?","Yes. enCloud9 built a Power App for Green Print Partners. <a class=\"lnk\" href=\"nine-contact.html\">Book a call</a> to talk through yours."),("What is Power Apps?","Microsoft's tool for building business apps with little code. Apps run on Dataverse, the same data platform as Dynamics 365, in a browser or on a phone."),
       ("Is Dynamics 365 built on Power Apps?","Yes. Dynamics 365 Sales and Customer Service are model-driven Power Apps. That is why we can add your own screens and forms without moving data anywhere."),
       ("How much does Power Apps cost?","Power Apps Premium is $20 per user per month, paid yearly, or $12 at 2,000 seats or more. The Developer Plan is free for building and testing. Our build work is quoted in writing after a short call."),
       ("Do our Dynamics 365 users need a separate Power Apps license?","Not always. A Dynamics 365 license covers apps that extend that Dynamics 365 app, in the same environment. An app used outside that context needs Power Apps licensing. We check your licenses before you buy anything new."),
       ("What changes in February 2027?","Microsoft starts enforcing Power Apps licensing more strictly. Users of model-driven apps, apps in managed environments and apps used outside a Dynamics 365 environment need a qualifying license, or they cannot open the app. Check your license assignments before then."),
       ("Power Apps or a generative page?",'A generative page builds one focused page from a prompt. A Power App is a full app with forms, screens and logic. See <a class="lnk" href="nine-copilot.html#genpages">generative pages</a>.')],
  related=[('nine-power-platform.html','Power Platform','All the tools'),('nine-power-bi.html','Power Platform','Power BI'),('nine-dynamics-365.html','Dynamics 365','All Dynamics 365 apps'),('nine-copilot.html','Copilot and AI','Copilot and agents')]),
'nine-power-bi.html': dict(
  url='https://www.encloud9.com/microsoft-power-bi/', name='Power BI', h1=('Power BI','for Dynamics 365'),
  title='Power BI for Dynamics 365 Reporting | enCloud9', kicker='Power Platform &middot; Power BI',
  meta='Power BI reports on your Dynamics 365 data and the other systems your business runs on. Power BI Pro is $14 per user per month, paid yearly.',
  answer=('Power BI is Microsoft\'s reporting tool. It turns your Dynamics 365 data, and data from your other systems, into reports and dashboards your leaders can open in a browser or on a phone. '
          'Power BI Pro is $14 per user per month, paid yearly, and Premium Per User is $24.'),
  plans=[('Free account','Free','Build reports for yourself; sharing needs Pro'),('Pro','$14 per user per month','Share reports with your team; paid yearly'),
         ('Premium Per User','$24 per user per month','Bigger data and more frequent refresh; paid yearly'),('Embedded and Fabric capacity','Variable','Priced by capacity; for large or public reporting')],
  plan_h='How much does Power BI cost?', plan_lead='Microsoft licenses Power BI per user. Everyone who shares or views a shared report needs Pro or Premium Per User, unless you buy capacity. Our build work is quoted in writing after a short call.',
  cells=[('b1','#plans','Price','$14','Per user per month, Pro','&#8600;',''),('b2','#fit','Builds','Reports','Sales, service, finance','&#8600;',''),('b3','#fit','Connects','Many systems','Dynamics 365 and the rest','&#8600;',''),
         ('b4','#fit','Shows','Phone and web','Reports anywhere','&#8600;',''),('b5','#plans','Power BI','Reporting','On Dynamics 365 data','','core'),
         ('b6','nine-power-platform.html','Family','Power Platform','All five tools','&#8599;','lt'),('b7','nine-power-apps.html','Pairs with','Power Apps','Apps on the same data','&#8599;','lt'),
         ('b8','nine-story-rei.html','Client story','REI','Dashboards for five divisions','&#8599;','lt'),('b9','nine-copilot.html','Pairs with','Copilot','Questions about your data','&#8599;','lt')],
  fit_h='When does a Dynamics 365 team need Power BI?', fit_lead='Dynamics 365 has its own dashboards, and for many teams they are enough. Power BI earns its license when you report across several systems, need heavy analysis, or share reports beyond CRM users.',
  fit=['Your report pulls from Dynamics 365 and another system, such as accounting.','Someone rebuilds the same report in a spreadsheet every week.',
       'Leaders want trends over years, not just this quarter\'s pipeline.','People who do not use the CRM need to see the numbers.'],
  faq=[("Has enCloud9 built Power BI reports for clients?","Yes. enCloud9 built Power BI reports for <a class=\"lnk\" href=\"nine-story-pricemds.html\">PriceMDs</a>."),("What is Power BI?","Microsoft's reporting tool. It connects to Dynamics 365 and many other data sources and turns them into reports and dashboards in a browser or on a phone."),
       ("Do we need Power BI if Dynamics 365 has dashboards?",'Not always. Dynamics 365 dashboards cover day-to-day pipeline and service views; we built them for <a class="lnk" href="nine-story-bsi.html">BSI</a> and <a class="lnk" href="nine-story-rei.html">REI</a>. Power BI is for reporting across systems or heavier analysis.'),
       ("How much does Power BI cost?","Power BI Pro is $14 per user per month and Premium Per User is $24, both paid yearly. A free account works for your own reports. Our build work is quoted in writing after a short call."),
       ("Who needs a Power BI license?","Anyone who shares reports, and anyone who views a shared report, needs Pro or Premium Per User, unless your company buys capacity."),
       ("Does Copilot replace Power BI?",'No. Use Power BI for heavy analytics and Copilot for questions about your data. See <a class="lnk" href="nine-copilot.html">Copilot and AI</a>.')],
  related=[('nine-power-platform.html','Power Platform','All the tools'),('nine-power-apps.html','Power Platform','Power Apps'),('nine-dynamics-365-sales.html','Dynamics 365','Dynamics 365 Sales'),('nine-copilot.html','Copilot and AI','Copilot and agents')]),
'nine-copilot-studio.html': dict(
  url='https://www.encloud9.com/microsoft-copilot-studio/', name='Copilot Studio', h1=('Copilot Studio','agents'),
  parent=('Copilot and AI','https://www.encloud9.com/microsoft-copilot-for-business/','nine-copilot.html'),
  title='Microsoft Copilot Studio Agents | enCloud9', kicker='Copilot and AI &middot; Copilot Studio',
  meta='We build Copilot Studio agents on your Dynamics 365 data: agents that answer questions and take actions. Priced by Copilot Credits, from Microsoft.',
  answer=('Copilot Studio is Microsoft\'s tool for building your own AI agents: agents that answer questions from your data and take actions, such as creating a case or updating a record. '
          'It runs on the same data as Dynamics 365. Microsoft prices it by Copilot Credits, sold in packs or pay as you go.'),
  plans=[('Copilot Credit pack','$200 per pack per month','25,000 Copilot Credits for your whole company'),('Pre-purchase plan','Prepaid, you pick the amount','Up to 20% off with an up-front commitment; needs Azure'),
         ('Pay-as-you-go','Billed monthly for what you use','No commitment; needs an Azure subscription'),('Microsoft 365 Copilot users','Included','Agents published to Microsoft 365 Copilot, for users licensed for it')],
  plan_h='How much does Copilot Studio cost?', plan_lead='Microsoft charges by Copilot Credits: each answer or action an agent completes uses some. You buy credit packs, commit up front, or pay as you go. Our build work is quoted in writing after a short call.',
  cells=[('b1','#plans','Price','$200','25,000 credits a month','&#8600;',''),('b2','#fit','Answers','Questions','From your own data','&#8600;',''),('b3','#fit','Acts','Actions','Creates and updates records','&#8600;',''),
         ('b4','#fit','Runs in','Teams and web','Where people already work','&#8600;',''),('b5','#plans','Copilot Studio','Your agents','On your Dynamics 365 data','','core'),
         ('b6','nine-copilot.html','Family','Copilot and AI','Built-in agents too','&#8599;','lt'),('b7','nine-power-platform.html','Pairs with','Power Platform','Apps, flows, reports','&#8599;','lt'),
         ('b8','nine-story-compana.html','Client story','Compana','Copilot Studio and chatbots','&#8599;','lt'),('b9','nine-copilot.html#genpages','New','Generative pages','Pages from a prompt','&#8599;','lt')],
  fit_h='When does a business need its own Copilot Studio agent?', fit_lead='When the agents built into Dynamics 365 do not cover the job: questions only your own documents can answer, or a task that crosses your systems. Start with the built-in agents, then build your own for what is left.',
  fit=['Customers or staff ask the same questions every day, and the answers live in your own documents.','A task crosses systems, for example a store and the CRM. We explored a Copilot Studio integration with Shopify for <a class="lnk" href="nine-story-compana.html">Compana</a>.',
       'You want a chat on your website that can look things up in Dynamics 365.','Your team uses Microsoft 365 Copilot and needs it to reach business data.'],
  faq=[("Has enCloud9 built Copilot Studio agents for clients?","Yes. enCloud9 built Copilot Studio chat agents for <a class=\"lnk\" href=\"nine-story-compana.html\">Compana Pet Brands</a>."),("What is Copilot Studio?","Microsoft's tool for building your own AI agents. An agent answers questions from your data and can take actions, such as creating a case or updating a record."),
       ("How is Copilot Studio different from Copilot in Dynamics 365?",'Copilot in Dynamics 365 Sales and Customer Service comes built in. Copilot Studio is for agents you design for your own business. See <a class="lnk" href="nine-copilot.html">Copilot and AI</a>.'),
       ("How much does Copilot Studio cost?","Microsoft sells Copilot Credits: a pack of 25,000 credits is $200 a month for your whole company, or you can commit up front or pay as you go. Our build work is quoted in writing after a short call."),
       ("What uses Copilot Credits?","Each answer or action an agent completes uses a varying number of credits. Agents published to Microsoft 365 Copilot are included for users licensed for Microsoft 365 Copilot."),
       ("Can an agent work with our Dynamics 365 data?","Yes. Copilot Studio runs on the same platform as Dynamics 365, so an agent can read and update your records within the security roles you set.")],
  related=[('nine-copilot.html','Copilot and AI','Copilot and agents'),('nine-power-platform.html','Power Platform','All the tools'),('nine-story-compana.html','Client story','Compana'),('nine-dynamics-365.html','Dynamics 365','All Dynamics 365 apps')]),
'nine-d365-pricing.html': dict(
  url='https://www.encloud9.com/dynamics-365-pricing/', name='Dynamics 365 pricing', h1=('Dynamics 365','pricing'), parent=('Dynamics 365','https://www.encloud9.com/power-platform-dynamics-365/','nine-dynamics-365.html'),
  title='Dynamics 365 Pricing, Plans and Total Cost | enCloud9', kicker='Dynamics 365 &middot; Pricing',
  meta='Dynamics 365 list prices for Sales, Customer Service, Field Service and more, plus what else goes into the bill: storage, Copilot Credits, setup and support.',
  answer=('Dynamics 365 Sales costs $65 to $150 per user per month and Customer Service $50 to $195, at Microsoft list price paid yearly. Paying monthly on an annual plan costs 5% more. '
          'Setup and support are separate: our build work is quoted in writing, and support plans start at $500 a month.'),
  caption='Dynamics 365 plans and Microsoft list prices', cols=('Plan','Microsoft list price','Good for'),
  plans=[('Sales Professional','$65 per user per month','Small sales teams that need core pipeline tracking'),('Sales Enterprise','$105 per user per month','Most B2B sales teams; Copilot in Sales, Outlook and Teams'),
         ('Sales Premium','$150 per user per month','Agents at volume; 1,000 Copilot Credits per user per month'),('Customer Service Professional','$50 per user per month','Basic case management'),
         ('Customer Service Enterprise','$105 per user per month','Cases, queues, knowledge and service levels'),('Customer Service Premium','$195 per user per month','Case work and contact center in one plan'),
         ('Contact Center','$110 per user per month; Digital or Voice $95','Phone, chat and messaging with routing'),('Field Service','$105 per user per month; Contractor $50','Work orders, scheduling, technicians'),
         ('Project Operations','$135 per user per month','Project quotes, staffing, time and billing'),('Customer Insights','$1,700 per tenant per month; $1,000 attach','Customer data and marketing journeys'),
         ('Microsoft 365 Copilot','$30 per user per month','Copilot in Word, Excel, Outlook and Teams'),('Copilot Credit pack','$200 per pack per month','25,000 credits for agents, company-wide')],
  note='Microsoft US list prices, paid yearly, checked 4 Nov 2026. Prices are Microsoft\'s, can change, and do not include setup or support. <a class="lnk" href="https://www.encloud9.com/blog/dynamics-365-pricing-licensing-2025-guide/">See every plan and Copilot cost in our 2026 guide</a>',
  plan_h='How much does Dynamics 365 cost per user?', plan_lead='Each app is priced per user per month, paid yearly, except Customer Insights, which is priced per company. Most teams start with Sales Enterprise, Customer Service Enterprise, or both.',
  cells=[('b1','#plans','Sales','$65 to $150','Per user per month','&#8600;',''),('b2','#plans','Service','$50 to $195','Per user per month','&#8600;',''),('b3','#fit','Monthly billing','+5%','On an annual plan','&#8600;',''),
         ('b4','#fit','Storage','$40 a GB','Extra database storage','&#8600;',''),('b5','#plans','Dynamics 365','List prices','Checked 4 Nov 2026','','core'),
         ('b6','nine-d365-licensing.html','How it works','Licensing','Base, attach, Team Members','&#8599;','lt'),('b7','nine-support.html','After go-live','Support','From $500 a month','&#8599;','lt'),
         ('b8','nine-copilot.html','AI','Copilot','What is included','&#8599;','lt'),('b9','nine-packages.html','Setup','Packages','Fixed scope, quoted in writing','&#8599;','lt')],
  fit_h='What else goes into the total cost?', fit_lead='Licenses are only part of the bill. Budget for storage, Copilot Credits if you run agents, the build itself, and someone to keep the system healthy after go-live.',
  fit_title='Budget for', fit=['Storage: every company gets a default amount; extra database storage is $40 per GB per month.','Copilot Credits if you run agents, unless you are on a Premium plan with credits included.',
       'The build: our packages are fixed scope, <a class="lnk" href="nine-packages.html">quoted in writing</a> after a short call.','Support after go-live: <a class="lnk" href="nine-support.html">our plans</a> start at $500 a month.'],
  faq=[("Can we buy Microsoft licenses from enCloud9?","Yes. enCloud9 sells Microsoft licenses. Ask about them on your call."),("How much does Dynamics 365 cost per user?","At Microsoft list price, paid yearly, Dynamics 365 Sales runs $65 to $150 per user per month, Customer Service $50 to $195, Field Service $105 and Project Operations $135. Customer Insights is priced per company, from $1,000 a month with attach pricing."),
       ("What is the cheapest Dynamics 365 license?","For full users, Customer Service Professional and Field Service Contractor are the lowest listed prices at $50 per user per month. For light users, the Team Members license costs less; ask us for the current price."),
       ("Can I pay for Dynamics 365 monthly?","Yes. Microsoft's listed prices are for paying yearly. Paying monthly on an annual subscription costs 5% more, a rule Microsoft has applied since 1 April 2025."),
       ("Is there a minimum number of users?","Most apps have no minimum on Microsoft's pricing pages. Microsoft Relationship Sales needs 10 seats, and Customer Insights Attach needs 10 or more users of a qualifying Dynamics 365 app."),
       ("What does setup cost?","Accelerators are $7,500 fixed, a full implementation starts at $20,000, and Rescue and Repair runs $500 to $10,000, each quoted in writing. Microsoft licenses are a separate cost, and support plans start at $500 a month.")],
  related=[('nine-d365-licensing.html','Dynamics 365','Licensing'),('nine-dynamics-365.html','Dynamics 365','All Dynamics 365 apps'),('nine-support.html','After go-live','Support plans'),('nine-packages.html','Packages','All packages')]),
'nine-d365-licensing.html': dict(
  url='https://www.encloud9.com/dynamics-365-licensing/', name='Dynamics 365 licensing', h1=('Dynamics 365','licensing'), parent=('Dynamics 365','https://www.encloud9.com/power-platform-dynamics-365/','nine-dynamics-365.html'),
  title='Dynamics 365 Licensing Explained | enCloud9', kicker='Dynamics 365 &middot; Licensing', seelink='See the license types',
  meta='How Dynamics 365 licensing works: one base license per user, attach licenses for extra apps, Team Members for light users, and the 2027 Power Apps checks.',
  answer=('Each full Dynamics 365 user needs one base license for the highest-priced app they use, plus a lower-priced attach license for each extra app. People who only view records or enter time can use the lower-cost Team Members license. '
          'Getting this mix right is how you avoid paying twice.'),
  caption='Dynamics 365 license types', cols=('License','Who it is for','What to know'),
  plans=[('Base license','Every full user','One per user, for the highest-priced app that person needs'),('Attach license','A full user who needs a second app','Lower price than a second full license'),
         ('Team Members','People who view records, enter time or update their own items','Set apps only, and up to 15 tables in a custom app; price from your partner or the Microsoft 365 admin center'),
         ('Power Apps use rights','Full Dynamics 365 users','Covers apps that extend the licensed app, in the same environment; stricter checks from February 2027'),
         ('Copilot Credits','Companies that run agents','Sales Premium includes 1,000 per user per month; others buy packs or pay as they go'),
         ('Storage','Every company','Default storage grows with full licenses; extra database storage is $40 per GB per month')],
  note='From Microsoft Learn and Microsoft\'s pricing pages, checked 4 and 9 Nov 2026. <a class="lnk" href="https://www.encloud9.com/blog/dynamics-365-pricing-licensing-2025-guide/">Full 2026 price list and licensing guide</a>',
  plan_h='What kinds of Dynamics 365 licenses are there?', plan_lead='Three license types decide most of the bill: base, attach and Team Members. Power Apps use rights, Copilot Credits and storage come with them or on top.',
  cells=[('b1','#plans','One per user','Base','Highest-priced app','&#8600;',''),('b2','#plans','Extra apps','Attach','Lower price','&#8600;',''),('b3','#plans','Light users','Team Members','View, time, own items','&#8600;',''),
         ('b4','#fit','From Feb 2027','Stricter checks','Power Apps licensing','&#8600;',''),('b5','#plans','Licensing','Pay once','Not twice','','core'),
         ('b6','nine-d365-pricing.html','Prices','Pricing','Every plan and list price','&#8599;','lt'),('b7','nine-power-apps.html','Use rights','Power Apps','What Dynamics 365 covers','&#8599;','lt'),
         ('b8','nine-storage.html','Storage','Dataverse','When you run out','&#8599;','lt'),('b9','nine-copilot.html','AI','Copilot Credits','How agents are billed','&#8599;','lt')],
  fit_h='How do we know our licenses are right?', fit_lead='Most waste comes from two mistakes: full licenses for people who only need Team Members, and two full licenses where one base plus an attach would do. Book a call and we go through your users, apps and storage with you.',
  fit_title='Time for a check if', fit=['Some users only view records or enter time, but have full licenses.','One person holds two full licenses for two apps.',
       'Your storage is near 100%. Past that, Microsoft blocks new environments, and sandboxes lock after 30 and 90 days. See <a class="lnk" href="nine-storage.html">storage</a>.',
       'You run custom apps outside a Dynamics 365 environment. Microsoft enforces <a class="lnk" href="nine-power-apps.html">Power Apps licensing</a> more strictly from February 2027.'],
  faq=[("Can we buy Microsoft licenses from enCloud9?","Yes. enCloud9 sells Microsoft licenses. Ask about them on your call."),("What is a Dynamics 365 attach license?","An attach license adds a second app to a user who already has a base license, at a lower price than a full license. The base must be the highest-priced app that user needs."),
       ("What can a Team Members user do?","View records, enter time and expenses, and update their own items through set apps, with up to 15 tables in a custom app. If a Team Members user starts doing full work, Microsoft expects a full license."),
       ("Do Dynamics 365 users need Power Apps licenses?","Not for apps that extend their licensed Dynamics 365 app in the same environment. Apps used outside that context need Power Apps licensing, and Microsoft enforces this more strictly from February 2027."),
       ("What happens if we run out of storage?","Once a company passes 100% of its storage, Microsoft blocks creating, copying and restoring environments. After 30 days sandboxes go to admin-only mode, and after 90 days sign-in to them is blocked."),
       ("Can you check our licenses?","Yes. Book a call and we go through your users, apps and storage with you, and tell you where you can save or what you are missing. Free checkups, no obligation.")],
  related=[('nine-d365-pricing.html','Dynamics 365','Pricing'),('nine-power-apps.html','Power Platform','Power Apps'),('nine-storage.html','Storage','Dataverse storage'),('nine-dynamics-365.html','Dynamics 365','All Dynamics 365 apps')]),
}
def render(fn, d):
    par = d.get('parent', ('Power Platform','https://www.encloud9.com/microsoft-power-platform/','nine-power-platform.html'))
    hd = mkhead(d['title'], d['meta'], [('Home','https://www.encloud9.com/'),(par[0],par[1]),(d['name'],d['url'])], faq=d['faq'], css=TCSS)
    rows = ''.join(f'          <tr><th scope="row">{e(a)}</th><td data-l="{d.get('cols',('Plan','Price','What you get'))[1]}">{e(b)}</td><td data-l="{d.get('cols',('Plan','Price','What you get'))[2]}">{e(c)}</td></tr>\n' for a,b,c in d['plans'])
    fit = ''.join(f'        <li>{x}</li>\n' for x in d['fit'])
    main = crumbnav([('Home','nine-home.html'),(par[0],par[2]),(d['name'],None)]) + f'''  <section class="hero" aria-labelledby="h1">
    <div class="copy">
      <span class="mono rise" style="--d:0">{d['kicker']}</span>
      <h1 class="h1" id="h1" style="font-size:clamp(40px,5.4vw,72px)"><span class="ln"><span style="--d:1">{d['h1'][0]}</span></span> <span class="ln"><span style="--d:2">{d['h1'][1]}</span></span></h1>
      <p class="lead rise" style="--d:3">{e(d['answer'])}</p>
      <div class="acts rise" style="--d:4"><a class="btn btn-p" href="{BOOK}">Book a call</a><a class="lnk" href="#plans">{d.get('seelink','See the prices')} <span>&rarr;</span></a></div>
      <p class="phone-note rise" style="--d:5">Prefer the phone? Call <a href="tel:+18442640729">1-844-264-0729</a>.</p>
    </div>
    <div>
{grid('What '+d['name']+' does', d['cells'])}    </div>
  </section>

  <section class="sec" id="plans" aria-labelledby="pl-h">
    <div class="sec-head rev">
      <h2 class="h2" id="pl-h">{d['plan_h']}</h2>
      <p class="lead">{e(d['plan_lead'])}</p>
    </div>
    <div class="tbl-wrap rev" tabindex="0" role="region" aria-label="Table, scrolls sideways on small screens">
      <table class="tbl">
        <caption class="mono" style="text-align:left;padding-bottom:10px">{d.get('caption', d['name']+' plans and Microsoft list prices')}</caption>
        <thead><tr><th scope="col">{d.get('cols',('Plan','Price','What you get'))[0]}</th><th scope="col">{d.get('cols',('Plan','Price','What you get'))[1]}</th><th scope="col">{d.get('cols',('Plan','Price','What you get'))[2]}</th></tr></thead>
        <tbody>
{rows}        </tbody>
      </table>
      <p class="fine">{d.get('note', "Microsoft list prices from Microsoft's own pricing page, checked 9 Nov 2026. Microsoft licenses are a separate cost from our build work.")}</p>
    </div>
  </section>

  <section class="sec" id="fit" aria-labelledby="fit-h">
    <div class="fitsplit">
    <div class="side rev">
      <h2 class="h2" id="fit-h">{d['fit_h']}</h2>
      <p class="lead">{e(d['fit_lead'])}</p>
      <div class="acts" style="margin-top:0"><a class="btn btn-p" href="{BOOK}">Book a call</a></div>
    </div>
    <div class="fit rev">
      <div class="yes"><h3 class="h3">{d.get('fit_title','A good fit if')}</h3><ul>
{fit}      </ul></div>
    </div>
    </div>
  </section>

''' + faqsec(d['name'] + ' questions we get asked', d['faq']) + '\n' + lnav('Related', d['related'])
    write(fn, hd, main)
    print(fn, len(d['answer'].split()), len(d['title']), len(d['meta']))

if __name__ == '__main__':
    for fn, d in PAGES.items(): render(fn, d)
