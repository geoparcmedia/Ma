<?php
if ( a2s_is_elementor( get_queried_object_id() ) ) {
	get_template_part( 'template-parts/elementor-content' );
	return;
}
require __DIR__ . '/index.php';
