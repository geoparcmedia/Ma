<?php
if (!defined('ABSPATH')) {
	exit;
}
$c = s22_contact();
?>
<footer class="s22-footer">
	<div class="s22-wrap s22-footer-in">
		<div>
			<div class="s22-logo">STUDIO<span>22</span></div>
			<p><?php echo esc_html(s22_t('footer')); ?></p>
		</div>
		<div class="s22-footer-links">
			<?php if ($c['instagram_url']) : ?><a href="<?php echo esc_url($c['instagram_url']); ?>" target="_blank" rel="noopener">Instagram</a><?php endif; ?>
			<?php if ($c['whatsapp_url']) : ?><a href="<?php echo esc_url($c['whatsapp_url']); ?>" target="_blank" rel="noopener">WhatsApp</a><?php endif; ?>
			<?php if ($c['email']) : ?><a href="mailto:<?php echo esc_attr($c['email']); ?>"><?php echo esc_html($c['email']); ?></a><?php endif; ?>
		</div>
		<p class="s22-copy">&copy; <?php echo esc_html(date('Y')); ?> Studio22. <?php echo esc_html(s22_t('rights')); ?></p>
	</div>
</footer>
<?php if ($c['whatsapp_url']) : ?>
<a class="s22-wa-float" href="<?php echo esc_url($c['whatsapp_url']); ?>" target="_blank" rel="noopener" aria-label="WhatsApp"><?php echo s22_icon('whatsapp'); ?></a>
<?php endif; ?>
<?php wp_footer(); ?>
</body>
</html>
