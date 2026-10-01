# Epic Travel Morocco – new home page (zellij design)

- `build.py` → `elementor-data.json` (value of `_elementor_data` for the page) and `preview.html`.
- Live home page: page ID 3648 "Home" on epictravelmorocco.com (template `elementor_header_footer`), set as `page_on_front`; menu item 3366 points to it.
  The previous home page (ID 862, "Home 03") is still published; to go back: Settings → Reading → Homepage → "Home 03".
- Zellij tiles (8-point khatam) are drawn by a small inline script into CSS variables `--zb --zc --zt --zd`.
- The HTML has no double quotes or backslashes on purpose (WordPress unslashes meta on save).
- Tours, photos, texts and contacts come from the live site. Reviews: `[trustindex no-registration=tripadvisor]`.
- Banner: stays fixed (sticky) while the page slides over it. Video: upload an MP4 to Media with the title
  "hero-video"; the page finds it through the REST API (`/wp-json/wp/v2/media?search=hero-video`) and plays it
  muted in a loop over the photos. No video → the two photos keep cross-fading.
- Banner "film": 6 site photos with slow zoom/drift (Ken Burns), cross-fading every 6.5 s, with place captions and
  progress bars. Header: own fixed header (logo PDF-2-1.png, menu, phone, "Plan my trip", mobile drawer); on load
  the script hides the theme header (elements near the top of the page with the destination/contact links).
- Zellij kept subtle: plain cream sections, thin tile bands (10px / 6px), very faint pattern on teal and dark sections, none over the banner.
- After changing `_elementor_data` directly, delete `_elementor_element_cache` and `_elementor_css` on the page (Elementor caches the rendered page for 24 h), then save the post so LiteSpeed purges it.
- `footer.py` → `footer-3433.json` (main footer template: new footer + the new header, injected on every page that has no home banner) and `copyright-3436.json`. Old versions: `backups/epictravelmorocco/footer-templates-before-redesign.md`.


## Inner pages, header and footer – chic Moroccan style (1 Oct 2026)
- `chic.py`: shared design (Cormorant Garamond + Jost, ink / gold / paper), arched image frames, khatam star ornaments, faint rosette watermark.
- `footer.py` -> footer-3433.json (fixed header on every page except the home page, footer, newsletter form) and copyright-3436.json.
  The header is plain HTML (shows without JavaScript); the mobile menu uses a CSS checkbox.
- `contact.py` -> contact-1360.json; `pages.py` -> about-1247.json, fleet-1334.json, tours-69.json.
- Previews in `previews/`. Each page is also set to the `elementor_header_footer` template with the theme spacing (page_spacing_top/bottom) at 0.
- Deploy: write the JSON to `_elementor_data`, delete `_elementor_element_cache` and `_elementor_css`, re-save the post title, then LiteSpeed Purge All.
- The Tours page lists 10 tours by hand (it no longer uses the theme's automatic tour grid): add new tours in `pages.py` (TOURS).

### Update: header/footer on every page + tour programme pages
- The theme does not render Elementor templates 3433/3436, so `footer.py` now writes `chrome-widget.html`, stored as the
  Custom HTML widget `custom_html-2` in the theme footer widget areas. It shows on every page (pages, tours, blog).
- Its script moves the header/footer to <body>, hides the theme header and footer, hides the home page's old header,
  and on tour pages (/all-tour/...) rebuilds the programme from the tour content (.itinerary .day-title / .day-content):
  hero, Overview (duration, start, end), Route, Day by day itinerary with a booking card, and an enquiry section.
  New tours written in the same format get the design automatically.
- Deploy the widget: wp_update_option widget_custom_html {"2":{"title":"","content":<chrome-widget.html>},"_multiwidget":1}.
