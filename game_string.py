#------------------------ Enemy ----------------------
monsters = {
    # --- Batch 1 ---
    "Owlbear": {
        "Hit": [
            "HIT - Cakar Owlbear merobek pertahananmu!",
            "HIT - Paruh Owlbear menyambar bahumu!",
            "HIT - Serangan ganda Owlbear membuatmu terpental!",
            "HIT - Tubuh besar Owlbear menabrakmu keras!",
            "HIT - Owlbear mengaum dan menghantammu!",
            "HIT - Sayap dan cakarnya menyerang bersamaan!",
            "HIT - Serangan brutal Owlbear membuatmu kehilangan keseimbangan!"
        ],
        "Miss": [
            "MISS - Owlbear meleset saat mencakar!",
            "MISS - Paruhnya mengayun tapi tak mengenai!",
            "MISS - Kau berhasil menghindari tebasan cakarnya!",
            "MISS - Owlbear terpeleset dan serangannya gagal!",
            "MISS - Kau menunduk tepat waktu!",
            "MISS - Serangan beruntunnya tak satu pun kena!",
            "MISS - Owlbear mengaum frustrasi setelah meleset!"
        ]
    },

    "Werewolf": {
        "Hit": [
            "HIT - Werewolf mencakar punggungmu dengan brutal!",
            "HIT - Taringnya hampir menerkammu!",
            "HIT - Serangan cepat Werewolf mengenai dadamu!",
            "HIT - Cakarnya menyayat kulitmu!",
            "HIT - Terjangan Werewolf membuatmu tersungkur!",
            "HIT - Dia menggigit dengan kekuatan tak manusiawi!",
            "HIT - Serangan liar Werewolf menembus pertahananmu!"
        ],
        "Miss": [
            "MISS - Serangan Werewolf meleset tepat di sampingmu!",
            "MISS - Kau menghindar dari cakaran mematikan!",
            "MISS - Werewolf terpeleset sebelum mengenai!",
            "MISS - Taringnya nyaris menyentuhmu!",
            "MISS - Kau berguling keluar dari jangkauannya!",
            "MISS - Serangannya tidak terarah!",
            "MISS - Werewolf menggeram marah setelah meleset!"
        ]
    },

    "Goblin Hexer": {
        "Hit": [
            "HIT - Kutukan Goblin Hexer membuatmu pusing!",
            "HIT - Bola energi gelap menghantammu!",
            "HIT - Racun sihirnya membakar kulitmu!",
            "HIT - Serangan ritual mengenai dadamu!",
            "HIT - Goblin itu tertawa saat kamu terkena mantranya!",
            "HIT - Ledakan sihir kecil mengenai kakimu!",
            "HIT - Kutukan melayang dan langsung mengenaimu!"
        ],
        "Miss": [
            "MISS - Mantranya gagal dan meledak di udara!",
            "MISS - Energi gelapnya meleset dari tubuhmu!",
            "MISS - Kamu menangkis mantra kecilnya!",
            "MISS - Hexer gugup dan salah ucapan!",
            "MISS - Proyektil ajaib melewati bahumu!",
            "MISS - Kau bersembunyi di balik batu!",
            "MISS - Goblin itu mengumpat karena meleset!"
        ]
    },

    "Ogre": {
        "Hit": [
            "HIT - Pukulannya mengenai dan membuatmu limbung!",
            "HIT - Gada besar Ogre menghantammu!",
            "HIT - Terjangan raksasa itu membuatmu terlempar!",
            "HIT - Benturan kuat meretakkan pertahananmu!",
            "HIT - Ogre menghantam tanah hingga pecah dan mengenai dirimu!",
            "HIT - Genggaman besar Ogre mencengkram bahumu!",
            "HIT - Dia menjatuhkanmu dengan pukulan keras!"
        ],
        "Miss": [
            "MISS - Ogre terlalu lambat dan meleset!",
            "MISS - Gada raksasanya menghantam tanah kosong!",
            "MISS - Kamu dengan mudah menghindar!",
            "MISS - Ogre kehilangan keseimbangan!",
            "MISS - Pukulan besar lewat di atas kepalamu!",
            "MISS - Tanah bergetar namun tak terkena dirimu!",
            "MISS - Ogre menggeram bingung saat meleset!"
        ]
    },

    "Grick": {
        "Hit": [
            "HIT - Tentakel Grick mencambuk kakimu!",
            "HIT - Paruhnya menggigit tajam!",
            "HIT - Gerakan cepatnya membuatmu tak siap!",
            "HIT - Serangan mendadak mengenai punggungmu!",
            "HIT - Tentakelnya membelit dan memukul!",
            "HIT - Paruh runcingnya menembus armor!",
            "HIT - Makhluk itu menyerang dua kali berturut-turut!"
        ],
        "Miss": [
            "MISS - Tentakelnya melibas udara!",
            "MISS - Paruh menggigit kosong!",
            "MISS - Kau menarik tubuhmu tepat waktu!",
            "MISS - Serangan cepatnya gagal mengenai!",
            "MISS - Grick memukul batu di sampingmu!",
            "MISS - Kau bergerak terlalu cepat baginya!",
            "MISS - Makhluk itu merayap mundur karena meleset!"
        ]
    },

    # --- Batch 2 ---
    "Mummy": {
        "Hit": [
            "HIT - Pukulan Mummy yang berat menghantam dadamu!",
            "HIT - Debu kutukan mengenaimu!",
            "HIT - Balutan kain mistis menjerat kakimu!",
            "HIT - Serangan lambat namun kuat mengenai kepala!",
            "HIT - Aura kematian membuat tubuhmu lemas!",
            "HIT - Tangan keringnya mencakar kulitmu!",
            "HIT - Kutukan Mummy melemahkan stamina!"
        ],
        "Miss": [
            "MISS - Serangan Mummy terlalu lambat!",
            "MISS - Kainnya hanya menyapu udara!",
            "MISS - Kamu bergerak sebelum pukulannya tiba!",
            "MISS - Debu kutukannya tertiup angin!",
            "MISS - Kau menangkis serangan keringnya!",
            "MISS - Pukulan memecahkan tembok di belakangmu!",
            "MISS - Mummy mengerang ketika gagal!"
        ]
    },

    "Giant Scorpion": {
        "Hit": [
            "HIT - Sengatannya menusuk lenganmu!",
            "HIT - Capit besar menjepit kakimu!",
            "HIT - Racun mematikan mengalir ke tubuhmu!",
            "HIT - Serangan cepat mengejutkanmu!",
            "HIT - Capit menghantam dada!",
            "HIT - Ekor sengat menyodok armor!",
            "HIT - Kau terjatuh oleh hantaman capit!"
        ],
        "Miss": [
            "MISS - Sengatan lewat di sebelah badanmu!",
            "MISS - Capit menjepit udara!",
            "MISS - Kau menghindar dengan cepat!",
            "MISS - Serangannya tidak akurat!",
            "MISS - Ekor terpeleset menghantam tanah!",
            "MISS - Kamu memblok capitnya!",
            "MISS - Scorpion mendesis frustasi!"
        ]
    },

    "Leucrotta": {
        "Hit": [
            "HIT - Gigitan Leucrotta menghancurkan perisaimu!",
            "HIT - Tendangannya membuatmu terpental!",
            "HIT - Rahang kuat merobek dagingmu!",
            "HIT - Serangan gesit membuatmu tak siap!",
            "HIT - Dia menandukmu dengan brutal!",
            "HIT - Cakarannya menyayat bahumu!",
            "HIT - Suara tiruannya membuatmu lengah lalu menyerang!"
        ],
        "Miss": [
            "MISS - Kau menyingkir sebelum rahangnya menutup!",
            "MISS - Tendangannya melenceng jauh!",
            "MISS - Serangannya gagal menipu dirimu!",
            "MISS - Cakaran hanya menggores tanah!",
            "MISS - Kau melompat ke samping!",
            "MISS - Nafas busuknya mengenai udara saja!",
            "MISS - Leucrotta meraung marah!"
        ]
    },

    "Meazel": {
        "Hit": [
            "HIT - Belati berkaratnya melukai tanganmu!",
            "HIT - Serangan teleportasi mengejutkanmu!",
            "HIT - Bayangan gelap mencakar tubuhmu!",
            "HIT - Meazel mencekik dari belakang!",
            "HIT - Jeratan tali panjangnya melilit kakimu!",
            "HIT - Serangan tiba-tiba mengenai wajahmu!",
            "HIT - Dia merobek kulitmu dengan cekikan cepat!"
        ],
        "Miss": [
            "MISS - Teleportasinya meleset dari posisi!",
            "MISS - Belatinya hanya mencakar udara!",
            "MISS - Kau berputar menghindar serangan bayangan!",
            "MISS - Tali jeratnya tak berhasil menangkapmu!",
            "MISS - Dia muncul di tempat yang salah!",
            "MISS - Serangannya kurang akurat!",
            "MISS - Meazel memekik kecewa!"
        ]
    },

    "Giant Spider": {
        "Hit": [
            "HIT - Taring berbisa menembus kulitmu!",
            "HIT - Jaring lengket menahan tubuhmu!",
            "HIT - Kaki raksasanya menusuk pundakmu!",
            "HIT - Gigitan cepat mengenai kakimu!",
            "HIT - Racun mulai menjalar di tubuhmu!",
            "HIT - Spider melompat tepat ke arahmu!",
            "HIT - Serangan jaring menutupi wajahmu!"
        ],
        "Miss": [
            "MISS - Gigitan meleset beberapa inci!",
            "MISS - Jaring menempel ke pohon di belakangmu!",
            "MISS - Kau menghindar tepat waktu!",
            "MISS - Serangannya tak terarah!",
            "MISS - Spider kehilangan pijakan!",
            "MISS - Kakinya hanya menyentuh tanah!",
            "MISS - Makhluk itu memekik karena meleset!"
        ]
    },

    # --- Batch 3 ---
    "Saber Toothed Tiger": {
        "Hit": [
            "HIT - Taring panjangnya menghantam bahumu!",
            "HIT - Cakar besar menyayat tubuhmu!",
            "HIT - Terjangan membuatmu jatuh keras!",
            "HIT - Gigitan kuat mengguncang tubuhmu!",
            "HIT - Hewan itu menerkammu tanpa peringatan!",
            "HIT - Cakar depannya menusuk armor!",
            "HIT - Serangan cepat membuatmu tak siap!"
        ],
        "Miss": [
            "MISS - Taringnya menggores udara!",
            "MISS - Kau melompat menjauh dengan cepat!",
            "MISS - Cakaran liar meleset!",
            "MISS - Tiger terpeleset di tanah!",
            "MISS - Kau berhasil menghindar tepat waktu!",
            "MISS - Serangannya melenceng!",
            "MISS - Ia menggeram setelah gagal!"
        ]
    },

    "Yeti": {
        "Hit": [
            "HIT - Pukulan esnya menghantammu!",
            "HIT - Cakar dingin menyayat tubuhmu!",
            "HIT - Napas dinginnya membekukan tubuhmu!",
            "HIT - Serangan brutal menerbangkanmu!",
            "HIT - Yeti memukul tanah hingga pecah dan serpihannya mengenai dirimu!",
            "HIT - Tubuhmu membeku sebagian!",
            "HIT - Dia menghempaskanmu ke dinding es!"
        ],
        "Miss": [
            "MISS - Pukulan besar itu meleset!",
            "MISS - Serangan dingin tidak mengenaimu!",
            "MISS - Kau berlindung di balik batu!",
            "MISS - Cakaran mengenai es di belakangmu!",
            "MISS - Yeti terlalu lambat!",
            "MISS - Kau menghindar sebelum ia siap menyerang!",
            "MISS - Yeti meraung frustrasi!"
        ]
    },

    "Winter Wolf": {
        "Hit": [
            "HIT - Gigitan dingin menggigit kulitmu!",
            "HIT - Nafas beku mengenai tubuhmu!",
            "HIT - Cakaran cepat menyayat lenganmu!",
            "HIT - Serangan timnya terkoordinasi!",
            "HIT - Dia menabrakmu dengan tubuh besar!",
            "HIT - Es tipis muncul dan membuatmu jatuh!",
            "HIT - Gigitan kedua mengenai bahumu!"
        ],
        "Miss": [
            "MISS - Kau melompat sebelum napas beku mengenamu!",
            "MISS - Cakaran meleset!",
            "MISS - Es membeku di tempat yang salah!",
            "MISS - Serangannya tidak mengenai target!",
            "MISS - Wolf terpeleset di esnya sendiri!",
            "MISS - Gigitan hanya mengenai udara!",
            "MISS - Kau berlari keluar jangkauannya!"
        ]
    },

    "Polar Bear": {
        "Hit": [
            "HIT - Cakar besar menghantammu!",
            "HIT - Gigitan kuat mengenai bahumu!",
            "HIT - Beruang itu menjatuhkanmu dengan tubuhnya!",
            "HIT - Serangan cepat mengejutkanmu!",
            "HIT - Pukulan depan hampir mematahkan tulangmu!",
            "HIT - Dia menggigit kakimu!",
            "HIT - Kau terkena serangan bertubi-tubi!"
        ],
        "Miss": [
            "MISS - Cakar besar itu meleset!",
            "MISS - Kau berguling keluar dari jangkauan!",
            "MISS - Gigitan beruang tidak mengenai apa-apa!",
            "MISS - Serangannya lambat!",
            "MISS - Beruang terpeleset di es!",
            "MISS - Kau menangkis dengan senjata!",
            "MISS - Dia mengaum karena gagal!"
        ]
    },

    "Manticore": {
        "Hit": [
            "HIT - Duri ekornya menancap di tubuhmu!",
            "HIT - Cakar manticore menghantam dada!",
            "HIT - Gigitan brutal mengenai lenganmu!",
            "HIT - Rentetan duri mengenai kakimu!",
            "HIT - Dia menabrakmu dengan sayap runcing!",
            "HIT - Serangan ekor bertubi-tubi membuatmu terkejut!",
            "HIT - Kau terkena gigitan kedua!"
        ],
        "Miss": [
            "MISS - Duri ekor meleset!",
            "MISS - Cakaran hanya menyentuh tanah!",
            "MISS - Kau menghindar dari gigitan!",
            "MISS - Tembakan duri tidak akurat!",
            "MISS - Manticore terbang melewatimu!",
            "MISS - Serangannya gagal karena angin!",
            "MISS - Dia meraung karena meleset!"
        ]
    },

    # --- Batch 4 ---
    "Basilisk": {
        "Hit": [
            "HIT - Gigitan kuat basilisk mengenai lenganmu!",
            "HIT - Ekor keras memukul punggungmu!",
            "HIT - Tatapan mematung melemahkanmu!",
            "HIT - Serangan cepat mengejutkanmu!",
            "HIT - Taring beracun menyayat kulitmu!",
            "HIT - Dia melilitkan tubuhnya padamu!",
            "HIT - Gigitannya hampir mematungkan tubuhmu!"
        ],
        "Miss": [
            "MISS - Kau menutup mata dan menghindar!",
            "MISS - Gigitan meleset dari pundakmu!",
            "MISS - Ekor menghantam batu!",
            "MISS - Serangan beracun gagal!",
            "MISS - Basilisk tergelincir!",
            "MISS - Kau menangkis dengan perisai!",
            "MISS - Tatapannya tidak mengenai dirimu!"
        ]
    },

    "Griffon": {
        "Hit": [
            "HIT - Cakar griffon merobek armor!",
            "HIT - Paruh besar menghantam pundakmu!",
            "HIT - Dia menyapumu dari udara!",
            "HIT - Serangan terbang menghantammu keras!",
            "HIT - Cakar belakang mencabik kulitmu!",
            "HIT - Kau terkena pukulan sayap!",
            "HIT - Paruh griffon mematuk dengan cepat!"
        ],
        "Miss": [
            "MISS - Serangan udara meleset!",
            "MISS - Kau berjongkok tepat waktu!",
            "MISS - Paruh hanya menggores udara!",
            "MISS - Cakar meleset dari tubuhmu!",
            "MISS - Griffon kehilangan sudut serangan!",
            "MISS - Sayapnya tak mengenai apa-apa!",
            "MISS - Dia terbang melampai batas jangkauan!"
        ]
    },

    "Neogi": {
        "Hit": [
            "HIT - Gigitan tajam Neogi mengenaimu!",
            "HIT - Racun melemahkan ototmu!",
            "HIT - Serangan psionik membuat kepalamu pusing!",
            "HIT - Cakaran kecilnya merobek kulitmu!",
            "HIT - Dia menyentuhmu dan memaksakan kehendaknya!",
            "HIT - Tentakel pendeknya memukul wajahmu!",
            "HIT - Kau terkena gigitan kedua!"
        ],
        "Miss": [
            "MISS - Serangan psionik gagal!",
            "MISS - Gigitan meleset!",
            "MISS - Kau menghindar dari tentakel!",
            "MISS - Neogi kehilangan fokus!",
            "MISS - Serangannya melenceng jauh!",
            "MISS - Racun gagal mengenai kulitmu!",
            "MISS - Ia memaki setelah meleset!"
        ]
    },

    "Harpy": {
        "Hit": [
            "HIT - Cakar tajam harpy menghantammu!",
            "HIT - Suaranya memikat lalu dia menyerang!",
            "HIT - Dia mencakar wajahmu dengan cepat!",
            "HIT - Pukulan sayap keras mengenai tubuhmu!",
            "HIT - Paruh kecilnya mencabik kulitmu!",
            "HIT - Serangan terbang menjatuhkanmu!",
            "HIT - Harpy mencengkeram pundakmu!"
        ],
        "Miss": [
            "MISS - Nyanyiannya gagal mempengaruhimu!",
            "MISS - Cakaran meleset!",
            "MISS - Kau merunduk tepat waktu!",
            "MISS - Dia terbang terlalu tinggi!",
            "MISS - Serangan sayap tidak akurat!",
            "MISS - Paruh mengenai batu!",
            "MISS - Harpy menjerit marah!"
        ]
    },

    "Giant Vulture": {
        "Hit": [
            "HIT - Paruh besar mencabik bahumu!",
            "HIT - Cakar kuat mencengkeram lenganmu!",
            "HIT - Vulture mematuk berulang-ulang!",
            "HIT - Serangan terbang menghantammu!",
            "HIT - Dia menarik rambut atau helm-mu!",
            "HIT - Cakaran belakang merobek baju perang!",
            "HIT - Kau terkena patukan keras!"
        ],
        "Miss": [
            "MISS - Patukan meleset!",
            "MISS - Sayap mengibas tapi gagal menabrakmu!",
            "MISS - Kau menghindar dari cakarannya!",
            "MISS - Serangannya tidak terarah!",
            "MISS - Vulture kehilangan ketinggian!",
            "MISS - Patukan kedua melenceng!",
            "MISS - Makhluk itu memekik kecewa!"
        ]
    },

    # --- Batch 5 ---
    "Ghoul": {
        "Hit": [
            "HIT - Cakaran busuk ghoul merobek kulitmu!",
            "HIT - Gigitan menjijikkan mengenai bahumu!",
            "HIT - Serangan cepat membuatmu tak siap!",
            "HIT - Racun paralyzing mulai membuatmu kaku!",
            "HIT - Ghoul mencakar wajahmu!",
            "HIT - Dia menggigit dengan buas!",
            "HIT - Tubuhmu mulai melemah!"
        ],
        "Miss": [
            "MISS - Cakaran ghoul meleset!",
            "MISS - Gigitan membentur udara!",
            "MISS - Kau bergerak lebih cepat!",
            "MISS - Ghoul terpeleset!",
            "MISS - Serangan liar tidak akurat!",
            "MISS - Kau menangkis dengan senjata!",
            "MISS - Makhluk itu menggeram frustrasi!"
        ]
    },

    "Giant Crocodile": {
        "Hit": [
            "HIT - Rahang besar menggigit kakimu!",
            "HIT - Ekor kuat menghantam tubuhmu!",
            "HIT - Kubangan air memperkuat serangannya!",
            "HIT - Gigitan brutal hampir menarikmu masuk air!",
            "HIT - Cakar besar mencakar dadamu!",
            "HIT - Serangan renang cepat mengejutkanmu!",
            "HIT - Dia menjepitmu dengan rahang besi!"
        ],
        "Miss": [
            "MISS - Gigitan besar meleset!",
            "MISS - Kau meloncat dari air!",
            "MISS - Ekor menghantam kosong!",
            "MISS - Crocodile tidak cukup cepat!",
            "MISS - Kau memblok serangan airnya!",
            "MISS - Rahang menutup sedikit terlambat!",
            "MISS - Makhluk itu mengibas air marah!"
        ]
    },

    "Giant Snakes": {
        "Hit": [
            "HIT - Gigitan berbisa mengenai lengamu!",
            "HIT - Tubuhnya melilit tubuhmu kuat!",
            "HIT - Serangan cepat mencaplok pundakmu!",
            "HIT - Lilitan mempersempit udara pernapasanmu!",
            "HIT - Taring beracun masuk ke kulit!",
            "HIT - Dia menjatuhkanmu lalu membelit!",
            "HIT - Serangan mendadak membuatmu terkejut!"
        ],
        "Miss": [
            "MISS - Gigitan meleset dari tubuhmu!",
            "MISS - Kau melepaskan diri sebelum lilitan kuat!",
            "MISS - Kepala ular meluncur namun tidak mengenai!",
            "MISS - Dia kehilangan momentum!",
            "MISS - Kau melompat mundur!",
            "MISS - Serangannya terlalu terbaca!",
            "MISS - Ular menggelepar marah!"
        ]
    },

    "Flail Snail": {
        "Hit": [
            "HIT - Tentakel kerasnya memukul kakimu!",
            "HIT - Serangan flail menghantam dadamu!",
            "HIT - Cangkangnya memantulkan energi ke tubuhmu!",
            "HIT - Tentakel liar mengenai wajahmu!",
            "HIT - Energi berwarna memantul dan melukaimu!",
            "HIT - Dia memukul dengan kekuatan mengejutkan!",
            "HIT - Serangan beruntun tentakel mengenai tubuhmu!"
        ],
        "Miss": [
            "MISS - Tentakel meleset!",
            "MISS - Kau berguling menghindar!",
            "MISS - Energi memantul ke arah lain!",
            "MISS - Serangannya lambat!",
            "MISS - Tentakel hanya menghantam tanah!",
            "MISS - Cangkang berputar arah salah!",
            "MISS - Flail Snail mendesis kesal!"
        ]
    },

    "Wight": {
        "Hit": [
            "HIT - Serangan necrotic merenggut sebagian kehidupanmu!",
            "HIT - Pedang kegelapan menghantam tubuhmu!",
            "HIT - Sentuhan dinginnya menyerap energi!",
            "HIT - Wight menusuk sisi tubuhmu!",
            "HIT - Aura kematian membuatmu lemas!",
            "HIT - Dia melukai dengan kekuatan tak kasat mata!",
            "HIT - Serangan kedua menambah kerusakan jiwamu!"
        ],
        "Miss": [
            "MISS - Energi gelap melewati tubuhmu!",
            "MISS - Pedang wight meleset!",
            "MISS - Kau menghindar dari sentuhan kematian!",
            "MISS - Serangan magisnya tidak fokus!",
            "MISS - Kau menangkis dengan perisai!",
            "MISS - Wight tersentak mundur!",
            "MISS - Dia menggeram karena gagal!"
        ]
    }
}


#ini belom jadi. tadinya tiap serangan mau ada deskripsi kayak gini

#------------------------ Help ----------------------
help_command = {
    'cek' : (
        'Perintah \'cek\' digunakan untuk melihat daftar item dalam kategori tertentu.',
        'Kategori cek: ability, status, buah, equipment.',
        'Contoh penggunaan: cek buah'
    ),
    'jalan' : (
        'Perintah \'jalan\' digunakan untuk memulai perjalanan menjauh dari rumah.',
        'Setiap kali kamu menggunakan perintah ini, posisimu akan bertambah 50 meter.'
    ),
    'exit' : (
        'Perintah \'exit\' digunakan untuk keluar dari permainan.',
    ),
    'equipment' : (
        'Armor berfungsi untuk mengurangi kemungkinanmu terkena serangan musuh.',
        'Weapon adalah senjata yang kamu gunakan.'
    ),
    'objective' : (
        'Tujuan utama game ini adalah mengumpulkan buah-buahan.',
        'Kumpulkan masing-masing 5 dan berhasil kembali ke rumah untuk menyelesaikan permainan'
    )
}

#Nanti fungsi help bakal ngereferensiin ini