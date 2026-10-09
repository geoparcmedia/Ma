# We Gravel Morocco – website work

- `homepage-redesign/` – source of the new homepage (wegravelmorocco.com, page ID 3247).
  Run `python3 build.py` inside the folder to regenerate `elementor-data.json`
  (the value stored in the page's `_elementor_data` meta). Previews use placeholder images.
- `backups/wegravelmorocco/home-elementor-data-before-redesign.json` – the previous
  homepage `_elementor_data`, to restore the old design if needed.

## Atlas2Sahara (atlas2sahara.com)

- `atlas2sahara-theme/` – custom WordPress theme (English, text logo) laid out like
  hour-away.com: off-white page, grey tour cards with Book/Info, sage strip, "Why cycling /
  Why the Sahara" split rows, custom-holiday tiles, About panel over a photo, guest reviews
  slider (shown once reviews are added under Reviews), wide banner, Our Stories (latest
  posts) and a grey footer listing tours per type. Photos in `assets/img/` are the client's.
  Tours: `Tour` post type (duration/difficulty/price/style/region/highlights). Starter tours
  and three stories are created once (versioned via the `a2s_seed_version` option).
  Texts, images and contact details: Appearance → Customize → Atlas2Sahara options.
- `atlas2sahara-theme.zip` – the same theme, ready for Appearance → Themes → Add New → Upload.
- `atlas2sahara-elementor/build.py` – builds the homepage as native Elementor widgets
  (sections/columns with Heading, Text, Image, Button). Writes
  `atlas2sahara-theme/inc/elementor-home.json`, which the theme turns into an Elementor
  "Home" page (set as front page, plus a "Stories" posts page) as soon as Elementor is
  active, and `atlas2sahara-elementor/atlas2sahara-home-template.json` for manual import
  (Templates → Saved Templates → Import). Re-run `python3 build.py` after editing it.

## All in Marrakech (allinmarrakech.com)

- `allinmarrakech/build.py` – transport-first homepage (EN/FR) as Elementor data with full
  per-widget styling; `build_lite.py` – the compact version actually sent to the site
  (styling in one stylesheet inside an HTML widget, classes `aim2-*`). Draft pages on the
  site: 1965 "Home – Transport (EN)" and 1966 "Accueil – Transport (FR)". Prices = current
  site prices + 20 EUR. Previews use placeholder photos.
