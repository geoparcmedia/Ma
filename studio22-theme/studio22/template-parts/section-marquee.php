<?php
/**
 * Moving strip of service keywords.
 *
 * @package Studio22
 */

$s22_words = array_filter( array_map( 'trim', preg_split( '/[,،]/u', studio22_text( 'marquee' ) ) ) );
if ( ! $s22_words ) {
	return;
}
?>
<div class="marquee" aria-hidden="true">
	<div class="marquee__track">
		<?php for ( $s22_copy = 0; $s22_copy < 2; $s22_copy++ ) : ?>
			<ul class="marquee__list">
				<?php foreach ( $s22_words as $s22_word ) : ?>
					<li><?php echo esc_html( $s22_word ); ?></li>
				<?php endforeach; ?>
			</ul>
		<?php endfor; ?>
	</div>
</div>
