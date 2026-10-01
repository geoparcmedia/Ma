<?php
/**
 * Contact details, booking form and map.
 *
 * @package Studio22
 */

$s22_email     = studio22_opt( 'email' );
$s22_phone     = studio22_opt( 'phone' );
$s22_wa_number = studio22_whatsapp_number();
$s22_shortcode = trim( (string) studio22_opt( 'form_shortcode' ) );
$s22_map       = trim( (string) studio22_opt( 'map' ) );
?>
<section class="section contact" id="contact" aria-labelledby="contact-title">
	<div class="container contact__grid">
		<div class="contact__info">
			<?php studio22_section_heading( 'contact_kicker', 'contact_title', 'contact-title' ); ?>
			<ul class="contact-list contact-list--big reveal">
				<li><?php echo studio22_icon( 'pin' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?><span><?php studio22_e( 'address' ); ?></span></li>
				<?php if ( $s22_wa_number ) : ?>
					<li><?php echo studio22_icon( 'whatsapp' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?><a href="<?php echo esc_url( studio22_whatsapp_url( studio22_text( 'wa_message' ) ) ); ?>" target="_blank" rel="noopener" dir="ltr">+<?php echo esc_html( $s22_wa_number ); ?></a></li>
				<?php endif; ?>
				<?php if ( $s22_phone ) : ?>
					<li><?php echo studio22_icon( 'phone' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?><a href="tel:<?php echo esc_attr( preg_replace( '/[^\d+]/', '', $s22_phone ) ); ?>" dir="ltr"><?php echo esc_html( $s22_phone ); ?></a></li>
				<?php endif; ?>
				<?php if ( $s22_email ) : ?>
					<li><?php echo studio22_icon( 'mail' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?><a href="mailto:<?php echo esc_attr( antispambot( $s22_email ) ); ?>"><?php echo esc_html( antispambot( $s22_email ) ); ?></a></li>
				<?php endif; ?>
				<li><?php echo studio22_icon( 'clock' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?><span><?php studio22_e( 'hours' ); ?></span></li>
			</ul>
			<?php if ( $s22_map ) : ?>
				<div class="contact__map reveal">
					<iframe title="<?php esc_attr_e( 'Map', 'studio22' ); ?>" src="<?php echo esc_url( 'https://www.google.com/maps?q=' . rawurlencode( $s22_map ) . '&output=embed' . ( studio22_is_arabic() ? '&hl=ar' : '' ) ); ?>" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
				</div>
			<?php endif; ?>
		</div>

		<div class="contact__form reveal">
			<?php if ( $s22_shortcode ) : ?>
				<?php echo do_shortcode( $s22_shortcode ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
			<?php else : ?>
				<form class="booking-form" data-wa-form <?php echo $s22_wa_number ? '' : 'data-email="' . esc_attr( antispambot( $s22_email ) ) . '"'; ?>>
					<h3 class="booking-form__title"><?php esc_html_e( 'Book a session', 'studio22' ); ?></h3>
					<p class="field">
						<label for="bf-name"><?php esc_html_e( 'Name', 'studio22' ); ?></label>
						<input id="bf-name" name="name" type="text" autocomplete="name" required>
					</p>
					<p class="field">
						<label for="bf-service"><?php esc_html_e( 'Service', 'studio22' ); ?></label>
						<select id="bf-service" name="service">
							<?php
							for ( $s22_i = 1; $s22_i <= 6; $s22_i++ ) {
								$s22_title = studio22_text( "service{$s22_i}_title" );
								if ( $s22_title ) {
									echo '<option>' . esc_html( $s22_title ) . '</option>';
								}
							}
							?>
							<option><?php esc_html_e( 'Other', 'studio22' ); ?></option>
						</select>
					</p>
					<p class="field">
						<label for="bf-date"><?php esc_html_e( 'Date', 'studio22' ); ?></label>
						<input id="bf-date" name="date" type="date">
					</p>
					<p class="field">
						<label for="bf-message"><?php esc_html_e( 'Tell us about your project', 'studio22' ); ?></label>
						<textarea id="bf-message" name="message" rows="4" required></textarea>
					</p>
					<button class="btn btn--accent btn--block" type="submit">
						<?php echo studio22_icon( $s22_wa_number ? 'whatsapp' : 'mail' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
						<?php echo $s22_wa_number ? esc_html__( 'Send on WhatsApp', 'studio22' ) : esc_html__( 'Send by email', 'studio22' ); ?>
					</button>
				</form>
			<?php endif; ?>
		</div>
	</div>
</section>
