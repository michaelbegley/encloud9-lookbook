#!/bin/sh
# Build the theme and load all 106 pages into a local test WordPress.
# usage (from the repo root): sh wp-theme-fable/setup.sh <wordpress dir>     e.g. /home/claude/wpenv-fable/wp
# Needs wp-cli.phar next to the WordPress folder (as in the cloud workspace). Safe to run again.
set -e
WPD=${1:?wordpress dir}
HERE=$(cd "$(dirname "$0")" && pwd)
WP="php $(dirname "$WPD")/wp-cli.phar --allow-root --path=$WPD"
python3 -I "$HERE/build.py"
ln -sfn "$HERE/encloud9-nine" "$WPD/wp-content/themes/encloud9-nine"
ln -sfn "$HERE/encloud9-site" "$WPD/wp-content/plugins/encloud9-site"
$WP plugin activate encloud9-site 2>/dev/null | tail -1
$WP theme activate encloud9-nine 2>/dev/null | tail -1
$WP rewrite structure '/blog/%postname%/' --hard 2>/dev/null | tail -1
$WP n9 import "$HERE/content/pages.json" 2>/dev/null | tail -1
$WP rewrite flush --hard 2>/dev/null | tail -1
