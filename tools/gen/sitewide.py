import re,sys,glob
files=sys.argv[1:]
tot={}
def fix(s):
    n={}
    def r(pat,rep,flags=0):
        nonlocal s
        s2,k=re.subn(pat,rep,s,flags=flags);s=s2;n[pat[:30]]=k
    r(r'Every plan includes Microsoft escalation','Every monthly plan includes Microsoft escalation')
    r(r',? excluding US federal holidays','')
    r(r'Anyone can ask\. No SLA, so plan clients come first\.','Anyone can ask. No SLA.')
    r(r'Probably not a fit if','Consider another option if')
    r(r'rescued within a mere three-month timeframe','back on track within three months')
    # link grids: links are not list items; the container becomes a labelled group
    r(r'(<a\b[^>]*?) role=(\\?)"listitem"',r'\1')
    r(r'(<(?:div|nav|section|ul|ol)\b[^>]*?) role=(\\?)"list"([^>]*>\s*<a\b)',r'\1 role=\2"group"\3')
    return s,n
for f in files:
    s=open(f,encoding='utf-8').read();s2,n=fix(s)
    if s2!=s:open(f,'w',encoding='utf-8').write(s2)
    for k,v in n.items():tot[k]=tot.get(k,0)+v
print(tot)
