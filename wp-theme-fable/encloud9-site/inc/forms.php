<?php
/**
 * Website forms into Dynamics through ClickDimensions.
 *
 * Every form on the site posts to /wp-json/n9/v1/form. The plugin checks the entry, saves it as a private
 * "Form entry" record first, then posts it to that form's ClickDimensions Form Capture from the server
 * (Click's "Programmatic Form Capture": the Click field IDs, cd_visitorkey from the visitor's cuvid cookie,
 * and a Referer on our domain). A failed post is kept, retried hourly and emailed to the alert address.
 *
 * Capture addresses and the Click tracking script are settings (Settings > enCloud9 forms), never code:
 * they are pasted by a site admin, so no capture address or account key is ever in the repo.
 */
if (!defined('ABSPATH')) exit;

/* ------------------------------------------------------------------ what each form is
 * capture: which setting holds its Form Capture address.
 * fields:  what the visitor fills in (name => required).
 * click:   Click Form Field IDs this capture has (read from Dynamics 15 Nov 2026), so nothing unknown is sent.
 * thanks:  where the visitor goes after a good send.
 */
function n9_form_kinds() {
	// Only fields the capture has today. Company, UTM and lead source can join once Form Capture Fields are added in Dynamics
	// (FORMS-RESEARCH doc); until then company and source travel inside the message.
	// company, utm_source, utm_medium, utm_campaign and gclid added to the Home Page capture 15 Nov 2026 (Michael's go).
	$contact_click = ['Topic', 'first-name', 'last-name', 'your-email', 'phone', 'company', 'your-message', 'Form Name', 'Page Name', 'current-url', 'Referral URL',
		'utm_source', 'utm_medium', 'utm_campaign', 'gclid'];
	$guide_click = ['first-name', 'last-name', 'your-email', 'ipaddress', 'Page Name', 'current-url', 'Referral URL',
		'utm_source', 'utm medium', 'utm_campaign', 'utm_term', 'utm_content'];
	return apply_filters('n9_form_kinds', [
		'contact'  => ['label' => 'Contact us', 'capture' => 'contact', 'thanks' => '/thank-you-contact/',
			'fields' => ['name' => 1, 'company' => 1, 'email' => 1, 'msg' => 1, 'ok' => 1], 'click' => $contact_click],
		'consult'  => ['label' => 'Free consultation', 'capture' => 'contact', 'thanks' => '/request-received/',
			'fields' => ['name' => 1, 'company' => 1, 'email' => 1, 'msg' => 1, 'consent' => 1], 'click' => $contact_click],
		'check'    => ['label' => 'Free check', 'capture' => 'contact', 'thanks' => '/request-received/',
			'fields' => ['asset' => 0, 'name' => 1, 'company' => 1, 'email' => 1], 'click' => $contact_click],
		'guide'    => ['label' => 'Guide download', 'capture' => 'guide', 'thanks' => '/thank-you/',
			'fields' => ['first' => 1, 'last' => 0, 'email' => 1, 'consent' => 1], 'click' => $guide_click],
		'storage'  => ['label' => 'Dataverse storage analysis', 'capture' => 'storage', 'thanks' => '/request-received/',
			'fields' => ['first' => 1, 'last' => 1, 'email' => 1, 'company' => 1, 'phone' => 0, 'seeing' => 0],
			'click' => ['first-name', 'last-name', 'your-email', 'company', 'phone', 'your-message']],
		'callprep' => ['label' => 'Call preparation', 'capture' => 'callprep', 'thanks' => '/call-prep-received/',
			'fields' => ['name' => 1, 'email' => 1, 'using' => 0, 'why' => 0, 'users' => 0, 'win' => 1, 'cover' => 0, 'heard' => 0],
			'click' => ['first-name', 'last-name', 'your-email', 'utm_source', 'utm_medium', 'utm_campaign', 'gclid', 'current-crm',
				'call-reason', 'team-size', 'success-definition', 'call-topics', 'heard-about-us']],
		'newsletter' => ['label' => 'Newsletter', 'capture' => 'newsletter', 'thanks' => '/newsletter-signup-successful/',
			'fields' => ['name' => 1, 'email' => 1, 'consent' => 1],
			'click' => ['last-name', 'your-email', 'Topic', 'current-url', 'Referral URL', 'Form Name']],
	]);
}

