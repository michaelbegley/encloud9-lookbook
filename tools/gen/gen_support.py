"""Support plans page (T4), Draft 1. Facts: dynamics365support.com plan cards, footnotes and terms (PLANS-CHECK.md, 4 Nov 2026,
D365SUPPORT-SWEEP.md), and the shared round 8 support wording on the package pages. Brian 4 Nov: Stability is the minimum plan for new clients."""
import re, json, html as H
P = '/home/claude/lb/pages/'
base = open(P + 'nine-sales-accelerator.html', encoding='utf-8').read()
head = base[:base.index('<header class="top">')]
hdr = base[base.index('<header class="top">'):base.index('</header>') + 9]
tail = base[base.index('<section class="final"'):]
BOOK = 'https://www.encloud9.com/lp/schedule-a-meeting/'
SUP = 'nine-support.html#plans'
URL = 'https://www.encloud9.com/microsoft-dynamics-365-support-services/'
def e(s): return H.escape(s, quote=False)

TITLE = 'Dynamics 365 Support Plans, From $500 a Month | enCloud9'
META = 'Dynamics 365 support plans from enCloud9: Stability $500 a month for 4 hours, Optimization $1,500 for 20 hours, Partnership $2,000 for 35 hours.'
ANSWER = ("enCloud9's Dynamics 365 support plans start at $500 a month for 4 hours on Stability, the minimum plan for new clients. "
          "Optimization is $1,500 a month for 20 hours and up to 50 users, and Partnership is $2,000 a month for 35 hours and 50 users and up. "
          "Every monthly plan includes Microsoft escalation management.")
PLANS = [
 dict(c='b4', tag='Hourly', name='On-Demand', price='$200', unit='an hour', sub='As needed, no retainer. Anyone can ask. No SLA.',
      inc=['Case portal access', 'Same-day response, no SLA', 'Self-service knowledge base', 'Monthly newsletter', 'Live webinars']),
 dict(c='b1', tag='Minimum plan', name='Stability', price='$500', unit='a month', sub='4 hours a month.',
      inc=['Case portal access', '1-hour response time', 'Break and fix support', 'Enhancements included', 'System monitoring', 'User management', 'Annual assessment meeting']),
 dict(c='b2', tag='Monthly plan', name='Optimization', price='$1,500', unit='a month', sub='20 hours a month. Up to 50 users.',
      inc=['Everything in Stability', 'Training documentation', 'Video library access', 'Monthly usage reporting', 'Quarterly assessments', 'Add-on hour blocks available', 'Solution update management']),
 dict(c='b3', tag='Monthly plan', name='Partnership', price='$2,000', unit='a month', sub='35 hours a month. 50 users and up.',
      inc=['Everything in Optimization', 'Built for larger organizations', 'Discounted add-on hours', 'Full solution management', 'Priority routing', 'Multi-user coordination']),
]
FINE = ("Monthly plans run on a 12-month agreement. New clients pay an onboarding fee of up to one month's charge. Hours 7:00am to 5:00pm Central, "
        "Monday to Friday. Monthly plans include a 1-hour response during business hours, which means a person has picked up "
        "your request, not that it is solved. Every monthly plan includes Microsoft escalation management. "
        "Plan hours cover the system you run; new builds, integrations and data moves are quoted as packages, and Microsoft licenses are separate.")
FAQ = [
 ("How much does Dynamics 365 support cost?", "Support starts at $500 a month for 4 hours on the Stability plan, which is the minimum plan for new clients. Optimization is $1,500 a month for 20 hours and Partnership is $2,000 a month for 35 hours. Monthly plans run on a 12-month agreement."),
 ("Which support plan fits our team?", "Optimization is built for teams of up to 50 users and Partnership for 50 users and up. Stability gives 4 hours a month for teams that need steady break and fix help, enhancements and user management."),
 ("What does the 1-hour response mean?", "On monthly plans, a person picks up your request within 1 hour during business hours, 7:00am to 5:00pm Central, Monday to Friday. It means the request has been picked up and reviewed, not that it is solved."),
 ("Is there a setup or onboarding fee?", "New clients pay an onboarding fee of up to one month's charge."),
 ("What happens if we need more hours?", "Optimization can add blocks of hours, and Partnership gets discounted add-on hours. On-Demand work is $200 an hour."),
 ("Do we need a support plan after go-live?", "Yes. New clients start on at least the Stability plan, $500 a month for 4 hours, on a 12-month agreement. Monthly plans include a 1-hour response during business hours, 7:00am to 5:00pm Central, Monday to Friday."),
 ("Can you support a Dynamics 365 system another partner built?", "Yes. If the system needs repair first, Rescue and Repair gets it working, then a support plan keeps it that way."),
]

