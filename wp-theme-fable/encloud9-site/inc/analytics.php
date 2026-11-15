<?php
/**
 * Analytics: GA4 and Microsoft Clarity.
 * Output only on the live encloud9.com host, so the private Flywheel test site
 * never sends test visits. Skipped for signed-in users (staff editing pages).
 */
if (!defined('ABSPATH')) exit;

const N9_GA4_ID     = 'G-J6NX9ZYD8C'; // GA4 property 399425106 (SYSTEMS.md)
const N9_CLARITY_ID = '';             // Clarity project ID, filled in once Michael creates the project

function n9_analytics_on() {
	$host = isset($_SERVER['HTTP_HOST']) ? strtolower($_SERVER['HTTP_HOST']) : '';
	$live = in_array($host, array('encloud9.com', 'www.encloud9.com'), true);
	return apply_filters('n9_analytics_on', $live && !is_user_logged_in());
}

add_action('wp_head', function () {
	if (!n9_analytics_on()) return;
	$ga = esc_js(N9_GA4_ID);
	echo "<script async src=\"https://www.googletagmanager.com/gtag/js?id={$ga}\"></script>\n";
	echo "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','{$ga}');</script>\n";
	if (N9_CLARITY_ID !== '') {
		$cl = esc_js(N9_CLARITY_ID);
		echo "<script>(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src=\"https://www.clarity.ms/tag/\"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,\"clarity\",\"script\",\"{$cl}\");</script>\n";
	}
}, 1);
