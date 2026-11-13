// Accessibility and speed pass (added by Agent 6; the parity scorecard in wp-theme/score is unchanged).
// usage: node a11y.js <pages.json> <wpBase> <out.json> [path to axe.min.js] [mockBase, to score the mock the same way]
// Per page at 1440 and 390 px: axe-core with the WCAG 2.0, 2.1 and 2.2 A and AA rule sets (includes target size 24 px),
// landmark checks (one main, footer outside main, skip link works), focus not hidden under the sticky header,
// the header menu by keyboard (opens on Enter, Escape closes and returns focus), and lab numbers for speed
// (largest paint, layout shift, requests, bytes, lazy-loaded image on the first screen).
const { chromium } = require('playwright'); const fs = require('fs');
const [,, pj, base, outFile, axePath, mockBase] = process.argv;
const axeSrc = axePath && fs.existsSync(axePath) ? fs.readFileSync(axePath, 'utf8') : null;
const items = JSON.parse(fs.readFileSync(pj)).map(i => [i.old, i.path]);
const med = a => { const s = [...a].sort((x, y) => x - y); return s.length ? s[Math.floor(s.length / 2)] : null; };

async function onePage(p, url, w) {
  await p.addInitScript(() => {
    window.__lcp = 0; window.__cls = 0;
    try {
      new PerformanceObserver(l => { for (const e of l.getEntries()) window.__lcp = e.startTime; }).observe({ type: 'largest-contentful-paint', buffered: true });
      new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) window.__cls += e.value; }).observe({ type: 'layout-shift', buffered: true });
    } catch (e) {}
  });
  const r = await p.goto(url, { waitUntil: 'networkidle' });
  await p.waitForTimeout(300);
  const out = { status: r.status() };
  out.perf = await p.evaluate(() => {
    const res = performance.getEntriesByType('resource');
    const vh = innerHeight;
    return { lcp_ms: Math.round(window.__lcp), cls: +window.__cls.toFixed(4), requests: res.length + 1,
      bytes: res.reduce((a, e) => a + (e.transferSize || 0), 0) + (performance.getEntriesByType('navigation')[0] || {}).transferSize,
      blocking: res.filter(e => e.renderBlockingStatus === 'blocking').length,
      dom: document.getElementsByTagName('*').length,
      lazyAboveFold: [...document.images].filter(i => i.loading === 'lazy' && i.getBoundingClientRect().top < vh).length };
  });
  out.landmarks = await p.evaluate(() => {
    const main = document.querySelectorAll('main'), skip = document.querySelector('a.skip, a.skip-link, a[href="#main"]');
    const first = [...document.querySelectorAll('a[href],button,input,select,textarea,[tabindex]')].find(e => e.tabIndex >= 0 && !e.closest('[hidden]'));
    return { mains: main.length, footerInMain: !!document.querySelector('main footer.foot, main [role=contentinfo]'),
      footerLandmarks: [...document.querySelectorAll('footer')].filter(f => !f.closest('article,aside,main,nav,section')).length,
      headerInMain: !!document.querySelector('main header.top'), skipIsFirst: !!skip && first === skip,
      skipTarget: !!skip && !!document.querySelector(skip.getAttribute('href')), h1: document.querySelectorAll('h1').length,
      scrollPadding: parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop) || 0,
      headerBottom: (() => { const h = document.querySelector('header.top'); return h && getComputedStyle(h).position === 'sticky' ? Math.round(h.getBoundingClientRect().height) : 0; })() };
  });
  // focus not hidden: tab through the first 40 stops; a focused element must not sit under the sticky header
  out.focusHidden = 0;
  await p.evaluate(() => { document.documentElement.style.scrollBehavior = 'auto'; window.scrollTo(0, 600); });   // instant scrolling, so positions are final when read
  for (let i = 0; i < 40; i++) {
    await p.keyboard.press('Tab');
    const hid = await p.evaluate(() => {
      const a = document.activeElement, h = document.querySelector('header.top');
      if (!a || a === document.body || !h || h.contains(a) || getComputedStyle(h).position !== 'sticky') return false;
      const r = a.getBoundingClientRect(), hb = h.getBoundingClientRect().bottom;
      return r.height > 0 && r.bottom <= hb && r.bottom > 0;
    });
    if (hid) out.focusHidden++;
  }
  if (w >= 1000) {
    out.menu = await p.evaluate(async () => {
      const b = document.querySelector('.nav-x'); if (!b) return null;
      window.scrollTo(0, 0); b.focus();
      const panel = document.getElementById(b.getAttribute('aria-controls'));
      const hoverOpens = !panel.hidden;
      b.click(); const opened = b.getAttribute('aria-expanded') === 'true' && !panel.hidden;
      document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
      return { hoverOpens, opened, escCloses: panel.hidden && b.getAttribute('aria-expanded') === 'false', focusBack: document.activeElement === b };
    });
  }
  if (axeSrc) {
    await p.evaluate(axeSrc);
    const ax = await p.evaluate(async () => {
      const r = await axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] }, resultTypes: ['violations'] });
      return r.violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, sample: v.nodes[0] && v.nodes[0].target.join(' ').slice(0, 120) }));
    });
    out.axe = ax;
  }
  return out;
}

