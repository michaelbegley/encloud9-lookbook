from rep import run
P='/home/claude/lb/pages/nine-marketing.html'
css=r'''@media (max-width:860px){.vs{grid-template-columns:1fr}}
/* ===== polish round (4 Nov): consistent with the home page ===== */
/* journey cubes are links now; the hovered one comes toward you, the rest step back (home hero values) */
.jc .ar{position:absolute;right:14px;top:12px;opacity:0;transform:translate(-4px,4px);transition:opacity .3s,transform .35s var(--ease)}
.jc:hover .ar,.jc:focus-visible .ar{opacity:1;transform:none}
.jc:focus-visible{outline-offset:-4px;outline-color:var(--white)}
.jc.lt:focus-visible,.jc:not(.lit):focus-visible{outline-color:var(--b5)}
@media (hover:hover) and (prefers-reduced-motion:no-preference){
  .jgrid{perspective:900px}
  .jc{transition:background .5s var(--ease),color .5s,transform .5s var(--bounce),box-shadow .4s var(--ease),filter .4s var(--ease)}
  .jgrid:hover .jc{filter:saturate(.85) brightness(.92);transform:perspective(900px) scale(.97)}
  .jgrid:hover .jc:hover{filter:none;z-index:3;transform:perspective(900px) translateZ(80px) translateY(-10px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg)) scale(1.1);box-shadow:0 34px 60px -26px rgba(14,26,58,.7),0 10px 20px -12px rgba(14,26,58,.45)}
}
.jplay button{min-height:44px;transition:background .25s,color .25s}
.jplay button .gl{display:inline-grid;grid-template-columns:repeat(3,4px);gap:1px;margin-right:10px;vertical-align:1px}
.jplay button .gl i{width:4px;height:4px;background:currentColor;opacity:.35}
.jplay button .gl i:nth-child(-n+4){opacity:1}
/* what we set up: four coloured cubes on the left, words on the right */
.mk-split{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:clamp(32px,5vw,72px);align-items:center}
.mk-split .copyc{display:flex;flex-direction:column;gap:20px}
.mk-set{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.mt{position:relative;background:var(--c);color:var(--white);aspect-ratio:1/.86;padding:clamp(18px,2vw,26px);display:flex;flex-direction:column;gap:10px}
.mt.lt{color:var(--ink)}
.mt .pt-top{display:flex;justify-content:space-between;align-items:flex-start}
.mt .mono{color:rgba(255,255,255,.78)}.mt.lt .mono{color:var(--ink2)}
.mt b{font-family:var(--head);font-size:clamp(22px,2vw,28px);font-weight:600;letter-spacing:-.025em;line-height:1.08;margin-top:auto}
.mt span.d{font-size:15px;line-height:1.45;opacity:.86}
.mt.lt .g.big i{background:rgba(14,26,58,.16)}.mt.lt .g.big i.on{background:var(--ink)}
@media (hover:hover) and (prefers-reduced-motion:no-preference){
  .mk-set{perspective:900px}
  .mt{transition:transform .5s var(--bounce),box-shadow .4s var(--ease),filter .4s var(--ease)}
  .mk-set:hover .mt{filter:saturate(.85) brightness(.92);transform:perspective(900px) scale(.97)}
  .mk-set:hover .mt:hover{filter:none;z-index:3;transform:perspective(900px) translateZ(60px) translateY(-8px) scale(1.06);box-shadow:0 34px 60px -26px rgba(14,26,58,.7),0 10px 20px -12px rgba(14,26,58,.45)}
}
@media (max-width:1080px){.mk-split{grid-template-columns:1fr}.mk-split .copyc{order:-1}}
@media (max-width:560px){.mk-set{grid-template-columns:1fr}.mt{aspect-ratio:auto;min-height:190px}}
/* client grid in the band: every cube carries a label, the four Click clients are links */
.mk-cg{width:min(380px,100%)}
.mk-cg .aic{display:flex;align-items:flex-end;padding:10px;font-family:var(--label);font-size:11px;line-height:1.3;color:var(--b8);position:relative}
.mk-cg .aic.cl{background:var(--b4);border-color:transparent;color:var(--white);font-family:var(--head);font-size:15px;font-weight:600;letter-spacing:-.01em;line-height:1.15}
.mk-cg .aic.cl::before{content:"";position:absolute;top:10px;left:10px;width:8px;height:8px;background:var(--b8)}
.mk-cg .aic.on{align-items:center;justify-content:center;font-family:var(--head);font-size:26px;font-weight:600;letter-spacing:-.02em;color:var(--white)}
.mk-cg .aic.cl:focus-visible{outline-color:var(--white)}
.js body.p-marketing .mk-cg.in .aic{opacity:1;transform:none;animation-fill-mode:backwards}
@media (hover:hover) and (prefers-reduced-motion:no-preference){
  .mk-cg{perspective:900px}
  .js body.p-marketing .mk-cg .aic{transition:transform .5s var(--bounce),box-shadow .4s var(--ease),filter .4s var(--ease),background .3s}
  .js body.p-marketing .mk-cg.in:hover .aic{filter:brightness(.85);transform:perspective(900px) scale(.97)}
  .js body.p-marketing .mk-cg.in:hover .aic.cl:hover{filter:none;z-index:3;background:var(--b5);transform:perspective(900px) translateZ(80px) translateY(-10px) scale(1.1);box-shadow:0 34px 60px -26px rgba(0,0,0,.7)}
}
@media (max-width:860px){.mk-cg{width:min(340px,100%)}.mk-cg .aic.cl{font-size:13px}.mk-cg .aic{font-size:10px;padding:8px}.mk-cg .aic.on{font-size:20px}}
/* support: table left, words right, so it does not mirror the band above */
@media (min-width:1081px){body.p-marketing .plans-grid.flip{grid-template-columns:minmax(0,1fr) minmax(0,440px)}body.p-marketing .plans-grid.flip>.tbl-wrap{order:-1}}
'''
pairs=[
('@media (max-width:860px){.vs{grid-template-columns:1fr}}\n',css),
]
# journey cubes -> links
J=[('01','Email','Campaign sent','From Click or Customer Insights','#click','b1',''),
   ('02','Click','Link opened','The visit is tied to the person','#click','b2',''),
   ('03','Web','Pages read','Web tracking on your site','#click','b3',''),
   ('04','Form','Form filled','A form or landing page','#setup','b4',''),
   ('05','Dynamics 365','On the record','Lead or contact, with its history','#setup','b5',' core'),
   ('06','Score','Lead scored','Points for what they did','#setup','b6',''),
   ('07','Alert','Seller told','A named owner follows up','#setup','b7',' lt'),
   ('08','Sales','Opportunity','In the same pipeline','#stories','b8',' lt'),
   ('09','Report','What worked','Campaigns measured by results','#setup','b9',' lt')]
