const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
  await p.goto('file:///home/claude/lb/pages/nine-about.html'); await p.waitForTimeout(500);
  const top = await p.evaluate(() => document.querySelector('[data-bel]').getBoundingClientRect().top + scrollY);
  const res=[];
  for (const off of [-700,-400,-100,300,800]) { await p.evaluate(y => scrollTo({top:y,behavior:'instant'}), top+off); await p.waitForTimeout(250); res.push(await p.textContent('[data-beln]')); }
  await p.evaluate(y => scrollTo({top:y,behavior:'instant'}), top-400); 
  console.log(res.join(' / '));
  await p.evaluate(y => scrollTo({top:y,behavior:'instant'}), top-150);
  await p.screenshot({path:'/home/claude/dec/shots/nine-about-1440-beliefs-later.png'});
  await b.close();
})();
