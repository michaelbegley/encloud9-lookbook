"""Port live blog posts into the Look 9 post template, Draft 1. Text read from the live WordPress REST API in Michael's Chrome, 9 Nov 2026,
saved in posts/*.txt (headings fixed where the live post used paragraphs as headings; booking-link CTAs dropped for the template CTA).
Dashes converted to commas or colons (house rule). Authors and categories from the blog index (nine-blog.html)."""
import re, json, html as H, glob, os
L = '/home/claude/lb/pages/'
TPL = open(L + 'nine-blog-post.html', encoding='utf-8').read()
AUTH = {'1': 'Brian Begley', '5': 'Kristin Caniglia'}
META = {  # slug: (file, category, topic page, topic label, topic blurb, meta description)
 'clickdimensions-dashboards-2025-update': ('nine-post-click-dashboards.html','Marketing automation','nine-marketing.html','Marketing automation','ClickDimensions and email marketing in Dynamics 365.',
   'ClickDimensions added five dashboards inside Dynamics 365 for campaigns, emails, forms, surveys and landing pages. What they show and where they help.'),
 'dynamics-365-sales-qualification-agent': ('nine-post-qualification-agent.html','Copilot and AI','nine-copilot.html','Copilot and agents','The agents in Dynamics 365 Sales and Customer Service.',
   'How the Dynamics 365 Sales Qualification Agent researches, scores and follows up with leads against your ideal customer profile, with a worked example.'),
 'encloud9-recognized-on-crm-software-blogs-best-dynamics-365-partner-list-2026': ('nine-post-partner-list-2026.html','News','nine-about.html','About enCloud9','Who we are and how we work.',
   "enCloud9 was named on CRM Software Blog's Best Dynamics 365 Partner List 2026, the only partner in the Professional Services category."),
 'how-dynamics-365-activate-makes-leaving-salesforce-easier': ('nine-post-activate-salesforce.html','Switching to Dynamics 365','nine-move-salesforce.html','Move from Salesforce','How we move a team from Salesforce to Dynamics 365.',
   'Dynamics 365 Activate maps a Salesforce environment before a move. What it does, what it cannot decide for you, and how to plan a better CRM.'),
 'how-to-stop-leads-from-falling-through-the-cracks-in-dynamics-365': ('nine-post-leads-cracks.html','Admin and how-to','nine-dynamics-365-sales.html','Dynamics 365 Sales','The app your sellers work in every day.',
   'Four ways to stop leads going cold in Dynamics 365: an owner for every lead, a next step with sequences, regular reviews and automation as a safety net.'),
 'how-to-track-the-last-activity-date-in-microsoft-dynamics-365-sales': ('nine-post-last-activity.html','Admin and how-to','nine-dynamics-365-sales.html','Dynamics 365 Sales','The app your sellers work in every day.',
   'Dynamics 365 has no built-in last activity date. Add rollup fields for last activity and next activity due, step by step, with a video tutorial.'),
 'microsoft-dataverse-storage-notifications': ('nine-post-storage-warning.html','Admin and how-to','nine-storage.html','Dataverse storage','Free Dataverse Storage Analysis.',
   'What a Microsoft Dataverse storage warning means, what happens when you go over your limit, and how to get back under it before sandboxes lock.'),
 'microsoft-dynamics-365-crm-skills-copilot': ('nine-post-crm-skills.html','Copilot and AI','nine-copilot.html','Copilot and agents','The agents in Dynamics 365 Sales and Customer Service.',
   'Microsoft added 30 CRM skills for Copilot, built on more than 180 Dynamics 365 tools. What they do for sales, service and marketing teams.'),
 'which-dynamics-365-customizations-are-worth-it-and-which-ones-we-usually-advise-against': ('nine-post-customizations.html','Admin and how-to','nine-rescue-repair.html','Rescue and Repair','For a Dynamics 365 system that has grown too complex.',
   'The Dynamics 365 customizations we usually recommend, the ones we advise against, and five questions to ask before you build one.'),
}
def nodash(t):
    t = re.sub(r'\s+[–—]\s+', ': ', t); t = t.replace('—', ', ').replace('–', ', ')
    return re.sub(r',\s*,', ',', t).replace(' ,', ',')
def slugify(t): return re.sub(r'[^a-z0-9]+', '-', re.sub('<[^>]+>', '', t).lower()).strip('-')[:40]
def parse(path):
    lines = open(path, encoding='utf-8').read().strip().split('\n')
    m = re.match(r'# (.*) \| (\S+) \| author (\d+)', lines[0]); title, date, aid = m.groups()
    blocks = []
    for ln in lines[1:]:
        if not ln.strip(): continue
        k, _, v = ln.partition(': '); blocks.append((k, nodash(v.strip())))
    return H.unescape(title), date, AUTH[aid], blocks