for n,lab,b,sm,href,c,cls in J:
    old=f'<div role="listitem" class="jc{cls}" style="--c:var(--{c})"><span class="n">{n} &middot; {lab}</span><b>{b}</b><small>{sm}</small></div>'
    new=f'<a role="listitem" class="jc{cls}" style="--c:var(--{c})" href="{href}"><span class="n">{n} &middot; {lab}</span><b>{b}</b><small>{sm}</small><span class="ar" aria-hidden="true">&#8599;</span></a>'
    pairs.append((old,new))
pairs+= [
('<button type="button" id="jbtn">Play the journey</button>','<button type="button" id="jbtn"><span class="gl" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span>Play the journey</button>'),
('''    <div class="proof rev">
      <div class="pf">Click Gold Partner [confirm current tier]</div>
      <a class="pf" href="nine-stories.html">23 client stories<small>See the stories &rarr;</small></a>
      <div class="pf">Microsoft partner since 2008, specializing in Dynamics 365</div>
      <a class="pf" href="#support">Support from $500 a month<small>See support plans &rarr;</small></a>
    </div>''','''    <div class="proof big rev">
      <div class="pf"><b class="num">Gold</b><span>Click partner tier [confirm current tier]</span></div>
      <a class="pf" href="#stories"><b class="num">23</b><span>client stories, four of them run Click</span><small>See the four &rarr;</small></a>
      <div class="pf"><b class="num">2008</b><span>The year we became a Microsoft partner. We specialize in Dynamics 365.</span></div>
      <a class="pf" href="#support"><b class="num">$500</b><span>a month, where support plans start</span><small>See support plans &rarr;</small></a>
    </div>'''),
]
# setup section
old_setup_start='''  <section class="sec" aria-labelledby="set-h">
    <div class="sec-head rev">
      <h2 class="h2" id="set-h">What does enCloud9 set up?</h2>
      <p class="lead">A marketing setup is only useful if every form and email lands on the right record. That is the part we build carefully.</p>
    </div>
    <div class="rows rev">'''
