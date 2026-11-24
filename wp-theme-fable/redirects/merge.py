import csv,json
base='/home/claude/lookbook/wp-theme-fable/encloud9-site/data/'
pages=json.load(open(base+'pages.json'));live=set(p['path'] for p in pages)
for l in open(base+'kept-posts.txt'):
    l=l.strip()
    if l and not l.startswith('#'): live.add(l.split()[0])
# Target fixes: the six dead targets below, Claude's call 15 Nov 2026, Michael approved all six, 15 Nov 2026 2:50 AM Central.
# Was also kept as claude/site-build/REDIRECT-MAP-Draft2-TARGET-FIXES.csv in the Claude project (removed 23 Nov 2026; this line is its record).
fix={'/support/':'/microsoft-dynamics-365-support-services/','/implementation/':'/microsoft-dynamics-365-implementation/','/microsoft-dynamics-365-copilot/':'/microsoft-copilot-for-business/','/microsoft-365-copilot/':'/microsoft-copilot-for-business/','/clickdimensions-powerpack/':'/marketing-services/','/dynamics-365-marketing-accelerator/':'/marketing-services/'}
rows={}
d1=list(csv.DictReader(open('draft1.csv')))
ad=list(csv.DictReader(open('REDIRECT-MAP-Draft2-ADDITIONS.csv')))
key=lambda p:p.rstrip('/').lower() if p!='/' else '/'
for r in d1: rows[key(r['old_address'])]=dict(old=r['old_address'],new=r['new_address'],code=r['code'],src='Draft1')
over=0
for r in ad:
    k=key(r['old_address'])
    if k in rows: over+=1
    rows[k]=dict(old=r['old_address'],new=r['new_address'],code=r['code'],src='Additions')
nfix=0
for r in rows.values():
    if r['code']=='301' and r['new'] in fix: r['new']=fix[r['new']];nfix+=1
# chains: follow target if it is itself a source
chain=0
for r in rows.values():
    seen=0
    while r['code']=='301' and key(r['new']) in rows and seen<5 and key(r['new'])!=key(r['old']):
        t=rows[key(r['new'])]; r['new']=t['new']; r['code']=t['code']; chain+=1; seen+=1
drop={'/blog/clickdimensions-dashboards-2025-update','/blog/dynamics-365-adoption'}
for k in drop: rows.pop(k,None)
bad=[(r['old'],r['new']) for r in rows.values() if r['code']=='301' and r['new'] not in live]
shadow=[r['old'] for r in rows.values() if (r['old'] if r['old'].endswith('/') else r['old']+'/') in live]
print('Draft1',len(d1),'additions',len(ad),'overrides',over,'total rules',len(rows))
print('target fixes applied',nfix,'chain hops collapsed',chain)
print('301',sum(r['code']=='301' for r in rows.values()),'410',sum(r['code']=='410' for r in rows.values()))
print('TARGET NOT ON NEW SITE',len(bad));[print('  ',x) for x in bad]
print('SOURCE IS A LIVE NEW PAGE (would hide it)',len(shadow));[print('  ',x) for x in shadow]
with open('redirection-import-301.csv','w',newline='') as f:
    w=csv.writer(f)
    for r in sorted(rows.values(),key=lambda r:r['old']):
        if r['code']=='301': w.writerow([r['old'],r['new'],0,301])
with open('redirection-410.txt','w') as f:
    for r in sorted(rows.values(),key=lambda r:r['old']):
        if r['code']=='410': f.write(r['old']+'\n')
with open('REDIRECT-MAP-Draft2-MERGED.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['old_address','new_address','code','from'])
    for r in sorted(rows.values(),key=lambda r:r['old']): w.writerow([r['old'],r['new'],r['code'],r['src']])
