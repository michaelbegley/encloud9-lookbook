const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const w of [1440, 390]) {
    const p = await (await b.newContext({ viewport: { width: w, height: 1000 } })).newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto('file:///home/claude/lb/pages/nine-copilot.html');
    await p.waitForTimeout(3000);
    const hero = await p.evaluate(() => [...document.querySelectorAll('.cc')].map(c => c.classList.contains('on') ? 1 : 0).join(''));
    await p.locator('[data-gx]').scrollIntoViewIfNeeded(); await p.waitForTimeout(800);
    const typingMid = await p.evaluate(() => document.querySelector('[data-q]').textContent.length);
    await p.click('[data-pick="b"]'); await p.waitForTimeout(800);
    await p.click('[data-pick="c"]'); await p.waitForTimeout(4500);
    const q = await p.evaluate(() => document.querySelector('[data-q]').textContent);
    const vis = await p.evaluate(() => [...document.querySelectorAll('[data-sc="c"] .pt')].every(x => x.classList.contains('in')));
    const boxes = p.locator('[data-sc="c"] input');
    await boxes.nth(0).check(); await boxes.nth(2).check();
    const sel = await p.textContent('[data-apn]');
    await p.click('[data-apgo]'); await p.waitForTimeout(300);
    const st = await p.evaluate(() => [...document.querySelectorAll('[data-st]')].map(x => x.textContent).join('|'));
    const wait = await p.textContent('[data-apw]');
    console.log(w, 'hero lit', hero, 'typing len mid', typingMid, 'C request ok', q.startsWith('List the quotes'), 'parts in', vis, sel, st, 'waiting', wait, 'errors', errs.length);
    await p.locator('.gx-win').screenshot({ path: `/home/claude/dec/shots/nine-copilot-${w}-approvals.png` });
    await p.click('[data-pick="b"]'); await p.waitForTimeout(4500);
    await p.locator('.gx-win').screenshot({ path: `/home/claude/dec/shots/nine-copilot-${w}-opp.png` });
  }
  // reduced motion
  const p = await (await b.newContext({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' })).newPage();
  await p.goto('file:///home/claude/lb/pages/nine-copilot.html'); await p.waitForTimeout(300);
  const r = await p.evaluate(() => ({ seq: document.querySelector('.cgrid').classList.contains('seq'), q: document.querySelector('[data-q]').textContent.length }));
  await p.click('[data-pick="c"]'); await p.waitForTimeout(100);
  const r2 = await p.evaluate(() => ({ building: document.querySelector('[data-gx]').classList.contains('building'), q: document.querySelector('[data-q]').textContent.slice(0, 20) }));
  console.log('reduced', JSON.stringify(r), JSON.stringify(r2));
  await b.close();
})();
