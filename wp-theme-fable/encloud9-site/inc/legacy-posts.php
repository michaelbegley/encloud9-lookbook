<?php
/**
 * Tools > enCloud9 old posts: brings the blog posts kept from the old site (not on the mock site) across from the
 * live site's public REST API, ten at a time. Runs on the server, so nothing passes through anyone's computer.
 *
 * For each address in data/kept-posts.txt:
 *  - read the post from the old site (public /wp-json/wp/v2/posts, by slug; if the old address now redirects there,
 *    the redirect is followed to find the post),
 *  - strip the Divi layout code (section, row, column wrappers; the old title bar, sidebar and menu modules),
 *  - copy its images into this site's media library and point the post at the copies,
 *  - move its internal links to the approved new addresses,
 *  - save it with its original date, excerpt, categories, featured image and author name.
 * Running it again updates posts in place (matched on the old post's id). Site admins only.
 */
if (!defined('ABSPATH')) exit;

function n9_legacy_source() { return untrailingslashit(get_option('n9_legacy_source', 'https://www.encloud9.com')); }

function n9_legacy_list() {
	$f = N9_SITE_DIR . '/data/kept-posts.txt';
	if (!is_readable($f)) return [];
	$out = [];
	foreach (file($f, FILE_IGNORE_NEW_LINES) as $l) {
		$l = trim($l);
		if ($l === '' || $l[0] === '#') continue;
		$p = preg_split('/\s+/', $l);
		$out[] = ['new' => $p[0], 'old' => $p[1] ?? $p[0]];
	}
	return $out;
}

/* Old address => new address for every moved page (data/address-moves.json, ADDRESS-SCHEME-Draft1). */
function n9_legacy_moves() {
	static $m = null;
	if ($m !== null) return $m;
	$f = N9_SITE_DIR . '/data/address-moves.json';
	$m = is_readable($f) ? (array) json_decode(file_get_contents($f), true) : [];
	return $m;
}

function n9_legacy_get($url) {
	$r = wp_remote_get($url, ['timeout' => 25, 'redirection' => 5, 'headers' => ['Accept' => 'application/json']]);
	if (is_wp_error($r) || wp_remote_retrieve_response_code($r) !== 200) return null;
	return json_decode(wp_remote_retrieve_body($r), true);
}

/* Find the old post: by slug, else follow the old address's redirect to the slug it lands on. */
function n9_legacy_find($old_path) {
	$src = n9_legacy_source();
	$slug = basename(untrailingslashit($old_path));
	$embed = '&_embed=author,wp:featuredmedia,wp:term';
	$j = n9_legacy_get($src . '/wp-json/wp/v2/posts?slug=' . rawurlencode($slug) . $embed);
	if (!empty($j[0])) return [$j[0], ''];
	$r = wp_remote_head($src . $old_path, ['timeout' => 15, 'redirection' => 0]);
	$loc = is_wp_error($r) ? '' : (string) wp_remote_retrieve_header($r, 'location');
	if ($loc) {
		$s2 = basename(untrailingslashit((string) parse_url($loc, PHP_URL_PATH)));
		if ($s2 && $s2 !== $slug) {
			$j = n9_legacy_get($src . '/wp-json/wp/v2/posts?slug=' . rawurlencode($s2) . $embed);
			if (!empty($j[0])) return [$j[0], $s2];
		}
	}
	return [null, ''];
}

/* Divi: drop the old title bar, sidebar, menu and post nav modules; keep what is inside the rest; keep a call to action as a paragraph and link. */
function n9_legacy_clean($html) {
	$html = preg_replace('#\[(et_pb_fullwidth_post_title|et_pb_sidebar|et_pb_fullwidth_menu|et_pb_menu|et_pb_post_nav|et_pb_comments)\b[^\]]*\](.*?\[/\1\])?#s', '', $html);
	$html = preg_replace_callback('#\[et_pb_cta\b([^\]]*)\](.*?)\[/et_pb_cta\]#s', function ($m) {
		$a = shortcode_parse_atts($m[1]);
		$out = '';
		if (!empty($a['title'])) $out .= '<h3>' . esc_html($a['title']) . '</h3>';
		$out .= $m[2];
		if (!empty($a['button_url']) && !empty($a['button_text'])) $out .= '<p><a href="' . esc_url($a['button_url']) . '">' . esc_html($a['button_text']) . '</a></p>';
		return $out;
	}, $html);
	$html = preg_replace('#\[/?et_pb_[a-z_]+\b[^\]]*\]#', '', $html);
	$html = preg_replace('#\[/?insert\b[^\]]*\]#', '', $html);
	// Layout wrappers and inline styles from the old builder; the theme styles the reading column.
	$html = preg_replace('#\s(style|class|data-[a-z-]+|srcset|sizes)="[^"]*"#i', '', $html);
	$html = preg_replace('#<p>(\s|&nbsp;|<br\s*/?>)*</p>#i', '', $html);
	$html = preg_replace('#<div>\s*</div>#i', '', $html);
	return trim($html);
}

