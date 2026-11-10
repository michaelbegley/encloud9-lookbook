const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const p of ['nine-home.html','nine-sales-accelerator.html','nine-service-accelerator.html','nine-support.html','nine-full-implementation.html']){
const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1});const pg=await ctx.newPage();
await pg.goto('http://localhost:8766/pages/'+p,{waitUntil:'networkidle'});
const r=await pg.evaluate(()=>{const small=[...document.querySelectorAll('main a.btn, header a.btn, header button, main button')].filter(e=>e.offsetParent&&!e.closest('#lbbar')).map(e=>[e.innerText.trim().slice(0,20),Math.round(e.getBoundingClientRect().height)]).filter(x=>x[1]<48);
const lb=document.getElementById('lbbar');return {H:document.documentElement.scrollHeight,lbH:lb?lb.offsetHeight:0,small:small.slice(0,8),nGrid:document.querySelectorAll('.grid9 .cell').length,cells:[...document.querySelectorAll('.grid9 .cell')].slice(0,9).map(c=>{const r=c.getBoundingClientRect();return Math.round(r.width)+'x'+Math.round(r.height)})}});
console.log(p,JSON.stringify(r));await ctx.close();}
// 1440 grid cells
for(const p of ['nine-sales-accelerator.html','nine-service-accelerator.html']){const ctx=await b.newContext({viewport:{width:1440,height:900}});const pg=await ctx.newPage();await pg.goto('http://localhost:8766/pages/'+p);await pg.waitForTimeout(1200);
console.log(p,'1440',await pg.evaluate(()=>JSON.stringify({cells:[...document.querySelectorAll('.grid9 .cell')].map(c=>{const r=c.getBoundingClientRect();return Math.round(r.width)+'x'+Math.round(r.height)}),ptiles:[...document.querySelectorAll('.ptile')].map(c=>Math.round(c.getBoundingClientRect().height)),lnav:[...document.querySelectorAll('.lnav a')].map(c=>Math.round(c.getBoundingClientRect().height))})));await ctx.close();}
await b.close();})();
