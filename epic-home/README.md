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
