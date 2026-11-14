<?php
/**
 * Tools > enCloud9 import: loads the bundled data/pages.json from wp-admin, for hosts where WP-CLI is not
 * reachable. Site admins only, behind a nonce. Safe to run again (pages are matched on their address).
 */
if (!defined('ABSPATH')) exit;
require_once __DIR__ . '/import.php';

add_action('admin_menu', function () {
    add_management_page('enCloud9 import', 'enCloud9 import', 'manage_options', 'n9-import', 'n9_import_screen');
});

function n9_import_screen() {
    if (!current_user_can('manage_options')) wp_die('Not allowed');
    $file = dirname(__DIR__) . '/data/pages.json';
    echo '<div class="wrap"><h1>enCloud9 import</h1>';
    if (isset($_POST['n9_run']) && check_admin_referer('n9_import')) {
        @set_time_limit(600);
        $items = is_readable($file) ? json_decode(file_get_contents($file), true) : null;
        if (!is_array($items)) {
            echo '<div class="notice notice-error"><p>data/pages.json is missing or unreadable.</p></div>';
        } else {
            $lines = [];
            $n = n9_import_items($items, function ($m) use (&$lines) { $lines[] = $m; });
            if (!empty($_POST['n9_permalinks'])) { update_option('permalink_structure', '/blog/%postname%/'); flush_rewrite_rules(); }
            echo '<div class="notice notice-success"><p>Done: ' . (int) $n['created'] . ' created, ' . (int) $n['updated'] . ' updated.</p></div>';
            if ($lines) echo '<pre>' . esc_html(implode("\n", $lines)) . '</pre>';
        }
    }
    $count = is_readable($file) ? count((array) json_decode(file_get_contents($file), true)) : 0;
    echo '<p>Bundled file: data/pages.json, ' . (int) $count . ' items. Running it again updates pages in place.</p>';
    echo '<form method="post">';
    wp_nonce_field('n9_import');
    echo '<p><label><input type="checkbox" name="n9_permalinks" value="1" checked> Set permalinks to /blog/%postname%/</label></p>';
    submit_button('Import pages', 'primary', 'n9_run');
    echo '</form></div>';
}
