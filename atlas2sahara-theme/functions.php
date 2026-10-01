<?php
/**
 * Atlas2Sahara theme setup.
 */

define( 'A2S_VERSION', '1.0.0' );

require get_template_directory() . '/inc/tours.php';
require get_template_directory() . '/inc/customizer.php';

add_action( 'after_setup_theme', function () {
	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
	add_image_size( 'a2s-card', 800, 560, true );
	register_nav_menus( array(
		'primary' => __( 'Primary menu', 'atlas2sahara' ),
		'footer'  => __( 'Footer menu', 'atlas2sahara' ),
	) );
} );

add_action( 'wp_enqueue_scripts', function () {
	wp_enqueue_style( 'a2s-fonts', 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap', array(), null );
	wp_enqueue_style( 'a2s-main', get_template_directory_uri() . '/assets/css/main.css', array(), A2S_VERSION );
	wp_enqueue_script( 'a2s-main', get_template_directory_uri() . '/assets/js/main.js', array(), A2S_VERSION, true );
} );

/** Fallback menu used until a menu is assigned in Appearance → Menus. */
function a2s_fallback_menu() {
	$items = array(
		home_url( '/#tours' )        => 'Tours',
		home_url( '/#experiences' )  => 'Experiences',
		home_url( '/#destinations' ) => 'Destinations',
		home_url( '/#how' )          => 'How it works',
		home_url( '/#contact' )      => 'Contact',
	);
	echo '<ul class="menu">';
	foreach ( $items as $url => $label ) {
		printf( '<li><a href="%s">%s</a></li>', esc_url( $url ), esc_html( $label ) );
	}
	echo '</ul>';
}

/** Small inline icon set. */
function a2s_icon( $name ) {
	$icons = array(
		'bike'     => '<circle cx="5.5" cy="17.5" r="3.5"/><circle cx="18.5" cy="17.5" r="3.5"/><path d="M15 6h2l3 11.5M5.5 17.5 9 9h6l-3.5 8.5M9 9 7.5 6H5"/>',
		'hike'     => '<path d="m3 20 6-11 4 6 3-4 5 9z"/><path d="m11.5 12.5 1.5-2"/>',
		'desert'   => '<circle cx="17" cy="6" r="2.5"/><path d="M2 19c3-4 6-6 10-6s7 2 10 6"/><path d="M2 21h20"/>',
		'star'     => '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
		'guide'    => '<circle cx="12" cy="7" r="3.5"/><path d="M5 21v-2a7 7 0 0 1 14 0v2"/>',
		'shield'   => '<path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
		'leaf'     => '<path d="M5 19c0-8 5-14 15-14 0 10-6 15-14 15"/><path d="M5 19 12 12"/>',
		'map'      => '<path d="m3 6 6-3 6 3 6-3v15l-6 3-6-3-6 3z"/><path d="M9 3v15M15 6v15"/>',
		'clock'    => '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
		'gauge'    => '<path d="M4 18a8 8 0 1 1 16 0"/><path d="m12 18 4-6"/>',
		'arrow'    => '<path d="M5 12h14M13 6l6 6-6 6"/>',
		'mail'     => '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
		'phone'    => '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
		'pin'      => '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
	);
	if ( ! isset( $icons[ $name ] ) ) {
		return '';
	}
	return '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' . $icons[ $name ] . '</svg>';
}
