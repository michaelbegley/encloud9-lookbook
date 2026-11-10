"""Client story template (T5), Draft 2. Data driven: one dict per story (fields in SPEC-STORY-TEMPLATE-NOTES.md).
Optional fields (timeline, tiles, quote, next_steps, found_us, packages) drop their blocks when empty.
Story CSS lives in nine.css (body.p-story), so story pages carry no inline style."""
import re, json, html as H
P = '/home/claude/lb/pages/'
base = open(P + 'nine-sales-accelerator.html', encoding='utf-8').read()
head = base[:base.index('<header class="top">')]
hdr = base[base.index('<header class="top">'):base.index('</header>') + 9]
tail = base[base.index('<section class="final"'):]
BOOK = 'nine-book.html'
LIVE = 'https://www.encloud9.com/blog/success_stories/'
HUB_LIVE = 'https://www.encloud9.com/about-encloud9/microsoft-dynamics-365-success/'

STORIES = {
 'hogan': dict(
  file='nine-story-hogan.html', slug='hogans-crm-rescue-story-a-fresh-start-with-dynamics-365',
  client='Hogan Assessments', work_type='Rescue or fix',
  title='Hogan Assessments: Dynamics 365 Rescue | enCloud9',
  meta='How enCloud9 cleaned up Hogan Assessments’ over-customized Dynamics 365 and moved the team to the out-of-the-box Sales Hub, on time and under budget.',
  h1=('Hogan Assessments:', 'a usable CRM in three months'),
  answer="Hogan Assessments, a personality assessment company in Tulsa, Oklahoma, had a Dynamics 365 system so heavily customized that sales reps avoided it. We removed the unnecessary customizations and moved the team to the out-of-the-box Dynamics 365 Sales Hub. Within three months Hogan had a clean, simpler system, and the project finished on time and under budget.",
  facts=[('Client','Hogan Assessments'),('Location','Tulsa, OK'),('Industry','Personality assessments for hiring and development, certification and training'),
         ('Starting point','An over-customized Dynamics 365 system'),('Products','Dynamics 365 Sales Hub; HubSpot integration'),
         ('Services','Implementation, sales team training, mailbox configuration')],
  timeline='Within three months',
  tiles=[('3 months','to a clean, simpler system'),('On time','and under budget'),('Standard','Sales Hub, lead to opportunity')],
  outcomes=['Activities and follow-ups became trackable.','Management finally had visibility into the pipeline.',
            'A standard lead-to-opportunity process gives the team consistent workflows.'],
  chapters=[
   ('What was wrong with Hogan’s CRM?', ["Hogan’s Dynamics 365 system had been customized so heavily that it had become “virtually unusable.” Sales reps avoided it, and management lacked the pipeline visibility it needed to drive performance.",
                                            "Hogan found enCloud9 through one of our YouTube videos."]),
   ('What did we change?', ["We removed the unnecessary customizations and moved Hogan to the out-of-the-box Dynamics 365 Sales Hub, with a standard lead-to-opportunity process.",
                            "We also trained the sales team and configured their mailboxes."]),
   ('What changed day to day?', ["The sales team now works in a system that is easy to use, with consistent workflows. Activities and follow-ups are trackable, and management can see the pipeline."]),
  ],
  next_steps=('What comes next for Hogan?', "Hogan plans to add sequences, the Dynamics 365 Sales feature that lines up a set of steps (emails, calls and tasks) for sellers to follow, to automate more of its sales process."),
  quote=None,
  packages=[('nine-rescue-repair.html','Package for work like this','Rescue and Repair'),('nine-dynamics-365-sales.html','Product','Dynamics 365 Sales')],
  author='Kristin Caniglia', published='2025-05-28', published_h='May 28, 2025',
  prev=('milestone','Milestone Leasing','A clean-up and optimization of an existing Dynamics 365 system'),
  next=(LIVE+'how-price-mds-transformed-healthcare-operations-with-dynamics-365/','PriceMDs','A new Dynamics 365 system in place of Monday CRM'),
 ),
 'milestone': dict(
  file='nine-story-milestone.html', slug='how-milestone-leasing-optimized-dynamics-365-to-support-sales-and-lease-renewals',
  client='Milestone Leasing', work_type='Rescue or fix',
  title='Milestone Leasing: Dynamics 365 Clean-up | enCloud9',
  meta='How enCloud9 cleaned up and automated Milestone Leasing’s Dynamics 365: lease renewals, lead routing, quote approvals and standard quotes from the CRM.',
  h1=('Milestone Leasing:', 'a cleaner CRM that tracks renewals'),
  answer="Milestone Leasing, a trailer, chassis and container leasing company in St. Charles, Missouri, had a Dynamics 365 system that had become hard to use, with reps updating opportunities by hand. We cleaned it up, automated lease renewals, lead routing and quote approvals, and set reps up to create standard quotes directly from the CRM.",
  facts=[('Client','Milestone Leasing'),('Location','St. Charles, MO'),('Industry','Trailer, chassis and container leasing'),
         ('Starting point','An existing Dynamics 365 system that had become hard to use'),('Products','Dynamics 365 Sales; Dataverse; Document Core Pack; Click'),
         ('Services','Clean-up, optimization, implementation, data migration, training and ongoing support')],
  timeline=None,
  tiles=[('Renewals','tracked automatically, not by hand'),('Quotes','created directly from the CRM')],
  outcomes=['Lease renewals, task assignments and follow-ups run automatically.','Leads are routed and quotes approved inside the CRM.',
            'Reps create standard, professional quotes directly from the CRM.','Pipeline visibility matches real sales activity.'],
  chapters=[
   ('What was wrong with Milestone’s CRM?', ["Milestone Leasing had an existing Dynamics 365 system, but it had become hard to use. Updating opportunities by hand could take each rep significant time, so the CRM felt more like a burden than a help."]),
   ('What did we change?', ["We removed unused components, cleaned the data and simplified workflows. We streamlined lead and opportunity management, replaced manual renewal tracking with automated renewals, task assignments and follow-ups, and set up lead routing and quote approvals.",
                            "Reps now create standard quotes directly from the CRM with Document Core Pack."]),
   ('What changed day to day?', ["The CRM now matches how Milestone sells and renews leases: renewals and follow-ups are automated, and the pipeline reflects real sales activity. We continue to work with Milestone on further improvements."]),
  ],
  next_steps=None, quote=None,
  packages=[('nine-rescue-repair.html','Package for work like this','Rescue and Repair'),('nine-dynamics-365-sales.html','Product','Dynamics 365 Sales')],
  author='Kristin Caniglia', published='2026-06-16', published_h='June 16, 2026',
  prev=(LIVE+'collaborative-for-children-success-story/','Collaborative for Children','A custom Dynamics 365 solution, designed and built'),
  next=('hogan','Hogan Assessments','An over-customized system cleaned up within three months'),
 ),
}

