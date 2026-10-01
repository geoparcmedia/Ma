<?php
/**
 * Not found.
 *
 * @package Studio22
 */

get_header();
?>
<section class="page-hero page-hero--404">
	<div class="container">
		<p class="big-404" aria-hidden="true">404</p>
		<h1 class="page-hero__title"><?php esc_html_e( 'This frame is missing.', 'studio22' ); ?></h1>
		<p class="page-hero__lead"><?php esc_html_e( 'The page you are looking for does not exist or has moved.', 'studio22' ); ?></p>
		<p><a class="btn btn--accent" href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Back to home', 'studio22' ); ?></a></p>
	</div>
</section>
<?php
get_footer();
