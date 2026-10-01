( function () {
	document.documentElement.classList.add( 'js' );

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

	// Reviews slider: one page of three cards (one on mobile) at a time.
	var track = document.querySelector( '.review-track' );
	var count = document.querySelector( '.slider-count' );
	if ( track ) {
		var page = 0;
		document.querySelectorAll( '.slider-nav [data-dir]' ).forEach( function ( btn ) {
			btn.addEventListener( 'click', function () {
				var pages = Math.max( 1, Math.ceil( track.scrollWidth / track.clientWidth - 0.01 ) );
				page = ( page + parseInt( btn.getAttribute( 'data-dir' ), 10 ) + pages ) % pages;
				track.scrollLeft = page * ( track.clientWidth + 24 );
				if ( count ) {
					count.textContent = ( page + 1 ) + ' / ' + pages;
				}
			} );
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
