<?php
get_header();
while ( have_posts() ) :
	the_post();
	$types      = get_the_terms( get_the_ID(), 'tour_type' );
	$type_slug  = ( $types && ! is_wp_error( $types ) ) ? $types[0]->slug : 'biking';
	$highlights = array_filter( array_map( 'trim', explode( "\n", (string) a2s_tour_meta( 'a2s_highlights' ) ) ) );
	$thumb      = get_the_post_thumbnail_url( null, 'full' );
	?>
	<section class="page-hero media-<?php echo esc_attr( $type_slug ); ?>"<?php echo $thumb ? ' style="background-image:url(' . esc_url( $thumb ) . ')"' : ''; ?>>
		<div class="hero-overlay"></div>
		<div class="container page-hero-content">
			<?php if ( a2s_tour_meta( 'a2s_region' ) ) : ?><p class="eyebrow light"><?php echo esc_html( a2s_tour_meta( 'a2s_region' ) ); ?></p><?php endif; ?>
			<h1><?php the_title(); ?></h1>
			<?php if ( has_excerpt() ) : ?><p class="lead"><?php echo esc_html( get_the_excerpt() ); ?></p><?php endif; ?>
		</div>
	</section>
	<section class="section">
		<div class="container tour-layout">
			<article class="prose">
				<?php the_content(); ?>
				<?php if ( $highlights ) : ?>
					<h2>Highlights</h2>
					<ul class="checklist">
						<?php foreach ( $highlights as $h ) : ?><li><?php echo esc_html( $h ); ?></li><?php endforeach; ?>
					</ul>
				<?php endif; ?>
			</article>
			<aside class="tour-box">
				<?php if ( a2s_tour_meta( 'a2s_price' ) ) : ?><p class="price big"><small>from</small> <?php echo esc_html( a2s_tour_meta( 'a2s_price' ) ); ?></p><?php endif; ?>
				<dl>
					<?php
					$facts = array( 'a2s_duration' => 'Duration', 'a2s_difficulty' => 'Difficulty', 'a2s_style' => 'Style', 'a2s_region' => 'Region' );
					foreach ( $facts as $key => $label ) {
						if ( a2s_tour_meta( $key ) ) {
							printf( '<div><dt>%s</dt><dd>%s</dd></div>', esc_html( $label ), esc_html( a2s_tour_meta( $key ) ) );
						}
					}
					?>
				</dl>
				<?php if ( a2s_opt( 'a2s_email' ) ) : ?>
					<a class="btn btn-block" href="mailto:<?php echo esc_attr( a2s_opt( 'a2s_email' ) ); ?>?subject=<?php echo rawurlencode( 'Enquiry: ' . get_the_title() ); ?>">Enquire about this tour</a>
				<?php else : ?>
					<a class="btn btn-block" href="<?php echo esc_url( home_url( '/#contact' ) ); ?>">Enquire about this tour</a>
				<?php endif; ?>
			</aside>
		</div>
	</section>
	<?php
endwhile;
get_footer();
