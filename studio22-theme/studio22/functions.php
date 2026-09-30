<?php
/**
 * Studio22 theme: one-page site, English at /, Arabic at /ar/.
 */

if (!defined('ABSPATH')) {
	exit;
}

define('S22_VER', '1.0.0');

require_once __DIR__ . '/inc/content.php';

/* ---------- language: /ar/ is the Arabic version of the home page ---------- */
add_action('init', function () {
	add_rewrite_rule('^ar/?$', 'index.php?s22_lang=ar', 'top');
});
add_filter('query_vars', function ($v) {
	$v[] = 's22_lang';
	return $v;
});
// new rewrite rule needs a flush once, when the theme is switched on (and after an update)
add_action('after_switch_theme', 'flush_rewrite_rules');
add_action('init', function () {
	if (get_option('s22_rules_ver') !== S22_VER) {
		flush_rewrite_rules();
		update_option('s22_rules_ver', S22_VER);
	}
}, 99);

function s22_lang() {
	return get_query_var('s22_lang') === 'ar' ? 'ar' : 'en';
}

// /ar/ goes to the one-page template, not the blog index
add_filter('template_include', function ($t) {
	if (get_query_var('s22_lang') === 'ar') {
		return get_theme_file_path('front-page.php');
	}
	return $t;
});
// WordPress would treat /ar/ as the home query; keep it from 404ing
add_action('parse_query', function ($q) {
	if ($q->is_main_query() && $q->get('s22_lang') === 'ar') {
		$q->is_home = false;
		$q->is_404 = false;
	}
});

/* ---------- setup ---------- */
add_action('after_setup_theme', function () {
	add_theme_support('title-tag');
	add_theme_support('post-thumbnails');
	add_theme_support('custom-logo', array('height' => 80, 'width' => 240, 'flex-width' => true, 'flex-height' => true));
});

add_filter('pre_get_document_title', function ($t) {
	if (is_front_page() || get_query_var('s22_lang') === 'ar') {
		return s22_t('meta_title');
	}
	return $t;
});

add_action('wp_enqueue_scripts', function () {
	$lang = s22_lang();
	$fonts = $lang === 'ar'
		? 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap'
		: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap';
	wp_enqueue_style('s22-fonts', $fonts, array(), null);
	wp_enqueue_style('s22', get_theme_file_uri('assets/main.css'), array('s22-fonts'), S22_VER);
	wp_enqueue_script('s22', get_theme_file_uri('assets/main.js'), array(), S22_VER, true);
	// the one-page site doesn't use block styles
	if (is_front_page() || $lang === 'ar') {
		wp_dequeue_style('wp-block-library');
		wp_dequeue_style('global-styles');
		wp_dequeue_style('classic-theme-styles');
	}
});

