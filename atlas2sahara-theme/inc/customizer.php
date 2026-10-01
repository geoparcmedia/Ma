<?php
/**
 * Customizer options: homepage texts, images and contact details.
 */

/** Default values for every text option. */
function a2s_defaults() {
	return array(
		'a2s_hero_title'     => 'Bike Tours & Desert Adventures in Morocco',
		'a2s_hero_subtitle'  => 'Ride through palm groves, cross the High Atlas, walk with camel caravans into the Sahara and share mint tea in Berber villages – all with local guides who call this land home.',
		'a2s_hero_note'      => 'Welcome to Morocco, from the Atlas mountains to the Sahara desert.',
		'a2s_tours_title'    => 'Our Most Popular Biking and Desert Tours',
		'a2s_tours_subtitle' => 'Experience the best of Morocco\'s outdoors with Atlas2Sahara\'s favourite biking, hiking and desert trips.',
		'a2s_strip_text'     => 'Guided & self-guided tours · Local Moroccan guides · Small groups · Tailor-made trips',
		'a2s_about_kicker'   => 'Local guides, Moroccan hospitality, real adventures',
		'a2s_about_text'     => 'We craft biking, hiking and desert journeys across Morocco for travellers who want more than a postcard.',
		'a2s_about_text_2'   => 'By partnering with local families, guesthouses and desert camps, we create authentic adventures that also support the communities we travel through.',
		'a2s_custom_text'    => 'Every trip is a personal chapter in your story. Tell us your dates, pace and interests and we will build the Moroccan journey you have in mind.',
		'a2s_email'          => '',
		'a2s_phone'          => '',
		'a2s_address'        => 'Marrakech, Morocco',
		'a2s_instagram'      => '',
		'a2s_facebook'       => '',
	);
}

/** Read a customizer value with the same default the control uses. */
function a2s_opt( $id ) {
	$defaults = a2s_defaults();
	return get_theme_mod( $id, isset( $defaults[ $id ] ) ? $defaults[ $id ] : '' );
}

add_action( 'customize_register', function ( $wp_customize ) {
	$wp_customize->add_section( 'a2s_options', array(
		'title'    => __( 'Atlas2Sahara options', 'atlas2sahara' ),
		'priority' => 30,
	) );

	$images = array(
		'a2s_hero_image'   => 'Hero image',
		'a2s_about_image'  => 'About section background',
		'a2s_banner_image' => 'Wide banner image (above Stories)',
	);
	foreach ( $images as $id => $label ) {
		$wp_customize->add_setting( $id, array( 'sanitize_callback' => 'esc_url_raw' ) );
		$wp_customize->add_control( new WP_Customize_Image_Control( $wp_customize, $id, array(
			'label'   => $label,
			'section' => 'a2s_options',
		) ) );
	}

	$textareas = array( 'a2s_hero_subtitle', 'a2s_tours_subtitle', 'a2s_about_text', 'a2s_about_text_2', 'a2s_custom_text' );
	foreach ( a2s_defaults() as $id => $default ) {
		$wp_customize->add_setting( $id, array(
			'default'           => $default,
			'sanitize_callback' => in_array( $id, array( 'a2s_instagram', 'a2s_facebook' ), true ) ? 'esc_url_raw' : 'sanitize_text_field',
		) );
		$wp_customize->add_control( $id, array(
			'label'   => ucfirst( str_replace( array( 'a2s_', '_' ), array( '', ' ' ), $id ) ),
			'section' => 'a2s_options',
			'type'    => in_array( $id, $textareas, true ) ? 'textarea' : 'text',
		) );
	}
} );

/** Hero/about/banner image with the theme photo as fallback. */
function a2s_section_image( $id, $fallback ) {
	$url = get_theme_mod( $id );
	return $url ? $url : a2s_img( $fallback );
}
