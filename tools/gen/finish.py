"""After generating pages: apply shared chrome (file:section pairs as args) and relink every live encloud9.com URL that has a built concept page."""
import sys, re, glob, subprocess, ast
L = '/home/claude/lb/'
for a in sys.argv[1:]:
    f, sec = a.split(':'); subprocess.run(['python3', '/home/claude/lb/tools/n9kit/chrome.py', L + 'pages/' + f, sec], check=True, stdout=subprocess.DEVNULL)
src = open(L + 'tools/build_site.py').read()
MAP = dict(re.findall(r"'(nine-[\w-]+\.html)':\s*'([^']+)'", src))
rel = {}
for k, v in MAP.items():
    if v == '/': continue
    rel['https://www.encloud9.com' + v] = k
    rel['https://www.encloud9.com' + v.rstrip('/')] = k
ALIAS = {'/microsoft-dynamics-365-vs-salesforce/': 'nine-vs-crm.html', '/encloud9-dynamics-365-crm-services/microsoft-dynamics-365-support-services/': 'nine-support.html'}  # old live paths that redirect
for a, f in ALIAS.items(): rel['https://www.encloud9.com' + a] = f
n = 0
for f in glob.glob(L + 'pages/nine-*.html'):
    # links only: the canonical <link rel="canonical" href=...> must keep the live address (fixed 10 Nov 2026)
    t = open(f).read(); u = re.sub(r'(?<!rel="canonical" )href="(https://www\.encloud9\.com/[^"#]*)(#[^"]*)?"', lambda m: f'href="{rel[m.group(1)]}{m.group(2) or ""}"' if m.group(1) in rel else m.group(0), t)
    if u != t: open(f, 'w').write(u); n += 1
c = '/home/claude/lb/tools/n9kit/chrome.py'; t = open(c).read()
u = re.sub(r'href="(https://www\.encloud9\.com/[^"#]*)"', lambda m: f'href="{rel[m.group(1)]}"' if m.group(1) in rel else m.group(0), t)
if u != t: open(c, 'w').write(u)
print('finish: chrome', len(sys.argv) - 1, 'relinked', n, 'map', len(MAP))
