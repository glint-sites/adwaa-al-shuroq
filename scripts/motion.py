from bs4 import BeautifulSoup

def add_motion(html, lang, service=None):
    ar=lang=='ar'
    def tr(en,arabic):return arabic if ar else en
    s=BeautifulSoup(html,'html.parser')
    def frag(markup):return BeautifulSoup(markup,'html.parser')
    if service is None:
        image=s.select_one('.hero-photo');image['src']='/assets/herohq.webp';image['width']='1672';image['height']='941'
        image['alt']=tr('Illustrative interior concept with detailed gypsum ceilings, painted walls and oak finishes','تصور توضيحي لمساحة بأسقف جبسية وتشطيبات دهان وخشب بلوط')
        panel=s.select_one('.hero-detail');panel.clear()
        panel.append(frag(f'<p class="eyebrow">{tr("DESIGN IDEAS IN MOTION","أفكار وتصاميم متحركة")}</p><video class="hero-video" data-media-key="design" muted playsinline loop preload="none" poster="/assets/media/design-poster.webp" aria-label="{tr("Interior design reel from the company Instagram","فيديو تصاميم داخلية من حساب المؤسسة على إنستغرام")}"><source src="/assets/media/design-reel-smooth.mp4" type="video/mp4"></video><div class="hero-reel-caption"><span>@design._decor</span><button type="button" data-media-toggle aria-controls="hero-film" data-play-label="{tr("Play video","تشغيل الفيديو")}" data-pause-label="{tr("Pause video","إيقاف الفيديو")}">{tr("Play video","تشغيل الفيديو")} ▷</button></div><a href="https://www.instagram.com/design._decor/reel/DeaGM8Eiw71/" target="_blank" rel="noopener">{tr("View the original design reel","شاهد عرض التصاميم الأصلي")} ↗</a>'))
        caption=s.select_one('.hero-caption');caption.select_one('span').string=tr('ILLUSTRATIVE INTERIOR CONCEPT','تصور توضيحي للتشطيبات')
        s.select_one('.hero-video')['id']='hero-film'
    if service is None or service=='renovation-finishing':
        title=tr('A space, reimagined.<br><em>See the transformation.</em>','مساحة تتجدد.<br><em>شاهد التحول.</em>')
        intro=tr('A short renovation sequence shared by the team: from exposed surfaces and ceiling work to a finished, brighter interior. Watch the original footage, right here.','لقطات تجديد شاركها الفريق: من الأعمال الأولية وتجهيز الأسقف إلى مساحة مكتملة وأكثر إشراقاً. شاهد الفيديو الأصلي هنا.')
        section=f'<section id="project-film" class="project-film"><div class="shell project-film-grid"><div class="film-copy"><p class="eyebrow">{tr("FROM THE COMPANY’S INSTAGRAM","من حساب المؤسسة على إنستغرام")}</p><h2>{title}</h2><p>{intro}</p><ul><li>{tr("The space before the refresh","المكان قبل التجديد")}</li><li>{tr("Ceiling & interior work in progress","تجهيز الأسقف والأعمال الداخلية")}</li><li>{tr("The finished room","المساحة بعد التشطيب")}</li></ul><a class="button" href="#contact" data-enquiry-service="3">{tr("Talk about your renovation","ناقش تجديد مساحتك")} ↗</a><a class="film-source" href="https://www.instagram.com/design._decor/reel/De4Ndd0CnKJ/" target="_blank" rel="noopener">{tr("View the original reel","شاهد الفيديو على إنستغرام")} ↗</a></div><figure class="film-player"><video id="renovation-film" data-media-key="renovation" controls muted playsinline loop preload="none" poster="/assets/media/renovation-poster.webp" aria-label="{tr("Before-and-after home renovation video","فيديو لترميم المنزل قبل الأعمال وبعدها")}"><source src="/assets/media/renovation-reel.mp4" type="video/mp4"></video><button type="button" class="film-start" data-film-play aria-controls="renovation-film">▷ {tr("Play the transformation","شاهد التحول")}</button><figcaption>{tr("Original visual sequence · no audio","لقطات أصلية · دون صوت")}</figcaption></figure></div></section>'
        target=s.select_one('.process-section') if service else s.select_one('#about')
        target.insert_before(frag(section))
    return str(s)
