# Epic Travel Morocco – footer templates before the redesign (30 Sep 2026)

Values of `_elementor_data` (as returned by the API, JSON string literals) for the Elementor footer templates.
To restore one: `json.loads()` the line and write the result back to the template's `_elementor_data`.

## 3436 – copyright bar
"[{\"id\":\"3d1b3e42\",\"elType\":\"container\",\"settings\":{\"flex_direction\":\"column\",\"boxed_width\":{\"unit\":\"px\",\"size\":1400,\"sizes\":[]},\"padding\":{\"unit\":\"px\",\"top\":\"35\",\"right\":\"10\",\"bottom\":\"38\",\"left\":\"10\",\"isLinked\":false},\"padding_tablet\":{\"unit\":\"px\",\"top\":\"35\",\"right\":\"10\",\"bottom\":\"38\",\"left\":\"10\",\"isLinked\":false},\"background_background\":\"classic\",\"background_color\":\"#FFF9F0\"},\"elements\":[{\"id\":\"21be86a8\",\"elType\":\"container\",\"settings\":{\"container_type\":\"grid\",\"presetTitle\":\"Grid\",\"presetIcon\":\"eicon-container-grid\",\"content_width\":\"full\",\"grid_columns_grid\":{\"unit\":\"fr\",\"size\":2,\"sizes\":[]},\"grid_rows_grid\":{\"unit\":\"fr\",\"size\":1,\"sizes\":[]},\"grid_gaps\":{\"column\":\"25\",\"row\":\"25\",\"isLinked\":true,\"unit\":\"px\"},\"grid_align_items\":\"center\",\"padding\":{\"unit\":\"px\",\"top\":\"0\",\"right\":\"0\",\"bottom\":\"0\",\"left\":\"0\",\"isLinked\":false}},\"elements\":[{\"id\":\"306c4e0c\",\"elType\":\"container\",\"settings\":{\"container_type\":\"grid\",\"presetTitle\":\"Grid\",\"presetIcon\":\"eicon-container-grid\",\"content_width\":\"full\",\"grid_columns_grid\":{\"unit\":\"fr\",\"size\":1,\"sizes\":[]},\"grid_rows_grid\":{\"unit\":\"fr\",\"size\":1,\"sizes\":[]},\"padding\":{\"unit\":\"px\",\"top\":\"0\",\"right\":\"0\",\"bottom\":\"0\",\"left\":\"0\",\"isLinked\":false}},\"elements\":[{\"id\":\"328d6e25\",\"elType\":\"widget\",\"settings\":{\"title\":\"Copyright \\u00a9 2025  EPICTRAVELMOOCCO All Rights Reserved.\",\"typography_typography\":\"custom\",\"typography_font_family\":\"Poppins\",\"typography_font_size\":{\"unit\":\"px\",\"size\":16,\"sizes\":[]},\"typography_font_weight\":\"400\",\"title_color\":\"#113A74\",\"align_mobile\":\"left\",\"typography_line_height_tablet\":{\"unit\":\"px\",\"size\":26,\"sizes\":[]},\"typography_line_height_mobile\":{\"unit\":\"px\",\"size\":\"\",\"sizes\":[]}},\"elements\":[],\"widgetType\":\"heading\"}],\"isInner\":true},{\"id\":\"5d85e6e7\",\"elType\":\"container\",\"settings\":{\"container_type\":\"grid\",\"presetTitle\":\"Grid\",\"presetIcon\":\"eicon-container-grid\",\"content_width\":\"full\",\"grid_columns_grid\":{\"unit\":\"fr\",\"size\":1,\"sizes\":[]},\"grid_rows_grid\":{\"unit\":\"fr\",\"size\":1,\"sizes\":[]},\"padding\":{\"unit\":\"px\",\"top\":\"0\",\"right\":\"0\",\"bottom\":\"0\",\"left\":\"0\",\"isLinked\":false}},\"elements\":[],\"isInner\":true}],\"isInner\":true}],\"isInner\":false}]"

## 3433 – main footer (summary)
Grid of 4 columns: logo PDF-2-1.png (ID 3206); "Say Hello" epictravelmorocco@gmail.com, +(1) 579 484 7707, +(212) 661 292 596;
"Subscribe newsletter" [contact-form-7 id="a4499c9" title="footer email"], "By subscribing, you’re accept Privacy Policy",
social icons (facebook.com/epictravelmorocco, instagram.com/epictravelmorocco, Tripadvisor d25394757);
"Quick links": Home (/), Destination (/destination/), Contact us (/contact/), Abou us (/about/).
Fonts Philosopher / Poppins, colours #113A74 on #FFF9F0 style, border #DEE2E6.
The full original JSON is also kept by WordPress in the template's revisions if the editor saved it; otherwise rebuild from this summary.

