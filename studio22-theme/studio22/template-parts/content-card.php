<?php
/**
 * Post card for the blog, archives and search.
 *
 * @package Studio22
 */

?>
<article id="post-<?php the_ID(); ?>" <?php post_class( 'post-card reveal' ); ?>>
	<a class="post-card__media" href="<?php the_permalink(); ?>" tabindex="-1" aria-hidden="true">
		<?php
		if ( has_post_thumbnail() ) {
			the_post_thumbnail( 'studio22-wide', array( 'loading' => 'lazy' ) );
		} else {
			echo '<span class="post-card__placeholder">' . studio22_icon( 'camera' ) . '</span>'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
		}
		?>
	</a>
	<div class="post-card__body">
		<?php studio22_post_meta(); ?>
		<h2 class="post-card__title"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
		<div class="post-card__excerpt"><?php the_excerpt(); ?></div>
	</div>
</article>
