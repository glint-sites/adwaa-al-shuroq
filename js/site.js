function initPage(isLanguageChange=false){
if(typeof initProjectMedia==='function')initProjectMedia();
const nav=document.getElementById('nav'),menu=document.querySelector('.menu');
function closeMenu(){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');nav.querySelectorAll('details').forEach(d=>d.open=false)}
menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open))});
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){closeMenu();menu.focus()}});
document.addEventListener('click',e=>{if(!nav.contains(e.target)&&!menu.contains(e.target))closeMenu()});
nav.querySelectorAll('details').forEach(details=>details.addEventListener('keydown',event=>{if(event.key==='Escape'){details.open=false;details.querySelector('summary').focus()}}));
const form=document.getElementById('enquiry');
try{const draft=JSON.parse(sessionStorage.getItem('adwaa-draft'));if(draft)for(const key of ['name','phone','location','details'])form.elements[key].value=draft[key]||'';if(draft&&Number.isInteger(draft.serviceIndex))form.elements.service.selectedIndex=draft.serviceIndex}catch{}
if(!isLanguageChange&&document.body.dataset.defaultService!==undefined)form.elements.service.selectedIndex=Number(document.body.dataset.defaultService);
form.addEventListener('input',()=>{try{sessionStorage.setItem('adwaa-draft',JSON.stringify({...Object.fromEntries(new FormData(form)),serviceIndex:form.elements.service.selectedIndex}))}catch{}});
form.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;const d=Object.fromEntries(new FormData(form));const title=document.documentElement.lang==='ar'?'طلب معاينة مجانية':'Free site visit enquiry';location.href='https://wa.me/966535056668?text='+encodeURIComponent(`${title}\n${d.name}\n${d.phone}\n${d.service}\n${d.location||''}\n${d.details}`)});

const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
if(!reduce&&!isLanguageChange&&'IntersectionObserver' in window){
 const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible');observer.unobserve(entry.target)}}),{threshold:.08});
 document.querySelectorAll('.section-heading,.service,.gallery figure,.about>div,.contact-grid>div,form,.process-grid article,.renovation-card,.faq-section' ).forEach((el,i)=>{el.classList.add('reveal');el.style.setProperty('--delay',`${Math.min(i%4,3)*65}ms`);observer.observe(el)});
}
document.querySelectorAll('[data-enquiry-service]').forEach(a=>a.addEventListener('click',()=>{form.elements.service.selectedIndex=Number(a.dataset.enquiryService);form.dispatchEvent(new Event('input',{bubbles:true}));}));
const galleryDialog=document.getElementById('gallery-dialog');
document.querySelectorAll('[data-gallery]').forEach(button=>button.addEventListener('click',()=>{const img=button.querySelector('img');galleryDialog.querySelector('img').src=img.src;galleryDialog.querySelector('img').alt=img.alt;galleryDialog.querySelector('p').textContent=button.closest('figure').querySelector('figcaption strong').textContent;galleryDialog.showModal();}));
document.querySelectorAll('dialog').forEach(dialog=>{dialog.querySelector('[data-close]').addEventListener('click',()=>dialog.close());dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close()}})});
const language=document.querySelector('[data-lang-switch]');
const preload=()=>loadLanguage(language.href).catch(()=>{});
language.addEventListener('pointerenter',preload,{once:true});language.addEventListener('focus',preload,{once:true});
language.addEventListener('click',async e=>{
 if(e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.defaultPrevented)return;
 e.preventDefault();if(languageBusy)return;languageBusy=true;language.setAttribute('aria-busy','true');
 const href=language.href;
 try{await changeLanguage(href,true)}catch{location.href=href}finally{languageBusy=false}
});
}
const languageCache=new Map();let languageBusy=false;
function loadLanguage(href){
 const url=new URL(href,location.href);url.hash='';
 if(!languageCache.has(url.href))languageCache.set(url.href,fetch(url.href).then(async response=>{if(!response.ok)throw Error('Language unavailable');return new DOMParser().parseFromString(await response.text(),'text/html')}).catch(error=>{languageCache.delete(url.href);throw error}));
 return languageCache.get(url.href);
}
async function changeLanguage(href,push){
 const next=await loadLanguage(href);
 await Promise.all([document.fonts.load('400 16px Plex'),document.fonts.load('400 16px Archivo')]);
 const sections=[...document.querySelectorAll('main>section')];const top=document.getElementById('site-header').offsetHeight+(document.querySelector('.preview-strip')?.offsetHeight||0);
 let index=sections.findIndex(s=>s.getBoundingClientRect().bottom>top);if(index<0)index=0;
 const ratio=Math.min(1,Math.max(0,(top-sections[index].getBoundingClientRect().top)/sections[index].offsetHeight));const atTop=scrollY<5;
 const swap=()=>{
  document.documentElement.classList.add('language-changing');
  document.documentElement.lang=next.documentElement.lang;document.documentElement.dir=next.documentElement.dir;
  document.title=next.title;document.body.innerHTML=next.body.innerHTML;
  for(const rel of ['canonical']){const source=next.querySelector(`link[rel="${rel}"]`),target=document.querySelector(`link[rel="${rel}"]`);if(source&&target)target.href=source.href}
  const description=next.querySelector('meta[name="description"]');if(description)document.querySelector('meta[name="description"]').content=description.content;
  if(push)history.pushState({},'',href);
  initPage(true);
  document.querySelector('[data-lang-switch]').focus({preventScroll:true});
  const block=document.querySelectorAll('main>section')[index];
  scrollTo({top:atTop?0:Math.max(0,block.getBoundingClientRect().top+scrollY+ratio*block.offsetHeight-document.getElementById('site-header').offsetHeight-(document.querySelector('.preview-strip')?.offsetHeight||0)),behavior:'instant'});
 };
 const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
 if(document.startViewTransition&&!reduce){const transition=document.startViewTransition(swap);try{await transition.finished}catch{}finally{document.documentElement.classList.remove('language-changing')}}else{swap();document.documentElement.classList.remove('language-changing')}
}
window.addEventListener('popstate',()=>{if(document.documentElement.lang!==(location.pathname.includes('/ar/')?'ar':'en'))changeLanguage(location.href,false).catch(()=>location.reload())});
initPage();
