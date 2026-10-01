<?php
/**
 * Blog index and fallback template.
 *
 * @package Studio22
 */

get_header();
?>
<header class="page-hero">
	<div class="container">
		<?php if ( is_home() && ! is_front_page() ) : ?>
			<h1 class="page-hero__title"><?php single_post_title(); ?></h1>
		<?php elseif ( is_search() ) : ?>
			<p class="kicker"><?php esc_html_e( 'Search', 'studio22' ); ?></p>
			<h1 class="page-hero__title"><?php echo esc_html( get_search_query() ); ?></h1>
		<?php elseif ( is_archive() ) : ?>
			<?php the_archive_title( '<h1 class="page-hero__title">', '</h1>' ); ?>
			<?php the_archive_description( '<div class="page-hero__lead">', '</div>' ); ?>
		<?php else : ?>
			<h1 class="page-hero__title"><?php esc_html_e( 'Journal', 'studio22' ); ?></h1>
		<?php endif; ?>
	</div>
</header>

<section class="section section--tight">
	<div class="container">
		<?php if ( have_posts() ) : ?>
			<div class="post-grid">
				<?php
				while ( have_posts() ) :
					the_post();
					get_template_part( 'template-parts/content', 'card' );
				endwhile;
				?>
			</div>
			<?php studio22_pagination(); ?>
		<?php else : ?>
			<div class="empty-state">
				<p><?php esc_html_e( 'Nothing found here yet.', 'studio22' ); ?></p>
				<?php get_search_form(); ?>
			</div>
		<?php endif; ?>
	</div>
</section>
<?php
get_footer();
