<?php
/**
 * Send every plain http page view to the same address on https (301).
 *
 * Why: on 17 Nov 2026 the staging site answered http://encloud9-new.flywheelsites.com/
 * with a 200 (no redirect), so a phone that typed the bare address got the http page.
 *
 * Safe by design:
 * - only when the site's own home address is https;
 * - only GET and HEAD (a 301 would turn a form POST into a GET);
 * - never wp-admin, wp-login.php, REST, cron or WP-CLI, so admin always stays
 *   reachable to roll this back;
 * - treats a request as https if the host's proxy says so (X-Forwarded-Proto,
 *   X-Forwarded-SSL, CF-Visitor), so it cannot loop behind a proxy;
 * - only for this site's own host name.
 */
if (!defined('ABSPATH')) exit;

function n9_request_is_https() {
    if (is_ssl()) return true;
    $p = strtolower((string) ($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? ''));
    if ($p !== '' && strpos($p, 'https') !== false) return true;
    if (strtolower((string) ($_SERVER['HTTP_X_FORWARDED_SSL'] ?? '')) === 'on') return true;
    if (strpos((string) ($_SERVER['HTTP_CF_VISITOR'] ?? ''), 'https') !== false) return true;
    return false;
}

add_action('init', function () {
    if (n9_request_is_https()) return;
    if (defined('WP_CLI') || wp_doing_cron() || wp_doing_ajax()) return;
    if (is_admin()) return;
    $method = strtoupper((string) ($_SERVER['REQUEST_METHOD'] ?? 'GET'));
    if ($method !== 'GET' && $method !== 'HEAD') return;
    $uri = (string) ($_SERVER['REQUEST_URI'] ?? '/');
    if (strpos($uri, '/wp-login.php') === 0 || strpos($uri, '/wp-json/') === 0 || strpos($uri, '/wp-admin') === 0) return;
    $home = home_url('/');
    if (strpos($home, 'https://') !== 0) return;
    $home_host = strtolower((string) parse_url($home, PHP_URL_HOST));
    $req_host = strtolower(preg_replace('/:\d+$/', '', (string) ($_SERVER['HTTP_HOST'] ?? '')));
    if ($req_host === '' || $req_host !== $home_host) return;
    nocache_headers();
    header('Location: https://' . $home_host . $uri, true, 301);
    exit;
}, 0);

/*
 * Browser-side backstop: if a page is ever shown over http anyway (a host
 * layer or cache answers before WordPress, or the server cannot tell the
 * scheme), the first thing in <head> moves the visitor to https before any
 * styles load.
 */
add_action('wp_head', function () {
    echo "<script>if(location.protocol==='http:'&&location.hostname!=='localhost'){location.replace('https:'+location.href.slice(5));}</script>\n";
}, -1000);
