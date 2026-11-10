import sys,re,html
from html.parser import HTMLParser
s=open(sys.argv[1]).read()
t=re.search(r'<title>(.*?)</title>',s,re.S); print("TITLE:",html.unescape(t.group(1)) if t else None)
m=re.search(r'<meta name="description" content="(.*?)"',s,re.S); print("META:",html.unescape(m.group(1)) if m else None)
mm=re.search(r'<main.*?</main>',s,re.S).group(0)
mm=re.sub(r'<(script|style).*?</\1>','',mm,flags=re.S)
mm=re.sub(r'</(p|h\d|li|div|section|dt|dd|time|span|a)>',r'</\1>\n',mm)
txt=html.unescape(re.sub(r'<[^>]+>','',mm))
print("\n".join(l.strip() for l in txt.splitlines() if l.strip()))
