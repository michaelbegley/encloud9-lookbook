"""Build the encloud9.com block theme, its parts and the page import file from the Look 9 mock site.

Usage (from the repo root):  python3 -I wp-theme-fable/build.py
Reads   site/ (the 106 approved pages), pages/nine*.css, pages/nine.js, assets/
Writes  wp-theme-fable/encloud9-nine/   parts, page styles, page scripts, assets, inc/manifest.php
        wp-theme-fable/content/pages.json   what `wp n9 import` loads

Agent 6 run 1, 13 Nov 2026. How a page is stored:
  encloud9/box      an element that only holds other blocks (the page wrap, the article frame)
  encloud9/section  one section of the page: the mock's own markup, kept exactly; in the editor its
                    words, links and images are edited in place and its structure cannot change
  core paragraph, heading and list blocks for the running text of blog posts, so writers can add,
  remove and reorder paragraphs freely
No word of the mock is changed. Links are moved to the approved addresses (address-moves.json).
"""
import os, re, json, shutil, posixpath, html, hashlib, collections, sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SITE = os.path.join(ROOT, 'site')
THEME = os.path.join(HERE, 'encloud9-nine')
CONTENT = os.path.join(HERE, 'content')
TURI = '/wp-content/themes/encloud9-nine/assets/'
MOVE = json.load(open(os.path.join(HERE, 'address-moves.json')))
NAVKEY = {'Dynamics 365': 'd365', 'Marketing': 'marketing', 'Copilot and AI': 'copilot', 'Packages': 'packages',
          'Stories': 'stories', 'Blog': 'blog', 'About': 'about'}
NOINDEX = ['/thank-you/', '/thank-you-contact/', '/request-received/', '/newsletter-signup-successful/', '/call-prep/', '/404/']
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
INLINE = {'a', 'strong', 'em', 'b', 'i', 'span', 'br', 'code', 'sub', 'sup', 'small', 'abbr', 'mark', 'u', 's', 'kbd', 'q', 'cite'}


# ---------------------------------------------------------------- addresses
def new(p):
    base, frag = (p.split('#', 1) + [''])[:2]
    base = MOVE.get(base, base)
    return base + ('#' + frag if frag else '')


def fix_urls(s, page):
    """Asset paths point into the theme; page links become root-relative at their approved new address."""
    s = re.sub(r'(?:\./)?((?:\.\./)+)assets/([^"\'\s)]+)', lambda m: TURI + m.group(2), s)
    s = re.sub(r'(?:\./)?((?:\.\./)+)pages/([^"\'\s)]+)', lambda m: TURI + 'pages/' + m.group(2), s)

    def link(m):
        q, h = m.group(1), m.group(2)
        if re.match(r'^(https?:|mailto:|tel:|#|/wp-content/|data:|javascript:)', h):
            return m.group(0)
        if h.startswith('/'):
            t = h
        else:
            t = posixpath.normpath(posixpath.join(page, h))
            if not t.endswith('/') and '.' not in t.rsplit('/', 1)[-1] and '#' not in h:
                t += '/'
            if h.endswith('/') and not t.endswith('/'):
                t += '/'
            if '#' in h:
                b, f = h.split('#', 1)
                t = posixpath.normpath(posixpath.join(page, b or '.')) + '/' if b else page
                t = t.replace('//', '/') + '#' + f
        return f'href={q}{new(t)}{q}'
    return re.sub(r'href=(["\'])([^"\']*)\1', link, s)


# ---------------------------------------------------------------- a small tree with source offsets
class Node:
    __slots__ = ('tag', 'attrs', 's', 'se', 'es', 'e', 'kids', 'parent', 'raw')

    def __init__(self, tag, attrs, s, se, parent):
        self.tag, self.attrs, self.s, self.se, self.parent = tag, attrs, s, se, parent
        self.es = self.e = se
        self.kids = []

    def get(self, k, d=''):
        for a, v in self.attrs:
            if a == k:
                return v if v is not None else ''
        return d

    def classes(self):
        return self.get('class').split()

    def walk(self):
        for k in self.kids:
            yield k
            yield from k.walk()


