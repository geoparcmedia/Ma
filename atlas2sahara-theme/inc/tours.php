<?php
/**
 * Tour post type, tour types, tour details and starter content.
 */

add_action( 'init', function () {
	register_post_type( 'tour', array(
		'labels'       => array(
			'name'          => __( 'Tours', 'atlas2sahara' ),
			'singular_name' => __( 'Tour', 'atlas2sahara' ),
			'add_new_item'  => __( 'Add new tour', 'atlas2sahara' ),
			'edit_item'     => __( 'Edit tour', 'atlas2sahara' ),
		),
		'public'       => true,
		'has_archive'  => 'tours',
		'rewrite'      => array( 'slug' => 'tour' ),
		'menu_icon'    => 'dashicons-palmtree',
		'supports'     => array( 'title', 'editor', 'excerpt', 'thumbnail', 'page-attributes' ),
		'show_in_rest' => true,
	) );

	register_taxonomy( 'tour_type', 'tour', array(
		'labels'            => array(
			'name'          => __( 'Tour types', 'atlas2sahara' ),
			'singular_name' => __( 'Tour type', 'atlas2sahara' ),
		),
		'hierarchical'      => true,
		'public'            => true,
		'show_admin_column' => true,
		'show_in_rest'      => true,
		'rewrite'           => array( 'slug' => 'tours/type' ),
	) );
} );

/** Detail fields stored as post meta. */
function a2s_tour_fields() {
	return array(
		'a2s_duration'   => 'Duration (e.g. 7 days)',
		'a2s_difficulty' => 'Difficulty (Easy / Moderate / Challenging)',
		'a2s_price'      => 'Price from (e.g. €890)',
		'a2s_style'      => 'Style (Guided / Self-guided)',
		'a2s_region'     => 'Region (e.g. High Atlas)',
		'a2s_highlights' => 'Highlights (one per line)',
	);
}

function a2s_tour_meta( $key, $post_id = null ) {
	return get_post_meta( $post_id ? $post_id : get_the_ID(), $key, true );
}

add_action( 'add_meta_boxes', function () {
	add_meta_box( 'a2s_tour_details', __( 'Tour details', 'atlas2sahara' ), function ( $post ) {
		wp_nonce_field( 'a2s_tour_details', 'a2s_tour_nonce' );
		foreach ( a2s_tour_fields() as $key => $label ) {
			$value = get_post_meta( $post->ID, $key, true );
			echo '<p><label for="' . esc_attr( $key ) . '"><strong>' . esc_html( $label ) . '</strong></label><br>';
			if ( 'a2s_highlights' === $key ) {
				echo '<textarea id="' . esc_attr( $key ) . '" name="' . esc_attr( $key ) . '" rows="5" style="width:100%">' . esc_textarea( $value ) . '</textarea>';
			} else {
				echo '<input type="text" id="' . esc_attr( $key ) . '" name="' . esc_attr( $key ) . '" value="' . esc_attr( $value ) . '" style="width:100%">';
			}
			echo '</p>';
		}
	}, 'tour', 'normal', 'high' );
} );

add_action( 'save_post_tour', function ( $post_id ) {
	if ( ! isset( $_POST['a2s_tour_nonce'] ) || ! wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST['a2s_tour_nonce'] ) ), 'a2s_tour_details' ) ) {
		return;
	}
	if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
		return;
	}
	if ( ! current_user_can( 'edit_post', $post_id ) ) {
		return;
	}
	foreach ( array_keys( a2s_tour_fields() ) as $key ) {
		if ( isset( $_POST[ $key ] ) ) {
			$value = 'a2s_highlights' === $key
				? sanitize_textarea_field( wp_unslash( $_POST[ $key ] ) )
				: sanitize_text_field( wp_unslash( $_POST[ $key ] ) );
			update_post_meta( $post_id, $key, $value );
		}
	}
} );

/**
 * Starter content, created once per seed version so a theme update
 * (which does not re-run activation hooks) still adds new content.
 */
define( 'A2S_SEED_VERSION', 4 );

