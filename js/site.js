const nav=document.getElementById('nav'),menu=document.querySelector('.menu');
function closeMenu(){nav.classList.remove('open');menu.setAttribute('aria-expanded','false')}
menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open))});
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){closeMenu();menu.focus()}});
document.addEventListener('click',e=>{if(!nav.contains(e.target)&&!menu.contains(e.target))closeMenu()});
const form=document.getElementById('enquiry');
try{const draft=JSON.parse(sessionStorage.getItem('adwaa-draft'));if(draft)for(const key of ['name','phone','details'])form.elements[key].value=draft[key]||''}catch{}
form.addEventListener('input',()=>{try{sessionStorage.setItem('adwaa-draft',JSON.stringify(Object.fromEntries(new FormData(form))))}catch{}});
form.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;const d=Object.fromEntries(new FormData(form));const title=document.documentElement.lang==='ar'?'طلب معاينة مجانية':'Free site visit enquiry';location.href='https://wa.me/966535056668?text='+encodeURIComponent(`${title}\n${d.name}\n${d.phone}\n${d.service}\n${d.details}`)});
document.querySelector('[data-lang-switch]').addEventListener('click',e=>{if(e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;const sections=[...document.querySelectorAll('main > section')],top=document.getElementById('site-header').offsetHeight;let index=sections.findIndex(s=>s.getBoundingClientRect().bottom>top);if(index<0)index=0;const block=sections[index];try{localStorage.setItem('adwaa-language-transition',JSON.stringify({to:new URL(e.currentTarget.href).pathname,index,ratio:Math.min(1,Math.max(0,(top-block.getBoundingClientRect().top)/block.offsetHeight)),top:scrollY<5,time:Date.now()}))}catch{}});
