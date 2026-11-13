/* signature: the app picker. Hover, focus or press a cube to see that app's line and Microsoft "from" price. Arrow keys move around the grid. */
(function(){
  var g=document.querySelector('.pk');if(!g)return;
  var cells=[].slice.call(g.querySelectorAll('button')),pds=[].slice.call(document.querySelectorAll('#pick-d .pd'));
  var fine=window.matchMedia('(pointer:fine)').matches;
  function sel(k){
    cells.forEach(function(c){c.setAttribute('aria-pressed',c.getAttribute('data-k')===k?'true':'false')});
    pds.forEach(function(p){var on=p.getAttribute('data-k')===k;if(on&&p.classList.contains('on'))return;p.classList.toggle('on',on);p.setAttribute('aria-hidden',on?'false':'true');p.querySelectorAll('a').forEach(function(a){a.tabIndex=on?0:-1})});
  }
  sel('sales');
  cells.forEach(function(c,i){
    var k=c.getAttribute('data-k');
    c.addEventListener('click',function(){sel(k)});
    c.addEventListener('focus',function(){sel(k)});
    if(fine)c.addEventListener('pointerenter',function(){sel(k)});
    c.addEventListener('keydown',function(e){
      var m={ArrowRight:1,ArrowLeft:-1,ArrowDown:3,ArrowUp:-3}[e.key];if(!m)return;
      var j=i+m;if(j<0||j>8)return;e.preventDefault();cells[j].focus();
    });
  });
})();
