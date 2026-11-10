const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch();
 const out='/tmp/claude-0/-home-claude/560b35a6-e00c-5990-89dc-05dfaaa63f19/scratchpad/rev-c/';
 const pages=['nine-dynamics-365-sales','nine-customer-service','nine-dynamics-365'];
 const res={};
 for(const p of pages){for(const w of [390,1440]){
  const ctx=await b.newContext({viewport:{width:w,height:900},deviceScaleFactor:1});
  const pg=await ctx.newPage();
  await pg.goto('file:///home/claude/lb/pages/'+p+'.html',{waitUntil:'load'});
  // scroll to trigger reveals
  const h=await pg.evaluate(()=>document.documentElement.scrollHeight);
  for(let y=0;y<h;y+=600){await pg.evaluate(y=>window.scrollTo(0,y),y);await pg.waitForTimeout(120);}
  await pg.evaluate(()=>window.scrollTo(0,0));await pg.waitForTimeout(1500);
  await pg.screenshot({path:out+p+'-'+w+'.png',fullPage:true});
  await pg.screenshot({path:out+p+'-'+w+'-fold.png'});
  const info=await pg.evaluate(()=>{
   const r={height:document.documentElement.scrollHeight,sw:document.documentElement.scrollWidth};
   const btns=[...document.querySelectorAll('main a.btn, main button')].filter(e=>e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().height));
   r.minBtn=Math.min(...btns); r.btnsUnder48=btns.filter(x=>x<48).length;
   const h1=document.querySelector('h1'); r.h1px=getComputedStyle(h1).fontSize;
   const h2=document.querySelector('h2.h2'); r.h2px=h2?getComputedStyle(h2).fontSize:null;
   const book=[...document.querySelectorAll('a')].filter(a=>/schedule-a-meeting/.test(a.href)&&a.offsetParent);
   r.bookCount=book.length;
   r.bookAboveFold=book.filter(a=>a.getBoundingClientRect().top<900).length;
   r.telAboveFold=[...document.querySelectorAll('a[href^="tel:"]')].filter(a=>a.offsetParent&&a.getBoundingClientRect().top<900).length;
   const lead=document.querySelector('.hero .lead'); r.leadWords=lead?lead.textContent.trim().split(/\s+/).length:0;
   // cut-off / overflow text check
   r.overflow=[...document.querySelectorAll('main *')].filter(e=>e.offsetParent&&e.children.length===0&&e.scrollWidth>e.clientWidth+1&&getComputedStyle(e).overflowX!=='visible').slice(0,8).map(e=>e.className+':'+e.textContent.trim().slice(0,30));
   return r;});
  res[p+'-'+w]=info; await ctx.close();
 }}
 console.log(JSON.stringify(res,null,1)); await b.close();
})();
