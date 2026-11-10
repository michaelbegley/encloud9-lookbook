const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
const base='http://localhost:8765/site/';const seen=new Set(),queue=[base],bad=[];let n=0;
const fails=[];p.on('response',r=>{if(r.status()>=400&&r.url().startsWith('http://localhost'))fails.push(r.status()+' '+r.url())});
while(queue.length){const u=queue.shift();if(seen.has(u))continue;seen.add(u);const r=await p.goto(u);n++;
 if(!r||r.status()>=400){bad.push(u+' '+(r&&r.status()));continue}
 const info=await p.evaluate(()=>({css:getComputedStyle(document.body).fontFamily,lb:!!document.getElementById('lbbar'),imgs:[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src),links:[...document.querySelectorAll('a[href]')].map(a=>a.href)}));
 if(!/Hanken/.test(info.css))bad.push('NO CSS '+u+' '+info.css);if(info.lb)bad.push('LBBAR '+u);if(info.imgs.length)bad.push('IMG '+u+' '+info.imgs.join(','));
 for(const l of info.links){const x=l.split('#')[0];if(x.startsWith('http://localhost:8765/')&&!seen.has(x))queue.push(x)}}
console.log('pages',n,'bad',JSON.stringify(bad.slice(0,20)),'404s',JSON.stringify([...new Set(fails)].slice(0,20)));await b.close()})();
