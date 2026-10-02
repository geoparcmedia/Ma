# Morocco Sky Travel – website work (moroccoskytravel.com)

- `tours.py` – content of the 21 program pages (same facts as the original pages, rewritten).
- `build.py` – builds each page's Elementor data + SEO fields into `out/<page-id>.json`, and local previews in `preview/`.
- `style.css` – shared design system (`.mst-*` classes). Published minified in WordPress
  *Appearance > Customize > Additional CSS* (custom_css post 2976).
- `backups/` – original `_elementor_data` of the Home, Destinations and Day Trips pages.
- Booking form: Contact Form 7 #389 ("Trip request"), used on every program page and on Contact/Book.

Pages keep their URLs; only titles, content and SEO meta changed.
