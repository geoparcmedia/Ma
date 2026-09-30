(function () {
	var d = document, W = window;
	d.documentElement.classList.add('s22-js');

	// header gets a background once the page scrolls
	var head = d.querySelector('.s22-header');
	function solid() { if (head) head.classList.toggle('is-solid', W.scrollY > 40); }
	W.addEventListener('scroll', solid, { passive: true }); solid();

	// mobile menu
	var burger = d.querySelector('.s22-burger'), menu = d.getElementById('s22-menu');
	if (burger && menu) {
		burger.addEventListener('click', function () {
			var open = burger.getAttribute('aria-expanded') !== 'true';
			burger.setAttribute('aria-expanded', open); menu.hidden = !open;
			head.classList.add('is-solid');
		});
		menu.addEventListener('click', function (e) {
			if (e.target.closest('a')) { burger.setAttribute('aria-expanded', 'false'); menu.hidden = true; }
		});
	}

	// sections fade in when they come on screen
	var items = d.querySelectorAll('.s22-head, .s22-service, .s22-work-item, .s22-work-empty, .s22-about > *, .s22-steps li, .s22-book > *, .s22-card');
	if ('IntersectionObserver' in W) {
		var io = new IntersectionObserver(function (es) {
			es.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } });
		}, { rootMargin: '0px 0px -8% 0px' });
		items.forEach(function (el, i) { el.classList.add('s22-rv'); el.style.transitionDelay = (i % 4) * 80 + 'ms'; io.observe(el); });
	}

	// booking form: build a WhatsApp message from the fields
	var f = d.querySelector('.s22-form');
	if (f) {
		f.addEventListener('submit', function (e) {
			e.preventDefault();
			var wa = f.getAttribute('data-wa'), lines = [f.getAttribute('data-intro'), ''];
			f.querySelectorAll('input, select, textarea').forEach(function (el) {
				var v = (el.value || '').trim();
				if (v) lines.push(el.name + ': ' + v);
			});
			var url = 'https://wa.me/' + wa + '?text=' + encodeURIComponent(lines.join('\n'));
			W.open(url, '_blank', 'noopener');
		});
	}
})();
