<?php
/**
 * Plugin Name: enCloud9 Site
 * Description: What belongs to the site's content, not its look: client stories, the Section and Container blocks, the layout guard, the search tags carried from the design until All in One SEO takes over, and the page importer (wp n9 import).
 * Version: 0.2.0
 * Author: enCloud9
 * Requires at least: 6.6
 * Requires PHP: 7.4
 *
 * Kept apart from the theme so a theme change never takes the content types or blocks with it.
 */
if (!defined('ABSPATH')) exit;

define('N9_SITE_VER', '0.2.0');
define('N9_SITE_DIR', __DIR__);

/* Who may change structure (unlock, code editor): people who can already edit the theme. */
function n9_can_restructure() {
    return current_user_can('edit_theme_options');
}

/* ------------------------------------------------------------------ content types and fields */
add_action('init', function () {
    register_post_type('story', [
        'label' => 'Client stories',
        'labels' => ['singular_name' => 'Client story', 'add_new_item' => 'Add client story', 'edit_item' => 'Edit client story'],
        'public' => true,
        'show_in_rest' => true,
        'has_archive' => false,
        'menu_icon' => 'dashicons-awards',
        'menu_position' => 21,
        'rewrite' => ['slug' => 'stories', 'with_front' => false],
        'supports' => ['title', 'editor', 'excerpt', 'thumbnail', 'custom-fields', 'revisions'],
    ]);
    // Per-page settings carried from the design. Set by the importer; not shown to editors.
    foreach (['_n9_path', '_n9_old_mock_path', '_n9_section', '_n9_bodyclass', '_n9_style', '_n9_script', '_n9_progress',
              '_n9_title', '_n9_description', '_n9_jsonld', '_n9_noindex'] as $k) {
        register_post_meta('', $k, ['single' => true, 'type' => 'string', 'show_in_rest' => false,
            'auth_callback' => 'n9_can_restructure']);
    }
});

/* ------------------------------------------------------------------ blocks */
add_action('init', function () {
    wp_register_script('n9-blocks', plugins_url('blocks/editor.js', __FILE__),
        ['wp-blocks', 'wp-element', 'wp-block-editor', 'wp-components', 'wp-data', 'wp-notices'], N9_SITE_VER, true);
    wp_register_style('n9-blocks-editor', plugins_url('blocks/editor.css', __FILE__), [], N9_SITE_VER);
    $common = ['api_version' => 3, 'editor_script_handles' => ['n9-blocks'], 'editor_style_handles' => ['n9-blocks-editor']];
    register_block_type('encloud9/section', $common);
    register_block_type('encloud9/box', $common);
    // A page's blocks shown somewhere else by its address (the 404 template shows the private "404" page).
    register_block_type('encloud9/page-content', ['api_version' => 3, 'attributes' => ['path' => ['type' => 'string']],
        'render_callback' => function ($a) {
            $id = n9_find_by_path($a['path'] ?? '');
            return $id ? do_blocks(get_post($id)->post_content) : '';
        }]);
});

add_action('enqueue_block_editor_assets', function () {
    wp_add_inline_script('n9-blocks', 'window.n9Editor=' . wp_json_encode(['canRestructure' => n9_can_restructure()]) . ';', 'before');
});

/* Editors change words, links and images. Unlocking blocks and the code view are for site admins. */
add_filter('block_editor_settings_all', function ($s) {
    if (!n9_can_restructure()) {
        $s['canLockBlocks'] = false;
        $s['codeEditingEnabled'] = false;
    }
    return $s;
});

function n9_find_by_path($path) {
    static $memo = [];
    if (isset($memo[$path])) return $memo[$path];
    $q = get_posts(['post_type' => ['page', 'post', 'story'], 'post_status' => ['publish', 'private'], 'meta_key' => '_n9_path',
        'meta_value' => $path, 'numberposts' => 1, 'fields' => 'ids']);
    return $memo[$path] = ($q ? (int) $q[0] : 0);
}

/* ------------------------------------------------------------------ the layout guard
 * The editor only lets words, link targets and images change inside a Section, and lets a writer add or remove
 * a copy of a repeated item (a question, a table row, a list item). This is the matching rule on the server, so
 * it also holds for anything that saves another way: a Section saved by someone who is not a site admin may
 * only contain kinds of elements (tag and class) that a Section with the same outer element already had on
 * that page, or has in a theme pattern. New kinds of markup, scripts and frames are refused.
 * It is a guard against accidents, not a security wall: WordPress trusts Editors with HTML on a single site. */
function n9_tokens($html) {
    $out = [];
    if (!preg_match_all('#<([a-zA-Z][a-zA-Z0-9]*)((?:\s+[^<>]*)?)>#', preg_replace('#<!--.*?-->#s', '', $html), $m, PREG_SET_ORDER)) return $out;
    foreach ($m as $t) {
        $tag = strtolower($t[1]);
        if ($tag === 'br') continue;
        if (in_array($tag, ['b', 'i', 'strong', 'em', 'u'], true) && trim($t[2], " /") === '') continue;
        $cls = preg_match('#\sclass\s*=\s*"([^"]*)"#', $t[2], $c) ? trim(preg_replace('#\s+#', ' ', $c[1])) : '';
        $out[] = $tag . '.' . $cls;
    }
    return $out;
}

