(function(){var f=document.getElementById('cform'),m=document.getElementById('cmsg');if(!f)return;
f.addEventListener('submit',function(ev){ev.preventDefault();if(!f.checkValidity()){m.hidden=false;m.textContent='Please fill in every field and tick the privacy box.';f.reportValidity();return;}
m.hidden=false;m.textContent='Concept form: not connected yet. On the live site this goes to our CRM. For now, email sales@encloud9.com or book a call.';});})();
