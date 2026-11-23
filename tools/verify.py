#!/usr/bin/env python3
"""encloud9-verify, local half (16 Nov 2026). Run before every plugin zip and every commit that touches the site.

Usage: python3 -I tools/verify.py [--since REF] [--launch]     (REF defaults to the last commit stamped "Verified: live")

Always runs (cheap, seconds):
  1. build.py runs clean and the plugin's data/pages.json equals content/pages.json (the copy step is easy to forget).
  2. php -l on every plugin .php file; the header Version and N9_SITE_VER agree.
  3. Every page: one H1, no em or en dash, no visible [placeholder], title and description present,
     JSON-LD parses, phone written as 1-844-264-0729 only.
  4. Every internal link in a page body resolves to a built page, a kept old post, or a 301 source.
  5. Redirects: each 301 target is a live page (built or kept post), no target is itself a redirect source
     (no chains), none points at the home page, no source is also a live page, 301 and 410 lists do not overlap.
  6. Thank-you and confirmation pages are noindex.
Then prints the trigger checklist items (tools/verify-checklist.tsv) whose triggers match the files changed
since REF, so the live half knows which checks to run. Exit 1 on any failure.
"""
import csv, glob, html, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WP = os.path.join(ROOT, 'wp-theme-fable')
PLUGIN = os.path.join(WP, 'encloud9-site')
PHONE_OK = '1-844-264-0729'
fails, warns = [], []
LAUNCH = '--launch' in sys.argv  # launch mode: every open [placeholder] fails
HOME_ALIASES = {'/home/', '/index.php'}  # old home addresses may 301 to /


def fail(area, msg): fails.append(f'{area}: {msg}')
def warn(area, msg): warns.append(f'{area}: {msg}')


def run(cmd, cwd=ROOT):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


# 1. build and copy
rc, out = run([sys.executable, '-I', 'build.py'], cwd=WP)
if rc: fail('build', out[-400:])
built = open(os.path.join(WP, 'content/pages.json'), 'rb').read()
shipped = open(os.path.join(PLUGIN, 'data/pages.json'), 'rb').read()
if built != shipped: fail('copy', 'encloud9-site/data/pages.json differs from content/pages.json: copy it before zipping')
pages = json.loads(shipped)  # check what actually ships in the zip
paths = {p['path'] for p in pages}

# 2. php
for f in glob.glob(os.path.join(PLUGIN, '**/*.php'), recursive=True):
    rc, out = run(['php', '-l', f])
    if rc: fail('php', f'{os.path.relpath(f, ROOT)}: {out.splitlines()[0] if out else "error"}')
main = open(os.path.join(PLUGIN, 'encloud9-site.php')).read()
v1 = re.search(r'Version:\s*([\d.]+)', main); v2 = re.search(r"N9_SITE_VER',\s*'([\d.]+)'", main)
if not v1 or not v2 or v1.group(1) != v2.group(1): fail('version', 'header Version and N9_SITE_VER disagree')
version = v1.group(1) if v1 else '?'
theme_css = open(os.path.join(WP, 'encloud9-nine', 'style.css')).read()
theme_fn = open(os.path.join(WP, 'encloud9-nine', 'functions.php')).read()
t1 = re.search(r'Version:\s*([\d.]+)', theme_css); t2 = re.search(r"N9_VER',\s*'([\d.]+)'", theme_fn)
if not t1 or not t2 or t1.group(1) != t2.group(1): fail('version', 'theme style.css Version and N9_VER disagree (browsers keep the old CSS)')

# kept old posts and redirects
kept = set()
for line in open(os.path.join(PLUGIN, 'data/kept-posts.txt')):
    line = line.strip()
    if line and not line.startswith('#'): kept.add(line.split()[0])
moves = json.load(open(os.path.join(PLUGIN, 'data/address-moves.json')))
live = paths | kept
r301 = {}
for row in csv.reader(open(os.path.join(WP, 'redirects/redirection-import-301.csv'))):
    if len(row) >= 2 and row[0].startswith('/'): r301[row[0]] = row[1]
r410 = {l.strip() for l in open(os.path.join(WP, 'redirects/redirection-410.txt')) if l.strip().startswith('/')}

