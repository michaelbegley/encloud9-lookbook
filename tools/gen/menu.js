const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const p of ['nine-sales-accelerator.html','nine-service-accelerator.html','nine-support.html']){
const ctx=await b.newContext({viewport:{width:390,height:844}});const pg=await ctx.newPage();
await pg.goto('http://localhost:8766/pages/'+p);
const st=()=>pg.evaluate(()=>[document.querySelector('.menu-btn').getAttribute('aria-expanded'),getComputedStyle(document.getElementById('mnav')).display]);
await pg.click('.menu-btn');const o=await st();await pg.keyboard.press('Escape');const e=await st();
const foc=await pg.evaluate(()=>document.activeElement.className);
await pg.click('.menu-btn');await pg.click('#mnav > a[href="nine-marketing.html"]').catch(x=>'');await pg.waitForTimeout(300);
console.log(p,'open',o,'esc',e,'focusAfterEsc',foc,'urlAfterTap',pg.url().split('/').pop());
// FAQ open
await ctx.close();}
await b.close();})();
