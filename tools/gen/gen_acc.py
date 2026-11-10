"""Accelerators hub (T4 hub), Draft 1. All copy reuses the Sales and Service Accelerator Draft 2 pages word for word or in summary;
Microsoft prices as on those pages (spec 2.3, read 4 Nov 2026). Marketing Accelerator is $5,000 fixed (Brian, call 27); the hub shows only Sales and Service (cards() is unused; the ROWS table renders)."""
import re, json, html as H
P = '/home/claude/lb/pages/'
base = open(P + 'nine-sales-accelerator.html', encoding='utf-8').read()
head = base[:base.index('<header class="top">')]
hdr = base[base.index('<header class="top">'):base.index('</header>') + 9]
tail = base[base.index('<section class="final"'):]
stages = base[base.index('    <div class="stages flowbar">'):]
stages = stages[:stages.index('  </section>')].rstrip('\n')
sup = base[base.index('  <section class="sec" id="support"'):]
sup = sup[:sup.index('  </section>') + len('  </section>')]
BOOK = 'https://www.encloud9.com/lp/schedule-a-meeting/'
URL = 'https://www.encloud9.com/encloud9-dynamics-365-crm-services/microsoft-dynamics-365-crm-accelerators/'
def e(s): return H.escape(s, quote=False)
TITLE = 'Dynamics 365 Accelerators, Fixed-Scope Packages | enCloud9'
META = 'Fixed-scope packages for a first Dynamics 365 system: the Sales Accelerator for Dynamics 365 Sales and the Service Accelerator for Customer Service.'
ANSWER = ("Our accelerators are fixed-scope packages for a first Dynamics 365 system: the Sales Accelerator for Dynamics 365 Sales and the Service Accelerator "
          "for Dynamics 365 Customer Service. Each has a written scope and a fixed price, quoted after a short call. Microsoft licenses are a separate cost, "
          "and support plans start at $500 a month.")
FAQ = [
 ("What is a Dynamics 365 accelerator?", "Our accelerators are fixed-scope packages for a first Dynamics 365 system. You see the scope, price and timeline in writing before we start, and anything outside the package is a written change order you approve first."),
 ("Which accelerator do we need?", "The Sales Accelerator is for a team that sells through stages, quotes or products and is starting on Dynamics 365 Sales. The Service Accelerator is for a team that handles customer requests and is starting on Dynamics 365 Customer Service."),
 ("How much does an accelerator cost?", "Each accelerator is a fixed $7,500 for our build work. Microsoft licenses are a separate cost, and support plans start at $500 a month."),
 ("Is the Sales Accelerator the same as the sales accelerator in Dynamics 365?", "No. Microsoft's sales accelerator is a feature inside Dynamics 365 Sales that gives sellers a prioritized work list and sequences of follow-up steps. Our Sales Accelerator is a package: we build Dynamics 365 Sales for your team to a fixed scope."),
 ("What if we need more than an accelerator covers?", "Anything outside the package is a written change order you approve before work starts. If you need integrations or data from several systems at go-live, a full implementation fits better."),
 ("Are Microsoft licenses included?", "No. Microsoft licenses and Copilot Credits are not part of the package price, and you pay for them separately. As part of the build we assign your licenses to each user and set their security roles, because Microsoft does not let a user open the app until both are done."),
]
ROWS = [
 ('Builds', 'Dynamics 365 Sales configured to your sales stages', 'Dynamics 365 Customer Service configured to how your team handles requests'),
 ('Set up', 'Users, security roles, licenses, records and custom fields', 'Users, security roles, licenses, cases, queues and service levels'),
 ('Fits', 'A first Dynamics 365 Sales system, with a standard sales process and data in spreadsheets or one old CRM', 'A first Dynamics 365 Customer Service system, with requests in a shared inbox, spreadsheets or one old help desk tool'),
 ('Microsoft list price', '$65, $105 or $150 per user per month, paid yearly', '$50, $105 or $195 per user per month, paid yearly'),
 ('Copilot', 'Included in Sales Enterprise and Premium', 'Included in Customer Service Enterprise and Premium'),
 ('Our price', '$7,500 fixed', '$7,500 fixed'),
 ('Time', '[Brian sets] weeks', '[Brian sets] weeks'),
]
hd = re.sub(r'<title>.*?</title>', f'<title>{e(TITLE)}</title>', head)
hd = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{H.escape(META)}">', hd)
hd = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', hd, flags=re.S)
ld = [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":"https://www.encloud9.com/"},
        {"@type":"ListItem","position":2,"name":"Packages and support","item":"https://www.encloud9.com/crm-cloud-automation-solutions/"},
        {"@type":"ListItem","position":3,"name":"Accelerators","item":URL}]},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in FAQ]}]
