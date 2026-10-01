<?php
/**
 * Customizer options: hero image and contact details.
 */

add_action( 'customize_register', function ( $wp_customize ) {
	$wp_customize->add_section( 'a2s_options', array(
		'title'    => __( 'Atlas2Sahara options', 'atlas2sahara' ),
		'priority' => 30,
	) );

	$wp_customize->add_setting( 'a2s_hero_image', array( 'sanitize_callback' => 'esc_url_raw' ) );
	$wp_customize->add_control( new WP_Customize_Image_Control( $wp_customize, 'a2s_hero_image', array(
		'label'   => __( 'Hero background image', 'atlas2sahara' ),
		'section' => 'a2s_options',
	) ) );

	$text_fields = array(
		'a2s_hero_title'    => array( 'Hero title', 'From the Atlas to the Sahara, one adventure away' ),
		'a2s_hero_subtitle' => array( 'Hero subtitle', 'Guided and self-guided biking, hiking and desert tours across Morocco, planned by local people who ride and walk these trails every week.' ),
		'a2s_email'         => array( 'Contact email', '' ),
		'a2s_phone'         => array( 'Phone / WhatsApp', '' ),
		'a2s_address'       => array( 'Address', 'Marrakech, Morocco' ),
	);
	foreach ( $text_fields as $id => $field ) {
		$wp_customize->add_setting( $id, array(
			'default'           => $field[1],
			'sanitize_callback' => 'sanitize_text_field',
		) );
		$wp_customize->add_control( $id, array(
			'label'   => $field[0],
			'section' => 'a2s_options',
			'type'    => 'a2s_hero_subtitle' === $id ? 'textarea' : 'text',
		) );
	}
} );

/** Read a customizer value with the same default the control uses. */
function a2s_opt( $id ) {
	$defaults = array(
		'a2s_hero_title'    => 'From the Atlas to the Sahara, one adventure away',
		'a2s_hero_subtitle' => 'Guided and self-guided biking, hiking and desert tours across Morocco, planned by local people who ride and walk these trails every week.',
		'a2s_address'       => 'Marrakech, Morocco',
	);
	return get_theme_mod( $id, isset( $defaults[ $id ] ) ? $defaults[ $id ] : '' );
}