add_action('wp_head', function () {
	if (!(is_front_page() || get_query_var('s22_lang') === 'ar')) {
		return;
	}
	$lang = s22_lang();
	$url = $lang === 'ar' ? home_url('/ar/') : home_url('/');
	$img = s22_img('hero');
	echo '<meta name="description" content="' . esc_attr(s22_t('meta_desc')) . '">' . "\n";
	echo '<link rel="canonical" href="' . esc_url($url) . '">' . "\n";
	echo '<link rel="alternate" hreflang="en" href="' . esc_url(home_url('/')) . '">' . "\n";
	echo '<link rel="alternate" hreflang="ar" href="' . esc_url(home_url('/ar/')) . '">' . "\n";
	echo '<link rel="alternate" hreflang="x-default" href="' . esc_url(home_url('/')) . '">' . "\n";
	echo '<meta property="og:type" content="website">' . "\n";
	echo '<meta property="og:title" content="' . esc_attr(s22_t('meta_title')) . '">' . "\n";
	echo '<meta property="og:description" content="' . esc_attr(s22_t('meta_desc')) . '">' . "\n";
	echo '<meta property="og:url" content="' . esc_url($url) . '">' . "\n";
	if ($img) {
		echo '<meta property="og:image" content="' . esc_url($img) . '">' . "\n";
	}
	$c = s22_contact();
	$ld = array(
		'@context' => 'https://schema.org',
		'@type' => 'ProfessionalService',
		'name' => 'Studio22',
		'url' => home_url('/'),
		'description' => s22_t('meta_desc', 'en'),
		'telephone' => $c['phone'],
		'email' => $c['email'],
		'address' => array('@type' => 'PostalAddress', 'addressLocality' => 'Doha', 'addressCountry' => 'QA'),
		'areaServed' => 'Qatar',
		'founder' => array('@type' => 'Person', 'name' => 'Abdulaziz Alajmi', 'jobTitle' => 'Founder'),
		'sameAs' => array_values(array_filter(array($c['instagram_url']))),
	);
	echo '<script type="application/ld+json">' . wp_json_encode($ld, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . '</script>' . "\n";
});

/* ---------- Customizer: contact details and photos ---------- */
add_action('customize_register', function ($wp) {
	$wp->add_section('s22', array('title' => 'Studio22', 'priority' => 30,
		'description' => 'Contact details and photos of the home page. Leave a photo empty to hide it.'));
	$text = array(
		's22_phone' => array('Phone (international format)', '+97460055600'),
		's22_whatsapp' => array('WhatsApp number (digits only, with country code)', '97460055600'),
		's22_email' => array('Email', 'studio22qa@gmail.com'),
		's22_instagram' => array('Instagram username (without @)', 'alajmiofficial'),
		's22_location' => array('Location', 'Doha, Qatar'),
	);
	foreach ($text as $id => $d) {
		$wp->add_setting($id, array('default' => $d[1], 'sanitize_callback' => 'sanitize_text_field'));
		$wp->add_control($id, array('label' => $d[0], 'section' => 's22', 'type' => 'text'));
	}
	$imgs = array('hero' => 'Hero photo (wide)', 'about' => 'Founder photo (portrait)');
	for ($i = 1; $i <= 6; $i++) {
		$imgs['work' . $i] = 'Work photo ' . $i;
	}
	foreach ($imgs as $k => $label) {
		$wp->add_setting('s22_img_' . $k, array('default' => '', 'sanitize_callback' => 'absint'));
		$wp->add_control(new WP_Customize_Media_Control($wp, 's22_img_' . $k,
			array('label' => $label, 'section' => 's22', 'mime_type' => 'image')));
	}
});

function s22_contact() {
	$ig = trim(ltrim(get_theme_mod('s22_instagram', 'alajmiofficial'), '@'));
	$wa = preg_replace('/\D+/', '', get_theme_mod('s22_whatsapp', '97460055600'));
	return array(
		'phone' => get_theme_mod('s22_phone', '+97460055600'),
		'whatsapp' => $wa,
		'whatsapp_url' => $wa ? 'https://wa.me/' . $wa : '',
		'email' => get_theme_mod('s22_email', 'studio22qa@gmail.com'),
		'instagram' => $ig,
		'instagram_url' => $ig ? 'https://www.instagram.com/' . rawurlencode($ig) . '/' : '',
		'location' => get_theme_mod('s22_location', 'Doha, Qatar'),
	);
}

function s22_img($key, $size = 'large') {
	$id = (int) get_theme_mod('s22_img_' . $key, 0);
	if (!$id) {
		return '';
	}
	$src = wp_get_attachment_image_url($id, $size);
	return $src ? $src : '';
}

// "+97460055600" -> "+974 6005 5600"
function s22_phone_display($p) {
	$d = preg_replace('/\D+/', '', $p);
	if (strpos($d, '974') === 0 && strlen($d) === 11) {
		return '+974 ' . substr($d, 3, 4) . ' ' . substr($d, 7);
	}
	return $p;
}

// inline line icons (stroke uses currentColor)
function s22_icon($name) {
	$p = array(
		'event' => '<path d="M4 7h16v13H4z"/><path d="M4 11h16M9 3v4M15 3v4"/><path d="M9.5 15.5l1.8 1.8 3.4-3.6"/>',
		'corp' => '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>',
		'brand' => '<path d="M4 20l4-12 4 6 3-4 5 10z"/><circle cx="17" cy="6" r="2"/>',
		'social' => '<rect x="6" y="2.5" width="12" height="19" rx="3"/><path d="M10.5 9.5v5l4-2.5z"/>',
		'camera' => '<path d="M3 8h4l2-3h6l2 3h4v12H3z"/><circle cx="12" cy="13.5" r="3.8"/>',
		'phone' => '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
		'mail' => '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
		'pin' => '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
		'instagram' => '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/>',
		'arrow' => '<path d="M5 12h14M13 6l6 6-6 6"/>',
	);
	if ($name === 'whatsapp') {
		return '<svg class="s22-i" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" stroke="none" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2c0 1.3.9 2.5 1.1 2.7.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>';
	}
	return isset($p[$name]) ? '<svg class="s22-i" viewBox="0 0 24 24" aria-hidden="true">' . $p[$name] . '</svg>' : '';
}
