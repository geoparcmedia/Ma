<?php
/**
 * How we work, four steps.
 *
 * @package Studio22
 */

?>
<section class="section process" id="process" aria-labelledby="process-title">
	<div class="container">
		<?php studio22_section_heading( 'process_kicker', 'process_title', 'process-title' ); ?>
		<ol class="process__list">
			<?php for ( $s22_i = 1; $s22_i <= 4; $s22_i++ ) : ?>
				<li class="step reveal" style="--delay:<?php echo esc_attr( $s22_i - 1 ); ?>">
					<span class="step__num"><?php echo esc_html( sprintf( '%02d', $s22_i ) ); ?></span>
					<h3 class="step__title"><?php studio22_e( "step{$s22_i}_title" ); ?></h3>
					<p class="step__text"><?php studio22_e( "step{$s22_i}_text" ); ?></p>
				</li>
			<?php endfor; ?>
		</ol>
	</div>
</section>
