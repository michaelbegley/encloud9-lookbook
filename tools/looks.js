// Gate G15 "Looks right" (added 9 Nov 2026, Michael). Usage: node tools/looks.js pages/nine-home.html [more pages...]
// Per page, at 1440, 1024, 768 and 390:
//  orphans  - a grid or wrapping row of cards whose last row is lonely (1 card under 3 or more, or under half a row: "4 over 1")
//  nine     - every 3 x 3 grid: nine equal squares (within 1.5 px), equal gaps across and down, colours only from the brand blues
//  sets     - cards side by side match: same title size, same icon size, same button height
//  type     - h1, h2, h3 and body text sizes, compared across pages in the summary (one size per role per width)
// With several pages it adds a site summary: the gap-to-square ratio of every nine grid and the size of each text role.
const {chromium}=require('playwright');const path=require('path');
const WIDTHS=[1440,1024,768,390];
const files=process.argv.slice(2).map(f=>path.resolve(f));
(async()=>{const b=await chromium.launch();const site={nine:[],type:{}};const out=[];
for(const file of files){const page={file:path.basename(file),orphans:[],nine:[],sets:[],type:{}};
 const ctx=await b.newContext({viewport:{width:1440,height:900},reducedMotion:'reduce'});const p=await ctx.newPage();await p.goto('file://'+file);await p.waitForTimeout(500);
 for(const w of WIDTHS){await p.setViewportSize({width:w,height:900});await p.waitForTimeout(250);
  const r=await p.evaluate((w)=>{
   const vis=e=>{const r=e.getBoundingClientRect();const cs=getComputedStyle(e);return r.width>1&&r.height>1&&cs.visibility!=='hidden'&&cs.display!=='none'&&cs.position!=='absolute'&&cs.position!=='fixed'};
   const name=e=>e.tagName.toLowerCase()+(e.id?'#'+e.id:'')+(e.classList.length?'.'+[...e.classList].slice(0,3).join('.'):'');
   const where=e=>{const s=e.closest('section,header,footer,main');const h=s&&s.querySelector('h1,h2,h3');return (h?h.textContent.trim().slice(0,40):name(s||e))};
   const rgb=c=>{const m=c.match(/rgba?\(([^)]+)\)/);if(!m)return null;const v=m[1].split(',').map(x=>parseFloat(x));return v.length>3&&v[3]===0?null:v.slice(0,3).map(Math.round).join(',')};
   const root=getComputedStyle(document.documentElement);
   const hex=h=>{h=h.trim().replace('#','');if(h.length===3)h=h.split('').map(c=>c+c).join('');return [0,2,4].map(i=>parseInt(h.substr(i,2),16)).join(',')};
   const palette=new Set();for(const t of ['--ink','--ink2','--muted','--line','--bg','--tint','--white','--b1','--b2','--b3','--b4','--b5','--b6','--b7','--b8','--b9']){const v=root.getPropertyValue(t);if(v&&v.trim().startsWith('#'))palette.add(hex(v))}
   const res={orphans:[],nine:[],sets:[],type:{}};
   const conts=[...document.querySelectorAll('main *, footer *')].filter(e=>{const cs=getComputedStyle(e);return vis(e)&&(cs.display==='grid'||cs.display==='inline-grid'||(cs.display==='flex'&&cs.flexWrap==='wrap'))});
   for(const c of conts){if(c.closest('nav,[role="tablist"]'))continue;const kids=[...c.children].filter(vis);
    // orphans
    if(kids.length>=3&&kids.every(k=>{const r=k.getBoundingClientRect();return r.width>=120&&r.height>=48})){
     const rows={};kids.forEach(k=>{const t=Math.round(k.getBoundingClientRect().top/4);rows[t]=(rows[t]||0)+1});const counts=Object.keys(rows).sort((a,b)=>a-b).map(k=>rows[k]);
     if(counts.length>=2){const first=Math.max(...counts.slice(0,-1)),last=counts[counts.length-1];
      const lastKids=kids.filter(k=>Math.round(k.getBoundingClientRect().top/4)==Object.keys(rows).sort((a,b)=>a-b).pop());const fullBand=lastKids.length===1&&lastKids[0].getBoundingClientRect().width>=c.getBoundingClientRect().width-4;
      // a last item that spans the whole row on purpose (a band) is not an orphan
      if(!fullBand&&first>=3&&last<first&&(last===1||last/first<0.5))res.orphans.push({where:where(c),grid:name(c),rows:counts.join(' + ')})}}
    // nine grids
    if(kids.length===9){const R=kids.map(k=>k.getBoundingClientRect());const tops=[...new Set(R.map(r=>Math.round(r.top)))],lefts=[...new Set(R.map(r=>Math.round(r.left)))];
     if(tops.length===3&&lefts.length===3){const ws=R.map(r=>r.width),hs=R.map(r=>r.height);const sp=a=>Math.max(...a)-Math.min(...a);
      const gx=R[1].left-R[0].right,gy=R[3].top-R[0].bottom;const cell=(ws.reduce((a,b)=>a+b)/9);
      const cols=kids.map(k=>rgb(getComputedStyle(k).backgroundColor)).filter(Boolean);const off=[...new Set(cols.filter(x=>!palette.has(x)))];
      const issues=[];if(sp(ws)>1.5||sp(hs)>1.5)issues.push('squares not all the same size ('+Math.round(Math.min(...ws))+' to '+Math.round(Math.max(...ws))+' wide, '+Math.round(Math.min(...hs))+' to '+Math.round(Math.max(...hs))+' tall)');
      if(Math.abs(cell-hs.reduce((a,b)=>a+b)/9)>1.5)issues.push('not square ('+Math.round(cell)+' x '+Math.round(hs.reduce((a,b)=>a+b)/9)+')');
      if(Math.abs(gx-gy)>1)issues.push('gap across '+gx.toFixed(1)+' vs down '+gy.toFixed(1));
      if(off.length)issues.push('colours off the brand blues: '+off.join(' | '));
      res.nine.push({where:where(c),grid:name(c),cell:Math.round(cell),gap:+gx.toFixed(1),ratio:+(gx/cell).toFixed(3),issues})}}
    // sets: cards side by side
    const sig=k=>k.tagName+'.'+(k.classList[0]||'');const kw=kids.map(k=>k.getBoundingClientRect().width);
    // a card set: same kind of element, similar widths, and no section heading inside (that is a two-column layout, not cards)
    if(kids.length>=2&&kids.length<=12&&kw.every(x=>x>=120)&&new Set(kids.filter((k,i)=>!(kids.length===9&&i===4)).map(sig)).size===1&&Math.max(...kw)/Math.min(...kw)<=1.15&&!kids.some(k=>k.querySelector('h2'))){
     const byTop={};kids.forEach(k=>{const t=Math.round(k.getBoundingClientRect().top/4);(byTop[t]=byTop[t]||[]).push(k)});
     const issues=[];const nineGrid=kids.length===9&&new Set(kids.map(k=>Math.round(k.getBoundingClientRect().top))).size===3;
     // the centre square of a nine grid may stand out on purpose (the Look 9 "core" cell)
     const cmp=nineGrid?kids.filter((k,i)=>i!==4):kids;const ttl=cmp.map(k=>{const h=k.querySelector('h2,h3,h4,strong,.nm,.t');return h?getComputedStyle(h).fontSize:null}).filter(Boolean);
     if(ttl.length===cmp.length&&new Set(ttl).size>1)issues.push('card titles in different sizes: '+[...new Set(ttl)].join(', '));
     const ic=cmp.map(k=>{const i=k.querySelector('img,svg');if(!i)return null;const r=i.getBoundingClientRect();return Math.round(r.width)+'x'+Math.round(r.height)}).filter(Boolean);
     if(ic.length===cmp.length&&new Set(ic).size>1)issues.push('icons in different sizes: '+[...new Set(ic)].join(', '));
     const bt=kids.map(k=>{const x=k.querySelector('.btn');return x?Math.round(x.getBoundingClientRect().height):null}).filter(Boolean);
     if(bt.length===kids.length&&new Set(bt).size>1)issues.push('buttons in different heights: '+[...new Set(bt)].join(', '));
     if(issues.length)res.sets.push({where:where(c),grid:name(c),issues})}}
   const fs=s=>{const e=document.querySelector(s);return e?getComputedStyle(e).fontSize:null};
   const ps=[...document.querySelectorAll('main p')].filter(vis).map(e=>getComputedStyle(e).fontSize);const mode=a=>{const c={};a.forEach(x=>c[x]=(c[x]||0)+1);return Object.keys(c).sort((x,y)=>c[y]-c[x])[0]||null};
   const h2=[...document.querySelectorAll('main h2')].filter(vis).map(e=>getComputedStyle(e).fontSize);
   res.type={h1:fs('main h1'),h2:mode(h2),h2Sizes:[...new Set(h2)],body:mode(ps)};
   return res},w);
  for(const o of r.orphans)page.orphans.push({width:w,...o});
  for(const n of r.nine){page.nine.push({width:w,...n});if(w===1440)site.nine.push({page:page.file,where:n.where,ratio:n.ratio})}
  for(const s of r.sets)page.sets.push({width:w,...s});
  page.type[w]=r.type;for(const k of ['h1','h2','body']){const key=k+'@'+w;(site.type[key]=site.type[key]||{});const v=r.type[k];if(v)(site.type[key][v]=site.type[key][v]||[]).push(page.file)}}
 // dedupe across widths
 const dd=a=>{const m=new Map();for(const x of a){const k=JSON.stringify({...x,width:0});if(m.has(k))m.get(k).width+=', '+x.width;else m.set(k,{...x,width:String(x.width)})}return [...m.values()]};
 page.orphans=dd(page.orphans);page.sets=dd(page.sets);page.nineIssues=dd(page.nine.filter(n=>n.issues.length).map(n=>({where:n.where,grid:n.grid,issues:n.issues,width:n.width})));
 page.nineCount=page.nine.filter(n=>n.width==1440).length;delete page.nine;
 page.pass=!page.orphans.length&&!page.nineIssues.length&&!page.sets.length;out.push(page);await ctx.close()}
const summary={};if(files.length>1){const ratios=site.nine.map(n=>n.ratio);const med=ratios.sort((a,b)=>a-b)[Math.floor(ratios.length/2)];
 summary.nineGapRatio={median:med,offBy10pct:site.nine.filter(n=>Math.abs(n.ratio-med)/med>0.1)};
 summary.typeRoles=Object.fromEntries(Object.entries(site.type).map(([k,v])=>[k,Object.fromEntries(Object.entries(v).map(([s,ps])=>[s,ps.length>6?ps.length+' pages':ps]))]))}
console.log(JSON.stringify({pages:out,summary},null,1));await b.close()})();
