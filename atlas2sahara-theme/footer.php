</main>
<footer class="site-footer">
	<div class="container footer-grid">
		<div>
			<a class="brand" href="<?php echo esc_url( home_url( '/' ) ); ?>">Atlas<span>2</span>Sahara</a>
			<p class="muted">Biking, hiking and desert adventures across Morocco, from the peaks of the High Atlas to the dunes of the Sahara.</p>
		</div>
		<div>
			<h4>Tours</h4>
			<ul>
				<?php
				$types = get_terms( array( 'taxonomy' => 'tour_type', 'hide_empty' => false ) );
				if ( ! is_wp_error( $types ) ) {
					foreach ( $types as $type ) {
						printf( '<li><a href="%s">%s tours</a></li>', esc_url( get_term_link( $type ) ), esc_html( $type->name ) );
					}
				}
				?>
				<li><a href="<?php echo esc_url( get_post_type_archive_link( 'tour' ) ); ?>">All tours</a></li>
			</ul>
		</div>
		<div>
			<h4>Explore</h4>
			<?php
			wp_nav_menu( array(
				'theme_location' => 'footer',
				'container'      => false,
				'fallback_cb'    => 'a2s_fallback_menu',
			) );
			?>
		</div>
		<div>
			<h4>Contact</h4>
			<ul class="contact-list">
				<?php if ( a2s_opt( 'a2s_email' ) ) : ?>
					<li><?php echo a2s_icon( 'mail' ); ?><a href="mailto:<?php echo esc_attr( a2s_opt( 'a2s_email' ) ); ?>"><?php echo esc_html( a2s_opt( 'a2s_email' ) ); ?></a></li>
				<?php endif; ?>
				<?php if ( a2s_opt( 'a2s_phone' ) ) : ?>
					<li><?php echo a2s_icon( 'phone' ); ?><?php echo esc_html( a2s_opt( 'a2s_phone' ) ); ?></li>
				<?php endif; ?>
				<li><?php echo a2s_icon( 'pin' ); ?><?php echo esc_html( a2s_opt( 'a2s_address' ) ); ?></li>
			</ul>
		</div>
	</div>
	<div class="container footer-bottom">
		<span>&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> Atlas2Sahara. All rights reserved.</span>
		<a href="#top">Back to top ↑</a>
	</div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
