# We Gravel Morocco – website work

- `homepage-redesign/` – source of the new homepage (wegravelmorocco.com, page ID 3247).
  Run `python3 build.py` inside the folder to regenerate `elementor-data.json`
  (the value stored in the page's `_elementor_data` meta). Previews use placeholder images.
- `backups/wegravelmorocco/home-elementor-data-before-redesign.json` – the previous
  homepage `_elementor_data`, to restore the old design if needed.
- `trip-pages/` – new layout of the 10 tour pages (WP Travel Engine trips): key facts, overview,
  highlights, route map (Leaflet, line per day: cycling / hiking / transfer), day-by-day itinerary,
  what's included, and a booking card moved into the sidebar. Run `python3 build.py` to regenerate
  `out/<trip id>.html` (the trip's `post_content`) and `out/shared.html` (CSS, script and icons, stored
  once as the synced pattern / `wp_block` ID 4048). Routes are in `routes.py` (approximate coordinates).
  The old trip `post_content` is in `backups/wegravelmorocco/trips-post-content-before-redesign.json`.
