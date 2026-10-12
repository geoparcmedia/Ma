# We Gravel Morocco – website work

- `homepage-redesign/` – source of the new homepage (wegravelmorocco.com, page ID 3247).
  Run `python3 build.py` inside the folder to regenerate `elementor-data.json`
  (the value stored in the page's `_elementor_data` meta). Previews use placeholder images.
- `backups/wegravelmorocco/home-elementor-data-before-redesign.json` – the previous
  homepage `_elementor_data`, to restore the old design if needed.
- `seo-content/category_guides.py` – adds an intro text block and a "Plan Your Trip" guides
  section to the Cycling (3493) and Trekking (498) pages → `*_elementor_guides.json` (live since 2026-10-12).
- `seo-content/home_guides.py` – same guides section on the homepage after the FAQ →
  `home_elementor_guides.json` (live since 2026-10-12). The pre-change homepage data is
  `homepage-redesign/elementor-data.json` (also copied to `backups/wegravelmorocco/home-elementor-data-2026-10-12.json`).
- `seo-content/guide_links.py` – blocks added to the 5 travel guides: "More guides" links on each,
  plus quick answer, trip comparison table and FAQ (with FAQPage schema) on the Toubkal guide (4007).
