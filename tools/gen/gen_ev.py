"""Email Verifier product page, Draft 1. Facts from moves-data/PRODUCTS-RESEARCH.md section 1 (live page read 9 Nov 2026).
Prices as published on the live page; EULA conflict and Sendex owner flagged for Brian."""
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
BOOK = 'nine-book.html'
URL = 'https://www.encloud9.com/encloud9-dynamics-365-crm-services/microsoft-dynamics-365-crm-accelerators/'
def e(s): return H.escape(s, quote=False)
TITLE = 'Dynamics 365 Accelerators, Fixed-Scope Packages | enCloud9'
URL = 'https://www.encloud9.com/email-verifier/'
def e(s): return H.escape(s, quote=False)
TITLE = 'Email Verifier for Dynamics 365 | enCloud9'
META = 'Email Verifier checks every email address in Dynamics 365 for deliverability, in real time and in bulk. Annual plans from $240. First 100 verifications free.'
ANSWER = ("Email Verifier is our Dynamics 365 add-on that checks every email address in your CRM for deliverability. It verifies new leads and contacts "
          "as they are entered, cleans existing lists in bulk, and scores each address. Annual plans start at $240 for 12,000 verifications, and your first 100 are free.")
FAQ = [
 ("How do I start with Email Verifier?", "Book a call or ask for the free start. Your first 100 verifications are free, and our team sets Email Verifier up in your Dynamics 365 environment, so you see results on your own records before you pick a plan."),
 ("Does Email Verifier run inside Dynamics 365?", "Yes. Email Verifier is built for Dynamics 365 and runs in your environment. It works with Power Apps, so verification fits the way your team already enters leads and contacts."),
 ("What is the quality score?", "Each address gets a score that ranks its quality, so marketers can put high-value prospects first and hold back addresses that are likely to bounce."),
 ("What kinds of bad addresses does it catch?", "It shows why an address failed: disposable, role-based, defunct or undeliverable. Your team sees the reason on the record, not just a pass or fail."),
 ("How is this different from the built-in email validation in Dynamics 365?", "Built-in validation catches basic problems like bad syntax. Email Verifier checks whether an address can actually receive mail, scores it, and cleans whole lists in bulk."),
 ("Does it help with ClickDimensions or Customer Insights campaigns?", "Yes. Verifying a list before a send cuts bounces in any email platform, including ClickDimensions and Dynamics 365 Customer Insights."),
 ("What does Email Verifier cost?", "Annual plans are $240 for 12,000 verifications, $1,080 for 60,000, or $1,920 for 120,000. You can add verification packs anytime, and the first 100 verifications are free."),
]
PLANS = [('Essentials', '$240', '12,000', '2.0 cents'), ('Premium (most popular)', '$1,080', '60,000', '1.8 cents'), ('Enterprise', '$1,920', '120,000', '1.6 cents')]
FEATS = [
 ('Real time', 'Verify at the point of entry', 'Every address is checked as it is entered, so bad data stays out of your CRM from the start.'),
 ('Bulk', 'Clean what you already have', 'Verify whole marketing lists, leads and contacts in one pass before a big campaign.'),
 ('Score', 'A quality score on every address', 'Each address is ranked, so marketers can put high-value prospects first.'),
 ('Reasons', 'See why an address failed', 'Disposable, role-based, defunct or undeliverable, shown on the record.'),
 ('Sending', 'Fewer bounces', 'Fewer bounces and spam traps protect your sender reputation.'),
 ('Built in', 'Runs in your Dynamics 365', 'Runs in your environment and works with Power Apps.'),
]
hd = re.sub(r'<title>.*?</title>', f'<title>{e(TITLE)}</title>', head)
hd = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{H.escape(META)}">', hd)
hd = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', hd, flags=re.S)
ld = [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":"https://www.encloud9.com/"},
        {"@type":"ListItem","position":2,"name":"Email Verifier","item":URL}]},
      {"@context":"https://schema.org","@type":"SoftwareApplication","name":"Email Verifier for Dynamics 365","applicationCategory":"BusinessApplication",
       "operatingSystem":"Microsoft Dynamics 365","url":URL,"publisher":{"@type":"Organization","name":"enCloud9","url":"https://www.encloud9.com/"},
       "offers":[{"@type":"Offer","name":n.split(' (')[0],"price":p.strip('$').replace(',',''),"priceCurrency":"USD"} for n,p,_,_ in PLANS]},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in FAQ]}]
