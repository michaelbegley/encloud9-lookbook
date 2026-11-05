/* Look 9 "Nine": shared script for the built concept pages */
(function(){
  var d=document,root=d.documentElement;
  root.classList.add('js');

  /* font switcher (lookbook review only) */
  var KEY='n9font',fonts=['hanken','jakarta','public','bricolage'];
  function setFont(f){
    if(fonts.indexOf(f)<0)f='hanken';
    if(f==='hanken')root.removeAttribute('data-font');else root.setAttribute('data-font',f);
    d.querySelectorAll('[data-setfont]').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-setfont')===f?'true':'false')});
    try{localStorage.setItem(KEY,f)}catch(e){}
  }
  var saved='hanken';try{saved=localStorage.getItem(KEY)||'hanken'}catch(e){}
  var q=(location.search.match(/[?&]font=(\w+)/)||[])[1];
  setFont(q||saved);
  d.addEventListener('click',function(e){
    var b=e.target.closest('[data-setfont]');
    if(b){setFont(b.getAttribute('data-setfont'));return}
    var m=e.target.closest('.menu-btn');
    if(m){var n=d.getElementById('mnav'),open=n.classList.toggle('open');m.setAttribute('aria-expanded',open?'true':'false');m.textContent=open?'Close':'Menu'}
  });

  /* header border once scrolled */
  var top=d.querySelector('.top');
  function onScroll(){if(top)top.classList.toggle('scrolled',window.scrollY>8)}
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();

  /* reveal once on scroll */
  var els=d.querySelectorAll('.rev,.aigrid,.stages,.scale');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target)}})},{rootMargin:'0px 0px -10% 0px'});
    els.forEach(function(el){io.observe(el)});
  }else{els.forEach(function(el){el.classList.add('in')})}

  /* readiness check */
  var box=d.querySelector('.qbox');
  if(box){
    var qs=box.querySelectorAll('.q'),count=box.querySelector('[data-count]'),score=box.querySelector('[data-score]'),note=box.querySelector('[data-note]');
    box.addEventListener('click',function(e){
      var b=e.target.closest('.q button');if(!b)return;
      b.parentNode.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed','false')});
      b.setAttribute('aria-pressed','true');
      var answered=0,yes=0;
      qs.forEach(function(q){var p=q.querySelector('[aria-pressed="true"]');if(p){answered++;if(p.getAttribute('data-v')==='y')yes++}});
      count.textContent=answered+' of '+qs.length+' answered';
      score.textContent=yes+' of '+qs.length;
      note.textContent=answered<qs.length?'Answer all five to see your next step.':(yes===qs.length?'Your data looks ready. An agent pilot on a small group is a sensible next step.':(yes>=3?'Close. Fix the "No" and "Not sure" answers first, then plan a pilot.':'Start with the basics first. A free checkup shows what to fix.'));
    });
  }

  /* grid light and tilt under the cursor (fine pointers only, motion allowed) */
  var calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches,fine=window.matchMedia('(pointer:fine)').matches;
  var g=d.querySelector('.grid9');
  if(g&&fine&&!calm){
    g.addEventListener('pointermove',function(e){
      var r=g.getBoundingClientRect();g.style.setProperty('--mx',(e.clientX-r.left)+'px');g.style.setProperty('--my',(e.clientY-r.top)+'px');
      var c=e.target.closest('.cell');if(!c)return;var cr=c.getBoundingClientRect();
      c.style.setProperty('--ry',(((e.clientX-cr.left)/cr.width-.5)*10).toFixed(2)+'deg');
      c.style.setProperty('--rx',(-((e.clientY-cr.top)/cr.height-.5)*10).toFixed(2)+'deg');
    });
    g.addEventListener('pointerout',function(e){var c=e.target.closest('.cell');if(c&&!c.contains(e.relatedTarget)){c.style.removeProperty('--rx');c.style.removeProperty('--ry')}});
  }

  /* generative page mock: type the request once, then build the page */
  var mock=d.querySelector('.mock[data-type]');
  if(mock){
    var out=mock.querySelector('.typed'),text=mock.getAttribute('data-type'),parts=mock.querySelectorAll('.kpi,.mock-line');
    if(calm||!('IntersectionObserver' in window)){out.textContent=text}
    else{
      mock.classList.add('wait');out.textContent='';
      var mo=new IntersectionObserver(function(es){if(!es[0].isIntersecting)return;mo.disconnect();var i=0;
        (function step(){out.textContent=text.slice(0,++i);if(i<text.length){setTimeout(step,28)}else{setTimeout(function(){parts.forEach(function(p,k){p.style.transitionDelay=(k*110)+'ms'});mock.classList.remove('wait')},250)}})();
      },{threshold:.5});mo.observe(mock);
    }
  }
})();

/* home polish: labelled AI grid lights once in view (hero cubes now just grow on hover, via CSS) */
(function(){
  var d=document,calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ai=d.querySelector('.aigrid.labelled');
  if(ai){
    var a=ai.querySelectorAll('.aic'),order=[0,1,2,5,8,7,6,3];
    function light(){order.forEach(function(k,i){setTimeout(function(){a[k].classList.add('lit')},calm?0:600+i*160)})}
    if(calm||!('IntersectionObserver' in window)){light()}
    else{var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){io.disconnect();light()}},{threshold:.5});io.observe(ai)}
  }
})();
