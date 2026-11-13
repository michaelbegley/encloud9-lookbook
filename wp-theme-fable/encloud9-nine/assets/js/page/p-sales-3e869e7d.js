/* sales page: price cubes tilt under the cursor; the readiness check fills a cube meter as you answer */
(function(){
  var d=document,calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches,fine=window.matchMedia('(pointer:fine)').matches;
  var lic=d.querySelector('.p-sales .lic');
  if(lic&&fine&&!calm){
    lic.addEventListener('pointermove',function(e){
      var c=e.target.closest('.cell');if(!c)return;var r=c.getBoundingClientRect();
      c.style.setProperty('--ry',(((e.clientX-r.left)/r.width-.5)*10).toFixed(2)+'deg');
      c.style.setProperty('--rx',(-((e.clientY-r.top)/r.height-.5)*10).toFixed(2)+'deg');
    });
    lic.addEventListener('pointerout',function(e){var c=e.target.closest('.cell');if(c&&!c.contains(e.relatedTarget)){c.style.removeProperty('--rx');c.style.removeProperty('--ry')}});
  }
  var rc=d.querySelector('.p-sales .rc');if(!rc)return;
  var qs=[].slice.call(rc.querySelectorAll('.q')),cubes=[].slice.call(rc.querySelectorAll('.meter i')),meter=rc.querySelector('.meter');
  rc.addEventListener('click',function(e){
    var b=e.target.closest('.q button');if(!b)return;
    var q=b.closest('.q'),k=qs.indexOf(q),v=b.getAttribute('data-v');
    q.classList.remove('y','n','u');q.classList.add(v);
    var c=cubes[k];c.classList.remove('y','n','u','hit');c.classList.add(v);
    if(!calm){void c.offsetWidth;c.classList.add('hit')}
    var all=qs.every(function(x){return x.classList.contains('y')});
    meter.classList.toggle('all',all);
  });
})();
