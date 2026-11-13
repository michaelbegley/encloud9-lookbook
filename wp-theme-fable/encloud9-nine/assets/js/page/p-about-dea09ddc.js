(function(){
  /* hero fact cubes and stage cubes: tilt the hovered cube toward the cursor (fine pointers, motion allowed) */
  var calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches,fine=window.matchMedia('(pointer:fine)').matches;
  if(!fine||calm)return;
  document.querySelectorAll('.fgrid,.dgx').forEach(function(g){
    g.addEventListener('pointermove',function(e){var c=e.target.closest('a');if(!c)return;var r=c.getBoundingClientRect();
      c.style.setProperty('--ry',(((e.clientX-r.left)/r.width-.5)*10).toFixed(2)+'deg');c.style.setProperty('--rx',(-((e.clientY-r.top)/r.height-.5)*10).toFixed(2)+'deg')});
    g.addEventListener('pointerout',function(e){var c=e.target.closest('a');if(c&&!c.contains(e.relatedTarget)){c.style.removeProperty('--rx');c.style.removeProperty('--ry')}});
  });
})();
(function(){
  /* nine beliefs: each one lights as you scroll down to it, once, never hides again */
  var calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var bel=document.querySelector('[data-bel]');if(!bel||calm)return;
  var cells=bel.querySelectorAll('.bc'),n=document.querySelector('[data-beln]'),bar=document.querySelector('.bel-n .bar i'),shown=0,ticking=false;
  bel.classList.add('go');
  function upd(){
    ticking=false;var r=bel.getBoundingClientRect(),vh=window.innerHeight;
    var p=(vh*0.9-r.top)/(r.height*0.75+vh*0.25),want=Math.max(0,Math.min(cells.length,Math.ceil(p*cells.length)));
    while(shown<want){cells[shown].classList.add('in');shown++}
    n.textContent=shown+' of '+cells.length;bar.style.setProperty('--p',shown/cells.length);
    if(shown>=cells.length)window.removeEventListener('scroll',onS);
  }
  function onS(){if(!ticking){ticking=true;requestAnimationFrame(upd)}}
  window.addEventListener('scroll',onS,{passive:true});window.addEventListener('resize',onS);upd();
})();
