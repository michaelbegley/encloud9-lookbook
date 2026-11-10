const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();
for(const f of ['nine-service-accelerator.html','nine-sales-accelerator.html']){
for(const w of [320,390,1440]){const p=await b.newPage({viewport:{width:w,height:900}});
await p.goto('file:///home/claude/lb/pages/'+f);await p.waitForTimeout(300);
console.log(f,w,JSON.stringify(await p.evaluate(()=>{
 const o={};o.secs=[...document.querySelectorAll('main section')].map(s=>(s.id||s.className||'?')+':'+Math.round(s.querySelector('h2,.proof,.hero *')?.getBoundingClientRect().left??-1)+':par='+s.parentElement.className);
 o.wide=[...document.querySelectorAll('.pf .num')].map(e=>e.textContent+':'+Math.round(e.getBoundingClientRect().right)+'/'+Math.round(e.scrollWidth));
 return o;})));await p.close();}}
await b.close();})();
