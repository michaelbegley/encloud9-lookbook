const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
  await p.goto('file:///home/claude/lb/pages/nine-about.html'); await p.waitForTimeout(500);
  const top = await p.evaluate(() => document.querySelector('[data-bel]').getBoundingClientRect().top + scrollY);
  await p.evaluate(y => scrollTo({top:y,behavior:'instant'}), top-350); await p.waitForTimeout(1200);
  await p.screenshot({path:'/home/claude/dec/shots/nine-about-1440-beliefs-mid.png'});
  const t = await p.evaluate(() => document.querySelector('#team').getBoundingClientRect().top + scrollY);
  await p.evaluate(y => scrollTo({top:y,behavior:'instant'}), t-100); await p.waitForTimeout(1200);
  await p.screenshot({path:'/home/claude/dec/shots/nine-about-1440-team.png'});
  await b.close();
})();
