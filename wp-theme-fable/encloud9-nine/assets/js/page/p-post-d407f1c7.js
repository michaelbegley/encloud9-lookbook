/* post: reading progress and the current section in the contents */
(function(){
  var d=document,bar=d.querySelector('.progress i'),art=d.getElementById('art'),
      links=[].slice.call(d.querySelectorAll('.toc a')),heads=links.map(function(a){return d.getElementById(a.getAttribute('href').slice(1))}),
      tocd=d.getElementById('tocd'),ticking=false;
  if(window.matchMedia('(max-width:1080px)').matches&&tocd)tocd.removeAttribute('open');
  function upd(){
    ticking=false;
    var r=art.getBoundingClientRect(),h=window.innerHeight,tot=r.height-h*.6,p=tot>0?Math.min(1,Math.max(0,(-r.top+h*.25)/tot)):0;
    bar.style.transform='scaleX('+p.toFixed(4)+')';
    var cur=-1;heads.forEach(function(el,i){if(el&&el.getBoundingClientRect().top<170)cur=i});
    links.forEach(function(a,i){var on=i===cur;a.classList.toggle('on',on);if(on)a.setAttribute('aria-current','true');else a.removeAttribute('aria-current')});
  }
  window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(upd)}},{passive:true});
  window.addEventListener('resize',upd);upd();
})();