hd = hd.replace('<style>', ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + '<style>', 1)
rows = ''.join(f'          <tr><th scope="row">{e(a)}</th><td data-l="Price">{b} a year</td><td data-l="Verifications a year">{c}</td><td data-l="Per verification">{d}</td></tr>\n' for a, b, c, d in PLANS)
faq = ''.join(f'      <details><summary>{e(q)}</summary><p>{e(a)}</p></details>\n' for q, a in FAQ)
cols = ['b1','b2','b3','b4','b5','b6','b7','b8','b9']
cells = ''.join(f'        <a class="cell{" lt" if i>4 else ""}" style="background:var(--{cols[i]});--d:{i}" href="#how"><span class="lab">{l}</span><span class="nm">{e(t)}</span><span class="ds">{e(d[:60].rsplit(" ",1)[0] if len(d)>60 else d)}</span><span class="ar" aria-hidden="true">&#8600;</span></a>\n' for i,(l,t,d) in enumerate(FEATS[:4]))
cells += '        <a class="cell core" style="background:var(--b5);--d:4" href="#plans"><span class="lab">Email Verifier</span><span class="nm">100 free</span><span class="ds">Your first 100 verifications</span></a>\n'
cells += ''.join(f'        <a class="cell lt" style="background:var(--{c});--d:{i}" href="{h}"><span class="lab">{l}</span><span class="nm">{t}</span><span class="ds">{d}</span><span class="ar" aria-hidden="true">{ar}</span></a>\n' for i,(c,h,l,t,d,ar) in enumerate([
  ('b6','#plans','Plans','From $240','12,000 verifications a year','&#8600;'),
  ('b7','#how','Sending','Fewer bounces','Protect your sender reputation','&#8600;'),
  ('b8','nine-story-bgland.html','Client story','B&amp;G Landholdings','Cleaner email data in Dynamics 365','&#8599;'),
  ('b9','nine-marketing.html','Pairs with','Marketing','ClickDimensions and Customer Insights','&#8599;')], start=5))