function n9_form_captures() {
	return [
		'contact'    => 'Home Page Contact Us Form (contact, consultation, free checks)',
		'guide'      => '24 - Download our Free Guide',
		'storage'    => '28 - Dataverse storage analysis',
		'callprep'   => '27 - Call Preparation',
		'newsletter' => '26 - Newsletter pop up form',
	];
}

function n9_forms_opt($k = null) {
	$o = get_option('n9_forms', []);
	if (!is_array($o)) $o = [];
	return $k === null ? $o : ($o[$k] ?? '');
}

/* ------------------------------------------------------------------ entries */
add_action('init', function () {
	register_post_type('n9_entry', [
		'label' => 'Form entries',
		'labels' => ['singular_name' => 'Form entry'],
		'public' => false, 'show_ui' => true, 'show_in_menu' => true, 'show_in_rest' => false,
		'menu_icon' => 'dashicons-email-alt', 'menu_position' => 26,
		'supports' => ['title'],
		'capability_type' => 'post',
		'capabilities' => ['create_posts' => 'do_not_allow'],
		'map_meta_cap' => true,
	]);
});

add_filter('manage_n9_entry_posts_columns', function ($c) {
	return ['cb' => $c['cb'], 'title' => 'Entry', 'n9_form' => 'Form', 'n9_status' => 'Sent to Dynamics', 'n9_source' => 'Source', 'date' => 'Received'];
});
add_action('manage_n9_entry_posts_custom_column', function ($col, $id) {
	if ($col === 'n9_form') echo esc_html(get_post_meta($id, '_n9_kind', true));
	if ($col === 'n9_status') echo esc_html(get_post_meta($id, '_n9_status', true));
	if ($col === 'n9_source') echo esc_html(get_post_meta($id, '_n9_channel', true));
}, 10, 2);

add_action('add_meta_boxes_n9_entry', function () {
	add_meta_box('n9_entry_data', 'What was sent', function ($post) {
		$data = json_decode(get_post_meta($post->ID, '_n9_data', true), true) ?: [];
		$touch = json_decode(get_post_meta($post->ID, '_n9_touch', true), true) ?: [];
		$log = json_decode(get_post_meta($post->ID, '_n9_log', true), true) ?: [];
		echo '<table class="widefat striped"><tbody>';
		foreach ($data as $k => $v) echo '<tr><th>' . esc_html($k) . '</th><td>' . nl2br(esc_html(is_array($v) ? implode(', ', $v) : $v)) . '</td></tr>';
		foreach ($touch as $k => $v) echo '<tr><th>' . esc_html($k) . '</th><td>' . esc_html($v) . '</td></tr>';
		echo '</tbody></table><h4>Sends</h4><ul>';
		foreach ($log as $l) echo '<li>' . esc_html($l) . '</li>';
		echo '</ul>';
	}, 'n9_entry', 'normal');
});

/* ------------------------------------------------------------------ where a visitor came from */
function n9_channel($t) {
	$src = strtolower($t['utm_source'] ?? '');
	$med = strtolower($t['utm_medium'] ?? '');
	$ref = strtolower((string) parse_url($t['referrer'] ?? '', PHP_URL_HOST));
	$ref = preg_replace('/^www\./', '', $ref);
	$ai = ['chatgpt.com', 'chat.openai.com', 'perplexity.ai', 'copilot.microsoft.com', 'gemini.google.com', 'claude.ai', 'you.com', 'phind.com'];
	$hay = $src . ' ' . $ref;
	foreach ($ai as $h) if (strpos($hay, $h) !== false) return 'AI assistant';
	if (in_array($src, ['chatgpt', 'chatgpt.com', 'openai', 'perplexity', 'perplexity.ai', 'copilot', 'gemini', 'claude', 'claude.ai'], true)) return 'AI assistant';
	if (!empty($t['gclid']) || in_array($med, ['cpc', 'ppc', 'paid'], true)) return 'Paid search';
	if (strpos($hay, 'linkedin') !== false || $ref === 'lnkd.in') return 'LinkedIn';
	if (strpos($hay, 'crmsoftwareblog') !== false) return 'CRM Software Blog';
	if (strpos($hay, 'youtube') !== false || $ref === 'youtu.be') return 'YouTube';
	if (in_array($src, ['gbp', 'google-business-profile', 'googlemybusiness'], true)) return 'Google Business Profile';
	if ($med === 'email' || strpos($hay, 'clickdimensions') !== false) return 'Email';
	if (preg_match('/(^|\.)google\./', $ref) || $src === 'google') return 'Google search';
	if (preg_match('/(^|\.)bing\.com$/', $ref) || $src === 'bing') return 'Bing search';
	if (preg_match('/duckduckgo|yahoo|ecosia/', $ref)) return 'Other search';
	if ($ref !== '' && strpos($ref, 'encloud9') === false) return 'Referral: ' . $ref;
	if ($src !== '') return 'Campaign: ' . $src;
	return 'Direct';
}

