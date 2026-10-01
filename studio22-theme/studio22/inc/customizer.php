<?php
/**
 * Customizer options. Every text has an English and an Arabic field.
 *
 * @package Studio22
 */

defined( 'ABSPATH' ) || exit;

/**
 * Default texts, English and Arabic.
 *
 * @return array key => [ 'en' => ..., 'ar' => ... ]
 */
function studio22_text_defaults() {
	static $defaults = null;
	if ( null !== $defaults ) {
		return $defaults;
	}

	$defaults = array(
		// Hero.
		'hero_eyebrow'   => array(
			'en' => 'Photo & Video Production — Doha, Qatar',
			'ar' => 'إنتاج الصور والفيديو — الدوحة، قطر',
		),
		'hero_title'     => array(
			'en' => 'We frame the moments that move you.',
			'ar' => 'نؤطّر اللحظات التي تُلهمك.',
		),
		'hero_subtitle'  => array(
			'en' => 'Photography, film and studio production with a cinematic eye.',
			'ar' => 'تصوير فوتوغرافي وأفلام وإنتاج استوديو برؤية سينمائية.',
		),
		'hero_line2'     => array(
			'en' => 'Every frame is lit, composed and graded with intent.',
			'ar' => 'كل لقطة تُضاء وتُكوَّن وتُلوَّن بعناية.',
		),
		'hero_line3'     => array(
			'en' => 'From the first idea to the final cut.',
			'ar' => 'من الفكرة الأولى حتى المونتاج النهائي.',
		),
		'hero_btn1'      => array(
			'en' => 'Book a shoot',
			'ar' => 'احجز جلسة تصوير',
		),
		'hero_btn2'      => array(
			'en' => 'View our work',
			'ar' => 'شاهد أعمالنا',
		),
		'marquee'        => array(
			'en' => 'Photography, Films, Commercials, Equestrian, Portraits, Events, Products, Drone, Post-production',
			'ar' => 'تصوير فوتوغرافي، أفلام، إعلانات، الخيل، بورتريه، فعاليات، منتجات، درون، مونتاج',
		),

		// Services.
		'services_kicker' => array(
			'en' => 'What we do',
			'ar' => 'ماذا نقدّم',
		),
		'services_title' => array(
			'en' => 'Production, from concept to delivery.',
			'ar' => 'إنتاج متكامل، من الفكرة إلى التسليم.',
		),
		'service1_title' => array(
			'en' => 'Photography',
			'ar' => 'التصوير الفوتوغرافي',
		),
		'service1_text'  => array(
			'en' => 'Portraits, fashion, editorial and corporate photography, on location or in our studio.',
			'ar' => 'بورتريه، أزياء، تصوير تحريري وتصوير للشركات، في الموقع أو داخل الاستوديو.',
		),
		'service2_title' => array(
			'en' => 'Video & films',
			'ar' => 'الفيديو والأفلام',
		),
		'service2_text'  => array(
			'en' => 'Commercials, brand films, documentaries and social content shot in 4K and beyond.',
			'ar' => 'إعلانات، أفلام للعلامات التجارية، وثائقيات ومحتوى للتواصل الاجتماعي بدقة 4K وأعلى.',
		),
		'service3_title' => array(
			'en' => 'Equestrian & heritage',
			'ar' => 'الخيل والتراث',
		),
		'service3_text'  => array(
			'en' => 'Arabian horses, shows and heritage stories, captured with patience and respect.',
			'ar' => 'الخيل العربية والبطولات وقصص التراث، نصوّرها بصبر واحترام.',
		),
		'service4_title' => array(
			'en' => 'Studio rental',
			'ar' => 'تأجير الاستوديو',
		),
		'service4_text'  => array(
			'en' => 'A fully equipped studio with lighting, backdrops and a team ready for your production.',
			'ar' => 'استوديو مجهّز بالكامل بالإضاءة والخلفيات وفريق جاهز لإنتاجك.',
		),
		'service5_title' => array(
			'en' => 'Products & commercial',
			'ar' => 'المنتجات والإعلانات',
		),
		'service5_text'  => array(
			'en' => 'Product, food and e-commerce imagery that sells, with consistent lighting and colour.',
			'ar' => 'صور منتجات وأطعمة ومتاجر إلكترونية تبيع، بإضاءة وألوان متناسقة.',
		),
		'service6_title' => array(
			'en' => 'Post-production',
			'ar' => 'ما بعد الإنتاج',
		),
		'service6_text'  => array(
			'en' => 'Editing, colour grading, retouching, motion graphics and sound design.',
			'ar' => 'مونتاج، تصحيح ألوان، تنقيح الصور، موشن جرافيك وتصميم صوتي.',
		),

		// Work.
		'work_kicker'    => array(
			'en' => 'Selected work',
			'ar' => 'أعمال مختارة',
		),
		'work_title'     => array(
			'en' => 'Stories we have told.',
			'ar' => 'قصص رويناها.',
		),
		'work_all'       => array(
			'en' => 'View all projects',
			'ar' => 'عرض كل المشاريع',
		),

		// Studio / about.
		'studio_kicker'  => array(
			'en' => 'The studio',
			'ar' => 'الاستوديو',
		),
		'studio_title'   => array(
			'en' => 'A creative home for images that last.',
			'ar' => 'بيت إبداعي لصور تدوم.',
		),
		'studio_text'    => array(
			'en' => 'Studio22 is a photo and video production house based in Doha. We work with brands, families, institutions and horse owners across Qatar and the Gulf, bringing a cinematic eye and a calm, professional crew to every shoot.',
			'ar' => 'ستوديو 22 دار إنتاج للصور والفيديو مقرّها الدوحة. نعمل مع العلامات التجارية والعائلات والمؤسسات وملّاك الخيل في قطر والخليج، ونجلب إلى كل جلسة تصوير رؤية سينمائية وفريقًا محترفًا وهادئًا.',
		),
		'studio_more'    => array(
			'en' => 'About us',
			'ar' => 'من نحن',
		),
		'stat1_label'    => array(
			'en' => 'Years behind the lens',
			'ar' => 'سنوات خلف العدسة',
		),
		'stat2_label'    => array(
			'en' => 'Projects delivered',
			'ar' => 'مشروع منجز',
		),
		'stat3_label'    => array(
			'en' => 'Happy clients',
			'ar' => 'عميل سعيد',
		),
		'stat4_label'    => array(
			'en' => 'Hours of footage',
			'ar' => 'ساعة تصوير',
		),

		// Founder (About page).
		'founder_kicker' => array(
			'en' => 'Founder',
			'ar' => 'المؤسس',
		),
		'founder_name'   => array(
			'en' => 'Abdulaziz Al Ajmi',
			'ar' => 'عبدالعزيز العجمي',
		),
		'founder_role'   => array(
			'en' => 'Founder · Qatari photographer & visual artist',
			'ar' => 'المؤسس · مصوّر وفنان بصري قطري',
		),
		'founder_quote'  => array(
			'en' => '',
			'ar' => '',
		),
		'founder_bio'    => array(
			'en' => "Abdulaziz Al Ajmi is a Qatari photographer and visual artist with extensive experience in professional photography and visual production. His work reflects a strong passion for capturing people, events, culture, and memorable moments through creative and authentic imagery.\n\nOver the years, Abdulaziz has developed his expertise across photography and video production, working on a variety of professional and cultural projects in Qatar. His creative approach combines technical skills with a distinctive visual style, allowing him to tell stories through powerful images.\n\nThrough his work and experience in the Qatari creative industry, Abdulaziz Al Ajmi has established himself as a dedicated photographer committed to quality, creativity, and visual storytelling.",
			'ar' => "عبدالعزيز العجمي مصوّر وفنان بصري قطري يمتلك خبرة واسعة في التصوير الاحترافي والإنتاج البصري. تعكس أعماله شغفًا كبيرًا بتوثيق الناس والفعاليات والثقافة واللحظات التي لا تُنسى من خلال صور إبداعية وأصيلة.\n\nعلى مرّ السنين، طوّر عبدالعزيز خبرته في التصوير الفوتوغرافي وإنتاج الفيديو، وعمل على مجموعة متنوعة من المشاريع المهنية والثقافية في قطر. ويجمع أسلوبه الإبداعي بين المهارة التقنية وهوية بصرية مميزة تتيح له رواية القصص من خلال صور مؤثرة.\n\nومن خلال أعماله وخبرته في القطاع الإبداعي القطري، رسّخ عبدالعزيز العجمي مكانته كمصوّر ملتزم بالجودة والإبداع وفن السرد البصري.",
		),

		// Clients.
		'clients_kicker' => array(
			'en' => 'Our clients',
			'ar' => 'عملاؤنا',
		),
		'clients_title'  => array(
			'en' => 'Trusted by leading names in Qatar.',
			'ar' => 'ثقة أبرز الأسماء في قطر.',
		),
		'client1_name'   => array(
			'en' => 'Katara',
			'ar' => 'كتارا',
		),
		'client2_name'   => array(
			'en' => 'Al Shaqab',
			'ar' => 'الشقب',
		),
		'client3_name'   => array(
			'en' => 'Arabians Tour',
			'ar' => 'أرابيانز تور',
		),
		'client4_name'   => array(
			'en' => 'Doha Bank',
			'ar' => 'بنك الدوحة',
		),
		'client5_name'   => array(
			'en' => 'ACTA',
			'ar' => 'أكتا',
		),
		'client6_name'   => array(
			'en' => 'KIAF',
			'ar' => 'كياف',
		),

		// Process.
		'process_kicker' => array(
			'en' => 'How we work',
			'ar' => 'كيف نعمل',
		),
		'process_title'  => array(
			'en' => 'Four steps, no surprises.',
			'ar' => 'أربع خطوات، بلا مفاجآت.',
		),
		'step1_title'    => array(
			'en' => 'Brief',
			'ar' => 'الفكرة',
		),
		'step1_text'     => array(
			'en' => 'We listen, ask the right questions and agree on goals, budget and timing.',
			'ar' => 'نستمع ونطرح الأسئلة الصحيحة ونتفق على الأهداف والميزانية والتوقيت.',
		),
		'step2_title'    => array(
			'en' => 'Pre-production',
			'ar' => 'التحضير',
		),
		'step2_text'     => array(
			'en' => 'Moodboard, shot list, locations, talent and permits are planned in detail.',
			'ar' => 'نخطط بالتفصيل للوحة الإلهام وقائمة اللقطات والمواقع والمواهب والتصاريح.',
		),
		'step3_title'    => array(
			'en' => 'Shoot',
			'ar' => 'التصوير',
		),
		'step3_text'     => array(
			'en' => 'Our crew captures every moment with cinema cameras, lighting and drones.',
			'ar' => 'يلتقط فريقنا كل لحظة بكاميرات سينمائية وإضاءة احترافية وطائرات درون.',
		),
		'step4_title'    => array(
			'en' => 'Delivery',
			'ar' => 'التسليم',
		),
		'step4_text'     => array(
			'en' => 'Edited, graded and delivered in every format you need, on time.',
			'ar' => 'مونتاج وتلوين وتسليم بكل الصيغ التي تحتاجها، في الموعد المحدد.',
		),

		// CTA.
		'cta_title'      => array(
			'en' => 'Have a story to tell?',
			'ar' => 'لديك قصة تريد روايتها؟',
		),
		'cta_text'       => array(
			'en' => 'Tell us about your project and we will reply within the day.',
			'ar' => 'حدّثنا عن مشروعك وسنرد عليك في نفس اليوم.',
		),
		'cta_btn'        => array(
			'en' => 'Chat on WhatsApp',
			'ar' => 'تواصل عبر واتساب',
		),

		// Contact.
		'contact_kicker' => array(
			'en' => 'Contact',
			'ar' => 'تواصل معنا',
		),
		'contact_title'  => array(
			'en' => 'Let’s create something together.',
			'ar' => 'لنصنع شيئًا معًا.',
		),
		'address'        => array(
			'en' => 'Doha, Qatar',
			'ar' => 'الدوحة، قطر',
		),
		'hours'          => array(
			'en' => 'Saturday – Thursday, 9:00 – 21:00',
			'ar' => 'السبت – الخميس، 9:00 – 21:00',
		),
		'wa_message'     => array(
			'en' => 'Hello Studio22, I would like to book a shoot.',
			'ar' => 'مرحبًا ستوديو 22، أرغب في حجز جلسة تصوير.',
		),

		// Footer.
		'footer_text'    => array(
			'en' => 'Photo and video production studio in Doha, Qatar.',
			'ar' => 'استوديو إنتاج صور وفيديو في الدوحة، قطر.',
		),
	);

	return $defaults;
}

