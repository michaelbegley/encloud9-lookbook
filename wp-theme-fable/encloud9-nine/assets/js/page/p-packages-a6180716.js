/* signature: which package fits picker (plain JS, no loops, motion gated in CSS) */
(function(){
  var root=document.getElementById('picker');if(!root)return;
  var dest=root.querySelector('.dest'),cubes=dest.querySelectorAll('[data-k]'),name=root.querySelector('[data-res-name]'),note=root.querySelector('[data-res-note]');
  var R={
    sales:['Sales Accelerator','../dynamics-365-sales-accelerator/',1],
    service:['Service Accelerator','../dynamics-365-service-accelerator/',1],
    full:['Full implementation','../microsoft-dynamics-365-implementation/',1],
    rescue:['Rescue and Repair','../encloud9-dynamics-365-crm-services/dynamics-365-crm-solutions-rescue-repair/',1],
    cc:['Talk to us about Dynamics 365 Contact Center','../dynamics-365-contact-center/',0],
    move:['Move from Salesforce, HubSpot or another CRM','../microsoft-dynamics-365-implementation/',1,['salesforce','hubspot'],'See the Full implementation package','Moving your data is part of a full implementation. '],
    checkup:['CRM Health Check, free','../crm-health-check/',0,0,'See the free CRM Health Check']
  };
  root.addEventListener('click',function(e){
    var b=e.target.closest('.pick-q button');if(!b)return;
    root.querySelectorAll('.pick-q button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
    var k=b.getAttribute('data-go'),r=R[k];
    dest.classList.add('on');
    cubes.forEach(function(c){var ck=c.getAttribute('data-k');c.classList.remove('lit','also');void c.offsetWidth;if(r[3]?r[3].indexOf(ck)>-1:ck===k)c.classList.add('lit');else if(ck==='support'&&r[2])c.classList.add('also')});
    name.textContent=r[0];
    note.innerHTML='';
    if(r[5]){note.appendChild(document.createTextNode(r[5]))}
    if(r[1]){var a=document.createElement('a');a.className='lnk';a.href=r[1];a.innerHTML=(r[4]||(k==='cc'?'See Dynamics 365 Contact Center':'See the '+r[0]+' package'))+' <span>&rarr;</span>';note.appendChild(a)}
    if(r[2]){note.appendChild(document.createTextNode(' Then professional, responsive monthly support plans from $500.'))}
    if(window.matchMedia('(max-width:860px)').matches){var sd=root.querySelector('.pick-side'),rr=sd.getBoundingClientRect();if(rr.top>window.innerHeight*.5||rr.bottom<0)sd.scrollIntoView({block:'start',behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'})}
  });
})();
