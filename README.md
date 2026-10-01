# We Gravel Morocco – website work

- `homepage-redesign/` – source of the new homepage (wegravelmorocco.com, page ID 3247).
  Run `python3 build.py` inside the folder to regenerate `elementor-data.json`
  (the value stored in the page's `_elementor_data` meta). Previews use placeholder images.
- `backups/wegravelmorocco/home-elementor-data-before-redesign.json` – the previous
  homepage `_elementor_data`, to restore the old design if needed.

## Epic Travel Morocco (epictravelmorocco.com) – `epictravel/`
Moroccan-style redesign (zellige patterns, arch frames, 8-point-star itinerary timeline).
- `python3 build.py 3639 3640` → `out/<post_id>.json` = `_elementor_data` for each page/tour
  (3639 = shared header template incl. CSS, 3640 = footer template incl. icon sprite).
- Pages use the `elementor_canvas` template; tours (post type `tour`) too — their original
  `post_content` is untouched, so deleting `_elementor_edit_mode` restores the old tour page.
- `tours_*.py` = the 15 programs (same facts/wording as the live site), `site.css` = design system.
- `backups/home-862-elementor-data.json` = old homepage.
