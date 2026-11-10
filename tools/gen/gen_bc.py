"""Business Central integration page, Draft 1. Brian, call 27 (48:05): keep that we work with partners, talk about integrating Dynamics 365 with
Business Central (credit limits, open invoices), dedicated partner network, do not name partners. Lifts the 4 Nov "no Business Central focus" rule
for this page only. Facts from Microsoft Learn, read 9 Nov 2026: business-central/integration-overview, marketing-integrate-dynamicscrm,
admin-prepare-dynamics-365-for-sales-for-integration (BC integrates only with Dynamics 365 Sales; via Dataverse; default jobs every 30 minutes;
posted invoices sync as Billed then Paid; Business Central Account Statistics on the account; item availability; quotes and orders).
No client proof: WID and BG Peterson stories wait on Brian question 5."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import gen_ppprod as G
L1='https://learn.microsoft.com/dynamics365/business-central/marketing-integrate-dynamicscrm'
d = dict(url='https://www.encloud9.com/dynamics-365-business-central/', name='Business Central integration', h1=('Dynamics 365 Sales','with Business Central'),
  parent=('Dynamics 365','https://www.encloud9.com/power-platform-dynamics-365/','nine-dynamics-365.html'), seelink='See what syncs',
  title='Dynamics 365 and Business Central Integration | enCloud9', kicker='Dynamics 365 &middot; Integration',
  meta='Connect Dynamics 365 Sales to Business Central so sellers see balances, credit limits, open invoices and stock. enCloud9 sets up the integration.',
  answer=('Connect Dynamics 365 Sales to Business Central and your sales team sees each customer\'s balance, credit limit and open invoices, plus item prices and stock, without leaving the CRM. '
          'Orders submitted in Sales flow to Business Central. enCloud9 sets up the connection and works with a network of Business Central partners for the accounting side.'),
  caption='What syncs between Dynamics 365 Sales and Business Central', cols=('Data','Direction','What your team gets'),
  plans=[('Customers and accounts','Both ways','One customer record, coupled in both systems'),
         ('Balances and statistics','Business Central to Sales','Balance and total sales on the account, in a Business Central statistics panel'),
         ('Posted invoices','Business Central to Sales','Invoices show as billed, then paid when the payment comes in'),
         ('Items, prices and stock','Business Central to Sales','Price lists and item availability while building a quote or order'),
         ('Quotes and orders','Sales to Business Central, or both ways','Orders submitted in Sales arrive in Business Central to ship and invoice')],
  note=f'From Microsoft\'s Business Central integration documentation, checked 9 Nov 2026. <a class="lnk" href="{L1}">Read Microsoft\'s guide</a>. Our setup work is quoted in writing; Business Central and Dynamics 365 are licensed separately.',
  plan_h='What syncs between Dynamics 365 Sales and Business Central?', plan_lead='Microsoft\'s built-in integration runs through Dataverse. These are the pieces sales and finance teams use most.',
  fit_h='When is the integration worth it?', fit_lead='When sellers have to ask finance before they can answer a customer.',
  fit=['Sellers ask accounting whether a customer is over their credit limit or has unpaid invoices.','Someone retypes orders from the CRM into Business Central.',
       'Quotes go out with prices or stock that changed in Business Central.','Finance and sales keep two customer lists that never quite match.'],
  cells=[('b1','#plans','Credit','Credit limits','Seen before the deal','&#8600;',''),('b2','#plans','Invoices','Open invoices','Billed and paid status','&#8600;',''),
         ('b3','#plans','Orders','Sales to Business Central','No retyping','&#8600;',''),('b4','#plans','Stock','Item availability','While quoting','&#8600;',''),
         ('b5','#plans','Integration','Sales and Business Central','One customer, two systems','','core'),('b6','nine-dynamics-365-sales.html','Pairs with','Dynamics 365 Sales','Where sellers work','&#8599;','lt'),
         ('b7','nine-full-implementation.html','Package','Full implementation','Integrations included','&#8599;','lt'),('b8','nine-power-platform.html','Extend','Power Platform','Flows and reports','&#8599;','lt'),
         ('b9','nine-contact.html','Next step','Book a call','Talk through your setup','&#8599;','lt')],
  faq=[("Can Dynamics 365 Sales show Business Central data?","Yes. With Microsoft's integration, sellers see a customer's balance, open invoices and item availability from Business Central while they work in Dynamics 365 Sales."),
       ("Do you implement Business Central?","enCloud9 focuses on Dynamics 365 and works with a network of Business Central partners for the accounting setup. enCloud9 connects the two systems so they work as one."),
       ("Does Business Central integrate with Customer Service?","Microsoft's built-in integration is with Dynamics 365 Sales only. Other connections can be built with Power Automate or custom work, quoted in writing."),
       ("How often does data sync?","Microsoft's default sync jobs run every 30 minutes, and the schedule can be changed. Some updates, like account statistics, can also be run by hand."),
       ("What does the integration cost?","Our setup work is quoted in writing after a short call. Business Central and Dynamics 365 are licensed separately, and enCloud9 sells Microsoft licenses.")],
  related=[('nine-dynamics-365-sales.html','Dynamics 365','Dynamics 365 Sales'),('nine-full-implementation.html','Package','Full implementation'),('nine-power-platform.html','Power Platform','All the tools'),('nine-contact.html','Company','Contact us')])
G.render('nine-business-central.html', d)
