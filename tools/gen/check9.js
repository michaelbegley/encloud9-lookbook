// usage: node check9.js page-basename   (e.g. nine-packages)
const { chromium } = require('playwright');
const page_ = process.argv[2];
const url = 'file:///home/claude/lb/pages/' + page_ + '.html';
(async () => {
  const b = await chromium.launch();
  for (const w of [1440, 390, 360]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1 });
    const p = await ctx.newPage();
    const errs = [];
    p.on('pageerror', e => errs.push('pageerror: ' + e.message));
    p.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
    p.on('requestfailed', r => errs.push('reqfail: ' + r.url()));
    await p.goto(url, { waitUntil: 'load' });
    const H = await p.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < H; y += 600) { await p.evaluate(y => window.scrollTo({ top: y, behavior: 'instant' }), y); await p.waitForTimeout(120); }
    await p.waitForTimeout(1500);
    await p.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
    await p.waitForTimeout(400);
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    // overflowing text inside cubes / cards
    const over = await p.evaluate(() => [...document.querySelectorAll('.cell .nm,.dest .nm,.pk .h3,.sp-scale .pr,.st .h3,.chips button,.cell .lab')].filter(e => e.scrollWidth > e.clientWidth + 1 || (e.getBoundingClientRect().right > e.parentElement.getBoundingClientRect().right + 1)).map(e => e.textContent.trim().slice(0, 40)));
    // wider-than-viewport elements
    const wide = await p.evaluate((w) => [...document.querySelectorAll('main *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > w + 1 && getComputedStyle(e).position !== 'fixed' && !e.closest('.tbl-wrap'); }).slice(0, 8).map(e => e.tagName + '.' + e.className + ' ' + Math.round(e.getBoundingClientRect().right)), w);
    console.log(`w=${w} scrollWidth=${sw} ${sw === w ? 'OK' : 'FAIL'} errors=${errs.length} ${errs.join(' | ')}`);
    if (over.length) console.log('  overflow text:', JSON.stringify(over));
    if (wide.length) console.log('  wide:', JSON.stringify(wide));
    if (w !== 360) await p.screenshot({ path: `/home/claude/dec/shots/${page_}-${w}.png`, fullPage: true });
    await ctx.close();
  }
  await b.close();
})();
