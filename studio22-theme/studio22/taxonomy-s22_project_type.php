<?php
/**
 * Project type pages, same layout as the projects archive.
 *
 * @package Studio22
 */

get_header();
?>
<header class="page-hero">
	<div class="container">
		<p class="kicker"><?php studio22_e( 'work_kicker' ); ?></p>
		<h1 class="page-hero__title">
			<?php
			if ( is_tax() ) {
				single_term_title();
			} else {
				studio22_e( 'work_title' );
			}
			?>
		</h1>
	</div>
</header>

<section class="section section--tight work">
	<div class="container">
		<?php
		if ( ! is_tax() ) {
			studio22_project_filters();
		}
		?>
		<?php if ( have_posts() ) : ?>
			<div class="work__grid">
				<?php
				while ( have_posts() ) :
					the_post();
					studio22_project_card();
				endwhile;
				?>
			</div>
			<?php studio22_pagination(); ?>
		<?php else : ?>
			<p class="empty-state"><?php esc_html_e( 'No projects yet.', 'studio22' ); ?></p>
		<?php endif; ?>
	</div>
</section>
<?php
get_template_part( 'template-parts/section', 'cta' );
get_footer();
