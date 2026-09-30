<?php
// Other pages and posts: simple layout with the site header and footer.
if (!defined('ABSPATH')) {
	exit;
}
get_header();
?>
<main id="main" class="s22-page">
	<div class="s22-wrap s22-narrow">
		<?php if (have_posts()) : while (have_posts()) : the_post(); ?>
			<article <?php post_class(); ?>>
				<h1><?php the_title(); ?></h1>
				<div class="s22-content"><?php the_content(); ?></div>
			</article>
		<?php endwhile; else : ?>
			<h1><?php echo s22_lang() === 'ar' ? 'الصفحة غير موجودة' : 'Page not found'; ?></h1>
			<p><a class="s22-btn" href="<?php echo esc_url(home_url('/')); ?>">Studio22</a></p>
		<?php endif; ?>
	</div>
</main>
<?php
get_footer();
