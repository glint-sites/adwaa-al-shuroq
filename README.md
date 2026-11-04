# Adwaa Al Shuroq Contracting
Bilingual English/Arabic preview for Adwaa Al Shuroq Contracting & Decoration, Jubail. Static HTML, local fonts and client imagery. Run npm run build to validate and assemble dist. Deploy with npx wrangler deploy in the Glint account. No dependencies required for build. Regeneration: python scripts/generate.py (BeautifulSoup4 and requests required).

Sources: leads-20261027-2156.csv matched via ahmadqader00966@gmail.com; https://shuroqmuqawalat.com/ confirms brand, services, phone, email, hours and Eastern Province coverage. CSV uses the alternate listing name Design Contracting. Gallery and service interior photos are clean full-resolution originals from the company website. Hero and painting-service images are AI-generated illustrative visuals, labelled in both editions; no invented project names, testimonials, metrics or client endorsements. Assets are retained solely for this client preview.

Preview route: https://glintsites.com/adwaa-al-shuroq/ and /ar/. Language transitions follow Lift Arabia and Binary System patterns. No backend: the labelled enquiry form opens WhatsApp with the user's message. Preview carries noindex; review indexing, domain, contact details and photo rights before production handover.

Image provenance and source dimensions: assets/image-sources.json. Removed screenshot-based and watermarked imagery; original service photos retained at 1200px+ source resolution.


## Sales preview experience
`python scripts/generate.py` uses `scripts/polish.py` for the localized service journey, renovation feature, project lightbox, process, FAQ and navigation. Edit `css/polish.css` for the presentation refinements. All five service enquiry links select the corresponding form option, which survives language changes. Mobile visitors have fixed call and free-site-visit actions. The previously tested preview strip and sales dialog have been removed at the user’s request. Build checks include the five enquiry mappings, three gallery controls and the image viewer in each language.


## Complete service editions
Five detail routes are available in English and Arabic under `/services/` and `/ar/services/`: gypsum-ceilings, painting, interior-decoration, flooring-cladding, renovation-finishing. Verified scopes come from the matching five service pages on shuroqmuqawalat.com; the source slug is retained in scripts/services.py. This includes exterior paints, Jotun paint options, wallpaper, parquet/SPC, porcelain/marble, residential annexes, plumbing, electrical work and plastering. Do not infer licensing, approvals, fixed guarantees or pricing from these descriptions. Instagram links use the exact design._decor account listed on the original site.

Run `python scripts/generate.py`, `npm test`, and `npm run build`. Route tests verify all ten service pages, reciprocal language links, local links, anchors and assets across twelve pages. Build does not require Python; generated pages are tracked. The site-visit form includes optional project location, preserved across language switches and included in the message the visitor reviews in WhatsApp. The selected service defaults to the page being viewed.


## Project video
The homepage uses a high-quality still architectural concept as its hero background. The locally hosted 16-second company design reel plays in a compact desktop panel so its 720p source is never stretched across the viewport. The panel is hidden on mobile; the renovation film remains available below. An 8.4-second original renovation sequence appears on the homepage and renovation service pages with native playback controls. Both are from the company's Instagram, retrieved through the user's authorized Glint browser session; stable original post links and encoding details are in `assets/media/sources.json`. No expiring CDN URLs or Instagram embeds are shipped. The two videos total under 4 MB; they contain no audio tracks. Design-reel playback respects reduced-motion and data-saver preferences, pauses offscreen/in hidden tabs, and has a persistent manual pause choice during language swaps. The renovation film is click-to-play and pauses offscreen. Posters are real frames from the corresponding clips. Media lifecycle is isolated in js/media.js and css/media.css.

The hero is re-edited from the original 12-second Instagram source: five-second scene pacing, one-second dissolves, and a cyclic dissolve between the last and first scene. Delivery uses design-reel-smooth.mp4 so returning visitors receive the corrected video.

Hero concept: 1672×941 native output, WebP quality 98, capped at native CSS width on wide displays. Painting illustration: 1536×1024, WebP quality 98, no people. Client gallery photos use the exact original uploaded WebP files without an extra lossy encoding step.
