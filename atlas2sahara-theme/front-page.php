<?php
get_header();
$hero_image = get_theme_mod( 'a2s_hero_image' );
$types      = get_terms( array( 'taxonomy' => 'tour_type', 'hide_empty' => false ) );
$type_info  = array(
	'biking' => array( 'bike', 'Gravel, mountain and e-bike routes over Atlas passes and desert tracks.' ),
	'hiking' => array( 'hike', 'Summits, valleys and village-to-village walks with mountain guides.' ),
	'desert' => array( 'desert', 'Camel caravans, 4x4 crossings and nights in Sahara camps.' ),
);
?>

<section class="hero<?php echo $hero_image ? ' has-image' : ''; ?>"<?php echo $hero_image ? ' style="background-image:url(' . esc_url( $hero_image ) . ')"' : ''; ?>>
	<?php if ( ! $hero_image ) : ?>
		<svg class="hero-art" viewBox="0 0 1440 800" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
			<defs>
				<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b1a3d"/><stop offset=".55" stop-color="#c2553a"/><stop offset="1" stop-color="#f2a65a"/></linearGradient>
			</defs>
			<rect width="1440" height="800" fill="url(#sky)"/>
			<circle cx="1080" cy="420" r="90" fill="#ffd28a" opacity=".85"/>
			<path d="M0 470 180 300 300 400 470 220 640 410 760 330 930 460 1100 290 1260 400 1440 310V800H0z" fill="#5a2f3d" opacity=".9"/>
			<path d="m470 220 40 40-25-5-15 25-20-30-20 10z" fill="#f4ece2" opacity=".85"/>
			<path d="m1100 290 35 35-22-4-13 20-18-24-17 8z" fill="#f4ece2" opacity=".85"/>
			<path d="M0 600c200-90 380-100 560-40s360 70 520 0 260-60 360-20V800H0z" fill="#b5532f"/>
			<path d="M0 690c260-70 520-60 760-10s440 40 680-20V800H0z" fill="#d9874a"/>
		</svg>
	<?php endif; ?>
	<div class="hero-overlay"></div>
	<div class="container hero-content">
		<p class="eyebrow light">Morocco adventure tours</p>
		<h1><?php echo esc_html( a2s_opt( 'a2s_hero_title' ) ); ?></h1>
		<p class="lead"><?php echo esc_html( a2s_opt( 'a2s_hero_subtitle' ) ); ?></p>
		<div class="hero-actions">
			<a class="btn" href="#tours">Explore tours</a>
			<a class="btn btn-ghost" href="#contact">Tailor-made trip</a>
		</div>
	</div>
	<a class="scroll-cue" href="#experiences" aria-label="Scroll down"><span></span></a>
</section>

<section class="section" id="experiences">
	<div class="container">
		<div class="section-head">
			<p class="eyebrow">Choose your adventure</p>
			<h2>Three ways to discover Morocco</h2>
		</div>
		<div class="type-grid">
			<?php
			if ( ! is_wp_error( $types ) ) :
				foreach ( $types as $type ) :
					$info = isset( $type_info[ $type->slug ] ) ? $type_info[ $type->slug ] : array( 'map', $type->description );
					?>
					<a class="type-card reveal media-<?php echo esc_attr( $type->slug ); ?>" href="<?php echo esc_url( get_term_link( $type ) ); ?>">
						<span class="type-icon"><?php echo a2s_icon( $info[0] ); ?></span>
						<h3><?php echo esc_html( $type->name ); ?></h3>
						<p><?php echo esc_html( $type->description ? $type->description : $info[1] ); ?></p>
						<span class="link-arrow">See <?php echo esc_html( strtolower( $type->name ) ); ?> tours <?php echo a2s_icon( 'arrow' ); ?></span>
					</a>
					<?php
				endforeach;
			endif;
			?>
		</div>
	</div>
</section>

<section class="section section-sand" id="tours">
	<div class="container">
		<div class="section-head split">
			<div>
				<p class="eyebrow">Featured tours</p>
				<h2>Trips our guests love</h2>
			</div>
			<div class="filters" role="tablist">
				<button class="filter is-active" data-filter="all">All</button>
				<?php
				if ( ! is_wp_error( $types ) ) {
					foreach ( $types as $type ) {
						printf( '<button class="filter" data-filter="%s">%s</button>', esc_attr( $type->slug ), esc_html( $type->name ) );
					}
				}
				?>
			</div>
		</div>
		<div class="tour-grid">
			<?php
			$tours = new WP_Query( array(
				'post_type'      => 'tour',
				'posts_per_page' => 9,
				'orderby'        => array( 'menu_order' => 'ASC', 'date' => 'DESC' ),
			) );
			if ( $tours->have_posts() ) :
				while ( $tours->have_posts() ) :
					$tours->the_post();
					get_template_part( 'template-parts/tour-card' );
				endwhile;
				wp_reset_postdata();
			else :
				echo '<p class="muted">Tours are coming soon. Add them under Tours → Add new tour.</p>';
			endif;
			?>
		</div>
		<p class="center"><a class="btn btn-outline" href="<?php echo esc_url( get_post_type_archive_link( 'tour' ) ); ?>">See all tours</a></p>
	</div>