/**
 * Defaults for options that are the same in both languages.
 *
 * @return array
 */
function studio22_option_defaults() {
	return array(
		'accent'           => '#c21d4f',
		'hero_mode'        => 'scrub',
		'hero_video'       => '',
		'hero_poster'      => '',
		'hero_length'      => 300,
		'service1_icon'    => 'camera',
		'service2_icon'    => 'video',
		'service3_icon'    => 'horse',
		'service4_icon'    => 'studio',
		'service5_icon'    => 'product',
		'service6_icon'    => 'edit',
		'work_count'       => 6,
		'studio_image'     => '',
		'founder_photo'    => '',
		'stat1_number'     => '10',
		'stat2_number'     => '850',
		'stat3_number'     => '300',
		'stat4_number'     => '5000',
		'client1_url'      => 'https://www.katara.net',
		'client2_url'      => 'https://www.alshaqab.com',
		'client3_url'      => '',
		'client4_url'      => 'https://www.dohabank.qa',
		'client5_url'      => 'https://acta.qa',
		'client6_url'      => '',
		'clients_color'    => false,
		'instagram_feed'   => '',
		'social_instagram' => 'https://www.instagram.com/alajmiofficial/',
		'whatsapp'         => '',
		'phone'            => '',
		'email'            => '',
		'map'              => 'Doha, Qatar',
		'form_shortcode'   => '',
		'show_marquee'     => true,
		'show_services'    => true,
		'show_work'        => true,
		'show_studio'      => true,
		'show_clients'     => true,
		'show_process'     => true,
		'show_cta'         => true,
		'show_contact'     => true,
		'show_wa_float'    => true,
	);
}

