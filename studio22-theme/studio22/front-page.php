<?php
if (!defined('ABSPATH')) {
	exit;
}
get_header();
$lang = s22_lang();
$c = s22_contact();
$location = ($lang === 'ar' && $c['location'] === 'Doha, Qatar') ? s22_t('location') : $c['location'];
$hero = s22_img('hero', 'full');
$about = s22_img('about', 'large');
$works = array();
$labels = s22_t('work_labels');
for ($i = 1; $i <= 6; $i++) {
	$src = s22_img('work' . $i, 'large');
	if ($src) {
		$works[] = array('src' => $src, 'label' => $labels[$i - 1]);
	}
}
$services = s22_t('services');
?>
<main id="main">

	<section class="s22-hero<?php echo $hero ? ' has-img' : ''; ?>">
		<?php if ($hero) : ?><img class="s22-hero-img" src="<?php echo esc_url($hero); ?>" alt="" fetchpriority="high"><?php endif; ?>
		<div class="s22-hero-grain" aria-hidden="true"></div>
		<div class="s22-wrap s22-hero-in">
			<p class="s22-eyebrow"><?php echo esc_html(s22_t('hero_eyebrow')); ?></p>
			<h1><?php echo wp_kses(s22_t('hero_title'), array('em' => array())); ?></h1>
			<p class="s22-lead"><?php echo esc_html(s22_t('hero_text')); ?></p>
			<div class="s22-cta">
				<a class="s22-btn" href="#book"><?php echo esc_html(s22_t('hero_cta')); ?> <?php echo s22_icon('arrow'); ?></a>
				<a class="s22-btn s22-btn-ghost" href="#work"><?php echo esc_html(s22_t('hero_cta2')); ?></a>
			</div>
		</div>
		<div class="s22-hero-num" aria-hidden="true">22</div>
	</section>

	<section class="s22-sec" id="services">
		<div class="s22-wrap">
			<div class="s22-head">
				<p class="s22-eyebrow"><?php echo esc_html(s22_t('services_eyebrow')); ?></p>
				<h2><?php echo esc_html(s22_t('services_title')); ?></h2>
			</div>
			<div class="s22-services">
				<?php foreach ($services as $n => $s) : ?>
					<article class="s22-service">
						<span class="s22-service-n"><?php echo esc_html(sprintf('%02d', $n + 1)); ?></span>
						<?php echo s22_icon($s['icon']); ?>
						<h3><?php echo esc_html($s['t']); ?></h3>
						<p><?php echo esc_html($s['d']); ?></p>
					</article>
				<?php endforeach; ?>
			</div>
		</div>
	</section>

	<section class="s22-sec s22-sec-dark" id="work">
		<div class="s22-wrap">
			<div class="s22-head s22-head-row">
				<div>
					<p class="s22-eyebrow"><?php echo esc_html(s22_t('work_eyebrow')); ?></p>
					<h2><?php echo esc_html(s22_t('work_title')); ?></h2>
				</div>
				<?php if ($c['instagram_url']) : ?>
					<a class="s22-link" href="<?php echo esc_url($c['instagram_url']); ?>" target="_blank" rel="noopener"><?php echo s22_icon('instagram'); ?> <?php echo esc_html(s22_t('work_more')); ?></a>
				<?php endif; ?>
			</div>
			<?php if ($works) : ?>
				<div class="s22-work s22-work-<?php echo count($works); ?>">
					<?php foreach ($works as $w) : ?>
						<figure class="s22-work-item">
							<img src="<?php echo esc_url($w['src']); ?>" alt="<?php echo esc_attr($w['label']); ?>" loading="lazy">
							<figcaption><?php echo esc_html($w['label']); ?></figcaption>
						</figure>
					<?php endforeach; ?>
				</div>
			<?php else : ?>
				<a class="s22-work-empty" href="<?php echo esc_url($c['instagram_url']); ?>" target="_blank" rel="noopener">
					<?php echo s22_icon('instagram'); ?>
					<span><?php echo esc_html(s22_t('work_empty')); ?></span>
					<strong dir="ltr">@<?php echo esc_html($c['instagram']); ?></strong>
				</a>
			<?php endif; ?>
		</div>
	</section>

	<section class="s22-sec" id="about">
		<div class="s22-wrap s22-about">
			<div class="s22-about-media<?php echo $about ? '' : ' is-empty'; ?>">
				<?php if ($about) : ?>
					<img src="<?php echo esc_url($about); ?>" alt="<?php echo $lang === 'ar' ? 'عبدالعزيز العجمي' : 'Abdulaziz Alajmi'; ?>" loading="lazy">
				<?php else : ?>
					<span aria-hidden="true"><?php echo s22_icon('camera'); ?></span>
				<?php endif; ?>
			</div>
			<div class="s22-about-text">
				<p class="s22-eyebrow"><?php echo esc_html(s22_t('about_eyebrow')); ?></p>
				<h2><?php echo esc_html(s22_t('about_title')); ?></h2>
				<p class="s22-role"><?php echo esc_html(s22_t('about_role')); ?></p>
				<p><?php echo esc_html(s22_t('about_p1')); ?></p>
				<p><?php echo esc_html(s22_t('about_p2')); ?></p>
				<p><?php echo esc_html(s22_t('about_p3')); ?></p>
				<?php if ($c['instagram_url']) : ?>
					<a class="s22-link" href="<?php echo esc_url($c['instagram_url']); ?>" target="_blank" rel="noopener"><?php echo s22_icon('instagram'); ?> <?php echo esc_html(s22_t('about_follow')); ?> · <bdi dir="ltr">@<?php echo esc_html($c['instagram']); ?></bdi></a>
				<?php endif; ?>
			</div>
		</div>
	</section>

	<section class="s22-sec s22-sec-soft" id="process">
		<div class="s22-wrap">
			<div class="s22-head">
				<p class="s22-eyebrow"><?php echo esc_html(s22_t('process_eyebrow')); ?></p>
				<h2><?php echo esc_html(s22_t('process_title')); ?></h2>
			</div>
			<ol class="s22-steps">
				<?php foreach (s22_t('process') as $n => $p) : ?>
					<li><span><?php echo esc_html(sprintf('%02d', $n + 1)); ?></span><h3><?php echo esc_html($p['t']); ?></h3><p><?php echo esc_html($p['d']); ?></p></li>
				<?php endforeach; ?>
			</ol>
		</div>
	</section>

	<section class="s22-sec s22-sec-dark" id="book">
		<div class="s22-wrap s22-book">
			<div class="s22-book-text">
				<p class="s22-eyebrow"><?php echo esc_html(s22_t('book_eyebrow')); ?></p>
				<h2><?php echo esc_html(s22_t('book_title')); ?></h2>
				<p><?php echo esc_html(s22_t('book_text')); ?></p>
			</div>
			<form class="s22-form" data-wa="<?php echo esc_attr($c['whatsapp']); ?>" data-intro="<?php echo esc_attr(s22_t('f_msg_intro')); ?>">
				<label><span><?php echo esc_html(s22_t('f_name')); ?></span><input name="<?php echo esc_attr(s22_t('f_name')); ?>" required autocomplete="name"></label>
				<label><span><?php echo esc_html(s22_t('f_service')); ?></span>
					<select name="<?php echo esc_attr(s22_t('f_service')); ?>">
						<?php foreach ($services as $s) : ?><option><?php echo esc_html($s['t']); ?></option><?php endforeach; ?>
						<option><?php echo esc_html(s22_t('f_other')); ?></option>
					</select>
				</label>
				<div class="s22-form-row">
					<label><span><?php echo esc_html(s22_t('f_date')); ?></span><input type="date" name="<?php echo esc_attr(s22_t('f_date')); ?>"></label>
					<label><span><?php echo esc_html(s22_t('f_place')); ?></span><input name="<?php echo esc_attr(s22_t('f_place')); ?>"></label>
				</div>
				<label><span><?php echo esc_html(s22_t('f_details')); ?></span><textarea name="<?php echo esc_attr(s22_t('f_details')); ?>" rows="4" placeholder="<?php echo esc_attr(s22_t('f_details_ph')); ?>"></textarea></label>
				<button class="s22-btn s22-btn-wa" type="submit"><?php echo s22_icon('whatsapp'); ?> <?php echo esc_html(s22_t('f_send')); ?></button>
				<?php if ($c['email']) : ?>
					<a class="s22-form-alt" href="mailto:<?php echo esc_attr($c['email']); ?>?subject=<?php echo rawurlencode('Studio22 booking'); ?>"><?php echo esc_html(s22_t('f_or')); ?> · <?php echo esc_html($c['email']); ?></a>
				<?php endif; ?>
			</form>
		</div>
	</section>

	<section class="s22-sec" id="contact">
		<div class="s22-wrap">
			<div class="s22-head">
				<p class="s22-eyebrow"><?php echo esc_html(s22_t('contact_eyebrow')); ?></p>
				<h2><?php echo esc_html(s22_t('contact_title')); ?></h2>
			</div>
			<div class="s22-contact">
				<?php if ($c['phone']) : ?>
					<a class="s22-card" href="tel:<?php echo esc_attr(preg_replace('/[^\d+]/', '', $c['phone'])); ?>"><?php echo s22_icon('phone'); ?><span><?php echo esc_html(s22_t('c_phone')); ?></span><strong dir="ltr"><?php echo esc_html(s22_phone_display($c['phone'])); ?></strong></a>
				<?php endif; ?>
				<?php if ($c['whatsapp_url']) : ?>
					<a class="s22-card" href="<?php echo esc_url($c['whatsapp_url']); ?>" target="_blank" rel="noopener"><?php echo s22_icon('whatsapp'); ?><span><?php echo esc_html(s22_t('c_whatsapp')); ?></span><strong dir="ltr"><?php echo esc_html(s22_phone_display('+' . $c['whatsapp'])); ?></strong></a>
				<?php endif; ?>
				<?php if ($c['email']) : ?>
					<a class="s22-card" href="mailto:<?php echo esc_attr($c['email']); ?>"><?php echo s22_icon('mail'); ?><span><?php echo esc_html(s22_t('c_email')); ?></span><strong dir="ltr"><?php echo esc_html($c['email']); ?></strong></a>
				<?php endif; ?>
				<?php if ($c['instagram_url']) : ?>
					<a class="s22-card" href="<?php echo esc_url($c['instagram_url']); ?>" target="_blank" rel="noopener"><?php echo s22_icon('instagram'); ?><span><?php echo esc_html(s22_t('c_instagram')); ?></span><strong dir="ltr">@<?php echo esc_html($c['instagram']); ?></strong></a>
				<?php endif; ?>
				<div class="s22-card"><?php echo s22_icon('pin'); ?><span><?php echo esc_html(s22_t('c_location')); ?></span><strong><?php echo esc_html($location); ?></strong></div>
			</div>
		</div>
	</section>

</main>
<?php
get_footer();
