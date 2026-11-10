from rep import run
import re
P='/home/claude/lb/pages/nine-stories.html'
s=open(P).read()
pairs=[]
SHORT={"Within three months":"3 months","Completed in 90 days":"90 days","Completed in six months":"6 months","Completed in three months":"3 months","Completed within two months":"2 months","In one month":"1 month","Within 3 to 4 months":"3 to 4 months"}
LT={'upgrade','support','integration'}
cards=re.findall(r'<a class="st" href="[^"]+" data-kind="\w+" data-time="\d" data-cp="\d">.*?</a>',s)
print('cards',len(cards))
times=[]
for c in cards:
    m=re.search(r'<span class="st-top"><span class="kind"><i class="sw k-(\w+)" aria-hidden="true"></i>([^<]+)</span>(?:<span class="tm">([^<]+)</span>)?</span><span class="t">([^<]+)</span><span class="mono pl">([^<]+)</span>',c)
    kind,klab,tm,name,place=m.groups()
    lt=' lt' if kind in LT else ''
    if tm:
        big=SHORT[tm];small=f'<span class="sm">{klab} &middot; {tm[0].lower()+tm[1:]}</span>'
    else:
        big=klab;small=''
    head=f'<span class="st-head k-{kind}{lt}"><span class="mono">{place}</span><span class="ar" aria-hidden="true">&#8599;</span><span class="big">{big}</span>{small}</span><span class="t">{name}</span>'
    nc=c.replace(m.group(0),head)
    pairs.append((c,nc))
    if tm: times.append((name,klab,tm,re.search(r'href="([^"]+)"',c).group(1)))
print(times)
css=r'''@media (prefers-reduced-motion:no-preference){
  .js body.p-stories .st-hero .cell{animation:pop .75s var(--ease) backwards;'''
pairs.append(('''@media (prefers-reduced-motion:no-preference){
  .js body.p-stories .st-hero .cell{animation:pop .75s var(--ease) both;''',css))
newcss=r'''/* ===== polish round (4 Nov): consistent with the home page ===== */
/* story cards open with a coloured cube: place, then the big outcome (delivery time where the story states one, otherwise the kind of project) */
.st{padding:0;gap:0;min-height:0;overflow:hidden}
.st-head{position:relative;display:flex;flex-direction:column;gap:6px;min-height:156px;padding:18px 22px 20px;color:var(--white)}
.st-head.lt{color:var(--ink)}
.st-head .mono{color:rgba(255,255,255,.8)}.st-head.lt .mono{color:var(--ink2)}
.st-head .big{margin-top:auto;font-family:var(--head);font-size:clamp(30px,2.8vw,40px);font-weight:600;letter-spacing:-.035em;line-height:1}
.st-head .sm{font-family:var(--label);font-size:14px;opacity:.85}
.st-head .ar{position:absolute;right:18px;top:14px;opacity:0;transform:translate(-4px,4px);transition:opacity .3s,transform .35s var(--ease)}
.st:hover .st-head .ar,.st:focus-visible .st-head .ar{opacity:1;transform:none}
.st>.t{padding:20px 22px 0;margin:0}
.st .prod{padding:12px 22px 0}
.st>.ds{padding:12px 22px 0}
.st>.go{padding:16px 22px 22px}
@media (hover:hover) and (prefers-reduced-motion:no-preference){
  .st-grid{perspective:1400px}
  .st{transition:transform .5s var(--bounce),box-shadow .4s var(--ease),filter .4s var(--ease),border-color .3s}
  .st-grid:hover .st{filter:saturate(.85) brightness(.95);transform:perspective(1400px) scale(.97)}
  .st-grid:hover .st:hover{filter:none;z-index:3;border-color:var(--b7);transform:perspective(1400px) translateZ(60px) translateY(-10px) scale(1.05);box-shadow:0 34px 60px -26px rgba(14,26,58,.7),0 10px 20px -12px rgba(14,26,58,.45)}
}
@media (prefers-reduced-motion:no-preference){.js .st.pop{animation-fill-mode:backwards}}
/* delivery times: one cube per month, filled once on scroll */
.tl-top{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,5vw,72px);align-items:end;margin-bottom:clamp(36px,4vw,56px)}
.tl{border-top:2px solid rgba(255,255,255,.85)}
.tl-row,.tl-scale{display:grid;grid-template-columns:minmax(0,1.1fr) auto minmax(0,1fr);gap:clamp(16px,3vw,40px);align-items:center}
.tl-scale{padding:14px 0 10px;font-family:var(--label);font-size:14px;color:var(--b8)}
.tl-row{position:relative;padding:14px 18px;margin-inline:-18px;border-bottom:1px solid rgba(255,255,255,.14);transition:background .3s}
.tl-row:hover{background:rgba(255,255,255,.07)}
.tl-row .nm{font-family:var(--head);font-size:clamp(18px,1.6vw,22px);font-weight:600;letter-spacing:-.015em;line-height:1.2}
.tl-row .nm small{display:block;font-family:var(--label);font-size:14px;font-weight:400;letter-spacing:0;color:var(--b8);margin-top:4px}
.tl-row .ph{font-size:15px;color:var(--b8);display:flex;justify-content:space-between;gap:12px}
.tl-row .ph b{color:var(--white);font-weight:600}
.tl-row .ph .go{white-space:nowrap;color:var(--white);opacity:.7;transition:opacity .3s,transform .3s}
.tl-row:hover .ph .go{opacity:1;transform:translateX(3px)}
.bar,.ticks{display:grid;grid-template-columns:repeat(6,34px);gap:5px}
.bar i{display:block;width:34px;height:34px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);position:relative}
.bar i:nth-child(n+4){background:transparent;border-style:dashed;border-color:rgba(255,255,255,.18)}
.bar i.f{background:var(--b7);border-color:var(--b7)}
.bar i.f.on3{background:var(--b6);border-color:var(--b6)}
.bar i.h{background:linear-gradient(90deg,var(--b7) 50%,transparent 50%);border:1px dashed var(--b7)}
.ticks span{text-align:center}
.ticks span:nth-child(3){color:var(--white)}
.tl-scale .lbl{color:var(--white)}
@media (prefers-reduced-motion:no-preference){
  .js .tl .bar i.f,.js .tl .bar i.h{transform:scale(0);transition:transform .5s var(--bounce);transition-delay:calc(var(--r,0)*110ms + var(--k,0)*70ms + 200ms)}
  .js .tl.in .bar i.f,.js .tl.in .bar i.h{transform:none}
}
@media (max-width:1080px){.tl-row,.tl-scale{grid-template-columns:minmax(0,1fr) auto}.tl-row .ph{grid-column:1/-1}.tl-scale>span:last-child{display:none}}
@media (max-width:640px){.tl-top{grid-template-columns:1fr}.tl-row,.tl-scale{grid-template-columns:1fr}.tl-scale>span:first-child{display:none}.bar,.ticks{grid-template-columns:repeat(6,minmax(0,34px))}.bar i{width:auto;aspect-ratio:1/1;height:auto}.tl-row{margin-inline:-12px;padding-inline:12px}}
</style>'''
pairs.append(('</style>',newcss))
# hero core cell arrow
pairs.append(('<span class="lab">The Schiff Group</span><span class="nm">1 month</span><span class="ds">A new Dynamics 365 Sales system</span></a>','<span class="lab">The Schiff Group</span><span class="nm">1 month</span><span class="ds">A new Dynamics 365 Sales system</span><span class="ar" aria-hidden="true">&#8599;</span></a>'))
# proof
pairs.append(('''    <div class="proof rev">
      <a class="pf" href="#all">23 client stories<small>See them all &rarr;</small></a>
      <div class="pf">12 states</div>
      <a class="pf" href="#all" data-jump="time">9 published delivery times: 1 to 6 months, 7 of the 9 in three months or less<small>See the 9 &rarr;</small></a>
      <a class="pf" href="nine-support.html#plans">Support from $500 a month<small>See support plans &rarr;</small></a>
    </div>''','''    <div class="proof big rev">
      <a class="pf" href="#all"><b class="num">23</b><span>client stories, new builds to rescues</span><small>See them all &rarr;</small></a>
      <div class="pf"><b class="num">12</b><span>states across the US in these stories</span></div>
      <a class="pf" href="#times"><b class="num">7 of 9</b><span>published delivery times were three months or less. All 9 ran 1 to 6 months.</span><small>See the 9 &rarr;</small></a>
      <a class="pf" href="nine-support.html#plans"><b class="num">$500</b><span>a month, where support plans start</span><small>See support plans &rarr;</small></a>
    </div>'''))
