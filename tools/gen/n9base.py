import re, json, html as H
P = '/home/claude/lb/pages/'
base = open(P + 'nine-sales-accelerator.html', encoding='utf-8').read()
head = base[:base.index('<header class="top">')]
hdr = base[base.index('<header class="top">'):base.index('</header>') + 9]
tail = base[base.index('<section class="final"'):]
BOOK = 'nine-book.html'
def e(s): return H.escape(s, quote=False)
def mkhead(title, meta, crumbs, extra_ld=(), faq=None, css=''):
    hd = re.sub(r'<title>.*?</title>', f'<title>{e(title)}</title>', head)
    hd = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{H.escape(meta)}">', hd)
    hd = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', hd, flags=re.S)
    ld = [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u} for i,(n,u) in enumerate(crumbs)]}] + list(extra_ld)
    if faq:
        qa = [(q, re.sub('<[^>]+>','',a)) for q,a in faq]
        qa = [(q,a) for q,a in qa if '[' not in a]
        ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":H.unescape(a)}} for q,a in qa]})
    hd = hd.replace('<style>', ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + '<style>', 1)
    if css: hd = hd.replace('</head>', '<style>' + css + '</style>\n</head>', 1)
    return hd
def crumbnav(items):
    out = []
    for n,h in items[:-1]: out.append(f'<a href="{h}">{e(n)}</a><span class="sep" aria-hidden="true">/</span>')
    out.append(f'<span aria-current="page">{e(items[-1][0])}</span>')
    return '  <nav class="crumb" aria-label="Breadcrumb">' + ''.join(out) + '</nav>\n'
def grid(label, cells):
    out = []
    for i,(bg,h,lab,nm,ds,ar,cls) in enumerate(cells):
        a = f'<span class="ar" aria-hidden="true">{ar}</span>' if ar else ''
        out.append(f'        <a class="cell{(" "+cls) if cls else ""}" style="background:var(--{bg});--d:{i}" href="{h}"><span class="lab">{lab}</span><span class="nm">{nm}</span><span class="ds">{ds}</span>{a}</a>\n')
    return f'      <div class="grid9" role="list" aria-label="{label}">\n' + ''.join(out) + '      </div>\n'
def faqsec(h2, faq, sid='faq'):
    items = ''.join(f'      <details><summary>{e(q)}</summary><p>{a}</p></details>\n' for q,a in faq)
    return f'''  <section class="sec" id="{sid}" aria-labelledby="fq-h">
    <div class="faqsplit">
    <div class="faqside rev">
      <h2 class="h2" id="fq-h">{h2}</h2>
      <p class="lead" style="margin-top:18px">Something else on your mind? Ask us on a call. You get a straight answer, whether or not you work with us.</p>
      <div class="acts" style="margin-top:24px"><a class="btn btn-p" href="{BOOK}">Book a call</a><a class="lnk" href="nine-faq.html">All questions <span>&rarr;</span></a></div>
    </div>
    <div>
    <div class="faq rev">
{items}    </div>
    </div>
    </div>
  </section>
'''
def lnav(title, links):
    cols = ['b6','b5','b4','b3','b2','b1']
    a = ''.join(f'      <a{" class=\"lt\"" if i==0 else ""} href="{h}" style="--c:var(--{cols[i]})"><span class="mono">{m}</span>{t}</a>\n' for i,(h,m,t) in enumerate(links))
    return f'''  <section class="sec" id="others" aria-labelledby="op-h">
    <h2 class="mono" id="op-h" style="font-weight:400;margin:0 0 16px">{title}</h2>
    <nav class="lnav rev" aria-labelledby="op-h">
{a}    </nav>
  </section>
'''
def write(fn, hd, main):
    open(P + fn, 'w', encoding='utf-8').write(hd + hdr + '\n\n<main id="main">\n<div class="wrap">\n' + main + '</div>\n\n' + tail)
