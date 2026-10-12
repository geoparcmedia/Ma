# PiikoPlay SEO changes – 2026-10-12

Done through the WordPress connector (no theme/plugin files touched).

## noindex (Rank Math `rank_math_robots` = noindex, follow)
- 158 Most Played Games, 162 Most Popular Games – empty theme-demo pages from 2014,
  duplicates of /popular-games/
- 892 My Games – per-user page
- 618 Activity, 619 Members, 623 Groups – BuddyPress directory pages

## Deleted empty demo tags (0 posts each)
wordpress, theme, html5, gaming, games, great, slide, aventure, cars

## Rewrote copied GameMonetize descriptions (same structure as the other games:
intro, tips, controls, FAQ, internal links; facts only from the stored game data)
952 EPIC Escape from Barrys Prison, 953 Dead Rails, 954 99 Nights In The Forest,
955 Obby Tsunami Runner, 956 Obby Tower: Only Up!, 957 Obby +1 Double Jump,
958 Obby: Lucky Block Heist. The original developer texts are still in each
post's `mabp_description` / `mabp_instructions` meta.

## Checked, no change needed
- Search engine visibility on, SeedProd coming-soon/maintenance modes off
- Permalinks /%postname%/, Rank Math sitemap in robots.txt
- Tags, date archives, search and empty categories already noindex
- The other 88 games already have unique descriptions

## Not verifiable from here
Old /index.php/... URLs still in Google. WordPress normally 301-redirects them to
the /%postname%/ URL; check one in a browser (e.g. /index.php/category/horror/).
