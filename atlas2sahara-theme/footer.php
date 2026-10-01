</main>
<footer class="site-footer">
	<div class="footer-grid">
		<div class="footer-brand">
			<a class="brand" href="<?php echo esc_url( home_url( '/' ) ); ?>">Atlas<b>2</b>Sahara</a>
			<div class="socials">
				<?php if ( a2s_opt( 'a2s_email' ) ) : ?><a href="mailto:<?php echo esc_attr( a2s_opt( 'a2s_email' ) ); ?>" aria-label="Email"><?php echo a2s_icon( 'mail' ); ?></a><?php endif; ?>
				<?php if ( a2s_opt( 'a2s_phone' ) ) : ?><a href="https://wa.me/<?php echo esc_attr( preg_replace( '/\D/', '', a2s_opt( 'a2s_phone' ) ) ); ?>" aria-label="WhatsApp"><?php echo a2s_icon( 'whatsapp' ); ?></a><?php endif; ?>
				<?php if ( a2s_opt( 'a2s_instagram' ) ) : ?><a href="<?php echo esc_url( a2s_opt( 'a2s_instagram' ) ); ?>" aria-label="Instagram"><?php echo a2s_icon( 'instagram' ); ?></a><?php endif; ?>
				<?php if ( a2s_opt( 'a2s_facebook' ) ) : ?><a href="<?php echo esc_url( a2s_opt( 'a2s_facebook' ) ); ?>" aria-label="Facebook"><?php echo a2s_icon( 'facebook' ); ?></a><?php endif; ?>
			</div>
		</div>
		<div>
			<h4>About:</h4>
			<?php
			wp_nav_menu( array(
				'theme_location' => 'footer',
				'container'      => false,
				'fallback_cb'    => 'a2s_fallback_menu',
			) );
			?>
		</div>
		<?php
		$columns = array(
			'biking' => 'Our bike tours:',
			'desert' => 'Our desert tours:',
			'hiking' => 'Our hiking tours:',
		);
		foreach ( $columns as $slug => $heading ) :
			$col_tours = get_posts( array(
				'post_type'   => 'tour',
				'numberposts' => 10,
				'orderby'     => 'menu_order',
				'order'       => 'ASC',
				'tax_query'   => array( array( 'taxonomy' => 'tour_type', 'field' => 'slug', 'terms' => $slug ) ),
			) );
			if ( ! $col_tours ) {
				continue;
			}
			?>
			<div>
				<h4><?php echo esc_html( $heading ); ?></h4>
				<ul>
					<?php foreach ( $col_tours as $t ) : ?>
						<li><a href="<?php echo esc_url( get_permalink( $t ) ); ?>"><?php echo esc_html( get_the_title( $t ) ); ?></a></li>
					<?php endforeach; ?>
				</ul>
			</div>
		<?php endforeach; ?>
		<div>
			<h4>Contact:</h4>
			<ul>
				<?php if ( a2s_opt( 'a2s_email' ) ) : ?><li>E-mail: <a href="mailto:<?php echo esc_attr( a2s_opt( 'a2s_email' ) ); ?>"><?php echo esc_html( a2s_opt( 'a2s_email' ) ); ?></a></li><?php endif; ?>
				<?php if ( a2s_opt( 'a2s_phone' ) ) : ?><li>Phone: <?php echo esc_html( a2s_opt( 'a2s_phone' ) ); ?></li><?php endif; ?>
				<li><?php echo esc_html( a2s_opt( 'a2s_address' ) ); ?></li>
			</ul>
		</div>
	</div>
	<div class="footer-bottom">
		<p>Atlas2Sahara &copy; <?php echo esc_html( gmdate( 'Y' ) ); ?></p>
	</div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
