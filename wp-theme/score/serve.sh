#!/bin/sh
# usage: sh serve.sh <wordpress dir> <wp port> <repo root> <mock port>
# starts PHP's server for WordPress (pretty links through router.php) and a static server for the mock site
WP=$1; P=$2; R=$3; M=$4
cat > "$WP/../router.php" <<'PHP'
<?php
$root = getenv('WP_ROOT'); $p = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
if ($p !== '/' && file_exists($root.$p) && !is_dir($root.$p)) return false;
$_SERVER['SCRIPT_NAME'] = '/index.php'; chdir($root); require $root.'/index.php';
PHP
WP_ROOT="$WP" nohup php -S 127.0.0.1:$P -t "$WP" "$WP/../router.php" >/tmp/wp-$P.log 2>&1 &
cd "$R" && nohup python3 -m http.server $M >/tmp/mock-$M.log 2>&1 &
sleep 2
