const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const pg of ['nine-dynamics-365-sales','nine-dynamics-365','nine-customer-service'])for(const w of [1440,390,360]){
const p=await b.newPage({viewport:{width:w,height:900}});await p.emulateMedia({reducedMotion:'reduce'});
await p.goto('file:///home/claude/lb/pages/'+pg+'.html');await p.waitForTimeout(800);
const r=await p.evaluate(()=>{const out=[];document.querySelectorAll('.aic,.ptile,.lstack>i,.meter i,.lic .cell,.grid9 .cell,.ch-head,.q button,.pf').forEach(e=>{if(e.scrollWidth>e.clientWidth+1||e.scrollHeight>e.clientHeight+1)out.push(e.className+':'+e.textContent.trim().slice(0,30)+' '+e.scrollWidth+'/'+e.clientWidth+' '+e.scrollHeight+'/'+e.clientHeight)});
const small=[...document.querySelectorAll('main a,main button')].filter(e=>{const r=e.getBoundingClientRect();return r.width&&r.height&&r.height<24&&getComputedStyle(e).display!=='inline'}).map(e=>e.textContent.trim().slice(0,25));
return {out,small}});
console.log(pg,w,JSON.stringify(r));await p.close()}
await b.close()})();
