<?php
/**
 * Single project.
 *
 * @package Studio22
 */

get_header();

while ( have_posts() ) :
	the_post();
	$s22_video  = studio22_video_source( get_post_meta( get_the_ID(), '_s22_video', true ) );
	$s22_client = get_post_meta( get_the_ID(), '_s22_client', true );
	$s22_year   = get_post_meta( get_the_ID(), '_s22_year', true );
	$s22_types  = get_the_term_list( get_the_ID(), 's22_project_type', '', ', ' );
	?>
	<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
		<header class="page-hero page-hero--project">
			<div class="container">
				<p class="kicker"><a href="<?php echo esc_url( get_post_type_archive_link( 's22_project' ) ); ?>"><?php studio22_e( 'work_kicker' ); ?></a></p>
				<h1 class="page-hero__title"><?php the_title(); ?></h1>
				<?php if ( has_excerpt() ) : ?>
					<p class="page-hero__lead"><?php echo esc_html( get_the_excerpt() ); ?></p>
				<?php endif; ?>
				<dl class="project-facts">
					<?php if ( $s22_client ) : ?>
						<div><dt><?php esc_html_e( 'Client', 'studio22' ); ?></dt><dd><?php echo esc_html( $s22_client ); ?></dd></div>
					<?php endif; ?>
					<?php if ( $s22_types && ! is_wp_error( $s22_types ) ) : ?>
						<div><dt><?php esc_html_e( 'Type', 'studio22' ); ?></dt><dd><?php echo wp_kses_post( $s22_types ); ?></dd></div>
					<?php endif; ?>
					<?php if ( $s22_year ) : ?>
						<div><dt><?php esc_html_e( 'Year', 'studio22' ); ?></dt><dd><?php echo esc_html( $s22_year ); ?></dd></div>
					<?php endif; ?>
				</dl>
			</div>
		</header>

		<div class="container project-media">
			<?php if ( $s22_video && 'iframe' === $s22_video['type'] ) : ?>
				<div class="ratio-16x9"><iframe src="<?php echo esc_url( remove_query_arg( 'autoplay', $s22_video['src'] ) ); ?>" title="<?php the_title_attribute(); ?>" allow="fullscreen; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>
			<?php elseif ( $s22_video ) : ?>
				<video src="<?php echo esc_url( $s22_video['src'] ); ?>" controls playsinline preload="metadata" <?php echo has_post_thumbnail() ? 'poster="' . esc_url( get_the_post_thumbnail_url( null, 'full' ) ) . '"' : ''; ?>></video>
			<?php elseif ( has_post_thumbnail() ) : ?>
				<?php the_post_thumbnail( 'full' ); ?>
			<?php endif; ?>
		</div>

		<div class="section section--tight">
			<div class="container container--narrow entry-content">
				<?php the_content(); ?>
			</div>
			<div class="container container--narrow">
				<?php
				the_post_navigation(
					array(
						'prev_text' => '<span class="nav-label">' . esc_html__( 'Previous project', 'studio22' ) . '</span> %title',
						'next_text' => '<span class="nav-label">' . esc_html__( 'Next project', 'studio22' ) . '</span> %title',
					)
				);
				?>
			</div>
		</div>
	</article>
	<?php
endwhile;

get_template_part( 'template-parts/section', 'cta' );
get_footer();
