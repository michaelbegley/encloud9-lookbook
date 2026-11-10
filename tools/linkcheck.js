// linkcheck.js: internal linking check for built pages (stage 6 QA).
// Source: claude/site-build/tools/linkcheck.js (loose chat, 5 Nov 2026); added to the lookbook site gates 10 Nov 2026.
// Usage: node tools/linkcheck.js <pages-folder> [--prefix=nine-] [--json]
// Reads every .html file in the folder, finds links between them inside <main>
// (header, footer and nav links are ignored), and reports:
//   orphan       no other page links to it in body copy        FAIL
//   self         a page links to itself                          FAIL
//   duplicate    the same target linked twice in body copy       FAIL (only plain links in prose count; buttons, arrow links,
//                                                                section links and card tiles repeat by design)
//   generic      anchor text like "click here" or "read more"    FAIL
//   too many     more than 5 internal body links to other pages  WARN (hubs and index pages may exceed)
// Footer, nav and aside are dropped first, even when they sit inside <main>.
// Card-style links ("Read the post" tiles, related posts) count as links but are
// exempt from the generic-anchor rule when the card has a title inside it.
const fs = require('fs'), path = require('path');
const dir = process.argv[2]; const asJson = process.argv.includes('--json');
if (!dir) { console.error('usage: node linkcheck.js <pages-folder>'); process.exit(2); }
const pre = (process.argv.find(x => x.startsWith('--prefix=')) || '--prefix=').slice(9);
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html') && f.startsWith(pre));
const GENERIC = /^(click here|here|read more|learn more|more|this|this page|link|go|see more)$/i;
const strip = s => s.replace(/<[^>]+>/g, ' ').replace(/&[a-z#0-9]+;/gi, ' ').replace(/\s+/g, ' ').trim();
const pages = {};
for (const f of files) {
  const html = fs.readFileSync(path.join(dir, f), 'utf8');
  const m = html.match(/<main[\s\S]*?<\/main>/i);
  // body copy only: drop footer, nav, the contents list and the lookbook bar inside main
  const main = (m ? m[0] : '').replace(/<(footer|nav|aside)\b[\s\S]*?<\/\1>/gi, '');
  const links = [];
  const re = /<a\b([^>]*)>([\s\S]*?)<\/a>/gi; let a;
  while ((a = re.exec(main))) {
    const href = (a[1].match(/href="([^"]*)"/i) || [])[1] || '';
    if (/^(https?:|mailto:|tel:|#)/i.test(href) || !href) continue;
    const target = href.split('#')[0].split('?')[0].replace(/^\.\//, '');
    if (!target.endsWith('.html')) continue;
    // a link that holds a title span (class="t") is a story or post card even without a card class (10 Nov 2026, Marketing story list)
    const isCard = /class="[^"]*\b(pc|ptile|card|tile|fc|feat|cell|row|pf)\b/i.test(a[1]) || /class="t"/.test(a[2]);
    // actions: buttons, arrow links (lnk) and links to a section (#check, #checkups)
    const isButton = /class="[^"]*\b(btn|lnk)\b/i.test(a[1]) || href.includes('#');
    links.push({ target, anchor: strip(a[2]).slice(0, 80), isCard, isButton });
  }
  pages[f] = { links, inbound: 0 };
}
for (const f of files) for (const l of pages[f].links) if (pages[l.target] && l.target !== f) pages[l.target].inbound++;
const issues = [];
for (const f of files) {
  const p = pages[f], seen = {};
  for (const l of p.links) {
    if (l.target === f) issues.push({ page: f, level: 'FAIL', rule: 'self', detail: l.anchor });
    if (l.isButton || l.isCard) { seen[l.target] = seen[l.target] || 0; continue; } // buttons and card tiles may repeat by design
    if (seen[l.target]) issues.push({ page: f, level: 'FAIL', rule: 'duplicate', detail: l.target + ' (' + l.anchor + ')' });
    seen[l.target] = 1;
    if (!l.isCard && GENERIC.test(l.anchor)) issues.push({ page: f, level: 'FAIL', rule: 'generic', detail: l.anchor + ' -> ' + l.target });
  }
  const out = Object.keys(seen).filter(t => t !== f && pages[t]).length;
  if (out > 5) issues.push({ page: f, level: 'WARN', rule: 'too many', detail: out + ' body links to other pages (fine on a hub)' });
  // footer-only pages (404, legal) are not meant to be linked from body copy (10 Nov 2026)
  if (p.inbound === 0 && /^(nine-)?(404|accessibility|terms|privacy)\.html$/.test(f)) issues.push({ page: f, level: 'INFO', rule: 'footer only', detail: 'linked from the footer only, by design' });
  else if (p.inbound === 0) issues.push({ page: f, level: 'FAIL', rule: 'orphan', detail: 'no link in the body copy of any other page (nav and footer links do not count)' });
}
const summary = files.map(f => ({ page: f, out: new Set(pages[f].links.map(l => l.target).filter(t => t !== f && pages[t])).size, in: pages[f].inbound }));
if (asJson) { console.log(JSON.stringify({ summary, issues }, null, 1)); }
else {
  console.log('page | links out | links in');
  for (const s of summary) console.log(`${s.page} | ${s.out} | ${s.in}`);
  console.log('\n' + (issues.length ? issues.map(i => `${i.level} ${i.rule}: ${i.page}: ${i.detail}`).join('\n') : 'No issues.'));
}
process.exit(issues.some(i => i.level === 'FAIL') ? 1 : 0);
