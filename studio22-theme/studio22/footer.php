<?php
/**
 * Footer.
 *
 * @package Studio22
 */

$s22_email = studio22_opt( 'email' );
$s22_phone = studio22_opt( 'phone' );
$s22_wa    = studio22_whatsapp_url( studio22_text( 'wa_message' ) );
?>
</main>

<footer class="site-footer">
	<div class="container site-footer__grid">
		<div class="site-footer__brand">
			<?php studio22_logo( 'site-logo--footer' ); ?>
			<p><?php studio22_e( 'footer_text' ); ?></p>
			<?php studio22_social_links(); ?>
		</div>

		<div class="site-footer__col">
			<h2 class="site-footer__title"><?php esc_html_e( 'Explore', 'studio22' ); ?></h2>
			<?php
			wp_nav_menu(
				array(
					'theme_location' => has_nav_menu( 'footer' ) ? 'footer' : 'primary',
					'container'      => false,
					'depth'          => 1,
					'fallback_cb'    => 'studio22_menu_fallback',
				)
			);
			?>
		</div>

		<div class="site-footer__col">
			<h2 class="site-footer__title"><?php esc_html_e( 'Contact', 'studio22' ); ?></h2>
			<ul class="contact-list">
				<li><?php echo studio22_icon( 'pin' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?><span><?php studio22_e( 'address' ); ?></span></li>
				<?php if ( $s22_phone ) : ?>
					<li><?php echo studio22_icon( 'phone' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?><a href="tel:<?php echo esc_attr( preg_replace( '/[^\d+]/', '', $s22_phone ) ); ?>" dir="ltr"><?php echo esc_html( $s22_phone ); ?></a></li>
				<?php endif; ?>
				<?php if ( $s22_email ) : ?>
					<li><?php echo studio22_icon( 'mail' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?><a href="mailto:<?php echo esc_attr( antispambot( $s22_email ) ); ?>"><?php echo esc_html( antispambot( $s22_email ) ); ?></a></li>
				<?php endif; ?>
				<?php if ( studio22_text( 'hours' ) ) : ?>
					<li><?php echo studio22_icon( 'clock' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?><span><?php studio22_e( 'hours' ); ?></span></li>
				<?php endif; ?>
			</ul>
		</div>

		<?php if ( is_active_sidebar( 'footer-1' ) ) : ?>
			<div class="site-footer__col">
				<?php dynamic_sidebar( 'footer-1' ); ?>
			</div>
		<?php endif; ?>
	</div>

	<div class="container site-footer__bottom">
		<p>&copy; <?php echo esc_html( wp_date( 'Y' ) ); ?> <?php bloginfo( 'name' ); ?>. <?php esc_html_e( 'All rights reserved.', 'studio22' ); ?></p>
		<a href="#content" class="to-top"><?php esc_html_e( 'Back to top', 'studio22' ); ?> ↑</a>
	</div>
</footer>

<?php if ( $s22_wa && studio22_opt( 'show_wa_float' ) ) : ?>
	<a class="wa-float" href="<?php echo esc_url( $s22_wa ); ?>" target="_blank" rel="noopener" aria-label="<?php esc_attr_e( 'Chat on WhatsApp', 'studio22' ); ?>">
		<?php echo studio22_icon( 'whatsapp' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
	</a>
<?php endif; ?>

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="<?php esc_attr_e( 'Media viewer', 'studio22' ); ?>" hidden>
	<button type="button" class="lightbox__close" aria-label="<?php esc_attr_e( 'Close', 'studio22' ); ?>"><?php echo studio22_icon( 'close' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></button>
	<div class="lightbox__stage"></div>
</div>

<?php wp_footer(); ?>
</body>
</html>
