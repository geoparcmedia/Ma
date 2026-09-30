<?php
/**
 * All text of the one-page site, in English and Arabic.
 * Founder facts come from the existing studio22.qa Team page.
 */

if (!defined('ABSPATH')) {
	exit;
}

function s22_content() {
	static $c = null;
	if ($c !== null) {
		return $c;
	}
	$c = array(
		'en' => array(
			'meta_title' => 'Studio22 | Photography & Video Production in Qatar',
			'meta_desc' => 'Studio22 is a creative photography and video production studio in Doha, Qatar: event coverage, corporate productions and brand campaigns, led by photographer Abdulaziz Alajmi.',
			'nav' => array('services' => 'Services', 'work' => 'Work', 'about' => 'About', 'process' => 'Process', 'contact' => 'Contact'),
			'book' => 'Book a shoot',
			'lang_switch' => 'العربية',
			'hero_eyebrow' => 'Photography & video production · Qatar',
			'hero_title' => 'We turn moments into <em>stories</em>.',
			'hero_text' => 'Studio22 is a creative production studio in Doha. We photograph and film events, companies and brands across Qatar, with the care of a small team and the quality of a big one.',
			'hero_cta' => 'Book a shoot',
			'hero_cta2' => 'See our work',
			'services_eyebrow' => 'What we do',
			'services_title' => 'Photo and video, from brief to final cut',
			'services' => array(
				array('icon' => 'event', 't' => 'Event coverage', 'd' => 'Conferences, launches, weddings and private celebrations, covered in photo and video so nothing important is missed.'),
				array('icon' => 'corp', 't' => 'Corporate productions', 'd' => 'Company films, interviews, team portraits and behind-the-scenes content that show who you are.'),
				array('icon' => 'brand', 't' => 'Brand campaigns', 'd' => 'Concept, shooting and editing for campaigns and commercials that make people stop and look.'),
				array('icon' => 'social', 't' => 'Social media content', 'd' => 'Reels, short videos and photo sets made for Instagram, TikTok and YouTube, ready to post.'),
			),
			'work_eyebrow' => 'Selected work',
			'work_title' => 'Recent projects',
			'work_labels' => array('Events', 'Corporate', 'Brand campaign', 'Portrait', 'Behind the scenes', 'Social content'),
			'work_more' => 'More on Instagram',
			'work_empty' => 'Our latest projects are on Instagram.',
			'about_eyebrow' => 'About us',
			'about_title' => 'Led by Abdulaziz Alajmi',
			'about_role' => 'Founder · Photographer & videographer',
			'about_p1' => 'Abdulaziz Alajmi is a Qatari professional photographer, videographer and visual storyteller with extensive experience in creative production.',
			'about_p2' => 'As the founder of Studio22, he leads the creative vision of the studio and makes sure every project meets the highest standards of quality, creativity and professionalism.',
			'about_p3' => 'He has worked on a wide range of projects across Qatar, including corporate productions, brand campaigns and major events.',
			'about_follow' => 'Follow on Instagram',
			'process_eyebrow' => 'How we work',
			'process_title' => 'Simple, from first message to delivery',
			'process' => array(
				array('t' => 'Brief', 'd' => 'Tell us about your event, brand or idea, your date and what you need.'),
				array('t' => 'Plan', 'd' => 'We suggest the approach, team and schedule, and send you a clear quote.'),
				array('t' => 'Shoot', 'd' => 'Our team captures the day or the campaign, on location or in studio.'),
				array('t' => 'Deliver', 'd' => 'You receive edited photos and videos, ready to share and publish.'),
			),
			'book_eyebrow' => 'Book a shoot',
			'book_title' => 'Tell us about your project',
			'book_text' => 'Fill in the form and send it to us on WhatsApp. We will get back to you with availability and a quote.',
			'f_name' => 'Your name',
			'f_service' => 'Service',
			'f_date' => 'Date',
			'f_place' => 'Location',
			'f_details' => 'Details',
			'f_details_ph' => 'Type of event or project, number of guests, photo, video or both…',
			'f_send' => 'Send on WhatsApp',
			'f_or' => 'or email us',
			'f_other' => 'Other',
			'f_msg_intro' => 'Hello Studio22, I would like to book a shoot.',
			'contact_eyebrow' => 'Contact',
			'contact_title' => 'Let’s create something together',
			'c_phone' => 'Phone',
			'c_whatsapp' => 'WhatsApp',
			'c_email' => 'Email',
			'c_instagram' => 'Instagram',
			'c_location' => 'Location',
			'location' => 'Doha, Qatar',
			'footer' => 'Photography & video production in Qatar.',
			'rights' => 'All rights reserved.',
		),
		'ar' => array(
			'meta_title' => 'ستوديو22 | تصوير فوتوغرافي وإنتاج فيديو في قطر',
			'meta_desc' => 'ستوديو22 استوديو إبداعي للتصوير الفوتوغرافي وإنتاج الفيديو في الدوحة، قطر: تغطية الفعاليات، والإنتاجات المؤسسية، والحملات الإعلانية، بقيادة المصور عبدالعزيز العجمي.',
			'nav' => array('services' => 'خدماتنا', 'work' => 'أعمالنا', 'about' => 'من نحن', 'process' => 'طريقة العمل', 'contact' => 'تواصل معنا'),
			'book' => 'احجز جلسة تصوير',
			'lang_switch' => 'English',
			'hero_eyebrow' => 'تصوير فوتوغرافي وإنتاج فيديو · قطر',
			'hero_title' => 'نحوّل اللحظات إلى <em>قصص</em>.',
			'hero_text' => 'ستوديو22 استوديو إنتاج إبداعي في الدوحة. نصوّر الفعاليات والشركات والعلامات التجارية في جميع أنحاء قطر، باهتمام فريق صغير وجودة فريق كبير.',
			'hero_cta' => 'احجز جلسة تصوير',
			'hero_cta2' => 'شاهد أعمالنا',
			'services_eyebrow' => 'ماذا نقدّم',
			'services_title' => 'تصوير وفيديو، من الفكرة حتى المونتاج النهائي',
			'services' => array(
				array('icon' => 'event', 't' => 'تغطية الفعاليات', 'd' => 'المؤتمرات وحفلات الإطلاق والأعراس والمناسبات الخاصة، بالصور والفيديو حتى لا تفوتك أي لحظة مهمة.'),
				array('icon' => 'corp', 't' => 'الإنتاجات المؤسسية', 'd' => 'أفلام تعريفية للشركات، ومقابلات، وصور للفرق، ومحتوى من خلف الكواليس يعكس هويتكم.'),
				array('icon' => 'brand', 't' => 'الحملات الإعلانية', 'd' => 'الفكرة والتصوير والمونتاج لحملات وإعلانات تلفت الانتباه.'),
				array('icon' => 'social', 't' => 'محتوى وسائل التواصل', 'd' => 'ريلز وفيديوهات قصيرة ومجموعات صور مخصّصة لإنستغرام وتيك توك ويوتيوب، جاهزة للنشر.'),
			),
			'work_eyebrow' => 'مختارات من أعمالنا',
			'work_title' => 'أحدث المشاريع',
			'work_labels' => array('فعاليات', 'شركات', 'حملة إعلانية', 'بورتريه', 'خلف الكواليس', 'محتوى رقمي'),
			'work_more' => 'المزيد على إنستغرام',
			'work_empty' => 'أحدث مشاريعنا على إنستغرام.',
			'about_eyebrow' => 'من نحن',
			'about_title' => 'بقيادة عبدالعزيز العجمي',
			'about_role' => 'المؤسس · مصوّر فوتوغرافي ومصوّر فيديو',
			'about_p1' => 'عبدالعزيز العجمي مصوّر فوتوغرافي ومصوّر فيديو وراوٍ بصري قطري محترف، يمتلك خبرة واسعة في الإنتاج الإبداعي.',
			'about_p2' => 'بصفته مؤسس ستوديو22، يقود الرؤية الإبداعية للاستوديو ويحرص على أن يلبّي كل مشروع أعلى معايير الجودة والإبداع والاحترافية.',
			'about_p3' => 'عمل على مجموعة واسعة من المشاريع في جميع أنحاء قطر، منها الإنتاجات المؤسسية والحملات الإعلانية والفعاليات الكبرى.',
			'about_follow' => 'تابعنا على إنستغرام',
			'process_eyebrow' => 'طريقة العمل',
			'process_title' => 'خطوات بسيطة، من أول رسالة حتى التسليم',
			'process' => array(
				array('t' => 'الفكرة', 'd' => 'أخبرنا عن فعاليتك أو علامتك التجارية أو فكرتك، والتاريخ، وما تحتاجه.'),
				array('t' => 'التخطيط', 'd' => 'نقترح الأسلوب والفريق والجدول الزمني، ونرسل لك عرض سعر واضحًا.'),
				array('t' => 'التصوير', 'd' => 'يلتقط فريقنا يومك أو حملتك، في الموقع أو في الاستوديو.'),
				array('t' => 'التسليم', 'd' => 'تستلم الصور والفيديوهات بعد المونتاج، جاهزة للمشاركة والنشر.'),
			),
			'book_eyebrow' => 'احجز جلسة تصوير',
			'book_title' => 'أخبرنا عن مشروعك',
			'book_text' => 'املأ النموذج وأرسله إلينا عبر واتساب، وسنرد عليك بالمواعيد المتاحة وعرض السعر.',
			'f_name' => 'الاسم',
			'f_service' => 'الخدمة',
			'f_date' => 'التاريخ',
			'f_place' => 'الموقع',
			'f_details' => 'التفاصيل',
			'f_details_ph' => 'نوع الفعالية أو المشروع، عدد الضيوف، صور أو فيديو أو كلاهما…',
			'f_send' => 'أرسل عبر واتساب',
			'f_or' => 'أو راسلنا بالبريد',
			'f_other' => 'أخرى',
			'f_msg_intro' => 'مرحبًا ستوديو22، أرغب في حجز جلسة تصوير.',
			'contact_eyebrow' => 'تواصل معنا',
			'contact_title' => 'لنصنع شيئًا مميزًا معًا',
			'c_phone' => 'الهاتف',
			'c_whatsapp' => 'واتساب',
			'c_email' => 'البريد الإلكتروني',
			'c_instagram' => 'إنستغرام',
			'c_location' => 'الموقع',
			'location' => 'الدوحة، قطر',
			'footer' => 'تصوير فوتوغرافي وإنتاج فيديو في قطر.',
			'rights' => 'جميع الحقوق محفوظة.',
		),
	);
	return $c;
}

function s22_t($key, $lang = null) {
	$c = s22_content();
	$lang = $lang ? $lang : s22_lang();
	return isset($c[$lang][$key]) ? $c[$lang][$key] : (isset($c['en'][$key]) ? $c['en'][$key] : '');
}
