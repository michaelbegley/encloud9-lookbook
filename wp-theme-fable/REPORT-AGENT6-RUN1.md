# Report: encloud9.com WordPress theme, the independent build

Agent 6, run 1, Fable 5.2. Fri 13 Nov 2026. Branch `wp-theme-fable`, folder `wp-theme-fable/`.

Every number below is **measured** in the cloud workspace on WordPress 6.8 (SQLite, PHP 8.3, Chrome), unless it is labelled inferred or could not determine.

## Questions for Michael

1. **The main call, yours to make.** I did not build "approach C" (core blocks in locked patterns). I kept the mock's markup exact and built a Section block that is edited in place. The reason and the trade-off are in section 1. If you would rather have core blocks only, say so; it means rewriting the markup and CSS of 835 sections, and parity would have to be won again.
2. **Kept posts.** The theme now frames any post that has no designed layout (breadcrumb, title, author, date, a contents list from its headings, and the closing call to action of the generative pages post, word for word). That is how the 139 blog addresses not in the mock would look. Is that an approved use of the design, or does Brian need to see it first?
3. **Placeholders in approved copy.** The generative pages post shows "[Author]", "[Publish date]", a "[Screenshot: ...]" box, "Draft for the December theme" and one link to "#". I left every word as it is (locked). Who fills them before 9 Dec?
4. **Menus.** The header holds the desktop menu and the phone menu as two separate lists (as in the mock). An admin can edit both in the Site Editor, but a change to one must be made in the other. Fine for launch, or should one list feed both?

## 0 Identity and scope

Agent 6, run 1, Fable 5.2. The independent second build of the encloud9.com block theme, from the same brief as `wp-theme/`.

- Worked only in `/home/claude/lookbook-fable` (branch `wp-theme-fable`), `/home/claude/wpenv-fable` and a scratch folder. `wp-theme/`, `site/`, `pages/`, `/home/claude/lookbook` and `/home/claude/wpenv` are untouched.
- Locked items kept: no word changed, no page added or removed, all 106 pages at their addresses in ADDRESS-SCHEME-Draft1 (checked by script: 106 of 106 are in the scheme), design unchanged.
- **Project docs: I could not read them** (no Projects tool in this session). I worked from the brief, the repo and the brief folder.
- No internal document is committed: no brief, no CSV, no client data. `address-moves.json` is a copy of the file already public in `wp-theme/`.
- Sign-ins: only two throwaway local test users that a script generates for the editor test. Their passwords are random, written outside the repo and never printed.

## 1 Research and the approach chosen

Sources read (public pages on developer.wordpress.org):

| Title | URL | What I took from it |
|---|---|---|
| Block Templates (Block API reference) | https://developer.wordpress.org/block-editor/reference-guides/block-api/block-templates/ | `templateLock` values: all, insert, contentOnly. A contentOnly lock cannot be overridden by child blocks. |
| How to add content-only editing support to a block (WordPress Developer Blog, Nov 2024) | https://developer.wordpress.org/news/2024/11/how-to-add-content-only-editing-support-to-a-block/ | In a contentOnly container only attributes marked `"role": "content"` can be edited, the settings sidebar is off, and blocks without content cannot be selected. |
| Block Bindings (Block API reference) | https://developer.wordpress.org/block-editor/reference-guides/block-api/block-bindings/ | Bindings cover image (id, url, title, alt, caption), heading and paragraph (content), button (url, text, linkTarget, rel), navigation link and submenu (url) and post date. WordPress 6.5 and up. |
| Block Locking API (Curating the editor experience) | https://developer.wordpress.org/block-editor/how-to-guides/curating-the-editor-experience/block-locking/ | `canLockBlocks` can be set by capability through `block_editor_settings_all`. The page describes no server-side enforcement (my reading, inferred: a lock is an editor control, not a guarantee). |

