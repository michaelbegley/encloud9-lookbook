// Editor test: does editing really work, for someone with Editor rights, without breaking the layout?
// usage: node editor-test.js <wpBase e.g. http://localhost:8090> <secrets.json from test-users.sh> <out.json>
// Local test WordPress only. It signs in as the throwaway Editor, then:
//  1 validity   every stored block of every page is parsed by the real editor; counts blocks WordPress calls invalid
//  2 words      changes a heading on the home page in place, saves, checks the live page shows it
//  3 layout     tries to wipe a paragraph that holds a link (would remove a styled part): must be undone
//  4 link       changes a button's target in the sidebar, saves, checks the live page
//  5 guard      tries to save a section with changed structure through the REST API: the server must refuse
//  6 prose      adds a paragraph to a blog post's running text, saves, checks the live page
// Everything it changes is put back at the end.
const { chromium } = require('playwright');
const fs = require('fs');
const [,, base, secretsFile, outFile] = process.argv;
if (!/^http:\/\/(localhost|127\.0\.0\.1):\d+$/.test(base || '')) { console.error('local test sites only'); process.exit(1); }
const secrets = JSON.parse(fs.readFileSync(secretsFile));
const res = { base, checks: {} };
const ok = (name, pass, detail) => { res.checks[name] = { pass: !!pass, detail }; console.log((pass ? 'PASS ' : 'FAIL ') + name + (detail ? '  ' + JSON.stringify(detail).slice(0, 300) : '')); };

async function login(page, who) {
  await page.goto(base + '/wp-login.php', { waitUntil: 'domcontentloaded' });
  await page.fill('#user_login', secrets[who].user);
  await page.fill('#user_pass', secrets[who].pass);
  await Promise.all([page.waitForNavigation({ waitUntil: 'domcontentloaded' }), page.click('#wp-submit')]);
}

async function openEditor(page, id) {
  await page.goto(`${base}/wp-admin/post.php?post=${id}&action=edit`, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => window.wp && wp.data && wp.data.select('core/editor') && wp.data.select('core/editor').getCurrentPostId() && wp.data.select('core/block-editor').getBlockCount() > 0, null, { timeout: 60000 });
  await page.evaluate(() => { try { wp.data.dispatch('core/preferences').set('core/edit-post', 'welcomeGuide', false); wp.data.dispatch('core/preferences').set('core', 'enableChoosePatternModal', false); } catch (e) {} });
  await page.keyboard.press('Escape').catch(() => {});
  const frame = page.frameLocator('iframe[name="editor-canvas"]');
  await frame.locator('.n9-section').first().waitFor({ timeout: 60000 });
  return frame;
}

async function save(page) {
  await page.evaluate(() => wp.data.dispatch('core/editor').savePost());
  await page.waitForFunction(() => !wp.data.select('core/editor').isSavingPost() && !wp.data.select('core/editor').isEditedPostDirty(), null, { timeout: 30000 }).catch(() => {});
  return page.evaluate(() => ({ dirty: wp.data.select('core/editor').isEditedPostDirty(), failed: wp.data.select('core/editor').didPostSaveRequestFail() }));
}

const rest = (page, path, opts) => page.evaluate(async ([p, o]) => {
  try { return { ok: true, data: await wp.apiFetch(Object.assign({ path: p }, o || {})) }; } catch (e) { return { ok: false, error: e && (e.code || e.message) }; }
}, [path, opts]);

