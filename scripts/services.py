"""Service scope adapted from the client's five public service pages, 2026-11-04."""
from bs4 import BeautifulSoup
from copy import deepcopy

SERVICES = [
    dict(slug='gypsum-ceilings', index=0, image='gypsum', source='gypsum-board-jubail',
         title=['Gypsum ceilings & decorative details', 'أسقف جبسية وتفاصيل ديكورية'],
         intro=['Give the room a new dimension. Gypsum-board and suspended ceilings, Moroccan-style details and foam mouldings for living rooms and majlis spaces.', 'امنح مساحتك بُعداً جديداً. جبس بورد وأسقف مستعارة وتفاصيل مغربية وبراويز فوم للصالات والمجالس.'],
         scope=[('Gypsum board & suspended ceilings','Design and installation of ceiling details for living rooms and majlis spaces.','جبس بورد وأسقف مستعارة','تصميم وتنفيذ تفاصيل الأسقف للصالات والمجالس.'),('Foam frames & mouldings','Supply and installation of decorative frames, skirting and modern gypsum alternatives.','إطارات وبراويز فوم','توريد وتركيب النعلات والإطارات وبراويز الفوم وبدائل الجبس الحديثة.'),('Paint & finishing','Coordinate the ceiling details with painting and the surrounding finishes.','الدهان والتشطيب','تنسيق تفاصيل الأسقف مع الدهان والتشطيبات المحيطة.')]),
    dict(slug='painting', index=1, image='paint', source='paints-jubail',
         title=['Painting that changes the whole room', 'دهانات تغير إحساس المكان'],
         intro=['From a fresh interior palette to exterior painting. Discuss colours, decorative finishes and Jotun paint options with the team.', 'من ألوان داخلية جديدة إلى دهانات الواجهات. ناقش الألوان والتشطيبات الديكورية وخيارات أصباغ جوتن مع الفريق.'],
         scope=[('Interior painting','Painting for rooms, apartments and villas, with colours chosen around your space.','دهانات داخلية','دهانات للغرف والشقق والفلل بألوان تناسب مساحتك.'),('Exterior painting','Exterior paintwork for residential properties as part of a refresh or finishing project.','دهانات خارجية','أعمال دهانات خارجية للمباني السكنية ضمن مشاريع التجديد والتشطيب.'),('Decorative finishes & Jotun paints','Discuss the look you want and the suitable paint materials before starting.','تشطيبات ديكورية وأصباغ جوتن','ناقش المظهر المطلوب ومواد الدهان المناسبة قبل بدء العمل.')]),
    dict(slug='interior-decoration', index=2, image='interior', source='interior-decor-jubail',
         title=['A room with its own character', 'مساحة تعبر عن ذوقك'],
         intro=['Modern and neoclassical decoration, TV feature walls and wallpaper. Bring your inspiration and shape the details around your home.', 'ديكورات مودرن ونيو كلاسيك وخلفيات شاشات وورق جدران. شاركنا ما يلهمك، ولننسق التفاصيل بما يناسب منزلك.'],
         scope=[('Modern & neoclassical decoration','Design and execution of contemporary and neoclassical decorative details.','مودرن ونيو كلاسيك','تصميم وتنفيذ تفاصيل ديكورية معاصرة وبطراز نيو كلاسيك.'),('TV feature walls','Decorative screen backdrops that bring the focal point of the room together.','خلفيات الشاشات','ديكورات لخلفيات الشاشة تنسق نقطة التركيز الرئيسية في الغرفة.'),('Wallpaper supply & installation','Korean, European and 3D wallpaper options; discuss the right selection for your room.','توريد وتركيب ورق الجدران','خيارات كورية وأوروبية وثلاثية الأبعاد، مع مناقشة الأنسب لمساحتك.')]),
    dict(slug='flooring-cladding', index=4, image='floor', source='flooring-parquet-jubail',
         title=['A foundation for the whole space', 'أرضيات تكتمل بها المساحة'],
         intro=['Wood and SPC parquet, tiles, marble and decorative cladding. Explore the surfaces that bring your rooms together.', 'باركيه خشبي وSPC وبلاط ورخام وتكسيات ديكورية. اكتشف الأسطح التي تمنح غرفك الانسجام.'],
         scope=[('Wood & SPC parquet','Supply and installation of wood parquet and SPC flooring.','باركيه خشبي وSPC','توريد وتركيب الباركيه الخشبي وأرضيات SPC.'),('Tile, porcelain & marble','Installation for floors, bathrooms and façades according to the project scope.','بلاط وبورسلان ورخام','تركيب للأرضيات والحمامات والواجهات بحسب الأعمال المطلوبة.'),('Decorative cladding','Supply and installation of wood-effect, marble-effect and chipboard alternatives.','تكسيات ديكورية','توريد وتركيب بدائل الخشب والرخام والشيبورد.')]),
    dict(slug='renovation-finishing', index=3, image='about', source='renovation-finishing-jubail',
         title=['Keep the place. Renew the possibilities.', 'احتفظ بالمكان. وجدد إمكانياته.'],
         intro=['Renovation for older homes and majlis spaces, apartment and villa finishing, and annex construction. Start by discussing what your property needs.', 'ترميم المنازل والمجالس القديمة وتشطيب الشقق والفلل وبناء الملاحق. لنبدأ بمناقشة ما يحتاجه عقارك.'],
         scope=[('Home renovation & façades','Refresh older homes and majlis spaces, renew façades, and discuss cracks or leaks requiring attention.','ترميم المنازل والواجهات','تجديد المنازل والمجالس القديمة والواجهات ومناقشة التشققات أو التسريبات التي تحتاج إلى معالجة.'),('Apartment & villa finishing','Interior and exterior finishing including plumbing, electrical work, plastering and modern lighting coordination.','تشطيب الشقق والفلل','تشطيبات داخلية وخارجية تشمل السباكة والكهرباء واللياسة وتنسيق الإضاءة الحديثة.'),('Annex construction & finishing','Building and finishing residential annexes, with scope and requirements discussed during the site visit.','بناء الملاحق وتشطيبها','بناء الملاحق السكنية وتشطيبها، مع مناقشة المتطلبات والأعمال خلال المعاينة.')]),
]