def render(blocks):
    out, toc, faq, i, answer, cta = [], [], [], 0, None, None
    in_faq = False
    while i < len(blocks):
        k, v = blocks[i]
        if k == 'ANSWER': answer = v
        elif k == 'CTA': cta = v.split('|')
        elif k == 'BLOCKQUOTE' and answer is None and not out: answer = v
        elif k == 'H2':
            in_faq = bool(re.search(r'frequently asked', v, re.I))
            if in_faq: out.append('        <h2 id="faq">Frequently asked questions</h2>\n        <div class="faq">\n'); toc.append(('faq', 'Frequently asked questions'))
            else:
                a = slugify(v); toc.append((a, re.sub('<[^>]+>', '', v))); out.append(f'        <h2 id="{a}">{v}</h2>\n')
        elif k == 'H3' and in_faq:
            q = re.sub('<[^>]+>', '', v); a = blocks[i+1][1] if i+1 < len(blocks) and blocks[i+1][0] == 'P' else ''
            faq.append((q, re.sub('<[^>]+>', '', a))); out.append(f'          <details><summary>{q}</summary><p>{a}</p></details>\n'); i += 1
        elif k in ('H3', 'H4'): out.append(f'        <h3>{v}</h3>\n')
        elif k == 'LI':
            items = []
            while i < len(blocks) and blocks[i][0] == 'LI': items.append(blocks[i][1]); i += 1
            out.append('        <ul>\n' + ''.join(f'          <li>{x}</li>\n' for x in items) + '        </ul>\n'); continue
        elif k in ('P', 'BLOCKQUOTE'): out.append(f'        <p>{v}</p>\n')
        if in_faq and (i+1 >= len(blocks) or blocks[i+1][0] == 'H2' or blocks[i+1][0] == 'CTA'): out.append('        </div>\n'); in_faq = False
        i += 1
    return ''.join(out), toc, faq, answer, cta
SEO = {'clickdimensions-dashboards-2025-update':'New ClickDimensions Dashboards in Dynamics 365',
 'dynamics-365-sales-qualification-agent':'The Dynamics 365 Sales Qualification Agent, Explained',
 'encloud9-recognized-on-crm-software-blogs-best-dynamics-365-partner-list-2026':"enCloud9 on CRM Software Blog's Best Partner List 2026",
 'how-to-stop-leads-from-falling-through-the-cracks-in-dynamics-365':'Stop Leads Falling Through the Cracks in Dynamics 365',
 'how-to-track-the-last-activity-date-in-microsoft-dynamics-365-sales':'Track the Last Activity Date in Dynamics 365 Sales',
 'microsoft-dynamics-365-crm-skills-copilot':'30 New Dynamics 365 CRM Skills for Copilot',
 'which-dynamics-365-customizations-are-worth-it-and-which-ones-we-usually-advise-against':'Which Dynamics 365 Customizations Are Worth It?'}
