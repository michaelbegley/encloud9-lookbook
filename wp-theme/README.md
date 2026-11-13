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
All 106 pages answer 200 at their new addresses (the 404 page answers 404). Screenshots of every page at 1440 and 390 px, mock against WordPress: the same height at 1440 on every page, median pixel difference 0.23%, no broken images, no script errors. Known differences:
- On phones the footer's first column is 14 px as the footer style sets it; in the mock a page-wide paragraph rule made it 17 px (13 to 14 px taller). Claude's call: keep 14 px.
- The 404 game's idle animation is caught at different moments.

## Not done yet
- Page bodies are Custom HTML blocks (exact match first). Next: section types become locked patterns so words and images can be edited safely (WP-THEME-FROM-LOOK9.md, approach C).
- Images live in the theme for now; they move to the media library at the import on Local.
- Forms (Gravity Forms to ClickDimensions), the Bookings embed, All in One SEO, the Redirection import (REDIRECT-MAP-Draft1), the 104 kept posts, the site plugin.
- `nine.js` still carries the lookbook's font switcher; harmless, removed before launch.
