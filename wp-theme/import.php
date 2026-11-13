<?php
/**
 * Load content/pages.json into WordPress. Run with WP-CLI:
 *   wp eval-file wp-theme/import.php wp-theme/content/pages.json
 * Safe to run again: each item is matched on its new address (_n9_path) and updated in place.
 * On the real site, pages that already exist are matched by address first so post IDs are kept (B5 2.4).
 */
if (!defined('ABSPATH')) { echo "Run through wp eval-file\n"; exit(1); }
$file = $args[0] ?? __DIR__ . '/content/pages.json';
$items = json_decode(file_get_contents($file), true);
$noindex = ['/thank-you/', '/thank-you-contact/', '/request-received/', '/newsletter-signup-successful/', '/call-prep/', '/404/'];
kses_remove_filters(); // page bodies carry their own markup and scripts; only admins run this
$by_path = [];
function n9_find($path, $type) {
    $q = get_posts(['post_type' => $type, 'post_status' => 'any', 'meta_key' => '_n9_path', 'meta_value' => $path, 'numberposts' => 1]);
    if ($q) return $q[0]->ID;
    if ($type === 'page') { $p = get_page_by_path(trim($path, '/'), OBJECT, 'page'); if ($p) return $p->ID; }
    return 0;
}
function n9_parent($path, &$by_path) {
    $parts = array_values(array_filter(explode('/', trim($path, '/'))));
    array_pop($parts);
    $parent = 0; $acc = '/';
    foreach ($parts as $seg) {
        $acc .= $seg . '/';
        $id = $by_path[$acc] ?? n9_find($acc, 'page');
        if (!$id) {
            $id = wp_insert_post(['post_type' => 'page', 'post_status' => 'publish', 'post_title' => ucwords(str_replace('-', ' ', $seg)),
                'post_name' => $seg, 'post_parent' => $parent, 'post_content' => '']);
            update_post_meta($id, '_n9_path', $acc);
            update_post_meta($id, '_n9_noindex', '1');
            echo "parent created $acc\n";
        }
        $by_path[$acc] = $id; $parent = $id;
    }
    return $parent;
}
// pages first, shortest address first, so parents exist before children
usort($items, function ($a, $b) { return [$a['type'] !== 'page', substr_count($a['path'], '/')] <=> [$b['type'] !== 'page', substr_count($b['path'], '/')]; });
$n = ['created' => 0, 'updated' => 0];
foreach ($items as $it) {
    $type = $it['type'];
    $title = preg_replace('/\s*\|\s*enCloud9$/', '', $it['title']);
    $post = ['post_type' => $type, 'post_status' => $it['path'] === '/404/' ? 'private' : 'publish', 'post_title' => $title,
        'post_content' => wp_slash($it['content']), 'post_name' => $it['slug'] ?: 'home'];
    if ($type === 'page') $post['post_parent'] = $it['path'] === '/' ? 0 : n9_parent($it['path'], $by_path);
    $id = n9_find($it['path'], $type);
    if ($id) { $post['ID'] = $id; wp_update_post($post); $n['updated']++; } else { $id = wp_insert_post($post); $n['created']++; }
    $by_path[$it['path']] = $id;
    update_post_meta($id, '_n9_path', $it['path']);
    update_post_meta($id, '_n9_old_mock_path', $it['old']);
    update_post_meta($id, '_n9_section', $it['section']);
    update_post_meta($id, '_n9_bodyclass', $it['bodyclass']);
    update_post_meta($id, '_n9_title', $it['title']);
    update_post_meta($id, '_n9_description', $it['description']);
    update_post_meta($id, '_n9_css', wp_slash($it['css'] ?? ''));
    update_post_meta($id, '_n9_js', wp_slash($it['js'] ?? ''));
    update_post_meta($id, '_n9_before', wp_slash($it['before'] ?? ''));
    update_post_meta($id, '_n9_header', wp_slash($it['header'] ?? ''));
    update_post_meta($id, '_n9_jsonld', wp_slash(json_encode($it['jsonld'])));
    update_post_meta($id, '_n9_noindex', in_array($it['path'], $noindex, true) ? '1' : '');
}
$home = $by_path['/'] ?? 0;
if ($home) { update_option('show_on_front', 'page'); update_option('page_on_front', $home); }
echo json_encode($n) . "\n";
