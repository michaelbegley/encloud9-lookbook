<?php
/**
 * enCloud9 Nine: the look of encloud9.com (Look 9). Agent 6 run 1, 13 Nov 2026.
 * Content types, blocks and search tags live in the enCloud9 Site plugin; this file is presentation only.
 */
if (!defined('ABSPATH')) exit;

define('N9_VER', '0.2.0');

add_action('after_setup_theme', function () {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('responsive-embeds');
    add_theme_support('html5', ['search-form', 'gallery', 'caption', 'style', 'script']);
    remove_theme_support('core-block-patterns');
});

function n9_manifest() {
    static $m;
    if ($m === null) $m = json_decode((string) @file_get_contents(get_theme_file_path('inc/manifest.json')), true) ?: [];
    return $m;
}

/* The post whose page settings apply: the page being shown, or the private "404" page on a 404. */
function n9_page_id() {
    if (function_exists('n9_meta_post_id')) return n9_meta_post_id();
    return is_singular() ? get_queried_object_id() : 0;
}

/* A page setting, with the post type's default for posts and stories written after the import. */
function n9_setting($id, $key) {
    if (!$id) return '';
    $v = get_post_meta($id, '_n9_' . $key, true);
    if ($v !== '' && $v !== false) return $v;
    if (metadata_exists('post', $id, '_n9_' . $key)) return '';
    return n9_manifest()[$key][get_post_type($id)] ?? '';
}

function n9_page_file($kind, $name) {
    if (!$name || !preg_match('/^[a-z0-9-]+$/', $name)) return '';
    $f = get_theme_file_path("assets/$kind/page/$name.$kind");
    return is_readable($f) ? trim(file_get_contents($f)) : '';
}

/* Styles in the mock's order: the shared sheet, then the page's own styles, then the site-wide scale, then theme fixes.
   One request; the rest is printed in the head, so nothing blocks on a second file. */
add_action('wp_enqueue_scripts', function () {
    wp_enqueue_style('n9', get_theme_file_uri('assets/css/nine.css'), [], N9_VER);
    $css = n9_page_file('css', n9_setting(n9_page_id(), 'style'));
    $css .= "\n" . file_get_contents(get_theme_file_path('assets/css/nine-scale.css'));
    $css .= "\n" . file_get_contents(get_theme_file_path('assets/css/wp.css'));
    wp_add_inline_style('n9', $css);
    wp_enqueue_script('n9', get_theme_file_uri('assets/js/nine.js'), [], N9_VER, ['strategy' => 'defer', 'in_footer' => false]);
});

/* The editor canvas wears the same styles, so a section looks in the editor as it does on the site.
   They are handed to the editor as settings and placed inside the canvas frame only (the enCloud9 Site plugin
   does that), so they never touch the WordPress admin screens around it. */
add_filter('block_editor_settings_all', function ($s, $ctx) {
    $id = !empty($ctx->post) ? $ctx->post->ID : 0;
    $scale = file_get_contents(get_theme_file_path('assets/css/nine-scale.css'));
    // on the site the scale rules are scoped to <main>; in the editor the page body is the canvas itself
    $scale = str_replace('html body main ', 'html body ', $scale);
    $s['n9Canvas'] = [
        'href' => get_theme_file_uri('assets/css/nine.css') . '?ver=' . N9_VER,
        'css' => n9_page_file('css', n9_setting($id, 'style')) . "\n" . $scale . "\n" . file_get_contents(get_theme_file_path('assets/css/editor.css')),
        'bodyClass' => $id ? (string) n9_setting($id, 'bodyclass') : '',
    ];
    return $s;
}, 10, 2);

/* Fonts the first screen needs are fetched early (two weights; the others load when used). */
add_action('wp_head', function () {
    foreach (['400', '600'] as $w) {
        echo '<link rel="preload" as="font" type="font/woff2" crossorigin href="' . esc_url(get_theme_file_uri("assets/fonts/hanken-grotesk-latin-$w-normal.woff2")) . '">' . "\n";
    }
}, 1);

/* Page scripts sat after </main> in the mock; they are printed in the same place. */
add_action('wp_footer', function () {
    $js = n9_page_file('js', n9_setting(n9_page_id(), 'script'));
    if ($js) echo '<script id="n9-page-js">' . $js . "</script>\n";
}, 20);

/* The reading progress bar sits before the header on posts. */
add_action('wp_body_open', function () {
    if (n9_setting(n9_page_id(), 'progress')) echo '<div class="progress" aria-hidden="true"><i></i></div>' . "\n";
});

add_filter('body_class', function ($c) {
    $b = n9_setting(n9_page_id(), 'bodyclass');
    return $b ? array_merge($c, preg_split('/\s+/', $b)) : $c;
});

/* Which top menu item is the current section. */
function n9_current_section() {
    if (is_singular()) {
        $s = get_post_meta(get_queried_object_id(), '_n9_section', true);
        if ($s) return $s;
        if (is_singular('story')) return 'stories';
        if (is_singular('post')) return 'blog';
    }
    if (is_home() || is_category() || is_tag() || is_author() || is_date()) return 'blog';
    return '';
}

/* The header is a template part an admin can edit; the current section is marked as it is printed. */
add_filter('render_block_core/template-part', function ($html, $block) {
    if (($block['attrs']['slug'] ?? '') !== 'header') return $html;
    $map = ['d365' => '/power-platform-dynamics-365/', 'marketing' => '/marketing-services/', 'copilot' => '/microsoft-copilot-for-business/',
            'packages' => '/packages/', 'stories' => '/about-encloud9/microsoft-dynamics-365-success/', 'blog' => '/blog/', 'about' => '/about-encloud9/'];
    $cur = n9_current_section();
    if (!$cur || !isset($map[$cur])) return $html;
    return preg_replace('#(<nav class="nav"[^>]*>.*?)<a href="' . preg_quote($map[$cur], '#') . '">([^<]+)</a>#s',
        '$1<a href="' . $map[$cur] . '" class="cur">$2<span class="sr-only"> (current section)</span></a>', $html, 1);
}, 10, 2);

/* Keep the approved copy exactly as written: no curly-quote swaps, smileys or respellings. */
add_filter('run_wptexturize', '__return_false');
remove_filter('the_content', 'convert_smilies', 20);
remove_filter('the_content', 'capital_P_dangit', 11);
remove_filter('the_title', 'capital_P_dangit', 11);

/* Nothing the site does not use. The design has its own skip link, so WordPress does not add a second one. */
add_action('init', function () {
    remove_action('wp_head', 'print_emoji_detection_script', 7);
    remove_action('wp_print_styles', 'print_emoji_styles');
    remove_action('admin_print_scripts', 'print_emoji_detection_script');
    remove_action('wp_head', 'wp_generator');
    remove_action('wp_head', 'wlwmanifest_link');
    remove_action('wp_head', 'rsd_link');
    remove_action('wp_footer', 'the_block_template_skip_link');
    remove_action('wp_enqueue_scripts', 'wp_enqueue_block_template_skip_link');
});

/* Images: the first image on a page is never lazy-loaded (it may be the largest thing on the first screen). */
add_filter('wp_omit_loading_attr_threshold', function () { return 1; });

/* WordPress underlines every link by default at a strength that would beat the design's own link rules.
   The design decides where links are underlined, so that one default is dropped. */
add_filter('wp_theme_json_data_default', function ($json) {
    $d = $json->get_data();
    unset($d['styles']['elements']['link']);
    return new WP_Theme_JSON_Data($d, 'default');
});
