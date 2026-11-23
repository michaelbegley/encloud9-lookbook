(function(){var f=document.getElementById('cform'),m=document.getElementById('cmsg');if(!f)return;
f.addEventListener('submit',function(ev){ev.preventDefault();if(!f.checkValidity()){m.hidden=false;m.textContent='Fill in every field and tick the privacy box.';f.reportValidity();return;}
m.hidden=false;m.textContent='That did not send. Call 1-844-264-0729 or email sales@encloud9.com.';});})();
