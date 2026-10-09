<?php
/* Full-width Elementor content between the theme header and footer. */
get_header();
while ( have_posts() ) :
	the_post();
	the_content();
endwhile;
get_footer();