/* Every Section and Container in some content: [outer element => [kinds of element inside]]. */
function n9_section_kinds($content, &$into) {
    $walk = function ($blocks) use (&$walk, &$into) {
        foreach ($blocks as $b) {
            if ($b['blockName'] === 'encloud9/section' || $b['blockName'] === 'encloud9/box') {
                $html = $b['blockName'] === 'encloud9/box' ? implode('', array_filter($b['innerContent'], 'is_string')) : $b['innerHTML'];
                $t = n9_tokens($html);
                if (!$t) { $into['(empty)'] = []; }
                else {
                    $root = ($b['blockName'] === 'encloud9/box' ? 'box:' : '') . $t[0];
                    $into[$root] = ($into[$root] ?? []) + array_flip($t);
                }
            }
            if (!empty($b['innerBlocks'])) $walk($b['innerBlocks']);
        }
    };
    $walk(parse_blocks($content));
}

function n9_guard($prepared, $request) {
    if (n9_can_restructure() || !isset($prepared->post_content)) return $prepared;
    $known = []; $new = [];
    if (!empty($prepared->ID)) n9_section_kinds(get_post($prepared->ID)->post_content, $known);
    foreach (WP_Block_Patterns_Registry::get_instance()->get_all_registered() as $p) n9_section_kinds($p['content'] ?? '', $known);
    n9_section_kinds(wp_unslash($prepared->post_content), $new);
    foreach ($new as $root => $kinds) {
        if (!isset($known[$root]) || array_diff_key($kinds, $known[$root])) {
            return new WP_Error('n9_layout_locked',
                'A section\'s layout was changed, so this was not saved. Words, links and images can be changed; the layout cannot. Undo the last change and save again.',
                ['status' => 400]);
        }
    }
    return $prepared;
}
foreach (['page', 'post', 'story'] as $n9_t) add_filter("rest_pre_insert_$n9_t", 'n9_guard', 10, 2);

/* Editors do not get the blocks that hold raw code. */
add_filter('allowed_block_types_all', function ($allowed, $ctx) {
    if (n9_can_restructure()) return $allowed;
    $all = is_array($allowed) ? $allowed : array_keys(WP_Block_Type_Registry::get_instance()->get_all_registered());
    return array_values(array_diff($all, ['core/html', 'core/shortcode', 'core/freeform']));
}, 10, 2);

/* ------------------------------------------------------------------ search tags, until All in One SEO owns them */
function n9_seo_owned_elsewhere() {
    return defined('AIOSEO_VERSION') || defined('AIOSEO_FILE') || function_exists('aioseo');
}

function n9_meta_post_id() {
    if (is_singular()) return get_queried_object_id();
    if (is_404()) return n9_find_by_path('/404/');
    return 0;
}

add_filter('pre_get_document_title', function ($t) {
    if (n9_seo_owned_elsewhere() || !is_singular()) return $t;
    $s = get_post_meta(get_queried_object_id(), '_n9_title', true);
    return $s ?: $t;
});

add_action('wp_head', function () {
    if (n9_seo_owned_elsewhere() || !is_singular()) return;
    $id = get_queried_object_id();
    $title = get_post_meta($id, '_n9_title', true) ?: wp_get_document_title();
    $d = get_post_meta($id, '_n9_description', true);
    $url = get_permalink($id);
    if ($d) echo '<meta name="description" content="' . esc_attr($d) . '">' . "\n";
    echo '<meta property="og:site_name" content="enCloud9">' . "\n";
    echo '<meta property="og:type" content="' . (is_singular('post') ? 'article' : 'website') . '">' . "\n";
    echo '<meta property="og:title" content="' . esc_attr($title) . '">' . "\n";
    if ($d) echo '<meta property="og:description" content="' . esc_attr($d) . '">' . "\n";
    echo '<meta property="og:url" content="' . esc_url($url) . '">' . "\n";
    $card = get_theme_file_path('assets/brand/share-card.png');
    if (file_exists($card)) {
        echo '<meta property="og:image" content="' . esc_url(get_theme_file_uri('assets/brand/share-card.png')) . '">' . "\n";
        echo '<meta property="og:image:width" content="1200">' . "\n" . '<meta property="og:image:height" content="630">' . "\n";
        echo '<meta property="og:image:alt" content="enCloud9, Microsoft Dynamics 365 partner in Bellevue, Nebraska">' . "\n";
    }
    echo '<meta name="twitter:card" content="summary_large_image">' . "\n";
    $ld = json_decode((string) get_post_meta($id, '_n9_jsonld', true), true);
    if (is_array($ld)) foreach ($ld as $j) echo '<script type="application/ld+json">' . $j . "</script>\n";
}, 5);

/* Pages that must stay out of search (thank-you pages, the 404 body). Works with or without an SEO plugin. */
add_filter('wp_robots', function ($r) {
    $id = n9_meta_post_id();
    if ($id && get_post_meta($id, '_n9_noindex', true)) { $r['noindex'] = true; unset($r['max-image-preview']); }
    return $r;
});

/* ------------------------------------------------------------------ importer */
if (defined('WP_CLI') && WP_CLI) {
    require_once __DIR__ . '/inc/import.php';
}