## Page 1360 "Contact us" (/contact-2/) – before redesign (summary)
Template elementor_header_footer. Sections: banner (bg pexels-zakariahanif-12214734-scaled.jpg, "Let’s Start Planning",
"Don’t hesitate to reach out — whether it’s a fully-crafted itinerary or just a question about one of our tours, we’re ready to help.
Your Moroccan adventure starts here."); 3 icon boxes (address "Marrakech , Gueliz 22000, MOROCCO"; phones "+(1) 579 484 7707 / +(212) 661 292 596";
email epictravelmorocco@gmail.com); "Get in touch" + "We’d love to hear from you! Whether you’re ready to embark on a tailored Moroccan adventure,
have questions about one of our tours, or just want to explore options — we’re here."; Google map "marrakech" (350px);
form [contact-form-7 id="f402750" title="Main Contact"]; widget travelor-tour-slider-two-widget (Explore More, 4 tours).

## Page 1360 Contact – first redesign (1 Oct 2026)
Rebuilt by `epic-home/contact.py` (git history keeps every version of contact-1360.json).

## Page 69 "Destination" (/destination/) – before redesign (exact _elementor_data)
[{"id":"4c2043e","elType":"container","settings":{"flex_direction":"column"},"elements":[{"id":"eb9e0bf","elType":"widget","settings":{"button_text":"Explore More","total":"-1"},"elements":[],"widgetType":"travelor-tour-grid-widget"}],"isInner":false}]

## Page 1247 "About Us" (/about-us/) – before redesign (summary)
1. Banner: bg pexels-henrik-le-botos-1588507-3878114-scaled.jpg (id 3340), heading "About Us", spacers 95px.
2. travelor-theme-about-one-widget: subtitle "About Us", title "Your epic Moroccan adventure awaits.", description "At Epic Travel Morocco, we’re passionate about one thing crafting journeys…",
   button "explore more" → /destination/, images WhatsApp-Image-2023-03-27-at-22.53.18-1.jpeg (3266) and pexels-piotr-arnoldes-7862031-6441048-scaled.jpg (3228);
   section bg ChatGPT-Image-7-nov.-2025-02_34_35.png (3294) with white overlay .91, padding 140/130.
3. Row: left 50% headings (#5C828F) + texts "Who We Are", "Our Offerings", "Our Story" (texts in the page content); right 50% bg pexels-reyyan-505450018-33429795-scaled.jpg (3214).

## Page 1334 "Our fleet" (/fleet/) – before redesign (summary)
1. Banner bg Gemini_Generated_Image_vvja03vvja03vvja.png (3554), html "Our fleet" (animated gradient text), min-height 505.
2. html banner "CAR RENTAL WITH DRIVER / Tailored Travel Transport Service in Morocco" + long text, on bg ChatGPT-Image-Nov-7-2025-05_03_56-PM.png (3355) overlay white .92.
3. Four rows image + card: Gemini_Generated_Image_kunskunskunskuns-2.png (3573) "Mercedes Mini Van" 2–7 passengers;
   Gemini_Generated_Image_tqr8vttqr8vttqr8.png (3575) "Toyota SUV" ("from 2 up to 2 passengers" as written);
   Gemini_Generated_Image_pelh0jpelh0jpelh.png (3576) "Mercedes Sprinter Minibus" 8–17; Gemini_Generated_Image_wnw2hgwnw2hgwnw2.png (3588) "Big Buses" 18–48.

## Page settings changed on 1 Oct 2026
- Page 69: `_wp_page_template` was `templates/template-destination.php`, now `elementor_header_footer`.
- Pages 69, 1247, 1334, 1360: `travelor_page_container_options.page_spacing_top` and `page_spacing_bottom` were "120", now "0"
  (the theme added 120px empty space above and below the content).

## Site-wide header/footer moved to a widget (1 Oct 2026, later)
Templates 3433/3436 turned out not to be rendered by the theme, so the header/footer block (`epic-home/chrome-widget.html`)
is now a Custom HTML widget: option `widget_custom_html[2]`, placed in `sidebars_widgets` areas footer-widget, footer-widget-two
and footer-widget-three (all three were empty before). To undo: set those three areas back to [] .
Templates 3433 and 3436 were emptied (their previous content is in git: epic-home/footer-3433.json history).
