const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
(async()=>{const f=process.argv[2],name=process.argv[3];const b=await chromium.launch();
for(const w of [1440,390,360]){const p=await b.newPage({viewport:{width:w,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push('console:'+m.text())});
await p.goto('file://'+f);await p.waitForTimeout(400);
await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,60))}window.scrollTo(0,0)});await p.waitForTimeout(800);
const r=await p.evaluate(()=>{const ids=new Set([...document.querySelectorAll('[id]')].map(e=>e.id));const bad=[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href').slice(1)).filter(h=>h&&!ids.has(h));const rel=[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href')).filter(h=>!/^(https?:|tel:|mailto:|#)/.test(h));
const wide=[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.right>document.documentElement.clientWidth+1&&r.width>0}).slice(0,5).map(e=>e.tagName+'.'+e.className);
return{sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,badAnchors:bad,rel:[...new Set(rel)],wide,h1:document.querySelectorAll('h1').length,edges:[...new Set([...document.querySelectorAll('main section.sec')].map(e=>Math.round(e.getBoundingClientRect().left)))]}});
const relMissing=r.rel.filter(h=>!fs.existsSync(path.join(path.dirname(f),h.split('#')[0])));
if(r.edges.length>1)errs.push('SECTION EDGES DIFFER '+r.edges);console.log(w,JSON.stringify({sw:r.sw,edges:r.edges,cw:r.cw,badAnchors:r.badAnchors,relMissing,wide:r.wide,h1:r.h1,errs}));
if(w!==360)await p.screenshot({path:`/home/claude/dec/shots/${name}-${w}.png`,fullPage:true});await p.close()}
await b.close()})();
