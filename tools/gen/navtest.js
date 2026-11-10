const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
const url='http://localhost:8765/site/dynamics-365-sales/';
for(const w of [1081,1180,1280,1366,1440]){const p=await b.newPage({viewport:{width:w,height:900}});await p.goto(url);await p.waitForTimeout(300);
 const r=await p.evaluate(()=>{const n=document.querySelector('.nav'),items=[...n.querySelectorAll(':scope>.nav-i')];const tops=new Set(items.map(i=>Math.round(i.getBoundingClientRect().top)));const wrap=document.querySelector('.top .wrap');return {lines:tops.size,sw:document.documentElement.scrollWidth,wrapOver:wrap.scrollWidth>wrap.clientWidth+1,telR:Math.round(document.querySelector('.top .btn').getBoundingClientRect().right)}});
 console.log(w,JSON.stringify(r));await p.close()}
const p=await b.newPage({viewport:{width:1440,height:900}});await p.goto(url);await p.waitForTimeout(300);
const st=async()=>p.evaluate(()=>[...document.querySelectorAll('.nav-x')].map(x=>x.getAttribute('aria-expanded')[0]).join('')+' focus:'+(document.activeElement.className||document.activeElement.tagName));
await p.click('.nav-x[aria-controls="p-d365"]');console.log('click d365',await st());
await p.screenshot({path:process.argv[2]+'/panel1440.png'});
await p.click('.nav-x[aria-controls="p-packages"]');console.log('click packages',await st());
await p.keyboard.press('Escape');console.log('esc',await st());
await p.focus('.nav-x[aria-controls="p-copilot"]');await p.keyboard.press('Enter');console.log('enter copilot',await st());
await p.keyboard.press('Tab');console.log('tab into panel',await p.evaluate(()=>document.activeElement.textContent));
await p.keyboard.press('Escape');console.log('esc from panel',await st());
await p.click('.nav-x[aria-controls="p-about"]');await p.mouse.click(700,600);console.log('outside',await st());
await p.hover('.nav-i:first-child');console.log('hover no open',await st());
const m=await b.newPage({viewport:{width:390,height:844}});await m.goto(url);await m.click('.menu-btn');await m.click('#mnav details:first-of-type summary');await m.waitForTimeout(200);
console.log('mobile open details',await m.evaluate(()=>document.querySelector('#mnav details').open), await m.evaluate(()=>document.documentElement.scrollWidth));
await m.screenshot({path:process.argv[2]+'/mnav390.png'});
// axe
const fs=require('fs');const axe=fs.readFileSync('/tmp/claude-0/-home-claude/560b35a6-e00c-5990-89dc-05dfaaa63f19/scratchpad/po/node_modules/axe-core/axe.min.js','utf8');
for(const [pg,w,open] of [[p,1440,true],[m,390,true]]){ if(w===1440){await pg.click('.nav-x[aria-controls="p-d365"]')}
 await pg.addScriptTag({content:axe});const v=await pg.evaluate(async()=>{const r=await axe.run(document,{resultTypes:['violations']});return r.violations.map(v=>v.impact+' '+v.id+' '+v.nodes.length)});console.log('axe',w,v)}
await b.close()})()