class Tree(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.lines = [0]
        for m in re.finditer('\n', src):
            self.lines.append(m.end())
        self.root = Node('#root', [], 0, 0, None)
        self.cur = self.root
        self.comments = []
        self.feed(src)
        self.close()
        self.root.e = self.root.es = len(src)

    def off(self):
        l, c = self.getpos()
        return self.lines[l - 1] + c

    def handle_starttag(self, tag, attrs):
        o = self.off()
        n = Node(tag, attrs, o, o + len(self.get_starttag_text()), self.cur)
        self.cur.kids.append(n)
        if tag in VOID:
            n.es = n.e = n.se
        else:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        o = self.off()
        n = Node(tag, attrs, o, o + len(self.get_starttag_text()), self.cur)
        n.es = n.e = n.se
        self.cur.kids.append(n)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        o = self.off()
        if self.cur.tag != tag:
            raise ValueError(f'mismatched </{tag}> at {o}, open <{self.cur.tag}>')
        self.cur.es = o
        self.cur.e = self.src.index('>', o) + 1
        self.cur = self.cur.parent

    def handle_comment(self, data):
        o = self.off()
        self.comments.append((o, o + len(data) + 7))


def find(node, pred):
    for n in node.walk():
        if pred(n):
            return n
    return None


# ---------------------------------------------------------------- block markup
def jattrs(d):
    """Block comment attributes, escaped the way WordPress serialises them."""
    if not d:
        return ''
    s = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
    s = s.replace('--', '\\u002d\\u002d').replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    s = re.sub(r'\\\\"', '\\\\u0022', s)
    return ' ' + s


def blk(name, attrs, inner):
    return f'<!-- wp:{name}{jattrs(attrs)} -->\n{inner}\n<!-- /wp:{name} -->'


class Page:
    def __init__(self, path, src):
        self.path, self.src = path, src
        self.t = Tree(src)
        self.cuts = []       # spans removed from the page body (footer, scripts, comments)
        self.scripts = []    # scripts lifted out of the body
        self.stats = collections.Counter()

    def text(self, a, b):
        """Source between a and b without the cut spans."""
        out, pos = [], a
        for s, e in sorted(self.cuts):
            if e <= a or s >= b:
                continue
            out.append(self.src[pos:max(s, pos)])
            pos = max(pos, e)
        out.append(self.src[pos:b])
        return ''.join(out)

    def outer(self, n):
        return fix_urls(self.text(n.s, n.e), self.path).strip()

    def inner(self, n):
        return fix_urls(self.text(n.se, n.es), self.path).strip()

    def gap_ok(self, n):
        """Only white space (or cut spans) sits between the element children of n."""
        pos = n.se
        for k in n.kids:
            if self.text(pos, k.s).strip():
                return False
            pos = k.e
        return not self.text(pos, n.es).strip()

    # -- running text as core blocks
    def inline_only(self, n):
        for k in n.walk():
            if k.tag not in INLINE:
                return False
            if k.tag != 'br' and not re.sub(r'<[^>]*>', '', self.src[k.se:k.es]).strip():
                return False   # an empty inline element cannot live in rich text
        return True

    def prose_block(self, n):
        names = {a for a, _ in n.attrs}
        cls = n.get('class')
        if n.tag == 'p' and names <= {'class'} and self.inline_only(n) and self.inner(n):
            self.stats['core'] += 1
            return blk('paragraph', {'className': cls} if cls else {}, f'<p{" class=%s" % json.dumps(cls) if cls else ""}>{self.inner(n)}</p>')
        if n.tag in ('h2', 'h3', 'h4') and names <= {'class', 'id'} and self.inline_only(n):
            a = {}
            if n.tag != 'h2':
                a['level'] = int(n.tag[1])
            if cls:
                a['className'] = cls
            idp = f' id="{n.get("id")}"' if n.get('id') else ''
            self.stats['core'] += 1
            return blk('heading', a, f'<{n.tag} class="wp-block-heading{" " + cls if cls else ""}"{idp}>{self.inner(n)}</{n.tag}>')
        if n.tag in ('ul', 'ol') and names <= {'class'} and n.kids and self.gap_ok(n) \
                and all(k.tag == 'li' and not k.attrs and self.inline_only(k) for k in n.kids):
            a = {}
            if n.tag == 'ol':
                a['ordered'] = True
            if cls:
                a['className'] = cls
            items = '\n\n'.join(blk('list-item', {}, f'<li>{self.inner(k)}</li>') for k in n.kids)
            self.stats['core'] += 1
            return blk('list', a, f'<{n.tag} class="wp-block-list{" " + cls if cls else ""}">{items}</{n.tag}>')
        return None

    # -- containers and sections
    def is_box(self, n, depth):
        c = n.classes()
        if not self.gap_ok(n) or not n.kids:
            return False
        if depth == 0 and n.tag == 'div' and c == ['wrap']:
            return 'wrap'
        if n.tag == 'article' and find(n, lambda k: k.tag == 'div' and 'art' in k.classes()):
            return 'frame'
        if n.tag == 'div' and c == ['pgrid'] and find(n, lambda k: k.tag == 'div' and 'art' in k.classes()):
            return 'frame'
        if n.tag == 'div' and 'art' in c and n.parent and 'pgrid' in n.parent.classes():
            return 'prose'
        return False

    def block(self, n, depth, prose=False):
        kind = self.is_box(n, depth)
        if kind:
            attrs = collections.OrderedDict((k, fix_urls(v or '', self.path) if k == 'href' else (v or '')) for k, v in n.attrs)
            a = {'tag': n.tag, 'attrs': attrs}
            if kind == 'prose':
                a['prose'] = True
            elif depth == 0:
                a['lock'] = {'move': True, 'remove': True}
            kids = '\n\n'.join(self.block(k, depth + 1, kind == 'prose') for k in n.kids if not self.cut(k))
            open_tag = '<' + n.tag + ''.join(f' {k}="{html.escape(v, quote=True)}"' for k, v in attrs.items()) + '>'
            self.stats['box'] += 1
            return blk('encloud9/box', a, f'{open_tag}{kids}</{n.tag}>')
        if prose:
            b = self.prose_block(n)
            if b:
                return b
        self.stats['section'] += 1
        a = {'lock': {'move': True, 'remove': True}} if depth == 0 else {}
        return blk('encloud9/section', a, self.outer(n))

    def cut(self, n):
        return any(s <= n.s and n.e <= e for s, e in self.cuts)


def split_page(path, src):
    p = Page(path, src)
    main = find(p.t.root, lambda n: n.tag == 'main')
    if not main or not p.gap_ok(main):
        raise ValueError('main is missing or holds loose text: ' + path)
    for n in main.walk():
        if n.tag == 'script':
            p.cuts.append((n.s, n.e))
            p.scripts.append(src[n.se:n.es])
        if n.tag == 'footer' and 'foot' in n.classes():
            p.cuts.append((n.s, n.e))
        if n.tag == 'div' and n.classes() == ['scale'] and n.parent and 'final' in n.parent.classes():
            p.cuts.append((n.s, n.e))
    for s, e in p.t.comments:           # builder notes in comments stay out of the live site
        if main.se <= s and e <= main.es:
            p.cuts.append((s, e))
    blocks = [p.block(k, 0) for k in main.kids if not p.cut(k)]
    return p, main, '\n\n'.join(blocks)


# ---------------------------------------------------------------- run
def pages():
    for d, _, fs in os.walk(SITE):
        if 'index.html' in fs:
            rel = '/' + os.path.relpath(d, SITE).replace(os.sep, '/') + '/'
            yield ('/' if rel == '/./' else rel), os.path.join(d, 'index.html')


def hnorm(x):
    x = re.sub(r'<span style="white-space:nowrap">([^<]*)</span>', r'\1', x)
    x = re.sub(r' class="cur"|<span class="sr-only"> \(current section\)</span>| aria-current="[^"]*"', '', x)
    return re.sub(r'\s+', ' ', re.sub(r'(href|src)="[^"]*"', '', x))


def part(markup):
    return blk('encloud9/section', {}, markup.strip()) + '\n'


def main():
    home = open(os.path.join(SITE, 'index.html'), encoding='utf-8').read()
    base_hdr = re.search(r'<header class="top">.*?</header>', home, re.S).group(0)
    base_ftr = re.search(r'<footer class="foot">.*?</footer>', home, re.S).group(0)
    scale = re.search(r'<div class="scale" aria-hidden="true">.*?</div>', home, re.S).group(0)

    css_sets, js_sets, items, totals = {}, {}, [], collections.Counter()
    ftr_variants = collections.Counter()
    for path, f in sorted(pages()):
        h = open(f, encoding='utf-8').read()
        head = h[:h.find('<body')]
        g = lambda r: (re.search(r, head, re.S) or [None, ''])[1]
        title = html.unescape(g(r'<title>(.*?)</title>'))
        desc = html.unescape(g(r'<meta name="description" content="(.*?)">'))
        css = fix_urls('\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', head, re.S)), path).strip()
        ld = [fix_urls(x, path) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', head, re.S)]
        bodyclass = (re.search(r'<body class="([^"]*)"', h) or [None, ''])[1]
        cur = re.search(r'<nav class="nav".*?<a href="[^"]*" class="cur">([^<]+)<', h, re.S)
        section = NAVKEY.get(cur.group(1).strip(), '') if cur else ''
        myhdr = re.search(r'<header class="top">.*?</header>', h, re.S).group(0)
        minimal = hnorm(myhdr) != hnorm(base_hdr)
        if minimal:
            open(os.path.join(THEME, 'parts', 'header-minimal.html'), 'w').write(part(fix_urls(myhdr, '/')))
        myftr = re.search(r'<footer class="foot">.*?</footer>', h, re.S)
        ftr_variants[hnorm(myftr.group(0)) == hnorm(base_ftr) if myftr else None] += 1

        p, mainnode, content = split_page(path, h)
        totals.update(p.stats)
        bo = h.find('>', h.find('<body')) + 1
        before = h[bo:h.find('<header class="top">')].strip()
        if before not in ('', '<div class="progress" aria-hidden="true"><i></i></div>'):
            raise ValueError('unexpected markup before the header: ' + path)
        after = h[mainnode.e:h.find('</body>')]
        js = '\n'.join(s.strip() for s in p.scripts + re.findall(r'<script>(.*?)</script>', after, re.S)).strip()
        if re.sub(r'<script>.*?</script>', '', after, flags=re.S).strip():
            raise ValueError('unexpected markup after main: ' + path)

        def keep(store, text, ext):
            if not text:
                return ''
            name = (bodyclass.split() or ['page'])[0] + '-' + hashlib.md5(text.encode()).hexdigest()[:8]
            store[name] = text
            return name
        np_ = new(path)
        kind = 'post' if re.match(r'^/blog/[^/]+/$', np_) else ('story' if np_.startswith('/stories/') else 'page')
        items.append(dict(
            old=path, path=np_, type=kind, slug=np_.strip('/').split('/')[-1] if np_ != '/' else '',
            title=title, description=desc, bodyclass=bodyclass, section=section, jsonld=ld,
            style=keep(css_sets, css, 'css'), script=keep(js_sets, js, 'js'), progress=bool(before),
            template='page-minimal' if minimal else '', noindex=np_ in NOINDEX, content=content))

    os.makedirs(CONTENT, exist_ok=True)
    json.dump(items, open(os.path.join(CONTENT, 'pages.json'), 'w'), indent=1, ensure_ascii=False)

    # page styles and scripts: one theme file per distinct set, printed inline where the mock had them
    for sub, store, ext in (('css/page', css_sets, 'css'), ('js/page', js_sets, 'js')):
        d = os.path.join(THEME, 'assets', sub)
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d)
        for name, text in store.items():
            open(os.path.join(d, f'{name}.{ext}'), 'w').write(text + '\n')

    # the shared sheet and script, from the mock's own files
    A = os.path.join(THEME, 'assets')
    os.makedirs(os.path.join(A, 'css'), exist_ok=True)
    os.makedirs(os.path.join(A, 'js'), exist_ok=True)
    nine = open(os.path.join(ROOT, 'pages', 'nine.css')).read()
    nine = fix_urls(nine.replace('url(../assets/', 'url(../../assets/'), '/')   # same rewrite path as page markup
    nine = nine.replace(TURI, '../')                                             # relative to assets/css/
    open(os.path.join(A, 'css', 'nine.css'), 'w').write(nine)
    shutil.copy(os.path.join(ROOT, 'pages', 'nine-scale.css'), os.path.join(A, 'css', 'nine-scale.css'))
    js = open(os.path.join(ROOT, 'pages', 'nine.js')).read()
    a, b = js.index("  /* font switcher (lookbook review only) */"), js.index("  d.addEventListener('click',function(e){")
    js = js[:a] + js[b:]                                                         # the lookbook's font switcher does not ship
    old = "    var b=e.target.closest('[data-setfont]');\n    if(b){setFont(b.getAttribute('data-setfont'));return}\n"
    assert old in js
    js = js.replace(old, '')
    assert 'setFont' not in js and 'n9font' not in js
    open(os.path.join(A, 'js', 'nine.js'), 'w').write(js)

    # only the files the pages use
    used = set(re.findall(re.escape(TURI) + r'([^"\'\s)]+)', ''.join(i['content'] for i in items) + fix_urls(base_hdr + base_ftr, '/')))
    used |= {'photos/' + m for m in re.findall(r'assets/photos/([^)"\']+)', nine)} | {'brand/share-card.png'}
    for rel in sorted(used):
        src = os.path.join(ROOT, 'assets', rel)
        if os.path.isfile(src):
            os.makedirs(os.path.dirname(os.path.join(A, rel)), exist_ok=True)
            shutil.copy(src, os.path.join(A, rel))
        else:
            print('MISSING ASSET', rel)
    os.makedirs(os.path.join(A, 'fonts'), exist_ok=True)
    for fn in os.listdir(os.path.join(ROOT, 'assets', 'fonts')):
        if fn.startswith('hanken-grotesk') and fn.endswith('.woff2'):
            shutil.copy(os.path.join(ROOT, 'assets', 'fonts', fn), os.path.join(A, 'fonts', fn))

    # header and footer template parts: the mock's markup, as blocks an admin can edit in the Site Editor
    hdr = fix_urls(base_hdr, '/')
    hdr = re.sub(r' class="cur"', '', hdr)
    hdr = re.sub(r'<span class="sr-only"> \(current section\)</span>', '', hdr)
    open(os.path.join(THEME, 'parts', 'header.html'), 'w').write(part(hdr))
    ftr = '<div class="site-foot"><div class="wrap">' + fix_urls(base_ftr, '/') + '</div>' + scale + '</div>'
    open(os.path.join(THEME, 'parts', 'footer.html'), 'w').write(part(ftr))

    # what PHP needs to know: which style and script a new post or story gets by default
    def common(kind, key):
        c = collections.Counter(i[key] for i in items if i['type'] == kind and i[key])
        return c.most_common(1)[0][0] if c else ''
    man = {'style': {k: common(k, 'style') for k in ('post', 'story')}, 'script': {k: common(k, 'script') for k in ('post', 'story')},
           'bodyclass': {'post': 'p-post', 'story': 'p-story'}}
    os.makedirs(os.path.join(THEME, 'inc'), exist_ok=True)
    open(os.path.join(THEME, 'inc', 'manifest.json'), 'w').write(json.dumps(man, indent=1))

    print(len(items), 'pages', dict(collections.Counter(i['type'] for i in items)))
    print('blocks', dict(totals), '| style sets', len(css_sets), '| script sets', len(js_sets), '| footer same as home', dict(ftr_variants))


if __name__ == '__main__':
    main()