What the mock is made of (measured across the 106 page bodies): 6,424 spans, 3,050 inline style attributes, 870 `aria-hidden`, 716 `data-l` labels for stacked tables, 558 FAQ entries, 42 tables, 13 images. Core blocks cannot carry inline custom properties, data attributes or this nesting, and they add wrappers of their own (an image gets a figure, a button gets a div).

| | A. Custom HTML block per section (`wp-theme/` 0.1.1) | B. Core blocks in contentOnly patterns ("approach C") | C. Section block edited in place, core blocks for running text (this build) |
|---|---|---|---|
| Match to the mock | Exact (0.02% worst) | Markup and CSS of 835 sections rewritten to fit core blocks; parity to be won again, risk of re-approval (inferred) | Exact (0.02% worst), markup untouched |
| What an Editor sees | HTML source in a code box | The real page, native block tools | The real page; click text and type |
| Can the layout break | Yes, one stray tag | The lock is editor-only; the code view or an unlock undoes it | Not in the editor (a structure change is undone on the spot), and a server guard refuses it on save |
| Adding a paragraph to a post | Edit HTML | Native | Native (core paragraph, heading, list) |
| Effort to launch by 9 Dec | Done | High (inferred: a pattern for every section type across 106 pages) | Done |
| Cost | Not editable | Most WordPress-native; best long term if the design is ever rebuilt for blocks | Two custom blocks to maintain (429 lines of plain script, no build step) |

Chosen: **C**. It meets "editable safely" now without touching the approved design. Both blocks are static (they save plain HTML), so the pages render even with the plugin off.

## 2 What I kept from Claude's version, what I changed, what I rebuilt, and why

**Kept (same idea, mostly the same code)**
- The link rewriting to the approved addresses (`fix_urls`, `address-moves.json`), the client story type at `/stories/<client>/`, the importer's match-by-address and update-in-place, the footer moved out of `main` with its fix rules, the 404 body as a private page shown by the 404 template, texturize off, and the scorecard (`wp-theme/score/`, not modified).

**Changed**
- **Page bodies**: Custom HTML blocks became 835 Section blocks, 177 Layout containers and 553 core blocks (346 paragraphs, 153 headings, 54 lists) for the running text of the 18 posts and the "how Microsoft updates" page. Custom HTML blocks left: 0.
- **Header and footer**: were PHP reading `inc/*.html`; now real template parts made of Section blocks, so an admin edits menu words and links in the Site Editor. The current-section mark is added as the header is printed.
- **Page styles and scripts**: were stored in post meta per page (576 KB of CSS across 106 pages); now 35 style files and 15 script files in the theme, printed inline in the same place the mock had them. A post or story written later gets its type's default set.
- **Scripts inside page bodies** (12 pages) are lifted into those theme files, so no page content carries a script.
- **Theme and plugin split**: content types, blocks, guard, search tags and importer are in the `encloud9-site` plugin; the theme is presentation only.
- **Assets**: only files the pages use are copied (theme folder 0.63 MB; `wp-theme/encloud9-nine` is about 5.6 MB). The lookbook's font switcher is cut from `nine.js` at build time.
- **Speed**: one style request instead of three (the scale sheet and page styles are inlined), two font weights preloaded (400 and 600, the two every page asks for first; checked on 4 pages at 2 widths), and WordPress's default link underline rule dropped because it outranks the design's own link rules.
- **Search tags**: Open Graph tags added; everything stops when All in One SEO is active; noindex goes through `wp_robots` so it holds with or without an SEO plugin. New `wp n9 seo-export file.csv` writes title, description and noindex per page for the hand-over (106 rows, no title over 60 characters, no description over 160, no duplicates).
- **Holding pages** for address levels with no page (`/lp/`, `/encloud9-dynamics-365-crm-services/`) are private: the level answers 404 and the pages under it keep their addresses (checked). Claude's were published and empty.
- **404**: the colour scale under the footer is hidden there, as in the mock. That removes the 24 px height difference.
- HTML comments inside page bodies (builder notes) are not carried into the site.

