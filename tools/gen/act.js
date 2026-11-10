// interaction shots: node act.js page selectorToClick shotname width
const { chromium } = require('playwright');
const [,, pg, sel, shot, wid, focus] = process.argv;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:+wid||1440,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file:///home/claude/lb/pages/'+pg+'.html');
await p.locator(sel).first().scrollIntoViewIfNeeded();await p.waitForTimeout(1200);
await p.locator(sel).first().click();await p.waitForTimeout(900);
const el=p.locator(focus||sel).first();await el.scrollIntoViewIfNeeded();
await p.evaluate(()=>window.scrollBy(0,-120));await p.waitForTimeout(300);
await p.screenshot({path:'/home/claude/dec/shots/'+shot+'.png'});
console.log('errors',errs.length,errs.join('|'));
const info=await p.evaluate(()=>{const r=document.querySelector('[data-res-name]');const st=document.querySelector('[data-status]');return (r?r.textContent:'')+' / '+(st?st.textContent:'')});console.log(info);
await b.close()})();
