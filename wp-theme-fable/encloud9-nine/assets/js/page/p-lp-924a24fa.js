(function(){document.querySelectorAll('form[data-concept]').forEach(function(f){var m=f.querySelector('.fm-msg');
function nm(el){var fs=el.closest('fieldset');if(fs&&fs.querySelector('legend'))return fs.querySelector('legend').textContent.replace(/Required/g,'').trim();
if(el.type==='checkbox')return 'the privacy policy box';var s=el.closest('label');s=s&&s.querySelector('span');return s?s.textContent.replace(/Required/g,'').trim():(el.name||'a field');}
f.addEventListener('submit',function(ev){ev.preventDefault();if(!m)return;m.textContent='';
f.querySelectorAll('[aria-invalid]').forEach(function(e){e.removeAttribute('aria-invalid')});
var bad=[],seen={};f.querySelectorAll('input,select,textarea').forEach(function(e){if(!e.checkValidity()){e.setAttribute('aria-invalid','true');var n=nm(e);if(!seen[n]){seen[n]=1;bad.push({n:n,e:e})}}});
var t=bad.length?'Please fill in: '+bad.map(function(b){return b.n}).join(', ')+'.':'Concept page: nothing is sent from here. On the live site this form goes to the CRM.';
if(bad.length)bad[0].e.focus();setTimeout(function(){m.textContent=t},60);});});})();
