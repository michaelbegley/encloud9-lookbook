// usage: node check.js PAGE (without .html)
const { chromium } = require('playwright');
const page = process.argv[2];
(async () => {
  const b = await chromium.launch();
  for (const w of [1440, 390, 360]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 } });
    const p = await ctx.newPage();
    const errs = [];
    p.on('pageerror', e => errs.push('pageerror: ' + e.message));
    p.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
    p.on('requestfailed', r => { if (r.url().startsWith('file:')) errs.push('reqfail: ' + r.url()); });
    await p.goto('file:///home/claude/lb/pages/' + page + '.html');
    await p.waitForTimeout(400);
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < h; y += 500) { await p.evaluate(y => window.scrollTo({ top: y, behavior: 'instant' }), y); await p.waitForTimeout(120); }
    await p.waitForTimeout(5500);
    await p.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
    await p.waitForTimeout(500);
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    const wide = await p.evaluate((w) => [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > w + 1 && getComputedStyle(e).position !== 'fixed' && !e.closest('.tbl-wrap,#lbbar'); }).slice(0, 8).map(e => e.tagName + '.' + e.className + ' ' + Math.round(e.getBoundingClientRect().right)), w);
    console.log(page, w, 'scrollWidth', sw, sw === w ? 'OK' : 'FAIL', 'errors', errs.length, errs.join(' | '), wide.length ? 'WIDE: ' + wide.join(', ') : '');
    if (w !== 360) await p.screenshot({ path: `/home/claude/dec/shots/${page}-${w}.png`, fullPage: true });
    await ctx.close();
  }
  await b.close();
})();
