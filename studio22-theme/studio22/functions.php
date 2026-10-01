<?php
/**
 * Studio22 theme functions.
 *
 * @package Studio22
 */

defined( 'ABSPATH' ) || exit;

define( 'STUDIO22_VERSION', '1.0.0' );
define( 'STUDIO22_CLIENTS', 10 );

require get_template_directory() . '/inc/helpers.php';
require get_template_directory() . '/inc/customizer.php';
require get_template_directory() . '/inc/projects.php';
require get_template_directory() . '/inc/template-tags.php';

/**
 * Theme setup.
 */
function studio22_setup() {
	load_theme_textdomain( 'studio22', get_template_directory() . '/languages' );

	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'automatic-feed-links' );
	add_theme_support( 'responsive-embeds' );
	add_theme_support( 'align-wide' );
	add_theme_support( 'editor-styles' );
	add_theme_support( 'html5', array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script', 'navigation-widgets' ) );
	add_theme_support(
		'custom-logo',
		array(
			'height'      => 80,
			'width'       => 240,
			'flex-height' => true,
			'flex-width'  => true,
		)
	);

	add_image_size( 'studio22-card', 900, 1100, true );
	add_image_size( 'studio22-wide', 1600, 900, true );

	register_nav_menus(
		array(
			'primary' => __( 'Main menu', 'studio22' ),
			'footer'  => __( 'Footer menu', 'studio22' ),
		)
	);

	add_editor_style( 'assets/css/editor.css' );

	// A ready-made front page and menu on a fresh site.
	add_theme_support(
		'starter-content',
		array(
			'posts'     => array(
				'home' => array(
					'post_type'  => 'page',
					'post_title' => __( 'Home', 'studio22' ),
				),
				'blog' => array(
					'post_type'  => 'page',
					'post_title' => __( 'Journal', 'studio22' ),
				),
			),
			'options'   => array(
				'show_on_front'  => 'page',
				'page_on_front'  => '{{home}}',
				'page_for_posts' => '{{blog}}',
			),
			'nav_menus' => array(
				'primary' => array(
					'name'  => __( 'Main menu', 'studio22' ),
					'items' => array(
						'link_home',
						'work'     => array(
							'title' => __( 'Work', 'studio22' ),
							'url'   => '#work',
						),
						'services' => array(
							'title' => __( 'Services', 'studio22' ),
							'url'   => '#services',
						),
						'studio'   => array(
							'title' => __( 'Studio', 'studio22' ),
							'url'   => '#studio',
						),
						'contact'  => array(
							'title' => __( 'Contact', 'studio22' ),
							'url'   => '#contact',
						),
					),
				),
			),
		)
	);
}
add_action( 'after_setup_theme', 'studio22_setup' );

/**
 * Content width for embeds.
 */
function studio22_content_width() {
	$GLOBALS['content_width'] = 1200;
}
add_action( 'after_setup_theme', 'studio22_content_width', 0 );

/**
 * Widget area in the footer.
 */
function studio22_widgets_init() {
	register_sidebar(
		array(
			'name'          => __( 'Footer', 'studio22' ),
			'id'            => 'footer-1',
			'description'   => __( 'Extra widgets shown in the footer.', 'studio22' ),
			'before_widget' => '<div id="%1$s" class="widget %2$s">',
			'after_widget'  => '</div>',
			'before_title'  => '<h3 class="widget-title">',
			'after_title'   => '</h3>',
		)
	);
}
add_action( 'widgets_init', 'studio22_widgets_init' );

/**
 * Google Fonts: Syne + Inter for English, Cairo + IBM Plex Sans Arabic for Arabic.
 */
function studio22_fonts_url() {
	$families = array(
		'family=Syne:wght@500;600;700;800',
		'family=Inter:wght@300;400;500;600',
		'family=Cairo:wght@500;600;700;800',
		'family=IBM+Plex+Sans+Arabic:wght@300;400;500;600',
	);
	return 'https://fonts.googleapis.com/css2?' . implode( '&', $families ) . '&display=swap';
}

/**
 * Scripts and styles.
 */
function studio22_scripts() {
	wp_enqueue_style( 'studio22-fonts', studio22_fonts_url(), array(), null );
	wp_enqueue_style( 'studio22-main', get_template_directory_uri() . '/assets/css/main.css', array(), STUDIO22_VERSION );
	wp_add_inline_style( 'studio22-main', studio22_dynamic_css() );

	wp_enqueue_script( 'studio22-main', get_template_directory_uri() . '/assets/js/main.js', array(), STUDIO22_VERSION, true );
	wp_localize_script(
		'studio22-main',
		'studio22',
		array(
			'whatsapp' => studio22_whatsapp_number(),
			'labels'   => array(
				'name'    => __( 'Name', 'studio22' ),
				'service' => __( 'Service', 'studio22' ),
				'date'    => __( 'Date', 'studio22' ),
				'close'   => __( 'Close', 'studio22' ),
			),
		)
	);

	if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
		wp_enqueue_script( 'comment-reply' );
	}
}
add_action( 'wp_enqueue_scripts', 'studio22_scripts' );

/**
 * Mark JS as available before the page paints, so scroll animations do not flash.
 */
function studio22_js_class() {
	echo "<script>document.documentElement.classList.add('js');</script>\n";
}
add_action( 'wp_head', 'studio22_js_class', 1 );

/**
 * Preconnect to Google Fonts.
 *
 * @param array  $urls          URLs to print for resource hints.
 * @param string $relation_type The relation type the URLs are printed for.
 * @return array
 */
function studio22_resource_hints( $urls, $relation_type ) {
	if ( 'preconnect' === $relation_type ) {
		$urls[] = array(
			'href' => 'https://fonts.gstatic.com',
			'crossorigin',
		);
	}
	return $urls;
}
add_filter( 'wp_resource_hints', 'studio22_resource_hints', 10, 2 );

/**
 * Accent colour from the Customizer.
 *
 * @return string
 */
function studio22_dynamic_css() {
	$accent = sanitize_hex_color( studio22_opt( 'accent' ) );
	if ( ! $accent ) {
		$accent = '#c21d4f';
	}
	return ':root{--s22-accent:' . $accent . ';}';
}

/**
 * Body classes.
 *
 * @param array $classes Body classes.
 * @return array
 */
function studio22_body_classes( $classes ) {
	if ( studio22_is_arabic() ) {
		$classes[] = 'lang-ar';
	}
	if ( is_front_page() && ! is_home() ) {
		$classes[] = 'has-hero';
	}
	return $classes;
}
add_filter( 'body_class', 'studio22_body_classes' );

/**
 * Shorter excerpts.
 *
 * @return int
 */
function studio22_excerpt_length() {
	return 22;
}
add_filter( 'excerpt_length', 'studio22_excerpt_length' );

/**
 * Excerpt "more" text.
 *
 * @return string
 */
function studio22_excerpt_more() {
	return '…';
}
add_filter( 'excerpt_more', 'studio22_excerpt_more' );
