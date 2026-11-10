"""Power Platform hub, Draft 1. Microsoft prices read from Microsoft's own pricing pages 9 Nov 2026 (Power Apps, Power Automate, Power BI).
Family chart with anchors per Brian, call 27 (one page for now; official Microsoft icons to add). Proof: Green Print Partners (Power App), PriceMDs (Power BI), CFC and PriceMDs (Power Pages portal), Compana (Copilot Studio), from stories-data."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from n9base import *
URL = 'https://www.encloud9.com/microsoft-power-platform/'
TITLE = 'Microsoft Power Platform Partner | enCloud9'
META = 'We build Power Apps, Power Automate flows, Power BI reports and Copilot Studio agents on the same Dataverse data as your Dynamics 365 system.'
ANSWER = ('Microsoft Power Platform is Microsoft\'s low-code family: Power Apps for business apps, Power Automate for workflows, Power BI for reports, '
          'Power Pages for portals and Copilot Studio for agents. It runs on Dataverse, the same data as Dynamics 365. We build on it for Dynamics 365 teams.')
ROWS = [
 ('Power Apps', 'Business apps on your Dynamics 365 data', '$20 per user per month (Premium)'),
 ('Power Automate', 'Workflows, approvals and alerts between systems', '$15 per user per month (Premium)'),
 ('Power BI', 'Reports and dashboards', '$14 per user per month (Pro); $24 (Premium Per User)'),
 ('Power Pages', 'Portals for clients, partners or the public', 'See Microsoft\'s price list'),
 ('Copilot Studio', 'Agents that answer questions and take actions', 'Prepaid Copilot Credits'),
]
FAQ = [
 ("What is Microsoft Power Platform?", "Microsoft's low-code family: Power Apps, Power Automate, Power BI, Power Pages and Copilot Studio. It runs on Dataverse, the same data platform as Dynamics 365."),
 ("Do we need Power Platform if we have Dynamics 365?", "Dynamics 365 already runs on Power Platform. You add Power Platform tools when you need an app, a workflow, a report or a portal that the Dynamics 365 app does not give you."),
 ("How much does Power Platform cost?", "Microsoft prices each tool separately. Power Apps Premium is $20 per user per month, Power Automate Premium is $15, and Power BI Pro is $14, all paid yearly. Our build work is quoted in writing after a short call."),
 ("Which tool should we start with?", "Start with the problem. A form or screen your team needs is Power Apps. A manual handoff is Power Automate. A report people build by hand in a spreadsheet is Power BI. A portal for people outside your company is Power Pages."),
 ("Can you build a portal for our clients?", 'Yes. Power Pages portals sit on the same data as Dynamics 365. See the <a class="lnk" href="nine-story-cfc.html">Collaborative for Children</a> story.'),
 ("What about Copilot and agents?", 'Copilot Studio builds agents on the same data. See <a class="lnk" href="nine-copilot.html">Copilot and AI</a>.'),
]

FAM = [
 ('power-apps','Apps','Power Apps','b1','Business apps your team uses on a phone or a desk, built on your Dynamics 365 data.','$20 per user per month (Premium)','enCloud9 built a Power App for Green Print Partners.','nine-power-apps.html'),
 ('power-automate','Automate','Power Automate','b2','Workflows, approvals and alerts that move work between people and systems without copying data by hand.','$15 per user per month (Premium)','',BOOK),
 ('power-bi','BI','Power BI','b3','Reports and dashboards that pull from Dynamics 365 and your other systems.','$14 per user per month (Pro); $24 (Premium Per User)','enCloud9 built Power BI reports for <a class="lnk" href="nine-story-pricemds.html">PriceMDs</a>.','nine-power-bi.html'),
 ('power-pages','Pages','Power Pages','b4','Portals for clients, partners or the public, on the same data as your CRM.','See Microsoft\'s price list','enCloud9 built a client portal for Collaborative for Children.','nine-story-cfc.html'),
 ('copilot-studio','Copilot','Copilot Studio','b5','Agents that answer questions from your data and take actions.','Prepaid Copilot Credits','enCloud9 built Copilot Studio chat agents for <a class="lnk" href="nine-story-compana.html">Compana Pet Brands</a>.','nine-copilot-studio.html'),
]
ICON = {'power-apps':'PowerApps','power-automate':'PowerAutomate','power-bi':'PowerBI','power-pages':'PowerPages','copilot-studio':'CopilotStudio'}
badge = lambda i,b,sz: (f'<img class="fm-i" src="../assets/icons/ms/{ICON[i]}_scalable.svg" width="{sz}" height="{sz}" alt="">' if i in ICON else f'<span class="fm-b" aria-hidden="true">{b}</span>')
famtiles = ''.join(f'        <li><a class="fm-t" href="#{i}" style="--c:var(--{c})">{badge(i,b,56)}<span class="fm-n">{n}</span></a></li>\n' for i,b,n,c,d,pr,pf,pg in FAM)
famblocks = ''.join(f'      <div class="fm-blk rev" id="{i}" style="--c:var(--{c})"><h3 class="h3">{badge(i,b,40)}{n}</h3><p>{e(d)}</p><p class="fine">Microsoft list price: {e(pr)}</p>'
                    + (f'<p>{pf}</p>' if pf else '') + ((f'<a class="lnk" href="{pg}">Talk through a flow <span>&rarr;</span></a>' if pg==BOOK else (f'<a class="lnk" href="{pg}">Read the portal story <span>&rarr;</span></a>' if pg.startswith('nine-story') else f'<a class="lnk" href="{pg}">More on {n} <span>&rarr;</span></a>')) if pg else '') + '</div>\n' for i,b,n,c,d,pr,pf,pg in FAM)
rows = ''.join(f'          <tr><th scope="row">{e(a)}</th><td data-l="What it does">{e(b)}</td><td data-l="Microsoft list price">{e(c)}</td></tr>\n' for a,b,c in ROWS)
css = ('.fm-row{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:12px}.fm-t{display:flex;flex-direction:column;align-items:center;gap:10px;padding:18px 8px;border:1px solid var(--line);border-radius:14px;text-decoration:none;color:inherit;transition:transform .2s,border-color .2s}.fm-t:hover,.fm-t:focus-visible{transform:translateY(-2px);border-color:var(--c)}.fm-b{display:inline-grid;place-items:center;min-width:56px;height:56px;padding:0 8px;border-radius:14px;background:var(--c);color:#fff;font-family:var(--mono);font-size:13px;font-weight:600}.fm-n{font-weight:600;text-align:center}.fm-i{display:block;flex:none}.fm-base{display:flex;align-items:center;justify-content:center;gap:10px}.fm-base{margin-top:12px;padding:12px;border-radius:12px;background:var(--b5);color:#fff;text-align:center;font-family:var(--mono);font-size:13px}.fm-grid{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:20px;margin-top:28px}.fm-blk{grid-column:span 2;display:flex;flex-direction:column;gap:2px;background:var(--white,#fff);border:1px solid var(--line);border-top:4px solid var(--c);padding:20px 22px 22px;scroll-margin-top:96px}.fm-blk:nth-child(n+4){grid-column:span 3}.fm-blk p{margin:6px 0 0}.fm-blk>a.lnk{margin-top:auto;padding-top:12px}.fm-blk h3{display:flex;align-items:center;gap:12px}.fm-blk .fm-b{min-width:40px;height:40px;font-size:11px;border-radius:10px}@media(max-width:1000px){.fm-grid{grid-template-columns:minmax(0,1fr)}.fm-blk,.fm-blk:nth-child(n+4){grid-column:auto}}@media(max-width:640px){.fm-row{grid-template-columns:repeat(2,1fr)}.fm-row li:last-child{grid-column:1/-1}}@media(prefers-reduced-motion:reduce){.fm-t{transition:none}.fm-t:hover{transform:none}}' + '@media(max-width:640px){#tools .tbl{min-width:0}#tools .tbl thead{position:absolute;left:-9999px}#tools .tbl tr{display:grid;grid-template-columns:1fr;padding:14px 0;border-bottom:1px solid var(--line)}'
       '#tools .tbl tbody th,#tools .tbl td{display:block;border:0;padding:2px 0}#tools .tbl td::before{content:attr(data-l) ": ";font-family:var(--mono);font-size:11px;color:var(--muted)}}')
hd = mkhead(TITLE, META, [('Home','https://www.encloud9.com/'),('Power Platform',URL)], faq=FAQ, css=css)
hd = hd.replace('</title>', '</title>', 1)
cells = [
 ('b1','#power-apps','Apps','Power Apps','Business apps on your data','&#8600;',''),
 ('b2','#power-automate','Workflows','Power Automate','Approvals, alerts, handoffs','&#8600;',''),
 ('b3','#power-bi','Reports','Power BI','Reports and dashboards','&#8600;',''),
 ('b4','#power-pages','Portals','Power Pages','Portals for people outside','&#8600;',''),
 ('b5','#family','Power Platform','One data','Dataverse, shared with Dynamics 365','','core'),
 ('b6','#copilot-studio','Agents','Copilot Studio','Agents that take actions','&#8600;','lt'),
 ('b7','nine-dynamics-365.html','Pairs with','Dynamics 365','Sales and Customer Service','&#8599;','lt'),
 ('b8','nine-copilot.html#genpages','New','Generative pages','Pages built from a prompt','&#8599;','lt'),
 ('b9','nine-stories.html','Proof','Client stories','What we built','&#8599;','lt'),
]
main = crumbnav([('Home','nine-home.html'),('Power Platform',None)]) + f'''  <section class="hero" aria-labelledby="h1">
    <div class="copy">
      <span class="mono rise" style="--d:0">Copilot and AI &middot; Power Platform</span>
      <h1 class="h1" id="h1" style="font-size:clamp(40px,5.4vw,72px)"><span class="ln"><span style="--d:1">Microsoft</span></span> <span class="ln"><span style="--d:2">Power Platform</span></span></h1>
      <p class="lead rise" style="--d:3">{e(ANSWER)}</p>
      <div class="acts rise" style="--d:4"><a class="btn btn-p" href="{BOOK}">Book a call</a><a class="lnk" href="#family">See the tools <span>&rarr;</span></a></div>
      <p class="phone-note rise" style="--d:5">Prefer the phone? Call <a href="tel:+18442640729">1-844-264-0729</a>.</p>
    </div>
    <div>
{grid('The Power Platform tools', cells)}    </div>
  </section>

  <section class="sec" id="family" aria-labelledby="fm-h">
    <div class="sec-head rev">
      <h2 class="h2" id="fm-h">Which tools make up the Power Platform family?</h2>
      <p class="lead">Five tools, one data platform. Pick a tool to jump to what it does and what enCloud9 has built with it.</p>
    </div>
    <nav aria-label="Power Platform tools" class="rev">
      <ul class="fm-row">
{famtiles}      </ul>
      <div class="fm-base"><img class="fm-i" src="../assets/icons/ms/Dataverse_scalable.svg" width="28" height="28" alt=""> Dataverse: all five run on the same data as Dynamics 365</div>
    </nav>
    <div class="fm-grid">
{famblocks}    </div>
  </section>

  <section class="sec" id="tools" aria-labelledby="tl-h">
    <div class="sec-head rev">
      <h2 class="h2" id="tl-h">What is in Power Platform, and what does it cost?</h2>
      <p class="lead">Five tools on one data platform. Microsoft licenses each one separately, and none of them includes our build work.</p>
    </div>
    <div class="tbl-wrap rev" tabindex="0" role="region" aria-label="Table, scrolls sideways on small screens">
      <table class="tbl">
        <caption class="mono" style="text-align:left;padding-bottom:10px">Power Platform tools and Microsoft list prices</caption>
        <thead><tr><th scope="col">Tool</th><th scope="col">What it does</th><th scope="col">Microsoft list price</th></tr></thead>
        <tbody>
{rows}        </tbody>
      </table>
      <p class="fine">Prices per user per month, paid yearly, from Microsoft's pricing pages, checked 9 Nov 2026. Microsoft licenses are a separate cost from our build work.</p>
    </div>
  </section>

  <section class="sec" id="fit" aria-labelledby="fit-h">
    <div class="fitsplit">
    <div class="side rev">
      <h2 class="h2" id="fit-h">When does a Dynamics 365 team need Power Platform?</h2>
      <p class="lead">When the Dynamics 365 app does most of the job and one piece is missing: a screen, a handoff, a report or a portal. We build that piece on the same data, so nothing is copied between systems.</p>
      <div class="acts" style="margin-top:0"><a class="btn btn-p" href="{BOOK}">Book a call</a></div>
    </div>
    <div class="fit rev">
      <div class="yes"><h3 class="h3">A good fit if</h3><ul>
        <li>Your team keeps a spreadsheet next to the CRM to track one thing.</li>
        <li>Someone emails or rekeys data between two systems every day.</li>
        <li>Clients or partners need to see or send information without a Dynamics 365 license. That is a <a class="lnk" href="nine-story-cfc.html">portal</a>.</li>
        <li>Leaders build the same report by hand every week.</li>
      </ul></div>
    </div>
    </div>
  </section>

''' + faqsec('Power Platform questions we get asked', FAQ) + '\n' + lnav('Related', [
  ('nine-copilot.html','Copilot and AI','Copilot and agents'),('nine-dynamics-365.html','Dynamics 365','All Dynamics 365 apps'),
  ('nine-story-cfc.html','Client story','Collaborative for Children'),('nine-document-core-pack.html','Add-on','Document Core Pack'),('nine-packages.html','Packages','All packages')])
write('nine-power-platform.html', hd, main)
print('ok', len(ANSWER.split()), len(TITLE), len(META))
