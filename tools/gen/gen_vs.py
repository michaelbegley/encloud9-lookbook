"""Dynamics 365 vs Salesforce vs HubSpot, Draft 1. Prices read 9 Nov 2026 on each vendor's own page: salesforce.com/sales/pricing (page modified 6 Nov 2026),
hubspot.com/pricing/sales ("Starts at" figures; second figures shown beside them not used), Dynamics from the 2026 pricing guide (checked 4 Nov). Fair wording, no claims about competitors beyond their own pages."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from n9base import *
URL = 'https://www.encloud9.com/dynamics-365-vs-salesforce-vs-hubspot/'
TITLE = 'Dynamics 365 vs Salesforce vs HubSpot Compared | enCloud9'
META = 'Dynamics 365 Sales, Salesforce Sales Cloud and HubSpot Sales Hub compared: list prices from each vendor, AI, Microsoft 365 fit and who each one suits.'
ANSWER = ('At each vendor\'s list price, Dynamics 365 Sales costs $65 to $150 per user per month, Salesforce Sales Cloud $25 to $550, and HubSpot Sales Hub starts free, then from $7 to $150 per seat. '
          'Price is rarely the deciding factor. AI, fit with Microsoft 365, and setup decide which one your team will actually use.')
ROWS = [('Entry plan','Sales Professional, $65','Starter Suite, $25','Free for up to 2 users; Starter from $7'),
        ('Middle plan','Sales Enterprise, $105','Pro Suite, $100; Core, $195','Professional from $90, plus a $1,500 one-time onboarding fee'),
        ('Top plan','Sales Premium, $150','Advanced, $395; Max, $550','Enterprise from $150, plus a $3,500 one-time onboarding fee'),
        ('AI','Copilot included in Enterprise and Premium; agents run on Copilot Credits, 1,000 per user per month included in Premium','Built-in AI in Core and up; Agentforce for Sales from $125 per user per month, included in Max','AI agents run on HubSpot Credits; 500 to 5,000 credits included by plan'),
        ('Works inside','Outlook, Teams and Microsoft 365, on the same platform as Power Apps and Power BI','Its own platform','Its own platform, with marketing and service hubs from HubSpot'),
        ('Billing','Per user per month, paid yearly; monthly billing costs 5% more','Per user per month; most plans billed annually','Per seat per month; monthly or annual')]
FAQ = [("Is Dynamics 365 cheaper than Salesforce?","At list price, Dynamics 365 Sales runs $65 to $150 per user per month and Salesforce Sales Cloud $25 to $550. The plans differ in what they include, so compare the plan you would actually need, plus AI and setup."),
       ("Is HubSpot free?","HubSpot's Free plan is free for up to 2 users. Paid Sales Hub plans start from $7 per seat per month, and Professional and Enterprise add a one-time onboarding fee of $1,500 or $3,500."),
       ("Which CRM works best with Microsoft 365?","Dynamics 365 works inside Outlook and Teams and runs on the same platform as Power Apps and Power BI. Sales Enterprise and Premium include Copilot in Dynamics 365 Sales, Outlook and Teams."),
       ("When is Dynamics 365 the wrong choice?","When a very small team wants a free start with no Microsoft 365 in the business, or when a company is deeply invested in another platform and happy with it. We will tell you if that is you."),
       ("Can you move us from Salesforce or HubSpot?",'Yes. See <a class="lnk" href="nine-move-salesforce.html">Move from Salesforce</a> and <a class="lnk" href="nine-move-hubspot.html">Move from HubSpot</a>.')]
css = ('.vtbl th[scope=col]{white-space:nowrap}'
       '@media(max-width:760px){#compare .tbl{min-width:0}#compare .tbl thead{position:absolute;left:-9999px}#compare .tbl tr{display:grid;grid-template-columns:1fr;padding:14px 0;border-bottom:1px solid var(--line)}'
       '#compare .tbl tbody th,#compare .tbl td{display:block;border:0;padding:3px 0}#compare .tbl td::before{content:attr(data-l) ": ";font-family:var(--mono);font-size:11px;color:var(--muted)}}')
hd = mkhead(TITLE, META, [('Home','https://www.encloud9.com/'),('Dynamics 365','https://www.encloud9.com/power-platform-dynamics-365/'),('Dynamics 365 vs Salesforce vs HubSpot',URL)], faq=FAQ, css=css)
cols = ('Dynamics 365 Sales','Salesforce Sales Cloud','HubSpot Sales Hub')
rows = ''.join(f'          <tr><th scope="row">{e(a)}</th>' + ''.join(f'<td data-l="{cols[i]}">{e(v)}</td>' for i, v in enumerate((b, c, d))) + '</tr>\n' for a, b, c, d in ROWS)
cells = [('b1','#compare','Dynamics 365','$65 to $150','Per user per month','&#8600;',''),('b2','#compare','Salesforce','$25 to $550','Per user per month','&#8600;',''),
         ('b3','#compare','HubSpot','Free to $150','Per seat, plus onboarding','&#8600;',''),('b4','#fit','Decides it','Fit','Not the sticker price','&#8600;',''),
         ('b5','#compare','Compared','Three CRMs','Prices checked Nov 2026','','core'),('b6','nine-move-salesforce.html','Switching','From Salesforce','How the move works','&#8599;','lt'),
         ('b7','nine-move-hubspot.html','Switching','From HubSpot','How the move works','&#8599;','lt'),('b8','nine-d365-pricing.html','Prices','Dynamics 365','Every plan','&#8599;','lt'),
         ('b9','nine-copilot.html','AI','Copilot','What is included','&#8599;','lt')]
main = crumbnav([('Home','nine-home.html'),('Dynamics 365','nine-dynamics-365.html'),('Compared',None)]) + f'''  <section class="hero" aria-labelledby="h1">
    <div class="copy">
      <span class="mono rise" style="--d:0">Dynamics 365 &middot; Compared</span>
      <h1 class="h1" id="h1" style="font-size:clamp(36px,4.6vw,62px)"><span class="ln"><span style="--d:1">Dynamics 365 vs</span></span> <span class="ln"><span style="--d:2">Salesforce vs HubSpot</span></span></h1>
      <p class="lead rise" style="--d:3">{e(ANSWER)}</p>
      <div class="acts rise" style="--d:4"><a class="btn btn-p" href="{BOOK}">Book a call</a><a class="lnk" href="#compare">See the comparison <span>&rarr;</span></a></div>
    </div>
    <div>
{grid('Three CRMs compared', cells)}    </div>
  </section>

  <section class="sec" id="compare" aria-labelledby="cp-h">
    <div class="sec-head rev">
      <h2 class="h2" id="cp-h">How do the three compare on price and AI?</h2>
      <p class="lead">List prices per user per month, as each vendor publishes them. Your price can differ with your agreement, and none of them includes setup by a partner.</p>
    </div>
    <div class="tbl-wrap rev" tabindex="0" role="region" aria-label="Table, scrolls sideways on small screens">
      <table class="tbl vtbl">
        <caption class="mono" style="text-align:left;padding-bottom:10px">Dynamics 365 Sales, Salesforce Sales Cloud and HubSpot Sales Hub</caption>
        <thead><tr><th scope="col"></th>{''.join(f'<th scope="col">{c}</th>' for c in cols)}</tr></thead>
        <tbody>
{rows}        </tbody>
      </table>
      <p class="fine">Salesforce and HubSpot prices from their own pricing pages, read 9 Nov 2026; Dynamics 365 from Microsoft's pricing pages, checked 4 Nov 2026. US list prices; vendors change them. HubSpot shows "starts at" prices.</p>
    </div>
  </section>

  <section class="sec" id="fit" aria-labelledby="fit-h">
    <div class="fitsplit">
    <div class="side rev">
      <h2 class="h2" id="fit-h">Which one fits which team?</h2>
      <p class="lead">All three are serious CRMs. The right one is the one that fits how your business already works, and that your team will use every day.</p>
      <div class="acts" style="margin-top:0"><a class="btn btn-p" href="{BOOK}">Book a call</a></div>
    </div>
    <div class="fit rev">
      <div class="yes"><h3 class="h3">A good rule of thumb</h3><ul>
        <li><strong>Dynamics 365</strong> fits teams that live in Outlook and Teams and want the CRM, apps, reports and AI on one Microsoft platform.</li>
        <li><strong>Salesforce</strong> fits teams already invested in Salesforce and its ecosystem.</li>
        <li><strong>HubSpot</strong> fits small teams that want to start free with marketing and sales in one tool.</li>
        <li>Not sure? We will tell you which one fits, even when it is not Dynamics 365.</li>
      </ul></div>
    </div>
    </div>
  </section>

''' + faqsec('CRM comparison questions we get asked', FAQ) + '\n' + lnav('Related', [
  ('nine-move-salesforce.html','Switching','Move from Salesforce'),('nine-move-hubspot.html','Switching','Move from HubSpot'),('nine-d365-pricing.html','Dynamics 365','Pricing'),('nine-dynamics-365-sales.html','Dynamics 365','Dynamics 365 Sales')])
write('nine-vs-crm.html', hd, main)
print('ok', len(ANSWER.split()), len(TITLE), len(META))
