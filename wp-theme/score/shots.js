// Screenshot every page of the mock and of a WordPress build, at 1440 and 390 px.
// usage: node shots.js <pages.json> <mockBase e.g. http://localhost:8081/site> <wpBase e.g. http://localhost:8080> <outDir>
// pages.json: [{old:"/mock/path/", path:"/new/path/"}...]  (wp-theme/content/pages.json works as is)
const { chromium } = require('playwright'); const fs = require('fs');
const [,, pj, mockBase, wpBase, out] = process.argv; fs.mkdirSync(out, { recursive: true });
const items = JSON.parse(fs.readFileSync(pj)).map(i => [i.old, i.path]);
(async () => {
  const b = await chromium.launch({ executablePath: '/usr/bin/google-chrome' }); const res = [];
  for (const w of [1440, 390]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 }, reducedMotion: 'reduce' });
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    for (const [old, nw] of items) {
      const name = (old.replace(/\//g, '_') || '_') + '-' + w;
      for (const [tag, url] of [['mock', mockBase + old], ['wp', wpBase + (nw === '/404/' ? '/no-such-page-test/' : nw)]]) {
        errs.length = 0; const r = await p.goto(url, { waitUntil: 'networkidle' }); await p.waitForTimeout(250);
        await p.screenshot({ path: `${out}/${name}-${tag}.png`, fullPage: true });
        const info = await p.evaluate(() => ({ h: document.documentElement.scrollHeight,
          broken: [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.getAttribute('src')),
          bytes: performance.getEntriesByType('resource').reduce((a, e) => a + (e.transferSize || 0), 0) }));
        res.push({ old, nw, w, tag, status: r.status(), ...info, errs: [...errs] });
      }
    }
    await p.close();
  }
  fs.writeFileSync(`${out}/shots.json`, JSON.stringify(res, null, 1)); await b.close();
})();
