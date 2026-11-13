(function(){var f=document.getElementById('cform'),m=document.getElementById('cmsg');if(!f)return;f.addEventListener('submit',function(ev){ev.preventDefault();m.hidden=false;
m.textContent=f.checkValidity()?'Concept form: not connected yet. On the live site this goes to our CRM with the check named.':'Please fill in every field.';});})();
