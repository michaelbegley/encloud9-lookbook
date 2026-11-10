"""Draft 1 of the two move pages (Move from Salesforce, Move from HubSpot), built on the Sales Accelerator
Draft 2 shell. Copy from PAGE-SALESFORCE-MOVE.md and PAGE-HUBSPOT-MOVE.md (4 Nov 2026), with kit rules applied."""
import re, json, html as H
P = '/home/claude/lb/pages/'
base = open(P + 'nine-sales-accelerator.html', encoding='utf-8').read()

head_end = base.index('<header class="top">')
head = base[:head_end]
hdr = base[head_end:base.index('</header>') + len('</header>')]
final_start = base.index('<section class="final"')
tail = base[final_start:]

BOOK = 'nine-book.html'
SUP = 'nine-support.html#plans'

V = {
 'sf': dict(
   file='nine-move-salesforce.html', url='https://www.encloud9.com/microsoft-dynamics-365-salesforce-crm-migration/',
   name='Salesforce', crumb='Move from Salesforce', unit='org',
   title='Move from Salesforce to Dynamics 365 Sales | enCloud9',
   meta='We move growing US businesses from Salesforce to Dynamics 365 Sales, with records mapped and checked before go-live, and support from $500 a month.',
   answer="We move growing US businesses from Salesforce to Dynamics 365 Sales: your accounts, contacts, leads, opportunities and history, with record counts checked against Salesforce before go-live. Moving data from your old CRM or spreadsheets is part of a full implementation. Microsoft licenses are a separate cost, and support plans start at $500 a month.",
   inc_lead="Your Salesforce records, users and sales process move to Dynamics 365 Sales, mapped field by field and tested in a trial run before the full move. Salesforce flows, Apex code and add-on apps do not move on their own; we review them first and quote any rebuild separately.",
   inc=["A written review of your Salesforce org: objects, fields, automation, integrations and add-on apps",
        "Your Salesforce objects and fields mapped to Dynamics 365 Sales",
        "Your Salesforce users mapped to Dynamics 365 users and security roles",
        "Your Microsoft licenses assigned to each user",
        "A trial run first, then the full move, with record counts checked against Salesforce",
        "Up to [Brian sets] records moved", "[Brian sets] training sessions", "[Brian sets] days of help after go-live"],
   noinc=["Rebuilding Salesforce flows, Apex code and add-on apps, quoted separately",
          "Other Salesforce products, such as Marketing Cloud",
          "Integrations with other systems, quoted separately",
          "Microsoft licenses and Copilot Credits",
          "Ending your Salesforce contract, which stays between you and Salesforce"],
   grid=[('Reviewed','Your org','A written review of your Salesforce org'),('Mapped','Objects and fields','Salesforce objects and fields mapped to Dynamics 365 Sales'),
         ('Mapped','Users and roles','Salesforce users mapped to Dynamics 365 users and security roles'),('Assigned','Licenses','Your Microsoft licenses assigned to each user')],
   price_h='What do Dynamics 365 Sales and Salesforce Sales Cloud cost per user?',
   price_lead="Microsoft lists Dynamics 365 Sales at $65, $105 or $150 per user per month, paid yearly. Salesforce lists Sales Cloud at $25 for Starter Suite, $100 for Pro Suite, $195 for Core, $395 for Advanced and $550 for Max per user per month, billed annually except Starter Suite, which can be billed monthly.",
   col5='AI on the vendor\'s page',
   rows=[('Microsoft','Dynamics 365 Sales Professional','$65','Paid yearly','No Copilot; Sales agents need Copilot Credits'),
         ('Microsoft','Dynamics 365 Sales Enterprise','$105','Paid yearly','Copilot included; agents need Copilot Credits'),
         ('Microsoft','Dynamics 365 Sales Premium','$150','Paid yearly','Copilot included; 1,000 Copilot Credits per user per month'),
         ('Salesforce','Sales Cloud Starter Suite','$25','Billed monthly or annually','AI that syncs emails, events and contacts'),
         ('Salesforce','Sales Cloud Pro Suite','$100','Billed annually','None listed'),
         ('Salesforce','Sales Cloud Core','$195','Billed annually','Built-in AI and Agentforce skills'),
         ('Salesforce','Sales Cloud Advanced','$395','Billed annually','More AI; Agentforce for Sales sold separately'),
         ('Salesforce','Sales Cloud Max','$550','Billed annually','Agentforce for Sales included')],
   price_note2="Salesforce sells Agentforce for Sales as an add-on from $125 per user per month.",
   fit_lead="A move fits a sales team on Salesforce whose setup is mostly standard records, such as accounts, contacts, leads and opportunities, and who already work in Outlook and Teams. It is a weaker fit if your Salesforce org runs on heavy custom code, or if you need other systems connected on day one.",
   fit_yes=["Most of your Salesforce setup is standard records: accounts, contacts, leads and opportunities.",
            "Your Salesforce renewal date is coming and you want a plan before it arrives."],
   fit_no="Your Salesforce org runs on heavy custom code. We review it first and scope that rebuild separately.",
   q4=("Do our Salesforce flows and Apex code move across?","Not on their own. Microsoft's migration tooling reviews flows, Process Builder, workflow rules and Apex code but does not convert them, so they are rebuilt in Dynamics 365. We review them first and quote any rebuild separately."),
   q5=("Does Microsoft have a tool for moving from Salesforce?","Yes. Microsoft's Dynamics 365 Activate scans a Salesforce org, maps objects and fields to Dynamics 365 Sales and Customer Service, moves the records and checks record counts afterward. It is in preview, and Microsoft says preview features are not meant for production use."),
   checklist='Salesforce to Dynamics 365 Migration Readiness Checklist',
   other=('nine-move-hubspot.html','Move from HubSpot'),
 ),
 'hs': dict(
   file='nine-move-hubspot.html', url='https://www.encloud9.com/lp/microsoft-dynamics-365-hubspot-crm-migration/',
   name='HubSpot', crumb='Move from HubSpot', unit='portal',
   title='Move from HubSpot to Dynamics 365 Sales | enCloud9',
   meta='We move growing US businesses from HubSpot to Dynamics 365 Sales, with records mapped and checked before go-live, and support from $500 a month.',
   answer="We move growing US businesses from HubSpot to Dynamics 365 Sales: your contacts, companies, deals, pipelines and history, with record counts checked against HubSpot before go-live. Moving data from your old CRM or spreadsheets is part of a full implementation. Microsoft licenses are a separate cost, and support plans start at $500 a month.",
   inc_lead="Your HubSpot contacts, companies, deals, pipelines and activity history move to Dynamics 365 Sales, mapped field by field and tested in a trial run before the full move. HubSpot workflows, sequences and connected apps do not move on their own; we review them first and quote any rebuild separately.",
   inc=["A written review of your HubSpot portal: objects, properties, pipelines, workflows and connected apps",
        "Your HubSpot objects and properties mapped to Dynamics 365 Sales",
        "Your HubSpot users mapped to Dynamics 365 users and security roles",
        "Your Microsoft licenses assigned to each user",
        "A trial run first, then the full move, with record counts checked against HubSpot",
        "Up to [Brian sets] records moved", "[Brian sets] training sessions", "[Brian sets] days of help after go-live"],
   noinc=["Rebuilding HubSpot workflows, sequences and connected apps, quoted separately",
          "Marketing Hub emails, forms and landing pages, quoted separately",
          "Integrations with other systems, quoted separately",
          "Microsoft licenses and Copilot Credits",
          "Ending your HubSpot contract, which stays between you and HubSpot"],
   grid=[('Reviewed','Your portal','A written review of your HubSpot portal'),('Mapped','Objects and properties','HubSpot objects and properties mapped to Dynamics 365 Sales'),
         ('Mapped','Users and roles','HubSpot users mapped to Dynamics 365 users and security roles'),('Assigned','Licenses','Your Microsoft licenses assigned to each user')],
   price_h='What do Dynamics 365 Sales and HubSpot Sales Hub cost per user?',
   price_lead="Microsoft lists Dynamics 365 Sales at $65, $105 or $150 per user per month, paid yearly. HubSpot lists Sales Hub Starter from $7, Professional from $90 and Enterprise from $150 per seat per month, plus a one-time onboarding fee of $1,500 for Professional and $3,500 for Enterprise.",
   col5='One-time onboarding fee',
   rows=[('Microsoft','Dynamics 365 Sales Professional','$65','Paid yearly','None listed'),
         ('Microsoft','Dynamics 365 Sales Enterprise','$105','Paid yearly','None listed'),
         ('Microsoft','Dynamics 365 Sales Premium','$150','Paid yearly','None listed'),
         ('HubSpot','Sales Hub Starter','From $7 per seat','Monthly or annual','None listed'),
         ('HubSpot','Sales Hub Professional','From $90 per seat','Monthly or annual','$1,500'),
         ('HubSpot','Sales Hub Enterprise','From $150 per seat','Not shown','$3,500')],
   price_note2="HubSpot's starting prices are the lowest it shows; its page also shows higher prices for Starter and Professional, and some discounts are for new customers only.",
   fit_lead="A move fits a sales team on HubSpot whose setup is mostly standard records, such as contacts, companies and deals, and who already work in Outlook and Teams. It is a weaker fit if your HubSpot portal runs many workflows and connected apps, or if you need other systems connected on day one.",
   fit_yes=["Most of your HubSpot setup is standard records: contacts, companies and deals.",
            "Your HubSpot renewal date is coming and you want a plan before it arrives."],
   fit_no="Your HubSpot portal runs many workflows and connected apps. We review them first and scope that rebuild separately.",
   q4=("Do our HubSpot workflows and sequences move across?","Not on their own. Workflows, sequences and connected apps are rebuilt in Dynamics 365 rather than copied. We review them first and quote any rebuild separately."),
   q5=("Does Microsoft have a tool for moving from HubSpot?","Not a dedicated one. Microsoft's own migration tool, Dynamics 365 Activate, covers moves from Salesforce. For other systems, Microsoft's guidance points to data import, dataflows and data migration tools such as Azure Data Factory."),
   checklist='HubSpot CRM to Dynamics 365 Migration Readiness Checklist',
   other=('nine-move-salesforce.html','Move from Salesforce'),
 ),
}