</section>

<section class="section" id="why">
	<div class="container why">
		<div class="why-intro reveal">
			<p class="eyebrow">Why Atlas2Sahara</p>
			<h2>Local know-how, every kilometre of the way</h2>
			<p class="muted">We live between the mountains and the desert. Every route is one we have ridden or walked ourselves, with the families, cooks and drivers we work with all year round.</p>
		</div>
		<div class="why-grid">
			<div class="why-item reveal"><?php echo a2s_icon( 'guide' ); ?><h3>Local guides</h3><p>Certified Moroccan guides who speak English, French and Tamazight.</p></div>
			<div class="why-item reveal"><?php echo a2s_icon( 'map' ); ?><h3>Tested routes</h3><p>Hand-picked trails and tracks, with GPS files for self-guided trips.</p></div>
			<div class="why-item reveal"><?php echo a2s_icon( 'shield' ); ?><h3>Full support</h3><p>Luggage transfers, support vehicles and 24/7 help while you travel.</p></div>
			<div class="why-item reveal"><?php echo a2s_icon( 'leaf' ); ?><h3>Responsible travel</h3><p>Small groups, family guesthouses and fair pay for local teams.</p></div>
		</div>
	</div>
</section>

<section class="section section-dark" id="destinations">
	<div class="container">
		<div class="section-head">
			<p class="eyebrow light">Where we go</p>
			<h2>From snowy peaks to golden dunes</h2>
		</div>
		<div class="dest-grid">
			<div class="dest reveal dest-1"><span>01</span><h3>Marrakech &amp; Agafay</h3><p>Red-walled medina, then the stony desert just an hour away.</p></div>
			<div class="dest reveal dest-2"><span>02</span><h3>High Atlas</h3><p>Toubkal, Berber villages and passes above 2,000 m.</p></div>
			<div class="dest reveal dest-3"><span>03</span><h3>Draa &amp; Dadès valleys</h3><p>Palm oases, kasbahs and dramatic gorges.</p></div>
			<div class="dest reveal dest-4"><span>04</span><h3>The Sahara</h3><p>The dunes of Erg Chebbi and Erg Chegaga under the stars.</p></div>
		</div>
	</div>
</section>

<section class="section" id="how">
	<div class="container">
		<div class="section-head">
			<p class="eyebrow">How it works</p>
			<h2>Your trip in three steps</h2>
		</div>
		<ol class="steps">
			<li class="reveal"><span class="step-num">1</span><h3>Pick a tour</h3><p>Choose a ready-made trip or tell us what you dream of doing.</p></li>
			<li class="reveal"><span class="step-num">2</span><h3>We tailor it</h3><p>Dates, pace, guided or self-guided, hotels and extras: we shape it around you.</p></li>
			<li class="reveal"><span class="step-num">3</span><h3>Enjoy Morocco</h3><p>We meet you on arrival and take care of every detail until you fly home.</p></li>
		</ol>
	</div>
</section>

<section class="cta" id="contact">
	<div class="container cta-inner reveal">
		<div>
			<h2>Ready for your Moroccan adventure?</h2>
			<p>Tell us your dates and interests. We reply within 24 hours with a free, no-obligation proposal.</p>
		</div>
		<div class="cta-actions">
			<?php if ( a2s_opt( 'a2s_email' ) ) : ?>
				<a class="btn" href="mailto:<?php echo esc_attr( a2s_opt( 'a2s_email' ) ); ?>?subject=Trip%20enquiry"><?php echo a2s_icon( 'mail' ); ?> Email us</a>
			<?php endif; ?>
			<?php if ( a2s_opt( 'a2s_phone' ) ) : ?>
				<a class="btn btn-ghost" href="https://wa.me/<?php echo esc_attr( preg_replace( '/\D/', '', a2s_opt( 'a2s_phone' ) ) ); ?>"><?php echo a2s_icon( 'phone' ); ?> WhatsApp</a>
			<?php endif; ?>
			<?php if ( ! a2s_opt( 'a2s_email' ) && ! a2s_opt( 'a2s_phone' ) ) : ?>
				<a class="btn" href="<?php echo esc_url( get_post_type_archive_link( 'tour' ) ); ?>">Browse all tours</a>
			<?php endif; ?>
		</div>
	</div>
</section>

<?php
get_footer();