add_action( 'init', function () {
	$done = (int) get_option( 'a2s_seed_version', 0 );
	if ( $done >= A2S_SEED_VERSION ) {
		return;
	}
	// The Elementor step waits until Elementor is installed and active.
	if ( $done >= 2 && ! did_action( 'elementor/loaded' ) ) {
		return;
	}
	update_option( 'a2s_seed_version', did_action( 'elementor/loaded' ) ? A2S_SEED_VERSION : 2 );
	if ( $done < 1 ) {
		a2s_seed_tours();
	}
	if ( $done < 2 ) {
		a2s_seed_stories();
	}
	if ( did_action( 'elementor/loaded' ) ) {
		a2s_seed_elementor_home();
	}
	flush_rewrite_rules();
}, 20 );

/** Tour types and six starter tours (skipped if tours already exist). */
function a2s_seed_tours() {
	$types = array(
		'biking' => 'Biking',
		'hiking' => 'Hiking',
		'desert' => 'Desert',
	);
	foreach ( $types as $slug => $name ) {
		if ( ! term_exists( $slug, 'tour_type' ) ) {
			wp_insert_term( $name, 'tour_type', array( 'slug' => $slug ) );
		}
	}

	if ( get_posts( array( 'post_type' => 'tour', 'post_status' => 'any', 'numberposts' => 1 ) ) ) {
		return;
	}

	$tours = array(
		array(
			'title'   => 'Atlas to Sahara Gravel Ride',
			'type'    => 'biking',
			'excerpt' => 'Ride from the snow-capped High Atlas down through the Draa Valley palm groves to the dunes of Merzouga.',
			'content' => "Eight days on gravel and quiet tarmac, crossing the Tizi n'Tichka pass, the kasbahs of Aït Benhaddou and the Dadès gorges before finishing among the dunes of Erg Chebbi.\n\nLuggage transfers, a support vehicle and a local guide are included, so all you carry is water and a camera.",
			'meta'    => array( '8 days', 'Moderate', '€1,190', 'Guided', 'High Atlas – Merzouga', "Tizi n'Tichka pass\nAït Benhaddou kasbah\nDadès & Todra gorges\nNight in a desert camp" ),
		),
		array(
			'title'   => 'Toubkal Summit Trek',
			'type'    => 'hiking',
			'excerpt' => 'Climb North Africa\'s highest peak (4,167 m) through Berber villages and walnut-shaded valleys.',
			'content' => "Start in Imlil, walk through the Mizane valley and sleep in mountain refuges before an early summit push for sunrise over the Atlas.\n\nMules carry the bags and a certified mountain guide leads every day.",
			'meta'    => array( '4 days', 'Challenging', '€420', 'Guided', 'High Atlas', "Summit of Jbel Toubkal\nBerber village stays\nCertified mountain guide\nMule luggage support" ),
		),
		array(
			'title'   => 'Merzouga Dunes & Camel Trek',
			'type'    => 'desert',
			'excerpt' => 'Camel caravans, a starlit camp in Erg Chebbi and sunrise from the top of the dunes.',
			'content' => "Leave Marrakech for the edge of the Sahara, ride camels into the dunes at sunset and spend the night in a traditional camp with music around the fire.\n\nReturn via the Todra gorges and the road of a thousand kasbahs.",
			'meta'    => array( '3 days', 'Easy', '€290', 'Guided', 'Sahara – Erg Chebbi', "Sunset camel ride\nNight in a desert camp\nSunrise on the dunes\nTodra gorges" ),
		),
		array(
			'title'   => 'Agafay & Atlas Foothills E-Bike Day',
			'type'    => 'biking',
			'excerpt' => 'An easy e-bike day from Marrakech into the stony Agafay desert and the first Atlas villages.',
			'content' => "One hour from Marrakech, the Agafay desert opens onto wide views of the Atlas. Ride e-bikes on dirt tracks, stop for mint tea with a local family and lunch by Lake Lalla Takerkoust.",
			'meta'    => array( '1 day', 'Easy', '€95', 'Guided', 'Agafay', "Pick-up in Marrakech\nTop-quality e-bikes\nLunch by the lake\nAtlas panoramas" ),
		),
		array(
			'title'   => 'M\'Goun Valleys Self-Guided Walk',
			'type'    => 'hiking',
			'excerpt' => 'Walk inn to inn through the Happy Valley of Aït Bouguemez with GPS routes and luggage transfers.',
			'content' => "Go at your own pace with detailed GPS tracks, a route book and nightly stays in family-run guesthouses. Your bags travel ahead of you each day.",
			'meta'    => array( '6 days', 'Moderate', '€640', 'Self-guided', 'Central High Atlas', "Aït Bouguemez valley\nGPS tracks & route book\nLuggage transfers\nFamily guesthouses" ),
		),
		array(
			'title'   => 'Zagora Desert Overland',
			'type'    => 'desert',
			'excerpt' => 'Follow the Draa river south to Zagora and the quieter dunes of Erg Chegaga by 4x4.',
			'content' => "A slower journey through palm oases and ancient ksour, ending with two nights in the remote dunes of Erg Chegaga, far from the crowds.",
			'meta'    => array( '5 days', 'Easy', '€560', 'Guided', 'Draa Valley – Erg Chegaga', "Draa valley oases\nRemote Erg Chegaga dunes\n4x4 desert crossing\nTwo nights under the stars" ),
		),
	);

	$keys = array_keys( a2s_tour_fields() );
	foreach ( $tours as $i => $tour ) {
		$post_id = wp_insert_post( array(
			'post_type'    => 'tour',
			'post_status'  => 'publish',
			'post_title'   => $tour['title'],
			'post_excerpt' => $tour['excerpt'],
			'post_content' => $tour['content'],
			'menu_order'   => $i,
		) );
		if ( ! $post_id || is_wp_error( $post_id ) ) {
			continue;
		}
		wp_set_object_terms( $post_id, $tour['type'], 'tour_type' );
		foreach ( $keys as $k => $key ) {
			update_post_meta( $post_id, $key, $tour['meta'][ $k ] );
		}
	}
}

