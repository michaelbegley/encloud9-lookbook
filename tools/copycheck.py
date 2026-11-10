#!/usr/bin/env python3
"""Copy, search-target and placeholder checks for the built concept pages (10 Nov 2026).
Usage: python3 tools/copycheck.py [--query-map PATH] [pages/nine-*.html ...]

Per page: "we/us/our" against "enCloud9" counts (Brian, call 27: say enCloud9), sentences over 25 words,
passive headline verbs, banned words; the QUERY-MAP phrase in title, H1 and opening answer; every visible
bracket placeholder. Prints a table and a site-wide placeholder list. Exit 1 if a page has no query-map row
or its phrase is missing from the title or H1.
"""
import csv, glob, html, os, re, sys

BANNED = [r"\bseamless(ly)?\b", r"\brobust\b", r"\bleverage\b", r"\bunlock\b", r"\bgame[- ]chang", r"\bcutting[- ]edge\b",
          r"\bnot a fit\b", r"\bworld[- ]class\b", r"\bbest[- ]in[- ]class\b"]
PASSIVE_H1 = [r"\bworking on\b"]  # Brian, call 27: "working" in the Copilot headline reads passive
SLUG = {}  # concept file -> live URL, read from the built site's canonical tags


def canon_map(site="site"):
    out = {}
    for f in glob.glob(os.path.join(site, "**", "index.html"), recursive=True):
        s = open(f, encoding="utf-8").read()
        m = re.search(r'<link rel="canonical" href="([^"]+)"', s)
        src = re.search(r"<!-- source: (nine-[^ ]+\.html)", s)
        if m and src:
            out[src.group(1)] = m.group(1)
    return out


def visible(s):
    body = s[s.find("<main"):s.find("</main>")] if "<main" in s else s
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", body, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "\n", body)))


def main(argv):
    qpath = "/home/claude/src/QUERY-MAP.csv"
    if "--query-map" in argv:
        i = argv.index("--query-map"); qpath = argv[i + 1]; argv = argv[:i] + argv[i + 2:]
    pages = argv or sorted(glob.glob("pages/nine-*.html"))
    qmap = {}
    if os.path.exists(qpath):
        for r in csv.DictReader(open(qpath, encoding="utf-8")):
            qmap[r["page"].rstrip("/") + "/"] = r["primary_search"].lower()
    bad = 0
    holders = []
    print(f"{'page':38} {'we':>4} {'enC9':>4} {'>25w':>4} {'banned':>6}  search target")
    for p in pages:
        name = os.path.basename(p)
        s = open(p, encoding="utf-8").read()
        t = visible(s)
        we = len(re.findall(r"\b(we|We|us|our|Our)\b", t))
        e9 = len(re.findall(r"enCloud9", t))
        sents = [x for x in re.split(r"(?<=[.!?])\s+|\n", t) if len(x.split()) > 25]
        ban = sum(len(re.findall(b, t, re.I)) for b in BANNED)
        title = (re.search(r"<title>([^<]*)", s) or [None, ""])[1].lower()
        h1 = re.sub(r"<[^>]+>", "", (re.search(r"<h1.*?</h1>", s, re.S) or [""])[0]).lower()
        lead = re.sub(r"<[^>]+>", "", (re.search(r'<p class="lead rise".*?</p>', s, re.S) or [""])[0]).lower()
        cm = re.search(r'<link rel="canonical" href="(https://www\.encloud9\.com[^"]*)"', s)
        url = cm.group(1) if cm else ""
        q = qmap.get(url.rstrip("/") + "/", "") if url else ""
        if not q:
            tgt = "NO QUERY-MAP ROW" if url else "not built"
        else:
            words = [w for w in re.findall(r"[a-z0-9]+", q) if w not in ("and", "for", "the", "of", "in")]
            where = [lbl for lbl, txt in (("title", title), ("H1", h1), ("answer", lead)) if all(w in txt for w in words)]
            tgt = f'"{q}" in ' + (", ".join(where) if where else "NONE")
            if "title" not in where and "H1" not in where:
                bad += 1
        if url and not q:
            bad += 1
        pas = any(re.search(x, h1) for x in PASSIVE_H1)
        print(f"{name:38} {we:>4} {e9:>4} {len(sents):>4} {ban:>6}  {tgt}{'  PASSIVE H1' if pas else ''}")
        for m in set(re.findall(r"\[[^\]\n]{2,120}\]", t)):
            holders.append((name, m))
    print(f"\nPlaceholders still on pages ({len(holders)}):")
    for name, m in sorted(holders):
        print(f"  {name}: {m}")
    print(f"\n{bad} page(s) with no target row or the target missing from title and H1")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
