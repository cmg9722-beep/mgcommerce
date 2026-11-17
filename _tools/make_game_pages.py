# 261117 게임별 소개 페이지 /games/<slug>/ 생성 — 게임 이름·장르 검색에 우리 페이지가 걸리게(개인정보처리방침 페이지만 색인돼 있었다)
# 사용: python _tools/make_game_pages.py  (mgcommerce_pages 폴더에서)
import os, json, html

SITE = 'https://mgcommerce.net'
G = [
 dict(slug='cheonki', pkg='com.mgcommerce.cheonki', name='천기누설', full='천기누설: 사주 운세 오행 매치3 퍼즐 RPG', icon='cheonki.png',
      genre='사주·운세 매치3 퍼즐 RPG', kw='천기누설 게임, 사주 게임, 운세 게임, 오행 게임, 매치3 퍼즐, 퍼즐 RPG, 로그라이트, 한국 설화 게임',
      lead='태어난 해로 정해지는 나의 오행(용신)으로 싸우는 한국형 매치3 퍼즐 RPG입니다. 같은 색 타일 셋을 맞춰 구미호·저승사자·청룡·백호 같은 한국 설화 속 요괴와 신수를 봉인하세요.',
      feats=['불·물·나무·쇠·흙 다섯 오행 타일 — 보스의 약점 색을 노리는 매치3 전투',
             '4개·5개·ㄱ자 매치로 태극·팔괘 특수 타일, 연쇄 콤보의 손맛',
             '화산·용궁·숲·천계·황천 다섯 세계, 한국 설화 보스 18',
             '보스를 쓰러뜨릴 때마다 봉인(유물)을 골라 매 판 다른 빌드(로그라이트)',
             '매일 바뀌는 오늘의 일진 보스와 출석 보상, 12장 이야기 「숨긴 한 줄」'],
      who=['사주·운세·오행 이야기를 좋아하는 분', '매치3 퍼즐에 RPG 성장이 붙은 게임을 찾는 분', '한국 설화·요괴 소재 게임을 좋아하는 분'],
      faq=[('천기누설은 무료인가요?', '네, 구글 플레이에서 무료로 받을 수 있습니다. 광고가 포함되어 있고, 광고 없이 보상을 받는 상품을 따로 살 수 있습니다.'),
           ('사주를 꼭 입력해야 하나요?', '아니요. 태어난 해만 넣으면 용신 원소가 정해지고, 입력하지 않으면 자동으로 정할 수 있습니다. 사주·용신은 게임을 위한 재미 요소입니다.')]),
 dict(slug='jeongsi', pkg='com.mgcommerce.jeongsi', name='정시 퇴근', full='정시 퇴근: 칼퇴 직장인 서바이벌 액션 게임', icon='jeongsi.png',
      genre='직장인 칼퇴 서바이벌 액션', kw='정시 퇴근 게임, 칼퇴 게임, 퇴근 게임, 직장인 게임, 서바이벌 액션, 자동 공격 게임, 뱀서라이크',
      lead='09:00 지하 주차장에서 출근해 18:00 정문으로 칼퇴하는 직장인 서바이벌 액션입니다. 화면을 끌어 움직이기만 하면 공격은 저절로 — 붙잡으려는 사람들을 뚫고 오늘도 6시에 나가세요.',
      feats=['한 손으로 하는 쉬운 조작, 공격은 자동', '레벨이 오를 때마다 카드를 골라 싸우는 방식을 만드는 성장',
             '반려 도장·참조 메일·쏟은 커피·사직서… 무기 21가지, 진화 18가지', '본부장·점검단·대표이사 보스와 「결재 완료」',
             '서른 날 동안 이어지는 퇴근 이야기, 직군 5·직급 7'],
      who=['오늘도 정시 퇴근을 꿈꾸는 직장인', '자동 공격·카드 강화·무기 진화 서바이벌 액션을 좋아하는 분', '점심시간에 짧게 한 판 스트레스 풀 게임을 찾는 분'],
      faq=[('정시 퇴근은 무료인가요?', '네, 무료입니다. 광고가 포함되어 있고 광고 제거 상품이 있습니다.'),
           ('인터넷 없이도 되나요?', '네, 게임은 인터넷 없이 됩니다. 광고만 인터넷이 필요합니다.')]),
 dict(slug='fusionace', pkg='com.mgcommerce.fusionace', name='FUSION ACE', full='FUSION ACE: 비행기 슈팅 게임·탄막 오락실', icon='fusionace.png',
      genre='오락실 감성 종스크롤 비행기 슈팅', kw='퓨전 에이스, FUSION ACE, 비행기 게임, 비행기 슈팅 게임, 탄막 슈팅, 오락실 게임, 슈팅 게임, 전투기 게임',
      lead='보스를 쓰러뜨리면 하늘에서 합체기가 내려옵니다. 받아 내는 순간 전투기가 한 단계 진화하는 오락실 감성의 종스크롤 비행기 슈팅 게임입니다.',
      feats=['이글-1에서 OMEGA까지 7단 합체 진화', '용신·발키리·프로스트·스콜피온·보이드, 5대륙 보스전과 3단계 페이즈',
             '한 판 6~7분, 난이도마다 다른 결말의 이야기 「신호」', '히트스톱·진동·폭탄으로 살린 격파의 손맛', '격납고 강화, 별 45개, 업적 29개, 데일리 미션'],
      who=['옛날 오락실 비행기 게임·탄막 슈팅을 좋아하는 분', '짧게 한 판 시원하게 터뜨리는 게임을 찾는 분', '합체·진화로 강해지는 재미를 좋아하는 분'],
      faq=[('FUSION ACE는 무료인가요?', '네, 무료입니다. 광고가 포함되어 있고 광고 제거 상품이 있습니다.'),
           ('조작이 어렵나요?', '화면을 끌어 전투기를 움직이면 사격은 자동입니다. 위기 때만 폭탄을 누르면 됩니다.')]),
 dict(slug='dokkaebi', pkg='com.mgcommerce.dokkaebi', name='도깨비 여행', full='틀린그림찾기: 도깨비 여행 - 다른그림 찾기', icon='dokkaebi.png',
      genre='틀린그림찾기·다른그림찾기 두뇌 퍼즐', kw='틀린그림찾기, 다른그림찾기, 숨은그림찾기, 틀린그림찾기 게임, 도깨비 여행, 두뇌 게임, 무료 퍼즐 게임',
      lead='장난꾸러기 도깨비가 전국 여행 사진에 몰래 장난을 쳐 놓았어요. 두 그림에서 바뀐 곳 다섯 군데를 찾아 「팡!」 하고 되돌려 놓는 무료 틀린그림찾기·다른그림찾기 게임입니다.',
      feats=['서울 궁궐·전주 한옥·부산 바다·제주 귤밭·경주 첨성대까지 반실사 그림 30장', '찾을 때마다 터지는 효과와 국악 소리, 「도깨비 뿔났다」 피버',
             '여행지 엽서·지역 음식 카드·꼬마 도깨비를 모으는 도감', '한 폰으로 친구·가족과 대결 또는 협동', '매일 새 그림 「오늘의 그림」'],
      who=['틀린그림찾기·다른그림찾기·숨은그림찾기를 좋아하는 분', '눈 쉬며 짧게 머리 식히고 싶은 분', '가족과 한 폰으로 같이 할 게임을 찾는 분'],
      faq=[('도깨비 여행은 무료인가요?', '네, 무료입니다. 광고가 포함되어 있고 「광고 없이 즐기기」 상품이 있습니다. 확률형 아이템은 없습니다.'),
           ('어른도 할 만한가요?', '네. 처음엔 쉽게 시작해 갈수록 어려워지고, 보스 판과 시간 제한이 있어 어른도 충분히 집중해서 즐길 수 있습니다.')]),
 dict(slug='donggeul', pkg='com.mgcommerce.donggeul', name='동글분식', full='동글분식: 한식 머지 퍼즐 - 떡볶이 김밥 만들기', icon='donggeul.png',
      genre='한식 머지(합치기) 물리 퍼즐', kw='동글분식, 머지 게임, 합치기 게임, 머지 퍼즐, 떡볶이 게임, 김밥 게임, 요리 퍼즐',
      lead='같은 음식을 맞대면 한 단계 큰 음식이 되는 한식 머지 퍼즐입니다. 꼬마김밥·호떡·떡볶이·비빔밥을 거쳐 큰 요리를 완성하며 할머니의 분식집을 다시 열어 보세요.',
      feats=['떨어뜨리고 굴리고 합치는 물리 퍼즐, 연쇄가 터질 때의 「팡! 팡! 팡!」', '분식·시장·잔치 한식 33가지',
             '주문 만들기·한 방 퍼즐·바쁜 시간 세 가지 판', '7장 35판 이야기와 단골손님 9명의 사연', '가게 꾸미기, 하루 한 번 오늘의 주문, 무한 모드'],
      who=['합치기(머지) 퍼즐을 좋아하는 분', '귀여운 음식 그림과 한국 음식을 좋아하는 분', '짧게 한 판씩 머리 식히고 싶은 분'],
      faq=[('동글분식은 무료인가요?', '네, 무료입니다. 광고가 포함되어 있고 「광고 없이 즐기기」 상품이 있습니다. 확률형 아이템은 없습니다.'),
           ('인터넷 없이도 되나요?', '네, 게임은 인터넷 없이 됩니다. 광고만 인터넷을 씁니다.')]),
 dict(slug='ssireum', pkg='com.mgcommerce.robotssireum', name='로봇씨름', full='로봇씨름: 넘어뜨려라! 로봇 싸움 씨름 게임', icon='ssireum.png',
      genre='로봇 씨름 대전 액션', kw='로봇씨름, 로봇 씨름, 씨름 게임, 로봇 싸움 게임, 로봇 게임, 한국 전통 놀이 게임, 천하장사',
      lead='무릎 위 몸이 모래에 먼저 닿으면 지는 한국 씨름, 이번엔 로봇이 샅바를 잡았습니다. 버튼 셋으로 즐기는 짧고 시원한 로봇 씨름 대전 게임입니다.',
      feats=['버티기·기술·밀기, 버튼 세 개로 간단하게', '안다리걸기·잡채기·들배지기 등 진짜 씨름 기술 12가지와 로봇마다 다른 필살기',
             '장독 퉁이·가마솥 대장·돌해태… 로봇 친구 33대', '샅바·모자·장갑·기운 효과로 나만의 로봇 꾸미기', '단오 마을에서 천하장사 결승까지, 매일 바뀌는 「오늘의 장사」'],
      who=['짧게 한 판 시원한 손맛을 좋아하는 분', '귀여운 로봇과 한국 전통 놀이를 좋아하는 분', '온 가족이 함께 할 전체이용가 게임을 찾는 분'],
      faq=[('로봇씨름은 무료인가요?', '네, 무료입니다. 광고가 포함되어 있고 광고 제거와 꾸미기 세트를 살 수 있습니다. 겨루기 능력치는 돈으로 오르지 않습니다.'),
           ('아이도 할 수 있나요?', '전체이용가입니다. 피·다툼 표현이 없습니다.')]),
]

