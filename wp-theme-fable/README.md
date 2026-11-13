# encloud9.com WordPress build, the independent version (Agent 6, run 1, 13 Nov 2026)

Built from the Look 9 mock site in `site/`, the same brief as `wp-theme/`. Branch `wp-theme-fable`.
Nothing in `wp-theme/`, `site/` or `pages/` is changed. The full report is `REPORT-AGENT6-RUN1.md`.

## Parts

| Folder | What it is |
|---|---|
| `encloud9-nine/` | The block theme: the look only. theme.json (Look 9 colours, Hanken Grotesk), the mock's own style sheet and script, header and footer as editable template parts, templates, starting layouts for new posts and stories. |
| `encloud9-site/` | The site plugin: what belongs to content. Client stories (`/stories/<client>/`), the Section and Layout container blocks, the layout guard, the search tags carried from the mock until All in One SEO is active, and the importer (`wp n9 import`). |
| `build.py` | Reads `site/` and writes the theme's parts, page styles, page scripts, assets and `content/pages.json` (all 106 pages as blocks, every link at its approved new address). |
| `content/pages.json` | What the importer loads. |
| `score/` | Extra checks: `editor-test.js` (can an Editor really edit, and can the layout break), `a11y.js` (axe, landmarks, focus, menu, speed numbers), `run.sh` (everything in one go). The parity scorecard itself is `wp-theme/score/`, unchanged. |

## Run it from a clean checkout

```
git clone https://github.com/michaelbegley/encloud9-lookbook.git && cd encloud9-lookbook && git checkout wp-theme-fable
sh wp-theme-fable/setup.sh /home/claude/wpenv-fable/wp          # build, link theme and plugin, activate, import
sh wp-theme-fable/score/serve.sh /home/claude/wpenv-fable/wp 8090 "$PWD" 8091
```

`setup.sh` runs these, which also work one by one:

```
python3 -I wp-theme-fable/build.py
wp plugin activate encloud9-site
wp theme activate encloud9-nine
wp rewrite structure '/blog/%postname%/' --hard
wp n9 import wp-theme-fable/content/pages.json
```

## Score it

```
NODE_PATH=$(npm root -g) node wp-theme/score/shots.js wp-theme-fable/content/pages.json http://localhost:8091/site http://localhost:8090 <out dir>
python3 -I wp-theme/score/score.py <out dir> /home/claude/wpenv-fable/wp
```

or everything (parity, editing, accessibility and speed) with `sh wp-theme-fable/score/run.sh <wordpress dir> <out dir> [axe.min.js]`.
The editor test signs in as a throwaway local Editor that `score/test-users.sh` creates; its generated password is written outside the repo.

## How a page is stored

- **Section** (`encloud9/section`): one section of the page, holding the mock's own markup unchanged. In the editor it looks as it does on the site. Click any text and type; change link targets and images in the sidebar; add or remove a question, a table row or a list item with the toolbar. The element structure cannot change.
- **Layout container** (`encloud9/box`): the page wrap and the article frame. Its sections cannot be moved, removed or added to, except by a site admin who switches the lock off.
- **Running text of a blog post**: ordinary WordPress paragraphs, headings and lists, so a writer adds and reorders freely.
- Both blocks are static: the saved page is plain HTML. If the plugin were ever switched off the pages would still render.

## Not done

See the report, sections 2 and 5 and the stand-down answers.
