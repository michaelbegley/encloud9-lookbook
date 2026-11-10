const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1440,height:900}});
await pg.goto('file:///home/claude/lb/pages/nine-sales-accelerator.html');await pg.waitForTimeout(400);
const out=await pg.evaluate(()=>{
 const cv=document.createElement('canvas').getContext('2d');
 const rgb=c=>{cv.fillStyle='#000';cv.fillStyle=c;cv.fillRect(0,0,1,1);const d=cv.getImageData(0,0,1,1).data;cv.clearRect(0,0,1,1);return [d[0],d[1],d[2],d[3]/255]};
 const lum=([r,g,bb])=>{const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(r)+.7152*f(g)+.0722*f(bb)};
 const bgOf=e=>{while(e&&e!==document.documentElement){const c=getComputedStyle(e).backgroundColor;const p=rgb(c);if(c!=='rgba(0, 0, 0, 0)'&&c!=='transparent'&&p[3]>0.5)return {p,c};e=e.parentElement}return {p:[255,255,255,1],c:'default'}};
 const res=[];
 document.querySelectorAll('.grid9 .cell span, .ptile span, .lnav a, .lnav a span, .proof .pf *, .story span, .spec dt, .stg span').forEach(e=>{
  if(![...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()))return;
  const cs=getComputedStyle(e);const B=bgOf(e);let fg=rgb(cs.color);
  const f=fg.slice(0,3).map((v,i)=>v*fg[3]+B.p[i]*(1-fg[3]));
  const L1=lum(f),L2=lum(B.p);const r=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);
  res.push([r.toFixed(2),e.className||e.tagName,e.textContent.trim().slice(0,28),cs.fontSize,cs.color,B.c]);
 });
 return res.sort((a,b)=>a[0]-b[0]).slice(0,12);
});
out.forEach(r=>console.log(r.join(' | ')));await b.close();})();
