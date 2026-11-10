import re,glob,os,html,json,csv,collections
src=open('tools/build_site.py').read()
MAP=dict(re.findall(r"'(nine-[\w-]+\.html)':\s*'([^']+)'",src))
pages=sorted(os.path.basename(f) for f in glob.glob('pages/nine-*.html'))
def strip(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
info={};edges=[]
for p in pages:
    t=open('pages/'+p).read()
    title=strip(re.search(r'<title>(.*?)</title>',t,re.S).group(1))
    h1=strip(re.search(r'<h1[^>]*>(.*?)</h1>',t,re.S).group(1)) if '<h1' in t else ''
    info[p]=dict(title=title,h1=h1,url=MAP.get(p,'(not mapped)'))
    # regions
    hdr=re.search(r'<header class="top".*?</header>',t,re.S); ftr=re.search(r'<footer.*?</footer>',t,re.S)
    spans=[('header',hdr.span() if hdr else (0,0)),('footer',ftr.span() if ftr else (0,0))]
    for m in re.finditer(r'<a\b[^>]*href="(nine-[\w-]+\.html)(#[^"]*)?"[^>]*>(.*?)</a>',t,re.S):
        reg='body'
        for name,(a,b) in spans:
            if a<=m.start()<b: reg=name
        edges.append((p,m.group(1),reg,strip(m.group(3))[:60]))
inb=collections.defaultdict(lambda: collections.Counter())
for a,b,reg,txt in edges:
    if a!=b: inb[b][reg]+=1
rows=[]
for p in pages:
    c=inb[p]; out=collections.Counter(reg for a,b,reg,_ in edges if a==p and b!=p)
    rows.append(dict(page=p,url=info[p]['url'],title=info[p]['title'],in_header=c['header'],in_footer=c['footer'],in_body=c['body'],
        out_body=out['body'],out_body_unique=len({b for a,b,reg,_ in edges if a==p and reg=='body' and b!=p})))
with open(os.environ['OUT']+'/LINK-MAP.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(dict(info=info,edges=edges),open(os.environ['OUT']+'/linkmap.json','w'))
print('pages',len(pages),'edges',len(edges))
print('in header nav (unique pages):',sorted({b for a,b,r,_ in edges if r=='header'}))
print('NOT in header or footer:',[r['page'] for r in rows if r['in_header']==0 and r['in_footer']==0][:90])
print('body-inbound 0 and not in footer/header (orphans):',[r['page'] for r in rows if r['in_header']+r['in_footer']+r['in_body']==0])
print('body-inbound only from <=1 page:',[r['page'] for r in rows if r['in_header']==0 and r['in_footer']==0 and len({a for a,b,reg,_ in edges if b==r['page'] and a!=r['page']})<=1])
print('unmapped:',[p for p in pages if p not in MAP])