def faqs(v):
    n = v['name']
    return [
     (f"How much does a move from {n} cost?", f"A move from {n} is a fixed price for our work, quoted in writing after a short call. Microsoft licenses are a separate cost: Microsoft's list price is $65, $105 or $150 per user per month, paid yearly, for Sales Professional, Enterprise or Premium. Support plans start at $500 a month."),
     (f"How long does a move from {n} take?", "A move takes [Brian sets] weeks. You get the plan, with dates, before we build."),
     v['q4'], v['q5'],
     ("Are Microsoft licenses included?", "No. Microsoft licenses and Copilot Credits are not part of the package price, and you pay for them separately. As part of the move we assign your licenses to each user and set their security roles, because Microsoft does not let a user open the app until both are done."),
     ("Is Copilot included in Dynamics 365 Sales?", "Copilot in Dynamics 365 Sales, Outlook and Teams is included in Sales Enterprise and Sales Premium, not in Sales Professional. The Sales agents are available on all three plans but run on Copilot Credits. Only Sales Premium includes credits; on other plans you buy them separately."),
     ("Can you move our data from Salesforce, HubSpot or spreadsheets?", "Yes. Moving data from your old CRM or spreadsheets is part of a full implementation, and the Sales Accelerator includes an import of up to [Brian sets] records. Integrations with other systems are quoted separately."),
     ("What if we need more than the package covers?", "Anything outside the package is a written change order you approve before work starts. If you need integrations or data from several systems at go-live, a full implementation fits better."),
     ("Do we need a support plan after go-live?", "Yes. New clients start on at least the Stability plan, $500 a month for 4 hours, on a 12-month agreement. Monthly plans include a 1-hour response during business hours, 7:00am to 5:00pm Central, Monday to Friday."),
    ]

