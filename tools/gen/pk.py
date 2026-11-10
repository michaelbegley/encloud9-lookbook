from rep import run
import re
P='/home/claude/lb/pages/nine-packages.html'
s=open(P).read()
pairs=[]
css=r'''@media (prefers-reduced-motion:no-preference) and (max-width:860px){.js .sp-scale li{transform:scaleX(.04)}}
/* ===== polish round (4 Nov): consistent with the home page ===== */
/* hero cubes: let the hover-grow from nine.css win once the entrance pop has played */
@media (hover:hover) and (prefers-reduced-motion:no-preference){
  body.p-packages .grid9:hover .cell.base:hover{transform:perspective(900px) translateZ(40px) translateY(-8px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg)) scale(1.03)}
}
/* package cards become coloured cubes, the hovered one comes toward you */
.pk{background:var(--c);border:0;color:var(--white);min-height:400px}
.pk.lt{color:var(--ink)}
.pk .pt-top{display:flex;justify-content:space-between;align-items:flex-start}
.pk .pt-top .mono{color:rgba(255,255,255,.78)}.pk.lt .pt-top .mono{color:var(--ink2)}
.pk.lt .g.big i{background:rgba(14,26,58,.16)}.pk.lt .g.big i.on{background:var(--ink)}
.pk .h3{margin-top:auto}
.pk .one{color:rgba(255,255,255,.84)}.pk.lt .one{color:var(--ink2)}
.pk dl{margin:0;border-top:1.5px solid rgba(255,255,255,.5)}.pk.lt dl{border-top-color:rgba(14,26,58,.4)}
.pk dl div{border-bottom-color:rgba(255,255,255,.18)}.pk.lt dl div{border-bottom-color:rgba(14,26,58,.16)}
.pk dt{color:rgba(255,255,255,.72)}.pk.lt dt{color:var(--ink2)}
.pk .go{color:var(--white)}.pk.lt .go{color:var(--ink)}
.pk:hover{border-color:transparent}
.pk:focus-visible{outline-offset:3px}
@media (hover:hover) and (prefers-reduced-motion:no-preference){
  .pk-cards{perspective:1200px}
  .pk{transition:transform .5s var(--bounce),box-shadow .4s var(--ease),filter .4s var(--ease)}
  .pk-cards:hover .pk{filter:saturate(.85) brightness(.92);transform:perspective(1200px) scale(.97)}
  .pk-cards:hover .pk:hover{filter:none;z-index:3;transform:perspective(1200px) translateZ(60px) translateY(-10px) scale(1.05);box-shadow:0 34px 60px -26px rgba(14,26,58,.7),0 10px 20px -12px rgba(14,26,58,.45)}
}
/* support bars: same hover feel; the whole bar opens the plan comparison */
.sp-scale li .cover{position:absolute;inset:0;z-index:2}
.sp-scale li .cover:focus-visible{outline:2px solid var(--white);outline-offset:3px}
.sp-scale li .go{font-size:13px;font-weight:600;opacity:.85}
@media (hover:hover) and (prefers-reduced-motion:no-preference){
  .js body.p-packages .sp-scale li{transition:transform .9s var(--bounce) calc(var(--i,0)*140ms),opacity .5s calc(var(--i,0)*140ms),scale .5s var(--bounce),translate .5s var(--bounce),filter .4s var(--ease),box-shadow .4s var(--ease)}
  body.p-packages .sp-scale:hover li{filter:brightness(.85);scale:.98}
  body.p-packages .sp-scale:hover li:hover{filter:none;scale:1.05;translate:0 -10px;z-index:3;box-shadow:0 34px 60px -26px rgba(0,0,0,.7)}
}
/* the line-by-line table now sits behind a toggle under the picker */
.fitmore{margin-top:clamp(32px,4vw,48px);border-top:1px solid var(--line)}
.fitmore summary{cursor:pointer;list-style:none;display:inline-flex;align-items:center;gap:10px;min-height:44px;padding-top:12px;font-weight:600;font-size:15px}
.fitmore summary::-webkit-details-marker{display:none}
.fitmore summary::after{content:"+";font-size:20px;color:var(--b5);transition:transform .3s var(--ease)}
.fitmore[open] summary::after{transform:rotate(45deg)}
.fitmore .tbl-wrap{margin-top:16px}
/* stories: words left, two outcome cards right */
.pk-st{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:clamp(32px,5vw,72px);align-items:center}
.pk-st .copyc{display:flex;flex-direction:column;gap:20px}
.pk-st .story .big{margin-top:4px}
@media (max-width:1080px){.pk-st{grid-template-columns:1fr}}
'''
pairs.append(('@media (prefers-reduced-motion:no-preference) and (max-width:860px){.js .sp-scale li{transform:scaleX(.04)}}\n',css+'\n'))
pairs.append(('.js body.p-packages .pk-hero .cell{animation:pop .75s var(--ease) both;','.js body.p-packages .pk-hero .cell{animation:pop .75s var(--ease) backwards;'))
pairs.append(('.pk.flash{border-color:var(--b5);box-shadow:inset 0 0 0 2px var(--b5)}\n',''))
# hero base cell gets an arrow
pairs.append(('<span class="big">From $500<small>a month, Stability plan</small></span></a>','<span class="big">From $500<small>a month, Stability plan</small></span><span class="ar" aria-hidden="true">&#8599;</span></a>'))
# proof
pairs.append(('''    <div class="proof rev">
      <a class="pf" href="https://www.encloud9.com/blog/success_stories/streamlining-sales-processes-the-schiff-groups-transformation-with-dynamics-365-by-encloud9/">A new Dynamics 365 Sales system in one month for The Schiff Group<small>Read the story &rarr;</small></a>
      <a class="pf" href="nine-stories.html">23 client stories<small>See the stories &rarr;</small></a>
      <div class="pf">Clients in [30+] US states</div>
      <a class="pf" href="nine-support.html#plans">Support from $500 a month<small>See support plans &rarr;</small></a>
    </div>''','''    <div class="proof big rev">
      <a class="pf" href="https://www.encloud9.com/blog/success_stories/streamlining-sales-processes-the-schiff-groups-transformation-with-dynamics-365-by-encloud9/"><b class="num">1 month</b><span>A new Dynamics 365 Sales system for The Schiff Group</span><small>Read the story &rarr;</small></a>
      <a class="pf" href="nine-stories.html"><b class="num">23</b><span>client stories, new builds to rescues</span><small>See the stories &rarr;</small></a>
      <div class="pf"><b class="num">[30+]</b><span>US states with enCloud9 clients</span></div>
      <a class="pf" href="#support"><b class="num">$500</b><span>a month, where support plans start</span><small>See the plans &rarr;</small></a>
    </div>'''))
