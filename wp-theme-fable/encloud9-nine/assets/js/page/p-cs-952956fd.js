/* signature: the case summarizes itself once it scrolls into view. The service-level bar runs down, Copilot writes the summary word by word, then the next step appears. Once only; skipped for reduced motion. */
(function(){
  var m=document.querySelector('.csm');if(!m)return;
  var calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(calm||!('IntersectionObserver' in window))return;
  var p=m.querySelector('[data-sum]'),words=p.getAttribute('data-sum').split(' ');
  m.classList.add('wait');p.textContent='';
  var io=new IntersectionObserver(function(es){
    if(!es[0].isIntersecting)return;io.disconnect();
    setTimeout(function(){
      m.classList.remove('wait');m.classList.add('typing');
      var i=0,caret=document.createElement('span');caret.className='caret';
      (function step(){
        p.textContent=words.slice(0,++i).join(' ');p.appendChild(caret);
        if(i<words.length){setTimeout(step,70)}else{setTimeout(function(){caret.remove();m.classList.remove('typing')},300)}
      })();
    },500);
  },{threshold:.5});
  io.observe(m);
})();
/* price cubes tilt under the cursor (fine pointers, motion allowed) */
(function(){
  var lic=document.querySelector('.p-cs .lic');
  if(!lic||!window.matchMedia('(pointer:fine)').matches||window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  lic.addEventListener('pointermove',function(e){var c=e.target.closest('.cell');if(!c)return;var r=c.getBoundingClientRect();
    c.style.setProperty('--ry',(((e.clientX-r.left)/r.width-.5)*10).toFixed(2)+'deg');c.style.setProperty('--rx',(-((e.clientY-r.top)/r.height-.5)*10).toFixed(2)+'deg')});
  lic.addEventListener('pointerout',function(e){var c=e.target.closest('.cell');if(c&&!c.contains(e.relatedTarget)){c.style.removeProperty('--rx');c.style.removeProperty('--ry')}});
})();
