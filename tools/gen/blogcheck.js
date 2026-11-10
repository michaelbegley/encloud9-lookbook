const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const pg of ['nine-blog','nine-blog-post']){for(const font of ['','?font=jakarta']){for(const w of [1440,390,360]){
 const p=await b.newPage({viewport:{width:w,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file:///home/claude/lb/pages/'+pg+'.html'+font);
 await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){window.scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,80))}window.scrollTo({top:0,behavior:'instant'})});
 await p.waitForTimeout(2500);
 const sw=await p.evaluate(()=>document.documentElement.scrollWidth);
 // overflow inside cubes: any child whose scrollHeight > clientHeight or scrollWidth > clientWidth
 const clip=await p.evaluate(()=>[...document.querySelectorAll('.use,.fc,.pc,.ptile,.chip')].filter(e=>e.scrollWidth>e.clientWidth+1||e.scrollHeight>e.clientHeight+1).map(e=>e.className+':'+e.textContent.slice(0,30)));
 console.log(pg,font||'hanken',w,'sw',sw,errs.length?'ERR '+JSON.stringify(errs):'ok','clip',JSON.stringify(clip));
 if(w!==360&&!font)await p.screenshot({path:`/home/claude/dec/shots/blog-${pg.replace('nine-','')}-${w}.png`,fullPage:true});
 if(w===1440&&font)await p.screenshot({path:`/home/claude/dec/shots/blog-${pg.replace('nine-','')}-jakarta-${w}.png`,fullPage:true});
 await p.close();}}}
await b.close()})();
