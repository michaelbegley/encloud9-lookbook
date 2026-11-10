const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1440,height:900},reducedMotion:'reduce'});
await p.goto('file:///home/claude/lb/pages/nine-rescue-repair.html');await p.waitForTimeout(800);
console.log(await p.evaluate(()=>[...document.querySelectorAll('.rev,.rise,.grid9 .cell')].map(e=>{const s=getComputedStyle(e);return [e.className.slice(0,25),s.opacity,s.animationName,s.animationDuration,s.transitionDuration,s.transitionProperty.slice(0,40)]}).filter(x=>parseFloat(x[1])<1||x[2]!=='none'||parseFloat(x[4])>0.01)));
console.log(await p.evaluate(()=>{const e=[...document.querySelectorAll('.grid9 .cell .lab')].find(x=>x.textContent==='Stage B');const c=e.closest('.cell');return [c.className,getComputedStyle(c).backgroundColor,getComputedStyle(e).color,getComputedStyle(e).opacity]}));
console.log(await p.evaluate(()=>{const s=getComputedStyle(document.querySelector('section.final'));return [s.backgroundColor,s.backgroundImage.slice(0,60),getComputedStyle(document.querySelector('#fc-h')).color]}));
await b.close();})();
