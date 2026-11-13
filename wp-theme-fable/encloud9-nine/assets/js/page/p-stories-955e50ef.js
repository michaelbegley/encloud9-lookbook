/* signature: filter chips over all 23 stories, with the 23-cube map (plain JS, every card stays in the HTML) */
(function(){
  var bar=document.querySelector('.chips');if(!bar)return;
  var cards=[].slice.call(document.querySelectorAll('#grid .st')),cubes=[].slice.call(document.querySelectorAll('.st-map i')),stat=document.querySelector('[data-status]');
  var calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var L={all:'',new:'new builds',fix:'rescues and fixes',upgrade:'upgrades',time:'with a delivery time',cp:'Copilot and Power Platform'};
  function hit(el,f){if(f==='all')return true;if(f==='time')return el.getAttribute('data-time')==='1';if(f==='cp')return el.getAttribute('data-cp')==='1';return el.getAttribute('data-kind')===f}
  function apply(f){
    bar.querySelectorAll('button').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-f')===f?'true':'false')});
    var n=0;
    cards.forEach(function(c){var ok=hit(c,f);c.hidden=!ok;c.classList.remove('pop');if(ok){c.style.setProperty('--i',n);n++}});
    if(!calm){void document.body.offsetWidth;cards.forEach(function(c){if(!c.hidden)c.classList.add('pop')})}
    cubes.forEach(function(i){i.classList.toggle('off',!hit(i,f))});
    stat.textContent=f==='all'?'Showing all 23 stories':'Showing '+n+' of 23 stories: '+L[f];
  }
  bar.addEventListener('click',function(e){var b=e.target.closest('button[data-f]');if(b)apply(b.getAttribute('data-f'))});
  var j=document.querySelector('[data-jump]');if(j)j.addEventListener('click',function(){apply(j.getAttribute('data-jump'))});
})();
