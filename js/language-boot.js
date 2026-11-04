/* Run in the head: restore the matching section before the arrival frame. */
(function () {
  'use strict';
  const key = 'adwaa-language-transition';
  function pending() {
    try {
      const p = JSON.parse(localStorage.getItem(key));
      return p && p.to === location.pathname && Date.now() - p.time < 20000 &&
        Number.isInteger(p.index) && p.index >= 0 && Number.isFinite(p.ratio) &&
        p.ratio >= 0 && p.ratio <= 1 ? p : null;
    } catch { return null; }
  }
  if (pending()) {
    document.documentElement.classList.add('lang-arrival');
    if (!document.prerendering) document.write('<link rel="expect" href="#page-end" blocking="render">');
  }
  function restore() {
    const p = pending();
    if (!p) return;
    try { localStorage.removeItem(key); } catch {}
    if (p.top) { window.scrollTo({top:0,behavior:'instant'}); return; }
    const blocks = [...document.querySelectorAll('main > section')].filter(el => el.offsetHeight > 0);
    const block = blocks[p.index];
    if (!block) return;
    const header = document.getElementById('site-header');
    const apply = () => window.scrollTo({top:Math.max(0,block.getBoundingClientRect().top + window.scrollY +
      p.ratio * block.offsetHeight - (header ? header.offsetHeight : 0)),behavior:'instant'});
    apply();
    // Arabic font metrics can settle after the initial pre-rendered layout.
    if (document.fonts && window.requestAnimationFrame) {
      window.requestAnimationFrame(() => document.fonts.ready.then(() => window.requestAnimationFrame(apply)));
    }
  }
  if ('onpagereveal' in window) {
    window.addEventListener('pagereveal', event => {
      if (pending() && event.viewTransition?.types) event.viewTransition.types.add('lang');
      restore();
    });
  } else {
    document.addEventListener('DOMContentLoaded', restore, {once:true});
  }
})();
