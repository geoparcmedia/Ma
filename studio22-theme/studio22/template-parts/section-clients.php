<?php
/**
 * Client logos.
 *
 * @package Studio22
 */

$s22_clients = array();
for ( $s22_i = 1; $s22_i <= STUDIO22_CLIENTS; $s22_i++ ) {
	$s22_name = studio22_text( "client{$s22_i}_name" );
	$s22_logo = absint( studio22_opt( "client{$s22_i}_logo" ) );
	if ( '' === $s22_name && ! $s22_logo ) {
		continue;
	}
	$s22_clients[] = array(
		'name' => $s22_name,
		'logo' => $s22_logo,
		'url'  => studio22_opt( "client{$s22_i}_url" ),
	);
}
if ( ! $s22_clients ) {
	return;
}
?>
<section class="section clients<?php echo studio22_opt( 'clients_color' ) ? ' clients--color' : ''; ?>" id="clients" aria-labelledby="clients-title">
	<div class="container">
		<?php studio22_section_heading( 'clients_kicker', 'clients_title', 'clients-title' ); ?>
		<ul class="clients__grid">
			<?php foreach ( $s22_clients as $s22_n => $s22_client ) : ?>
				<li class="client reveal" style="--delay:<?php echo esc_attr( $s22_n % 6 ); ?>">
					<?php
					$s22_inner = $s22_client['logo']
						? wp_get_attachment_image(
							$s22_client['logo'],
							'medium',
							false,
							array(
								'class'   => 'client__logo',
								'alt'     => $s22_client['name'],
								'loading' => 'lazy',
							)
						)
						: '<span class="client__name">' . esc_html( $s22_client['name'] ) . '</span>';
					if ( $s22_client['url'] ) {
						echo '<a href="' . esc_url( $s22_client['url'] ) . '" target="_blank" rel="noopener" title="' . esc_attr( $s22_client['name'] ) . '">' . $s22_inner . '</a>'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
					} else {
						echo '<div title="' . esc_attr( $s22_client['name'] ) . '">' . $s22_inner . '</div>'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
					}
					?>
				</li>
			<?php endforeach; ?>
		</ul>
	</div>
</section>
