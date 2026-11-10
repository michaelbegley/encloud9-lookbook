// usage: node check.js page1 page2 ...  (names without .html) -> prints scrollWidth/errors, saves 1440 and 390 shots
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const pg of process.argv.slice(2)){for(const w of [1440,390,360]){
 const p=await b.newPage({viewport:{width:w,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file:///home/claude/lb/pages/'+pg+'.html');
 await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){window.scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,90))}window.scrollTo({top:0,behavior:'instant'})});
 await p.waitForTimeout(4500);
 const sw=await p.evaluate(()=>document.documentElement.scrollWidth);
 console.log(pg,w,'sw',sw,errs.length?'ERR '+JSON.stringify(errs):'ok');
 if(w!==360)await p.screenshot({path:`/home/claude/dec/shots/${pg}-${w}.png`,fullPage:true});
 await p.close();}}
await b.close()})();