CSS = """body{font-family:system-ui,'Malgun Gothic',sans-serif;max-width:760px;margin:0 auto;padding:20px 16px 40px;line-height:1.75;color:#111;background:#fff}
a{color:#01875f}
.top{font-size:14px;margin-bottom:14px}
.hero{display:flex;gap:16px;align-items:center}
.hero img{width:96px;height:96px;border-radius:20px;flex:none}
h1{font-size:23px;line-height:1.35;margin:0 0 4px}
.genre{color:#555;font-size:15px}
.btn{display:inline-block;background:#01875f;color:#fff!important;text-decoration:none;padding:10px 18px;border-radius:10px;font-weight:700;margin:14px 0}
.shots{display:flex;gap:10px;overflow-x:auto;padding:4px 0 10px}
.shots img{height:360px;width:auto;border-radius:12px;border:1px solid #eee;flex:none}
h2{font-size:19px;margin:26px 0 8px}
ul{padding-left:20px}
.faq dt{font-weight:700;margin-top:10px}
.faq dd{margin:4px 0 0}
.others a{display:inline-block;margin:4px 10px 4px 0}
small{color:#666}"""

def page(g):
    url = f'{SITE}/games/{g["slug"]}/'
    play = f'https://play.google.com/store/apps/details?id={g["pkg"]}'
    e = html.escape
    title = f'{g["full"]} — 무료 모바일 게임 | 구글 플레이'
    desc = f'{g["name"]} — {g["genre"]}. {g["lead"]} 구글 플레이에서 무료로 받으세요.'
    ld = {"@context": "https://schema.org", "@type": "MobileApplication", "name": g["full"], "alternateName": g["name"],
          "operatingSystem": "ANDROID", "applicationCategory": "GameApplication", "genre": g["genre"], "inLanguage": ["ko", "en"],
          "description": g["lead"], "url": url, "installUrl": play, "downloadUrl": play, "image": f'{SITE}/img/{g["icon"]}',
          "screenshot": [f'{SITE}/img/shots/{g["slug"]}-{i}.webp' for i in (1, 2, 3)],
          "offers": {"@type": "Offer", "price": "0", "priceCurrency": "KRW"},
          "author": {"@type": "Organization", "name": "MG Commerce(앰지커머스)", "url": SITE + '/'},
          "publisher": {"@type": "Organization", "name": "MG Commerce(앰지커머스)", "url": SITE + '/'}}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}
    others = ''.join(f'<a href="/games/{o["slug"]}/">{e(o["name"])}</a>' for o in G if o is not g)
    shots = ''.join(f'<img src="/img/shots/{g["slug"]}-{i}.webp" alt="{e(g["name"])} 게임 화면 {i}" width="203" height="360" loading="lazy">' for i in (1, 2, 3))
    feats = ''.join(f'<li>{e(f)}</li>' for f in g["feats"])
    who = ''.join(f'<li>{e(w)}</li>' for w in g["who"])
    faq = ''.join(f'<dt>{e(q)}</dt><dd>{e(a)}</dd>' for q, a in g["faq"])
    return f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="keywords" content="{e(g["kw"])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(g["full"])}">
