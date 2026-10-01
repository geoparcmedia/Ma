<?php
/**
 * Template tags.
 *
 * @package Studio22
 */

defined( 'ABSPATH' ) || exit;

/**
 * Site logo: the Customizer logo, or the Studio22 logo shipped with the theme.
 *
 * @param string $class Extra class.
 */
function studio22_logo( $class = '' ) {
	$name = get_bloginfo( 'name' );
	echo '<a class="site-logo ' . esc_attr( $class ) . '" href="' . esc_url( home_url( '/' ) ) . '" rel="home">';
	$logo_id = get_theme_mod( 'custom_logo' );
	if ( $logo_id ) {
		echo wp_get_attachment_image(
			$logo_id,
			'medium',
			false,
			array(
				'alt'   => $name,
				'class' => 'site-logo__img',
			)
		);
	} else {
		printf(
			'<img class="site-logo__img" src="%s" width="480" height="280" alt="%s">',
			esc_url( get_template_directory_uri() . '/assets/img/logo.png' ),
			esc_attr( $name )
		);
	}
	echo '</a>';
}

/**
 * Fallback when no menu is assigned: links to the home page sections.
 */
function studio22_menu_fallback() {
	$base  = is_front_page() ? '' : home_url( '/' );
	$items = array(
		'#work'     => __( 'Work', 'studio22' ),
		'#services' => __( 'Services', 'studio22' ),
		'#studio'   => __( 'Studio', 'studio22' ),
		'#clients'  => __( 'Clients', 'studio22' ),
		'#contact'  => __( 'Contact', 'studio22' ),
	);
	echo '<ul class="menu">';
	foreach ( $items as $anchor => $label ) {
		echo '<li class="menu-item"><a href="' . esc_url( $base . $anchor ) . '">' . esc_html( $label ) . '</a></li>';
	}
	echo '</ul>';
}

/**
 * Language switcher for Polylang or WPML.
 */
function studio22_language_switcher() {
	$languages = array();

	if ( function_exists( 'pll_the_languages' ) ) {
		$list = pll_the_languages(
			array(
				'raw'           => 1,
				'hide_if_empty' => 0,
			)
		);
		foreach ( (array) $list as $lang ) {
			$languages[] = array(
				'url'     => $lang['url'],
				'label'   => $lang['slug'],
				'name'    => $lang['name'],
				'current' => ! empty( $lang['current_lang'] ),
			);
		}
	} elseif ( has_filter( 'wpml_active_languages' ) ) {
		$list = apply_filters( 'wpml_active_languages', null, array( 'skip_missing' => 0 ) );
		foreach ( (array) $list as $lang ) {
			$languages[] = array(
				'url'     => $lang['url'],
				'label'   => $lang['language_code'],
				'name'    => $lang['native_name'],
				'current' => ! empty( $lang['active'] ),
			);
		}
	}

	if ( count( $languages ) < 2 ) {
		return;
	}

	echo '<nav class="lang-switch" aria-label="' . esc_attr__( 'Language', 'studio22' ) . '">';
	foreach ( $languages as $lang ) {
		$label = 'ar' === $lang['label'] ? 'ع' : strtoupper( $lang['label'] );
		printf(
			'<a href="%s" lang="%s" title="%s"%s>%s</a>',
			esc_url( $lang['url'] ),
			esc_attr( $lang['label'] ),
			esc_attr( $lang['name'] ),
			$lang['current'] ? ' aria-current="true" class="is-current"' : '',
			esc_html( $label )
		);
	}
	echo '</nav>';
}

/**
 * Social links.
 */
function studio22_social_links() {
	$links = '';
	foreach ( studio22_social_networks() as $slug => $label ) {
		$url = studio22_opt( "social_{$slug}" );
		if ( $url ) {
			$links .= '<a href="' . esc_url( $url ) . '" target="_blank" rel="noopener" aria-label="' . esc_attr( $label ) . '">' . studio22_icon( $slug ) . '</a>';
		}
	}
	if ( $links ) {
		echo '<div class="social">' . $links . '</div>'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- escaped above.
	}
}

/**
 * URL of an image picked in the Customizer.
 *
 * @param string $key  Option key.
 * @param string $size Image size.
 * @return string
 */
function studio22_image_url( $key, $size = 'full' ) {
	$id = absint( studio22_opt( $key ) );
	if ( ! $id ) {
		return '';
	}
	$src = wp_get_attachment_image_url( $id, $size );
	return $src ? $src : '';
}

