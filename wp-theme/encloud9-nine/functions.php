<?php
/**
 * enCloud9 Nine theme. Draft 1, 13 Nov 2026.
 * Header and footer are server-rendered blocks so the current section can be marked per page.
 * Page bodies come from wp-theme/content/pages.json through wp-theme/import.php.
 */
if (!defined('ABSPATH')) exit;

define('N9_VER', '0.1.0');

add_action('after_setup_theme', function () {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('responsive-embeds');
    add_theme_support('html5', ['search-form', 'gallery', 'caption', 'style', 'script']);
    remove_theme_support('core-block-patterns');
});

/* Styles and script: the same files the mock site uses, plus theme fixes. */
add_action('wp_enqueue_scripts', function () {
    $u = get_theme_file_uri('assets/pages/');
    wp_enqueue_style('n9', $u . 'nine.css', [], N9_VER);
    wp_enqueue_style('n9-scale', $u . 'nine-scale.css', ['n9'], N9_VER);
    wp_enqueue_style('n9-wp', get_theme_file_uri('assets/wp.css'), ['n9-scale'], N9_VER);
    wp_enqueue_script('n9', $u . 'nine.js', [], N9_VER, ['strategy' => 'defer', 'in_footer' => false]);
});

/* Nothing the site does not use. */
add_action('init', function () {
    remove_action('wp_head', 'print_emoji_detection_script', 7);
    remove_action('wp_print_styles', 'print_emoji_styles');
    remove_action('wp_head', 'wp_generator');
    remove_action('wp_head', 'wlwmanifest_link');
    remove_action('wp_head', 'rsd_link');
});

/* Client stories live at /stories/<client>/ (site move standard, approved 12 Nov 2026). */
add_action('init', function () {
    register_post_type('story', [
        'label' => 'Client stories',
        'labels' => ['singular_name' => 'Client story', 'add_new_item' => 'Add client story'],
        'public' => true,
        'show_in_rest' => true,
        'has_archive' => false,
        'menu_icon' => 'dashicons-awards',
        'rewrite' => ['slug' => 'stories', 'with_front' => false],
        'supports' => ['title', 'editor', 'excerpt', 'thumbnail', 'custom-fields', 'revisions'],
    ]);
    foreach (['_n9_section', '_n9_bodyclass', '_n9_description', '_n9_jsonld', '_n9_path', '_n9_noindex'] as $k) {
        register_post_meta('', $k, ['single' => true, 'type' => 'string', 'show_in_rest' => false,
            'auth_callback' => function () { return current_user_can('edit_posts'); }]);
    }
});

/* Server-rendered blocks: header, footer, and a page body by its old mock path (used by 404). */
add_action('init', function () {
    register_block_type('encloud9/site-header', ['render_callback' => 'n9_render_header', 'supports' => ['html' => false]]);
    register_block_type('encloud9/site-footer', ['render_callback' => 'n9_render_footer', 'supports' => ['html' => false]]);
    register_block_type('encloud9/page-content', ['attributes' => ['path' => ['type' => 'string']], 'render_callback' => 'n9_render_page_content']);
});

/* The post whose stored head, styles and scripts apply: the current page, or the 404 page body on a 404. */
function n9_meta_id() {
    if (is_singular()) return get_queried_object_id();
    if (is_404()) {
        $q = get_posts(['post_type' => 'page', 'post_status' => ['publish', 'private'], 'meta_key' => '_n9_path', 'meta_value' => '/404/', 'numberposts' => 1, 'fields' => 'ids']);
        return $q ? $q[0] : 0;
    }
    return 0;
}

/* Keep the approved copy exactly as written: no automatic curly quotes or dash swaps. */
add_filter('run_wptexturize', '__return_false');

function n9_current_section() {
    if (is_singular()) {
        $s = get_post_meta(get_queried_object_id(), '_n9_section', true);
        if ($s) return $s;
        if (is_singular('story')) return 'stories';
        if (is_singular('post')) return 'blog';
    }
    if (is_home() || is_category() || is_tag() || is_author()) return 'blog';
    return '';
}

