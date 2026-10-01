<?php
/**
 * Call-to-action banner.
 *
 * @package Studio22
 */

$s22_wa = studio22_whatsapp_url( studio22_text( 'wa_message' ) );
?>
<section class="cta" aria-labelledby="cta-title">
	<div class="container cta__inner reveal">
		<div>
			<h2 class="cta__title" id="cta-title"><?php studio22_e( 'cta_title' ); ?></h2>
			<p class="cta__text"><?php studio22_e( 'cta_text' ); ?></p>
		</div>
		<a class="btn btn--light" href="<?php echo esc_url( $s22_wa ? $s22_wa : '#contact' ); ?>"<?php echo $s22_wa ? ' target="_blank" rel="noopener"' : ''; ?>>
			<?php echo studio22_icon( $s22_wa ? 'whatsapp' : 'mail' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
			<?php studio22_e( 'cta_btn' ); ?>
		</a>
	</div>
</section>
