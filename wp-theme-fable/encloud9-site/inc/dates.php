<?php
/**
 * Publish dates and authors filled in when a page is shown, from WordPress itself, so the "[publish date]"
 * and "[author]" placeholders from the design never reach a visitor (five-second test, 15 Nov 2026).
 * - Inside a link to another post or page: that post's date and byline.
 * - Elsewhere on a post or page: the page's own date.
 * - "checked [publish date]" is left alone: it claims someone checked a price or a list, so only a person sets it.
 */
if (!defined('ABSPATH')) exit;

function n9_date_for($id) { return $id ? get_the_date('j M Y', $id) : ''; }

function n9_byline_for($id) {
	if (!$id) return '';
	$b = (string) get_post_meta($id, '_n9_byline', true);
	if ($b === '' && preg_match('#<span>By ([^<]{2,60})</span>#', (string) get_post_field('post_content', $id), $m)) $b = trim($m[1]);
	return $b !== '' ? $b : 'enCloud9';
}

function n9_fill_dates($html) {
	if (strpos($html, '[publish date]') === false && strpos($html, '[author]') === false) return $html;
	// Links to other posts first.
	$html = preg_replace_callback('#<a\b([^>]*)>(.*?)</a>#s', function ($m) {
		if (strpos($m[2], '[publish date]') === false && strpos($m[2], '[author]') === false) return $m[0];
		if (!preg_match('#href="([^"]+)"#', $m[1], $h)) return $m[0];
		$path = (string) parse_url(html_entity_decode($h[1]), PHP_URL_PATH);
		// The design links with ../ paths; resolve them against the site root.
		$path = '/' . ltrim(preg_replace('#^(\.\./)+#', '', $path), '/');
		$path = trailingslashit($path);
		$id = n9_find_by_path($path) ?: url_to_postid(home_url($path));
		if (!$id) return $m[0];
		$inner = preg_replace('#(?<!checked )\[publish date\]#', esc_html(n9_date_for($id)), $m[2]);
		$inner = str_replace('[author]', esc_html(n9_byline_for($id)), $inner);
		return '<a' . $m[1] . '>' . $inner . '</a>';
	}, $html);
	// Then the page's own date.
	$own = get_queried_object_id();
	if ($own) $html = preg_replace('#(?<!checked )\[publish date\]#', esc_html(n9_date_for($own)), $html);
	return $html;
}

add_filter('render_block', function ($content) {
	return is_admin() ? $content : n9_fill_dates((string) $content);
}, 20);