# package cards
def glyph(n):
    return '<span class="g big" aria-hidden="true">'+''.join('<i class="on"></i>' if k<n else '<i></i>' for k in range(9))+'</span>'
for m in re.finditer(r'<a class="pk" id="(pk-\w+)" href="([^"]+)"><span class="sq( lt)?" style="background:var\(--(b\d)\)">(0\d)</span>',s):
    pid,href,lt,col,num=m.groups()
    new=f'<a class="pk{lt or ""}" id="{pid}" style="--c:var(--{col})" href="{href}"><span class="pt-top"><span class="mono">Package {num}</span>{glyph(int(num))}</span>'
    pairs.append((m.group(0),new))
# support bars: cover links
names={'s1':'On-Demand','s2':'Stability','s3':'Optimization','s4':'Partnership'}
for k,v in names.items():
    m=re.search(r'(<li class="%s"[^>]*>)(.*?)</li>'%k,s)
    pairs.append((m.group(0),m.group(1)+m.group(2)+f'<a class="cover" href="nine-support.html#plans" aria-label="Compare the {v} plan"></a></li>'))
# fit table into details
pairs.append(('''    <div class="tbl-wrap rev" style="margin-top:clamp(40px,5vw,64px)" tabindex="0" role="region" aria-label="Table, scrolls sideways on small screens">
      <table class="tbl fit-tbl">''','''    <details class="fitmore">
    <summary>See every line as a table</summary>
    <div class="tbl-wrap" tabindex="0" role="region" aria-label="Table, scrolls sideways on small screens">
      <table class="tbl fit-tbl">'''))
