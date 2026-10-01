<?php
/**
 * Search form.
 *
 * @package Studio22
 */

$s22_id = wp_unique_id( 'search-' );
?>
<form role="search" method="get" class="search-form" action="<?php echo esc_url( home_url( '/' ) ); ?>">
	<label class="screen-reader-text" for="<?php echo esc_attr( $s22_id ); ?>"><?php esc_html_e( 'Search for:', 'studio22' ); ?></label>
	<input type="search" id="<?php echo esc_attr( $s22_id ); ?>" name="s" value="<?php echo esc_attr( get_search_query() ); ?>" placeholder="<?php esc_attr_e( 'Search…', 'studio22' ); ?>">
	<button type="submit" class="btn btn--accent btn--sm"><?php esc_html_e( 'Search', 'studio22' ); ?></button>
</form>
