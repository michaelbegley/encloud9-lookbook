const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1440,height:900}});
await pg.goto('file:///home/claude/lb/pages/nine-sales-accelerator.html');
await pg.emulateMedia({reducedMotion:'reduce'});
await pg.waitForTimeout(500);
const out=await pg.evaluate(()=>{
 const parse=c=>{const m=c.match(/[\d.]+/g).map(Number);return m};
 const lum=([r,g,bb])=>{const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(r)+.7152*f(g)+.0722*f(bb)};
 const bg=e=>{while(e){const c=getComputedStyle(e).backgroundColor;const p=parse(c);if(p.length<4||p[3]>0.5)return p.slice(0,3);e=e.parentElement}return [255,255,255]};
 const res=[];
 document.querySelectorAll('.grid9 .cell *, .ptile *, .lnav a, .lnav a *, .proof .pf *, .story *, .final .mono, .final .lead, .final a, .fine, .crumb a, .spec dt, .stg .mono, .stg .d').forEach(e=>{
  if(!e.childNodes.length||![...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()))return;
  const cs=getComputedStyle(e);let fg=parse(cs.color);const a=fg[3]??1;const B=bg(e);
  if(a<1)fg=fg.slice(0,3).map((v,i)=>v*a+B[i]*(1-a));
  const L1=lum(fg),L2=lum(B);const r=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);
  res.push([r.toFixed(2),e.className||e.tagName,e.textContent.trim().slice(0,30),cs.fontSize,cs.opacity]);
 });
 return res.sort((a,b)=>a[0]-b[0]).slice(0,14);
});
out.forEach(r=>console.log(r.join(' | ')));
// reduced motion: are rev elements visible?
const hid=await pg.evaluate(()=>[...document.querySelectorAll('.rev,.rise,.ln>span')].filter(e=>getComputedStyle(e).opacity<0.99||getComputedStyle(e).transform!=='none').length);
console.log('hidden/transformed under reduced motion (no scroll):',hid);
// focus visible
await pg.keyboard.press('Tab');
const foc=[];for(let i=0;i<30;i++){await pg.keyboard.press('Tab');foc.push(await pg.evaluate(()=>{const e=document.activeElement;const cs=getComputedStyle(e);return (e.className||e.tagName)+':'+(cs.outlineStyle!=='none'&&parseFloat(cs.outlineWidth)>0?'outline':(cs.boxShadow!=='none'?'shadow':'NONE'))}));}
console.log(foc.join(' , '));
await b.close();})();
