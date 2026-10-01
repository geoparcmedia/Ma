<?php
/**
 * Home page: pinned video hero followed by the studio sections.
 * When the front page shows the latest posts, WordPress uses home.php / index.php instead.
 *
 * @package Studio22
 */

if ( 'posts' === get_option( 'show_on_front' ) ) {
	get_template_part( 'index' );
	return;
}

get_header();

get_template_part( 'template-parts/section', 'hero' );

$studio22_sections = array( 'marquee', 'services', 'work', 'studio', 'clients', 'process', 'cta', 'contact' );
foreach ( $studio22_sections as $studio22_section ) {
	if ( studio22_opt( 'show_' . $studio22_section ) ) {
		get_template_part( 'template-parts/section', $studio22_section );
	}
}

// Anything written in the home page editor is shown after the sections.
while ( have_posts() ) :
	the_post();
	if ( '' !== trim( get_the_content() ) ) :
		?>
		<section class="section">
			<div class="container entry-content">
				<?php the_content(); ?>
			</div>
		</section>
		<?php
	endif;
endwhile;

get_footer();
