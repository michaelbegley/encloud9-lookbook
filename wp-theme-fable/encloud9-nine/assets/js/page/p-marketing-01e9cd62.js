(function(){
  var cells=[].slice.call(document.querySelectorAll('#journey .jc')),btn=document.getElementById('jbtn');
  var calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches,t=[];
  function all(){cells.forEach(function(c){c.classList.add('lit')})}
  function play(){
    t.forEach(clearTimeout);t=[];
    if(calm){all();return}
    cells.forEach(function(c){c.classList.remove('lit','pop')});
    cells.forEach(function(c,i){t.push(setTimeout(function(){c.classList.add('lit','pop');t.push(setTimeout(function(){c.classList.remove('pop')},380))},300+i*420))});
  }
  btn.addEventListener('click',play);
  var g=document.getElementById('journey');
  if(calm||!('IntersectionObserver' in window)){all();return}
  var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){io.disconnect();play()}},{threshold:.4});io.observe(g);
  /* tilt the hovered cube toward the cursor (fine pointers only) */
  if(window.matchMedia('(pointer:fine)').matches){
    g.addEventListener('pointermove',function(e){var c=e.target.closest('.jc');if(!c)return;var r=c.getBoundingClientRect();
      c.style.setProperty('--ry',(((e.clientX-r.left)/r.width-.5)*10).toFixed(2)+'deg');c.style.setProperty('--rx',(-((e.clientY-r.top)/r.height-.5)*10).toFixed(2)+'deg')});
    g.addEventListener('pointerout',function(e){var c=e.target.closest('.jc');if(c&&!c.contains(e.relatedTarget)){c.style.removeProperty('--rx');c.style.removeProperty('--ry')}});
  }
})();
