const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1440,height:900}});
await p.goto('file:///home/claude/lb/pages/nine-home.html');await p.waitForTimeout(2500);
console.log(await p.evaluate(()=>[matchMedia('(hover:hover)').matches,matchMedia('(pointer:fine)').matches]));
await p.addStyleTag({content:'.grid9 .cell{animation:none!important}'});
const el=p.locator('.grid9 .cell').nth(1);await el.hover();await p.waitForTimeout(900);
console.log(await p.evaluate(()=>[...document.querySelectorAll('.grid9 .cell')].slice(0,3).map(e=>getComputedStyle(e).transform)));
await b.close()})();
