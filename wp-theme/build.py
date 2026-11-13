"""Build the WordPress block theme and the page import file from the Look 9 mock site.

Usage: python3 -I wp-theme/build.py   (run from the repo root)
Writes wp-theme/encloud9-nine/ (the theme) and wp-theme/content/pages.json (what import.php loads).
Draft 1, 13 Nov 2026. Page bodies go in as Custom HTML blocks for an exact match first;
section types become editable patterns in later passes (WP-THEME-FROM-LOOK9.md, approach C).
"""
import os, re, json, shutil, posixpath, csv, sys, html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE=os.path.join(ROOT,'site'); OUT=os.path.join(ROOT,'wp-theme','encloud9-nine'); CONTENT=os.path.join(ROOT,'wp-theme','content')
TURI='/wp-content/themes/encloud9-nine/assets/'
# new addresses (ADDRESS-SCHEME-Draft1, approved 13 Nov 2026)
MOVE=json.load(open(os.path.join(ROOT,'wp-theme','address-moves.json')))
NAVKEY={'Dynamics 365':'d365','Marketing':'marketing','Copilot and AI':'copilot','Packages':'packages','Stories':'stories','Blog':'blog','About':'about'}

def pages():
    for d,_,fs in os.walk(SITE):
        if 'index.html' in fs:
            rel='/'+os.path.relpath(d,SITE).replace(os.sep,'/')+'/'
            yield ('/' if rel=='/./' else rel), os.path.join(d,'index.html')

def new(p):
    base,frag=(p.split('#',1)+[''])[:2]
    base=MOVE.get(base,base)
    return base+('#'+frag if frag else '')

def fix_urls(s,page):
    def asset(m): return TURI+m.group(2)
    s=re.sub(r'(?:\./)?((?:\.\./)+)assets/([^"\'\s)]+)',lambda m:TURI+m.group(2),s)
    s=re.sub(r'(?:\./)?((?:\.\./)+)pages/([^"\'\s)]+)',lambda m:TURI+'pages/'+m.group(2),s)
    def link(m):
        q,h=m.group(1),m.group(2)
        if re.match(r'^(https?:|mailto:|tel:|#|/wp-content/|data:|javascript:)',h): return m.group(0)
        if h.startswith('/'): t=h
        else:
            t=posixpath.normpath(posixpath.join(page,h))
            if not t.endswith('/') and '.' not in t.rsplit('/',1)[-1] and '#' not in h: t+='/'
            if h.endswith('/') and not t.endswith('/'): t+='/'
            if '#' in h:
                b,f=h.split('#',1); t=posixpath.normpath(posixpath.join(page,b or '.'))+'/' if b else page; t=t.replace('//','/')+'#'+f
        return f'href={q}{new(t)}{q}'
    s=re.sub(r'href=(["\'])([^"\']*)\1',link,s)
    return s

def block(html_):
    return '<!-- wp:html -->\n'+html_.strip()+'\n<!-- /wp:html -->'

def split_sections(main):
    # one Custom HTML block per top-level child of <main>, so later passes can swap them for patterns one by one
    parts=re.split(r'(?=\n<(?:section|div|article|aside|nav)\b)',main)
    return [p for p in parts if p.strip()]

def hnorm(x):
    x=re.sub(r'<span style="white-space:nowrap">([^<]*)</span>',r'\1',x)
    x=re.sub(r' class="cur"|<span class="sr-only"> \(current section\)</span>| aria-current="[^"]*"','',x)
    return re.sub(r'\s+',' ',re.sub(r'(href|src)="[^"]*"','',x))
