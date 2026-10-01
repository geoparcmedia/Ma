# We Gravel Morocco – website work

- `homepage-redesign/` – source of the new homepage (wegravelmorocco.com, page ID 3247).
  Run `python3 build.py` inside the folder to regenerate `elementor-data.json`
  (the value stored in the page's `_elementor_data` meta). Previews use placeholder images.
- `backups/wegravelmorocco/home-elementor-data-before-redesign.json` – the previous
  homepage `_elementor_data`, to restore the old design if needed.

## Atlas2Sahara (atlas2sahara.com)

- `atlas2sahara-theme/` – custom WordPress theme (English, text logo): homepage with hero,
  experience types, filterable tours, why-us, destinations, how-it-works and CTA; `Tour`
  post type with duration/difficulty/price/style/region/highlights; six starter tours are
  created on first activation. Hero image, texts and contact details: Appearance → Customize →
  Atlas2Sahara options.
- `atlas2sahara-theme.zip` – the same theme, ready for Appearance → Themes → Add New → Upload.
