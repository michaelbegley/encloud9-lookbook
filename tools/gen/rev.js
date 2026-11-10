const {chromium}=require('playwright');
(async()=>{
const b=await chromium.launch();
const url='file:///home/claude/lb/pages/nine-service-accelerator.html';
for(const w of [320,390,768,1440]){
 const p=await b.newPage({viewport:{width:w,height:900}});
 const errs=[];p.on('pageerror',e=>errs.push('PE '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push('CE '+m.text())});
 await p.goto(url);await p.waitForTimeout(500);
 const h=await p.evaluate(()=>document.body.scrollHeight);
 for(let y=0;y<h;y+=600){await p.evaluate(y=>window.scrollTo({top:y,behavior:'instant'}),y);await p.waitForTimeout(60);}
 await p.waitForTimeout(800);
 const r=await p.evaluate(()=>{const W=document.documentElement.clientWidth;const over=[...document.querySelectorAll('main *')].filter(e=>{const r=e.getBoundingClientRect();return r.right>W+1&&r.width>0}).slice(0,5).map(e=>e.className+':'+Math.round(e.getBoundingClientRect().right));return {sw:document.documentElement.scrollWidth,over}});
 console.log(w,JSON.stringify(r),errs);
 if(w==390||w==1440) await p.screenshot({path:`/home/claude/dec/shots/rev-sv-${w}.png`,fullPage:true});
 if(w==1440){
  const info=await p.evaluate(()=>{
   const o={};o.h1=document.querySelectorAll('h1').length;
   o.h2=[...document.querySelectorAll('h2')].map(h=>h.textContent.trim());
   o.lead=document.querySelector('.hero .lead').textContent.trim().split(/\s+/).length;
   o.badAnchors=[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.getElementById(h.slice(1)));
   o.rel=[...new Set([...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href')).filter(h=>!/^(https?:|tel:|#|mailto:)/.test(h)))];
   o.proof=[...document.querySelectorAll('.proof')].map(p=>p.children.length);
   o.orphanPf=[...document.querySelectorAll('.pf')].filter(e=>!e.closest('.proof')).map(e=>{const r=e.getBoundingClientRect();return e.textContent.trim().slice(0,40)+' @'+Math.round(r.top+scrollY)+' w'+Math.round(r.width)});
   o.jsonld=[...document.querySelectorAll('script[type="application/ld+json"]')].map(s=>{try{JSON.parse(s.textContent);return 'ok'}catch(e){return 'ERR '+e.message}});
   return o;});
  console.log(JSON.stringify(info,null,1));
 }
 await p.close();
}
// reduced motion
const p=await b.newPage({viewport:{width:1440,height:900},reducedMotion:'reduce'});await p.goto(url);await p.waitForTimeout(300);
console.log('RM', await p.evaluate(()=>{const els=[...document.querySelectorAll('.rev,.rise,.ln>span,.grid9 .cell')];return els.filter(e=>{const s=getComputedStyle(e);return parseFloat(s.opacity)<1||s.transform!=='none'&&s.transform!=='matrix(1, 0, 0, 1, 0, 0)'}).length+' of '+els.length+' hidden/transformed'}));
// focus
await p.keyboard.press('Tab');await p.keyboard.press('Tab');
for(let i=0;i<14;i++)await p.keyboard.press('Tab');
console.log('FOCUS', await p.evaluate(()=>{const e=document.activeElement;const s=getComputedStyle(e);return e.className+' '+e.textContent.trim().slice(0,30)+' outline:'+s.outlineStyle+' '+s.outlineWidth+' '+s.outlineColor+' shadow:'+s.boxShadow}));
await b.close();})();
