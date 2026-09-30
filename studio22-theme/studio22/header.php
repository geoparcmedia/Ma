<?php
if (!defined('ABSPATH')) {
	exit;
}
$lang = s22_lang();
$home = $lang === 'ar' ? home_url('/ar/') : home_url('/');
$other = $lang === 'ar' ? home_url('/') : home_url('/ar/');
$nav = s22_t('nav');
$is_one = is_front_page() || $lang === 'ar';
$base = $is_one ? '' : $home;
?><!doctype html>
<html lang="<?php echo $lang === 'ar' ? 'ar' : 'en'; ?>" dir="<?php echo $lang === 'ar' ? 'rtl' : 'ltr'; ?>">
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0c0c0e">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<?php wp_head(); ?>
</head>
<body <?php body_class('s22 s22-' . $lang); ?>>
<?php wp_body_open(); ?>
<a class="s22-skip" href="#main"><?php echo $lang === 'ar' ? 'انتقل إلى المحتوى' : 'Skip to content'; ?></a>
<header class="s22-header" id="top">
	<div class="s22-wrap s22-header-in">
		<a class="s22-logo" href="<?php echo esc_url($home); ?>" aria-label="Studio22">
			<?php if (has_custom_logo()) {
				$logo = wp_get_attachment_image_url(get_theme_mod('custom_logo'), 'medium');
				echo '<img src="' . esc_url($logo) . '" alt="Studio22">';
			} else {
				echo 'STUDIO<span>22</span>';
			} ?>
		</a>
		<nav class="s22-nav" aria-label="<?php echo $lang === 'ar' ? 'القائمة الرئيسية' : 'Main menu'; ?>">
			<?php foreach ($nav as $id => $label) : ?>
				<a href="<?php echo esc_url($base) . '#' . esc_attr($id); ?>"><?php echo esc_html($label); ?></a>
			<?php endforeach; ?>
		</nav>
		<div class="s22-header-actions">
			<a class="s22-lang" href="<?php echo esc_url($other); ?>" hreflang="<?php echo $lang === 'ar' ? 'en' : 'ar'; ?>" lang="<?php echo $lang === 'ar' ? 'en' : 'ar'; ?>"><?php echo esc_html(s22_t('lang_switch')); ?></a>
			<a class="s22-btn s22-btn-sm" href="<?php echo esc_url($base); ?>#book"><?php echo esc_html(s22_t('book')); ?></a>
			<button class="s22-burger" type="button" aria-expanded="false" aria-controls="s22-menu" aria-label="<?php echo $lang === 'ar' ? 'القائمة' : 'Menu'; ?>"><span></span><span></span></button>
		</div>
	</div>
	<div class="s22-menu" id="s22-menu" hidden>
		<?php foreach ($nav as $id => $label) : ?>
			<a href="<?php echo esc_url($base) . '#' . esc_attr($id); ?>"><?php echo esc_html($label); ?></a>
		<?php endforeach; ?>
		<a class="s22-btn" href="<?php echo esc_url($base); ?>#book"><?php echo esc_html(s22_t('book')); ?></a>
		<a class="s22-lang" href="<?php echo esc_url($other); ?>"><?php echo esc_html(s22_t('lang_switch')); ?></a>
	</div>
</header>
