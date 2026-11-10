# vaultmovement.fit — website v1

A static website: plain HTML, one stylesheet, one script and no build step. It deploys as-is from GitHub to Vercel.

## What's here
| Path | What it is |
|---|---|
| `index.html`, `journey.html`, `programmes/…`, `kids/…`, `more/…`, `story/…`, `locations/…` | The 38 pages. Vercel serves them at clean URLs (`/journey`, `/programmes/vault-12`). |
| `assets/css/site.css`, `assets/js/site.js` | Design system and behaviour: sticky header, hero sequence, click-to-load embeds, consent, analytics events. |
| `assets/brand`, `assets/characters`, `assets/og` | Logos (from the updated logo set), interim Vee & Mouve art, and the 1200×630 social image. |
| `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, `site.webmanifest` | Favicon and app icon set. |
| `robots.txt`, `sitemap.xml`, `llms.txt` | Search and AI-answer-engine files. |
| `vercel.json` | Clean URLs, security headers, caching, and 301 redirects from chennaiparkour.fit. |
| `404.html`, `thank-you.html` | Not-found page; Zoho thank-you page (noindex, fires `form_submit`). |
| `docs/` | Redirect CSV, meta title/description table, JSON-LD templates, open items, legacy photo list. Not deployed. |
| `_src/` | The generator that writes the pages. Not deployed. |

## Deploy
1. **Photos:** copy the old site's `assets/parkour`, `assets/schools`, `assets/corporate`, `assets/kaladi` and `assets/armed` folders into `assets/` (see `docs/legacy-photos.md`).
2. **Repo:** put these files at the root of the GitHub repo connected to Vercel. Commit and push.
3. **Vercel → Settings → Build & Development:**
   - Framework preset: **Other**
   - Build command: empty
   - Output directory: empty (repo root)
4. **Domains:**
   - In Vercel, add `vaultmovement.fit` and `www.vaultmovement.fit`, and set www to redirect to the apex domain.
   - At GoDaddy DNS, use the records Vercel shows. These are usually `A @ 76.76.21.21` and `CNAME www cname.vercel-dns.com`.
5. **Old domain (keep for at least 12 months):**
   - **Option A:** add `chennaiparkour.fit` and `www.chennaiparkour.fit` to this same Vercel project. `vercel.json` already 301-redirects every old page.
   - **Option B:** keep the old project, and replace its `vercel.json` with `docs/old-domain-vercel.json`.
6. **Zoho:** set the submit label, add the hidden fields and set the thank-you redirect (see `docs/OPEN-CONFIRM-ITEMS.md`, item 36).
7. **Analytics:** paste the GA4 and Meta Pixel IDs at the top of `assets/js/site.js`. They load only after a visitor accepts cookies.
8. **Search engines:**
   - Google Search Console and Bing Webmaster Tools: verify the domain and submit `https://vaultmovement.fit/sitemap.xml`.
   - In Search Console, use **Change of Address** for chennaiparkour.fit.

## Editing
- **Small text fix:** edit the HTML file directly.
- **Site-wide change** (header, footer, a fact used on many pages): edit `_src/lib.py` or the page content in `_src/pages_core.py` / `_src/pages_more.py`, then run `python3 _src/build.py` (Python 3, no packages needed) and commit the regenerated files.
- `_src/make_assets.py` rebuilds logos, icons and the social image from the logo source files. It needs Pillow and Playwright, and you'll rarely need it.