LABELS = [['Gypsum & ceilings','الجبس والأسقف'],['Painting & finishes','الدهانات والتشطيبات'],['Interior decoration','الديكور الداخلي'],['Flooring & cladding','الأرضيات والتكسيات'],['Renovation & finishing','الترميم والتشطيب']]
for service, labels in zip(SERVICES,LABELS):
    service['label']=labels

def url(lang, slug=''):
    return ('/ar/' if lang == 'ar' else '/') + ('services/'+slug+'/' if slug else '')

def enhance_home(html, lang):
    ar = lang == 'ar'
    def tr(en, arabic): return arabic if ar else en
    s = BeautifulSoup(html, 'html.parser')
    def frag(markup): return BeautifulSoup(markup, 'html.parser')
    nav = s.select_one('#nav')
    menu = s.new_tag('details', attrs={'class':'services-nav'})
    menu.append(frag(f'<summary>{tr("Services","خدماتنا")} <span aria-hidden="true">⌄</span></summary><div class="services-panel">'+''.join(f'<a href="{url(lang,d["slug"])}">{d["label"][ar]}</a>' for d in SERVICES)+f'<a class="all-services" href="#services">{tr("All services","جميع الخدمات")} ↗</a></div>'))
    nav.select_one('a').replace_with(menu)
    for card,d in zip(s.select('.service'),SERVICES[:4]):
        title=card.select_one('h3'); title.clear();title.append(frag(f'<a class="service-title" href="{url(lang,d["slug"])}">{d["label"][ar]}</a>'))
        more=s.new_tag('a',href=url(lang,d['slug']),attrs={'class':'service-more'})
        more.string=tr('Explore this service →','اكتشف هذه الخدمة ←')
        card.select_one('p').insert_after(more)
    reno=s.select_one('.renovation-card')
    reno.select_one('p:not(.eyebrow)').string=tr('Renovation, apartment and villa finishing, plumbing, electrical work, plastering and annex construction. Bring the whole scope together with one team.','ترميم وتشطيب شقق وفلل وأعمال سباكة وكهرباء ولياسة وبناء ملاحق. اجمع تفاصيل مشروعك مع فريق واحد.')
    reno.append(frag(f'<a class="renovation-more" href="{url(lang,"renovation-finishing")}">{tr("Explore renovation & finishing","اكتشف الترميم والتشطيب")} ↗</a>'))
    # Verified company social destination, with an explicit external-navigation label.
    social=f'<a class="instagram-link" href="https://www.instagram.com/design._decor/" target="_blank" rel="noopener">{tr("More from the team on Instagram","المزيد من الفريق على إنستغرام")} ↗</a>'
    s.select_one('#work .gallery').insert_after(frag(social))
    s.select_one('.contact-meta').insert_after(frag(f'<div class="contact-links"><a href="tel:+966535056668">{tr("Call the team","اتصل بالفريق")} ↗</a><a href="https://www.instagram.com/design._decor/" target="_blank" rel="noopener">Instagram ↗</a></div>'))
    form=s.select_one('form')
    form.select_one('textarea').find_parent('label').insert_before(frag(f'<label>{tr("Project location (optional)","موقع المشروع (اختياري)")}<input name="location" autocomplete="address-level2" maxlength="150" placeholder="{tr("City or neighbourhood","المدينة أو الحي")}"></label>'))
    s.select_one('.contact-meta').clear()
    s.select_one('.contact-meta').append(frag(tr('Jubail · Serving the Eastern Province<br>Jubail, Dammam & Al Khobar enquiries welcome<br>Saturday–Thursday · 8:00 AM–10:00 PM','الجبيل · نخدم المنطقة الشرقية<br>نرحب بطلبات الجبيل والدمام والخبر<br>السبت–الخميس · ٨ صباحاً–١٠ مساءً')))
    # Remove the dormant sales modal too; the user asked to remove the sales strip.
    if s.select_one('#buy-dialog'):s.select_one('#buy-dialog').decompose()
    return str(s)

