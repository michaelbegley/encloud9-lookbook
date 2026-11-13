/* blog index: search box and category chips filter the post cubes (plain JS) */
(function(){
  var d=document,q=d.getElementById('q'),cards=[].slice.call(d.querySelectorAll('#posts .pc')),chips=[].slice.call(d.querySelectorAll('.chip[data-cat]')),
      count=d.getElementById('count'),empty=d.getElementById('empty'),cat='all';
  function run(){
    var t=(q.value||'').trim().toLowerCase(),n=0;
    cards.forEach(function(c){
      var ok=(cat==='all'||c.getAttribute('data-cat')===cat)&&(!t||c.textContent.toLowerCase().indexOf(t)>-1);
      c.hidden=!ok;c.classList.remove('show');
      if(ok){c.style.setProperty('--o',n);void c.offsetWidth;c.classList.add('show');n++}
    });
    count.textContent='Showing '+n+' of '+cards.length+' posts';
    empty.hidden=n>0;
  }
  q.addEventListener('input',run);
  chips.forEach(function(b){b.addEventListener('click',function(){
    cat=b.getAttribute('data-cat');
    chips.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});run();
  })});
  d.getElementById('clear').addEventListener('click',function(){q.value='';cat='all';chips.forEach(function(x){x.setAttribute('aria-pressed',x.getAttribute('data-cat')==='all'?'true':'false')});run();q.focus()});
})();
