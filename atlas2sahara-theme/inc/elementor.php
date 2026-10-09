<?php
/**
 * Elementor integration: an editable Elementor "Home" page built from
 * inc/elementor-home.json, and full-width rendering of Elementor content.
 */

/** Bump when inc/elementor-home.json changes, so sites get the new Home page. */
define( 'A2S_HOME_VERSION', 2 );

/** True when the post was built with Elementor and Elementor is active. */
function a2s_is_elementor( $post_id = null ) {
	$post_id = $post_id ? $post_id : get_the_ID();
	return $post_id
		&& did_action( 'elementor/loaded' )
		&& 'builder' === get_post_meta( $post_id, '_elementor_edit_mode', true );
}

/** Elementor page data with the theme tokens replaced by this site's URLs. */
function a2s_elementor_home_data() {
	$json = file_get_contents( get_template_directory() . '/inc/elementor-home.json' );
	$url  = function ( $u ) {
		return substr( wp_json_encode( $u, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ), 1, -1 );
	};
	$find = function ( $slug, $type ) {
		$post = get_page_by_path( $slug, OBJECT, $type );
		return $post ? get_permalink( $post ) : home_url( '/' );
	};

	$json = str_replace(
		array( '{THEME}', '{HOME}', '{CONTACT}' ),
		array( $url( get_template_directory_uri() ), $url( untrailingslashit( home_url() ) ), $url( home_url( '/#contact' ) ) ),
		$json
	);
	return preg_replace_callback( '/\{(TOUR|POST|TYPE):([a-z0-9-]+)\}/', function ( $m ) use ( $url, $find ) {
		if ( 'TYPE' === $m[1] ) {
			$link = get_term_link( $m[2], 'tour_type' );
			return $url( is_wp_error( $link ) ? home_url( '/' ) : $link );
		}
		return $url( $find( $m[2], 'TOUR' === $m[1] ? 'tour' : 'post' ) );
	}, $json );
}

/**
 * Create the Elementor "Home" page (and a "Stories" page for the blog) and use
 * them as the front and posts pages, as soon as Elementor is active. The front
 * page is only switched if the site still shows latest posts there, or if it is
 * an older generated Home page (which is then kept as a draft).
 */
function a2s_seed_elementor_home() {
	$cpt = get_option( 'elementor_cpt_support', array( 'page', 'post' ) );
	if ( is_array( $cpt ) && ! in_array( 'tour', $cpt, true ) ) {
		$cpt[] = 'tour';
		update_option( 'elementor_cpt_support', $cpt );
	}

	$existing = get_posts( array( 'post_type' => 'page', 'post_status' => 'any', 'meta_key' => '_a2s_home', 'numberposts' => 1 ) );
	$old      = $existing ? $existing[0] : null;
	if ( $old && (int) get_post_meta( $old->ID, '_a2s_home', true ) >= A2S_HOME_VERSION ) {
		return;
	}

	$home_id = wp_insert_post( array(
		'post_type'   => 'page',
		'post_status' => 'publish',
		'post_title'  => 'Home',
	) );
	if ( ! $home_id || is_wp_error( $home_id ) ) {
		return;
	}
	update_post_meta( $home_id, '_a2s_home', A2S_HOME_VERSION );
	update_post_meta( $home_id, '_elementor_edit_mode', 'builder' );
	update_post_meta( $home_id, '_elementor_template_type', 'wp-page' );
	update_post_meta( $home_id, '_elementor_version', defined( 'ELEMENTOR_VERSION' ) ? ELEMENTOR_VERSION : '3.0.0' );
	update_post_meta( $home_id, '_elementor_page_settings', array( 'hide_title' => 'yes' ) );
	update_post_meta( $home_id, '_wp_page_template', 'elementor_header_footer' );
	update_post_meta( $home_id, '_elementor_data', wp_slash( a2s_elementor_home_data() ) );

	// An older generated Home page is kept as a draft (nothing is deleted).
	if ( $old ) {
		if ( (int) get_option( 'page_on_front' ) === $old->ID ) {
			update_option( 'page_on_front', $home_id );
		}
		delete_post_meta( $old->ID, '_a2s_home' );
		wp_update_post( array( 'ID' => $old->ID, 'post_status' => 'draft', 'post_title' => 'Home (previous design)' ) );
		return;
	}

	if ( 'posts' === get_option( 'show_on_front' ) ) {
		update_option( 'page_on_front', $home_id );
		update_option( 'show_on_front', 'page' );
		if ( ! get_option( 'page_for_posts' ) ) {
			$stories_id = wp_insert_post( array(
				'post_type'   => 'page',
				'post_status' => 'publish',
				'post_title'  => 'Stories',
				'post_name'   => 'stories',
			) );
			if ( $stories_id && ! is_wp_error( $stories_id ) ) {
				update_option( 'page_for_posts', $stories_id );
			}
		}
	}
}
