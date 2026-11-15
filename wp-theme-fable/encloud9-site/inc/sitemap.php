<?php
/**
 * Sitemap: keep confirmation pages, noindex pages and /lp/ campaign pages out (10 Nov rule).
 * Fix 2 of NEW-SITE-PAGE-CHECK-14-NOV.
 */
if (!defined('ABSPATH')) exit;

function n9_sitemap_excluded_ids() {
	static $ids = null;
	if ($ids !== null) return $ids;
	$ids = get_posts(['post_type' => 'any', 'post_status' => 'publish', 'numberposts' => -1, 'fields' => 'ids',
		'meta_key' => '_n9_noindex', 'meta_value' => '1']);
	$lp = get_page_by_path('lp');
	if ($lp) {
		$ids[] = $lp->ID;
		$ids = array_merge($ids, wp_list_pluck(get_pages(['child_of' => $lp->ID, 'post_status' => 'publish']), 'ID'));
	}
	$ids = array_values(array_unique(array_map('intval', $ids)));
	return $ids;
}

add_filter('wp_sitemaps_posts_query_args', function ($args) {
	$ex = n9_sitemap_excluded_ids();
	if ($ex) $args['post__not_in'] = array_merge($args['post__not_in'] ?? [], $ex);
	return $args;
});
