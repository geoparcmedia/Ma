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
