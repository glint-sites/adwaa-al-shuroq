/* Native local video: optional motion, no social embeds or autoplay audio. */
let projectMediaCleanup=()=>{};
const savedMediaPositions=new Map();
let heroPausedByUser=false;
function initProjectMedia(){
 projectMediaCleanup();
 const videos=[...document.querySelectorAll('video[data-media-key]')];
 if(!videos.length)return;
 const lifecycle=new AbortController(),options={signal:lifecycle.signal};
 const reduce=matchMedia('(prefers-reduced-motion: reduce)');
 const hero=videos.find(v=>v.dataset.mediaKey==='design');
 const toggle=document.querySelector('[data-media-toggle]');
 let manuallyPaused=heroPausedByUser,heroVisible=false;
 function sync(){if(!toggle||!hero)return;toggle.textContent=(hero.paused?toggle.dataset.playLabel+' ▷':toggle.dataset.pauseLabel+' Ⅱ');toggle.setAttribute('aria-pressed',String(!hero.paused))}
 function stop(video){if(!video.paused)video.pause()}
 function autoPlay(){if(hero&&heroVisible&&!manuallyPaused&&!reduce.matches&&!navigator.connection?.saveData&&!document.hidden)hero.play().catch(sync)}
 for(const video of videos){
  video.muted=true;
  const restore=()=>{const time=savedMediaPositions.get(video.dataset.mediaKey);if(time&&Number.isFinite(video.duration))video.currentTime=Math.min(time,video.duration-.05)};
  video.addEventListener('loadedmetadata',restore,{...options,once:true});
  if(video.readyState>=1)restore();
 }
 document.querySelectorAll('[data-film-play]').forEach(button=>{const video=document.getElementById(button.getAttribute('aria-controls'));button.addEventListener('click',()=>video.play().catch(()=>{}),options);video.addEventListener('play',()=>button.hidden=true,options)});
 if(hero){
  hero.addEventListener('loadeddata',()=>hero.classList.add('is-ready'),options);
  hero.addEventListener('play',sync,options);hero.addEventListener('pause',sync,options);hero.addEventListener('error',()=>{hero.classList.remove('is-ready');if(toggle)toggle.hidden=true},options);
  toggle?.addEventListener('click',()=>{if(hero.paused){manuallyPaused=false;heroPausedByUser=false;hero.play().catch(sync)}else{manuallyPaused=true;heroPausedByUser=true;stop(hero)}sync()},options);
  reduce.addEventListener('change',()=>{if(reduce.matches)stop(hero);else autoPlay()},options);
 }
 const observer='IntersectionObserver' in window?new IntersectionObserver(entries=>{for(const entry of entries){const video=entry.target;if(video===hero){heroVisible=entry.isIntersecting;if(heroVisible)autoPlay();else stop(video)}else if(!entry.isIntersecting)stop(video)}},{threshold:.15}):null;
 videos.forEach(v=>observer?.observe(v));
 document.addEventListener('visibilitychange',()=>{if(document.hidden)videos.forEach(stop);else autoPlay()},options);
 projectMediaCleanup=()=>{for(const video of videos){savedMediaPositions.set(video.dataset.mediaKey,video.currentTime);stop(video)}observer?.disconnect();lifecycle.abort()};
 sync();
}