<meta property="og:description" content="{e(g["lead"])}">
<meta property="og:image" content="{SITE}/img/shots/{g["slug"]}-1.webp">
<meta name="google-play-app" content="app-id={g["pkg"]}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<div class="top"><a href="/">MG Commerce 게임</a> › {e(g["name"])}</div>
<div class="hero"><img src="/img/{g["icon"]}" alt="{e(g["name"])} 아이콘" width="96" height="96">
<div><h1>{e(g["full"])}</h1><div class="genre">{e(g["genre"])} · 무료 · Android</div></div></div>
<a class="btn" href="{play}">Google Play에서 무료로 받기</a>
<p>{e(g["lead"])}</p>
<div class="shots">{shots}</div>
<h2>{e(g["name"])}의 특징</h2>
<ul>{feats}</ul>
<h2>이런 분께 추천합니다</h2>
<ul>{who}</ul>
<h2>자주 묻는 질문</h2>
<dl class="faq">{faq}</dl>
<p><a class="btn" href="{play}">{e(g["name"])} 받으러 가기 (Google Play)</a></p>
<h2>MG Commerce의 다른 게임</h2>
<p class="others">{others}</p>
<p><small><a href="/{g["slug"]}.html">개인정보처리방침</a> · 문의 <a href="mailto:contact@mgcommerce.net">contact@mgcommerce.net</a> · 앰지커머스(MG Commerce) · 사업자등록번호 635-55-01028</small></p>
</body>
</html>
'''

for g in G:
    d = os.path.join('games', g['slug'])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8', newline='\n').write(page(g))
    print('완료', d)
