<?php
/**
 * Template Name: About Studio22
 *
 * About page: page title, founder photo and story, the page content,
 * numbers, clients and a call to action.
 *
 * @package Studio22
 */

get_header();

$s22_photo = studio22_image_url( 'founder_photo', 'large' );
if ( ! $s22_photo && has_post_thumbnail() ) {
	$s22_photo = get_the_post_thumbnail_url( null, 'large' );
}
if ( ! $s22_photo ) {
	$s22_photo = studio22_theme_image( 'founder.jpg' );
}
$s22_quote = studio22_text( 'founder_quote' );
$s22_name = studio22_text( 'founder_name' );

while ( have_posts() ) :
	the_post();
	?>
	<header class="page-hero page-hero--about">
		<div class="container">
			<p class="kicker"><?php studio22_e( 'studio_kicker' ); ?></p>
			<h1 class="page-hero__title"><?php the_title(); ?></h1>
			<p class="page-hero__lead"><?php studio22_e( 'studio_title' ); ?></p>
		</div>
	</header>

	<section class="section founder" aria-labelledby="founder-title">
		<div class="container founder__grid">
			<figure class="founder__photo reveal">
				<?php if ( $s22_photo ) : ?>
					<img src="<?php echo esc_url( $s22_photo ); ?>" alt="<?php echo esc_attr( $s22_name ? $s22_name : studio22_text( 'founder_role' ) ); ?>">
				<?php else : ?>
					<div class="founder__placeholder">
						<?php echo studio22_icon( 'camera' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
						<?php if ( current_user_can( 'edit_theme_options' ) ) : ?>
							<a href="<?php echo esc_url( admin_url( 'customize.php?autofocus[section]=studio22_founder' ) ); ?>"><?php esc_html_e( 'Add the founder photo', 'studio22' ); ?></a>
						<?php endif; ?>
					</div>
				<?php endif; ?>
				<span class="founder__frame" aria-hidden="true"></span>
			</figure>
			<div class="founder__body">
				<p class="kicker reveal"><?php studio22_e( 'founder_kicker' ); ?></p>
				<h2 class="section-title reveal" id="founder-title"><?php echo esc_html( $s22_name ? $s22_name : studio22_text( 'founder_role' ) ); ?></h2>
				<?php if ( $s22_name ) : ?>
					<p class="founder__role reveal"><?php studio22_e( 'founder_role' ); ?></p>
				<?php endif; ?>
				<?php if ( $s22_quote ) : ?>
					<blockquote class="founder__quote reveal"><p><?php echo esc_html( $s22_quote ); ?></p></blockquote>
				<?php endif; ?>
				<div class="founder__bio lead reveal"><?php echo wp_kses_post( wpautop( esc_html( studio22_text( 'founder_bio' ) ) ) ); ?></div>
			</div>
		</div>
	</section>

	<?php if ( '' !== trim( get_the_content() ) ) : ?>
		<section class="section section--tight">
			<div class="container container--narrow entry-content">
				<?php the_content(); ?>
			</div>
		</section>
	<?php else : ?>
		<section class="section section--tight">
			<div class="container container--narrow">
				<p class="lead reveal"><?php studio22_e( 'studio_text' ); ?></p>
			</div>
		</section>
	<?php endif; ?>

	<section class="section section--tight">
		<div class="container">
			<?php get_template_part( 'template-parts/stats' ); ?>
		</div>
	</section>
	<?php
endwhile;

if ( studio22_opt( 'show_clients' ) ) {
	get_template_part( 'template-parts/section', 'clients' );
}
get_template_part( 'template-parts/section', 'cta' );

get_footer();
