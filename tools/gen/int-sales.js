const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file:///home/claude/lb/pages/nine-dynamics-365-sales.html');await p.waitForTimeout(2500);
await p.locator('.lic .cell').nth(1).hover();await p.waitForTimeout(900);
console.log('lic hover',await p.evaluate(()=>[...document.querySelectorAll('.lic .cell')].map(e=>getComputedStyle(e).transform.slice(0,40))));
await p.locator('.lic .cell').nth(1).click();await p.waitForTimeout(800);console.log('hash',await p.evaluate(()=>location.hash));
const qs=p.locator('.rc .q');await qs.nth(0).scrollIntoViewIfNeeded();
for(const [i,v] of [[0,'y'],[1,'n'],[2,'u'],[3,'y'],[4,'y']]){await qs.nth(i).locator(`button[data-v="${v}"]`).click();}
await p.waitForTimeout(700);
console.log(await p.evaluate(()=>({count:document.querySelector('[data-count]').textContent,score:document.querySelector('[data-score]').textContent,note:document.querySelector('[data-note]').textContent,meter:[...document.querySelectorAll('.meter i')].map(i=>i.className)})));
await p.locator('.rc').screenshot({path:'rc1.png'});
for(const i of [1,2]){await qs.nth(i).locator('button[data-v="y"]').click();}
await p.waitForTimeout(700);
console.log(await p.evaluate(()=>({note:document.querySelector('[data-note]').textContent,all:document.querySelector('.meter').className})));
await p.locator('.rc').screenshot({path:'rc2.png'});
await p.locator('.faq summary').first().click();await p.waitForTimeout(600);console.log('faq open',await p.evaluate(()=>document.querySelector('.faq details').open));
await p.locator('.ptiles .ptile').nth(1).hover();await p.waitForTimeout(600);console.log('ptile',await p.evaluate(()=>getComputedStyle(document.querySelectorAll('.ptile')[1]).transform));
console.log('errs',errs);await b.close()})();
