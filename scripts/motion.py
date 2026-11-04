from bs4 import BeautifulSoup

def add_motion(html, lang, service=None):
    ar=lang=='ar'
    def tr(en,arabic):return arabic if ar else en
    s=BeautifulSoup(html,'html.parser')
    def frag(markup):return BeautifulSoup(markup,'html.parser')
    if service is None:
        image=s.select_one('.hero-photo');image['src']='/assets/media/design-poster.webp';image['width']='1280';image['height']='720'
        image['alt']=tr('Interior design presentation from Adwaa Al Shuroq’s Instagram','عرض تصاميم داخلية من حساب أضواء الشروق على إنستغرام')
        image.insert_after(frag(f'<video class="hero-video" data-media-key="design" muted playsinline loop preload="none" poster="/assets/media/design-poster.webp" aria-label="{tr("Interior design reel from the company Instagram","فيديو تصاميم داخلية من حساب المؤسسة على إنستغرام")}"><source src="/assets/media/design-reel.mp4" type="video/mp4"></video>'))
        caption=s.select_one('.hero-caption');caption.select_one('span').string=tr('DESIGN REEL · @DESIGN._DECOR','عرض تصاميم · @DESIGN._DECOR')
        caption.append(frag(f'<button type="button" data-media-toggle aria-controls="hero-film" data-play-label="{tr("Play video","تشغيل الفيديو")}" data-pause-label="{tr("Pause video","إيقاف الفيديو")}">{tr("Play video","تشغيل الفيديو")} ▷</button>'))
        s.select_one('.hero-video')['id']='hero-film'
        # Keep source credit accessible without adding another layer over the headline.
        s.select_one('.hero-note').append(frag(f' <a href="https://www.instagram.com/design._decor/reel/DeaGM8Eiw71/" target="_blank" rel="noopener">{tr("View the design reel","شاهد عرض التصاميم")} ↗</a>'))
    if service is None or service=='renovation-finishing':
        title=tr('A space, reimagined.<br><em>See the transformation.</em>','مساحة تتجدد.<br><em>شاهد التحول.</em>')
        intro=tr('A short renovation sequence shared by the team: from exposed surfaces and ceiling work to a finished, brighter interior. Watch the original footage, right here.','لقطات تجديد شاركها الفريق: من الأعمال الأولية وتجهيز الأسقف إلى مساحة مكتملة وأكثر إشراقاً. شاهد الفيديو الأصلي هنا.')
        section=f'<section id="project-film" class="project-film"><div class="shell project-film-grid"><div class="film-copy"><p class="eyebrow">{tr("FROM THE COMPANY’S INSTAGRAM","من حساب المؤسسة على إنستغرام")}</p><h2>{title}</h2><p>{intro}</p><ul><li>{tr("The space before the refresh","المكان قبل التجديد")}</li><li>{tr("Ceiling & interior work in progress","تجهيز الأسقف والأعمال الداخلية")}</li><li>{tr("The finished room","المساحة بعد التشطيب")}</li></ul><a class="button" href="#contact" data-enquiry-service="3">{tr("Talk about your renovation","ناقش تجديد مساحتك")} ↗</a><a class="film-source" href="https://www.instagram.com/design._decor/reel/De4Ndd0CnKJ/" target="_blank" rel="noopener">{tr("View the original reel","شاهد الفيديو على إنستغرام")} ↗</a></div><figure class="film-player"><video id="renovation-film" data-media-key="renovation" controls muted playsinline loop preload="none" poster="/assets/media/renovation-poster.webp" aria-label="{tr("Before-and-after home renovation video","فيديو لترميم المنزل قبل الأعمال وبعدها")}"><source src="/assets/media/renovation-reel.mp4" type="video/mp4"></video><button type="button" class="film-start" data-film-play aria-controls="renovation-film">▷ {tr("Play the transformation","شاهد التحول")}</button><figcaption>{tr("Original visual sequence · no audio","لقطات أصلية · دون صوت")}</figcaption></figure></div></section>'
        target=s.select_one('.process-section') if service else s.select_one('#about')
        target.insert_before(frag(section))
    return str(s)
