const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
await p.goto('file:///home/claude/lb/pages/nine-blog.html');await p.waitForTimeout(2000);
await p.hover('.feat .fc:nth-child(3)');await p.waitForTimeout(1200);
console.log(await p.$$eval('.feat .fc',a=>a.map(e=>getComputedStyle(e).transform+' '+e.matches(':hover'))));
await p.screenshot({path:'/tmp/claude-0/-home-claude/560b35a6-e00c-5990-89dc-05dfaaa63f19/scratchpad/feathover.png',clip:{x:780,y:200,width:640,height:620}});
await b.close()})();