/* ------------------------------------------------------------------ the endpoint */
add_action('rest_api_init', function () {
	register_rest_route('n9/v1', '/form', ['methods' => 'POST', 'permission_callback' => '__return_true', 'callback' => 'n9_form_receive']);
});

function n9_form_receive(WP_REST_Request $r) {
	$kinds = n9_form_kinds();
	$kind = sanitize_key($r->get_param('kind'));
	if (!isset($kinds[$kind])) return new WP_REST_Response(['ok' => false, 'error' => 'form'], 400);
	$def = $kinds[$kind];

	// Bots: a field people never see, and a form sent faster than a person can.
	if (trim((string) $r->get_param('n9_hp')) !== '') return new WP_REST_Response(['ok' => true, 'thanks' => $def['thanks']], 200);
	$age = (int) $r->get_param('n9_age');
	if ($age < 2500) return new WP_REST_Response(['ok' => true, 'thanks' => $def['thanks']], 200);

	// Per-address limit: 20 sends in 10 minutes (an office shares one address).
	$ip = n9_client_ip();
	$rk = 'n9_rl_' . md5($ip);
	$n = (int) get_transient($rk);
	if ($n >= 20) return new WP_REST_Response(['ok' => false, 'error' => 'busy'], 429);
	set_transient($rk, $n + 1, 10 * MINUTE_IN_SECONDS);

	$f = (array) $r->get_param('fields');
	$data = [];
	$missing = [];
	foreach ($def['fields'] as $name => $req) {
		$v = $f[$name] ?? '';
		$v = is_array($v) ? implode(', ', array_map('sanitize_text_field', $v)) : (in_array($name, ['msg', 'win', 'cover'], true) ? sanitize_textarea_field($v) : sanitize_text_field($v));
		$v = mb_substr($v, 0, in_array($name, ['msg', 'win', 'cover'], true) ? 3500 : 250);
		if ($req && $v === '') $missing[] = $name;
		$data[$name] = $v;
	}
	if (!empty($data['email']) && !is_email($data['email'])) $missing[] = 'email';
	if ($missing) return new WP_REST_Response(['ok' => false, 'error' => 'missing', 'fields' => array_values(array_unique($missing))], 422);

	$t = (array) $r->get_param('touch');
	$touch = [];
	foreach (['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'referrer', 'landing', 'first_seen',
	          'first_utm_source', 'first_utm_medium', 'first_utm_campaign', 'first_referrer', 'first_landing'] as $k) {
		if (isset($t[$k]) && is_scalar($t[$k]) && trim($t[$k]) !== '') $touch[$k] = mb_substr(sanitize_text_field($t[$k]), 0, 250);
	}
	$page = esc_url_raw((string) $r->get_param('page'));
	$title = sanitize_text_field((string) $r->get_param('title'));
	$first = [
		'utm_source' => $touch['first_utm_source'] ?? '', 'utm_medium' => $touch['first_utm_medium'] ?? '',
		'referrer' => $touch['first_referrer'] ?? '', 'gclid' => $touch['gclid'] ?? '',
	];
	$last = ['utm_source' => $touch['utm_source'] ?? '', 'utm_medium' => $touch['utm_medium'] ?? '',
		'referrer' => $touch['referrer'] ?? '', 'gclid' => $touch['gclid'] ?? ''];
	$channel = n9_channel(array_filter($first) ? $first : $last);
	$channel_last = n9_channel($last);

	$id = wp_insert_post([
		'post_type' => 'n9_entry', 'post_status' => 'private',
		'post_title' => $def['label'] . ': ' . ($data['email'] ?? ''),
	], true);
	if (is_wp_error($id)) return new WP_REST_Response(['ok' => false, 'error' => 'save'], 500);
	update_post_meta($id, '_n9_kind', $kind);
	update_post_meta($id, '_n9_data', wp_json_encode($data));
	update_post_meta($id, '_n9_touch', wp_json_encode($touch + ['channel (first touch)' => $channel, 'channel (this visit)' => $channel_last]));
	update_post_meta($id, '_n9_channel', $channel);
	update_post_meta($id, '_n9_page', $page);
	update_post_meta($id, '_n9_title', $title);
	update_post_meta($id, '_n9_ip', $ip);
	update_post_meta($id, '_n9_cuvid', n9_visitor_key());
	update_post_meta($id, '_n9_status', 'waiting');
	update_post_meta($id, '_n9_tries', 0);

	n9_form_send($id);
	n9_form_notify($id);

	return new WP_REST_Response(['ok' => true, 'thanks' => $def['thanks']], 200);
}

