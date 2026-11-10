"""Healthcare industry page, Draft 1. Proof from stories-data (CRL, PriceMDs; MSA Source removed per Brian, call 27). HIPAA facts measured on Microsoft Learn 9 Nov 2026
(learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech): Dynamics 365, Power Apps, Power Automate, Power BI in BAA scope; BAA in the DPA by default
for covered entities and business associates; a BAA does not on its own achieve compliance. PriceMDs portal and e-signatures confirmed by Brian, call 27 (added)."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import gen_ppprod as G
LEARN = 'https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech'
d = dict(url='https://www.encloud9.com/lp/healthcare-crm-software-dynamics-365/', name='Healthcare', h1=('Dynamics 365','for healthcare'),
  parent=('Dynamics 365','https://www.encloud9.com/power-platform-dynamics-365/','nine-dynamics-365.html'), seelink='See the client stories',
  title='Dynamics 365 for Healthcare Companies | enCloud9', kicker='Industries &middot; Healthcare and compliance',
  meta='We build and support Dynamics 365 for healthcare and health compliance companies. Client stories, what Microsoft covers under HIPAA, and how we work.',
  answer=('We build and support Dynamics 365 for healthcare and health compliance companies, including a lab testing provider and a healthcare company managing patient and prescription data.'
          ' Microsoft includes Dynamics 365 in its HIPAA Business Associate Agreement; compliance still depends on how you set it up and use it.'),
  caption='Healthcare and compliance clients we work with', cols=('Client','Starting point','What we built'),
  plans=[('Clinical Reference Lab (CRL), Lenexa, KS','A CRM designed for smaller businesses, at a newly bought subsidiary','Dynamics 365 Sales, several years of data moved, workflows rebuilt, live in three months'),
         ('PriceMDs, Clearwater, FL','Monday CRM, with patient and prescription data to manage','Dynamics 365 Sales and Customer Service with custom tables, workflows and integrations, plus a pharmacist portal and e-signatures')],
  note='From our client stories. <a class="lnk" href="nine-stories.html">See all 23 client stories</a>',
  plan_h='Which healthcare companies do we work with?', plan_lead='Labs, healthcare services and health compliance firms, each starting from a different place: a CRM they outgrew, a tool not built for patient data, or a system another partner left hard to report on.',
  cells=[('b1','nine-story-crl.html','Lab testing','CRL','Live in three months','&#8599;',''),('b2','nine-story-pricemds.html','Healthcare','PriceMDs','Patient and prescription data','&#8599;',''),
         ('b3','nine-power-bi.html','Reporting','Power BI','Dashboards your team trusts','&#8599;',''),('b4','#fit','HIPAA','Microsoft BAA','Covers Dynamics 365','&#8600;',''),
         ('b5','#plans','Healthcare','Dynamics 365','Sales and Customer Service','','core'),('b6','nine-full-implementation.html','Package','Full implementation','A new system','&#8599;','lt'),
         ('b7','nine-rescue-repair.html','Package','Rescue and Repair','Fix one that is not working','&#8599;','lt'),('b8','nine-power-platform.html','Extend','Power Platform','Apps, flows, reports','&#8599;','lt'),
         ('b9','nine-support.html','After go-live','Support','From $500 a month','&#8599;','lt')],
  fit_h='What does Microsoft cover for health data?', fit_lead='Microsoft offers a HIPAA Business Associate Agreement that covers Dynamics 365, Power Apps, Power Automate and Power BI. It does not make you compliant on its own: your setup, security roles and processes still have to meet HIPAA.',
  fit_title='From Microsoft', fit=['Dynamics 365, Power Apps, Power Automate and Power BI are in scope for Microsoft\'s HIPAA Business Associate Agreement.',
       'The agreement comes with Microsoft\'s Data Protection Addendum by default for customers who are covered entities or business associates.',
       'Microsoft says a BAA supports your HIPAA compliance but does not achieve it on its own.',
       f'Read it on <a class="lnk" href="{LEARN}">Microsoft Learn</a>.'],
  faq=[("Is Dynamics 365 HIPAA compliant?","Microsoft includes Dynamics 365 in its HIPAA Business Associate Agreement. Using it does not make you compliant on its own; your setup, access rules and processes have to meet HIPAA too."),
       ("Do we need to sign a BAA with Microsoft?","Microsoft makes its HIPAA Business Associate Agreement available by default through its Data Protection Addendum to customers who are covered entities or business associates."),
       ("Does enCloud9 sign a BAA with clients?","[Brian confirms.]"),
       ("Which Dynamics 365 apps do healthcare clients use?","Our healthcare and compliance clients run Dynamics 365 Sales, and some add Customer Service. Power Apps, Power Automate and Power BI extend them on the same data."),
       ("Can you fix a healthcare CRM another partner built?",'Yes. enCloud9 takes over systems other partners built, finds what is broken, and fixes it in priority order. See <a class="lnk" href="nine-rescue-repair.html">Rescue and Repair</a>.')],
  related=[('nine-story-crl.html','Client story','CRL'),('nine-story-pricemds.html','Client story','PriceMDs'),('nine-rescue-repair.html','Package','Rescue and Repair'),('nine-dynamics-365.html','Dynamics 365','All Dynamics 365 apps')])
G.render('nine-healthcare.html', d)
