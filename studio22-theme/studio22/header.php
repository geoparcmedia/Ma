<?php
/**
 * Header.
 *
 * @package Studio22
 */

?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="theme-color" content="#0b0a0b">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<a class="skip-link screen-reader-text" href="#content"><?php esc_html_e( 'Skip to content', 'studio22' ); ?></a>

<header class="site-header" id="site-header">
	<div class="container site-header__inner">
		<?php studio22_logo(); ?>

		<nav class="main-nav" id="main-nav" aria-label="<?php esc_attr_e( 'Main menu', 'studio22' ); ?>">
			<?php
			wp_nav_menu(
				array(
					'theme_location' => 'primary',
					'container'      => false,
					'depth'          => 2,
					'fallback_cb'    => 'studio22_menu_fallback',
				)
			);
			?>
			<div class="main-nav__extra">
				<?php studio22_language_switcher(); ?>
				<a class="btn btn--accent btn--sm" href="<?php echo esc_url( studio22_book_url() ); ?>"<?php echo studio22_whatsapp_number() ? ' target="_blank" rel="noopener"' : ''; ?>><?php studio22_e( 'hero_btn1' ); ?></a>
			</div>
		</nav>

		<button class="nav-toggle" type="button" aria-controls="main-nav" aria-expanded="false">
			<span class="nav-toggle__open"><?php echo studio22_icon( 'menu' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
			<span class="nav-toggle__close"><?php echo studio22_icon( 'close' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
			<span class="screen-reader-text"><?php esc_html_e( 'Menu', 'studio22' ); ?></span>
		</button>
	</div>
</header>

<main id="content" class="site-main">
