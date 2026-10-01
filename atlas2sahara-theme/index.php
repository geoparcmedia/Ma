<?php get_header(); ?>
<section class="page-hero media-hiking">
	<div class="hero-overlay"></div>
	<div class="container page-hero-content">
		<h1><?php echo is_singular() ? esc_html( get_the_title() ) : esc_html( wp_strip_all_tags( get_the_archive_title() ) ); ?></h1>
	</div>
</section>
<section class="section">
	<div class="container prose">
		<?php
		if ( have_posts() ) :
			while ( have_posts() ) :
				the_post();
				if ( is_singular() ) {
					the_content();
				} else {
					printf( '<h2><a href="%s">%s</a></h2>', esc_url( get_permalink() ), esc_html( get_the_title() ) );
					the_excerpt();
				}
			endwhile;
			the_posts_pagination();
		else :
			echo '<p>Nothing found.</p>';
		endif;
		?>
	</div>
</section>
<?php
get_footer();
