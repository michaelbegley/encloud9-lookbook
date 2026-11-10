const {chromium}=require('playwright');
const P='file:///home/claude/lb/pages/';
(async()=>{
const b=await chromium.launch();
for(const w of [320,390,768,1440]){
 for(const pg of ['nine-rescue-repair.html','nine-dynamics-365-sales.html']){
  const p=await b.newPage({viewport:{width:w,height:900}});
  const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
  await p.goto(P+pg);
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,60))}window.scrollTo({top:0,behavior:'instant'})});
  await p.waitForTimeout(800);
  const r=await p.evaluate(()=>{
   const secs=[...document.querySelectorAll('main .sec, main .hero, main .crumb')].map(s=>Math.round(s.getBoundingClientRect().left));
   const wide=[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>document.documentElement.clientWidth+1).slice(0,5).map(e=>e.tagName+'.'+e.className);
   return {sw:document.documentElement.scrollWidth,lefts:[...new Set(secs)],wide};
  });
  console.log(w,pg,JSON.stringify(r),'errs',errs.length,errs.slice(0,3));
  if(pg==='nine-rescue-repair.html'&&(w===390||w===1440)) await p.screenshot({path:`/home/claude/dec/shots/rev-rr-${w}.png`,fullPage:true});
  await p.close();
 }
}
// contrast
const p=await b.newPage({viewport:{width:1440,height:900}});
await p.goto(P+'nine-rescue-repair.html');
await p.evaluate(()=>document.querySelectorAll('.rev,.rise,.ln span').forEach(e=>e.classList.add('in')));
await p.waitForTimeout(1500);
const c=await p.evaluate(()=>{
 function rgb(s){const m=s.match(/[\d.]+/g).map(Number);return m}
 function L(c){const a=c.slice(0,3).map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*a[0]+.7152*a[1]+.0722*a[2]}
 function bg(e){while(e){const s=getComputedStyle(e).backgroundColor;const m=rgb(s);if(m.length<4||m[3]>0.5)return m; e=e.parentElement}return [255,255,255]}
 const out=[];
 document.querySelectorAll('.grid9 .cell span, .ptile span, .lnav a, .lnav a .mono, .story span, .proof .pf *, .final *').forEach(e=>{
  if(!e.childNodes.length||![...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()))return;
  const f=rgb(getComputedStyle(e).color);const op=parseFloat(getComputedStyle(e).opacity);const k=bg(e);
  const fc=f.length>3&&f[3]<1?f.slice(0,3).map((v,i)=>v*f[3]+k[i]*(1-f[3])):f;
  const l1=L(fc),l2=L(k);const r=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);
  if(r<4.5)out.push([e.className||e.tagName,e.textContent.trim().slice(0,30),r.toFixed(2),getComputedStyle(e).fontSize]);
 });return out;});
console.log('LOW CONTRAST',JSON.stringify(c,null,0));
// focus
await p.keyboard.press('Tab');await p.keyboard.press('Tab');
for(let i=0;i<40;i++){await p.keyboard.press('Tab');}
const f=await p.evaluate(()=>{const e=document.activeElement;const s=getComputedStyle(e);return [e.tagName,e.className,e.textContent.slice(0,30),s.outlineStyle,s.outlineWidth,s.boxShadow]});
console.log('focus',f);
// details
const n=await p.$$eval('.faq details',d=>d.length);
await p.click('.faq details:nth-child(2) summary');const o=await p.$eval('.faq details:nth-child(2)',d=>d.open);console.log('faq',n,'open after click',o);
// reduced motion
const p2=await b.newPage({viewport:{width:1440,height:900},reducedMotion:'reduce'});
await p2.goto(P+'nine-rescue-repair.html');await p2.waitForTimeout(500);
const rm=await p2.evaluate(()=>[...document.querySelectorAll('.rev,.rise,.grid9 .cell')].filter(e=>{const s=getComputedStyle(e);return parseFloat(s.opacity)<1||(s.animationName!=='none'&&parseFloat(s.animationDuration)>0.01)||parseFloat(s.transitionDuration)>0.01}).length);
console.log('reduced motion animated/hidden',rm);
await b.close();})();
