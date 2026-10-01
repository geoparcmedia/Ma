<?php
$types     = get_the_terms( get_the_ID(), 'tour_type' );
$type_slug = ( $types && ! is_wp_error( $types ) ) ? $types[0]->slug : '';
$style     = a2s_tour_meta( 'a2s_style' );
$duration  = a2s_tour_meta( 'a2s_duration' );
$price     = a2s_tour_meta( 'a2s_price' );
$enquire   = a2s_opt( 'a2s_email' )
	? 'mailto:' . a2s_opt( 'a2s_email' ) . '?subject=' . rawurlencode( 'Booking: ' . get_the_title() )
	: home_url( '/#contact' );
?>
<article class="tour-card reveal" data-type="<?php echo esc_attr( $type_slug ); ?>">
	<a class="tour-media" href="<?php the_permalink(); ?>">
		<img src="<?php echo esc_url( a2s_post_photo( get_the_ID(), $type_slug ) ); ?>" alt="<?php echo esc_attr( get_the_title() ); ?>" loading="lazy">
		<?php if ( $style ) : ?><span class="badge"><?php echo esc_html( $style ); ?> tour</span><?php endif; ?>
	</a>
	<div class="tour-body">
		<?php if ( $duration ) : ?><p class="kicker"><?php echo esc_html( $duration ); ?></p><?php endif; ?>
		<h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
		<p class="tour-excerpt"><?php echo esc_html( get_the_excerpt() ); ?></p>
		<?php if ( $price ) : ?><p class="tour-price">From <?php echo esc_html( $price ); ?> <small>pp</small></p><?php endif; ?>
		<div class="tour-actions">
			<a class="btn" href="<?php echo esc_url( $enquire ); ?>">Book</a>
			<a class="info-link" href="<?php the_permalink(); ?>">Info <span class="circle-arrow">›</span></a>
		</div>
	</div>
</article>