hd = hd.replace('<style>', ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + '<style>', 1)
hd = hd.replace('nine-sales-accelerator.html" class="on" aria-current="page">Sales Accelerator', 'nine-accelerators.html" class="on" aria-current="page">Accelerators')
rows = ''.join(f'          <tr><th scope="row">{a}</th><td>{e(b)}</td><td>{e(c)}</td></tr>\n' for a, b, c in ROWS)
faq = ''.join(f'      <details><summary>{e(q)}</summary><p>{e(a)}</p></details>\n' for q, a in FAQ)
card = lambda n, h, c, num, t, d, inc, dl='<dl><div><dt>Time</dt><dd>[Brian sets] weeks</dd></div><div><dt>Users</dt><dd>Up to [Brian sets] users</dd></div><div><dt>Price</dt><dd>$7,500</dd></div></dl>': (f'      <a class="pk" style="--c:var(--{c})" href="{h}"><span class="pt-top"><span class="mono">{num}</span></span><h3 class="h3">{t}</h3><p class="one">{e(d)}</p>'
       f'{dl}<span class="go">See the {t} &rarr;</span></a>\n')
cards = (card(1, 'nine-sales-accelerator.html', 'b3', 'Package 03', 'Sales Accelerator', 'Dynamics 365 Sales built with your users, sales stages and records, for a first Dynamics 365 Sales system.', 0) +
         card(2, 'nine-service-accelerator.html', 'b4', 'Package 04', 'Service Accelerator', 'Dynamics 365 Customer Service built with your users, cases, queues and service levels, for a first Customer Service system.', 0) +
         card(3, 'nine-marketing.html', 'b5', 'Marketing', 'Marketing Accelerator', 'ClickDimensions set up in your Dynamics 365, training for your team, and your first email send.', 0, '<dl><div><dt>Includes</dt><dd>Setup, training, first email</dd></div><div><dt>Price</dt><dd>$5,000 fixed</dd></div></dl>'))
