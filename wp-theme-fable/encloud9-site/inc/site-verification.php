<?php
/**
 * Google Search Console ownership tag for the private staging site only.
 * Added 17 Nov 2026 so Michael can request a Safe Browsing review of
 * encloud9-new.flywheelsites.com (flagged "Dangerous site" on 17 Nov).
 * It prints nothing on any other host, so it does not follow the site to encloud9.com.
 */
if (!defined('ABSPATH')) exit;

add_action('wp_head', function () {
	$host = isset($_SERVER['HTTP_HOST']) ? strtolower($_SERVER['HTTP_HOST']) : '';
	if ($host !== 'encloud9-new.flywheelsites.com') return;
	echo '<meta name="google-site-verification" content="rNdBcKL99kESfq6F6pS8J8p5RvMOsNvrPq_RoSnrAM4" />' . "\n";
}, 1);