function n9_client_ip() {
	$ip = $_SERVER['REMOTE_ADDR'] ?? '';
	// Flywheel sits behind its own proxy; it passes the visitor's address here.
	foreach (['HTTP_X_REAL_IP', 'HTTP_X_FORWARDED_FOR'] as $h) {
		if (!empty($_SERVER[$h])) { $ip = trim(explode(',', $_SERVER[$h])[0]); break; }
	}
	return filter_var($ip, FILTER_VALIDATE_IP) ? $ip : '';
}

function n9_visitor_key() {
	$v = isset($_COOKIE['cuvid']) ? sanitize_text_field(wp_unslash($_COOKIE['cuvid'])) : '';
	// Click accepts v<number>_<UUID> or a bare UUID; anything else is left out rather than sent wrong.
	return preg_match('/^(v\d+_)?[0-9A-Fa-f]{32}$|^[0-9A-Fa-f-]{36}$/', $v) ? $v : '';
}

/* ------------------------------------------------------------------ what Click receives */
function n9_click_body($id) {
	$kind = get_post_meta($id, '_n9_kind', true);
	$def = n9_form_kinds()[$kind] ?? null;
	if (!$def) return [];
	$d = json_decode(get_post_meta($id, '_n9_data', true), true) ?: [];
	$t = json_decode(get_post_meta($id, '_n9_touch', true), true) ?: [];
	$name = trim($d['name'] ?? '');
	$first = $d['first'] ?? '';
	$last = $d['last'] ?? '';
	if ($name !== '') {
		$parts = preg_split('/\s+/', $name);
		$last = count($parts) > 1 ? array_pop($parts) : $name;
		$first = count($parts) >= 1 && $last !== $name ? implode(' ', $parts) : '';
	}
	$asset = $d['asset'] ?? '';
	$topic = $def['label'] . ($asset ? ': ' . ucwords(str_replace('-', ' ', $asset)) : '');
	$source = $t['channel (first touch)'] ?? '';

	$msg = $d['msg'] ?? '';
	if ($kind === 'storage') $msg = trim('What are you seeing: ' . ($d['seeing'] ?? ''));
	// Company and source also ride in the message so whoever opens the lead sees them at once.
	$note = "Company: " . ($d['company'] ?? '') . "\nForm: " . $topic . "\nSource: " . $source;
	if (in_array($kind, ['contact', 'consult', 'check'], true)) $msg = trim($msg . "\n\n" . $note);

	$all = [
		'first-name' => $first, 'last-name' => $kind === 'newsletter' ? ($name ?: $last) : $last,
		'your-email' => $d['email'] ?? '', 'company' => $d['company'] ?? '', 'phone' => $d['phone'] ?? '',
		'your-message' => $msg, 'Topic' => $topic, 'Form Name' => $def['label'],
		'Page Name' => get_post_meta($id, '_n9_title', true), 'current-url' => get_post_meta($id, '_n9_page', true),
		'Referral URL' => $t['first_referrer'] ?? ($t['referrer'] ?? ''), 'ipaddress' => get_post_meta($id, '_n9_ip', true),
		'utm_source' => $t['first_utm_source'] ?? ($t['utm_source'] ?? ''), 'utm_medium' => $t['first_utm_medium'] ?? ($t['utm_medium'] ?? ''),
		'utm medium' => $t['first_utm_medium'] ?? ($t['utm_medium'] ?? ''),
		'utm_campaign' => $t['first_utm_campaign'] ?? ($t['utm_campaign'] ?? ''), 'utm_term' => $t['utm_term'] ?? '',
		'utm_content' => $t['utm_content'] ?? '', 'gclid' => $t['gclid'] ?? '',
		'current-crm' => $d['using'] ?? '', 'call-reason' => $d['why'] ?? '', 'team-size' => $d['users'] ?? '',
		'success-definition' => $d['win'] ?? '', 'call-topics' => $d['cover'] ?? '', 'heard-about-us' => $d['heard'] ?? '',
	];
	// No utm on the visit: the source we worked out stands in, so Dynamics still shows where the lead came from.
	if ($all['utm_source'] === '' && $source !== '' && $source !== 'Direct') { $all['utm_source'] = $source; }
	$body = [];
	foreach ($def['click'] as $fid) if (isset($all[$fid]) && $all[$fid] !== '') $body[$fid] = $all[$fid];
	$lsf = trim(n9_forms_opt('lead_source_field'));
	if ($lsf !== '') $body[$lsf] = '8'; // Lead Source = Web (option value 8 in enCloud9's Dynamics, measured 15 Nov 2026)
	$cuvid = get_post_meta($id, '_n9_cuvid', true);
	if ($cuvid) $body['cd_visitorkey'] = $cuvid;
	return $body;
}