hd = re.sub(r'<title>.*?</title>', f'<title>{e(TITLE)}</title>', head)
hd = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{H.escape(META)}">', hd)
hd = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', hd, flags=re.S)
ld = [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":"https://www.encloud9.com/"},
        {"@type":"ListItem","position":2,"name":"Packages and support","item":"https://www.encloud9.com/crm-cloud-automation-solutions/"},
        {"@type":"ListItem","position":3,"name":"Support plans","item":URL}]},
      {"@context":"https://schema.org","@type":"Service","name":"Dynamics 365 support plans","serviceType":"CRM support","url":URL,"description":ANSWER,
       "provider":{"@type":"Organization","name":"enCloud9","url":"https://www.encloud9.com/"},"areaServed":{"@type":"Country","name":"United States"},
       "hasOfferCatalog":{"@type":"OfferCatalog","name":"Support plans","itemListElement":[
         {"@type":"Offer","name":"On-Demand","price":"200","priceCurrency":"USD","unitText":"hour"},
         {"@type":"Offer","name":"Stability","price":"500","priceCurrency":"USD","unitText":"month"},
         {"@type":"Offer","name":"Optimization","price":"1500","priceCurrency":"USD","unitText":"month"},
         {"@type":"Offer","name":"Partnership","price":"2000","priceCurrency":"USD","unitText":"month"}]}},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in FAQ]}]
hd = hd.replace('<style>', ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + '<style>', 1)
hd = hd.replace('</style>', "body.p-pkg .ptiles.plans .ptile .incl{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:6px;font-size:14px;line-height:1.4;color:rgba(255,255,255,.88)}\n"
                "body.p-pkg .ptiles.plans .ptile .incl li{padding-left:16px;position:relative}\n"
                "body.p-pkg .ptiles.plans .ptile .incl li::before{content:'';position:absolute;left:0;top:7px;width:7px;height:7px;background:rgba(255,255,255,.75)}\n"
                "body.p-pkg .every{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;margin-top:8px}\n"
                "body.p-pkg .every div{padding:20px;border:2px solid var(--ink)}body.p-pkg .every b{display:block;font-family:var(--head);font-size:20px;margin-bottom:6px}\n"
                "@media (max-width:760px){body.p-pkg .every{grid-template-columns:1fr}}\nbody.p-pkg .lnav a{overflow-wrap:anywhere}\n</style>", 1)
hd = hd.replace('nine-sales-accelerator.html" class="on" aria-current="page">Sales Accelerator', 'nine-support.html" class="on" aria-current="page">Support plans')

tiles = ''
for i, p in enumerate(PLANS):
    g = ''.join(f'<i class="{"on" if j == 4 else ("d" if j < i else "")}"></i>' for j in range(9))
    top = f'<span class="min">{p["tag"]}</span>' if p['tag'] == 'Minimum plan' else f'<span class="mono">{p["tag"]}</span>'
    tiles += (f'      <div role="listitem" class="ptile" style="--c:var(--{p["c"]})"><span class="pt-top">{top}<span class="g big" aria-hidden="true">{g}</span></span>'
              f'<span class="nm">{p["name"]}</span><span class="price">{p["price"]}<small>{p["unit"]}</small></span><span class="ds">{e(p["sub"])}</span>'
              f'<ul class="incl">' + ''.join(f'<li>{e(x)}</li>' for x in p['inc']) + '</ul></div>\n')
faq = ''.join(f'      <details><summary>{e(q)}</summary><p>{e(a)}</p></details>\n' for q, a in FAQ)
faq = faq.replace('<p>Yes. If the system needs repair first, Rescue and Repair', '<p>Yes. If the system needs repair first, <a class="lnk" href="nine-rescue-repair.html">Rescue and Repair</a>')

