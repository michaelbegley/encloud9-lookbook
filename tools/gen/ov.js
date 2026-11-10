const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const w of [320,390]){const p=await b.newPage({viewport:{width:w,height:900}});await p.goto('file://'+process.cwd()+'/wrapped.html');
const r=await p.evaluate(()=>[...document.querySelectorAll('.btn,.mailbtn,.ex-h1,.ex-h2,.face .big,.sw .use,h1')].map(e=>{const r=e.getBoundingClientRect(),pr=e.parentElement.getBoundingClientRect();return e.className+' "'+e.textContent.slice(0,20)+'" L'+Math.round(r.left)+' R'+Math.round(r.right)+' parentR'+Math.round(pr.right)+' sw'+e.scrollWidth+'/cw'+e.clientWidth}));
console.log(w,r.join('\n'));await p.close()}
await b.close()})();
