#!/bin/sh
# usage: sh serve.sh <wordpress dir> <wp port> <repo root> <mock port>
# Same job as wp-theme/score/serve.sh, with four PHP workers so the editor test and the screenshots
# do not queue behind each other. Local test use only.
WP=$1; P=$2; R=$3; M=$4
cat > "$WP/../router.php" <<'PHP'
<?php
$root = getenv('WP_ROOT'); $p = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
if ($p !== '/' && file_exists($root.$p) && !is_dir($root.$p)) return false;
$_SERVER['SCRIPT_NAME'] = '/index.php'; chdir($root); require $root.'/index.php';
PHP
WP_ROOT="$WP" PHP_CLI_SERVER_WORKERS=4 setsid nohup php -S 127.0.0.1:$P -t "$WP" "$WP/../router.php" >/tmp/wp-$P.log 2>&1 </dev/null &
cd "$R" && setsid nohup python3 -m http.server $M >/tmp/mock-$M.log 2>&1 </dev/null &
sleep 2