def e(s): return H.escape(s, quote=False)
SHORT = {'cfc': 'Collaborative for Children', 'tensionpa': 'Tension Packaging', 'schiff': 'The Schiff Group', 'tensionenv': 'Tension Envelope',
         'bgland': 'B&G Landholdings', 'pricemds': 'PriceMDs', 'msa': 'MSA Source', 'kbg': 'KBG Technologies', 'elmwood': 'Elmwood',
         'compana': 'Compana', 'miles': 'Miles Christi', 'jasco': 'JASCO', 'jwc': 'JWC Environmental', 'aureon': 'Aureon', 'ppc': 'PPC Flex'}
def short(k, v):
    if k in SHORT: return SHORT[k]
    m = re.search(r'\(([A-Z]{2,5})\)', v['client'])
    return m.group(1) if m else v['client'].split()[0]
def link(x): return STORIES[x]['file'] if x in STORIES else x

def build(k):
    v = STORIES[k]; url = LIVE + v['slug'] + '/'
    hd = re.sub(r'<title>.*?</title>', f'<title>{e(v["title"])}</title>', head)
    hd = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{H.escape(v["meta"])}">', hd)
    hd = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', hd, flags=re.S)
    hd = re.sub(r'<style>.*?</style>\n?', '', hd, flags=re.S)          # story CSS is in nine.css
    ld = [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Home","item":"https://www.encloud9.com/"},
            {"@type":"ListItem","position":2,"name":"Client stories","item":HUB_LIVE},
            {"@type":"ListItem","position":3,"name":v['client'],"item":url}]},
          {"@context":"https://schema.org","@type":"Article","headline":' '.join(v['h1']),"description":v['answer'],"url":url,
           "datePublished":v['published'],"author":{"@type":"Person","name":v['author']},
           "publisher":{"@type":"Organization","name":"enCloud9","url":"https://www.encloud9.com/"},"about":{"@type":"Organization","name":v['client']}}]
    hd = hd.replace('</head>', ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + '</head>', 1)
    hd = hd.replace('<body class="p-pkg">', '<body class="p-story">')
    hd = hd.replace('nine-sales-accelerator.html" class="on" aria-current="page">Sales Accelerator', f'{v["file"]}" class="on" aria-current="page">Story: {short(k, v)}')

    h1 = ' '.join(f'<span class="ln"><span style="--d:{i+1}">{e(t)}</span></span>' for i, t in enumerate(v['h1']))
    facts = list(v['facts']) + ([('Timeline', v['timeline'])] if v['timeline'] else [])
    facts_h = ''.join(f'        <div><dt class="mono">{a}</dt><dd>{e(b)}</dd></div>\n' for a, b in facts)
    tiles = v['tiles'] or []
    tiles_h = ''
    if tiles:
        tiles_h = (f'  <section class="sec" aria-label="Results at a glance" style="padding-top:clamp(56px,6vw,88px)">\n'
                   f'    <div class="proof big rev n{len(tiles)}">\n' +
                   ''.join(f'      <div class="pf"><b class="num">{e(n)}</b><span>{e(t)}</span></div>\n' for n, t in tiles) +
                   '    </div>\n  </section>\n')
    outc = ''.join(f'        <li>{e(x)}</li>\n' for x in v['outcomes'])
    quote_h = ''
    if v['quote']:
        q = v['quote']
        quote_h = f'        <figure class="squote"><blockquote>“{e(q["text"])}”</blockquote><figcaption>{e(q["name"])}, {e(q["title"])}</figcaption></figure>\n'
    chaps = ''.join(f'      <div class="chap rev"><h2 class="h2">{e(h2)}</h2>' + ''.join(f'<p>{e(p)}</p>' for p in ps) + '</div>\n' for h2, ps in v['chapters'])
    if v['next_steps']:
        chaps += f'      <div class="chap rev"><h2 class="h2">{e(v["next_steps"][0])}</h2><p>{e(v["next_steps"][1])}</p></div>\n'
    cols = ['b5', 'b3', 'b1']
    pk = ''
    if v['packages']:
        pk = ('  <section class="sec" id="used" aria-label="Related packages and products">\n'
              '    <p class="mono slab">Related packages and products</p>\n'
              f'    <nav class="lnav n{len(v["packages"])} rev" aria-label="Related packages and products">\n' +
              ''.join(f'      <a href="{h}" style="--c:var(--{cols[i]})"><span class="mono">{m}</span>{t}</a>\n' for i, (h, m, t) in enumerate(v['packages'])) +
              '    </nav>\n  </section>\n\n')
    pv, nx = v['prev'], v['next']

    main = f'''<main id="main">
<div class="wrap">
  <nav class="crumb" aria-label="Breadcrumb"><a href="nine-home.html">Home</a><span class="sep" aria-hidden="true">/</span><a href="nine-stories.html">Client stories</a><span class="sep" aria-hidden="true">/</span><span aria-current="page">{v['client']}</span></nav>
  <section class="hero" aria-labelledby="h1">
    <div class="copy">
      <span class="mono rise" style="--d:0">Client story &middot; {e(v['work_type'])}</span>
      <h1 class="h1" id="h1">{h1}</h1>
      <p class="lead rise" style="--d:3">{e(v['answer'])}</p>
      <p class="byline rise" style="--d:4">Written by {e(v['author'])} &middot; Published {v['published_h']}</p>
      <div class="acts rise" style="--d:4">
        <a class="btn btn-p" href="{BOOK}">Book a call</a>
        <a class="lnk" href="nine-stories.html">All client stories <span>&rarr;</span></a>
      </div>
    </div>
    <div>
      <span class="mono">Key facts</span>
      <dl class="spec rise" style="--d:5">
{facts_h}      </dl>
    </div>
  </section>

{tiles_h}
  <section class="sec" id="story" aria-labelledby="ko-h">
    <div class="story-body">
      <div class="side rev">
        <h2 class="h2" id="ko-h">What changed for {e(short(k, v))}?</h2>
        <ul class="outc">
{outc}        </ul>
{quote_h}        <div class="acts" style="margin-top:24px"><a class="btn btn-p" href="{BOOK}">Book a call</a></div>
      </div>
      <div>
{chaps}      </div>
    </div>
  </section>

{pk}  <section class="sec" id="more" aria-label="More client stories" style="padding-top:clamp(40px,5vw,64px)">
    <p class="mono slab">More client stories</p>
    <nav class="pn rev" aria-label="Previous and next client stories">
      <a href="{link(pv[0])}"><span class="mono">&larr; Previous story</span><span class="t">{pv[1]}</span><span class="d">{e(pv[2])}</span></a>
      <a class="nx" href="{link(nx[0])}"><span class="mono">Next story &rarr;</span><span class="t">{nx[1]}</span><span class="d">{e(nx[2])}</span></a>
    </nav>
    <div class="acts" style="margin-top:24px"><a class="lnk" href="nine-stories.html">All 23 client stories <span>&rarr;</span></a></div>
  </section>
</div>

'''
    t = tail.replace('Tell us where your system is today. You get a straight answer on which package fits, whether or not you work with us.',
                     'Tell us where your system is today. You get a straight answer on what it would take, whether or not you work with us.')
    open(P + v['file'], 'w', encoding='utf-8').write(hd + hdr + '\n\n' + main + t)
    print(v['file'])

