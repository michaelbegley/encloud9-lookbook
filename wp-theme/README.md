# encloud9.com WordPress theme (Draft 1, 13 Nov 2026)

The real site, built from the Look 9 mock site in `site/`. Branch `wp-theme`; the mock site on `main` is untouched.

## Parts
- `encloud9-nine/` the block theme: theme.json (Look 9 colours, Hanken), the mock's own CSS and script, header and footer as server-rendered blocks, templates, client stories at `/stories/<client>/`.
- `build.py` makes the theme's header, footer and assets and `content/pages.json` (all 106 pages) from `site/`, with every link moved to the approved new addresses (`address-moves.json`, ADDRESS-SCHEME-Draft1).
- `import.php` loads `pages.json` into WordPress. Run again any time; pages are updated in place.

## Run it
```
python3 -I wp-theme/build.py
wp theme activate encloud9-nine
wp rewrite structure '/blog/%postname%/' --hard
wp eval-file wp-theme/import.php wp-theme/content/pages.json
```

## Checked (13 Nov 2026, WordPress 6.8 on SQLite in the cloud workspace)
All 106 pages answer 200 at their new addresses (the 404 page answers 404). Scorecard (`score/`): all 106 pages at 1440 and 390 px against the mock. Worst page 0.02% of pixels different, median 0.00%, no broken images, no script errors, median page 95 KB. Only the 404 page differs in height (24 px, its game). Editable share of page content: 0% (every section is still Custom HTML).

## Scorecard
```
sh wp-theme/score/serve.sh <wordpress dir> 8080 <repo root> 8081
node wp-theme/score/shots.js wp-theme/content/pages.json http://localhost:8081/site http://localhost:8080 <out dir>
python3 -I wp-theme/score/score.py <out dir> <wordpress dir>
```

## Not done yet
- Page bodies are Custom HTML blocks (exact match first). Next: section types become locked patterns so words and images can be edited safely (WP-THEME-FROM-LOOK9.md, approach C).
- Images live in the theme for now; they move to the media library at the import on Local.
- Forms (Gravity Forms to ClickDimensions), the Bookings embed, All in One SEO, the Redirection import (REDIRECT-MAP-Draft1), the 104 kept posts, the site plugin.
- `nine.js` still carries the lookbook's font switcher; harmless, removed before launch.
