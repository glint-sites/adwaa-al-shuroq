import test from 'node:test';import assert from 'node:assert/strict';import {readFile,stat} from 'node:fs/promises';
for(const lang of ['en','ar'])test(`${lang}: locally hosted videos have motion and playback controls`,async()=>{
 const s=await readFile(lang==='ar'?'ar/index.html':'index.html','utf8');const hero=s.match(/<video\b[^>]*class="hero-video"[^>]*>/)?.[0];assert(hero,'Hero video exists');assert(hero.includes('muted')&&hero.includes('playsinline')&&hero.includes('loop'));assert(!hero.includes('autoplay'),'Autoplay policy handled by motion-aware enhancement');assert(s.includes('data-media-toggle'));assert(s.includes('id="project-film"'));const project=s.match(/<video\b[^>]*data-media-key="renovation"[^>]*>/)?.[0];assert(project?.includes('controls'));assert(!s.includes('fbcdn.net'),'No expiring Instagram CDN URLs in pages');
 for(const file of ['assets/media/design-reel-smooth.mp4','assets/media/renovation-reel.mp4'])assert((await stat(file)).size<4000000);
});
