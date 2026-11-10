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
  const vis=[...document.body.innerText.matchAll(/\[[^\]\n]{1,100}\]/g)].map(m=>m[0]);
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
 // ---- added 9 Nov 2026 (standard checks G11 to G14 and the keyboard walk in area 7) ----
 const repo=path.resolve(path.dirname(file),'..');const base=path.basename(file);
 const meta=n=>(html.match(new RegExp('<meta (?:property|name)="'+n+'" content="([^"]*)"'))||[])[1]||'';
 const canon=(html.match(/<link rel="canonical" href="([^"]*)"/)||[])[1]||'';
 // G11 share and find: preview tags, canonical, in sitemap, linked from another page (404 exempt)
 if(base==='nine-404.html'){out.gates.G11={pass:true,exempt:'404 page'}}else{
  let sm='';try{sm=fs.readFileSync(path.join(repo,'site','sitemap.xml'),'utf8')}catch(e){}
  const legal=/nine-(privacy|accessibility|terms)\.html/.test(base);
  const live=canon.replace('https://www.encloud9.com','');
  const inbound=fs.readdirSync(path.dirname(file)).filter(f=>/^nine-.*\.html$/.test(f)&&f!==base&&f!=='nine-faq.html').filter(f=>{const s=fs.readFileSync(path.join(path.dirname(file),f),'utf8');return s.includes('href="'+base)||(canon&&s.includes('href="'+canon))});
  const tags={canonical:!!canon,'og:title':!!meta('og:title'),'og:description':!!meta('og:description'),'og:image':!!meta('og:image'),'og:url':!!meta('og:url'),'twitter:card':!!meta('twitter:card')};
  const inSitemap=legal?'legal page, kept out until approved':sm.includes('<loc>'+canon+'</loc>');
  out.gates.G11={pass:Object.values(tags).every(Boolean)&&(legal||inSitemap===true)&&inbound.length>0,tags,inSitemap,inboundCount:inbound.length,inboundSample:inbound.slice(0,5)}}
 // G12 images: alt on every img, a row in assets/IMAGE-SOURCES.csv with a known licence, 300 KB or less
 let man='';try{man=fs.readFileSync(path.join(repo,'assets','IMAGE-SOURCES.csv'),'utf8')}catch(e){}
 const rows=man.split('\n').slice(1).filter(Boolean).map(l=>{const c=l.split(',');return {pat:c[0],licence:c[3]||''}});
 const match=u=>rows.find(r=>r.pat.includes('*')?new RegExp('^'+r.pat.replace(/[.+?^${}()|[\]\\]/g,'\\$&').replace(/\*/g,'.*')+'$').test(u):r.pat===u);
 const q2=await (await b.newContext({viewport:{width:1440,height:900}})).newPage();await q2.goto('file://'+file);await q2.waitForTimeout(400);
 const imgs=await q2.evaluate(()=>{const o=[];document.querySelectorAll('img').forEach(i=>o.push({src:i.getAttribute('src'),alt:i.hasAttribute('alt')?i.getAttribute('alt'):null,inLink:!!i.closest('a,button')}));
  document.querySelectorAll('body *').forEach(e=>{const bg=getComputedStyle(e).backgroundImage;const m=bg&&bg.match(/url\("?([^")]+)"?\)/);if(m)o.push({src:m[1],css:true})});return o});
 const imgRes=[];const seen=new Set();for(const im of imgs){const u0=im.src||'';let u=u0.startsWith('file://')?path.relative(repo,decodeURI(u0.slice(7))):u0.replace(/^\.\.\//,'');
  if(u.startsWith('data:'))continue;const key=u+(im.css?'#css':'')+(im.alt===null?'#noalt':'');if(seen.has(key))continue;seen.add(key);
  let kb=null;if(!/^https?:/.test(u)){try{kb=Math.round(fs.statSync(path.join(repo,u)).size/1024)}catch(e){kb='missing'}}
  const r=match(u);const lic=r?r.licence:'';const issues=[];
  if(!im.css&&im.alt===null)issues.push('no alt');if(!im.css&&im.inLink&&im.alt==='')issues.push('empty alt inside a link');
  if(!r)issues.push('not in IMAGE-SOURCES.csv');else if(/could not determine/i.test(lic))issues.push('licence unknown');
  if(kb==='missing')issues.push('file missing');else if(kb!==null&&kb>300)issues.push(kb+' KB, over 300');
  imgRes.push({src:u,kb,issues})}
 out.gates.G12={pass:imgRes.every(r=>!r.issues.length),problems:imgRes.filter(r=>r.issues.length),count:imgRes.length};
 // G13 outside links: listed here, opened by Claude's web fetch on review day (the shell cannot reach outside sites)
 const ext=[...new Set([...html.replace(/<nav id="lbbar".*?<\/nav>/s,'').matchAll(/href="(https?:\/\/[^"#]+)/g)].map(m=>m[1]).filter(u=>!u.startsWith('https://www.encloud9.com')))];
 out.gates.G13={pass:null,note:'open each with web fetch',outside:ext};
 // G14 spelling and Microsoft product names
 const sp=JSON.parse(require('child_process').execFileSync('python3',[path.join(__dirname,'spell.py'),file]).toString());
 out.gates.G14={pass:!sp.unknown.length&&!sp.names.length,unknown:sp.unknown,wrongNames:sp.names};
 // Area 7 keyboard walk at 1440: Tab through the page; every stop visible, no trap, reaches the footer
 const kb=await q2.evaluate(()=>{document.activeElement&&document.activeElement.blur();return document.querySelectorAll('a[href],button,input,select,textarea,summary,[tabindex]:not([tabindex="-1"])').length});
 const stops=[];let invisible=[];let reachedFooter=false;let trap=false;
 for(let i=0;i<Math.min(kb+20,600);i++){await q2.keyboard.press('Tab');const s=await q2.evaluate(()=>{const e=document.activeElement;if(!e||e===document.body)return null;const cs=getComputedStyle(e);const r=e.getBoundingClientRect();
   const shown=(cs.outlineStyle!=='none'&&parseFloat(cs.outlineWidth)>0)||cs.boxShadow!=='none';if(!e.dataset.kbi)e.dataset.kbi=String(document.querySelectorAll('[data-kbi]').length);return {id:e.dataset.kbi+' '+e.tagName+':'+(e.textContent||e.getAttribute('aria-label')||'').trim().slice(0,30),shown,size:r.width*r.height,footer:!!e.closest('footer')}});
  if(!s)break;if(stops.length&&stops[stops.length-1]===s.id){trap=true;break}if(stops.includes(s.id)&&stops.indexOf(s.id)===0)break;stops.push(s.id);if(!s.shown&&s.size>0)invisible.push(s.id);if(s.footer)reachedFooter=true}
 out.area7_keyboard={stops:stops.length,reachedFooter,trap,noVisibleFocus:invisible.slice(0,8),noVisibleFocusCount:invisible.length};
 console.log(JSON.stringify(out,null,1));await b.close()})();
