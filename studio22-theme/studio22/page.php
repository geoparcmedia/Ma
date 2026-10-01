<?php
/**
 * Page.
 *
 * @package Studio22
 */

get_header();

while ( have_posts() ) :
	the_post();
	?>
	<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
		<header class="page-hero">
			<div class="container">
				<h1 class="page-hero__title"><?php the_title(); ?></h1>
			</div>
		</header>
		<?php if ( has_post_thumbnail() ) : ?>
			<figure class="container featured-image"><?php the_post_thumbnail( 'studio22-wide' ); ?></figure>
		<?php endif; ?>
		<div class="section section--tight">
			<div class="container container--narrow entry-content">
				<?php
				the_content();
				wp_link_pages();
				?>
			</div>
			<?php if ( comments_open() || get_comments_number() ) : ?>
				<div class="container container--narrow"><?php comments_template(); ?></div>
			<?php endif; ?>
		</div>
	</article>
	<?php
endwhile;

get_footer();