import re
s=open(P).read()
i=s.index(old_setup_start); j=s.index('</section>',i)+len('</section>')
old_setup=s[i:j]
assert 'Anything outside the agreed scope' in old_setup
new_setup='''  <section class="sec" id="setup" aria-labelledby="set-h">
    <div class="mk-split">
      <div class="mk-set rev" role="list" aria-label="What we set up">
        <div role="listitem" class="mt" style="--c:var(--b1)"><span class="pt-top"><span class="mono">Email</span><span class="g big" aria-hidden="true"><i class="on"></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span></span><b>Sending you can trust</b><span class="d">Your sending domain authenticated (SPF, DKIM and DMARC) and Click's email sending domain set up, so campaigns reach inboxes.</span></div>
        <div role="listitem" class="mt" style="--c:var(--b3)"><span class="pt-top"><span class="mono">Forms</span><span class="g big" aria-hidden="true"><i class="on"></i><i class="on"></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span></span><b>Forms that reach Dynamics 365</b><span class="d">Every form on your site tested end to end, with source and campaign on the lead, and one alert per lead.</span></div>
        <div role="listitem" class="mt" style="--c:var(--b5)"><span class="pt-top"><span class="mono">Leads</span><span class="g big" aria-hidden="true"><i class="on"></i><i class="on"></i><i class="on"></i><i></i><i class="on"></i><i></i><i></i><i></i><i></i></span></span><b>Scoring and handoff</b><span class="d">A written rule for when a lead goes to sales, a named owner, and a Teams alert when it does.</span></div>
        <div role="listitem" class="mt lt" style="--c:var(--b8)"><span class="pt-top"><span class="mono">Reporting</span><span class="g big" aria-hidden="true"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i></span></span><b>Reports on results</b><span class="d">Campaigns judged by clicks, replies and meetings booked, not opens.</span></div>
      </div>
      <div class="copyc rev">
        <h2 class="h2" id="set-h">What does enCloud9 set up?</h2>
        <p class="lead">A marketing setup is only useful if every form and email lands on the right record. That is the part we build carefully.</p>
        <p class="fine" style="margin:0">Anything outside the agreed scope is a written change order you approve before work starts.</p>
        <div class="acts"><a class="btn btn-p" href="nine-book.html">Book a call</a><a class="lnk" href="#checkups">Free checkups, no obligation <span>&rarr;</span></a></div>
      </div>
    </div>
  </section>'''
pairs.append((old_setup,new_setup))
B={'bg':'https://www.encloud9.com/blog/success_stories/bg-landholdings-strengthens-data-quality-and-email-deliverability-with-encloud9-email-verifier/',
 'ms':'https://www.encloud9.com/blog/success_stories/how-milestone-leasing-optimized-dynamics-365-to-support-sales-and-lease-renewals/',
 'el':'https://www.encloud9.com/blog/success_stories/elmwood-reclaimed-timber-migrating-a-20-year-old-crm-to-the-cloud/',
 'jw':'https://www.encloud9.com/blog/success_stories/manufacturer-integrates-website-with-crm-to-automate-lead-assignment/'}
