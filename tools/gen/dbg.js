const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();console.log('launched');
const p=await b.newPage({viewport:{width:1440,height:900}});p.on('pageerror',e=>console.log('PE',e.message));
await p.goto('file:///home/claude/lb/pages/nine-stories.html');console.log('loaded');
const h=await p.evaluate(()=>document.body.scrollHeight);console.log('h',h);
await b.close()})().catch(e=>console.log('CATCH',e));
setTimeout(()=>console.log('timer alive'),20000);