**Rebuilt from scratch**
- `build.py` (a small parser that keeps the mock's source text as written and only cuts it into blocks), both blocks (`encloud9-site/blocks/editor.js`), the layout guard, the importer as `wp n9 import`, `setup.sh`, the editor test and the accessibility pass.

**New**
- Starting layouts for a new blog post and a new client story (theme patterns WordPress offers on "Add new").
- A theme frame for posts with no designed layout (question 2).
- Editors do not get the Custom HTML, Shortcode or Classic blocks, the code view, or the lock menu.

## 3 How editing works for an Editor

**Can change**
- Any visible words in a section, in place: headings, paragraphs, card text, table cells, FAQ questions and answers, link and button labels. Bold and italic with Ctrl+B and Ctrl+I. Paste comes in as plain text.
- Where a link or button goes: click it, then "The link you clicked" in the sidebar. All links of the section are listed there too.
- Images: replace from the media library and edit the alt text, in the sidebar.
- The number of items in a stacked list: FAQ questions, table rows, list items, a column of links. Click one, then plus or minus in the toolbar. A new item is a copy of the designed one.
- In a blog post's running text: add, remove and reorder paragraphs, headings, lists, images and other ordinary blocks.
- Start a new post or client story from the designed layout.

**Cannot change**
- The order or number of sections on a designed page (a site admin can unlock a container), classes, colours, spacing, fonts.
- Items in designed grids (the nine squares, the four "at a glance" cubes, step bars, card rows): no plus or minus is offered there.
- Add a link to, or remove a link from, a sentence inside a section (in a post's running text they can).
- Labels on real buttons (quiz answers, filter chips), form fields, drawings, hidden labels for screen readers.
- Header, footer and menus (site admin, in the Site Editor). The page title tag and description (carried by the plugin until All in One SEO is in).

**What stops a broken layout** (three layers, each tested)
1. In the editor, an edit that would remove or add a styled element is undone at once, with a notice.
2. Sections sit in locked containers; Editors have no unlock menu and no code view.
3. On save, the server refuses (for anyone who is not a site admin) a section holding a kind of element or class that its page, or the theme's layouts, did not already have. This is a guard against accidents, not a security wall: WordPress trusts Editors with HTML on a single site.

**Worked example: reword a heading and repoint the hero button on the home page**
1. Pages, Home, Edit. The page appears as it does on the site.
2. Click the heading "Which businesses has enCloud9 built for?" and type. Enter does nothing (a heading cannot be split).
3. Click the "Book a call" button in the hero. In the sidebar, under "The link you clicked", change `/lp/schedule-a-meeting/` to the new address.
4. Save. The live page shows both changes; nothing else moved.

The editor test does exactly this as a throwaway Editor, then checks the page still has the same tags and classes (872 before, 872 after).

**Limits I know of**
- The first edit to a section rewrites that section's HTML in the browser's spelling (for example `&rarr;` becomes the arrow character). It renders the same; the first revision diff is noisy.
- Undo works through WordPress (Ctrl+Z) but the cursor leaves the text.
- The FAQ search markup (JSON-LD) is carried from the mock per page; it does not follow an edited FAQ.
- A contents list in a designed post is a section: its links are edited in the sidebar and items added with plus. It does not rebuild itself from the headings (the theme frame for plain posts does).
- Not tested by script: replacing an image through the media library, the "Show template" view, the admin unlock switch, phones, and browsers other than Chrome.

## 4 Scorecard

Claude's scorecard, unchanged, on this build (106 pages, 1440 and 390 px):

| Measure | `wp-theme/` 0.1.1 (from the brief) | This build |
|---|---|---|
| Worst page, pixels different | 0.02% | 0.02% (/microsoft-power-platform/ at 390) |
| Median | 0.00% | 0.00% |
| Pages over 1% | not given | 0 |
| Height differences over 20 px | 404 page, 24 px (its README) | none |
| Non-200 | 0 | 0 |
| Broken images | 0 | 0 |
| Script errors | 0 | 0 |
| Median page weight at 1440 | 95 KB | 88.3 KB |
| Editable share (top-level blocks that are not Custom HTML) | 0.0% | 100.0% (240 of 240) |

Measures I added, kept apart in `wp-theme-fable/score/` (nothing existing was changed):

**`editor-test.js`: is it really editable, and can it break** (signs in as a throwaway Editor, in Chrome)

| Check | Result |
|---|---|
| Every stored block is valid in the real editor | 1,778 blocks on 108 posts, 0 invalid |
| Every section comes back from the browser with the same elements | 835 of 835 |
| Share of text an Editor can change (text not inside real buttons, form fields, drawings or hidden decoration) | 99.3% |
| Change a heading in place, save with the Save button, live page shows it | pass |
| Type over a paragraph that holds a link (would remove the link) | undone on the spot |
| Change a button target in the sidebar, live page shows it | pass |
| Add a FAQ question with the toolbar, live page shows it | pass |
| The nine-square grid offers no add or remove | pass |
| The server refuses a changed section layout from an Editor | pass (`n9_layout_locked`) |
| Add a paragraph to a post's running text, live page shows it | pass |
| An Editor cannot add, move or remove a section on a designed page | pass |
| Script errors in the editor | 0 |

**`a11y.js`: accessibility and speed** (105 pages at 2 widths = 210 page views a side; the 404 is left out; axe-core 4.14.0 with the WCAG 2.0, 2.1 and 2.2 A and AA rule sets, which include the 24 px target size)

| Measure | The mock (`site/`) | This build |
|---|---|---|
| Page views with an axe violation | 0 | 0 |
| Footer inside `main` | 210 | 0 |
| Page views with no footer landmark | 210 | 0 |
| Page views without exactly one `main` or one h1 | 0 | 0 |
| Skip link missing, not first, or with no target | 0 | 0 |
| Scroll padding smaller than the sticky header | 0 | 0 |
| Focus stops hidden under the sticky header (40 Tab presses a page view) | 0 | 0 |
| Header menu by keyboard fails (opens on press, Esc closes, focus returns) | 0 | 0 |
| Layout shift, worst page view | 0.27 (7 page views over 0.1; 0.20 and 6 on an earlier run) | 0.0002 (none over 0.1) |
| Largest paint, median and worst (localhost) | 88 ms, 156 ms | 116 ms, 192 ms |
| Render-blocking requests, median | 3 | 1 |
| Requests, median | 9 | 8 |
| Bytes with the document, median | 136.4 KB | 145.7 KB |
| Lazy-loaded images on the first screen | 0 | 0 |

How to read these: the speed numbers are lab numbers on localhost with no network delay. They are good for comparing the two sides and for layout shift, not a forecast of field Core Web Vitals. INP is not measured (it needs real interaction data). axe finds only what a machine can find. This build sends about 9 KB more per page view than the static mock (WordPress's own block and preset styles), in fewer requests.

## 5 What is missing from the launch plan, ranked

Inferred from the brief folder and from building. I could not read the project docs, so some of this may already be planned.

1. **166 of the 272 approved addresses are not in the mock (139 under /blog/).** They must come from the old site, where WHAT-STICKS marks posts as Divi or classic editor. Divi shortcodes print as raw text once Divi is gone. I found no conversion step, owner or test in the repo. Largest scope risk for 9 Dec.
2. **No working form.** Twelve pages carry a form and none of them works yet (contact, health check, license check, call prep, storage analysis, three guides, three ad landing pages, the blog sign-up). Gravity Forms to ClickDimensions to Dynamics, the thank-you addresses GA4 counts, spam control and a test lead per form are all still to do. A launch without them takes no leads.
3. **No analytics or tracking tag anywhere.** The mock and both themes load only `nine.js` (measured). GA4 or Tag Manager, the ClickDimensions tracking script and any chat widget need a place, an owner and a consent decision.
4. **The redirect map is not complete and not tested.** Its own notes say only 32 of the 94 existing Redirection rules are carried, Permalink Manager Pro's redirects are not in it, /security/ is unresolved, and posts after 19 Oct have no rows. There is no script that requests all 383 old addresses on staging and checks for one hop to a 200.
5. **The search tags hand-over to All in One SEO.** Titles, descriptions and JSON-LD live in the plugin's fields. When AIOSEO is switched on the plugin goes quiet; unless the values are loaded into AIOSEO first, the approved titles are replaced by defaults. `wp n9 seo-export` gives the file; the import and a before-and-after check are not built. FAQ JSON-LD will also drift from edited FAQs.
6. **The blog hub is a hand-written page.** A new post does not appear on /blog/ until someone edits that page. Category pages, paging, search results and the feed have no design (the theme gives them a plain list).
7. **Placeholders in approved copy** would go live: "[Author]", "[Publish date]", "[Screenshot: ...]", "Draft for the December theme" (on the post and on /blog/), a link to "#", and a form labelled "mock, not working".
8. **Site Editor changes shadow git.** Once an admin edits the header or footer in the Site Editor, WordPress keeps that copy in the database and stops reading the theme file. Later header changes pushed through git will not show. Decide: menus are edited in WordPress or in git, not both.
9. **Mail.** Flywheel rules out SMTP plugins; form notices and password resets still need a sending path tested for delivery (could not determine what is planned).
10. **Launch-day runbook and rollback.** Content freeze on the old site, the switch on Flywheel, cache purge, "discourage search engines" off on live and on for staging (every mock page says noindex; the build does not carry that), sitemap submitted, the 404 log watched, and how to go back. Could not determine if written (SITE-MOVE-STANDARD was not readable here).
11. **Address levels and Permalink Manager Pro.** Addresses such as /lp/... and /encloud9-dynamics-365-crm-services/... need parent pages in plain WordPress (the importer makes private ones). /lp/ itself is in the scheme as a real page but is not in the mock. If Permalink Manager Pro stays, its rules can fight these; if it goes, its own redirects go with it.
12. **Images are in the theme folder.** 13 images and the share card are addressed by the theme's path. Moving them to the media library is not done in either build.
13. **Editing rules for people.** Who is admin, who is Editor, a short walkthrough for Kristin, and where edits happen after launch (on live only, since content is never pushed over live).
14. **Eight links still point at www.encloud9.com for posts not built** (site/NOT-BUILT-YET.txt). On staging they leave staging; after launch they work only if item 1 is done.
15. **Field speed and manual accessibility.** Lab numbers are clean, but Flywheel's cache and CDN are untested with this theme, and a screen-reader and keyboard pass on the real forms and the 404 game is still needed. The accessibility statement page should match what was tested.
16. **The booking page.** /lp/schedule-a-meeting/ has no Bookings embed yet (named as not done in `wp-theme/README.md`).

## 6 How to run this build from a clean checkout

```
git clone https://github.com/michaelbegley/encloud9-lookbook.git && cd encloud9-lookbook
git checkout wp-theme-fable
cp -a /home/claude/wpenv /home/claude/wpenv-fable        # once; then fix the SQLite path in wp/wp-content/db.php
WP="php /home/claude/wpenv-fable/wp-cli.phar --allow-root --path=/home/claude/wpenv-fable/wp"
$WP option update siteurl http://localhost:8090 && $WP option update home http://localhost:8090
$WP post delete $($WP post list --post_type=page,post,story --post_status=any --format=ids) --force   # clear the other build's pages
sh wp-theme-fable/setup.sh /home/claude/wpenv-fable/wp   # build, link theme and plugin, activate, permalinks, import
sh wp-theme-fable/score/serve.sh /home/claude/wpenv-fable/wp 8090 "$PWD" 8091

# Claude's scorecard
NODE_PATH=$(npm root -g) node wp-theme/score/shots.js wp-theme-fable/content/pages.json http://localhost:8091/site http://localhost:8090 /tmp/fable-shots
python3 -I wp-theme/score/score.py /tmp/fable-shots /home/claude/wpenv-fable/wp

# everything, with the editor test and the accessibility pass
# (axe is optional: npm install axe-core in a scratch folder and pass its axe.min.js)
sh wp-theme-fable/score/run.sh /home/claude/wpenv-fable/wp /tmp/fable-score /path/to/axe.min.js
```

`score/serve.sh` is Claude's with four PHP workers. `setup.sh` runs `build.py`, activates `encloud9-site` and `encloud9-nine`, sets `/blog/%postname%/` and runs `wp n9 import wp-theme-fable/content/pages.json`.

## Stand-down

**(1) What did I see and not write down?**
- WordPress prints its default colour, gradient and size presets on every page (about 8 KB before compression) though the site uses none. I left them; old posts may rely on those classes.
- The feed and comment-feed links are still in the head; comments are closed on imported pages only.
- `nine-scale.css` scopes its type rules to `main`, which is why the footer needed two extra rules once it left `main` (kept from Claude's fix).
- The mock itself shifts layout on 6 or 7 page views (worst 0.20 to 0.27); this build does not. I did not find out why the mock shifts.
- The first scorecard run died with the workspace connection and took the local servers with it; nothing was lost. One push failed with a 503 and worked on retry.
- My first accessibility run counted one "hidden focus stop" per page on both sides; that was the test reading positions during smooth scrolling. Fixed in the test, then 0 on both.

**(2) What looked odd and did not fit the brief?**
- The brief says 106 pages and the scheme has 272 addresses; the other 166 have no source here (item 1 above).
- One "approved" post is visibly a draft (question 3).
- On the 404 page the closing section is empty once the footer leaves it, but keeps its label "Site links": an empty named region. axe does not flag it; it is untidy.
- The mock repeats the full header and footer on every page. They were identical on all 106 (checked), apart from the one ad landing page with no menu, which became its own template.
- The two page-weight numbers (88.3 KB and 145.7 KB) differ because the tools count differently; the second includes the document and waits longer.

**(3) What did I decide was out of scope?**
- Rewriting sections as core blocks; a dynamic blog hub; forms; redirects; the All in One SEO import; moving images to the media library; one-source menus; a "page look" picker for brand-new pages (a new page has no page-type styles unless it is made from a copy); converting old posts; anything on Flywheel, Dynamics or the live site.
- Fixing typos or placeholders (locked). I did not proofread for typos; the placeholders I ran into are in question 3.

**(4) What did I not look at that I should name?**
- The project docs (could not read them), so the rules in WP-THEME-FROM-LOOK9, SITE-MOVE-STANDARD and R-WP-TECH were not checked line by line.
- `tools/gen/STANDARD.txt` and `allsec.txt` beyond a skim; I cut pages by their markup, not by the generators' section types.
- REDIRECT-MAP-Draft1.csv and WHAT-STICKS.csv row by row (I read the notes, the headers and the counts).
- Safari, Firefox, real phones, a screen reader, WordPress versions other than 6.8, MySQL (the test site is SQLite), and the theme with All in One SEO or Gravity Forms actually installed (wordpress.org is blocked here).
- Two people editing at once, long editing sessions, and every word of every page by eye (parity is by pixel comparison).

Agent 6 run 1: done. Independent build on branch `wp-theme-fable` matches the mock as closely as Claude's (worst page 0.02%, median 0.00%), with 0 Custom HTML blocks, 99.3% of text editable in place by an Editor, the layout locked in the editor and on the server, 0 axe violations on 210 page views, and 4 questions waiting for Michael.
