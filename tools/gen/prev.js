// before/after: every nine grid at the logo's gap (4.5 on a 29 square = 0.155 of a square)
const {chromium}=require('playwright');const path=require('path');
const [file,sel,w,out]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();
for(const mode of ['before','after']){const p=await b.newPage({viewport:{width:+w,height:900},reducedMotion:'reduce'});await p.goto('file://'+path.resolve(file));await p.waitForTimeout(600);
 await p.evaluate(()=>{const l=document.getElementById('lbbar');if(l)l.remove()});
 if(mode==='after')await p.evaluate(()=>{for(const c of document.querySelectorAll('body *')){const k=[...c.children].filter(x=>x.getBoundingClientRect().width>1);if(k.length!==9)continue;const t=new Set(k.map(x=>Math.round(x.getBoundingClientRect().top))).size,l=new Set(k.map(x=>Math.round(x.getBoundingClientRect().left))).size;if(t!==3||l!==3)continue;
   const W=c.getBoundingClientRect().width;const cell=W/(3+2*0.155);c.style.gap=(cell*0.155).toFixed(1)+'px'}});
 await p.waitForTimeout(300);const el=await p.$(sel);await el.screenshot({path:out.replace('.png','-'+mode+'.png')});await p.close()}
await b.close()})();
