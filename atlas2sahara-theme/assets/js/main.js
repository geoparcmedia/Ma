( function () {
	document.documentElement.classList.add( 'js' );

	// Header turns solid after scrolling past the hero.
	var header = document.querySelector( '.site-header' );
	function onScroll() {
		if ( header ) {
			header.classList.toggle( 'is-scrolled', window.scrollY > 60 );
		}
	}
	window.addEventListener( 'scroll', onScroll, { passive: true } );
	onScroll();

	// Mobile menu.
	var toggle = document.querySelector( '.nav-toggle' );
	var nav = document.getElementById( 'site-nav' );
	if ( toggle && nav ) {
		toggle.addEventListener( 'click', function () {
			var open = nav.classList.toggle( 'is-open' );
			document.body.classList.toggle( 'nav-open', open );
			toggle.setAttribute( 'aria-expanded', open ? 'true' : 'false' );
		} );
		nav.addEventListener( 'click', function ( e ) {
			if ( e.target.closest( 'a' ) ) {
				nav.classList.remove( 'is-open' );
				document.body.classList.remove( 'nav-open' );
				toggle.setAttribute( 'aria-expanded', 'false' );
			}
		} );
	}

	// Tour filters on the homepage.
	var filters = document.querySelectorAll( '.filter' );
	filters.forEach( function ( btn ) {
		btn.addEventListener( 'click', function () {
			var value = btn.getAttribute( 'data-filter' );
			filters.forEach( function ( b ) { b.classList.toggle( 'is-active', b === btn ); } );
			document.querySelectorAll( '#tours .tour-card' ).forEach( function ( card ) {
				card.classList.toggle( 'is-hidden', value !== 'all' && card.getAttribute( 'data-type' ) !== value );
			} );
		} );
	} );

	// Fade sections in as they scroll into view.
	var items = document.querySelectorAll( '.reveal' );
	if ( 'IntersectionObserver' in window ) {
		var io = new IntersectionObserver( function ( entries ) {
			entries.forEach( function ( entry ) {
				if ( entry.isIntersecting ) {
					entry.target.classList.add( 'is-visible' );
					io.unobserve( entry.target );
				}
			} );
		}, { threshold: 0.12 } );
		items.forEach( function ( el ) { io.observe( el ); } );
	} else {
		items.forEach( function ( el ) { el.classList.add( 'is-visible' ); } );
	}
} )();