function n9_form_send($id) {
	$kind = get_post_meta($id, '_n9_kind', true);
	$def = n9_form_kinds()[$kind] ?? null;
	$url = $def ? trim(n9_forms_opt('capture_' . $def['capture'])) : '';
	$url = apply_filters('n9_forms_capture_url', $url, $def['capture'] ?? '');
	$test = apply_filters('n9_forms_test_mode', false);
	$tries = (int) get_post_meta($id, '_n9_tries', true) + 1;
	update_post_meta($id, '_n9_tries', $tries);
	$log = json_decode(get_post_meta($id, '_n9_log', true), true) ?: [];
	$stamp = wp_date('Y-m-d H:i:s T');

	if ($url === '' || (!$test && !preg_match('#^https://[a-z0-9.-]+\.clickdimensions\.com/#i', $url))) {
		update_post_meta($id, '_n9_status', 'kept, no capture set');
		$log[] = "$stamp try $tries: no Form Capture address set for '{$def['capture']}', entry kept here";
		update_post_meta($id, '_n9_log', wp_json_encode($log));
		return false;
	}
	$referer = get_post_meta($id, '_n9_page', true) ?: home_url('/');
	// ClickDimensions only knows enCloud9.com as our domain, so a post from the private
	// staging host is sent with the same page path on www.encloud9.com (what it will be after launch).
	$referer = preg_replace('#^https?://[^/]*flywheelsites\.com#i', 'https://www.encloud9.com', $referer);
	$res = wp_remote_post($url, [
		'timeout' => 15, 'redirection' => 0,
		'headers' => ['Referer' => $referer, 'Content-Type' => 'application/x-www-form-urlencoded'],
		'body' => n9_click_body($id),
	]);
	if (is_wp_error($res)) {
		$ok = false; $what = 'error: ' . $res->get_error_message();
	} else {
		$code = (int) wp_remote_retrieve_response_code($res);
		$loc = (string) wp_remote_retrieve_header($res, 'location');
		$err = trim(n9_forms_opt('error_marker'));
		$ok = $code >= 200 && $code < 400 && stripos($loc, 'error') === false && ($err === '' || stripos($loc, $err) === false);
		$what = "HTTP $code" . ($loc ? " to " . preg_replace('/\?.*/', '', $loc) : '');
	}
	$log[] = "$stamp try $tries: " . ($ok ? 'sent, ' : 'failed, ') . $what;
	update_post_meta($id, '_n9_log', wp_json_encode($log));
	update_post_meta($id, '_n9_status', $ok ? 'sent' : ($tries >= 6 ? 'failed, gave up' : 'failed, will retry'));
	if (!$ok && $tries === 1) n9_form_alert($id, $what);
	return $ok;
}