/**
 * Section heading (small kicker + title).
 *
 * @param string $kicker_key Text key of the kicker.
 * @param string $title_key  Text key of the title.
 * @param string $id         Heading id.
 */
function studio22_section_heading( $kicker_key, $title_key, $id = '' ) {
	echo '<header class="section-head reveal">';
	echo '<p class="kicker">' . esc_html( studio22_text( $kicker_key ) ) . '</p>';
	echo '<h2 class="section-title"' . ( $id ? ' id="' . esc_attr( $id ) . '"' : '' ) . '>' . esc_html( studio22_text( $title_key ) ) . '</h2>';
	echo '</header>';
}

/**
 * Project card used on the home page and in the archive.
 */
function studio22_project_card() {
	$post_id = get_the_ID();
	$video   = studio22_video_source( get_post_meta( $post_id, '_s22_video', true ) );
	$terms   = get_the_terms( $post_id, 's22_project_type' );
	$slugs   = array();
	$names   = array();
	if ( $terms && ! is_wp_error( $terms ) ) {
		foreach ( $terms as $term ) {
			$slugs[] = $term->slug;
			$names[] = $term->name;
		}
	}
	$full = get_the_post_thumbnail_url( $post_id, 'full' );

	$attrs = '';
	if ( $video ) {
		$attrs = ' data-lightbox="' . esc_attr( $video['type'] ) . '" data-src="' . esc_url( $video['src'] ) . '"';
	} elseif ( $full ) {
		$attrs = ' data-lightbox="image" data-src="' . esc_url( $full ) . '"';
	}
	?>
	<article class="project-card reveal" data-type="<?php echo esc_attr( implode( ' ', $slugs ) ); ?>">
		<a class="project-card__link" href="<?php the_permalink(); ?>"<?php echo $attrs; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- escaped above. ?>>
			<div class="project-card__media">
				<?php
				if ( has_post_thumbnail() ) {
					the_post_thumbnail( 'studio22-card', array( 'loading' => 'lazy' ) );
				} else {
					echo '<span class="project-card__placeholder">' . studio22_icon( $video ? 'video' : 'camera' ) . '</span>'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
				}
				if ( $video ) {
					echo '<span class="project-card__play">' . studio22_icon( 'play' ) . '</span>'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
				}
				?>
			</div>
			<div class="project-card__info">
				<?php if ( $names ) : ?>
					<span class="project-card__type"><?php echo esc_html( implode( ' · ', $names ) ); ?></span>
				<?php endif; ?>
				<h3 class="project-card__title"><?php the_title(); ?></h3>
			</div>
		</a>
	</article>
	<?php
}

/**
 * Filter buttons for the project grid.
 */
function studio22_project_filters() {
	$terms = get_terms(
		array(
			'taxonomy'   => 's22_project_type',
			'hide_empty' => true,
		)
	);
	if ( is_wp_error( $terms ) || count( $terms ) < 2 ) {
		return;
	}
	echo '<div class="filters reveal" role="group" aria-label="' . esc_attr__( 'Filter projects', 'studio22' ) . '">';
	echo '<button type="button" class="filter is-active" data-filter="*" aria-pressed="true">' . esc_html__( 'All', 'studio22' ) . '</button>';
	foreach ( $terms as $term ) {
		echo '<button type="button" class="filter" data-filter="' . esc_attr( $term->slug ) . '" aria-pressed="false">' . esc_html( $term->name ) . '</button>';
	}
	echo '</div>';
}

/**
 * Post date and category line.
 */
function studio22_post_meta() {
	echo '<p class="post-meta"><time datetime="' . esc_attr( get_the_date( 'c' ) ) . '">' . esc_html( get_the_date() ) . '</time>';
	$cats = get_the_category_list( ', ' );
	if ( $cats && 'post' === get_post_type() ) {
		echo ' · ' . wp_kses_post( $cats );
	}
	echo '</p>';
}

/**
 * Pagination.
 */
function studio22_pagination() {
	the_posts_pagination(
		array(
			'mid_size'  => 1,
			'prev_text' => '<span aria-hidden="true">←</span><span class="screen-reader-text">' . __( 'Previous', 'studio22' ) . '</span>',
			'next_text' => '<span class="screen-reader-text">' . __( 'Next', 'studio22' ) . '</span><span aria-hidden="true">→</span>',
		)
	);
}