/**
 * Register Customizer panels, sections, settings and controls.
 *
 * @param WP_Customize_Manager $wp_customize Customizer manager.
 */
function studio22_customize_register( $wp_customize ) {
	$defaults = studio22_text_defaults();
	$options  = studio22_option_defaults();

	$wp_customize->add_panel(
		'studio22',
		array(
			'title'       => __( 'Studio22 theme', 'studio22' ),
			'description' => __( 'Each text has an English and an Arabic field. The Arabic one is shown when the page language is Arabic (site language, Polylang or WPML).', 'studio22' ),
			'priority'    => 30,
		)
	);

	/*
	 * Helpers to add controls in a few lines.
	 */
	$add_text = function ( $section, $key, $label, $type = 'text' ) use ( $wp_customize, $defaults ) {
		foreach ( array(
			'en' => __( 'English', 'studio22' ),
			'ar' => __( 'Arabic', 'studio22' ),
		) as $lang => $lang_label ) {
			$id = "studio22_{$key}_{$lang}";
			$wp_customize->add_setting(
				$id,
				array(
					'default'           => $defaults[ $key ][ $lang ] ?? '',
					'sanitize_callback' => 'textarea' === $type ? 'sanitize_textarea_field' : 'sanitize_text_field',
					'transport'         => 'refresh',
				)
			);
			$wp_customize->add_control(
				$id,
				array(
					'label'       => $label . ' — ' . $lang_label,
					'section'     => $section,
					'type'        => $type,
					'input_attrs' => 'ar' === $lang ? array( 'dir' => 'rtl' ) : array(),
				)
			);
		}
	};

	$add_option = function ( $section, $key, $label, $type = 'text', $args = array() ) use ( $wp_customize, $options ) {
		$id       = "studio22_{$key}";
		$sanitize = 'sanitize_text_field';
		if ( 'checkbox' === $type ) {
			$sanitize = 'studio22_sanitize_checkbox';
		} elseif ( 'number' === $type ) {
			$sanitize = 'absint';
		} elseif ( 'email' === $type ) {
			$sanitize = 'sanitize_email';
		} elseif ( 'url' === $type ) {
			$sanitize = 'esc_url_raw';
		} elseif ( 'select' === $type ) {
			$choices  = $args['choices'];
			$fallback = $options[ $key ] ?? '';
			$sanitize = function ( $value ) use ( $choices, $fallback ) {
				return array_key_exists( $value, $choices ) ? $value : $fallback;
			};
		}
		$wp_customize->add_setting(
			$id,
			array(
				'default'           => $options[ $key ] ?? '',
				'sanitize_callback' => $sanitize,
			)
		);
		$wp_customize->add_control(
			$id,
			array_merge(
				array(
					'label'   => $label,
					'section' => $section,
					'type'    => $type,
				),
				$args
			)
		);
	};

	$add_media = function ( $section, $key, $label, $mime, $description = '' ) use ( $wp_customize ) {
		$id = "studio22_{$key}";
		$wp_customize->add_setting(
			$id,
			array(
				'default'           => '',
				'sanitize_callback' => 'absint',
			)
		);
		$wp_customize->add_control(
			new WP_Customize_Media_Control(
				$wp_customize,
				$id,
				array(
					'label'       => $label,
					'description' => $description,
					'section'     => $section,
					'mime_type'   => $mime,
				)
			)
		);
	};

	/*
	 * Brand.
	 */
	$wp_customize->add_section(
		'studio22_brand',
		array(
			'title' => __( 'Colours & sections', 'studio22' ),
			'panel' => 'studio22',
		)
	);
	$wp_customize->add_setting(
		'studio22_accent',
		array(
			'default'           => $options['accent'],
			'sanitize_callback' => 'sanitize_hex_color',
		)
	);
	$wp_customize->add_control(
		new WP_Customize_Color_Control(
			$wp_customize,
			'studio22_accent',
			array(
				'label'   => __( 'Accent colour', 'studio22' ),
				'section' => 'studio22_brand',
			)
		)
	);
	$sections = array(
		'show_marquee'  => __( 'Show the moving services strip', 'studio22' ),
		'show_services' => __( 'Show services', 'studio22' ),
		'show_work'     => __( 'Show portfolio', 'studio22' ),
		'show_studio'   => __( 'Show studio section', 'studio22' ),
		'show_clients'  => __( 'Show clients', 'studio22' ),
		'show_process'  => __( 'Show process', 'studio22' ),
		'show_cta'      => __( 'Show call-to-action banner', 'studio22' ),
		'show_contact'  => __( 'Show contact', 'studio22' ),
		'show_wa_float' => __( 'Show floating WhatsApp button', 'studio22' ),
	);
	foreach ( $sections as $key => $label ) {
		$add_option( 'studio22_brand', $key, $label, 'checkbox' );
	}

	/*
	 * Hero.
	 */
	$wp_customize->add_section(
		'studio22_hero',
		array(
			'title'       => __( 'Hero video banner', 'studio22' ),
			'panel'       => 'studio22',
			'description' => __( 'Tip for a smooth scroll effect: export the video as MP4 (H.264), 1920px wide, without sound, 10–20 seconds, with a keyframe every few frames, e.g. ffmpeg -i in.mov -vf scale=1920:-2 -c:v libx264 -crf 24 -g 6 -an -movflags +faststart hero.mp4', 'studio22' ),
		)
	);
	$add_option(
		'studio22_hero',
		'hero_mode',
		__( 'Video behaviour', 'studio22' ),
		'select',
		array(
			'choices' => array(
				'scrub' => __( 'Pinned — the video plays as you scroll', 'studio22' ),
				'loop'  => __( 'Pinned — the video plays on its own (loop)', 'studio22' ),
				'still' => __( 'Normal banner — video loops, no pinning', 'studio22' ),
			),
		)
	);
	$add_media( 'studio22_hero', 'hero_video', __( 'Hero video (MP4)', 'studio22' ), 'video' );
	$add_media( 'studio22_hero', 'hero_poster', __( 'Poster image', 'studio22' ), 'image', __( 'Shown while the video loads, and on its own when there is no video.', 'studio22' ) );
	$add_option(
		'studio22_hero',
		'hero_length',
		__( 'Scroll length of the pinned banner (% of screen height)', 'studio22' ),
		'number',
		array(
			'input_attrs' => array(
				'min'  => 150,
				'max'  => 600,
				'step' => 50,
			),
		)
	);
	$add_text( 'studio22_hero', 'hero_eyebrow', __( 'Small line above the title', 'studio22' ) );
	$add_text( 'studio22_hero', 'hero_title', __( 'Title', 'studio22' ) );
	$add_text( 'studio22_hero', 'hero_subtitle', __( 'Subtitle', 'studio22' ), 'textarea' );
	$add_text( 'studio22_hero', 'hero_line2', __( 'Second line (appears while scrolling)', 'studio22' ) );
	$add_text( 'studio22_hero', 'hero_line3', __( 'Third line (appears while scrolling)', 'studio22' ) );
	$add_text( 'studio22_hero', 'hero_btn1', __( 'Main button', 'studio22' ) );
	$add_text( 'studio22_hero', 'hero_btn2', __( 'Second button', 'studio22' ) );
	$add_text( 'studio22_hero', 'marquee', __( 'Moving strip words (comma separated)', 'studio22' ), 'textarea' );

	/*
	 * Services.
	 */
	$wp_customize->add_section(
		'studio22_services',
		array(
			'title' => __( 'Services', 'studio22' ),
			'panel' => 'studio22',
		)
	);
	$add_text( 'studio22_services', 'services_kicker', __( 'Small title', 'studio22' ) );
	$add_text( 'studio22_services', 'services_title', __( 'Title', 'studio22' ) );
	$icons = array(
		'camera'  => __( 'Camera', 'studio22' ),
		'video'   => __( 'Video', 'studio22' ),
		'horse'   => __( 'Horse', 'studio22' ),
		'studio'  => __( 'Studio', 'studio22' ),
		'product' => __( 'Product', 'studio22' ),
		'edit'    => __( 'Editing', 'studio22' ),
		'drone'   => __( 'Drone', 'studio22' ),
		'event'   => __( 'Event', 'studio22' ),
	);
	for ( $i = 1; $i <= 6; $i++ ) {
		/* translators: %d: service number. */
		$n = sprintf( __( 'Service %d', 'studio22' ), $i );
		$add_option( 'studio22_services', "service{$i}_icon", $n . ' — ' . __( 'icon', 'studio22' ), 'select', array( 'choices' => $icons ) );
		$add_text( 'studio22_services', "service{$i}_title", $n . ' — ' . __( 'title', 'studio22' ) );
		$add_text( 'studio22_services', "service{$i}_text", $n . ' — ' . __( 'text', 'studio22' ), 'textarea' );
	}

	/*
	 * Work.
	 */
	$wp_customize->add_section(
		'studio22_work',
		array(
			'title'       => __( 'Portfolio', 'studio22' ),
			'panel'       => 'studio22',
			'description' => __( 'Projects are added from the "Projects" menu in the dashboard.', 'studio22' ),
		)
	);
	$add_text( 'studio22_work', 'work_kicker', __( 'Small title', 'studio22' ) );
	$add_text( 'studio22_work', 'work_title', __( 'Title', 'studio22' ) );
	$add_text( 'studio22_work', 'work_all', __( 'Button text', 'studio22' ) );
	$add_option(
		'studio22_work',
		'work_count',
		__( 'Projects shown on the home page', 'studio22' ),
		'number',
		array(
			'input_attrs' => array(
				'min' => 3,
				'max' => 24,
			),
		)
	);

	$add_option(
		'studio22_work',
		'instagram_feed',
		__( 'Instagram feed shortcode (optional)', 'studio22' ),
		'text',
		array( 'description' => __( 'Install the free "Smash Balloon Instagram Feed" plugin, connect the Instagram account and paste its shortcode here, e.g. [instagram-feed]. The latest Instagram posts are then shown under the portfolio.', 'studio22' ) )
	);

	/*
	 * Studio.
	 */
	$wp_customize->add_section(
		'studio22_studio',
		array(
			'title' => __( 'Studio & numbers', 'studio22' ),
			'panel' => 'studio22',
		)
	);
	$add_media( 'studio22_studio', 'studio_image', __( 'Image', 'studio22' ), 'image' );
	$add_text( 'studio22_studio', 'studio_kicker', __( 'Small title', 'studio22' ) );
	$add_text( 'studio22_studio', 'studio_title', __( 'Title', 'studio22' ) );
	$add_text( 'studio22_studio', 'studio_text', __( 'Text', 'studio22' ), 'textarea' );
	$add_text( 'studio22_studio', 'studio_more', __( 'Link to the About page', 'studio22' ) );
	for ( $i = 1; $i <= 4; $i++ ) {
		/* translators: %d: number index. */
		$n = sprintf( __( 'Number %d', 'studio22' ), $i );
		$add_option( 'studio22_studio', "stat{$i}_number", $n );
		$add_text( 'studio22_studio', "stat{$i}_label", $n . ' — ' . __( 'label', 'studio22' ) );
	}

	/*
	 * Founder.
	 */
	$wp_customize->add_section(
		'studio22_founder',
		array(
			'title'       => __( 'Founder (About page)', 'studio22' ),
			'panel'       => 'studio22',
			'description' => __( 'Shown on pages using the "About Studio22" template.', 'studio22' ),
		)
	);
	$add_media( 'studio22_founder', 'founder_photo', __( 'Founder photo', 'studio22' ), 'image' );
	$add_text( 'studio22_founder', 'founder_kicker', __( 'Small title', 'studio22' ) );
	$add_text( 'studio22_founder', 'founder_name', __( 'Name', 'studio22' ) );
	$add_text( 'studio22_founder', 'founder_role', __( 'Role', 'studio22' ) );
	$add_text( 'studio22_founder', 'founder_quote', __( 'Quote', 'studio22' ), 'textarea' );
	$add_text( 'studio22_founder', 'founder_bio', __( 'Biography', 'studio22' ), 'textarea' );

	/*
	 * Clients.
	 */
	$wp_customize->add_section(
		'studio22_clients',
		array(
			'title'       => __( 'Clients', 'studio22' ),
			'panel'       => 'studio22',
			'description' => __( 'Upload each client logo (PNG or SVG with a transparent background works best). Until a logo is uploaded, the client name is shown instead. Leave the name empty to hide a client.', 'studio22' ),
		)
	);
	$add_text( 'studio22_clients', 'clients_kicker', __( 'Small title', 'studio22' ) );
	$add_text( 'studio22_clients', 'clients_title', __( 'Title', 'studio22' ) );
	$add_option( 'studio22_clients', 'clients_color', __( 'Show logos in their original colours (otherwise they are shown in white)', 'studio22' ), 'checkbox' );
	for ( $i = 1; $i <= STUDIO22_CLIENTS; $i++ ) {
		/* translators: %d: client number. */
		$n = sprintf( __( 'Client %d', 'studio22' ), $i );
		$add_media( 'studio22_clients', "client{$i}_logo", $n . ' — ' . __( 'logo', 'studio22' ), 'image' );
		$add_text( 'studio22_clients', "client{$i}_name", $n . ' — ' . __( 'name', 'studio22' ) );
		$add_option( 'studio22_clients', "client{$i}_url", $n . ' — ' . __( 'website (optional)', 'studio22' ), 'url' );
	}

	/*
	 * Process.
	 */
	$wp_customize->add_section(
		'studio22_process',
		array(
			'title' => __( 'Process', 'studio22' ),
			'panel' => 'studio22',
		)
	);
	$add_text( 'studio22_process', 'process_kicker', __( 'Small title', 'studio22' ) );
	$add_text( 'studio22_process', 'process_title', __( 'Title', 'studio22' ) );
	for ( $i = 1; $i <= 4; $i++ ) {
		/* translators: %d: step number. */
		$n = sprintf( __( 'Step %d', 'studio22' ), $i );
		$add_text( 'studio22_process', "step{$i}_title", $n . ' — ' . __( 'title', 'studio22' ) );
		$add_text( 'studio22_process', "step{$i}_text", $n . ' — ' . __( 'text', 'studio22' ), 'textarea' );
	}

	/*
	 * Contact.
	 */
	$wp_customize->add_section(
		'studio22_contact',
		array(
			'title' => __( 'Contact & booking', 'studio22' ),
			'panel' => 'studio22',
		)
	);
	$add_option( 'studio22_contact', 'whatsapp', __( 'WhatsApp number with country code (e.g. +974 5555 5555)', 'studio22' ) );
	$add_option( 'studio22_contact', 'phone', __( 'Phone', 'studio22' ) );
	$add_option( 'studio22_contact', 'email', __( 'Email', 'studio22' ), 'email' );
	$add_option( 'studio22_contact', 'map', __( 'Google Maps place or address', 'studio22' ) );
	$add_option(
		'studio22_contact',
		'form_shortcode',
		__( 'Contact form shortcode (optional)', 'studio22' ),
		'text',
		array( 'description' => __( 'E.g. a Contact Form 7 or WPForms shortcode. When empty, the form sends the request on WhatsApp.', 'studio22' ) )
	);
	$add_text( 'studio22_contact', 'contact_kicker', __( 'Small title', 'studio22' ) );
	$add_text( 'studio22_contact', 'contact_title', __( 'Title', 'studio22' ) );
	$add_text( 'studio22_contact', 'address', __( 'Address', 'studio22' ) );
	$add_text( 'studio22_contact', 'hours', __( 'Opening hours', 'studio22' ) );
	$add_text( 'studio22_contact', 'wa_message', __( 'Pre-filled WhatsApp message', 'studio22' ) );
	$add_text( 'studio22_contact', 'cta_title', __( 'Banner title', 'studio22' ) );
	$add_text( 'studio22_contact', 'cta_text', __( 'Banner text', 'studio22' ) );
	$add_text( 'studio22_contact', 'cta_btn', __( 'Banner button', 'studio22' ) );

	/*
	 * Social & footer.
	 */
	$wp_customize->add_section(
		'studio22_social',
		array(
			'title' => __( 'Social networks & footer', 'studio22' ),
			'panel' => 'studio22',
		)
	);
	foreach ( studio22_social_networks() as $slug => $label ) {
		$add_option( 'studio22_social', "social_{$slug}", $label, 'url' );
	}
	$add_text( 'studio22_social', 'footer_text', __( 'Footer text', 'studio22' ), 'textarea' );
}
add_action( 'customize_register', 'studio22_customize_register' );

/**
 * Checkbox sanitizer.
 *
 * @param mixed $value Value.
 * @return bool
 */
function studio22_sanitize_checkbox( $value ) {
	return (bool) $value;
}
