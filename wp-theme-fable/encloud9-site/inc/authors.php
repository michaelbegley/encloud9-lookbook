<?php
/**
 * Keep the admin login name private until real author pages exist.
 * - Author archives (/blog/author/<login>/ and ?author=N) 301 to the team page.
 * - No users sitemap.
 * - The REST users list is closed to visitors who are not signed in.
 */
if (!defined('ABSPATH')) exit;

add_filter('wp_sitemaps_add_provider', function ($provider, $name) {
	return $name === 'users' ? false : $provider;
}, 10, 2);

add_action('template_redirect', function () {
	if (is_author()) {
		wp_safe_redirect(home_url('/about-encloud9/team/'), 301);
		exit;
	}
});

add_filter('rest_endpoints', function ($endpoints) {
	if (is_user_logged_in()) return $endpoints;
	foreach (array_keys($endpoints) as $route) {
		if (strpos($route, '/wp/v2/users') === 0) unset($endpoints[$route]);
	}
	return $endpoints;
});
