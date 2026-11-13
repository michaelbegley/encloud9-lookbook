<?php
/**
 * wp n9 import <pages.json>
 * Loads the pages built by wp-theme-fable/build.py. Safe to run again: each item is matched on its address
 * and updated in place, so post IDs are kept. On a site that already has pages, a page at the same address
 * is reused rather than duplicated.
 */
if (!defined('ABSPATH')) exit;

WP_CLI::add_command('n9 import', function ($args) {
    $file = $args[0] ?? '';
    if (!is_readable($file)) WP_CLI::error("Cannot read $file");
    $items = json_decode(file_get_contents($file), true);
    if (!is_array($items)) WP_CLI::error('Not a pages.json file');
    kses_remove_filters(); // the importer is run by a site admin; sections carry their own markup
    $by_path = [];
    $find = function ($path, $type) {
        $q = get_posts(['post_type' => $type, 'post_status' => 'any', 'meta_key' => '_n9_path', 'meta_value' => $path, 'numberposts' => 1, 'fields' => 'ids']);
        if ($q) return (int) $q[0];
        if ($type === 'page' && $path !== '/') { $p = get_page_by_path(trim($path, '/'), OBJECT, 'page'); if ($p) return $p->ID; }
        return 0;
    };
    $parent_of = function ($path) use (&$by_path, $find) {
        $parts = array_values(array_filter(explode('/', trim($path, '/'))));
        array_pop($parts);
        $parent = 0; $acc = '/';
        foreach ($parts as $seg) {
            $acc .= $seg . '/';
            $id = $by_path[$acc] ?? $find($acc, 'page');
            if (!$id) {
                // an address level with no page of its own in the design (for example /lp/): a private holding page,
                // so the pages under it keep their addresses and the level itself answers "not found" to visitors
                $id = wp_insert_post(['post_type' => 'page', 'post_status' => 'private', 'post_title' => ucwords(str_replace('-', ' ', $seg)),
                    'post_name' => $seg, 'post_parent' => $parent, 'post_content' => '']);
                update_post_meta($id, '_n9_path', $acc);
                update_post_meta($id, '_n9_noindex', '1');
                WP_CLI::log("holding page created at $acc");
            }
            $by_path[$acc] = $id; $parent = $id;
        }
        return $parent;
    };
    usort($items, function ($a, $b) {
        return [$a['type'] !== 'page', substr_count($a['path'], '/')] <=> [$b['type'] !== 'page', substr_count($b['path'], '/')];
    });
    $n = ['created' => 0, 'updated' => 0];
    $admins = get_users(['role' => 'administrator', 'number' => 1, 'orderby' => 'ID', 'fields' => 'ID']);
    $author = $admins ? (int) $admins[0] : 0;
    foreach ($items as $it) {
        $type = $it['type'];
        $post = [
            'post_type' => $type,
            'post_status' => $it['path'] === '/404/' ? 'private' : 'publish',
            'post_title' => preg_replace('/\s*\|\s*enCloud9$/', '', $it['title']),
            'post_excerpt' => $it['description'],
            'post_content' => wp_slash($it['content']),
            'post_name' => $it['slug'] ?: 'home',
            'post_author' => $author,
            'comment_status' => 'closed', 'ping_status' => 'closed',
            'page_template' => $it['template'] ?: 'default',
        ];
        if ($type !== 'page') unset($post['page_template']);
        if ($type === 'page') $post['post_parent'] = $it['path'] === '/' ? 0 : $parent_of($it['path']);
        $id = $find($it['path'], $type);
        if ($id) { $post['ID'] = $id; wp_update_post($post); $n['updated']++; }
        else { $id = wp_insert_post($post); $n['created']++; }
        if (is_wp_error($id) || !$id) { WP_CLI::warning('failed: ' . $it['path']); continue; }
        $by_path[$it['path']] = $id;
        $meta = [
            '_n9_path' => $it['path'], '_n9_old_mock_path' => $it['old'], '_n9_section' => $it['section'], '_n9_bodyclass' => $it['bodyclass'],
            '_n9_style' => $it['style'], '_n9_script' => $it['script'], '_n9_progress' => $it['progress'] ? '1' : '',
            '_n9_title' => $it['title'], '_n9_description' => $it['description'],
            '_n9_jsonld' => wp_json_encode($it['jsonld']), '_n9_noindex' => $it['noindex'] ? '1' : '',
        ];
        foreach ($meta as $k => $v) update_post_meta($id, $k, wp_slash($v));
    }
    if (!empty($by_path['/'])) { update_option('show_on_front', 'page'); update_option('page_on_front', $by_path['/']); }
    WP_CLI::success(wp_json_encode($n));
});

/**
 * wp n9 seo-export <file.csv>
 * Writes the page title, description and noindex flag the design carries for every imported page, with its
 * address and post ID, so they can be loaded into All in One SEO before it takes over the search tags.
 */
WP_CLI::add_command('n9 seo-export', function ($args) {
    $file = $args[0] ?? '';
    if (!$file) WP_CLI::error('Give a file to write');
    $out = fopen($file, 'w');
    fputcsv($out, ['post_id', 'post_type', 'address', 'title', 'description', 'noindex']);
    $n = 0;
    foreach (get_posts(['post_type' => ['page', 'post', 'story'], 'post_status' => ['publish', 'private'], 'numberposts' => -1, 'meta_key' => '_n9_title']) as $p) {
        fputcsv($out, [$p->ID, $p->post_type, get_post_meta($p->ID, '_n9_path', true), get_post_meta($p->ID, '_n9_title', true),
            get_post_meta($p->ID, '_n9_description', true), get_post_meta($p->ID, '_n9_noindex', true) ? 'yes' : '']);
        $n++;
    }
    fclose($out);
    WP_CLI::success("$n rows written to $file");
});
