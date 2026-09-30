# Epic Travel Morocco – new home page (zellij design)

- `build.py` → `elementor-data.json` (value of `_elementor_data` for the page) and `preview.html`.
- Live as a draft page: "Home (new design)", ID 3648 on epictravelmorocco.com (template `elementor_header_footer`).
  The current home page (ID 862, "Home 03") is untouched. To switch: Settings → Reading → Homepage → "Home (new design)".
- Zellij tiles (8-point khatam) are drawn by a small inline script into CSS variables `--zb --zc --zt --zd`.
- The HTML has no double quotes or backslashes on purpose (WordPress unslashes meta on save).
- Tours, photos, texts and contacts come from the live site. Reviews: `[trustindex no-registration=tripadvisor]`.
