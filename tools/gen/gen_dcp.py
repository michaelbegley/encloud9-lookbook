"""Document Core Pack page, Draft 1 (Brian, call 27: own page; e-signatures via Adobe or DocuSign).
Product facts read 9 Nov 2026 on mscrm-addons.com/Products/DocumentsCorePack and support.mscrm-addons.com e-signing doc:
maker mscrm-addons (PTM EDV-Systeme GmbH); Word templates; PDF, DOCX and other formats; email, SharePoint, batch; Power Automate connector
with 25+ actions; e-signature with DocuSign, Adobe Sign, DeepSign, AssureSign; signed copy stored back in Dynamics 365; price by team size, not published.
Proof: Milestone Leasing (quotes from the CRM), PriceMDs (pharmacist portal and e-signatures with Adobe Sign). MSA Source left out (leaving).
Open: whether enCloud9 resells the license (Brian question 9)."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import gen_ppprod as G
d = dict(url='https://www.encloud9.com/add-on-products/document-core-pack/', name='Document Core Pack', h1=('Document Core Pack','for Dynamics 365'),
  parent=('Dynamics 365','https://www.encloud9.com/power-platform-dynamics-365/','nine-dynamics-365.html'), seelink='See what it does',
  title='Document Core Pack for Dynamics 365 | enCloud9', kicker='Add-ons &middot; Documents and e-signatures',
  meta='Quotes, contracts and reports from your Dynamics 365 data, sent for e-signature with DocuSign or Adobe Sign. enCloud9 sets up Document Core Pack.',
  answer=('Document Core Pack, made by mscrm-addons, creates quotes, contracts, reports and emails from your Dynamics 365 data using Word templates. '
          'It can send a document for e-signature through DocuSign or Adobe Sign and saves the signed copy back on the record. enCloud9 sets it up and builds your templates.'),
  caption='What Document Core Pack does, and where enCloud9 has built it', cols=('Job','How it works','Where enCloud9 built it'),
  plans=[('Quotes from the CRM','A Word template fills in from the quote, account and product records, then saves as a PDF','Milestone Leasing: reps create standard quotes directly from Dynamics 365'),
         ('Documents signed online','Send a document to one or more signers through DocuSign or Adobe Sign; the signed copy comes back to the record','PriceMDs: a pharmacist portal and e-signatures with Adobe Sign'),
         ('Reports and letters','Word templates with tables, charts and conditions, filled from related records','Built to your templates'),
         ('Many documents at once','Create and send documents in batches or on a schedule, or from a Power Automate flow','Built to your process')],
  note='Product details from mscrm-addons.com, checked 9 Nov 2026. Document Core Pack is licensed from mscrm-addons, priced by team size; our setup work is quoted in writing.',
  plan_h='What does Document Core Pack do in Dynamics 365?', plan_lead='It turns records into finished documents without copying data into Word by hand. These are the jobs clients bring to us most.',
  fit_h='When is Document Core Pack worth it?', fit_lead='When people copy CRM data into Word or Excel by hand, or chase signatures by email.',
  fit=['Reps build quotes or proposals by copying CRM data into a Word file.','Contracts go out by email and come back signed in different places.',
       'Reports are rebuilt by hand every month from the same records.','You send the same letter or document to many records at once.'],
  cells=[('b1','#plans','Quotes','From the CRM','Filled from your records','&#8600;',''),('b2','#plans','Sign','DocuSign or Adobe Sign','Signed copy saved back','&#8600;',''),
         ('b3','nine-story-pricemds.html','Client story','PriceMDs','Portal and e-signatures','&#8599;',''),('b4','nine-story-milestone.html','Client story','Milestone Leasing','Quotes in one click','&#8599;',''),
         ('b5','#plans','Add-on','Document Core Pack','Documents from Dynamics 365','','core'),('b6','nine-power-platform.html','Automate','Power Automate','Documents from a flow','&#8599;','lt'),
         ('b7','nine-dynamics-365-sales.html','Pairs with','Dynamics 365 Sales','Quotes and proposals','&#8599;','lt'),('b8','nine-customer-service.html','Pairs with','Customer Service','Letters and case documents','&#8599;','lt'),
         ('b9','nine-contact.html','Next step','Book a call','Talk through your documents','&#8599;','lt')],
  faq=[("What is Document Core Pack?","An add-on for Dynamics 365, made by mscrm-addons, that creates documents such as quotes, contracts and reports from your CRM data using Word templates."),
       ("Can Document Core Pack send documents for e-signature?","Yes. It works with DocuSign and Adobe Sign, among others. You can set one or more signers and the signing order, and the signed copy is saved back in Dynamics 365."),
       ("Which file types can it create?","PDF and Word documents, among other formats. Templates are built in Microsoft Word."),
       ("Can it run automatically?","Yes. It can create and send documents in batches, on a schedule, or from a Power Automate flow."),
       ("How much does Document Core Pack cost?","mscrm-addons licenses it based on team size and does not publish a single price. Our setup and template work is quoted in writing."),
       ("Have you set it up for clients?",'Yes. <a class="lnk" href="nine-story-milestone.html">Milestone Leasing</a> creates quotes with it, and <a class="lnk" href="nine-story-pricemds.html">PriceMDs</a> uses it with Adobe Sign for e-signatures.')],
  related=[('nine-story-pricemds.html','Client story','PriceMDs'),('nine-story-milestone.html','Client story','Milestone Leasing'),('nine-power-platform.html','Power Platform','All the tools'),('nine-dynamics-365.html','Dynamics 365','All Dynamics 365 apps')])
G.render('nine-document-core-pack.html', d)
