const {chromium}=require('playwright');const path=require('path');(async()=>{const b=await chromium.launch();const p=await b.newPage();let bad=0;
for(const f of process.argv.slice(2)){await p.goto('file://'+path.resolve(f));const r=await p.evaluate(()=>[...document.querySelectorAll('[role="list"]')].filter(l=>![...l.children].some(c=>c.getAttribute('role')==='listitem'||c.tagName==='LI')).map(l=>l.tagName+'.'+l.className));if(r.length){bad++;console.log(path.basename(f),r.join(' | '))}}
console.log('pages with empty lists',bad);await b.close()})();