function n9_legacy_link($url) {
	$src = n9_legacy_source();
	$host = parse_url($src, PHP_URL_HOST);
	$h = parse_url($url, PHP_URL_HOST);
	if ($h && preg_replace('/^www\./', '', $h) !== preg_replace('/^www\./', '', $host)) return $url;
	$path = (string) parse_url($url, PHP_URL_PATH);
	if (strpos($path, '/wp-content/') === 0) return $url;
	$frag = parse_url($url, PHP_URL_FRAGMENT);
	$path = trailingslashit($path ?: '/');
	$moves = n9_legacy_moves();
	if (isset($moves[$path])) $path = $moves[$path];
	return $path . ($frag ? '#' . $frag : '');
}

function n9_legacy_image($url, $post_id, &$log, $alt = '') {
	static $done = [];
	if (isset($done[$url])) return $done[$url];
	require_once ABSPATH . 'wp-admin/includes/media.php';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/image.php';
	$clean = preg_replace('#-\d+x\d+(\.[a-z]+)$#i', '$1', strtok($url, '?'));
	$have = get_posts(['post_type' => 'attachment', 'meta_key' => '_n9_legacy_src', 'meta_value' => $clean, 'numberposts' => 1, 'fields' => 'ids']);
	if ($have) return $done[$url] = (int) $have[0];
	$id = media_sideload_image($clean, $post_id, $alt ?: null, 'id');
	if (is_wp_error($id)) {
		$id = media_sideload_image(strtok($url, '?'), $post_id, $alt ?: null, 'id');
	}
	if (is_wp_error($id)) { $log[] = 'image not copied: ' . $url . ' (' . $id->get_error_message() . ')'; return $done[$url] = 0; }
	update_post_meta($id, '_n9_legacy_src', $clean);
	if ($alt) update_post_meta($id, '_wp_attachment_image_alt', $alt);
	return $done[$url] = (int) $id;
}

function n9_legacy_import_one($item, &$log) {
	list($p, $resolved) = n9_legacy_find($item['old']);
	if (!$p) { $log[] = 'NOT FOUND on the old site: ' . $item['old']; return 'missing'; }
	$new_path = $item['new'];
	if ($resolved) {
		$new_path = '/blog/' . $resolved . '/';
		$log[] = $item['old'] . ' now redirects to ' . $new_path . ' on the old site; imported at ' . $new_path . ' (redirect map: add ' . $item['new'] . ' -> ' . $new_path . ')';
	}
	$slug = basename(untrailingslashit($new_path));
	if (n9_find_by_path($new_path) && !get_posts(['post_type' => 'post', 'meta_key' => '_n9_legacy_id', 'meta_value' => $p['id'], 'post_status' => 'any', 'numberposts' => 1, 'fields' => 'ids'])) {
		$log[] = 'skipped, already on the new site from the mock: ' . $new_path;
		return 'skipped';
	}
	$existing = get_posts(['post_type' => 'post', 'meta_key' => '_n9_legacy_id', 'meta_value' => $p['id'], 'post_status' => 'any', 'numberposts' => 1, 'fields' => 'ids']);

	$html = n9_legacy_clean($p['content']['rendered'] ?? '');
	$postarr = [
		'post_type' => 'post', 'post_status' => 'publish', 'post_name' => $slug,
		'post_title' => wp_strip_all_tags(html_entity_decode($p['title']['rendered'] ?? '', ENT_QUOTES)),
		'post_excerpt' => wp_strip_all_tags(html_entity_decode($p['excerpt']['rendered'] ?? '', ENT_QUOTES)),
		'post_date' => str_replace('T', ' ', $p['date']), 'post_modified' => str_replace('T', ' ', $p['modified']),
		'post_content' => '', 'post_author' => get_current_user_id(),
	];
	if ($existing) $postarr['ID'] = $existing[0];
	$id = wp_insert_post(wp_slash($postarr), true);
	if (is_wp_error($id)) { $log[] = 'save failed: ' . $new_path . ' ' . $id->get_error_message(); return 'failed'; }

	// Images into the media library; links to the new addresses.
	$src_host = preg_replace('/^www\./', '', parse_url(n9_legacy_source(), PHP_URL_HOST));
	$html = preg_replace_callback('#<img\b[^>]*>#i', function ($m) use ($id, &$log, $src_host) {
		if (!preg_match('#\ssrc="([^"]+)"#i', $m[0], $s)) return '';
		$alt = preg_match('#\salt="([^"]*)"#i', $m[0], $a) ? html_entity_decode($a[1]) : '';
		$h = preg_replace('/^www\./', '', (string) parse_url($s[1], PHP_URL_HOST));
		if ($h !== $src_host) return '<img src="' . esc_url($s[1]) . '" alt="' . esc_attr($alt) . '">';
		$aid = n9_legacy_image($s[1], $id, $log, $alt);
		if (!$aid) return '<img src="' . esc_url($s[1]) . '" alt="' . esc_attr($alt) . '">';
		$u = wp_make_link_relative(wp_get_attachment_image_url($aid, 'large') ?: wp_get_attachment_url($aid));
		return '<img src="' . esc_url($u) . '" alt="' . esc_attr($alt) . '" class="wp-image-' . $aid . '" loading="lazy">';
	}, $html);
	$html = preg_replace_callback('#\shref="([^"]+)"#i', function ($m) { return ' href="' . esc_url(n9_legacy_link(html_entity_decode($m[1]))) . '"'; }, $html);
	// Plain paragraphs and headings stay plain HTML: the theme frames the post (title, author, date, contents list, closing call to action).
	wp_update_post(['ID' => $id, 'post_content' => wp_slash($html)]);

	// Featured image, categories, author name.
	$fm = $p['_embedded']['wp:featuredmedia'][0] ?? null;
	if ($fm && !empty($fm['source_url'])) {
		$aid = n9_legacy_image($fm['source_url'], $id, $log, $fm['alt_text'] ?? '');
		if ($aid) set_post_thumbnail($id, $aid);
	}
	$cats = [];
	foreach (($p['_embedded']['wp:term'][0] ?? []) as $t) {
		if (($t['taxonomy'] ?? '') !== 'category' || ($t['slug'] ?? '') === 'uncategorized') continue;
		$term = term_exists($t['slug'], 'category') ?: wp_insert_term(html_entity_decode($t['name']), 'category', ['slug' => $t['slug']]);
		if (!is_wp_error($term)) $cats[] = (int) (is_array($term) ? $term['term_id'] : $term);
	}
	if ($cats) wp_set_post_categories($id, $cats);
	$author = $p['_embedded']['author'][0]['name'] ?? '';
	if ($author === '' && !empty($p['link'])) {
		// The old site hides its users list; the post page itself names the author.
		$r = wp_remote_get($p['link'], ['timeout' => 20]);
		if (!is_wp_error($r) && preg_match('#<meta name="author" content="([^"]+)"#', wp_remote_retrieve_body($r), $am)) $author = html_entity_decode($am[1], ENT_QUOTES);
	}
	if ($author) update_post_meta($id, '_n9_byline', sanitize_text_field($author));
	update_post_meta($id, '_n9_legacy_id', (int) $p['id']);
	update_post_meta($id, '_n9_legacy_url', esc_url_raw($p['link'] ?? ''));
	update_post_meta($id, '_n9_path', $new_path);
	if (preg_match('/et_pb_/', $p['content']['rendered'] ?? '')) update_post_meta($id, '_n9_legacy_divi', 1);
	$log[] = ($existing ? 'updated ' : 'created ') . $new_path . ($author ? " (by $author)" : '');
	return $existing ? 'updated' : 'created';
}

