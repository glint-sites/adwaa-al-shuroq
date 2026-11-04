import test from 'node:test';import assert from 'node:assert/strict';import {readFile,stat} from 'node:fs/promises';
const slugs=['gypsum-ceilings','painting','interior-decoration','flooring-cladding','renovation-finishing'];
for(const lang of ['en','ar'])for(const slug of slugs)test(`${lang}/${slug}: complete page and matching language destination`,async()=>{
 const path=(lang==='ar'?'ar/':'')+'services/'+slug+'/index.html';const html=await readFile(path,'utf8');
 assert.equal((html.match(/<h1[ >]/g)||[]).length,1);assert(html.includes(`lang="${lang}"`));assert(!html.includes('class="preview-strip"'));assert(!html.includes('data-buy'));
 const other=(lang==='en'?'/ar':'')+'/services/'+slug+'/';const link=html.match(/<a\b[^>]*data-lang-switch[^>]*>/)?.[0];assert(link?.includes(`href="${other}"`),'Language link must remain on same service');
 assert(html.includes(`https://glintsites.com/adwaa-al-shuroq/${lang==='ar'?'ar/':''}services/${slug}/`));
 assert(html.includes('name="location"'));assert(html.includes('instagram.com/design._decor'));assert(html.includes('data-default-service='));
 for(const m of html.matchAll(/href="(\/(?:ar\/)?services\/[^"?#]+)"/g))await stat('.'+m[1]+'index.html');
});

test('all twelve editions have working local links, anchors and assets',async()=>{
 const pages=['index.html','ar/index.html',...['en','ar'].flatMap(lang=>slugs.map(slug=>(lang==='ar'?'ar/':'')+'services/'+slug+'/index.html'))];
 const contents=new Map(await Promise.all(pages.map(async p=>[p,await readFile(p,'utf8')])));
 for(const [page,html]of contents){
  const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);assert.equal(ids.length,new Set(ids).size,`${page}: duplicate id`);
  for(const [,href]of html.matchAll(/(?:href|src)="([^\"]+)"/g)){
   if(!href.startsWith('/')&&!href.startsWith('#'))continue;
   const pathname='/'+page.replace(/index.html$/,'');const u=new URL(href,'https://preview.test'+pathname);let file=u.pathname.slice(1);if(!file||file.endsWith('/'))file+='index.html';await stat(file);
   if(u.hash){const target=contents.get(file)||await readFile(file,'utf8');assert(target.includes(`id="${u.hash.slice(1)}"`),`${page}: missing ${href}`)}
  }
 }
});