function n9_render_header() {
    // a page with its own header (the ad landing page with no menu) keeps it
    $own = ($id = n9_meta_id()) ? get_post_meta($id, '_n9_header', true) : '';
    if ($own) return n9_links($own);
    $h = file_get_contents(get_theme_file_path('inc/header.html'));
    $map = ['d365' => '/power-platform-dynamics-365/', 'marketing' => '/marketing-services/', 'copilot' => '/microsoft-copilot-for-business/',
            'packages' => '/packages/', 'stories' => '/about-encloud9/microsoft-dynamics-365-success/', 'blog' => '/blog/', 'about' => '/about-encloud9/'];
    $cur = n9_current_section();
    if ($cur && isset($map[$cur])) {
        $href = $map[$cur];
        // mark only the top-level link of the current section (first match inside the main nav)
        $h = preg_replace('#(<nav class="nav"[^>]*>.*?)<a href="' . preg_quote($href, '#') . '">([^<]+)</a>#s',
            '$1<a href="' . $href . '" class="cur">$2<span class="sr-only"> (current section)</span></a>', $h, 1);
    }
    return n9_links($h);
}

function n9_render_footer() {
    $f = file_get_contents(get_theme_file_path('inc/footer.html'));
    return '<div class="site-foot"><div class="wrap">' . n9_links(preg_replace('#(<div class="scale".*)$#s', '', $f)) . '</div>'
        . (preg_match('#<div class="scale".*$#s', $f, $m) ? $m[0] : '') . '</div>';
}

function n9_render_page_content($a) {
    $q = get_posts(['post_type' => 'any', 'post_status' => ['publish', 'private'], 'meta_key' => '_n9_path', 'meta_value' => $a['path'] ?? '', 'numberposts' => 1]);
    return $q ? do_blocks($q[0]->post_content) : '';
}

/* Root-relative links work on Local, staging and live alike; this keeps them right if WordPress sits in a subfolder. */
function n9_links($html) {
    $base = rtrim(wp_parse_url(home_url('/'), PHP_URL_PATH) ?: '/', '/');
    if ($base === '') return $html;
    return preg_replace('#href="/(?!/)#', 'href="' . $base . '/', $html);
}

add_filter('body_class', function ($c) {
    if ($id = n9_meta_id()) {
        $b = get_post_meta($id, '_n9_bodyclass', true);
        if ($b) $c = array_merge($c, preg_split('/\s+/', $b));
    }
    return $c;
});

/* Head: description and JSON-LD carried over from the mock until All in One SEO takes over (checklist: one owner per tag). */
add_action('wp_head', function () {
    if (!is_singular() || defined('AIOSEO_VERSION')) return;
    $id = get_queried_object_id();
    $d = get_post_meta($id, '_n9_description', true);
    if ($d) echo '<meta name="description" content="' . esc_attr($d) . '">' . "\n";
    if (get_post_meta($id, '_n9_noindex', true)) echo '<meta name="robots" content="noindex">' . "\n";
    $ld = json_decode((string) get_post_meta($id, '_n9_jsonld', true), true);
    if (is_array($ld)) foreach ($ld as $j) echo '<script type="application/ld+json">' . $j . "</script>\n";
}, 5);

/* Page-specific styles from the mock's head, printed after the theme styles (same order as the mock). */
add_action('wp_head', function () {
    if (!($id = n9_meta_id())) return;
    $c = get_post_meta($id, '_n9_css', true);
    if ($c) echo '<style id="n9-page-css">' . $c . "</style>\n";
}, 20);

/* Page scripts that sat after </main> in the mock (reading progress, contents rail and the like). */
add_action('wp_footer', function () {
    if (!($id = n9_meta_id())) return;
    $j = get_post_meta($id, '_n9_js', true);
    if ($j) echo '<script id="n9-page-js">' . $j . "</script>\n";
}, 20);

/* Markup the mock placed before the header (the reading progress bar on posts). */
add_action('wp_body_open', function () {
    if (!($id = n9_meta_id())) return;
    $b = get_post_meta($id, '_n9_before', true);
    if ($b) echo $b . "\n";
});

/* The mock sets <title> per page; WordPress builds it from the post title, so use the stored one when present. */
add_filter('pre_get_document_title', function ($t) {
    if (is_singular() && !defined('AIOSEO_VERSION')) {
        $s = get_post_meta(get_queried_object_id(), '_n9_title', true);
        if ($s) return $s;
    }
    return $t;
});