# 3 and 4. pages
TAG = re.compile(r'<[^>]+>')
NOFOLLOW_PREFIX = ('/wp-', '/feed', '/blog/page/', '/category/', '/author/', '/tag/')
for p in pages:
    c = p.get('content') or ''
    where = p['path']
    if len(re.findall(r'<h1[\s>]', c)) != 1 and p['path'] != '/404/':
        warn('h1', f'{where}: {len(re.findall(r"<h1[\\s>]", c))} H1 in content (theme may add one)')
    text = html.unescape(TAG.sub(' ', re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', c)))
    vis = text + ' ' + (p.get('title') or '') + ' ' + (p.get('description') or '')
    if re.search('[–—]', vis): fail('dash', f'{where}: em or en dash in visible text')
    for b in set(re.findall(r'\[[A-Za-z][^\]\n]{2,80}\]', text)): (fail if LAUNCH else warn)('placeholder', f'{where}: {b}')
    if not (p.get('title') or '').strip(): fail('meta', f'{where}: no title')
    if not (p.get('description') or '').strip() and where != '/404/': warn('meta', f'{where}: no description')
    for blk in ([p['jsonld']] if isinstance(p.get('jsonld'), str) else (p.get('jsonld') or [])):
        if isinstance(blk, str) and blk.strip():
            try: json.loads(blk)
            except Exception as e: fail('schema', f'{where}: JSON-LD does not parse ({str(e)[:60]})')
    for ph in set(re.findall(r'\b\d[\d\s().-]{8,}\d\b', text)):
        digits = re.sub(r'\D', '', ph)
        if digits in ('18442640729', '8442640729') and ph.strip() != PHONE_OK: fail('phone', f'{where}: written "{ph.strip()}", use {PHONE_OK}')
    for href in set(re.findall(r'href="(/[^"#?]*)', c)):
        h = href if href.endswith('/') or '.' in href.rsplit('/', 1)[-1] else href + '/'
        if '.' in h.rsplit('/', 1)[-1] or h.startswith(NOFOLLOW_PREFIX): continue
        if h not in live and h not in moves and h not in r301: fail('link', f'{where} links to {h}: no page, kept post or redirect')

# 5. redirects
for src, dst in r301.items():
    d = dst if dst.startswith('/') else re.sub(r'^https?://[^/]+', '', dst)
    if d in ('/', '') and src not in HOME_ALIASES: fail('redirect', f'{src} -> home page (soft 404)')
    elif d in r301: fail('redirect', f'{src} -> {d}, which redirects again (chain)')
    elif d not in live and not d.startswith('/wp-content/'): fail('redirect', f'{src} -> {d}: target is not a built page or kept post')
    if src in paths: fail('redirect', f'{src} is a live page and also a redirect source')
for s in r410 & set(r301): fail('redirect', f'{s} is in both the 301 and the 410 lists')

# 6. noindex
for p in pages:
    if re.search(r'thank|received|successful|call-prep', p['path']) and not p.get('noindex'):
        fail('noindex', f"{p['path']} should be noindex")

# trigger checklist
since = None
if '--since' in sys.argv: since = sys.argv[sys.argv.index('--since') + 1]
else:
    rc, out = run(['git', 'log', '-1', '--format=%H', '--grep=Verified: live'])
    since = out.strip() or 'HEAD~1'
rc, out = run(['git', 'diff', '--name-only', since])
rc2, out2 = run(['git', 'ls-files', '--others', '--exclude-standard'])
changed = [l for l in (out + '\n' + out2).splitlines() if l.strip()]
due = []
cl = os.path.join(ROOT, 'tools/verify-checklist.tsv')
for row in csv.DictReader(open(cl), delimiter='\t'):
    if any(re.search(row['trigger'], f) for f in changed): due.append(row)

print(f'encloud9-verify local · plugin {version} · {len(pages)} pages · {len(kept)} kept posts · {len(r301)} redirects (301) · {len(r410)} (410)')
print(f'changed since {since[:10]}: {len(changed)} files')
print(f'FAIL {len(fails)} · WARN {len(warns)}')
for f in fails: print('  FAIL', f)
ph=[w for w in warns if w.startswith('placeholder')]
for w in [w for w in warns if not w.startswith('placeholder')][:15]: print('  warn', w)
if ph: print(f'  warn {len(ph)} open [placeholders] on {len({w.split(": ")[1] for w in ph})} pages (launch blockers; --launch lists them as failures)')
print(f'LIVE CHECKS DUE ({len(due)}):')
for r in due: print(f"  {r['id']} {r['check']}  [from: {r['origin']}]")
if not due: print('  none beyond the smoke pages')
sys.exit(1 if fails else 0)
