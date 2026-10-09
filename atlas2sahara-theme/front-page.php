<?php
// A static front page built with Elementor is rendered by Elementor.
if ( 'page' === get_option( 'show_on_front' ) && a2s_is_elementor( (int) get_option( 'page_on_front' ) ) ) {
	get_template_part( 'template-parts/elementor-content' );
	return;
}
get_header();
$biking_link = get_term_link( 'biking', 'tour_type' );
$desert_link = get_term_link( 'desert', 'tour_type' );
$hiking_link = get_term_link( 'hiking', 'tour_type' );
$contact_url = a2s_opt( 'a2s_email' ) ? 'mailto:' . a2s_opt( 'a2s_email' ) . '?subject=' . rawurlencode( 'Custom holiday' ) : '#contact';
?>

<section class="hero" style="background-image:url(<?php echo esc_url( a2s_section_image( 'a2s_hero_image', 'riders.jpg' ) ); ?>)">
	<div class="hero-content">
		<h1><?php echo esc_html( a2s_opt( 'a2s_hero_title' ) ); ?></h1>
		<p><?php echo esc_html( a2s_opt( 'a2s_hero_subtitle' ) ); ?></p>
		<p><?php echo esc_html( a2s_opt( 'a2s_hero_note' ) ); ?></p>
		<a class="btn" href="#tours">View our tours</a>
	</div>
</section>

<div class="strip">
	<span class="strip-label">Atlas2Sahara</span>
	<span class="strip-text"><?php echo esc_html( a2s_opt( 'a2s_strip_text' ) ); ?></span>
</div>

<section class="section" id="tours">
	<div class="container">
		<header class="section-title">
			<h2><?php echo esc_html( a2s_opt( 'a2s_tours_title' ) ); ?></h2>
			<p><?php echo esc_html( a2s_opt( 'a2s_tours_subtitle' ) ); ?></p>
		</header>
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
				echo '<p>Add tours under Tours → Add new tour.</p>';
			endif;
			?>
		</div>
	</div>
</section>

<section class="why-band">
	<div class="container">
		<div class="split reveal">
			<div class="split-media"><img src="<?php echo esc_url( a2s_img( 'cyclist.jpg' ) ); ?>" alt="Cycling through the palm groves near Marrakech" loading="lazy"></div>
			<div class="split-text">
				<h2>Why Cycling in Morocco?</h2>
				<p>Cycling in Morocco offers a <strong>captivating</strong> and <strong>diverse experience</strong> for riders of <strong>all levels</strong>, from easy palm-grove loops to epic mountain passes.</p>
				<p>Sitting at <em>the gateway to Africa</em>, Morocco packs <strong>snow-capped peaks, desert tracks and green oases</strong> into a single trip, with quiet roads and a warm welcome in every village.</p>
				<p>From the <strong>Palmeraie of Marrakech</strong> to the <strong>passes of the High Atlas</strong>, here's why we think cycling in Morocco is a must-try.</p>
				<?php if ( ! is_wp_error( $biking_link ) ) : ?><a class="btn" href="<?php echo esc_url( $biking_link ); ?>">Learn more</a><?php endif; ?>
			</div>
		</div>
		<div class="split split-reverse reveal">
			<div class="split-media"><img src="<?php echo esc_url( a2s_img( 'camels.jpg' ) ); ?>" alt="Camel caravan walking towards the Sahara dunes" loading="lazy"></div>
			<div class="split-text">
				<h2>Why the Sahara Desert?</h2>
				<p>For those who love exploring on foot, the Sahara offers an experience that is as <strong>peaceful</strong> as it is <strong>unforgettable</strong>. Walk beside camel caravans across stony plains towards dunes that glow orange at sunset.</p>
				<p>From <strong>starlit desert camps</strong> to <strong>ancient kasbahs and oases</strong>, nomadic culture and endless silence make the desert a place you will want to return to.</p>
				<?php if ( ! is_wp_error( $desert_link ) ) : ?><a class="btn" href="<?php echo esc_url( $desert_link ); ?>">Learn more</a><?php endif; ?>
			</div>
		</div>
	</div>
</section>

<section class="section" id="contact">
	<div class="container">
		<header class="section-title">
			<h2>Your Custom Holidays</h2>
			<p><?php echo esc_html( a2s_opt( 'a2s_custom_text' ) ); ?></p>
			<a class="btn" href="<?php echo esc_url( $contact_url ); ?>">Contact us</a>
		</header>
		<div class="tile-grid">
			<a class="tile reveal" href="<?php echo esc_url( is_wp_error( $biking_link ) ? '#tours' : $biking_link ); ?>"><img src="<?php echo esc_url( a2s_img( 'riders-square.jpg' ) ); ?>" alt="" loading="lazy"><span>Cycling</span></a>
			<a class="tile reveal" href="<?php echo esc_url( is_wp_error( $desert_link ) ? '#tours' : $desert_link ); ?>"><img src="<?php echo esc_url( a2s_img( 'camels-square.jpg' ) ); ?>" alt="" loading="lazy"><span>Desert</span></a>
			<a class="tile reveal" href="<?php echo esc_url( is_wp_error( $hiking_link ) ? '#tours' : $hiking_link ); ?>"><img src="<?php echo esc_url( a2s_img( 'culture-square.jpg' ) ); ?>" alt="" loading="lazy"><span>Culture</span></a>
		</div>
	</div>
