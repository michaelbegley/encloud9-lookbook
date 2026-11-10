const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file:///home/claude/lb/pages/nine-dynamics-365.html');await p.waitForTimeout(2500);
for(const i of [0,4,8]){await p.locator('.pk .cell').nth(i).click();await p.waitForTimeout(300);console.log(i,await p.evaluate(()=>document.querySelector('#pick-d .pd.on').getAttribute('data-k')))}
await p.locator('.pk .cell').nth(0).focus();await p.keyboard.press('ArrowRight');console.log('key',await p.evaluate(()=>document.activeElement.getAttribute('data-k')));
await p.locator('.faq summary').first().click();console.log('errs',errs);await b.close()})();