built = []
for slug, (fn, cat, tp, tl, tb, meta) in META.items():
    title, date, author, blocks = parse(f'posts/{slug}.txt')
    body, toc, faq, answer, cta = render(blocks)
    url = f'https://www.encloud9.com/blog/{slug}/'
    import datetime; d = datetime.date.fromisoformat(date[:10]); dh = f'{d:%B} {d.day}, {d.year}'
    words = len(re.sub('<[^>]+>', ' ', body).split()); mins = max(1, round(words / 230))
    ans = f'        <p class="answer"><span class="mono">The short answer</span><strong>{answer}</strong></p>\n' if answer else ''
    ctah, ctap, ctaurl, ctab = (('Want help with this?', 'Tell us where your Dynamics 365 system is today. You get a straight answer, whether or not you work with us.', 'nine-book.html', 'Book a call with enCloud9')
                               if not cta else ('Don\'t ignore the warning', cta[0], cta[1], cta[2]))
    toc.append(('see', ctah))
    tail = f'''        <section class="abox" aria-labelledby="ab-h">
          <span class="pic" aria-hidden="true"><i style="--c:var(--b9)"></i><i style="--c:var(--b8)"></i><i style="--c:var(--b7)"></i><i style="--c:var(--b6)"></i><i style="--c:var(--b5)"></i><i style="--c:var(--b4)"></i><i style="--c:var(--b3)"></i><i style="--c:var(--b2)"></i><i style="--c:var(--b1)"></i></span>
          <div><h2 class="nm" id="ab-h">About the author: {author}</h2><p>[One line on {author.split()[0]}'s role at enCloud9, {author.split()[0]} confirms.]</p></div>
        </section>

        <div class="ctabox">
          <h2 id="see">{ctah}</h2>
          <p>{ctap}</p>
          <a class="btn btn-w" href="{ctaurl}">{ctab}</a>
        </div>
'''
    s = TPL
    a0 = s.index('      <div class="art" id="art">'); a1 = s.index('      </div>\n    </div>\n  </article>')
    s = s[:a0] + '      <div class="art" id="art">\n' + ans + body + '\n' + tail + s[a1:]
    s = re.sub(r'<h1 class="h1 rise" id="h1" style="--d:2">.*?</h1>', lambda m: f'<h1 class="h1 rise" id="h1" style="--d:2">{H.escape(title)}</h1>', s, count=1, flags=re.S)
    s = re.sub(r'<span class="draft rise".*?</span>\n', '', s, count=1, flags=re.S)
    s = re.sub(r'<span class="mono cat rise" style="--d:1">.*?</span>', f'<span class="mono cat rise" style="--d:1">{cat}</span>', s, count=1, flags=re.S)
    s = re.sub(r'<p class="byline rise".*?</p>', f'<p class="byline rise" style="--d:3"><span class="av" aria-hidden="true"></span><span>By <b>{author}</b></span><span><b>{dh}</b></span><span>{mins} min read</span></p>', s, count=1, flags=re.S)
    gl = [('b9','Published',dh),('b8','Topic',cat),('b6','Reading time',f'{mins} minutes'),('b4','Written by',author)]
    s = re.sub(r'<ul class="gl">.*?</ul>', lambda m: '<ul class="gl">\n' + ''.join(f'          <li{" class=\"lt\"" if j<3 else ""} style="--c:var(--{c});--k:{j}"><span class="k">{k}</span><b>{v}</b></li>\n' for j,(c,k,v) in enumerate(gl)) + '        </ul>', s, count=1, flags=re.S)
    s = re.sub(r'(<summary>On this page</summary>\s*<ol>).*?(</ol>)', lambda m: m.group(1) + '\n' + ''.join(f'            <li><a href="#{a}">{t}</a></li>\n' for a,t in toc) + '          ' + m.group(2), s, count=1, flags=re.S)
    short = SEO.get(slug, title)
    s = re.sub(r'<span aria-current="page">.*?</span></nav>', lambda m: f'<span aria-current="page">{H.escape(short)}</span></nav>', s, count=1)
    s = re.sub(r'(<h2 class="h2" id="nx-h">Next step</h2>\s*<p class="lead">).*?(</p>)', lambda m: m.group(1) + f'See {tl}, start with a free checkup, or talk to us.' + m.group(2), s, count=1, flags=re.S)
    s = s.replace('href="nine-copilot.html#genpages"><span class="pt-top"><span class="mono">Copilot and AI</span>', f'href="{tp}"><span class="pt-top"><span class="mono">Related</span>', 1)
    s = s.replace('<span class="nm">Generative pages</span><span class="ds">How generative pages fit with Copilot and agents in Dynamics 365.</span><span class="pt-foot"><span class="go">See generative pages &rarr;</span>',
                  f'<span class="nm">{tl}</span><span class="ds">{tb}</span><span class="pt-foot"><span class="go">See {tl} &rarr;</span>', 1)
    s = s.replace('<span class="ds">Tell us about the screen your team wishes it had.</span>', '<span class="ds">Tell us where your system is today.</span>', 1)
    built.append((slug, fn, title, cat, dh))
    t = SEO.get(slug, title)
    assert len(t) <= 60, t
    s = re.sub(r'<title>.*?</title>', lambda m: f'<title>{H.escape(t)}</title>', s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', lambda m: f'<meta name="description" content="{H.escape(meta)}">', s, count=1)
    s = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', s, flags=re.S)
    ld = [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.encloud9.com/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://www.encloud9.com/blog/"},{"@type":"ListItem","position":3,"name":title,"item":url}]},
          {"@context":"https://schema.org","@type":"BlogPosting","headline":title,"description":meta,"url":url,"datePublished":date[:10],"author":{"@type":"Person","name":author},"publisher":{"@type":"Organization","name":"enCloud9","url":"https://www.encloud9.com/"}}]
    if faq: ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})
    s = s.replace('<style>', ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + '<style>', 1)
    s = s.replace('Look 9, Nine, built pages: Blog post', 'Look 9, Nine, built pages: Blog post', 1)
    open(L + fn, 'w', encoding='utf-8').write(s)
    print(fn, words, 'words', len(t), len(meta), 'faq', len(faq), 'h2', len(toc)-1)
# related posts: 3 newest other ported posts on each page
for slug, fn, title, cat, dh in built:
    s = open(L + fn, encoding='utf-8').read()
    others = [b for b in built if b[0] != slug][:3]
    cols = ['b7','b5','b3']
    rel = ''.join(f'      <a class="pc" style="--c:var(--{cols[j]})" href="{o[1]}"><span class="mono">{o[3]} &middot; {o[4]}</span><span class="t">{H.escape(o[2])}</span><span class="d">{H.escape(META[o[0]][5][:90].rsplit(" ",1)[0])}.</span><span class="go">Read the post &#8599;</span></a>\n' for j, o in enumerate(others))
    s = re.sub(r'(<div class="rel rev">\n).*?(    </div>\n  </section>)', lambda m: m.group(1) + rel + m.group(2), s, count=1, flags=re.S)
    s = s.replace('<p class="lead">More on Copilot and Dynamics 365.', '<p class="lead">More from the enCloud9 blog.', 1)
    open(L + fn, 'w', encoding='utf-8').write(s)
