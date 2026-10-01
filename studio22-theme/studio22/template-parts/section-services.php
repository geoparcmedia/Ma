<?php
/**
 * Services.
 *
 * @package Studio22
 */

?>
<section class="section services" id="services" aria-labelledby="services-title">
	<div class="container">
		<?php studio22_section_heading( 'services_kicker', 'services_title', 'services-title' ); ?>
		<div class="services__grid">
			<?php
			for ( $s22_i = 1; $s22_i <= 6; $s22_i++ ) :
				$s22_title = studio22_text( "service{$s22_i}_title" );
				if ( ! $s22_title ) {
					continue;
				}
				?>
				<article class="service reveal" style="--delay:<?php echo esc_attr( ( $s22_i - 1 ) % 3 ); ?>">
					<span class="service__num"><?php echo esc_html( sprintf( '%02d', $s22_i ) ); ?></span>
					<span class="service__icon"><?php echo studio22_icon( studio22_opt( "service{$s22_i}_icon" ) ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
					<h3 class="service__title"><?php echo esc_html( $s22_title ); ?></h3>
					<p class="service__text"><?php studio22_e( "service{$s22_i}_text" ); ?></p>
				</article>
			<?php endfor; ?>
		</div>
	</div>
</section>
