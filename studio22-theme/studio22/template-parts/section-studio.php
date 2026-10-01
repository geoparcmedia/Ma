<?php
/**
 * Studio introduction with numbers.
 *
 * @package Studio22
 */

$s22_image = studio22_image_url( 'studio_image', 'large' );
if ( ! $s22_image ) {
	$s22_image = studio22_theme_image( 'work-show.jpg' );
}
$s22_about = studio22_about_page_id() ? array( get_post( studio22_about_page_id() ) ) : array();
?>
<section class="section studio" id="studio" aria-labelledby="studio-title">
	<div class="container studio__grid">
		<div class="studio__media reveal">
			<?php if ( $s22_image ) : ?>
				<img src="<?php echo esc_url( $s22_image ); ?>" alt="" loading="lazy">
			<?php else : ?>
				<div class="studio__placeholder"><?php echo studio22_icon( 'camera' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></div>
			<?php endif; ?>
			<span class="studio__badge" aria-hidden="true">22</span>
		</div>
		<div class="studio__body">
			<?php studio22_section_heading( 'studio_kicker', 'studio_title', 'studio-title' ); ?>
			<p class="lead reveal"><?php studio22_e( 'studio_text' ); ?></p>
			<?php if ( $s22_about ) : ?>
				<p class="reveal"><a class="link-arrow" href="<?php echo esc_url( get_permalink( $s22_about[0] ) ); ?>"><?php studio22_e( 'studio_more' ); ?> <?php echo studio22_icon( 'arrow' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></a></p>
			<?php endif; ?>
			<?php get_template_part( 'template-parts/stats' ); ?>
		</div>
	</div>
</section>