pairs.append(('''<div class="aigrid" aria-hidden="true"><i class="aic" style="--d:0"></i><i class="aic on" style="--d:1"></i><i class="aic" style="--d:2"></i><i class="aic on" style="--d:3"></i><i class="aic" style="--d:4"></i><i class="aic on" style="--d:5"></i><i class="aic" style="--d:6"></i><i class="aic on" style="--d:7"></i><i class="aic" style="--d:8"></i></div>''',
f'''<div class="aigrid mk-cg" role="list" aria-label="What Click does, and the four clients whose stories name Click">
        <span role="listitem" class="aic" style="--d:0">Email</span>
        <a role="listitem" class="aic cl" style="--d:1" href="{B['bg']}">B&amp;G Landholdings</a>
        <span role="listitem" class="aic" style="--d:2">Forms</span>
        <a role="listitem" class="aic cl" style="--d:3" href="{B['ms']}">Milestone Leasing</a>
        <span role="listitem" class="aic on" style="--d:4">Click</span>
        <a role="listitem" class="aic cl" style="--d:5" href="{B['el']}">Elmwood Reclaimed Timber</a>
        <span role="listitem" class="aic" style="--d:6">Web tracking</span>
        <a role="listitem" class="aic cl" style="--d:7" href="{B['jw']}">JWC Environmental</a>
        <span role="listitem" class="aic" style="--d:8">Lead scoring</span>
      </div>'''))
pairs.append(('<div class="plans-grid">','<div class="plans-grid flip">'))
pairs.append(('''    <div class="sec-head rev"><h2 class="h2" id="fq-h">Marketing automation questions we get asked</h2></div>
    <div class="faq rev">''','''    <div class="faqsplit">
      <div class="faqside rev">
        <h2 class="h2" id="fq-h">Marketing automation questions we get asked</h2>
        <p class="lead" style="margin-top:18px">Something else on your mind? Ask us on a call. You get a straight answer, whether or not you work with us.</p>
        <div class="acts" style="margin-top:24px"><a class="btn btn-p" href="nine-book.html">Book a call</a><a class="lnk" href="tel:+18442640729">1-844-264-0729 <span>&rarr;</span></a></div>
      </div>
      <div>
    <div class="faq rev">'''))
pairs.append(('''    <p class="fine">More reading: <a class="lnk" href="https://www.encloud9.com/blog/clickdimensions-dashboards-2025-update/">New ClickDimensions dashboards</a> &middot; <a class="lnk" href="https://www.encloud9.com/email-verifier/">enCloud9 Email Verifier</a></p>
  </section>''','''    <p class="fine">More reading: <a class="lnk" href="https://www.encloud9.com/blog/clickdimensions-dashboards-2025-update/">New ClickDimensions dashboards</a> &middot; <a class="lnk" href="https://www.encloud9.com/email-verifier/">enCloud9 Email Verifier</a></p>
      </div>
    </div>
  </section>'''))
pairs.append(('''  var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){io.disconnect();play()}},{threshold:.4});io.observe(g);''','''  var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){io.disconnect();play()}},{threshold:.4});io.observe(g);
  /* tilt the hovered cube toward the cursor (fine pointers only) */
  if(window.matchMedia('(pointer:fine)').matches){
    g.addEventListener('pointermove',function(e){var c=e.target.closest('.jc');if(!c)return;var r=c.getBoundingClientRect();
      c.style.setProperty('--ry',(((e.clientX-r.left)/r.width-.5)*10).toFixed(2)+'deg');c.style.setProperty('--rx',(-((e.clientY-r.top)/r.height-.5)*10).toFixed(2)+'deg')});
    g.addEventListener('pointerout',function(e){var c=e.target.closest('.jc');if(c&&!c.contains(e.relatedTarget)){c.style.removeProperty('--rx');c.style.removeProperty('--ry')}});
  }'''))
run(P,pairs)