def build_service_pages(home, lang):
    ar=lang=='ar'
    def tr(en,arabic):return arabic if ar else en
    result={}
    for d in SERVICES:
        s=BeautifulSoup(home,'html.parser')
        def frag(markup):return BeautifulSoup(markup,'html.parser')
        s.body['data-page-key']=d['slug'];s.body['data-default-service']=str(d['index'])
        s.title.string=d['label'][ar]+tr(' | Adwaa Al Shuroq, Jubail',' | أضواء الشروق، الجبيل')
        s.select_one('meta[name=description]')['content']=d['intro'][ar]
        s.select_one('link[rel=canonical]')['href']='https://glintsites.com/adwaa-al-shuroq'+url(lang,d['slug'])
        for alternate in s.select('link[rel=alternate]'):
            alternate['href']='https://glintsites.com/adwaa-al-shuroq'+url(alternate['hreflang'],d['slug'])
        s.select_one('[data-lang-switch]')['href']=url('en' if ar else 'ar',d['slug'])
        s.select_one('.brand')['href']=url(lang)
        # All global homepage anchors retain a real destination from detail pages.
        for link in s.select('header a[href^="#"],footer a[href^="#"]'):
            if link['href']!='#contact':link['href']=url(lang)+link['href']
        contact=deepcopy(s.select_one('#contact'));process=deepcopy(s.select_one('.process-section'))
        selected=contact.select_one('select')
        selected.select('option')[d['index']]['selected']=''
        main=s.select_one('main');main.clear()
        label=d['label'][ar]+' / '+tr('JUBAIL & EASTERN PROVINCE','الجبيل والمنطقة الشرقية')
        image_note=tr('Illustrative service image','صورة توضيحية للخدمة') if d['image']=='paint' else tr('Imagery from the company website','من صور موقع المؤسسة')
        hero=f'<section class="detail-hero shell"><nav class="breadcrumbs" aria-label="{tr("Breadcrumb","مسار الصفحة")}"><a href="{url(lang)}">{tr("Home","الرئيسية")}</a><span>/</span><a href="{url(lang)}#services">{tr("Services","خدماتنا")}</a></nav><div class="detail-hero-grid"><div><p class="eyebrow">{label}</p><h1>{d["title"][ar]}</h1><p class="detail-intro">{d["intro"][ar]}</p><div class="actions"><a class="button" href="#contact" data-enquiry-service="{d["index"]}">{tr("Arrange a free site visit","احجز معاينة مجانية")} ↗</a><a class="text-link dark-link" href="tel:+966535056668">{tr("Call the team","اتصل بالفريق")} ↗</a></div><p class="detail-note">{tr("Your space, your preferences. Discuss the scope and finishes with the team.","مساحتك وذوقك أولاً. ناقش الأعمال والتشطيبات المطلوبة مع الفريق.")}</p></div><figure><img fetchpriority="high" src="/assets/{d["image"]}.webp" width="1200" height="1600" alt="{d["title"][ar]}"><figcaption>{image_note}</figcaption></figure></div></section>'
        main.append(frag(hero))
        scopes=''.join(f'<article><span>0{i+1}</span><h3>{row[2] if ar else row[0]}</h3><p>{row[3] if ar else row[1]}</p></article>' for i,row in enumerate(d['scope']))
        main.append(frag(f'<section class="scope-section"><div class="shell"><p class="eyebrow">{tr("THE SCOPE","تفاصيل الخدمة")}</p><h2>{tr("The details, brought together.","تفاصيل تتكامل معاً.")}</h2><div class="scope-grid">{scopes}</div><div class="scope-next"><p>{tr("Have a photo or a finish you like? Share it with the team on WhatsApp after opening your enquiry.","لديك صور للمكان أو تشطيبات تعجبك؟ أرسلها للفريق عبر واتساب بعد فتح طلبك.")}</p><a href="{url(lang)}#work">{tr("Explore the gallery","تصفح المعرض")} ↗</a></div></div></section>'))
        main.append(process)
        main.append(contact)
        related=''.join(f'<a href="{url(lang,other["slug"])}"><span>{other["label"][ar]}</span><span aria-hidden="true">↗</span></a>' for other in SERVICES if other!=d)
        main.append(frag(f'<section class="related-section shell"><p class="eyebrow">{tr("BRING THE WHOLE ROOM TOGETHER","لمساحة أكثر انسجاماً")}</p><h2>{tr("What else is on your list?","ما الذي تحتاجه أيضاً؟")}</h2><div class="related-links">{related}</div></section>'))
        result[url(lang,d['slug'])]=str(s)
    return result
