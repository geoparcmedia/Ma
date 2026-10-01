<?php
/**
 * Hero: full-screen video banner. In "scrub" mode it stays pinned while the
 * visitor scrolls and the video advances with the scroll.
 *
 * @package Studio22
 */

$s22_mode   = studio22_opt( 'hero_mode' );
$s22_vid_id = absint( studio22_opt( 'hero_video' ) );
$s22_poster = studio22_image_url( 'hero_poster' );
$s22_theme  = get_template_directory_uri() . '/assets';

// Video sources: the one picked in the Customizer, or the Studio22 reel shipped with the theme.
if ( $s22_vid_id && wp_get_attachment_url( $s22_vid_id ) ) {
	$s22_sources = array(
		array(
			'src'  => wp_get_attachment_url( $s22_vid_id ),
			'type' => get_post_mime_type( $s22_vid_id ) ? get_post_mime_type( $s22_vid_id ) : 'video/mp4',
		),
	);
} else {
	$s22_sources = array(
		array(
			'src'  => $s22_theme . '/media/hero.mp4',
			'type' => 'video/mp4',
		),
		array(
			'src'  => $s22_theme . '/media/hero.webm',
			'type' => 'video/webm',
		),
	);
	if ( ! $s22_poster ) {
		$s22_poster = $s22_theme . '/img/hero-poster.jpg';
	}
}
$s22_video = ! empty( $s22_sources );
$s22_length = max( 150, min( 600, absint( studio22_opt( 'hero_length' ) ) ) );
$s22_pinned = in_array( $s22_mode, array( 'scrub', 'loop' ), true );
$s22_lines  = array_filter( array( studio22_text( 'hero_line2' ), studio22_text( 'hero_line3' ) ) );
$s22_wa     = studio22_whatsapp_number();

$s22_classes = 'hero hero--' . $s22_mode . ( $s22_pinned ? ' hero--pinned' : '' ) . ( $s22_video ? ' has-video' : '' );
$s22_style   = $s22_pinned ? '--hero-length:' . $s22_length . 'vh;' : '';
?>
<section class="<?php echo esc_attr( $s22_classes ); ?>" data-mode="<?php echo esc_attr( $s22_mode ); ?>" style="<?php echo esc_attr( $s22_style ); ?>" aria-label="<?php esc_attr_e( 'Introduction', 'studio22' ); ?>">
	<div class="hero__sticky">
		<div class="hero__media">
			<?php if ( $s22_video ) : ?>
				<video class="hero__video" muted playsinline preload="auto" <?php echo 'scrub' === $s22_mode ? '' : 'autoplay loop'; ?> <?php echo $s22_poster ? 'poster="' . esc_url( $s22_poster ) . '"' : ''; ?> aria-hidden="true">
					<?php foreach ( $s22_sources as $s22_source ) : ?>
						<source src="<?php echo esc_url( $s22_source['src'] ); ?>" type="<?php echo esc_attr( $s22_source['type'] ); ?>">
					<?php endforeach; ?>
				</video>
			<?php elseif ( $s22_poster ) : ?>
				<img class="hero__image" src="<?php echo esc_url( $s22_poster ); ?>" alt="" fetchpriority="high">
			<?php else : ?>
				<div class="hero__placeholder" aria-hidden="true"></div>
			<?php endif; ?>
		</div>
		<div class="hero__shade" aria-hidden="true"></div>

		<div class="container hero__content">
			<div class="hero__step hero__step--1 is-active" data-step="0">
				<p class="eyebrow"><?php studio22_e( 'hero_eyebrow' ); ?></p>
				<h1 class="hero__title"><?php studio22_e( 'hero_title' ); ?></h1>
				<p class="hero__sub"><?php studio22_e( 'hero_subtitle' ); ?></p>
				<div class="hero__actions">
					<a class="btn btn--accent" href="<?php echo esc_url( studio22_book_url() ); ?>"<?php echo $s22_wa ? ' target="_blank" rel="noopener"' : ''; ?>><?php studio22_e( 'hero_btn1' ); ?> <?php echo studio22_icon( 'arrow' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></a>
					<a class="btn btn--ghost" href="#work"><?php studio22_e( 'hero_btn2' ); ?></a>
				</div>
			</div>
			<?php if ( $s22_pinned ) : ?>
				<?php foreach ( array_values( $s22_lines ) as $s22_i => $s22_line ) : ?>
					<p class="hero__step hero__line" data-step="<?php echo esc_attr( $s22_i + 1 ); ?>"><?php echo esc_html( $s22_line ); ?></p>
				<?php endforeach; ?>
			<?php endif; ?>
		</div>

		<?php if ( $s22_pinned ) : ?>
			<div class="hero__progress" aria-hidden="true"><span></span></div>
		<?php endif; ?>
		<a class="hero__scroll" href="#services" aria-label="<?php esc_attr_e( 'Scroll down', 'studio22' ); ?>"><span><?php esc_html_e( 'Scroll', 'studio22' ); ?></span><i aria-hidden="true"></i></a>
	</div>
</section>
