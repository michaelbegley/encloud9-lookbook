"""Tables on every concept page (standard G15 and area 6, added 9 Nov 2026).

For each <table> with a <thead>:
- adds the tbl-stack class, so on phones each row becomes short labelled lines instead of scrolling sideways;
- gives every body cell a data-l label taken from its column heading (cells that already have one keep it);
- gives the scrolling wrapper a unique aria-label taken from the table's caption or the nearest heading above it,
  replacing the generic "Table, scrolls sideways on small screens" (axe landmark-unique).
Safe to run again. build_site.py runs it before building.
"""
import os, re, html as H
from build_site import MAP, PAGES

GENERIC = 'Table, scrolls sideways on small screens'

def text(s):
    return H.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))).strip()

def label_cells(tbody, heads):
    def row(m):
        i = 0
        def cell(c):
            nonlocal i
            tag, attrs = c.group(1), c.group(2) or ''
            lab = heads[i] if i < len(heads) else ''
            i += 1
            span = re.search(r'colspan="(\d+)"', attrs)
            if span:
                i += int(span.group(1)) - 1
            if 'data-l=' in attrs or not lab:
                return c.group(0)
            return f'<{tag}{attrs} data-l="{H.escape(lab, quote=True)}">'
        return re.sub(r'<(td|th)(\s[^>]*)?>', cell, m.group(0))
    return re.sub(r'<tr\b.*?</tr>', row, tbody, flags=re.S)

def fix(s):
    out, pos, used = [], 0, {}
    for m in re.finditer(r'<table\b([^>]*)>(.*?)</table>', s, re.S):
        attrs, inner = m.group(1), m.group(2)
        th = re.search(r'<thead>(.*?)</thead>', inner, re.S)
        tb = re.search(r'<tbody>(.*?)</tbody>', inner, re.S)
        new = m.group(0)
        if th and tb:
            # column labels without badges such as <span class="tag">Most B2B teams start here</span>
            heads = [text(re.sub(r'<span class="tag">.*?</span>', '', h, flags=re.S)) for h in re.findall(r'<th[^>]*>(.*?)</th>', th.group(1), re.S)]
            inner2 = inner.replace(tb.group(1), label_cells(tb.group(1), heads))
            if 'class="' in attrs:
                attrs2 = attrs if 'tbl-stack' in attrs else re.sub(r'class="([^"]*)"', r'class="\1 tbl-stack"', attrs, 1)
            else:
                attrs2 = attrs + ' class="tbl-stack"'
            new = f'<table{attrs2}>{inner2}</table>'
        out.append(s[pos:m.start()]); out.append(new); pos = m.end()
    out.append(s[pos:])
    s = ''.join(out)
    # unique labels for the scroll wrappers
    def lab(m):
        before = s[:m.start()]
        after = s[m.end():m.end() + 4000]
        cap = re.search(r'<caption[^>]*>(.*?)</caption>', after, re.S)
        name = text(cap.group(1)) if cap and after.find('<caption') < after.find('</table>') else ''
        if not name:
            hs = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', before, re.S)
            name = text(hs[-1]) if hs else 'Table'
        name = re.sub(r',?\s*(checked\s*)?\[[^\]]*\]', '', name).strip(' ,')[:80]
        used[name] = used.get(name, 0) + 1
        if used[name] > 1:
            name = f'{name} ({used[name]})'
        return f'aria-label="Table: {H.escape(name, quote=True)}"'
    s = re.sub(r'aria-label="' + re.escape(GENERIC) + '"', lab, s)
    return s

def apply():
    n = 0
    for src in MAP:
        fp = os.path.join(PAGES, src)
        s = open(fp, encoding='utf-8').read()
        s2 = fix(s)
        if s2 != s:
            open(fp, 'w', encoding='utf-8').write(s2); n += 1
    return n

if __name__ == '__main__':
    print('tables: updated', apply(), 'pages')
