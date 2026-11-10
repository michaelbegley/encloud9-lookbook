const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
await p.goto('file:///home/claude/lb/pages/'+process.argv[2]+'.html');await p.waitForTimeout(2500);
const sel=process.argv[3];const els=await p.$$(sel);await els[+process.argv[4]||0].hover();await p.waitForTimeout(900);
console.log(await p.$$eval(sel,es=>es.map(e=>getComputedStyle(e).transform+' '+getComputedStyle(e).animationName).join('\n')));
await p.screenshot({path:process.argv[5]||'hov.png'});await b.close()})();