# ---- the other stories: data files written from the live story pages (stories-data/<key>.json) ----
import glob, os
HUB_ORDER = ['bgland', 'cfc', 'milestone', 'hogan', 'pricemds', 'tensionpa', 'schiff', 'msa', 'kbg', 'elmwood', 'compana',
             'miles', 'tensionenv', 'crl', 'jasco', 'rlh', 'jwc', 'aureon', 'rei', 'bsi', 'ppc']   # stories hub order; WID and BG Peterson held for Brian
PKG = {'New build': ('nine-full-implementation.html', 'Package for work like this', 'Full implementation'),
       'Rescue or fix': ('nine-rescue-repair.html', 'Package for work like this', 'Rescue and Repair'),
       'Upgrade': ('nine-rescue-repair.html', 'Package for work like this', 'Rescue and Repair'),
       'Integration': ('nine-full-implementation.html', 'Package for work like this', 'Full implementation'),
       'Support': ('nine-support.html#plans', 'After go-live', 'Support plans'),
       'Add-on': None}
def products_links(prod):
    p = prod.lower(); out = []
    if 'customer service' in p: out.append(('nine-customer-service.html', 'Product', 'Customer Service'))
    if 'sales' in p or not out: out.insert(0, ('nine-dynamics-365-sales.html', 'Product', 'Dynamics 365 Sales'))
    if 'copilot' in p: out.append(('nine-copilot.html', 'Product', 'Copilot and AI'))
    if 'email verifier' in p: out.append(('nine-email-verifier.html', 'Product', 'Email Verifier'))
    return out
