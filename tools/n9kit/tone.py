"""Soften the hover-grow to Brian's 'a little too much, but modern' level on any page given."""
import sys,re
for f in sys.argv[1:]:
    s=open(f).read();o=s
    s=s.replace('translateZ(80px) translateY(-10px)','translateZ(40px) translateY(-6px)')
    s=re.sub(r'(:hover[^{]*\{[^}]*?)scale\(1\.1\)',r'\1scale(1.05)',s)
    s=re.sub(r'(:hover[^{]*\{[^}]*?)scale\(1\.0[6-9]\)',r'\1scale(1.04)',s)
    s=s.replace('filter:saturate(.85) brightness(.92)','filter:saturate(.92) brightness(.96)')
    s=re.sub(r'(:hover[^{]*\{[^}]*?)scale\(\.97\)',r'\1scale(.98)',s)
    s=s.replace('0 34px 60px -26px rgba(14,26,58,.7)','0 26px 46px -24px rgba(14,26,58,.6)')
    if s!=o: open(f,'w').write(s); print('toned',f)
