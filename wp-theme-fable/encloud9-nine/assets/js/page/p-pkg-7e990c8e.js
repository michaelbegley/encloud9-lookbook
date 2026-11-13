(function(){var i=document.getElementById('fqs'),n=document.getElementById('fqn');if(!i)return;
var ds=[].slice.call(document.querySelectorAll('.fqg details')),gs=[].slice.call(document.querySelectorAll('.fqg'));
i.addEventListener('input',function(){var t=i.value.trim().toLowerCase(),c=0;
ds.forEach(function(d){var hit=!t||d.textContent.toLowerCase().indexOf(t)>-1;d.hidden=!hit;if(hit)c++;d.open=!!t&&hit&&c<=3;});
gs.forEach(function(g){g.hidden=!g.querySelector('details:not([hidden])');});
n.textContent=t?(c+' of 205 questions match'):'205 questions';});})();
