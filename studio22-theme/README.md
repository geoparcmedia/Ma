# Studio22 – WordPress theme (studio22.qa)

Dark premium theme for Studio22 (photo & video production, Doha). English + Arabic (RTL).

## Install
1. WordPress → Appearance → Themes → Add New → Upload Theme → `studio22.zip` → Activate.
2. Settings → Permalinks → Save (once).
3. Arabic + English: install the free **Polylang** plugin, add English and Arabic,
   create the home page in both languages and set them as front page. The theme shows
   the Arabic texts and RTL layout automatically on Arabic pages.

## Edit content (Appearance → Customize → Studio22 theme)
- **Hero video banner**: upload the MP4, poster image, choose
  "Pinned — the video plays as you scroll". For a smooth effect export the video like:
  `ffmpeg -i in.mov -vf scale=1920:-2 -c:v libx264 -crf 24 -g 6 -an -movflags +faststart hero.mp4`
- **Clients**: upload the logos of Katara, Al Shaqab, Arabians Tour, Doha Bank, ACTA, KIAF
  (names are already filled; until a logo is uploaded the name is shown).
- **Founder (About page)**: Abdulaziz Al Ajmi, photo and bio are built in (EN + AR). The "About us" page is created automatically.
  Create a page "About us" and choose the template **About Studio22**.
- **Contact & booking**: WhatsApp number, phone, email, map.
- Portfolio: Dashboard → **Projects** → Add new (title, featured image, optional YouTube/Vimeo/MP4 link, project type).

Every text has an English and an Arabic field.

Rebuild the zip: `cd studio22-theme && zip -r studio22.zip studio22 -x "*.DS_Store"`