(async () => {
  const b = await chromium.launch({ executablePath: '/usr/bin/google-chrome' }); const rows = [];
  for (const [tag, root] of [['wp', base]].concat(mockBase ? [['mock', mockBase]] : [])) {
    for (const w of [1440, 390]) {
      for (const [old, nw] of items) {
        if (nw === '/404/') continue;
        const ctx = await b.newContext({ viewport: { width: w, height: 900 }, reducedMotion: 'reduce' });
        const p = await ctx.newPage();
        try { rows.push(Object.assign({ tag, old, path: nw, w }, await onePage(p, root + (tag === 'wp' ? nw : old), w))); }
        catch (e) { rows.push({ tag, old, path: nw, w, error: String(e).slice(0, 200) }); }
        await ctx.close();
      }
    }
  }
  await b.close();
  const sum = {};
  for (const tag of [...new Set(rows.map(r => r.tag))]) {
    const R = rows.filter(r => r.tag === tag && !r.error), rules = {};
    R.forEach(r => (r.axe || []).forEach(v => { const k = v.id; rules[k] = rules[k] || { impact: v.impact, pages: 0, nodes: 0, sample: r.path + ' ' + v.sample }; rules[k].pages++; rules[k].nodes += v.nodes; }));
    sum[tag] = {
      page_views_checked: R.length, errors: rows.filter(r => r.tag === tag && r.error).length,
      axe_ran: !!axeSrc, axe_page_views_with_violations: R.filter(r => (r.axe || []).length).length, axe_rules: rules,
      footer_inside_main: R.filter(r => r.landmarks.footerInMain).length, pages_without_exactly_one_main: R.filter(r => r.landmarks.mains !== 1).length,
      pages_without_footer_landmark: R.filter(r => r.landmarks.footerLandmarks < 1).length,
      skip_link_not_first_or_broken: R.filter(r => !r.landmarks.skipIsFirst || !r.landmarks.skipTarget).length,
      pages_without_exactly_one_h1: R.filter(r => r.landmarks.h1 !== 1).map(r => r.path + '@' + r.w),
      scroll_padding_less_than_header: R.filter(r => r.landmarks.headerBottom && r.landmarks.scrollPadding < r.landmarks.headerBottom).length,
      focus_hidden_under_header_stops: R.reduce((a, r) => a + r.focusHidden, 0),
      menu_keyboard_fail: R.filter(r => r.menu && !(r.menu.opened && r.menu.escCloses && r.menu.focusBack)).length,
      lcp_ms_median: med(R.map(r => r.perf.lcp_ms)), lcp_ms_worst: Math.max(...R.map(r => r.perf.lcp_ms)),
      cls_worst: Math.max(...R.map(r => r.perf.cls)), cls_over_0_1: R.filter(r => r.perf.cls > 0.1).length,
      requests_median: med(R.map(r => r.perf.requests)), bytes_median_kb: +(med(R.map(r => r.perf.bytes)) / 1024).toFixed(1),
      render_blocking_median: med(R.map(r => r.perf.blocking)), dom_nodes_median: med(R.map(r => r.perf.dom)),
      lazy_images_on_first_screen: R.reduce((a, r) => a + r.perf.lazyAboveFold, 0)
    };
  }
  fs.writeFileSync(outFile, JSON.stringify({ summary: sum, rows }, null, 1));
  console.log(JSON.stringify(sum, null, 1));
})();
