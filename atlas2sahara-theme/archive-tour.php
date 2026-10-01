<?php get_header(); ?>
<section class="page-hero" style="background-image:url(<?php echo esc_url( a2s_img( 'camels.jpg' ) ); ?>)">
	<div class="container page-hero-content">
		<p class="kicker">Morocco adventure tours</p>
		<h1><?php echo is_tax() ? esc_html( single_term_title( '', false ) . ' tours' ) : 'All tours'; ?></h1>
		<?php if ( is_tax() && term_description() ) : ?><div class="lead"><?php echo wp_kses_post( term_description() ); ?></div><?php endif; ?>
	</div>
</section>
<section class="section">
	<div class="container">
		<div class="tour-grid">
			<?php
			if ( have_posts() ) :
				while ( have_posts() ) :
					the_post();
					get_template_part( 'template-parts/tour-card' );
				endwhile;
			else :
				echo '<p>No tours found.</p>';
			endif;
			?>
		</div>
		<?php the_posts_pagination(); ?>
	</div>
</section>
<?php
get_footer();