pkcss = re.search(r'\.pks\{[^}]*\}', open(P + 'nine-packages.html').read())
main = f'''<main id="main">
<div class="wrap">
  <nav class="crumb" aria-label="Breadcrumb"><a href="nine-home.html">Home</a><span class="sep" aria-hidden="true">/</span><a href="nine-packages.html">Packages and support</a><span class="sep" aria-hidden="true">/</span><span aria-current="page">Accelerators</span></nav>
  <section class="hero" aria-labelledby="h1">
    <div class="copy">
      <span class="mono rise" style="--d:0">Packages &middot; Accelerators</span>
      <h1 class="h1" id="h1" style="font-size:clamp(40px,5.4vw,72px)"><span class="ln"><span style="--d:1">Dynamics 365</span></span> <span class="ln"><span style="--d:2">accelerators</span></span></h1>
      <p class="lead rise" style="--d:3">{e(ANSWER)}</p>
      <div class="acts rise" style="--d:4">
        <a class="btn btn-p" href="{BOOK}">Book a call</a>
        <a class="lnk" href="#compare">Compare the two <span>&rarr;</span></a>
      </div>
      <p class="phone-note rise" style="--d:5">Prefer the phone? Call <a href="tel:+18442640729">1-844-264-0729</a>.</p>
    </div>
    <div>
      <div class="grid9" role="group" aria-label="The two accelerators">
        <a class="cell" style="background:var(--b1);--d:0" href="nine-sales-accelerator.html"><span class="lab">Package 03</span><span class="nm">Sales Accelerator</span><span class="ds">A first Dynamics 365 Sales system</span><span class="ar" aria-hidden="true">&#8599;</span></a>
        <a class="cell" style="background:var(--b2);--d:1" href="nine-service-accelerator.html"><span class="lab">Package 04</span><span class="nm">Service Accelerator</span><span class="ds">A first Customer Service system</span><span class="ar" aria-hidden="true">&#8599;</span></a>
        <a class="cell" style="background:var(--b3);--d:2" href="#compare"><span class="lab">Both</span><span class="nm">Fixed scope</span><span class="ds">Scope, price and timeline in writing first</span><span class="ar" aria-hidden="true">&#8600;</span></a>
        <a class="cell" style="background:var(--b4);--d:3" href="#compare"><span class="lab">Both</span><span class="nm">Licenses</span><span class="ds">Assigned to each user as part of the build</span><span class="ar" aria-hidden="true">&#8600;</span></a>
        <a class="cell core" style="background:var(--b5);--d:4" href="#compare"><span class="lab">Accelerators</span><span class="nm">2 packages</span><span class="ds">Sales and Customer Service</span></a>
        <a class="cell lt" style="background:var(--b6);--d:5" href="#process"><span class="lab">Stage C</span><span class="nm">Training</span><span class="ds">[Brian sets] training sessions</span><span class="ar" aria-hidden="true">&#8600;</span></a>
        <a class="cell lt" style="background:var(--b7);--d:6" href="#process"><span class="lab">After go-live</span><span class="nm">Help</span><span class="ds">[Brian sets] days of help after go-live</span><span class="ar" aria-hidden="true">&#8600;</span></a>
        <a class="cell lt" style="background:var(--b8);--d:7" href="nine-full-implementation.html"><span class="lab">Bigger build</span><span class="nm">Full imple&shy;mentation</span><span class="ds">Data moves and integrations</span><span class="ar" aria-hidden="true">&#8599;</span></a>
        <a class="cell lt" style="background:var(--b9);--d:8" href="#support"><span class="lab">After the package</span><span class="nm">Support plan</span><span class="ds">From $500 a month after go-live</span><span class="ar" aria-hidden="true">&#8600;</span></a>
      </div>
    </div>
  </section>

  <section class="sec" id="compare" aria-labelledby="cp-h">
    <div class="sec-head rev">
      <h2 class="h2" id="cp-h">How do the Sales and Service Accelerators compare?</h2>
      <p class="lead">Both build a first Dynamics 365 system to a fixed scope, with users, security roles, licenses, data import and training. The Sales Accelerator builds Dynamics 365 Sales around your sales stages; the Service Accelerator builds Customer Service around your cases, queues and service levels.</p>
    </div>
    <div class="tbl-wrap rev" tabindex="0" role="region" aria-label="Table, scrolls sideways on small screens">
      <table class="tbl">
        <caption class="mono" style="text-align:left;padding-bottom:10px">The two accelerators side by side</caption>
        <thead><tr><th scope="col"></th><th scope="col">Sales Accelerator</th><th scope="col">Service Accelerator</th></tr></thead>
        <tbody>
{rows}        </tbody>
      </table>
      <p class="fine">Microsoft list prices from Microsoft's own pricing pages, checked 4 Nov 2026. Microsoft licenses are not part of the package price. Anything outside the package is a written change order you approve before work starts.</p>
    </div>
    <div class="acts rev" style="margin-top:28px"><a class="btn btn-p" href="nine-sales-accelerator.html">See the Sales Accelerator</a><a class="btn btn-p" href="nine-service-accelerator.html">See the Service Accelerator</a></div>
  </section>

  <section class="sec" id="fit" aria-labelledby="fit-h">
    <div class="fitsplit">
    <div class="side rev">
      <h2 class="h2" id="fit-h">When is an accelerator the wrong fit?</h2>
      <p class="lead">An accelerator is built for a first system with a standard process. If you need integrations or data from several systems on day one, or you already have a Dynamics 365 system that is not working, another package fits better.</p>
      <p class="notsure-l">Not sure? Book a call and we will tell you which package fits.</p>
      <div class="acts" style="margin-top:0"><a class="btn btn-p" href="{BOOK}">Book a call</a></div>
    </div>
    <div class="fit rev">
      <div class="no"><h3 class="h3">Choose another package if</h3><ul>
        <li>You need other systems connected on day one. A <a class="lnk" href="nine-full-implementation.html">full implementation</a> covers data moves and integrations.</li>
        <li>You already have a Dynamics 365 system that is over-customized or stalled. <a class="lnk" href="nine-rescue-repair.html">Rescue and Repair</a> is built for that.</li>
        <li>You are leaving Salesforce. <a class="lnk" href="nine-move-salesforce.html">Move from Salesforce</a> covers the move.</li>
        <li>You need phone and chat routing for a contact center on day one. Dynamics 365 Contact Center is built for that.</li>
      </ul></div>
    </div>
    </div>
  </section>

  <section class="sec" id="process" aria-labelledby="st-h">
    <div class="sec-head rev">
      <h2 class="h2" id="st-h">How does an accelerator project run?</h2>
      <p class="lead">Every project runs through the same four stages: Plan, Build, Go live and Run. You see the written plan before we build, and every change after that is written down and approved.</p>
    </div>
STAGES
  </section>

SUPPORT

  <section class="sec" id="faq" aria-labelledby="fq-h">
    <div class="faqsplit">
    <div class="faqside rev">
      <h2 class="h2" id="fq-h">Accelerator questions we get asked</h2>
      <p class="lead" style="margin-top:18px">Something else on your mind? Ask us on a call. You get a straight answer, whether or not you work with us.</p>
      <div class="acts" style="margin-top:24px"><a class="btn btn-p" href="{BOOK}">Book a call</a><a class="lnk" href="tel:+18442640729">1-844-264-0729 <span>&rarr;</span></a></div>
    </div>
    <div>
    <div class="faq rev">
{faq}    </div>
    </div>
    </div>
  </section>

  <section class="sec" id="others" aria-labelledby="op-h" >
    <h2 class="mono" id="op-h" style="font-weight:400;margin:0 0 16px">Other packages</h2>
    <nav class="lnav rev" aria-labelledby="op-h">
      <a class="lt" href="nine-full-implementation.html" style="--c:var(--b6)"><span class="mono">Package</span>Full implementation</a>
      <a href="nine-rescue-repair.html" style="--c:var(--b5)"><span class="mono">Package</span>Rescue and Repair</a>
      <a href="nine-sales-accelerator.html" style="--c:var(--b4)"><span class="mono">Package</span>Sales Accelerator</a>
      <a href="nine-service-accelerator.html" style="--c:var(--b3)"><span class="mono">Package</span>Service Accelerator</a>
      <a href="nine-move-salesforce.html" style="--c:var(--b2)"><span class="mono">Move</span>Move from Salesforce</a>
      <a href="nine-support.html" style="--c:var(--b1)"><span class="mono">After go-live</span>Support plans</a>
    </nav>
  </section>
</div>

'''
main = main.replace('STAGES', stages.replace('Build Dynamics 365 Sales to the plan', 'Build to the plan').replace('We build Dynamics 365 Sales to the plan', 'We build Dynamics 365 to the plan').replace('We learn how you sell, using', 'We learn how your team works, using').replace('users, sales stages, data to move', 'users, stages or queues, data to move')).replace('SUPPORT', sup)
open(P + 'nine-accelerators.html', 'w', encoding='utf-8').write(hd + hdr + '\n\n' + main + tail)
print('ok', len(ANSWER.split()), len(TITLE), len(META))
