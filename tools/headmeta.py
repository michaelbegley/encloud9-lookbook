"""Share and find tags for every concept page (standard gate G11, added 9 Nov 2026).

Writes one block between <!--headmeta--> and <!--/headmeta--> right after the meta description:
canonical (the page's real encloud9.com address from build_site.MAP), Open Graph and Twitter card tags
built from the page's own title and description, and the share card image.
The 404 page gets none (it has no address of its own). Safe to run again: the block is replaced.
build_site.py runs this first, so the tags survive page regenerations.
"""
import os, re, html as H
from build_site import MAP, PAGES, LIVE

# The share card is served from the design site until launch; the WordPress theme swaps this for the live path.
SHARE_IMG = 'https://michaelbegley.github.io/encloud9-lookbook/assets/brand/share-card.png'
SKIP = {'nine-404.html'}

def block(path, title, desc):
    url = LIVE + path
    t, d = H.escape(title, quote=True), H.escape(desc, quote=True)
    return ('<!--headmeta-->\n'
            f'<link rel="canonical" href="{url}">\n'
            '<meta property="og:site_name" content="enCloud9">\n'
            f'<meta property="og:type" content="{"article" if "/blog/" in path else "website"}">\n'
            f'<meta property="og:title" content="{t}">\n'
            f'<meta property="og:description" content="{d}">\n'
            f'<meta property="og:url" content="{url}">\n'
            f'<meta property="og:image" content="{SHARE_IMG}">\n'
            '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
            '<meta property="og:image:alt" content="enCloud9, Microsoft Dynamics 365 partner in Bellevue, Nebraska">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<!--/headmeta-->\n')

SCALE = '<link rel="stylesheet" href="nine-scale.css">'

def apply():
    n = 0
    for src, path in MAP.items():
        fp = os.path.join(PAGES, src)
        s = open(fp, encoding='utf-8').read()
        # one gap and one type scale (nine-scale.css) load last, after the page's own styles
        if SCALE not in s:
            s0 = s
            s = s.replace('</head>', SCALE + '\n</head>', 1)
            open(fp, 'w', encoding='utf-8').write(s)
            n += 1
        if src in SKIP:
            continue
        title = H.unescape((re.search(r'<title>(.*?)</title>', s, re.S) or [None, ''])[1].strip())
        m = re.search(r'<meta name="description" content="([^"]*)">\n?', s)
        desc = H.unescape(m.group(1)) if m else ''
        s2 = re.sub(r'<!--headmeta-->.*?<!--/headmeta-->\n?', '', s, flags=re.S)
        b = block(path, title, desc)
        if m:
            i = s2.find(m.group(0)) + len(m.group(0))
            if not m.group(0).endswith('\n'):
                b = '\n' + b
        else:
            i = s2.find('</title>') + len('</title>\n')
        s2 = s2[:i] + b + s2[i:]
        if s2 != s:
            open(fp, 'w', encoding='utf-8').write(s2)
            n += 1
    return n

if __name__ == '__main__':
    print('headmeta: updated', apply(), 'pages')
