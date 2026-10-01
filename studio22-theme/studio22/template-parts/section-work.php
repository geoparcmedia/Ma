<?php
/**
 * Portfolio grid with filters and lightbox.
 *
 * @package Studio22
 */

$s22_projects = new WP_Query(
	array(
		'post_type'           => 's22_project',
		'posts_per_page'      => max( 3, absint( studio22_opt( 'work_count' ) ) ),
		'orderby'             => array(
			'menu_order' => 'ASC',
			'date'       => 'DESC',
		),
		'ignore_sticky_posts' => true,
	)
);
?>
<section class="section work" id="work" aria-labelledby="work-title">
	<div class="container">
		<div class="work__head">
			<?php studio22_section_heading( 'work_kicker', 'work_title', 'work-title' ); ?>
			<?php studio22_project_filters(); ?>
		</div>

		<?php if ( $s22_projects->have_posts() ) : ?>
			<div class="work__grid">
				<?php
				while ( $s22_projects->have_posts() ) :
					$s22_projects->the_post();
					studio22_project_card();
				endwhile;
				wp_reset_postdata();
				?>
			</div>
		<?php else : ?>
			<?php get_template_part( 'template-parts/work-gallery' ); ?>
			<?php if ( current_user_can( 'edit_posts' ) ) : ?>
				<p class="notice-empty">
					<?php esc_html_e( 'These are sample photos shipped with the theme. Add your own work from Dashboard → Projects → Add new (title, featured image and an optional video link).', 'studio22' ); ?>
					<a href="<?php echo esc_url( admin_url( 'post-new.php?post_type=s22_project' ) ); ?>"><?php esc_html_e( 'Add a project', 'studio22' ); ?></a>
				</p>
			<?php endif; ?>
		<?php endif; ?>

		<?php
		$s22_feed = trim( (string) studio22_opt( 'instagram_feed' ) );
		if ( $s22_feed ) :
			?>
			<div class="work__instagram reveal"><?php echo do_shortcode( $s22_feed ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></div>
		<?php endif; ?>

		<p class="work__more reveal">
			<?php if ( $s22_projects->have_posts() ) : ?>
				<a class="btn btn--ghost" href="<?php echo esc_url( get_post_type_archive_link( 's22_project' ) ); ?>"><?php studio22_e( 'work_all' ); ?> <?php echo studio22_icon( 'arrow' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></a>
			<?php endif; ?>
			<?php if ( studio22_opt( 'social_instagram' ) ) : ?>
				<a class="btn btn--accent" href="<?php echo esc_url( studio22_opt( 'social_instagram' ) ); ?>" target="_blank" rel="noopener"><?php echo studio22_icon( 'instagram' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?> <?php esc_html_e( 'More on Instagram', 'studio22' ); ?></a>
			<?php endif; ?>
		</p>
	</div>
</section>
