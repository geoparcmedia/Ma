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
			<p class="work__more reveal">
				<a class="btn btn--ghost" href="<?php echo esc_url( get_post_type_archive_link( 's22_project' ) ); ?>"><?php studio22_e( 'work_all' ); ?> <?php echo studio22_icon( 'arrow' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></a>
			</p>
		<?php elseif ( current_user_can( 'edit_posts' ) ) : ?>
			<p class="notice-empty">
				<?php esc_html_e( 'No projects yet. Add your work from Dashboard → Projects → Add new (title, featured image and an optional video link).', 'studio22' ); ?>
				<a href="<?php echo esc_url( admin_url( 'post-new.php?post_type=s22_project' ) ); ?>"><?php esc_html_e( 'Add a project', 'studio22' ); ?></a>
			</p>
		<?php endif; ?>
	</div>
</section>