BASEHDR=hnorm(re.search(r'<header class="top">.*?</header>',open(os.path.join(SITE,'index.html'),encoding='utf-8').read(),re.S).group(0))
items=[]; problems=[]
for path,f in sorted(pages()):
    h=open(f,encoding='utf-8').read()
    head=h[:h.find('<body')]
    g=lambda r:(re.search(r,head,re.S) or [None,''])[1]
    title=html.unescape(g(r'<title>(.*?)</title>'))
    desc=html.unescape(g(r'<meta name="description" content="(.*?)">'))
    robots=g(r'<meta name="robots" content="(.*?)">')
    css='\n'.join(re.findall(r'<style[^>]*>(.*?)</style>',head,re.S))
    ld=re.findall(r'<script type="application/ld\+json">(.*?)</script>',head,re.S)
    bodyclass=(re.search(r'<body class="([^"]*)"',h) or [None,''])[1]
    cur=re.search(r'<nav class="nav".*?<a href="[^"]*" class="cur">([^<]+)<',h,re.S)
    section=NAVKEY.get(cur.group(1).strip(),'') if cur else ''
    myhdr=re.search(r'<header class="top">.*?</header>',h,re.S).group(0)
    own_header=fix_urls(myhdr,path) if hnorm(myhdr)!=BASEHDR else ''
    m=re.search(r'<main id="main">(.*)</main>',h,re.S)
    if not m: problems.append((path,'no main')); continue
    main=m.group(1)
    after=h[m.end():h.find('</body>')]
    bo=h.find('>',h.find('<body'))+1
    before=h[bo:h.find('<header class="top">')].strip()
    js='\n'.join(re.findall(r'<script>(.*?)</script>',after,re.S))
    main=re.sub(r'<footer class="foot">.*?</footer>','',main,flags=re.S)
    main=re.sub(r'<div class="scale" aria-hidden="true">.*?</div>','',main,flags=re.S)
    main=fix_urls(main,path)
    ld=[fix_urls(x,path) for x in ld]; css=fix_urls(css,path)
    np_=new(path)
    kind='post' if re.match(r'^/blog/[^/]+/$',np_) and np_!='/blog/' else ('story' if np_.startswith('/stories/') else 'page')
    items.append(dict(old=path,path=np_,type=kind,slug=np_.strip('/').split('/')[-1] if np_!='/' else '',
        title=title,description=desc,css=css,js=js,before=before,header=own_header,robots=robots,bodyclass=bodyclass,section=section,jsonld=ld,
        content='\n\n'.join(block(p) for p in split_sections(main))))
os.makedirs(CONTENT,exist_ok=True)
json.dump(items,open(os.path.join(CONTENT,'pages.json'),'w'),indent=1,ensure_ascii=False)
# copy assets the pages use
A=os.path.join(OUT,'assets'); 
for sub in ('brand','icons','photos','thumbs'):
    src=os.path.join(ROOT,'assets',sub)
    if os.path.isdir(src): shutil.copytree(src,os.path.join(A,sub),dirs_exist_ok=True)
os.makedirs(os.path.join(A,'fonts'),exist_ok=True)
for fn in os.listdir(os.path.join(ROOT,'assets','fonts')):
    if fn.startswith('hanken-grotesk'): shutil.copy(os.path.join(ROOT,'assets','fonts',fn),os.path.join(A,'fonts',fn))
os.makedirs(os.path.join(A,'pages'),exist_ok=True)
for fn in os.listdir(os.path.join(ROOT,'pages')):
    if fn.endswith(('.css','.js','.png','.jpg','.webp','.svg')) and not fn.startswith('f'):
        shutil.copy(os.path.join(ROOT,'pages',fn),os.path.join(A,'pages',fn))
c=__import__('collections').Counter(i['type'] for i in items)
print(len(items),'pages',dict(c),'problems',problems)

# header and footer markup, taken from the mock home page so they stay in step with tools/n9kit/chrome.py
h=open(os.path.join(SITE,'index.html'),encoding='utf-8').read()
hdr=re.search(r'<header class="top">.*?</header>',h,re.S).group(0)
ftr=re.search(r'<footer class="foot">.*?</footer>',h,re.S).group(0)
scl=re.search(r'<div class="scale" aria-hidden="true">.*?</div>',h,re.S).group(0)
hdr=fix_urls(hdr,'/'); ftr=fix_urls(ftr,'/')
hdr=re.sub(r' class="cur"','',hdr); hdr=re.sub(r'<span class="sr-only"> \(current section\)</span>','',hdr)
inc=os.path.join(OUT,'inc'); os.makedirs(inc,exist_ok=True)
open(os.path.join(inc,'header.html'),'w').write(hdr)
open(os.path.join(inc,'footer.html'),'w').write(ftr+'\n'+scl)
print('header',len(hdr),'footer',len(ftr))