def e(s): return H.escape(s, quote=False)

def build(k):
    v = V[k]; n = v['name']
    fq = faqs(v)
    # head
    hd = head
    hd = re.sub(r'<title>.*?</title>', f'<title>{e(v["title"])}</title>', hd)
    hd = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{H.escape(v["meta"])}">', hd)
    hd = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', hd, flags=re.S)
    ld = [
     {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
       {"@type":"ListItem","position":1,"name":"Home","item":"https://www.encloud9.com/"},
       {"@type":"ListItem","position":2,"name":"Packages and support","item":"https://www.encloud9.com/crm-cloud-automation-solutions/"},
       {"@type":"ListItem","position":3,"name":v['crumb'],"item":v['url']}]},
     {"@context":"https://schema.org","@type":"Service","name":f"Move from {n} to Dynamics 365 Sales","serviceType":"CRM migration","url":v['url'],
      "description":v['answer'],"provider":{"@type":"Organization","name":"enCloud9","url":"https://www.encloud9.com/"},
      "brand":{"@type":"Organization","name":"Microsoft"},"areaServed":{"@type":"Country","name":"United States"}},
     {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in fq if '[' not in a]},
    ]
    lds = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld)
    hd = hd.replace('<style>', lds + '<style>', 1)
    extra_css = ("body.p-pkg #prices .tbl tbody th{font-size:18px}\n"
                 "body.p-pkg #prices .tbl .vd{display:block;font-family:var(--label);font-size:13px;font-weight:400;color:var(--muted);letter-spacing:0;margin-bottom:4px}\n"
                 "body.p-pkg #prices .tbl tr.ms th,body.p-pkg #prices .tbl tr.ms td{background:var(--tint)}\n"
                 "body.p-pkg #prices .tbl tr.ms th{padding-left:12px}\n"
                 "body.p-pkg .ckl{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,4vw,56px);align-items:center;padding:clamp(24px,3vw,40px);border:2px solid var(--ink)}\n"
                 "body.p-pkg .ckl .ph{padding:20px;border:1px dashed var(--line);font-family:var(--label);font-size:14px;color:var(--muted)}\n"
                 "@media (max-width:860px){body.p-pkg .ckl{grid-template-columns:1fr}}\n"
                 "body.p-pkg .ckl .lead{margin-top:14px}\n"
                 "@media (max-width:640px){body.p-pkg #prices .tbl{min-width:0}body.p-pkg #prices .tbl thead{position:absolute;left:-9999px}body.p-pkg #prices .tbl tr{display:grid;grid-template-columns:1fr;padding:14px 12px;border-bottom:1px solid var(--line)}body.p-pkg #prices .tbl tbody th,body.p-pkg #prices .tbl td{display:block;border:0;padding:2px 0}body.p-pkg #prices .tbl tr.ms{background:var(--tint)}body.p-pkg #prices .tbl tr.ms th,body.p-pkg #prices .tbl tr.ms td{background:none;padding-left:0}body.p-pkg #prices .tbl td::before{content:attr(data-l) \": \";font-family:var(--label);font-size:13px;color:var(--muted)}}\n")
    hd = hd.replace('</style>', extra_css + '</style>', 1)
    hd = hd.replace('nine-sales-accelerator.html" class="on" aria-current="page">Sales Accelerator', f'{v["file"]}" class="on" aria-current="page">{v["crumb"]}')

    cells = ''
    bgs = ['b1','b2','b3','b4']
    for i,(lab,nm,ds) in enumerate(v['grid']):
        cells += f'        <a class="cell" style="background:var(--{bgs[i]});--d:{i}" href="#included"><span class="lab">{lab}</span><span class="nm">{nm}</span><span class="ds">{ds}</span><span class="ar" aria-hidden="true">&#8600;</span></a>\n'
    cells += f'        <a class="cell core" style="background:var(--b5);--d:4" href="#included"><span class="lab">Move</span><span class="nm">From {n}</span><span class="ds">Your {n} data moved to Dynamics 365 Sales</span></a>\n'
    more = [('Tested','Trial run','A trial run first, then the full move','#included'),
            ('Checked','Record counts',f'Up to [Brian sets] records moved, counts checked against {n}','#included'),
            ('Stage C','Training','[Brian sets] training sessions','#process'),
            ('After go-live','Help','[Brian sets] days of help after go-live','#included')]
    for j,(lab,nm,ds,h) in enumerate(more):
        cells += f'        <a class="cell lt" style="background:var(--b{6+j});--d:{5+j}" href="{h}"><span class="lab">{lab}</span><span class="nm">{nm}</span><span class="ds">{ds}</span><span class="ar" aria-hidden="true">&#8600;</span></a>\n'

    def li(items): return ''.join(f'        <li>{e(x)}</li>\n' for x in items)
    inc = li(v['inc']).replace('mapped to Dynamics 365 Sales</li>', 'mapped to <a class="lnk" href="nine-dynamics-365-sales.html">Dynamics 365 Sales</a></li>', 1)

    rows = ''
    for vd,ed,pr,bill,c5 in v['rows']:
        cls = ' class="ms"' if vd == 'Microsoft' else ''
        rows += f'          <tr{cls}><th scope="row"><span class="vd">{vd}</span>{ed}</th><td class="pr" data-l="List price">{pr}</td><td data-l="Billing">{bill}</td><td data-l="{e(v['col5'])}">{e(c5)}</td></tr>\n'

    fq_html = ''.join(f'      <details><summary>{e(q)}</summary><p>{e(a)}</p></details>\n' for q,a in fq)
    fq_html = fq_html.replace('<p>Copilot in Dynamics 365 Sales,', '<p>Copilot in <a class="lnk" href="nine-dynamics-365-sales.html">Dynamics 365 Sales</a>,', 1)

    others = [('nine-full-implementation.html','Package','Full implementation'),('nine-rescue-repair.html','Package','Rescue and Repair'),
              ('nine-sales-accelerator.html','Package','Sales Accelerator'),('nine-service-accelerator.html','Package','Service Accelerator'),
              (v['other'][0],'Move',v['other'][1]),(SUP,'After go-live','Support plans')]
    onav = ''
    for i,(h,m,t) in enumerate(others):
        c = 6 - i
        lt = ' class="lt"' if c >= 6 else ''
        onav += f'      <a{lt} href="{h}" style="--c:var(--b{c})"><span class="mono">{m}</span>{t}</a>\n'

    main = f'''<main id="main">
<div class="wrap">
  <nav class="crumb" aria-label="Breadcrumb"><a href="nine-home.html">Home</a><span class="sep" aria-hidden="true">/</span><a href="nine-packages.html">Packages and support</a><span class="sep" aria-hidden="true">/</span><span aria-current="page">{v['crumb']}</span></nav>
  <section class="hero" aria-labelledby="h1">
    <div class="copy">
      <span class="mono rise" style="--d:0">Move &middot; {v['crumb']}</span>
      <h1 class="h1" id="h1" style="font-size:clamp(40px,5.4vw,72px)"><span class="ln"><span style="--d:1">Move from {n}</span></span> <span class="ln"><span style="--d:2">to Dynamics 365 Sales</span></span></h1>
      <p class="lead rise" style="--d:3">{e(v['answer'])}</p>
      <div class="acts rise" style="--d:4">
        <a class="btn btn-p" href="{BOOK}">Book a call</a>
        <a class="lnk" href="#checklist">Get the migration checklist <span>&rarr;</span></a>
      </div>
      <p class="phone-note rise" style="--d:5">Prefer the phone? Call <a href="tel:+18442640729">1-844-264-0729</a>.</p>
    </div>
    <div>
      <div class="grid9" role="list" aria-label="What a move from {n} includes">
{cells}      </div>
      <dl class="spec rise" style="--d:6">
        <div><dt class="mono">Price</dt><dd>Fixed, quoted in writing after a short call</dd></div>
        <div><dt class="mono">Time</dt><dd>[Brian sets] weeks</dd></div>
        <div><dt class="mono">Users</dt><dd>Up to [Brian sets] users</dd></div>
      </dl>
      <p class="fine" style="margin-top:12px">Microsoft licenses are not part of the package price. Microsoft's list price for Dynamics 365 Sales is $65, $105 or $150 per user per month, paid yearly.</p>
    </div>
  </section>

  <section class="sec" aria-label="Facts" style="padding-top:clamp(56px,6vw,88px)">
    <div class="proof big rev">
      <a class="pf" href="#prices"><b class="num">$65</b><span>a user a month, Microsoft's lowest Dynamics 365 Sales list price</span><small>Compare list prices &rarr;</small></a>
      <a class="pf" href="#process"><b class="num">4</b><span>stages: Plan, Build, Go live and Run</span><small>How a move runs &rarr;</small></a>
      <a class="pf" href="nine-stories.html"><b class="num">23</b><span>client stories, new builds to rescues</span><small>See the stories &rarr;</small></a>
      <a class="pf" href="#support"><b class="num">$500</b><span>a month, where support plans start</span><small>See support plans &rarr;</small></a>
    </div>
  </section>

  <section class="sec" id="included" aria-labelledby="inc-h">
    <div class="sec-head rev">
      <h2 class="h2" id="inc-h">What moves from {n} to Dynamics 365?</h2>
      <p class="lead">{e(v['inc_lead'])}</p>
    </div>
    <div class="fit two-col rev">
      <div class="yes"><h3 class="h3">Included</h3><ul>
{inc}      </ul></div>
      <div class="no"><h3 class="h3">Not included</h3><ul>
{li(v['noinc'])}      </ul></div>
    </div>
    <div class="inc-foot rev">
      <p class="fine" style="margin-top:0">Anything outside the package is a written change order you approve before work starts. Want to know what your {v['unit']} would take? Book a call.</p>
      <div class="acts"><a class="btn btn-p" href="{BOOK}">Ask about a move from {n}</a></div>
    </div>
  </section>

  <section class="sec" id="prices" aria-labelledby="pr-h">
    <div class="sec-head rev">
      <h2 class="h2" id="pr-h">{e(v['price_h'])}</h2>
      <p class="lead">{e(v['price_lead'])}</p>
    </div>
    <div class="tbl-wrap rev" tabindex="0" role="region" aria-label="Table, scrolls sideways on small screens">
      <table class="tbl">
        <caption class="mono" style="text-align:left;padding-bottom:10px">List prices per user per month, from each vendor's own pricing page</caption>
        <thead><tr><th scope="col">Edition</th><th scope="col">List price per user per month</th><th scope="col">Billing</th><th scope="col">{e(v['col5'])}</th></tr></thead>
        <tbody>
{rows}        </tbody>
      </table>
      <p class="fine">List prices from each vendor's own pricing page, checked {v.get('checked', '4 Nov 2026')}; we check them again before this page goes live. Editions do not line up feature for feature, so compare the edition you use today with the plan you need. Neither price includes setup or support.</p>
      <p class="fine">{e(v['price_note2'])}</p>
    </div>
  </section>

  <section class="sec" id="fit" aria-labelledby="fit-h">
    <div class="fitsplit">
    <div class="side rev">
      <h2 class="h2" id="fit-h">Is a move from {n} right for your team?</h2>
      <p class="lead">{e(v['fit_lead'])}</p>
      <p class="notsure-l">Not sure? Book a call and we will tell you which package fits.</p>
      <div class="acts" style="margin-top:0"><a class="btn btn-p" href="{BOOK}">Book a call</a></div>
    </div>
    <div class="fit rev">
      <div class="yes"><h3 class="h3">A good fit if</h3><ul>
        <li>Your team already works in Outlook and Teams every day.</li>
        <li>You sell through a sales process with stages, quotes or products.</li>
{li(v['fit_yes'])}      </ul></div>
      <div class="no"><h3 class="h3">Consider another option if</h3><ul>
        <li>You need other systems connected on day one. A <a class="lnk" href="nine-full-implementation.html">full implementation</a> covers data moves and integrations.</li>
        <li>{e(v['fit_no'])}</li>
        <li>You have one or two people who only need a shared address book.</li>
      </ul></div>
    </div>
    </div>
  </section>

  <section class="sec" id="process" aria-labelledby="st-h">
    <div class="sec-head rev">
      <h2 class="h2" id="st-h">How does a move from {n} run?</h2>
      <p class="lead">Every project runs through the same four stages: Plan, Build, Go live and Run. You see the written plan before we build, and every change after that is written down and approved.</p>
    </div>
STAGES
  </section>

SUPPORT

  <section class="sec" id="faq" aria-labelledby="fq-h">
    <div class="faqsplit">
    <div class="faqside rev">
      <h2 class="h2" id="fq-h">{n} move questions we get asked</h2>
      <p class="lead" style="margin-top:18px">Something else on your mind? Ask us on a call. You get a straight answer, whether or not you work with us.</p>
      <div class="acts" style="margin-top:24px"><a class="btn btn-p" href="{BOOK}">Book a call</a><a class="lnk" href="tel:+18442640729">1-844-264-0729 <span>&rarr;</span></a></div>
    </div>
    <div>
    <div class="faq rev">
{fq_html}    </div>
    </div>
    </div>
  </section>

  <section class="sec" id="checklist" aria-labelledby="ck-h">
    <div class="ckl rev">
      <div>
        <span class="mono">Free download</span>
        <h2 class="h2" id="ck-h" style="margin-top:10px">Want the migration readiness checklist?</h2>
        <p class="lead">The {e(v['checklist'])}: what to gather and decide before a move. Tell us where to send it.</p>
      </div>
      <div class="ph" role="note">[Form: the existing checklist download form (first name, last name, work email, consent). Michael supplies the checklist file and the form before this page goes live.]</div>
    </div>
  </section>

  <section class="sec" id="others" aria-labelledby="op-h" >
    <h2 class="mono" id="op-h" style="font-weight:400;margin:0 0 16px">Other packages</h2>
    <nav class="lnav rev" aria-labelledby="op-h">
{onav}    </nav>
  </section>
</div>

'''
    stages = base[base.index('    <div class="stages flowbar">'):]
    stages = stages[:stages.index('  </section>')].rstrip('\n')
    sup = base[base.index('  <section class="sec" id="support"'):]
    sup = sup[:sup.index('  </section>') + len('  </section>')]
    main = main.replace('STAGES', stages).replace('SUPPORT', sup)
    t = tail.replace('<main id="main">', '')
    page = hd + hdr + '\n\n' + main + t
    page = page.replace('licences', 'licenses')
    if not v.get('checklist'):
        page = re.sub(r'\n  <section class="sec" id="checklist".*?</section>\n', '\n', page, flags=re.S)
        page = page.replace('<a class="lnk" href="#checklist">Get the migration checklist <span>&rarr;</span></a>',
                            '<a class="lnk" href="nine-guides.html">Free checkups, no obligation <span>&rarr;</span></a>')
    open(P + v['file'], 'w', encoding='utf-8').write(page)
    print(v['file'], len(page))

import glob, os
for f in sorted(glob.glob('/home/claude/lb/moves-data/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    k = os.path.basename(f)[:-5]
    for x in ('sources', 'live_page_notes', 'notes'): d.pop(x, None)
    d['grid'] = [tuple(g) for g in d['grid']]; d['rows'] = [tuple(r) for r in d['rows']]
    d['q4'] = tuple(d['q4']); d['q5'] = tuple(d['q5']); d['other'] = tuple(d['other'])
    V[k] = d
for k in V: build(k)