(async () => {
  const b = await chromium.launch({ executablePath: '/usr/bin/google-chrome' });
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  await login(page, 'editor');

  // find the pages to work on
  await page.goto(base + '/wp-admin/post-new.php?post_type=page', { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => window.wp && wp.blocks && wp.apiFetch && wp.blocks.getBlockType('encloud9/section'), null, { timeout: 60000 });

  // 1 validity: the real block parser and validator, over every page, post and story
  const validity = await page.evaluate(async () => {
    const out = { posts: 0, blocks: 0, invalid: 0, byType: {}, invalidSamples: [], editableChars: 0, lockedChars: 0, htmlBlocks: 0 };
    const text = h => { const d = document.createElement('div'); d.innerHTML = h; d.querySelectorAll('script,style').forEach(x => x.remove()); return d; };
    const SKIP = 'script,style,svg,canvas,select,textarea,input,button,iframe,video,audio,form [type=submit]';
    for (const type of ['pages', 'posts', 'story']) {
      for (let pg = 1; pg < 20; pg++) {
        let list;
        try { list = await wp.apiFetch({ path: `/wp/v2/${type}?context=edit&per_page=50&page=${pg}&status=publish,private` }); } catch (e) { break; }
        if (!list.length) break;
        for (const p of list) {
          out.posts++;
          const walk = bs => bs.forEach(x => {
            if (!x.name) return;
            out.blocks++; out.byType[x.name] = (out.byType[x.name] || 0) + 1;
            if (x.name === 'core/html') out.htmlBlocks++;
            if (!x.isValid) { out.invalid++; if (out.invalidSamples.length < 12) out.invalidSamples.push({ page: p.link, name: x.name, html: (x.originalContent || '').slice(0, 160) }); }
            if (x.name === 'encloud9/section') {
              // a section must come back from the browser with the same elements it went in with
              const t = document.createElement('template'); t.innerHTML = (x.attributes.content || '').trim();
              const sk = h => (h.replace(/<!--[\s\S]*?-->/g, '').match(/<[a-zA-Z][^>]*>/g) || []).map(q => { const m = q.match(/^<([a-zA-Z0-9]+)/); const c = q.match(/\sclass="([^"]*)"/); return m[1].toLowerCase() + (c ? '.' + c[1].trim().replace(/\s+/g, ' ') : '.'); }).join('|');
              out.sections = (out.sections || 0) + 1;
              if (t.content.children.length !== 1 || sk(t.content.firstElementChild.outerHTML) !== sk(x.attributes.content || '')) {
                out.roundTripFails = (out.roundTripFails || 0) + 1;
                if ((out.roundTripSamples = out.roundTripSamples || []).length < 8) out.roundTripSamples.push({ page: p.link, roots: t.content.children.length, html: (x.attributes.content || '').slice(0, 120) });
              }
              const d = text(x.attributes.content || '');
              const all = (d.textContent || '').replace(/\s+/g, '').length;
              let locked = 0;
              d.querySelectorAll(SKIP + ',[aria-hidden="true"]').forEach(n => { if (!n.parentElement.closest(SKIP + ',[aria-hidden="true"]')) locked += (n.textContent || '').replace(/\s+/g, '').length; });
              out.editableChars += all - locked; out.lockedChars += locked;
            } else if (/^core\/(paragraph|heading|list-item)$/.test(x.name)) {
              out.editableChars += (text(x.originalContent || '').textContent || '').replace(/\s+/g, '').length;
            }
            walk(x.innerBlocks || []);
          });
          walk(wp.blocks.parse(p.content.raw));
        }
        if (list.length < 50) break;
      }
    }
    return out;
  });
  res.validity = validity;
  ok('1 every stored block is valid in the editor', validity.invalid === 0 && validity.blocks > 0, { posts: validity.posts, blocks: validity.blocks, invalid: validity.invalid, samples: validity.invalidSamples });
  ok('  every section survives a browser round trip unchanged', !validity.roundTripFails, { sections: validity.sections, fails: validity.roundTripFails || 0, samples: validity.roundTripSamples });
  res.editable_text_pct = +(100 * validity.editableChars / Math.max(1, validity.editableChars + validity.lockedChars)).toFixed(1);

  const home = (await rest(page, '/wp/v2/pages?slug=home&context=edit&_fields=id,link,content')).data[0];
  const original = home.content.raw;

  // 2 words: change the first section heading on the home page, in place
  let frame = await openEditor(page, home.id);
  const h2 = frame.locator('.n9-section h2[data-n9]').first();
  const before = (await h2.textContent()).trim();
  await h2.click();
  await page.keyboard.press('End');
  await page.keyboard.type(' EDITED-BY-TEST');
  await page.keyboard.press('Enter');          // must not split the heading
  await page.keyboard.type('!');
  let s = await save(page);
  let live = await (await ctx.request.get(home.link)).text();
  const want = before + ' EDITED-BY-TEST!';
  ok('2 an Editor changes a heading in place and the live page shows it', !s.failed && live.includes('EDITED-BY-TEST!</h2>'), { before, want, saveFailed: s.failed });

  // 3 layout: select everything in a paragraph that holds a link and type over it
  const lead = frame.locator('.n9-section p[data-n9]:has(a)').first();
  const leadBefore = await lead.innerHTML();
  await lead.click();
  await page.keyboard.press('Control+A');
  await page.keyboard.type('x');
  await page.waitForTimeout(300);
  const leadAfter = await lead.innerHTML();
  ok('3 an edit that would remove a link is undone on the spot', leadAfter === leadBefore, { same: leadAfter === leadBefore });

  // 4 link: change the first button target of the hero from the sidebar
  await frame.locator('.n9-section').first().locator('[data-n9]').first().click();
  await page.evaluate(() => wp.data.dispatch('core/edit-post').openGeneralSidebar('edit-post/block'));
  const field = page.locator('.components-panel__body:has-text("Links and buttons") input[type=text]').first();
  await field.waitFor({ timeout: 15000 });
  const oldHref = await field.inputValue();
  await field.fill('/contact-us/?n9test=1');
  s = await save(page);
  live = await (await ctx.request.get(home.link)).text();
  ok('4 an Editor changes a link target in the sidebar and the live page shows it', !s.failed && live.includes('href="/contact-us/?n9test=1"'), { oldHref, saveFailed: s.failed });

  // structure after the edits: same tags and classes as before
  const skel = h => (h.match(/<\/?[a-zA-Z][^>]*>/g) || []).map(t => { const m = t.match(/^<(\/?[a-zA-Z0-9]+)/); const c = t.match(/\sclass="([^"]*)"/); return m[1].toLowerCase() + (c ? '.' + c[1] : ''); }).join('|');
  const edited = (await rest(page, `/wp/v2/pages/${home.id}?context=edit&_fields=content`)).data.content.raw;
  ok('  the page structure is unchanged after the edits', skel(edited) === skel(original), { tagsBefore: skel(original).split('|').length, tagsAfter: skel(edited).split('|').length });

  // 5 guard: the server refuses a changed section structure from an Editor
  const broken = original.replace('<section class="hero"', '<section class="hero broken-by-test"');
  const g = await rest(page, `/wp/v2/pages/${home.id}`, { method: 'POST', data: { content: broken } });
  ok('5 the server refuses a changed layout from an Editor', !g.ok && g.error === 'n9_layout_locked', { error: g.error, changed: broken !== original });

  // put the home page back
  const back = await rest(page, `/wp/v2/pages/${home.id}`, { method: 'POST', data: { content: original } });
  ok('  home page restored', back.ok && back.data.content.raw === original);

  // 6 prose: add a paragraph to a blog post's running text
  const post = (await rest(page, '/wp/v2/posts?per_page=1&orderby=slug&order=asc&context=edit&_fields=id,link,content')).data[0];
  const postOriginal = post.content.raw;
  frame = await openEditor(page, post.id);
  const added = await page.evaluate(() => {
    const be = wp.data.select('core/block-editor');
    const find = bs => { for (const x of bs) { if (x.name === 'encloud9/box' && x.attributes.prose) return x; const r = find(x.innerBlocks || []); if (r) return r; } return null; };
    const box = find(be.getBlocks());
    if (!box) return 'no running text';
    if (!be.canInsertBlockType('core/paragraph', box.clientId)) return 'cannot insert';
    wp.data.dispatch('core/block-editor').insertBlock(wp.blocks.createBlock('core/paragraph', { content: 'PARAGRAPH-ADDED-BY-TEST' }), 1, box.clientId);
    const wrap = be.getBlocks()[0];
    return { canInsertInLockedWrap: be.canInsertBlockType('core/paragraph', wrap.clientId), canRemoveSection: be.canRemoveBlock(wrap.innerBlocks[0].clientId) };
  });
  s = await save(page);
  live = await (await ctx.request.get(post.link)).text();
  ok('6 an Editor adds a paragraph to a post and the live page shows it', !s.failed && live.includes('<p>PARAGRAPH-ADDED-BY-TEST</p>'), added);
  ok('  sections of a page cannot be added, moved or removed by an Editor', added && added.canInsertInLockedWrap === false && added.canRemoveSection === false, added);
  const back2 = await rest(page, `/wp/v2/posts/${post.id}`, { method: 'POST', data: { content: postOriginal } });
  ok('  post restored', back2.ok && back2.data.content.raw === postOriginal);

  res.script_errors_in_editor = errs;
  ok('  no script errors in the editor', errs.length === 0, errs.slice(0, 5));
  res.pass = Object.values(res.checks).every(c => c.pass);
  fs.writeFileSync(outFile, JSON.stringify(res, null, 1));
  await b.close();
  process.exit(res.pass ? 0 : 2);
})().catch(e => { console.error(e); fs.writeFileSync(outFile, JSON.stringify(Object.assign(res, { crashed: String(e) }), null, 1)); process.exit(3); });
