const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
await p.goto('file:///home/claude/lb/pages/nine-service-accelerator.html');await p.waitForTimeout(300);
const r=await p.evaluate(()=>{
 const parse=c=>{const m=c.match(/[\d.]+/g).map(Number);return {r:m[0],g:m[1],b:m[2],a:m.length>3?m[3]:1}};
 const L=c=>{const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(c.r)+.7152*f(c.g)+.0722*f(c.b)};
 const bgOf=e=>{let stack=[];while(e){const c=parse(getComputedStyle(e).backgroundColor);if(c.a>0){stack.push(c);if(c.a>=1)break;}e=e.parentElement}let base={r:255,g:255,b:255};for(let i=stack.length-1;i>=0;i--){const c=stack[i];base={r:c.r*c.a+base.r*(1-c.a),g:c.g*c.a+base.g*(1-c.a),b:c.b*c.a+base.b*(1-c.a)}}return base};
 const out=[];
 document.querySelectorAll('.grid9 .cell span, .lnav a, .lnav a .mono, .ptile span, .ptile .price small, .proof .pf span, .proof small, .stg .mono, .story .mono, .final .mono, .final .lead, .foot p, .foot a, .tm, .fine, .crumb a').forEach(e=>{
  const t=[...e.childNodes].filter(n=>n.nodeType==3).map(n=>n.textContent).join('').trim(); if(!t)return;
  const s=getComputedStyle(e);let c=parse(s.color);const bg=bgOf(e);
  if(c.a<1)c={r:c.r*c.a+bg.r*(1-c.a),g:c.g*c.a+bg.g*(1-c.a),b:c.b*c.a+bg.b*(1-c.a)};
  const l1=L(c),l2=L(bg);const cr=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);
  out.push([cr.toFixed(2),s.fontSize,s.fontWeight,(e.className||e.tagName)+' "'+t.slice(0,22)+'"']);});
 return out.sort((a,b)=>a[0]-b[0]);});
r.slice(0,22).forEach(x=>console.log(x.join(' | ')));console.log('total',r.length,'under4.5',r.filter(x=>x[0]<4.5).length);
await b.close();})();
