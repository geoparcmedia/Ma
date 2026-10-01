<!doctype html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<header class="site-header<?php echo is_front_page() ? ' is-transparent' : ''; ?>" id="top">
	<div class="container header-inner">
		<a class="brand" href="<?php echo esc_url( home_url( '/' ) ); ?>">Atlas<span>2</span>Sahara</a>
		<button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu"><span></span><span></span><span></span></button>
		<nav class="site-nav" id="site-nav">
			<?php
			wp_nav_menu( array(
				'theme_location' => 'primary',
				'container'      => false,
				'fallback_cb'    => 'a2s_fallback_menu',
			) );
			?>
			<a class="btn btn-sm" href="<?php echo esc_url( home_url( '/#contact' ) ); ?>">Plan your trip</a>
		</nav>
	</div>
</header>
<main id="main">
