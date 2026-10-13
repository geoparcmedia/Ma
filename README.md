# We Gravel Morocco – website work

- `homepage-redesign/` – source of the new homepage (wegravelmorocco.com, page ID 3247).
  Run `python3 build.py` inside the folder to regenerate `elementor-data.json`
  (the value stored in the page's `_elementor_data` meta). Previews use placeholder images.
- `backups/wegravelmorocco/home-elementor-data-before-redesign.json` – the previous
  homepage `_elementor_data`, to restore the old design if needed.

## Amasir Voyage (amasirvoyage.com)

- `media/amasir/` – guest photos (resized, metadata stripped), uploaded to the Media Library (IDs 8550–8554).
- `backups/amasir/*.json` – `_elementor_data` of Home (8276), About (8277), Contact (8279),
  header (38) and footer (41) before the October 2026 update.
- `amasir/build.py` – builds the updated `_elementor_data` into `amasir/out/`.
  When writing a value with the MCP `wp_update_post_meta` tool, double every backslash first
  (WordPress unslashes meta values). `out/custom-full.css` is the site's Additional CSS (post 7424).
- Full redesign (Oct 2026): `amasir/design.css` + `amasir/redesign.py` build header (38), footer (41),
  Home (8276), About (8277), Contact (8279) and Activities (8533) into `amasir/out2/`.
  Global header switched from 35 to 38 and theme colours changed in option `travolo_opt`
  (original in `backups/amasir/travolo_opt.json`).