/* Retry every hour, up to 6 tries in all. */
add_action('init', function () {
	if (!wp_next_scheduled('n9_forms_retry')) wp_schedule_event(time() + 600, 'hourly', 'n9_forms_retry');
});
add_action('n9_forms_retry', function () {
	$q = get_posts(['post_type' => 'n9_entry', 'post_status' => 'private', 'numberposts' => 20, 'fields' => 'ids',
		'meta_query' => [['key' => '_n9_status', 'value' => ['failed, will retry', 'kept, no capture set'], 'compare' => 'IN']]]);
	foreach ($q as $id) n9_form_send($id);
});

function n9_form_alert($id, $what) {
	$to = n9_forms_opt('alert_email') ?: get_option('admin_email');
	wp_mail($to, 'Website form did not reach Dynamics', "A form entry was saved on the website but ClickDimensions did not accept it.\n\n"
		. "Form: " . get_post_meta($id, '_n9_kind', true) . "\nResult: $what\n\nIt will be retried every hour. See it here:\n"
		. admin_url('post.php?post=' . $id . '&action=edit'));
}

/* Optional copy of each entry to people (set on the settings screen; empty sends nothing). */
function n9_form_notify($id) {
	$to = trim(n9_forms_opt('notify_email'));
	if ($to === '') return;
	$d = json_decode(get_post_meta($id, '_n9_data', true), true) ?: [];
	$lines = [];
	foreach ($d as $k => $v) if ($v !== '') $lines[] = "$k: $v";
	$lines[] = 'Source: ' . get_post_meta($id, '_n9_channel', true);
	$lines[] = 'Page: ' . get_post_meta($id, '_n9_page', true);
	wp_mail($to, 'New website form: ' . (n9_form_kinds()[get_post_meta($id, '_n9_kind', true)]['label'] ?? ''), implode("\n", $lines));
}

/* ------------------------------------------------------------------ front end */
add_action('wp_enqueue_scripts', function () {
	wp_enqueue_script('n9-forms', plugins_url('assets/forms.js', N9_SITE_DIR . '/encloud9-site.php'), [], N9_SITE_VER . '-f2', true);
	wp_add_inline_script('n9-forms', 'window.n9Forms=' . wp_json_encode(['endpoint' => esc_url_raw(rest_url('n9/v1/form'))]) . ';', 'before');
});

/* The ClickDimensions tracking script, pasted on the settings screen; it sets the cuvid cookie that ties a lead to its visits. */
add_action('wp_footer', function () {
	$s = n9_forms_opt('click_script');
	if ($s !== '' && !is_user_logged_in()) echo "\n" . $s . "\n";
}, 99);

/* ------------------------------------------------------------------ settings */
add_action('admin_menu', function () {
	add_options_page('enCloud9 forms', 'enCloud9 forms', 'manage_options', 'n9-forms', 'n9_forms_page');
});

add_action('admin_init', function () {
	register_setting('n9_forms', 'n9_forms', ['sanitize_callback' => function ($in) {
		$out = [];
		foreach (array_keys(n9_form_captures()) as $k) {
			$u = trim($in['capture_' . $k] ?? '');
			$u = preg_replace('#^http://#i', 'https://', $u);
			if ($u !== '' && !preg_match('#^https://[a-z0-9.-]+\.clickdimensions\.com/#i', $u)) {
				add_settings_error('n9_forms', 'n9_bad_' . $k, 'Not saved: ' . n9_form_captures()[$k] . ' needs a clickdimensions.com address.');
				$u = '';
			}
			$out['capture_' . $k] = $u === '' ? '' : esc_url_raw($u);
		}
		$out['click_script'] = current_user_can('unfiltered_html') ? trim($in['click_script'] ?? '') : '';
		$out['alert_email'] = implode(',', array_filter(array_map('sanitize_email', explode(',', $in['alert_email'] ?? ''))));
		$out['notify_email'] = implode(',', array_filter(array_map('sanitize_email', explode(',', $in['notify_email'] ?? ''))));
		$out['lead_source_field'] = sanitize_text_field($in['lead_source_field'] ?? '');
		$out['error_marker'] = sanitize_text_field($in['error_marker'] ?? '');
		$b = trim($in['bookings_url'] ?? '');
		if ($b !== '' && !preg_match('#^https://outlook\.(office|office365)\.com/(owa/calendar|book)/#i', $b)) {
			add_settings_error('n9_forms', 'n9_bad_bookings', 'Not saved: the Bookings link needs to start with https://outlook.office.com/book/');
			$b = '';
		}
		$out['bookings_url'] = $b === '' ? '' : esc_url_raw($b);
		return $out;
	}]);
});