# timeline band
def months(tm):
    return {"In one month":(1,0),"Completed within two months":(2,0),"Completed in 90 days":(3,0),"Within three months":(3,0),"Completed in three months":(3,0),"Within 3 to 4 months":(3,1),"Completed in six months":(6,0)}[tm]
times.sort(key=lambda x:(months(x[2])[0]+months(x[2])[1]*.5))
rows=[]
for r,(name,klab,tm,href) in enumerate(times):
    f,h=months(tm);cubes=''
    for k in range(6):
        cls='f' if k<f else ('h' if k==f and h else '')
        cubes+=f'<i class="{cls}" style="--k:{k}"></i>' if cls else '<i></i>'
    short=SHORT[tm]
    rows.append(f'      <a role="listitem" class="tl-row" href="{href}" style="--r:{r}"><span class="nm">{name}<small>{klab}</small></span><span class="bar" aria-hidden="true">{cubes}</span><span class="ph"><span><b>{short}</b>: {tm[0].lower()+tm[1:]}</span><span class="go">Read &rarr;</span></span></a>')
band='''<section class="band" id="times" aria-labelledby="tm-h">
  <div class="wrap">
    <div class="tl-top">
      <div class="rev">
        <span class="mono">Delivery times</span>
        <h2 class="h2" id="tm-h" style="margin-top:16px">How long did the projects take?</h2>
      </div>
      <p class="lead rev">Nine of our 23 client stories state a delivery time. They ran 1 to 6 months, and 7 of the 9 took three months or less. One cube is one month.</p>
    </div>
    <div class="tl rev" role="group" aria-label="The 9 stories that state a delivery time, shortest first">
      <div class="tl-scale" aria-hidden="true"><span>Client</span><span class="ticks"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span></span><span class="lbl">Months, as each story states it</span></div>
'''+'\n'.join(rows)+'''
    </div>
    <p class="fine" style="margin-top:20px;color:var(--b8)">The other 14 stories do not state a delivery time. The half cube is the "3 to 4 months" in the Elmwood story.</p>
  </div>
</section>

<div class="wrap">
  <section class="sec" id="next" aria-labelledby="nx-h">'''
pairs.append(('''    <p class="fine">Where a project started is our reading of each story. Delivery times are as stated in each story; the other 14 stories do not state one. Products are listed as each story lists them.</p>
  </section>

  <section class="sec" id="next" aria-labelledby="nx-h">''','''    <p class="fine">Where a project started is our reading of each story. Delivery times are as stated in each story; the other 14 stories do not state one. Products are listed as each story lists them.</p>
  </section>
</div>

'''+band))
run(P,pairs)
