import sys,re,html
from html.parser import HTMLParser
s=open(sys.argv[1]).read()
t=re.search(r'<title>(.*?)</title>',s,re.S); print("TITLE:",html.unescape(t.group(1)))
m=re.search(r'<meta name="description" content="(.*?)"',s,re.S); print("META:",html.unescape(m.group(1)) if m else None)
mm=re.search(r'<main.*?</main>',s,re.S).group(0)
mm=re.sub(r'<script.*?</script>','',mm,flags=re.S)
mm=re.sub(r'<style.*?</style>','',mm,flags=re.S)
mm=re.sub(r'<(br|/p|/h\d|/li|/div|/dd|/dt|/section|/figcaption|/time)[^>]*>','\n',mm)
mm=re.sub(r'<[^>]+>',' ',mm)
mm=html.unescape(mm)
lines=[re.sub(r'\s+',' ',l).strip() for l in mm.split('\n')]
print('\n'.join(l for l in lines if l))