main = f'''<main id="main">
<div class="wrap">
  <nav class="crumb" aria-label="Breadcrumb"><a href="nine-home.html">Home</a><span class="sep" aria-hidden="true">/</span><a href="nine-packages.html">Packages and support</a><span class="sep" aria-hidden="true">/</span><span aria-current="page">Support plans</span></nav>
  <section class="hero" aria-labelledby="h1">
    <div class="copy">
      <span class="mono rise" style="--d:0">After go-live &middot; Support plans</span>
      <h1 class="h1" id="h1" style="font-size:clamp(40px,5.4vw,72px)"><span class="ln"><span style="--d:1">Dynamics 365</span></span> <span class="ln"><span style="--d:2">support plans</span></span></h1>
      <p class="lead rise" style="--d:3">{e(ANSWER)}</p>
      <div class="acts rise" style="--d:4">
        <a class="btn btn-p" href="{BOOK}">Book a call</a>
        <a class="lnk" href="#plans">See the four plans <span>&rarr;</span></a>
      </div>
      <p class="phone-note rise" style="--d:5">Prefer the phone? Call <a href="tel:+18442640729">1-844-264-0729</a>.</p>
    </div>
    <div>
      <dl class="spec rise" style="--d:5">
        <div><dt class="mono">From</dt><dd>$500 a month for 4 hours (Stability)</dd></div>
        <div><dt class="mono">Term</dt><dd>12-month agreement on monthly plans</dd></div>
        <div><dt class="mono">Hours</dt><dd>7:00am to 5:00pm Central, Monday to Friday</dd></div>
        <div><dt class="mono">Response</dt><dd>1 hour during business hours on monthly plans</dd></div>
        <div><dt class="mono">Onboarding</dt><dd>Up to one month's charge for new clients</dd></div>
      </dl>
    </div>
  </section>

  <section class="sec" aria-label="Facts" style="padding-top:clamp(56px,6vw,88px)">
    <div class="proof big rev">
      <a class="pf" href="#plans"><b class="num">$500</b><span>a month for 4 hours, the minimum plan</span></a>
      <a class="pf" href="#plans"><b class="num">1 hour</b><span>response during business hours on monthly plans</span></a>
      <a class="pf" href="nine-story-compana.html"><b class="num">Support</b><span>Compana Pet Brands: ongoing support for Dynamics 365 Sales and Customer Service</span><small>Read the story &rarr;</small></a>
      <a class="pf" href="nine-stories.html"><b class="num">23</b><span>client stories, new builds to rescues</span><small>See the stories &rarr;</small></a>
    </div>
  </section>

  <section class="sec" id="plans" aria-labelledby="sp-h">
    <div class="sec-head rev">
      <h2 class="h2" id="sp-h">What does each support plan include?</h2>
      <p class="lead">Stability covers break and fix work, enhancements, system monitoring and user management for 4 hours a month. Optimization adds training documentation, usage reporting and quarterly assessments, and Partnership adds full solution management and priority routing for larger teams.</p>
    </div>
    <div class="ptiles plans rev" role="list" aria-label="Support plans, prices, hours and what each includes">
{tiles}    </div>
    <div class="sp-foot rev">
      <p class="fine">{e(FINE)}</p>
      <div class="acts"><a class="btn btn-p" href="{BOOK}">Ask about a support plan</a></div>
    </div>
  </section>

  <section class="sec" id="every" aria-labelledby="ev-h">
    <div class="sec-head rev">
      <h2 class="h2" id="ev-h">What comes with every monthly plan?</h2>
      <p class="lead">Every monthly plan includes a dedicated Dynamics consultant, customization support and Microsoft escalation management.</p>
    </div>
    <div class="every rev">
      <div><b>A dedicated consultant</b>A dedicated Dynamics consultant on your account.</div>
      <div><b>Customization support</b>Help with customizations to your Dynamics 365 system.</div>
      <div><b>Microsoft escalation</b>We manage escalations to Microsoft for you.</div>
    </div>
  </section>

  <section class="sec" id="fit" aria-labelledby="fit-h">
    <div class="fitsplit">
    <div class="side rev">
      <h2 class="h2" id="fit-h">Is a support plan right for your business?</h2>
      <p class="lead">A support plan fits a business whose Dynamics 365 system is live and needs regular help. If you are still building or your system is not working, start with a package.</p>
      <div class="acts" style="margin-top:0"><a class="btn btn-p" href="{BOOK}">Book a call</a></div>
    </div>
    <div class="fit rev">
      <div class="yes"><h3 class="h3">A good fit if</h3><ul>
        <li>Your Dynamics 365 system is live and your team uses it every day.</li>
        <li>You want a named consultant and a 1-hour response during business hours.</li>
        <li>You need changes, fixes or user updates most months.</li>
      </ul></div>
      <div class="no"><h3 class="h3">Consider another option if</h3><ul>
        <li>You need a new system. An <a class="lnk" href="nine-accelerators.html">accelerator</a> or a <a class="lnk" href="nine-full-implementation.html">full implementation</a> is built for that.</li>
        <li>Your system is stalled or not working. <a class="lnk" href="nine-rescue-repair.html">Rescue and Repair</a> comes first.</li>
        <li>You need help only now and then. On-Demand at $200 an hour is built for that.</li>
      </ul></div>
    </div>
    </div>
  </section>

  <section class="sec" id="stories" aria-labelledby="cs-h">
    <div class="sec-head rev">
      <h2 class="h2" id="cs-h">Who runs on an enCloud9 support plan?</h2>
      <p class="lead">Two of our 23 client stories with ongoing support: one multi-brand pet products company and one laboratory that has been a client for over 15 years.</p>
    </div>
    <div class="stories rev">
      <a class="story" href="nine-story-compana.html"><span class="mono">St. Louis, MO &middot; Dynamics 365 Sales and Customer Service</span><span class="big">Ongoing</span><span class="t">Compana Pet Brands</span><span class="d">Ongoing support and optimization for Dynamics 365 Sales and Customer Service, with Copilot Studio work alongside.</span><span class="go">Read the Compana story &rarr;</span></a>
      <a class="story" href="nine-story-crl.html"><span class="mono">Lenexa, KS &middot; Dynamics 365 &middot; Support contract</span><span class="big">15+ years</span><span class="t">Clinical Reference Laboratory</span><span class="d">An implementation, then a support contract. A client of enCloud9 for over 15 years.</span><span class="go">Read the CRL story &rarr;</span></a>
    </div>
  </section>

  <section class="sec" id="faq" aria-labelledby="fq-h">
    <div class="faqsplit">
    <div class="faqside rev">
      <h2 class="h2" id="fq-h">Support questions we get asked</h2>
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
    <h2 class="mono" id="op-h" style="font-weight:400;margin:0 0 16px">Packages that lead into support</h2>
    <nav class="lnav rev" aria-labelledby="op-h">
      <a class="lt" href="nine-full-implementation.html" style="--c:var(--b6)"><span class="mono">Package</span>Full implementation</a>
      <a href="nine-rescue-repair.html" style="--c:var(--b5)"><span class="mono">Package</span>Rescue and Repair</a>
      <a href="nine-sales-accelerator.html" style="--c:var(--b4)"><span class="mono">Package</span>Sales Accelerator</a>
      <a href="nine-service-accelerator.html" style="--c:var(--b3)"><span class="mono">Package</span>Service Accelerator</a>
      <a href="nine-move-salesforce.html" style="--c:var(--b2)"><span class="mono">Move</span>Move from Salesforce</a>
      <a href="nine-contact.html" style="--c:var(--b1)"><span class="mono">Company</span>Contact us</a>
    </nav>
  </section>
</div>

'''
t = tail.replace('Tell us where your system is today. You get a straight answer on which package fits, whether or not you work with us.',
                 'Tell us where your system is today. You get a straight answer on which plan fits, whether or not you work with us.')
open(P + 'nine-support.html', 'w', encoding='utf-8').write(hd + hdr + '\n\n' + main + t)
print('ok', len(ANSWER.split()), len(TITLE), len(META))
