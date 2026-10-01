<?php
/**
 * Numbers with count-up animation.
 *
 * @package Studio22
 */

$s22_has_stats = false;
for ( $s22_i = 1; $s22_i <= 4; $s22_i++ ) {
	if ( '' !== trim( (string) studio22_opt( "stat{$s22_i}_number" ) ) ) {
		$s22_has_stats = true;
	}
}
if ( ! $s22_has_stats ) {
	return;
}
?>
<dl class="stats">
	<?php
	for ( $s22_i = 1; $s22_i <= 4; $s22_i++ ) :
		$s22_number = trim( (string) studio22_opt( "stat{$s22_i}_number" ) );
		if ( '' === $s22_number ) {
			continue;
		}
		?>
		<div class="stat reveal" style="--delay:<?php echo esc_attr( $s22_i - 1 ); ?>">
			<dt class="stat__label"><?php studio22_e( "stat{$s22_i}_label" ); ?></dt>
			<dd class="stat__number" data-count="<?php echo esc_attr( preg_replace( '/\D/', '', $s22_number ) ); ?>"><?php echo esc_html( $s22_number ); ?><span>+</span></dd>
		</div>
	<?php endfor; ?>
</dl>
