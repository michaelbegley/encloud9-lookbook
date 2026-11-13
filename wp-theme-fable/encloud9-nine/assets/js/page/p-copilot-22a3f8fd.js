(function(){
  var d=document,calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches,fine=window.matchMedia('(pointer:fine)').matches;
  /* three forms grid: tilt the hovered cube toward the cursor (hero tilt comes from nine.js) */
  var fg=d.querySelector('.fgx');
  if(fg&&fine&&!calm){
    fg.addEventListener('pointermove',function(e){var c=e.target.closest('a');if(!c)return;var r=c.getBoundingClientRect();
      c.style.setProperty('--ry',(((e.clientX-r.left)/r.width-.5)*10).toFixed(2)+'deg');c.style.setProperty('--rx',(-((e.clientY-r.top)/r.height-.5)*10).toFixed(2)+'deg')});
    fg.addEventListener('pointerout',function(e){var c=e.target.closest('a');if(c&&!c.contains(e.relatedTarget)){c.style.removeProperty('--rx');c.style.removeProperty('--ry')}});
  }
  /* generative page builder: type the request, plan the layout, write the code, render; then take one change */
  var gx=d.querySelector('[data-gx]');if(!gx)return;
  var Q={a:'Add a tab to the account form with relationship health and the reason for it, win rate, open pipeline by month, contacts and open cases',
         b:'Make the first tab on a deal: revenue, a probability ring, stage, products, the activity timeline with overdue follow-ups in red, and the quote',
         c:'List the quotes waiting for a manager, so I can tick the ones I am happy with and approve them together'};
  var T={a:'Tables: Account, Opportunity, Case, Activity, Contact',b:'Tables: Opportunity, Product, Activity, Quote',c:'Tables: Quote, Opportunity, Account'};
  var N={a:'The page sits on the account form and gets the current record automatically. The finished page is an ordinary screen on your data.',b:'The first tab on a deal, with overdue follow-ups in red. The finished page is an ordinary screen on your data.',c:'Tick quotes and select Approve: the page updates each quote you tick. Try it.'};
  var R={a:'Put the open cases at the top',b:'Add a risk flag when follow-ups are overdue',c:'Sort by days waiting, longest first'};
  var RN={a:'Changed: the open cases now sit at the top of the tab. The rest of the page stayed as it was.',b:'Changed: a risk flag now sits at the top, built from the overdue follow-ups and the waiting quote.',c:'Changed: the longest wait is at the top. Tick and approve still work.'};
  var note=gx.querySelector('[data-note]'),out=gx.querySelector('[data-q]'),q2=gx.querySelector('[data-q2]'),q2t=gx.querySelector('[data-q2t]'),tb=gx.querySelector('[data-tb]'),
      steps=gx.querySelectorAll('.stp'),btns=gx.querySelectorAll('[data-pick]'),prog=gx.querySelector('[data-prog]'),chip=gx.querySelector('[data-refine]'),again=gx.querySelector('[data-again]'),
      cur='a',run=0,timers=[];
  function later(f,ms){timers.push(setTimeout(f,ms))}
  function p(v){prog.style.setProperty('--p',v)}
  function stop(){run++;timers.forEach(clearTimeout);timers=[];return run}
  function resetRefine(){gx.querySelectorAll('.gx-sc').forEach(function(s){s.classList.remove('rf')});q2.hidden=true;q2t.textContent='';chip.disabled=false;chip.classList.remove('ok');chip.textContent=R[cur]}
  function show(k,animate){
    var me=stop();cur=k;
    btns.forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-pick')===k?'true':'false')});
    gx.querySelectorAll('.gx-sc').forEach(function(s){s.classList.toggle('cur',s.getAttribute('data-sc')===k)});
    var sc=gx.querySelector('[data-sc="'+k+'"]'),parts=sc.querySelectorAll('.pt');
    tb.textContent=T[k];resetRefine();
    gx.querySelectorAll('.pt.flash').forEach(function(x){x.classList.remove('flash')});
    if(!animate){out.textContent=Q[k];steps.forEach(function(s){s.classList.add('done')});gx.classList.remove('building','planned');parts.forEach(function(x){x.classList.add('in')});p(1);note.textContent=N[k];return}
    gx.classList.add('building');gx.classList.remove('planned');parts.forEach(function(x){x.classList.remove('in')});
    steps.forEach(function(s){s.classList.remove('done')});chip.disabled=true;p(0);
    note.textContent='Reading your request.';
    var text=Q[k],i=0;out.textContent='';
    (function type(){if(me!==run)return;out.textContent=text.slice(0,++i);p(.3*i/text.length);if(i<text.length){later(type,15)}else{
      later(function(){steps[0].classList.add('done');gx.classList.add('planned');p(.5);note.textContent='Planning the layout from your request.'},300);
      later(function(){steps[1].classList.add('done');p(.75);note.textContent='Writing the code and connecting it to your Dataverse tables.'},1100);
      later(function(){steps[2].classList.add('done');p(1);note.textContent='Rendering on your data.'},1900);
      parts.forEach(function(x,n){later(function(){x.classList.add('in')},2000+n*130)});
      later(function(){gx.classList.remove('building','planned');note.textContent=N[k];chip.disabled=false},2200+parts.length*130+500);
    }})();
  }
  function refine(){
    if(chip.disabled)return;var k=cur,me=stop(),sc=gx.querySelector('[data-sc="'+k+'"]'),mv=sc.querySelector('[data-mv]');
    chip.disabled=true;q2.hidden=false;
    function apply(){sc.classList.add('rf');chip.classList.add('ok');chip.textContent='Change applied';note.textContent=RN[k];if(!calm){mv.classList.remove('flash');void mv.offsetWidth;mv.classList.add('flash')}}
    if(calm){q2t.textContent=R[k];steps.forEach(function(s){s.classList.add('done')});p(1);apply();return}
    steps.forEach(function(s){s.classList.remove('done')});p(0);note.textContent='Reading your change.';
    var text=R[k],i=0;q2t.textContent='';
    (function type(){if(me!==run)return;q2t.textContent=text.slice(0,++i);if(i<text.length){later(type,22)}else{
      steps.forEach(function(s,n){later(function(){s.classList.add('done');p((n+1)/3)},250+n*300)});
      later(apply,1200);
    }})();
  }
  btns.forEach(function(b){b.addEventListener('click',function(){show(b.getAttribute('data-pick'),!calm)})});
  chip.addEventListener('click',refine);
  again.addEventListener('click',function(){show(cur,!calm)});
  if(!calm&&'IntersectionObserver' in window){
    /* wait, empty, until the window is on screen, then build once */
    out.textContent='';steps.forEach(function(s){s.classList.remove('done')});p(0);chip.disabled=true;note.textContent='Waiting for a request.';
    gx.classList.add('building');gx.querySelectorAll('.gx-sc.cur .pt').forEach(function(x){x.classList.remove('in')});
    var io=new IntersectionObserver(function(es){if(!es[0].isIntersecting)return;io.disconnect();show(cur,true)},{threshold:.35});
    io.observe(gx.querySelector('.gx-win'));
  }else{show('a',false)}
  /* approvals: tick quotes, approve them together */
  var ap=gx.querySelector('[data-ap]'),go=ap.querySelector('[data-apgo]'),n=ap.querySelector('[data-apn]'),w=gx.querySelector('[data-apw]');
  function count(){var c=ap.querySelectorAll('input:checked:not([disabled])').length;n.textContent=c+' selected';go.disabled=c===0}
  ap.addEventListener('change',count);
  go.addEventListener('click',function(){
    ap.querySelectorAll('input:checked:not([disabled])').forEach(function(x){x.disabled=true;var st=x.parentNode.querySelector('[data-st]');st.textContent='Approved';st.className='badge g'});
    var left=ap.querySelectorAll('input:not([disabled])'),sum=0;left.forEach(function(x){sum+=+x.parentNode.querySelector('.amt').textContent.replace(/[^0-9]/g,'')});
    w.textContent=left.length;gx.querySelector('[data-apv]').textContent='$'+sum.toLocaleString('en-US');count();
  });
})();