pairs.append(('''      </table>
    </div>
    <p class="fine">Not sure?''','''      </table>
    </div>
    </details>
    <p class="fine">Not sure?'''))
# stories split
pairs.append(('''    <div class="sec-head rev">
      <h2 class="h2" id="cs-h">Which businesses have we set up or rescued on Dynamics 365?</h2>
      <p class="lead">Here are two of our 23 client stories: one new Dynamics 365 Sales system and one rescue of an over-customized system.</p>
    </div>
    <div class="stories two rev">''','''    <div class="pk-st">
    <div class="copyc rev">
      <h2 class="h2" id="cs-h">Which businesses have we set up or rescued on Dynamics 365?</h2>
      <p class="lead">Here are two of our 23 client stories: one new Dynamics 365 Sales system and one rescue of an over-customized system.</p>
      <div class="acts">
        <a class="btn btn-o" href="nine-stories.html">All 23 client stories</a>
        <a class="lnk" href="https://www.encloud9.com/lp/schedule-a-meeting/">Book a call <span>&rarr;</span></a>
      </div>
    </div>
    <div class="stories two rev">'''))
pairs.append(('<span class="mono">Maryland &middot; Product: Dynamics 365 Sales &middot; Timeline: 1 month</span><span class="t">The Schiff Group</span>','<span class="mono">Maryland &middot; Dynamics 365 Sales</span><span class="big">1 month</span><span class="t">The Schiff Group</span>'))
pairs.append(('<span class="mono">Tulsa &middot; Work: rescue and clean-up &middot; Timeline: within three months</span><span class="t">Hogan Assessments</span>','<span class="mono">Tulsa &middot; Rescue and clean-up</span><span class="big">3 months</span><span class="t">Hogan Assessments</span>'))
pairs.append(('''    </div>
    <div class="acts" style="margin-top:28px">
      <span>Want to know which package would fit your system? <a class="lnk" href="https://www.encloud9.com/lp/schedule-a-meeting/">Book a call <span>&rarr;</span></a></span>
      <a class="btn btn-o" href="nine-stories.html">All 23 client stories</a>
    </div>''','''    </div>
    </div>'''))
# FAQ split
pairs.append(('''    <div class="sec-head rev"><h2 class="h2" id="fq-h">Package questions we get asked</h2></div>
    <div class="faq rev">''','''    <div class="faqsplit">
      <div class="faqside rev">
        <h2 class="h2" id="fq-h">Package questions we get asked</h2>
        <p class="lead" style="margin-top:18px">Something else on your mind? Ask us on a call. You get a straight answer, whether or not you work with us.</p>
        <div class="acts" style="margin-top:24px"><a class="btn btn-p" href="https://www.encloud9.com/lp/schedule-a-meeting/">Book a call</a><a class="lnk" href="tel:+18442640729">1-844-264-0729 <span>&rarr;</span></a></div>
      </div>
    <div class="faq rev">'''))
pairs.append(('''      <details><summary>Do we need a support plan after go-live?</summary><p>Yes. New clients start on at least the Stability plan, $500 a month for 4 hours, on a 12-month agreement. Monthly plans include a 1-hour response during business hours, 7:00am to 5:00pm Central, Monday to Friday.</p></details>
    </div>''','''      <details><summary>Do we need a support plan after go-live?</summary><p>Yes. New clients start on at least the Stability plan, $500 a month for 4 hours, on a 12-month agreement. Monthly plans include a 1-hour response during business hours, 7:00am to 5:00pm Central, Monday to Friday.</p></details>
    </div>
    </div>'''))
run(P,pairs)
