"""Spelling check for one page's visible words (standard gate G14, added 9 Nov 2026).
Usage: python3 tools/spell.py pages/nine-home.html  -> prints JSON {unknown:[...], names:[...]}
Words in tools/words.txt (one per line, the site's own names and terms) are accepted."""
import sys, re, json, html, os
from spellchecker import SpellChecker
src = open(sys.argv[1], encoding='utf-8').read()
src = re.sub(r'<nav id="lbbar".*?</nav>', ' ', src, flags=re.S)
src = re.sub(r'<(script|style)\b.*?</\1>', ' ', src, flags=re.S)
src = re.sub(r'<span class="sh">&shy;</span>', '', src)
src = re.sub(r'<!--headmeta-->.*?<!--/headmeta-->', ' ', src, flags=re.S)
alts = ' '.join(re.findall(r'\b(?:alt|aria-label|title)="([^"]*)"', src) + re.findall(r'<meta name="description" content="([^"]*)"', src))
text = html.unescape(re.sub(r'<[^>]+>', ' ', src) + ' ' + alts).replace('\u00ad', '').replace('\u2019', "'").replace('\u2018', "'")  # curly apostrophes keep contractions whole (10 Nov 2026)
here = os.path.dirname(os.path.abspath(__file__))
extra = {w.strip().lower() for w in open(os.path.join(here, 'words.txt'), encoding='utf-8') if w.strip() and not w.startswith('#')}
sp = SpellChecker()
words = re.findall(r"[A-Za-z][A-Za-z']+", text)
unk = sorted({w for w in words if w.lower().strip("'") not in extra and not re.search(r'[A-Z].*[A-Z]', w[1:] or 'x') and sp.unknown([w.lower().strip("'").removesuffix("'s")])})
# Microsoft names written the wrong way
BAD = [r'\bPowerBI\b', r'\bPower Bi\b', r'\bCoPilot\b', r'\bCo-?pilot\b(?<!Copilot)', r'\bDynamics365\b', r'\bCommon Data Service\b',
       r'\bCopilot studio\b', r'\bPower (apps|automate|pages|bi)\b', r'\bDynamics 365 (sales|customer service|field service|customer insights|contact center|project operations)\b',
       r'\bDataVerse\b', r'\bMicrosoft partner\b', r'\bOffice 365\b']
names = sorted({m.group(0) for b in BAD for m in re.finditer(b, text)})
print(json.dumps({'unknown': unk, 'names': names}))
