const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const out={};
for(const w of [320,390,768,1440]){const p=await b.newPage({viewport:{width:w,height:900},deviceScaleFactor:1});
p.on('requestfailed',r=>{out.failed=(out.failed||new Set());out.failed.add(r.url().slice(0,70))});
await p.goto('file://'+process.cwd()+'/wrapped.html');await p.waitForTimeout(1500);
const r=await p.evaluate(()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,h:document.documentElement.scrollHeight,
fontOK:document.fonts.check('16px "Hanken Grotesk"'),
wide:[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>document.documentElement.clientWidth+0.5).map(e=>e.className+':'+Math.round(e.getBoundingClientRect().right)).slice(0,8),
h1:getComputedStyle(document.querySelector('h1')).fontFamily}));
out[w]=r; if(w===390||w===1440) await p.screenshot({path:`s${w}.png`,fullPage:true});
if(w===390) await p.screenshot({path:'s390-first.png'});
if(w===1440) await p.screenshot({path:'s1440-first.png'});
await p.close()}
// text scan
const p=await b.newPage();await p.goto('file://'+process.cwd()+'/wrapped.html');
const t=await p.evaluate(()=>document.body.innerText);
out.dash=[...t].filter(c=>c==='—'||c==='–').length;
out.links=await p.evaluate(()=>[...document.querySelectorAll('a')].map(a=>a.textContent.trim()+' -> '+a.getAttribute('href')));
// click swatch test
await p.click('#scale button:nth-child(5)');await p.waitForTimeout(200);out.toast=await p.textContent('#toast');
out.failed=out.failed?[...out.failed]:[];
require('fs').writeFileSync('text.txt',t);
console.log(JSON.stringify(out,null,1));await b.close()})();
