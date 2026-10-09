# allinmarrakech.com – new site (EN + FR)

- `programs.py` – the 16 programs (6 multi-day tours, 10 day trips) in English and French, with prices
  (reference prices + €20) and destination photos (Wikimedia Commons, credits on the About page).
- `site.py` – builds every page; run `python3 site.py` → `out/<slug>.html` and `out/blocks/*.html`.
- `style.css` – the shared design, stored in WordPress as Additional CSS (custom_css post 1911).
- `blocks.json` – IDs of the synced blocks (header / booking form / footer, EN + FR) that every page includes.
- `preview.py` – local preview with placeholder images (the live images are blocked from this sandbox).

WordPress IDs: EN pages 1921–1942 (home 1942), FR pages 1943–1964 (home 1964, slug `fr`).
Booking forms (Contact Form 7): EN 1909, FR 1910 – both send to allinmarrakechtravel@gmail.com.
Pages use the "Elementor Canvas" template with one Custom HTML block, so the old theme header/footer is not used.
