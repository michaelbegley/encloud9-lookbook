const {chromium}=require('playwright');
(async()=>{
const b=await chromium.launch();
const url='file:///home/claude/lb/pages/nine-story-hogan.html';
for(const w of [320,360,390,768,1024,1440,1920]){
 const p=await b.newPage({viewport:{width:w,height:900},reducedMotion:'reduce'});
 const errs=[];p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});p.on('requestfailed',r=>errs.push('FAIL '+r.url()));
 await p.goto(url);await p.waitForTimeout(400);
 const r=await p.evaluate(()=>{
  const sw=document.documentElement.scrollWidth, cw=document.documentElement.clientWidth;
  const over=[...document.querySelectorAll('body *')].filter(e=>{const b=e.getBoundingClientRect();return b.right>cw+1&&b.width>0&&getComputedStyle(e).position!=='fixed'}).slice(0,5).map(e=>e.tagName+'.'+e.className+':'+Math.round(e.getBoundingClientRect().right));
  const lead=document.querySelector('.lead');const lb=lead.getBoundingClientRect();
  const h1=document.querySelector('h1').getBoundingClientRect();
  return {sw,cw,over,leadBottom:Math.round(lb.bottom+scrollY),h1h:Math.round(h1.height),docH:document.documentElement.scrollHeight,
   firstBook:Math.round([...document.querySelectorAll('a')].filter(a=>/Book a call/.test(a.textContent)&&a.offsetParent).map(a=>a.getBoundingClientRect().top)[0]||-1)};
 });
 console.log(w,JSON.stringify(r),errs.join(' | '));
 if([360,390,1440].includes(w)) await p.screenshot({path:`s${w}.png`,fullPage:true});
 if([390,1440].includes(w)) await p.screenshot({path:`f${w}.png`});
 await p.close();
}
const p=await b.newPage({viewport:{width:1440,height:900}});await p.goto(url);
const d=await p.evaluate(()=>{
 const txt=document.body.innerText;
 const lead=document.querySelector('.lead').innerText;
 const ld=[...document.querySelectorAll('script[type="application/ld+json"]')].map(s=>{try{JSON.parse(s.textContent);return 'ok'}catch(e){return 'ERR '+e.message}});
 const links=[...document.querySelectorAll('a')].map(a=>a.getAttribute('href'));
 return {dash:(txt.match(/[–—]/g)||[]).length, brackets:txt.match(/\[[^\]]*\]/g), leadWords:lead.split(/\s+/).filter(Boolean).length,
  h1:document.querySelectorAll('h1').length, h2:[...document.querySelectorAll('h2')].map(h=>h.innerText), book:[...document.querySelectorAll('a')].filter(a=>/Book a call/.test(a.textContent)).length,
  hashLinks:links.filter(h=>!h||h==='#'), bc:/Business Central/i.test(txt), written:/written up/i.test(txt), partner:txt.match(/Microsoft partner/g), ld, imgs:[...document.images].map(i=>i.src.split('/').pop()+':'+i.naturalWidth),
  brits:txt.match(/\b\w+(isation|ise|ised|our)\b/g), links:[...new Set(links)]};
});
console.log(JSON.stringify(d,null,1));
await b.close();})();
