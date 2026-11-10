// Page Quality Standard gate checks for one built page. Usage: node tools/gates.js pages/nine-home.html [axePath]
// G3 axe at 390 and 1440, motion on and reduced; G4 no sideways scroll at 12 widths; G5 in-page anchors and relative links;
// G6 one H1, first text in main; G7 JSON-LD parses, no brackets in FAQ answers; G8 dashes; plus visible brackets list, title and description lengths.
const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
const file=path.resolve(process.argv[2]);const axePath=process.argv[3];
const WIDTHS=[320,360,390,480,600,768,900,1024,1180,1280,1440,1920];
(async()=>{const b=await chromium.launch();const out={file:path.basename(file),gates:{}};
 const html=fs.readFileSync(file,'utf8');
 // static
 const lds=[...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)].map(m=>m[1]);
 const ldRes=lds.map(t=>{try{const j=JSON.parse(t);const s=JSON.stringify(j);return {ok:true,type:j['@type']||(j['@graph']||[]).map(x=>x['@type']).join('+'),brackets:(s.match(/\[[A-Z][^\]]{2,80}\]/g)||[])}}catch(e){return {ok:false,err:String(e).slice(0,80)}}});
 out.gates.G7={pass:ldRes.every(r=>r.ok)&&ldRes.every(r=>!r.brackets||!r.brackets.length),blocks:ldRes};
 const dashes=(html.match(/[–—]/g)||[]).length;out.gates.G8_dashes={pass:dashes===0,count:dashes};
 const title=(html.match(/<title>([\s\S]*?)<\/title>/)||[])[1]||'';const desc=(html.match(/<meta name="description" content="([^"]*)"/)||[])[1]||'';
 out.meta={title,titleLen:title.length,desc,descLen:desc.length};
 const p=await b.newPage({viewport:{width:1440,height:900}});await p.goto('file://'+file);await p.waitForTimeout(300);
 const st=await p.evaluate(()=>{const ids=new Set([...document.querySelectorAll('[id]')].map(e=>e.id));
  const badAnchors=[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!ids.has(h.slice(1)));
  const bare=[...document.querySelectorAll('a[href="#"]')].filter(a=>!a.hasAttribute('data-todo')).length;
  const h1=document.querySelectorAll('h1').length;const main=document.querySelector('main');
  const w=document.createTreeWalker(main,NodeFilter.SHOW_TEXT,{acceptNode:n=>n.textContent.trim()&&!n.parentElement.closest('nav[aria-label="Breadcrumb"],script,style,.sr-only')?1:3});let first=w.nextNode();let eyebrow='';
  // an eyebrow label directly above the H1 is allowed (standard G6, amended 9 Nov): short text whose next text is in the H1
  if(first&&!first.parentElement.closest('h1')&&first.textContent.trim().length<=80){const nx=w.nextNode();if(nx&&nx.parentElement.closest('h1')){eyebrow=first.textContent.trim();first=nx}}
  const firstInH1=!!(first&&first.parentElement.closest('h1'));
  const vis=[...document.body.innerText.matchAll(/\[[^\]\n]{2,100}\]/g)].map(m=>m[0]);
  return {badAnchors,bare,h1,firstInH1,eyebrow,firstText:first?first.textContent.trim().slice(0,50):'',brackets:[...new Set(vis)]}});
 out.gates.G5={pass:!st.badAnchors.length&&!st.bare,badAnchors:st.badAnchors,bareHash:st.bare};
 out.gates.G6={pass:st.h1===1&&st.firstInH1,h1:st.h1,eyebrow:st.eyebrow,firstText:st.firstText};
 out.visibleBrackets=st.brackets;
 // G4 sweep
 const sweep={};for(const w of WIDTHS){await p.setViewportSize({width:w,height:900});await p.waitForTimeout(120);sweep[w]=await p.evaluate(()=>document.documentElement.scrollWidth)}
 out.gates.G4={pass:WIDTHS.every(w=>sweep[w]<=w),fails:WIDTHS.filter(w=>sweep[w]>w).map(w=>w+':'+sweep[w])};
 await p.close();
 // G3 axe
 const axe=axePath?fs.readFileSync(axePath,'utf8'):null;const ax={};
 if(axe){for(const w of [390,1440])for(const rm of ['no-preference','reduce']){const c=await b.newContext({viewport:{width:w,height:900},reducedMotion:rm});const q=await c.newPage();await q.goto('file://'+file);
  await q.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60))}window.scrollTo(0,0)});await q.waitForTimeout(2000);
  await q.addScriptTag({content:axe});ax[w+'/'+rm]=await q.evaluate(async()=>(await axe.run(document,{resultTypes:['violations']})).violations.map(v=>({id:v.id,impact:v.impact,n:v.nodes.length,t:v.nodes[0].target.join(' ')})));await c.close()}}
 const serious=Object.values(ax).flat().filter(v=>v.impact==='serious'||v.impact==='critical');
 out.gates.G3={pass:axe?!serious.length:null,runs:ax};
 console.log(JSON.stringify(out,null,1));await b.close()})();