feats = ''.join(f'      <div class="cell-f"><span class="mono">{l}</span><h3 class="h3">{e(t)}</h3><p>{e(d)}</p></div>\n' for l,t,d in FEATS)
main = f'''<main id="main">
<div class="wrap">
  <nav class="crumb" aria-label="Breadcrumb"><a href="nine-home.html">Home</a><span class="sep" aria-hidden="true">/</span><a href="nine-marketing.html">Marketing</a><span class="sep" aria-hidden="true">/</span><span aria-current="page">Email Verifier</span></nav>
  <section class="hero" aria-labelledby="h1">
    <div class="copy">
      <span class="mono rise" style="--d:0">Add-on &middot; Built by enCloud9</span>
      <h1 class="h1" id="h1" style="font-size:clamp(40px,5.4vw,72px)"><span class="ln"><span style="--d:1">Email Verifier</span></span> <span class="ln"><span style="--d:2">for Dynamics 365</span></span></h1>
      <p class="lead rise" style="--d:3">{e(ANSWER)}</p>
      <div class="acts rise" style="--d:4">
        <a class="btn btn-p" href="{BOOK}">Start with 100 free</a>
        <a class="lnk" href="#plans">See the plans <span>&rarr;</span></a>
      </div>
      <p class="phone-note rise" style="--d:5">Prefer the phone? Call <a href="tel:+18442640729">1-844-264-0729</a>.</p>
    </div>
    <div>
      <div class="grid9" role="list" aria-label="What Email Verifier does">
{cells}      </div>
    </div>
  </section>

  <section class="sec" id="how" aria-labelledby="hw-h">
    <div class="sec-head rev">
      <h2 class="h2" id="hw-h">How does Email Verifier work?</h2>
      <p class="lead">It checks each address when a lead or contact is entered, cleans the records you already have in one pass, and writes the result to the Dynamics 365 record: a quality score and, for a failed address, the reason. Your team acts on that before a campaign goes out.</p>
    </div>
    <div class="fgrid rev">
{feats}    </div>
  </section>

  <section class="sec" id="plans" aria-labelledby="pl-h">
    <div class="sec-head rev">
      <h2 class="h2" id="pl-h">How much does Email Verifier cost?</h2>
      <p class="lead">Three annual plans, priced by how many addresses you verify in a year. Every plan includes real time and bulk verification, and you can add verification packs anytime. Your first 100 verifications are free.</p>
    </div>
    <div class="tbl-wrap rev" tabindex="0" role="region" aria-label="Table, scrolls sideways on small screens">
      <table class="tbl">
        <caption class="mono" style="text-align:left;padding-bottom:10px">Email Verifier plans</caption>
        <thead><tr><th scope="col">Plan</th><th scope="col">Price</th><th scope="col">Verifications a year</th><th scope="col">Per verification</th></tr></thead>
        <tbody>
{rows}        </tbody>
      </table>
      <p class="fine">Prices in US dollars, as published on encloud9.com, read 9 Nov 2026.</p>
    </div>
    <div class="acts rev" style="margin-top:28px"><a class="btn btn-p" href="{BOOK}">Start with 100 free</a></div>
  </section>

  <section class="sec" id="fit" aria-labelledby="fit-h">
    <div class="fitsplit">
    <div class="side rev">
      <h2 class="h2" id="fit-h">Who is Email Verifier for?</h2>
      <p class="lead">Dynamics 365 teams that send email campaigns, and teams whose contact volume is growing faster than anyone can check it by hand. That was the situation at B&amp;G Landholdings, where bad addresses were entering the CRM.</p>
      <div class="acts" style="margin-top:0"><a class="btn btn-p" href="nine-story-bgland.html">Read the B&amp;G story</a></div>
    </div>
    <div class="fit rev">
      <div class="yes"><h3 class="h3">A good fit if</h3><ul>
        <li>You send campaigns from ClickDimensions or Dynamics 365 Customer Insights. See <a class="lnk" href="nine-marketing.html">marketing automation</a>.</li>
        <li>Leads come in from web forms and imports, and nobody checks the addresses.</li>
        <li>Bounces are rising, or a list is about to go out for a big campaign.</li>
      </ul></div>
    </div>
    </div>
  </section>

  <section class="sec" id="faq" aria-labelledby="fq-h">
    <div class="faqsplit">
    <div class="faqside rev">
      <h2 class="h2" id="fq-h">Email Verifier questions we get asked</h2>
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
    <h2 class="mono" id="op-h" style="font-weight:400;margin:0 0 16px">Related</h2>
    <nav class="lnav rev" aria-labelledby="op-h">
      <a class="lt" href="nine-marketing.html" style="--c:var(--b6)"><span class="mono">Marketing</span>Marketing automation</a>
      <a href="nine-story-bgland.html" style="--c:var(--b5)"><span class="mono">Client story</span>B&amp;G Landholdings</a>
      <a href="nine-support.html" style="--c:var(--b4)"><span class="mono">After go-live</span>Support plans</a>
    </nav>
  </section>
</div>

'''
css = '''<style>.fgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line,#ddd);border:1px solid var(--line,#ddd)}.fgrid .cell-f{background:var(--bg,#fff);padding:24px}.fgrid .cell-f p{margin:8px 0 0}
@media(max-width:900px){.fgrid{grid-template-columns:1fr 1fr}}@media(max-width:560px){.fgrid{grid-template-columns:1fr}}
@media(max-width:640px){#plans .tbl{min-width:0}#plans .tbl thead{position:absolute;left:-9999px}#plans .tbl tr{display:grid;grid-template-columns:1fr;padding:14px 0;border-bottom:1px solid var(--line)}#plans .tbl tbody th,#plans .tbl td{display:block;border:0;padding:2px 0}#plans .tbl td::before{content:attr(data-l) ": ";font-family:var(--label);font-size:13px;color:var(--muted)}}</style>
'''
hd = hd.replace('</head>', css + '</head>', 1)
open(P + 'nine-email-verifier.html', 'w', encoding='utf-8').write(hd + hdr + '\n\n' + main + tail)
print('ok', len(ANSWER.split()), len(TITLE), len(META), [len(a.split()) for q,a in FAQ])