for f in sorted(glob.glob('/home/claude/lb/stories-data/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    k = d['key']
    prod = dict(d['facts']).get('Products', '')
    pk = ([PKG[d['work_type']]] if PKG.get(d['work_type']) else []) + products_links(prod)
    STORIES[k] = dict(file=f'nine-story-{k}.html', slug=d['slug'], client=d['client'], work_type=d['work_type'],
        title=d['title'], meta=d['meta'], h1=tuple(d['h1']), answer=d['answer'], facts=[tuple(x) for x in d['facts']],
        timeline=d.get('timeline'), tiles=[tuple(x) for x in (d.get('tiles') or [])], outcomes=d['outcomes'],
        chapters=[(c[0], c[1]) for c in d['chapters']], next_steps=tuple(d['next_steps']) if d.get('next_steps') else None,
        quote=d.get('quote'), packages=pk[:3], author=d['author'], published=d['published'], published_h=d['published_h'])
# prev and next follow the hub order among built stories
built = [k for k in HUB_ORDER if k in STORIES]
def blurb(k):
    v = STORIES[k]; s = v['h1'][-1]
    return s[0].upper() + s[1:]
for i, k in enumerate(built):
    p, n = built[i - 1], built[(i + 1) % len(built)]
    STORIES[k]['prev'] = (p, STORIES[p]['client'], blurb(p))
    STORIES[k]['next'] = (n, STORIES[n]['client'], blurb(n))
for k in STORIES: build(k)
print(len(STORIES), 'stories built')