</section>

<section class="about" id="about" style="background-image:url(<?php echo esc_url( a2s_section_image( 'a2s_about_image', 'camels.jpg' ) ); ?>)">
	<div class="container">
		<div class="about-panel reveal">
			<div>
				<p class="kicker"><?php echo esc_html( a2s_opt( 'a2s_about_kicker' ) ); ?></p>
				<h2>About us</h2>
				<p><?php echo esc_html( a2s_opt( 'a2s_about_text' ) ); ?></p>
				<a class="btn" href="<?php echo esc_url( $contact_url ); ?>">Learn more</a>
			</div>
			<div>
				<p><?php echo esc_html( a2s_opt( 'a2s_about_text_2' ) ); ?></p>
			</div>
		</div>
	</div>
</section>

<?php
$reviews = get_posts( array( 'post_type' => 'review', 'numberposts' => 12 ) );
if ( $reviews ) :
	?>
	<section class="section" id="reviews">
		<div class="container">
			<header class="section-title">
				<h2>Loved By Our Guests</h2>
				<p>Here's what some of our guests have said about their Moroccan adventures.</p>
				<?php if ( count( $reviews ) > 3 ) : ?>
					<div class="slider-nav">
						<button class="circle-arrow" data-dir="-1" aria-label="Previous">‹</button>
						<span class="slider-count">1 / <?php echo (int) ceil( count( $reviews ) / 3 ); ?></span>
						<button class="circle-arrow" data-dir="1" aria-label="Next">›</button>
					</div>
				<?php endif; ?>
			</header>
			<div class="review-track">
				<?php foreach ( $reviews as $review ) : ?>
					<blockquote class="review">
						<div class="review-text"><?php echo wp_kses_post( wpautop( $review->post_content ) ); ?></div>
						<?php if ( $review->post_excerpt ) : ?><p class="review-tour"><?php echo esc_html( $review->post_excerpt ); ?></p><?php endif; ?>
						<cite><?php echo esc_html( $review->post_title ); ?></cite>
					</blockquote>
				<?php endforeach; ?>
			</div>
		</div>
	</section>
<?php endif; ?>

<div class="banner" style="background-image:url(<?php echo esc_url( a2s_section_image( 'a2s_banner_image', 'cyclist.jpg' ) ); ?>)"></div>

<?php
$stories = get_posts( array( 'post_type' => 'post', 'numberposts' => 3 ) );
if ( $stories ) :
	?>
	<section class="section" id="stories">
		<div class="container">
			<header class="section-title">
				<h2>Our Stories</h2>
				<p>Where stories come to life. Explore our travel notes and get inspired.</p>
			</header>
			<div class="tour-grid">
				<?php foreach ( $stories as $story ) : ?>
					<article class="story-card reveal">
						<a class="tour-media" href="<?php echo esc_url( get_permalink( $story ) ); ?>"><img src="<?php echo esc_url( a2s_post_photo( $story->ID ) ); ?>" alt="<?php echo esc_attr( get_the_title( $story ) ); ?>" loading="lazy"></a>
						<div class="tour-body">
							<p class="story-meta"><?php echo get_avatar( $story->post_author, 28 ); ?> <?php echo esc_html( get_the_author_meta( 'display_name', $story->post_author ) ); ?></p>
							<p class="story-date"><?php echo esc_html( get_the_date( 'D j M Y', $story ) ); ?></p>
							<h3><a href="<?php echo esc_url( get_permalink( $story ) ); ?>"><?php echo esc_html( get_the_title( $story ) ); ?></a></h3>
							<p class="tour-excerpt"><?php echo esc_html( get_the_excerpt( $story ) ); ?></p>
							<a class="info-link" href="<?php echo esc_url( get_permalink( $story ) ); ?>">Read <span class="circle-arrow">›</span></a>
						</div>
					</article>
				<?php endforeach; ?>
			</div>
			<?php
			$blog = get_option( 'page_for_posts' ) ? get_permalink( get_option( 'page_for_posts' ) ) : '';
			if ( $blog ) :
				?>
				<p class="center"><a class="btn btn-outline" href="<?php echo esc_url( $blog ); ?>">Read all stories</a></p>
			<?php endif; ?>
		</div>
	</section>
<?php endif; ?>

<?php
get_footer();
