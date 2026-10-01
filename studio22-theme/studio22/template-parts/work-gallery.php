<?php
/**
 * Portfolio photos shipped with the theme, shown until projects are added.
 *
 * @package Studio22
 */

$s22_gallery = array(
	array(
		'file'  => 'work-show.jpg',
		'type'  => __( 'Equestrian', 'studio22' ),
		'title' => __( 'Arabian horse show, Doha', 'studio22' ),
	),
	array(
		'file'  => 'work-doha.jpg',
		'type'  => __( 'Drone', 'studio22' ),
		'title' => __( 'The Pearl at dusk', 'studio22' ),
	),
	array(
		'file'  => 'founder.jpg',
		'type'  => __( 'Heritage', 'studio22' ),
		'title' => __( 'Horse & owner portrait', 'studio22' ),
	),
	array(
		'file'  => 'work-portrait.jpg',
		'type'  => __( 'Portrait', 'studio22' ),
		'title' => __( 'Event portraits', 'studio22' ),
	),
	array(
		'file'  => 'hero-poster.jpg',
		'type'  => __( 'Film', 'studio22' ),
		'title' => __( 'Studio22 reel', 'studio22' ),
		'video' => get_template_directory_uri() . '/assets/media/hero.mp4',
	),
);
?>
<div class="work__grid">
	<?php foreach ( $s22_gallery as $s22_item ) : ?>
		<?php
		$s22_src  = studio22_theme_image( $s22_item['file'] );
		$s22_full = empty( $s22_item['video'] ) ? $s22_src : $s22_item['video'];
		?>
		<article class="project-card reveal">
			<a class="project-card__link" href="<?php echo esc_url( $s22_full ); ?>" data-lightbox="<?php echo empty( $s22_item['video'] ) ? 'image' : 'video'; ?>" data-src="<?php echo esc_url( $s22_full ); ?>">
				<div class="project-card__media">
					<img src="<?php echo esc_url( $s22_src ); ?>" alt="<?php echo esc_attr( $s22_item['title'] ); ?>" loading="lazy">
					<?php if ( ! empty( $s22_item['video'] ) ) : ?>
						<span class="project-card__play"><?php echo studio22_icon( 'play' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
					<?php endif; ?>
				</div>
				<div class="project-card__info">
					<span class="project-card__type"><?php echo esc_html( $s22_item['type'] ); ?></span>
					<h3 class="project-card__title"><?php echo esc_html( $s22_item['title'] ); ?></h3>
				</div>
			</a>
		</article>
	<?php endforeach; ?>
</div>
