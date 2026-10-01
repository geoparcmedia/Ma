/**
 * Studio22 theme scripts. No dependencies.
 */
(function () {
	'use strict';

	var doc = document.documentElement;
	var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
	var settings = window.studio22 || { whatsapp: '', labels: {} };

	doc.classList.add('js');

	function clamp(value, min, max) {
		return Math.min(max, Math.max(min, value));
	}

	/* Header state on scroll
	   ---------------------------------------------------------------------- */
	var header = document.getElementById('site-header');
	function onScrollHeader() {
		if (header) {
			header.classList.toggle('is-scrolled', window.scrollY > 40);
		}
	}
	window.addEventListener('scroll', onScrollHeader, { passive: true });
	onScrollHeader();

	/* Mobile menu
	   ---------------------------------------------------------------------- */
	var toggle = document.querySelector('.nav-toggle');
	var nav = document.getElementById('main-nav');
	function closeMenu() {
		document.body.classList.remove('nav-open');
		if (toggle) {
			toggle.setAttribute('aria-expanded', 'false');
		}
	}
	if (toggle && nav) {
		toggle.addEventListener('click', function () {
			var open = document.body.classList.toggle('nav-open');
			toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
		});
		nav.addEventListener('click', function (event) {
			if (event.target.closest('a')) {
				closeMenu();
			}
		});
		document.addEventListener('keydown', function (event) {
			if ('Escape' === event.key) {
				closeMenu();
			}
		});
	}

	/* Hero: pinned while scrolling, video follows the scroll
	   ---------------------------------------------------------------------- */
	var hero = document.querySelector('.hero');
	if (hero) {
		var mode = hero.getAttribute('data-mode');
		var pinned = hero.classList.contains('hero--pinned') && !reduceMotion;
		var video = hero.querySelector('.hero__video');
		var steps = Array.prototype.slice.call(hero.querySelectorAll('.hero__step'));
		var target = 0;
		var current = 0;
		var duration = 0;
		var ticking = false;
		var scrub = pinned && 'scrub' === mode && video;

		if (video && reduceMotion) {
			video.removeAttribute('autoplay');
			video.pause();
		}

		var progress = function () {
			var rect = hero.getBoundingClientRect();
			var total = hero.offsetHeight - window.innerHeight;
			return total > 0 ? clamp(-rect.top / total, 0, 1) : 0;
		};

		var setStep = function (p) {
			if (steps.length < 2) {
				return;
			}
			// Keep the last 10% of the scroll for the final line to breathe.
			var index = Math.min(steps.length - 1, Math.floor((p / 0.9) * steps.length));
			steps.forEach(function (step, i) {
				step.classList.toggle('is-active', i === index);
				step.classList.toggle('is-past', i < index);
			});
		};

		var render = function () {
			ticking = false;
			if (scrub && duration) {
				current += (target - current) * 0.18;
				if (Math.abs(target - current) < 0.01) {
					current = target;
				}
				if (!video.seeking) {
					video.currentTime = current;
				}
				if (current !== target) {
					requestTick();
				}
			}
		};

		var requestTick = function () {
			if (!ticking) {
				ticking = true;
				window.requestAnimationFrame(render);
			}
		};

		var update = function () {
			var p = pinned ? progress() : 0;
			hero.style.setProperty('--p', p.toFixed(4));
			hero.classList.toggle('is-scrolling', window.scrollY > 60);
			if (pinned) {
				setStep(p);
			}
			if (scrub && duration) {
				// Stop a hair before the end: some browsers show a black frame at the very end.
				target = p * Math.max(0, duration - 0.05);
				requestTick();
			}
		};

		if (scrub) {
			video.pause();
			var setDuration = function () {
				duration = video.duration || 0;
				update();
			};
			if (video.readyState >= 1) {
				setDuration();
			} else {
				video.addEventListener('loadedmetadata', setDuration);
			}
			// iOS only allows seeking a video after it has been played once.
			var unlock = function () {
				var promise = video.play();
				if (promise && promise.then) {
					promise.then(function () {
						video.pause();
					}).catch(function () {});
				} else {
					video.pause();
				}
				window.removeEventListener('touchstart', unlock);
			};
			window.addEventListener('touchstart', unlock, { passive: true });
		}

		window.addEventListener('scroll', update, { passive: true });
		window.addEventListener('resize', update);
		update();

		// Save battery: pause the looping video when the hero is off screen.
		if (video && !scrub && 'IntersectionObserver' in window && !reduceMotion) {
			new IntersectionObserver(function (entries) {
				entries.forEach(function (entry) {
					if (entry.isIntersecting) {
						var promise = video.play();
						if (promise && promise.catch) {
							promise.catch(function () {});
						}
					} else {
						video.pause();
					}
				});
			}).observe(hero);
		}
	}

	/* Reveal on scroll + counters
	   ---------------------------------------------------------------------- */
	function countUp(el) {
		var end = parseInt(el.getAttribute('data-count'), 10);
		if (!end || reduceMotion) {
			return;
		}
		var suffix = el.querySelector('span');
		var textNode = el.firstChild;
		var start = null;
		var time = 1600;
		function frame(now) {
			if (!start) {
				start = now;
			}
			var t = clamp((now - start) / time, 0, 1);
			var eased = 1 - Math.pow(1 - t, 3);
			textNode.nodeValue = Math.round(end * eased).toLocaleString('en-US');
			if (t < 1) {
				window.requestAnimationFrame(frame);
			}
		}
		if (textNode && 3 === textNode.nodeType && suffix) {
			window.requestAnimationFrame(frame);
		}
	}

	var revealItems = document.querySelectorAll('.reveal');
	if ('IntersectionObserver' in window) {
		var observer = new IntersectionObserver(function (entries) {
			entries.forEach(function (entry) {
				if (!entry.isIntersecting) {
					return;
				}
				entry.target.classList.add('is-visible');
				var counter = entry.target.querySelector('[data-count]');
				if (counter) {
					countUp(counter);
				}
				observer.unobserve(entry.target);
			});
		}, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
		revealItems.forEach(function (item) {
			observer.observe(item);
		});
	} else {
		revealItems.forEach(function (item) {
			item.classList.add('is-visible');
		});
	}

	/* Portfolio filters
	   ---------------------------------------------------------------------- */
	document.querySelectorAll('.filters').forEach(function (group) {
		var scope = group.closest('section') || document;
		var cards = scope.querySelectorAll('.project-card');
		group.addEventListener('click', function (event) {
			var button = event.target.closest('.filter');
			if (!button) {
				return;
			}
			var filter = button.getAttribute('data-filter');
			group.querySelectorAll('.filter').forEach(function (b) {
				var active = b === button;
				b.classList.toggle('is-active', active);
				b.setAttribute('aria-pressed', active ? 'true' : 'false');
			});
			cards.forEach(function (card) {
				var types = (card.getAttribute('data-type') || '').split(' ');
				card.classList.toggle('is-hidden', '*' !== filter && -1 === types.indexOf(filter));
			});
		});
	});

	/* Lightbox for project images and videos
	   ---------------------------------------------------------------------- */
	var lightbox = document.getElementById('lightbox');
	if (lightbox) {
		var stage = lightbox.querySelector('.lightbox__stage');
		var closeButton = lightbox.querySelector('.lightbox__close');
		var lastFocus = null;

		var closeLightbox = function () {
			lightbox.hidden = true;
			stage.innerHTML = '';
			document.body.style.overflow = '';
			if (lastFocus) {
				lastFocus.focus();
			}
		};

		var openLightbox = function (type, src, title) {
			stage.innerHTML = '';
			var node;
			if ('iframe' === type) {
				node = document.createElement('div');
				node.className = 'ratio-16x9';
				var iframe = document.createElement('iframe');
				iframe.src = src;
				iframe.title = title || '';
				iframe.allow = 'autoplay; fullscreen; picture-in-picture';
				iframe.allowFullscreen = true;
				node.appendChild(iframe);
			} else if ('video' === type) {
				node = document.createElement('video');
				node.src = src;
				node.controls = true;
				node.autoplay = true;
				node.playsInline = true;
			} else {
				node = document.createElement('img');
				node.src = src;
				node.alt = title || '';
			}
			stage.appendChild(node);
			lightbox.hidden = false;
			document.body.style.overflow = 'hidden';
			closeButton.focus();
		};

		document.addEventListener('click', function (event) {
			var link = event.target.closest('[data-lightbox]');
			if (!link || event.metaKey || event.ctrlKey) {
				return;
			}
			event.preventDefault();
			lastFocus = link;
			var title = link.querySelector('.project-card__title');
			openLightbox(link.getAttribute('data-lightbox'), link.getAttribute('data-src'), title ? title.textContent : '');
		});

		closeButton.addEventListener('click', closeLightbox);
		lightbox.addEventListener('click', function (event) {
			if (event.target === lightbox || event.target === stage) {
				closeLightbox();
			}
		});
		document.addEventListener('keydown', function (event) {
			if ('Escape' === event.key && !lightbox.hidden) {
				closeLightbox();
			}
		});
	}

	/* Booking form: sends the request on WhatsApp (or by email)
	   ---------------------------------------------------------------------- */
	document.querySelectorAll('[data-wa-form]').forEach(function (form) {
		form.addEventListener('submit', function (event) {
			event.preventDefault();
			var data = new FormData(form);
			var labels = settings.labels || {};
			var lines = [
				(labels.name || 'Name') + ': ' + (data.get('name') || ''),
				(labels.service || 'Service') + ': ' + (data.get('service') || '')
			];
			if (data.get('date')) {
				lines.push((labels.date || 'Date') + ': ' + data.get('date'));
			}
			lines.push('', data.get('message') || '');
			var text = lines.join('\n');

			if (settings.whatsapp) {
				window.open('https://wa.me/' + settings.whatsapp + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
			} else if (form.getAttribute('data-email')) {
				window.location.href = 'mailto:' + form.getAttribute('data-email') + '?subject=' + encodeURIComponent(data.get('service') || '') + '&body=' + encodeURIComponent(text);
			}
		});
	});
})();
