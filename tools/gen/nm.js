const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const p of ['nine-sales-accelerator.html','nine-service-accelerator.html','nine-support.html','nine-home.html']){
for(const w of [1440,820]){const ctx=await b.newContext({viewport:{width:w,height:900}});const pg=await ctx.newPage();
await pg.goto('http://localhost:8766/pages/'+p);await pg.waitForTimeout(500);
console.log(p,w,await pg.evaluate(()=>JSON.stringify([...document.querySelectorAll('.ptile')].map(t=>{const n=t.querySelector('.nm'),pr=t.querySelector('.price');return n?[Math.round(n.getBoundingClientRect().top-t.getBoundingClientRect().top),pr?Math.round(pr.getBoundingClientRect().top-t.getBoundingClientRect().top):null]:null}))));
await ctx.close();}}
await b.close();})();
