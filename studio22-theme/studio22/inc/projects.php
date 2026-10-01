<?php
/**
 * Portfolio: "Projects" post type, "Project type" taxonomy and project details box.
 *
 * @package Studio22
 */

defined( 'ABSPATH' ) || exit;

/**
 * Register the post type and taxonomy.
 */
function studio22_register_projects() {
	register_post_type(
		's22_project',
		array(
			'labels'        => array(
				'name'          => __( 'Projects', 'studio22' ),
				'singular_name' => __( 'Project', 'studio22' ),
				'add_new_item'  => __( 'Add new project', 'studio22' ),
				'edit_item'     => __( 'Edit project', 'studio22' ),
				'all_items'     => __( 'All projects', 'studio22' ),
			),
			'public'        => true,
			'has_archive'   => true,
			'menu_icon'     => 'dashicons-format-video',
			'menu_position' => 5,
			'show_in_rest'  => true,
			'supports'      => array( 'title', 'editor', 'excerpt', 'thumbnail', 'page-attributes' ),
			'rewrite'       => array( 'slug' => 'work' ),
		)
	);

	register_taxonomy(
		's22_project_type',
		's22_project',
		array(
			'labels'            => array(
				'name'          => __( 'Project types', 'studio22' ),
				'singular_name' => __( 'Project type', 'studio22' ),
			),
			'hierarchical'      => true,
			'show_in_rest'      => true,
			'show_admin_column' => true,
			'rewrite'           => array( 'slug' => 'work-type' ),
		)
	);
}
add_action( 'init', 'studio22_register_projects' );

/**
 * Flush permalinks once when the theme is activated, so /work/ works right away.
 */
function studio22_flush_rewrites() {
	studio22_register_projects();
	flush_rewrite_rules();
}
add_action( 'after_switch_theme', 'studio22_flush_rewrites' );

/**
 * Project details meta box.
 */
function studio22_project_meta_box() {
	add_meta_box( 'studio22_project', __( 'Project details', 'studio22' ), 'studio22_project_meta_box_html', 's22_project', 'side' );
}
add_action( 'add_meta_boxes', 'studio22_project_meta_box' );

/**
 * Fields of the project details box.
 *
 * @return array
 */
function studio22_project_fields() {
	return array(
		'_s22_video'  => __( 'Video link (YouTube, Vimeo or .mp4)', 'studio22' ),
		'_s22_client' => __( 'Client', 'studio22' ),
		'_s22_year'   => __( 'Year', 'studio22' ),
	);
}

/**
 * Meta box output.
 *
 * @param WP_Post $post Current post.
 */
function studio22_project_meta_box_html( $post ) {
	wp_nonce_field( 'studio22_project', 'studio22_project_nonce' );
	foreach ( studio22_project_fields() as $key => $label ) {
		printf(
			'<p><label for="%1$s"><strong>%2$s</strong></label><br><input type="text" class="widefat" id="%1$s" name="%1$s" value="%3$s"></p>',
			esc_attr( $key ),
			esc_html( $label ),
			esc_attr( get_post_meta( $post->ID, $key, true ) )
		);
	}
	echo '<p class="description">' . esc_html__( 'The featured image is used as the cover. With a video link, the cover opens the video.', 'studio22' ) . '</p>';
}

/**
 * Save the project details.
 *
 * @param int $post_id Post ID.
 */
function studio22_save_project( $post_id ) {
	if ( ! isset( $_POST['studio22_project_nonce'] ) || ! wp_verify_nonce( sanitize_key( $_POST['studio22_project_nonce'] ), 'studio22_project' ) ) {
		return;
	}
	if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
		return;
	}
	if ( ! current_user_can( 'edit_post', $post_id ) ) {
		return;
	}
	foreach ( array_keys( studio22_project_fields() ) as $key ) {
		if ( ! isset( $_POST[ $key ] ) ) {
			continue;
		}
		$value = '_s22_video' === $key
			? esc_url_raw( wp_unslash( $_POST[ $key ] ) )
			: sanitize_text_field( wp_unslash( $_POST[ $key ] ) );
		update_post_meta( $post_id, $key, $value );
	}
}
add_action( 'save_post_s22_project', 'studio22_save_project' );

/**
 * Turn a YouTube / Vimeo / mp4 link into something the lightbox can play.
 *
 * @param string $url Video link.
 * @return array|null [ 'type' => 'iframe'|'video', 'src' => string ]
 */
function studio22_video_source( $url ) {
	if ( ! $url ) {
		return null;
	}
	if ( preg_match( '~(?:youtube\.com/(?:watch\?v=|embed/|shorts/)|youtu\.be/)([\w-]{6,})~', $url, $m ) ) {
		return array(
			'type' => 'iframe',
			'src'  => 'https://www.youtube-nocookie.com/embed/' . $m[1] . '?autoplay=1&rel=0',
		);
	}
	if ( preg_match( '~vimeo\.com/(?:video/)?(\d+)~', $url, $m ) ) {
		return array(
			'type' => 'iframe',
			'src'  => 'https://player.vimeo.com/video/' . $m[1] . '?autoplay=1',
		);
	}
	return array(
		'type' => 'video',
		'src'  => $url,
	);
}