function n9_forms_page() {
	$o = n9_forms_opt();
	echo '<div class="wrap"><h1>enCloud9 forms</h1><form method="post" action="options.php">';
	settings_fields('n9_forms');
	echo '<h2>Form Capture addresses</h2><p>From each Form Capture in Dynamics (ClickDimensions Settings). Leave one empty and that form\'s entries are kept here until it is set.</p><table class="form-table">';
	foreach (n9_form_captures() as $k => $label) {
		printf('<tr><th>%s</th><td><input type="url" class="large-text" name="n9_forms[capture_%s]" value="%s" autocomplete="off"></td></tr>',
			esc_html($label), esc_attr($k), esc_attr($o['capture_' . $k] ?? ''));
	}
	echo '</table><h2>Tracking script</h2><p>The ClickDimensions tracking script, as it is on the live site. It goes in every page footer for visitors.</p>';
	printf('<textarea name="n9_forms[click_script]" rows="8" class="large-text code">%s</textarea>', esc_textarea($o['click_script'] ?? ''));
	echo '<h2>Booking calendar</h2><p>The public link of the Microsoft Bookings page (from Bookings > Booking page > Copy link). Empty: the Book a call page shows the phone and contact options instead.</p><table class="form-table">';
	printf('<tr><th>Bookings page link</th><td><input type="url" class="large-text" name="n9_forms[bookings_url]" value="%s" placeholder="https://outlook.office.com/book/..."></td></tr>',
		esc_attr($o['bookings_url'] ?? ''));
	echo '</table><h2>Email</h2><table class="form-table">';
	printf('<tr><th>Alert when a send fails</th><td><input type="text" class="large-text" name="n9_forms[alert_email]" value="%s" placeholder="%s"><p class="description">Comma separated. Empty sends to the site admin email.</p></td></tr>',
		esc_attr($o['alert_email'] ?? ''), esc_attr(get_option('admin_email')));
	printf('<tr><th>Copy of every entry to</th><td><input type="text" class="large-text" name="n9_forms[notify_email]" value="%s"><p class="description">Comma separated. Empty sends no copies.</p></td></tr>',
		esc_attr($o['notify_email'] ?? ''));
	echo '</table><h2>Advanced</h2><table class="form-table">';
	printf('<tr><th>Lead source field ID</th><td><input type="text" class="regular-text" name="n9_forms[lead_source_field]" value="%s"><p class="description">The Click Form Field ID mapped to Lead Source. Empty until it exists in Dynamics.</p></td></tr>',
		esc_attr($o['lead_source_field'] ?? ''));
	printf('<tr><th>Error page marker</th><td><input type="text" class="regular-text" name="n9_forms[error_marker]" value="%s"><p class="description">Part of the Form Capture\'s error page address, so a refused send is caught.</p></td></tr>',
		esc_attr($o['error_marker'] ?? ''));
	echo '</table>';
	submit_button();
	echo '</form></div>';
}


/* The Book a call page's calendar box: the Bookings page once its link is set, otherwise the fallback text in the page. */
add_filter('render_block', function ($content) {
	if (is_admin() || strpos($content, 'data-n9-bookings') === false) return $content;
	$u = trim((string) n9_forms_opt('bookings_url'));
	if ($u === '') return $content;
	$frame = '<div class="embed" data-n9-bookings="1"><iframe src="' . esc_url($u) . '" title="Book a call with enCloud9" loading="lazy" style="width:100%;min-height:720px;border:0"></iframe></div>';
	return preg_replace('#<div class="embed" data-n9-bookings="1">.*?</div>#s', $frame, $content, 1);
}, 25);
