<?php
/**
 * Search and AI-answer basics for the imported old blog posts, which carry no design meta of their own
 * (AI-answer check, 15 Nov 2026): "<title> | enCloud9", a meta description from the post's excerpt,
 * and BlogPosting structured data (headline, dates, author, publisher, image).
 */
if (!defined('ABSPATH')) exit;

function n9_is_legacy_post($id) {
	return $id && get_post_type($id) === 'post' && get_post_meta($id, '_n9_legacy_id', true) && !get_post_meta($id, '_n9_title', true);
}

function n9_legacy_desc($id) {
	$t = trim(wp_strip_all_tags((string) get_post_field('post_excerpt', $id)));
	if ($t === '') $t = trim(wp_strip_all_tags(strip_shortcodes((string) get_post_field('post_content', $id))));
	$t = preg_replace('/\s+/', ' ', html_entity_decode($t, ENT_QUOTES, 'UTF-8'));
	if (mb_strlen($t) > 158) $t = rtrim(mb_substr($t, 0, 155), " ,.;:") . '...';
	return $t;
}

add_filter('pre_get_document_title', function ($t) {
	if (!is_singular('post') || n9_seo_owned_elsewhere()) return $t;
	$id = get_queried_object_id();
	return n9_is_legacy_post($id) ? wp_strip_all_tags(get_the_title($id)) . ' | enCloud9' : $t;
}, 20);

add_action('wp_head', function () {
	if (!is_singular('post') || n9_seo_owned_elsewhere()) return;
	$id = get_queried_object_id();
	if (!n9_is_legacy_post($id)) return;
	$d = n9_legacy_desc($id);
	if ($d) {
		echo '<meta name="description" content="' . esc_attr($d) . '">' . "\n";
		echo '<meta property="og:description" content="' . esc_attr($d) . '">' . "\n";
	}
	$author = (string) get_post_meta($id, '_n9_byline', true);
	$ld = [
		'@context' => 'https://schema.org',
		'@type' => 'BlogPosting',
		'headline' => wp_strip_all_tags(get_the_title($id)),
		'datePublished' => get_the_date('c', $id),
		'dateModified' => get_the_modified_date('c', $id),
		'mainEntityOfPage' => get_permalink($id),
		'publisher' => ['@type' => 'Organization', '@id' => home_url('/#organization'), 'name' => 'enCloud9'],
	];
	if ($d) $ld['description'] = $d;
	if ($author !== '') $ld['author'] = ['@type' => 'Person', 'name' => $author];
	else $ld['author'] = ['@type' => 'Organization', 'name' => 'enCloud9'];
	$img = get_the_post_thumbnail_url($id, 'large');
	if ($img) $ld['image'] = $img;
	echo '<script type="application/ld+json">' . wp_json_encode($ld, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . "</script>\n";
}, 6);