/** Three starter blog posts for the "Our Stories" section. */
function a2s_seed_stories() {
	$stories = array(
		array(
			'title'   => 'Riding the Palmeraie: Gravel Biking Around Marrakech',
			'excerpt' => 'Dusty tracks, thousands of palm trees and a sunset you will not forget – our favourite easy ride from the city.',
			'content' => "Just outside the walls of Marrakech, the Palmeraie offers kilometres of flat gravel tracks between date palms, small farms and earthen villages.\n\nThe best time to ride is late afternoon, when the light turns gold and the Atlas peaks glow on the horizon. Bring water, a light layer for the evening and plenty of curiosity.",
		),
		array(
			'title'   => 'A Taste of Morocco: Dishes to Try on Your Trip',
			'excerpt' => 'From slow-cooked tagine to Berber bread baked in the sand, here is what to look forward to after a long day outdoors.',
			'content' => "Food is one of the great joys of travelling in Morocco. In the mountains, try a vegetable tagine cooked over charcoal. In the desert, ask for medfouna – the \"Berber pizza\" baked in hot sand.\n\nAnd of course, mint tea: poured from high above the glass, served with every welcome.",
		),
		array(
			'title'   => 'From the Atlas to the Sahara: What to Expect',
			'excerpt' => 'Mountain passes, kasbahs, palm valleys and the dunes of Merzouga – a guide to Morocco\'s most spectacular journey.',
			'content' => "The road from Marrakech to the Sahara crosses the High Atlas at the Tizi n'Tichka pass, then winds past the kasbahs of Aït Benhaddou and Ouarzazate, through the Dadès and Todra gorges, before the dunes of Erg Chebbi rise from the horizon.\n\nWhether you ride, hike or travel by 4x4, plan for changing temperatures: cool mornings in the mountains, warm afternoons in the desert.",
		),
	);
	foreach ( $stories as $story ) {
		if ( get_posts( array( 'post_type' => 'post', 'post_status' => 'any', 'title' => $story['title'], 'numberposts' => 1 ) ) ) {
			continue;
		}
		wp_insert_post( array(
			'post_type'    => 'post',
			'post_status'  => 'publish',
			'post_title'   => $story['title'],
			'post_excerpt' => $story['excerpt'],
			'post_content' => $story['content'],
		) );
	}
}

/** Guest reviews: title = guest name, content = review, excerpt = tour taken. */
add_action( 'init', function () {
	register_post_type( 'review', array(
		'labels'       => array(
			'name'          => __( 'Reviews', 'atlas2sahara' ),
			'singular_name' => __( 'Review', 'atlas2sahara' ),
			'add_new_item'  => __( 'Add new review (title = guest name, excerpt = tour)', 'atlas2sahara' ),
		),
		'public'       => false,
		'show_ui'      => true,
		'menu_icon'    => 'dashicons-format-quote',
		'supports'     => array( 'title', 'editor', 'excerpt' ),
		'show_in_rest' => true,
	) );
} );
