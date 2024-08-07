from pymongo import MongoClient
from datetime import datetime
from main import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.bookstore
collection = db.books

books = [
    {
        "title": "О рабстве и свободе человека",
        "author": "Николай Бердяев",
        "genre": "Философия",
        "release_date": 1939,
        "description": "«… Философия этой книги сознательно личная, в ней говорится о человеке, о мире, о Боге лишь "
                       "то, что я увидел и пережил, в ней философствует конкретный человек, а не мировой разум или "
                       "мировой дух. Для объяснения моего умственного пути должен ещё сказать, что мир представляется "
                       "мне вечно новым, я воспринимаю его как бы в первичной интуиции, хотя бы это была давно "
                       "узнанная мною истина. Неверно поняли бы мою книгу те, которые захотели бы увидеть в ней "
                       "практическую программу и конкретное решение социальных вопросов. Это книга философская, "
                       "и она предполагает, прежде всего, духовную реформу. …»",
        "cover": "https://basket-13.wbbasket.ru/vol1960/part196039/196039699/images/big/1.webp"
    },
    {
        "title": "Замок Броуди",
        "author": "Арчибальд Кронин",
        "genre": "Художественная литература",
        "release_date": 1931,
        "description": "«Замок Броуди» — первый роман Арчибальда Кронина. В оригинале носит название «Hatter’s "
                       "Castle» («Замок шляпника»). При написании романа Кронин несколько раз уничтожал написанное, "
                       "начиная работу заново. Вопреки пессимистичным ожиданиям автора, «Замок Броуди» принёс ему "
                       "успех. Сюжет включает в себя много героев и побочных линий, но все они связаны с жизнью "
                       "торговца шляпами, Джеймса Броуди, чей нарциссизм и жестокость постепенно разрушают его семью.",
        "cover": "https://static2.my-shop.ru/products494/4936844/ph_001.jpg"
    },
    {
        "title": "Поединок",
        "author": "Александр Куприн",
        "genre": "Художественная литература",
        "release_date": 1905,
        "description": "«Поединок» — повесть русского писателя Александра Ивановича Куприна, написанная в период 1902 "
                       "— 1905 годах и опубликованная в мае 1905 года в VI книге сборника издательства «Знание». В "
                       "повести описывается история службы и трагической судьбы молодого офицера пехотного полка "
                       "Русской императорской армии, стоявшего в захолустном гарнизонном городке в конце XIX века. "
                       "Это произведение было и остаётся выдающимся явлением русской прозы XX века и является самым "
                       "значительным произведением в творчестве писателя.",
        "cover": "https://static.onlinetrade.ru/img/items/b"
                 "/kniga_poedinok_povest_kuprin_aleksandr_ivanovich_1605690044_1.jpg"
    },
    {
        "title": "Мир как воля и представление",
        "author": "Артур Шопенгауэр",
        "genre": "Философия",
        "release_date": 1818,
        "description": "Основная часть работы, как указано в начале работы, предполагает предварительное знакомство с "
                       "теориями Иммануила Канта. Шопенгауэр рассматривается многими как более верный сторонник "
                       "метафизической системы трансцендентального идеализма Канта, чем любой другой из последующих "
                       "немецких идеалистов. Как бы то ни было, книга содержит приложение, озаглавленное как «Критика "
                       "философии Канта», в которой отвергается кантианская этика и значительная часть кантианской "
                       "эпистемологии и эстетики. Шопенгауэр требует ознакомления со своим приложением перед чтением "
                       "самой книги, хотя оно не содержится в самой книге, а появилось ранее под названием "
                       "«Четырехкратный корень принципа достаточного основания». Он также утверждает во вступлении, "
                       "что читатель будет достаточно подготовлен для его теории, если будет знаком с платоновской "
                       "школой или индийской философией.",
        "cover": "https://avatars.mds.yandex.net/i?id=554ffbfe806688ce72b44042111153ed44f2f277-10637298-images-thumbs"
                 "&n=13"
    },
    {
        "title": "День опричника",
        "author": "Владимир Сорокин",
        "genre": "Художественная литература",
        "release_date": 2006,
        "description": "«День опри́чника» — антиутопическая повесть русского писателя Владимира Сорокина, изданная в "
                       "2006 году. Книга сатирически рисует мир, который ждёт Россию в случае продолжения текущего "
                       "политического курса. Повесть открывается посвящением Малюте Скуратову. В 2008 году вышло "
                       "продолжение — сборник рассказов «Сахарный Кремль».",
        "cover": "https://cdn1.ozone.ru/s3/multimedia-3/6008819247.jpg"
    },
    {
        "title": "Брятья Карамазовы",
        "author": "Федор Достоевский",
        "genre": "Художественная литература",
        "release_date": 1878,
        "description": "«Бра́тья Карама́зовы» — последний роман Ф. М. Достоевского. Роман был напечатан частями в "
                       "журнале «Русский вестник». Достоевский задумывал работу как первую часть эпического романа "
                       "«История Великого грешника». Произведение было окончено в ноябре 1880 года. Писатель умер "
                       "через два месяца после публикации. ",
        "cover": "https://avatars.mds.yandex.net/i?id=ef7a53a8035c3d7335dfbfceb9e0dc0658c79287-12685009-images-thumbs&n=13"
    },
    {
        "title": "Демиан",
        "author": "Герман Гессе",
        "genre": "Художественная литература",
        "release_date": 1919,
        "description": "Демиан - это философский роман немецкого писателя Германа Гессе. Роман о жизни главного героя "
                       "- Эмиля Синклера, начинается повествование с самого детства персонажа и заканчивается его "
                       "службой на войне. В его жизни случалось не мало странностей и очень не стандартных ситуаций, "
                       "в которых помогает разобраться Макс Демиан, который следует и помогает разобраться во всем "
                       "Синклеру до самого конца.",
        "cover": "https://foroom.by/upload/iblock/ae9/ae978fd72d041a5452329968229d6208/cover1.jpg"
    },
    {
        "title": "Искра жизни",
        "author": "Эрих Мария Ремарк",
        "genre": "Художественная литература",
        "release_date": 1952,
        "description": "Искра жизни - роман о концлагере, написанный Эрихом Марией Ремарком в 1952 году. Роман "
                       "состоит из 25 глав и рассказывает историю заключенных и сторожей Маленького "
                       "лагеря вымышленного концентрационного лагеря Меллерн за несколько месяцев до окончания Второй "
                       "мировой войны.",
        "cover": "https://img4.labirint.ru/rc/b6f46ea3c4b0227938c9ec2e3fa2ecf0/594x918q80/books45/441002/cover.jpg?1566211499"
    },
    {
        "title": "Мы",
        "author": "Евгений Замятин",
        "genre": "Художественная литература",
        "release_date": 1988,
        "description": "«Мы» — роман-антиутопия Евгения Замятина, написанный в 1920 году. В СССР не печатался до 1988 "
                       "года, потому что считался «идеологически враждебным» и «клеветническим». Повлиял на "
                       "творчество многих известных писателей XX века, в том числе на Олдоса Хаксли, Джорджа Оруэлла, "
                       "Курта Воннегута и Владимира Набокова.",
        "cover": "https://fkniga.ru/media/product/04/040404/KA-00407663.jpg"
    },
    {
        "title": "Тошнота",
        "author": "Жан Поль Сартр",
        "genre": "Философия",
        "release_date": 1938,
        "description": "«Тошнота» (фр. La Nausée, первое название «Меланхолия») — роман французского философа, "
                       "писателя и эссеиста Жан-Поля Сартра, самое известное из его художественных произведений, "
                       "написан в 1938 году, во время пребывания Сартра в Гавре. Некоторые критики называют «Тошноту» "
                       "самым удачным романом писателя.",
        "cover": "https://avatars.mds.yandex.net/i?id=d2f6959682ad7351a3c780e1a183ac5e6bdd6976-4580161-images-thumbs&n=13"
    },
    {
        "title": "Скорбь Сатаны",
        "author": "Мария Корелли",
        "genre": "Художественная литература",
        "release_date": 1895,
        "description": "«Скорбь Сатаны» — мистический декадентский роман английской писательницы Марии Корелли, "
                       "опубликованный в 1895 году и ставший крупнейшим бестселлером в истории викторианской Англии. "
                       "В книге обыгрывается традиционный мотив сделки с дьяволом. Корелли внесла новое слово в "
                       "литературу о Фаусте, показав, что Сатана больше, чем кто-либо, сознаёт истинность Евангелия и "
                       "вместе с тем ему запрещено передавать эту благую весть людям.",
        "cover": "https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:The_Sorrows_of_Satan.jpg"
    },
    {
        "title": "Преступление и наказание",
        "author": "Федор Достоевский",
        "genre": "Художественная литература",
        "release_date": 1865,
        "description": "Замысел «Преступления и наказания» созревал у Достоевского в течение многих лет, "
                       "однако центральная тема, связанная с идеей главного героя об «обыкновенных» и "
                       "«необыкновенных» людях, начала формироваться только в 1863 году в Италии. Приступив к "
                       "непосредственной работе над произведением, автор объединил черновики незавершённого романа "
                       "«Пьяненькие», в котором была намечена сюжетная линия, повествующая о семье Мармеладовых, "
                       "и наброски романа-исповеди, задуманного как откровение каторжанина. В процессе работы план "
                       "расширился, и в основу сюжета легло преступление студента Родиона Раскольникова, "
                       "убившего ради спасения близких старуху-процентщицу.",
        "cover": "https://avatars.mds.yandex.net/i?id=4b82c84e576cc890ff018040c3726aed1349d794c05aff96-11539738-images-thumbs&n=13"
    },
    {
        "title": "Замок",
        "author": "Франц Кафка",
        "genre": "Художественная литература",
        "release_date": 1922,
        "description": "Замок - один из известнейших романов автора. Это сочетание реализма и причудливости, "
                       "абсурда и таинственности. Не имеющий концовки, он, возможно, олицетворяет странствие души "
                       "самого Кафки.",
        "cover": "https://cdn1.ozone.ru/s3/multimedia-k/6007802804.jpg"
    },
    {
        "title": "Овод",
        "author": "Этель Лилиан Войнич",
        "genre": "Художественная литература",
        "release_date": 1897,
        "description": "«О́вод» — революционно-романтический роман, наиболее известный русскоязычному читателю труд "
                       "английской, позднее американской писательницы Этель Лилиан Войнич. Впервые вышел в 1897 году "
                       "в США.",
        "cover": "https://fkniga.ru/media/product/04/040404/KA-00408471.jpg"
    },
    {
        "title": "История западной философии",
        "author": "Бертран Рассел",
        "genre": "Философия",
        "release_date": 1945,
        "description": "История западной философии - книга английского математика, философа и общественного деятеля "
                       "Бертрана Рассела, написанная в 1945 году. Представляет собой изложение западной философии от "
                       "досократиков до начала XX века, включает в себя не только собственно философию, но и анализ "
                       "соответствующих эпох и исторический контекст. Книга подвергалась критике за излишние "
                       "обобщения и исключение некоторых направлений, особенно с пост-картезианского периода, "
                       "тем не менее стала очень популярной и коммерчески успешной, много раз переиздавалась. Когда "
                       "Рассел получил Нобелевскую премию по литературе в 1950 году, эта книга считалась главным "
                       "поводом для присуждения премии. ",
        "cover": "https://s3-goods.ozstatic.by/2000/574/579/10/10579574_0.jpg"
    },
    {
        "title": "Странник по звездам",
        "author": "Джек Лондон",
        "genre": "Художественная литература",
        "release_date": 1915,
        "description": "История рассказывается от первого лица заключённым тюрьмы Сан-Квентин (профессором агрономии "
                       "Дэррелом Стэндингом), приговорённым к смертной казни. Долгое время Дэррел пробыл в одиночной "
                       "камере, где многократно подвергался пыткам так называемой «смирительной рубашкой» — куском "
                       "брезента, туго стягивающим всё тело по принципу шнуровки, вызывающим стенокардию. Пытаясь "
                       "смягчить испытываемые мучения, Стэндинг пробует метод «малой смерти» (своего рода состояние "
                       "транса), подсказанный ему другим заключённым с помощью перестукивания. В результате он "
                       "путешествует среди звёзд, а потом испытывает опыт многих своих прошлых воплощений. Описание "
                       "путешествий по своим прошлым жизням представляет собой основной объём книги. ",
        "cover": "https://avatars.mds.yandex.net/i?id=0eb4fbe257e5943643e14476721f0408521c2e64-12652472-images-thumbs&n=13"
    },
    {
        "title": "Защита Лужина",
        "author": "Владимир Набоков",
        "genre": "Художественная литература",
        "release_date": 1929,
        "description": "«Защи́та Лу́жина» — один из наиболее известных романов Владимира Набокова. В основе сюжета — "
                       "история жизни аутистичного шахматного вундеркинда Лужина, в образе которого угадываются черты "
                       "знакомого Набокова — Курта фон Барделебена. При этом существенно, что Лужин русский — "
                       "подробно описано его детство, отношения с родителями, гимназия и эмигрантская среда в Берлине.",
        "cover": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/%D0%9D%D0%B0%D0%B1%D0%BE%D0%BA%D0%BE%D0"
                 "%B2_%D0%92.%D0%92._%D0%97%D0%B0%D1%89%D0%B8%D1%82%D0%B0_%D0%9B%D1%83%D0%B6%D0%B8%D0%BD%D0%B0._"
                 "%281930%29._%E2%80%94_%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F_%D1%81%D1%82%D0%BE%D1%80%D0"
                 "%BE%D0%BD%D0%B0_%D0%BE%D0%B1%D0%BB%D0%BE%D0%B6%D0%BA%D0%B8.jpg/273px-%D0%9D%D0%B0%D0%B1%D0%BE%D0%BA"
                 "%D0%BE%D0%B2_%D0%92.%D0%92._%D0%97%D0%B0%D1%89%D0%B8%D1%82%D0%B0_%D0%9B%D1%83%D0%B6%D0%B8%D0%BD%D0"
                 "%B0._%281930%29._%E2%80%94_%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F_%D1%81%D1%82%D0%BE%D1"
                 "%80%D0%BE%D0%BD%D0%B0_%D0%BE%D0%B1%D0%BB%D0%BE%D0%B6%D0%BA%D0%B8.jpg"
    },
    {
        "title": "Фигуры и складки",
        "author": "Фёдор Гиренок",
        "genre": "Философия",
        "release_date": 2014,
        "description": "В книге впервые выделены и обсуждаются важнейшие классические философские концепты человека: "
                       "человек-кукла Платона, человек-пловец в лодке Декарта, человек-марионетка Канта и "
                       "человек-ночь Гегеля. А также анализируются антропологические идеи Гуссерля, Сартра, Фуко, "
                       "Делёза и других современных мыслителей.",
        "cover": "https://img3.labirint.ru/rc/66767d6181dbc155447f1932e3905a86/363x561q80/books43/421501/cover.jpg?1563738461"
    },
    {
        "title": "Таинственный сад",
        "author": "Фрэнсис Бернетт",
        "genre": "Художественная литература",
        "release_date": 1910,
        "description": "«Таинственный сад» — роман англо-американской писательницы Фрэнсис "
                       "Элизы Бёрнетт. Впервые был опубликован по частям в журнале «Американ-Мэгазин» (ноябрь 1910 — "
                       "август 1911); отдельной книгой был опубликован в 1911 году. Является одной из самых "
                       "популярных книг писательницы. На русском языке впервые была опубликована в журнале «Родникъ», "
                       "предположительно, в 1912 году в переводе Розалии Рубиновой. Этот перевод после большого "
                       "перерыва был переиздан только в 1992 году, в дальнейшем было сделано ещё несколько переводов. ",
        "cover": "https://cdn1.ozone.ru/s3/multimedia-o/6008217924.jpg"
    },
    {
        "title": "Максимы",
        "author": "Франсуа де Ларошфуко",
        "genre": "Философия",
        "release_date": 1665,
        "description": "«Максимы» — второе произведение, написанное де Ларошфуко. В отличие от исторических по своему "
                       "содержанию «Мемуаров» (фр. Mémoires) 1662 года выпуска, «Максимы» — философское произведение, "
                       "в первую очередь освещающее вопросы этики и человеческой психологии. По своей форме «Максимы» "
                       "представляют собой сборник афоризмов, в редких случаях перемежаемых (см. афоризмы 233, "
                       "504) обычным повествовательным текстом[1]. Афоризмы последовательно пронумерованы. Основное "
                       "содержание текста не содержит отдельных структурных элементов. Вместо этого автор, "
                       "затрагивая определённую тему, посвящает ей ряд афоризмов, после чего переходит к рассмотрению "
                       "смежной темы.",
        "cover": "https://xn--80aaph2avkn4e.xn--p1ai/wa-data/public/shop/products/44/17/121744/images/267873/267873.750x0.jpg"
    },
    {
        "title": "Дама с камелиями",
        "author": "Александр Дюма",
        "genre": "Художественная литература",
        "release_date": 1848,
        "description": "Роман повествует о любви между парижской куртизанкой и молодым романтичным парнем Арманом "
                       "Дювалем. Прототипом Маргариты Готье являлась возлюбленная Дюма Мари Дюплесси, которая в 23 "
                       "года умерла от туберкулёза. Из-за болезни сильные запахи были для неё непереносимы; аромат "
                       "роз или гиацинтов вызывал головокружение, поэтому она любила камелии, которые почти не пахнут.",
        "cover": "https://cdn1.ozone.ru/s3/multimedia-1-l/6918416085.jpg"
    },
    {
        "title": "Жажда жизни",
        "author": "Ирвинг Стоун",
        "genre": "Художественная литература",
        "release_date": 1934,
        "description": "Роман американского писателя Ирвинга Стоуна «Жажда жизни» посвящен великому голландскому "
                       "художнику Винсенту Ван Гогу. В нем рассказывается о драматическом жизненном пути Ван Гога, "
                       "о его мощном и небывалом по форме творчестве, так и не получившем признания при жизни "
                       "мастере, о его глубокой вере в то, что «нет ничего более художественного, чем любить людей».",
        "cover": "https://www.knigovoz.ru/media/catalog/products/Stoun_cTEMBMP.jpg"
    },
    {
        "title": "Смерть в кредит",
        "author": "Луи-Фердинард Селин",
        "genre": "Художественная литература",
        "release_date": 1936,
        "description": "В романе «Смерть в кредит» Фердинанд Бардаму, бывший двойник Селина в «Путешествии на край "
                       "ночи», о котором можно сказать, что это своего рода приквел, - парижский врач, "
                       "лечит бедняков, которые редко ему платят, но пользуются всеми преимуществами его доступности. "
                       "Действие не является непрерывным, оно возвращается в прошлое, к более ранним воспоминаниям, "
                       "и часто переходит в область фантазий, особенно в сексуальных похождениях Фердинанда; стиль "
                       "намеренно становится более грубым, а предложения - более лаконичными, чтобы отразить "
                       "повседневные парижские трагедии: борьбу за выживание, болезни, венерические заболевания, "
                       "истории семей, чья судьба зависит от их собственной глупости, злости, похоти и жадности.",
        "cover": "https://media.oki.by/img/catalog/179000/179151_651784.jpg"
    },
    {
        "title": "Призрак Оперы",
        "author": "Леру Гастон",
        "genre": "Художественная литература",
        "release_date": 1910,
        "description": "«При́зрак О́перы» — готический роман Гастона Леру, который "
                       "печатался по частям в газете «Ле-Голуа» с 23 сентября 1909 года по 8 января 1910 года и позже "
                       "был издан отдельным романом. На создание романа Леру вдохновил только что построенный театр "
                       "оперы в Париже, который до сих пор является одним из самых знаменитых театров в мире. Сам "
                       "Леру посвятил роман своему младшему брату Жозефу. ",
        "cover": "https://cdn1.ozone.ru/s3/multimedia-4/6040899928.jpg"
    },
    {
        "title": "Люди Бездны",
        "author": "Джек Лондон",
        "genre": "Художественная литература",
        "release_date": 1903,
        "description": "Книга написана по результатам журналистского расследования, проведённого Джеком Лондоном в "
                       "столице Британской империи. В своём предисловии он объяснил, что летом 1902 года добровольно "
                       "опустился на «дно Лондона»: переодевшись и обретя внешность городского пролетария, "
                       "он некоторое время жил и работал в кварталах Ист-Энда, чтобы собственными глазами увидеть "
                       "степень лишений и повседневных опасностей, переживаемых социальными низами в столице "
                       "мощнейшего государства мира. Автор подчёркивал, что провёл свой эксперимент летом, "
                       "а зимой тяготы этих людей ещё более усугубляются.",
        "cover": "https://xn--80aaph2avkn4e.xn--p1ai/wa-data/public/shop/products/44/03/170344/images/417501/417501"
                 ".750x0.jpg"
    },
    {
        "title": "Норвежский Лес",
        "author": "Харуки Мураками",
        "genre": "Художественная литература",
        "release_date": 1987,
        "description": "Роман «Норвежский лес» принес автору поистине всемирную известность. Тонкие психологические "
                       "нюансы, музыка, наполняющая страницы, эротизм - все это есть в романе, от которого невозможно "
                       "оторваться. Фильм по мотивам бестселлера участвовал в основном конкурсе 67-го Венецианского "
                       "кинофестиваля!",
        "cover": "https://chitatel.by/storage/thumbs/6a/h1001_w1001_6a33f1e646af21f9c28b07fd15cff38c.jpg"
    },
    {
        "title": "Хлеб с ветчиной",
        "author": "Чарльз Буковски",
        "genre": "Художественная литература",
        "release_date": 1982,
        "description": "«Хлеб с ветчиной» — самый проникновенный роман Буковски. Подобно «Приключениям Гекльберри "
                       "Финна» и «Над пропастью во ржи», он написан с точки зрения впечатлительного ребенка, "
                       "имеющего дело с двуличием, претенциозностью и тщеславием взрослого мира. Ребенка, постепенно "
                       "открывающего для себя алкоголь и женщин, азартные игры и мордобой, Д. Г. Лоуренса и "
                       "Хемингуэя, Тургенева и Достоевского.",
        "cover": "https://xn--80aaph2avkn4e.xn--p1ai/wa-data/public/shop/products/65/43/84365/images/160880/160880.750x0.jpg"
    },
    {
        "title": "Страдания юного Вертера",
        "author": "Иоганн Гёте",
        "genre": "Художественная литература",
        "release_date": 1774,
        "description": "Роман «Страдания юного Вертера» стал вторым литературным успехом Гёте после драмы «Гёц фон "
                       "Берлихинген». Как драму, так и роман в письмах относят к направлению «Буря и натиск». "
                       "«Страдания юного Вертера» носят в некоторой степени автобиографический характер, "
                       "в нём в вольной интерпретации Гёте рассказал о своей платонической любви к Шарлотте Буфф. "
                       "Гёте познакомился с ней во время прохождения практики в имперском камеральном суде Вецлара "
                       "летом 1772 года. Мотив трагического исхода любовной истории, суицида Вертера Гёте навеяла "
                       "смерть его друга Карла Вильгельма Иерузалема, страдавшего от любви к замужней женщине. "
                       "Литературный образ Лотты обязан своим появлением другой знакомой Гёте того времени — "
                       "Максимилиане фон Ларош, с которой он познакомился в Зиндлингене. ",
        "cover": "https://chitatel.by/storage/thumbs/ba/h1001_w1001_ba768ea0e0d7573fe3fd9301db7104a1.jpg"
    },
    {
        "title": "Или - или",
        "author": "Сёрен Кьеркегор",
        "genre": "Философия",
        "release_date": 1843,
        "description": "«Или — или» — первая опубликованная работа датского философа Сёрена "
                       "Кьеркегора. Появившись в двух томах в 1843 году под псевдонимом Виктор Эремита (лат. "
                       "Отшельник-победитель), она излагает теорию человеческого существования, отмеченную различием "
                       "между гедонистическим, эстетическим образом жизни и этической жизнью, основанной на "
                       "обязательствах. «Или — или» изображает два взгляда на жизнь. Каждый взгляд на жизнь написан и "
                       "представлен вымышленным автором под псевдонимом, при этом проза произведения отражает и "
                       "зависит от обсуждаемого взгляда на жизнь. Например, «Эстетический взгляд на жизнь» написан в "
                       "форме короткого эссе с поэтическими образами и аллюзиями, в котором обсуждаются такие "
                       "эстетические темы, как музыка, соблазнение, драма и красота.",
        "cover": "https://avatars.mds.yandex.net/i?id=02c3857514c112b9a70fda13402e88abe355b6b2541b1e10-12422470-images-thumbs&n=13"
    },
    {
        "title": "Москва-Петушки",
        "author": "Венедикт Ерофеев",
        "genre": "Художественная литература",
        "release_date": 1969,
        "description": "«Москва́ — Петушки́» — постмодернистская поэма в прозе Венедикта Васильевича Ерофеева. "
                       "Написана в автобиографической манере. Поэма появилась на свет осенью 1969 года (по словам "
                       "автора, за пять недель «на кабельных работах в Шереметьево — Лобня», прокладывался кабель "
                       "телефонной связи). Впервые была опубликована летом 1973 года в Израиле в журнале «АМИ», "
                       "вышедшем тиражом в 300 экземпляров; затем — в 1977 году в Париже. Лирический герой поэмы — "
                       "интеллектуальный алкоголик Веня (Веничка) Ерофеев, едущий на электричке по 124-километровому "
                       "железнодорожному маршруту из Москвы в Петушки к любовнице и ребёнку. Петушки — цель поездки — "
                       "описываются рассказчиком как некое утопическое место. ",
        "cover": "https://varshavskycollection.com/wp-content/uploads/2023/03/LIB-3164.2023-1.jpeg"
    },

]

result = collection.insert_many(books)

print(f"Inserted {len(result.inserted_ids)} documents")

for book in collection.find():
    print(book)

client.close()