add_action('admin_menu', function () {
	add_management_page('enCloud9 old posts', 'enCloud9 old posts', 'manage_options', 'n9-legacy', 'n9_legacy_screen');
});

function n9_legacy_screen() {
	if (!current_user_can('manage_options')) wp_die('Not allowed');
	$list = n9_legacy_list();
	$next = (int) get_option('n9_legacy_next', 0);
	echo '<div class="wrap"><h1>enCloud9 old posts</h1>';
	if (isset($_POST['n9_legacy_run']) && check_admin_referer('n9_legacy')) {
		if (!empty($_POST['n9_legacy_restart'])) $next = 0;
		@set_time_limit(900);
		$log = []; $tally = [];
		$batch = array_slice($list, $next, 10);
		foreach ($batch as $item) { $r = n9_legacy_import_one($item, $log); $tally[$r] = ($tally[$r] ?? 0) + 1; }
		$next += count($batch);
		update_option('n9_legacy_next', $next, false);
		$all = (array) get_option('n9_legacy_log', []);
		update_option('n9_legacy_log', array_slice(array_merge($all, ['--- ' . wp_date('Y-m-d H:i T')], $log), -600), false);
		$t = [];
		foreach ($tally as $k => $v) $t[] = "$v $k";
		echo '<div class="notice notice-success"><p>This batch: ' . esc_html(implode(', ', $t) ?: 'nothing to do') . '.</p></div>';
		echo '<pre style="white-space:pre-wrap">' . esc_html(implode("\n", $log)) . '</pre>';
	}
	printf('<p>%d of %d posts done. Source: %s</p>', min($next, count($list)), count($list), esc_html(n9_legacy_source()));
	echo '<form method="post">';
	wp_nonce_field('n9_legacy');
	echo '<p><label><input type="checkbox" name="n9_legacy_restart" value="1"> Start again from the first post (updates in place)</label></p>';
	submit_button($next >= count($list) ? 'Run again' : 'Import the next 10', 'primary', 'n9_legacy_run');
	echo '</form>';
	$all = (array) get_option('n9_legacy_log', []);
	if ($all) echo '<h2>Log</h2><pre style="white-space:pre-wrap;max-height:400px;overflow:auto">' . esc_html(implode("\n", array_slice($all, -200))) . '</pre>';
	echo '</div>';
}
