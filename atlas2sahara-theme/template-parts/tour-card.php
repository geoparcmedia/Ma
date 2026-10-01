<?php
$types     = get_the_terms( get_the_ID(), 'tour_type' );
$type_slug = ( $types && ! is_wp_error( $types ) ) ? $types[0]->slug : 'biking';
$type_name = ( $types && ! is_wp_error( $types ) ) ? $types[0]->name : '';
?>
<article class="tour-card reveal" data-type="<?php echo esc_attr( $type_slug ); ?>">
	<a class="tour-media media-<?php echo esc_attr( $type_slug ); ?>" href="<?php the_permalink(); ?>">
		<?php if ( has_post_thumbnail() ) : ?>
			<?php the_post_thumbnail( 'a2s-card', array( 'loading' => 'lazy' ) ); ?>
		<?php else : ?>
			<span class="media-fallback"><?php echo a2s_icon( 'desert' === $type_slug ? 'desert' : ( 'hiking' === $type_slug ? 'hike' : 'bike' ) ); ?></span>
		<?php endif; ?>
		<?php if ( $type_name ) : ?><span class="tag"><?php echo esc_html( $type_name ); ?></span><?php endif; ?>
		<?php if ( a2s_tour_meta( 'a2s_style' ) ) : ?><span class="tag tag-light"><?php echo esc_html( a2s_tour_meta( 'a2s_style' ) ); ?></span><?php endif; ?>
	</a>
	<div class="tour-body">
		<?php if ( a2s_tour_meta( 'a2s_region' ) ) : ?><p class="eyebrow"><?php echo esc_html( a2s_tour_meta( 'a2s_region' ) ); ?></p><?php endif; ?>
		<h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
		<p class="muted"><?php echo esc_html( get_the_excerpt() ); ?></p>
		<ul class="tour-facts">
			<?php if ( a2s_tour_meta( 'a2s_duration' ) ) : ?><li><?php echo a2s_icon( 'clock' ); ?><?php echo esc_html( a2s_tour_meta( 'a2s_duration' ) ); ?></li><?php endif; ?>
			<?php if ( a2s_tour_meta( 'a2s_difficulty' ) ) : ?><li><?php echo a2s_icon( 'gauge' ); ?><?php echo esc_html( a2s_tour_meta( 'a2s_difficulty' ) ); ?></li><?php endif; ?>
		</ul>
		<div class="tour-foot">
			<?php if ( a2s_tour_meta( 'a2s_price' ) ) : ?><span class="price"><small>from</small> <?php echo esc_html( a2s_tour_meta( 'a2s_price' ) ); ?></span><?php endif; ?>
			<a class="link-arrow" href="<?php the_permalink(); ?>">View tour <?php echo a2s_icon( 'arrow' ); ?></a>
		</div>
	</div>
</article>
