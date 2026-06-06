#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the "Young Docents of the Southern Branch" bilingual course site.

A gift for the English teachers of Chiayi County Yung Ching Senior High School
(嘉義縣立永慶高級中學), produced by My Culture Connect 人師教育協會.

The course turns the National Palace Museum · Southern Branch — the world-class
Asian art museum on Yung Ching's doorstep — into a place-based bilingual course
that trains students to give a 2-minute English gallery tour.

    python3 build.py      # regenerates index.html + the 8 lesson folders

This generator is itself a demo of "making bilingual materials with AI": one
template + per-lesson content -> a whole course. Swap the content dicts for a
different landmark and the same machine produces a new course.
"""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE = "Young Docents of the Southern Branch"
SITE_ZH = "南院小小英語導覽員"
SCHOOL = "Yung Ching Senior High School"
SCHOOL_ZH = "嘉義縣立永慶高級中學"

# ----------------------------------------------------------------------------
# LESSON CONTENT
# Each reading paragraph is {en, zh}; "term" spans highlight target vocabulary.
# Quiz options are English only (Chinese lives in the stem hint + explanation).
# ----------------------------------------------------------------------------

LESSONS = [
    {
        "slug": "welcome",
        "num": 1,
        "title_en": "Welcome to the Southern Branch",
        "title_zh": "歡迎來到故宮南院",
        "tagline_en": "The museum at our doorstep — and the words to open its door.",
        "tagline_zh": "門口的博物館，與打開它大門的那幾句英文。",
        "gallery": "Orientation · 全館導覽",
        "tone": "",
        "reading": [
            {"en": 'Just a few minutes from our classrooms stands one of the most important museums in Asia: the <span class="term">Southern Branch</span> of the National Palace Museum, in Taibao City. While the original museum in Taipei is famous for Chinese treasures, the Southern Branch has a wider mission. It is an <span class="term">Asian Art and Culture Museum</span> — a place that tells the story of the whole continent.',
             "zh": "離我們教室只要幾分鐘，就矗立著亞洲最重要的博物館之一：位於太保市的「國立故宮博物院南部院區」。臺北的故宮以中國文物聞名，南院的使命卻更寬廣——它是一座「亞洲藝術文化博物館」，述說整個亞洲大陸的故事。"},
            {"en": 'The museum opened in 2015. Its address — 888 Gugong Boulevard — sits beside the high-speed rail station and the seat of Chiayi County. For an international traveller stepping off the train, the Southern Branch is often their first <span class="term">impression</span> of southern Taiwan. That is exactly why a <span class="term">docent</span> — a trained guide who explains the artworks — matters so much.',
             "zh": "南院於 2015 年開幕，地址「故宮大道 888 號」就在高鐵站與嘉義縣治旁邊。對一位剛下車的國際旅客來說，南院往往是他們對台灣南部的第一印象——這正是為什麼一位受過訓練、能解說作品的「導覽員（docent）」如此重要。"},
            {"en": 'In this course you will become a young docent. You will not memorise everything; instead you will learn how to <span class="term">introduce</span> one gallery, describe one object, and answer a visitor’s question — all in clear, friendly English. By the final lesson you will give a short tour of your own.',
             "zh": "在這門課裡，你會成為一位小小導覽員。你不必背下所有東西，而是學會如何用清楚、友善的英文「介紹」一個展廳、描述一件文物、回答訪客的提問。到最後一課，你將親自帶一段簡短的導覽。"},
        ],
        "pull_quote": {"en": "A docent is not someone who knows everything. A docent is someone who helps you see.",
                       "zh": "導覽員不是無所不知的人，而是幫助你「看見」的人。"},
        "vocab": [
            {"word": "branch", "pos": "(n.)", "def": "a part of a larger organisation in a different location", "zh": "分院；分支機構",
             "eg": "The Southern Branch is part of the National Palace Museum."},
            {"word": "docent", "pos": "(n.)", "def": "a person who guides visitors and explains the artworks in a museum", "zh": "（博物館）導覽員",
             "eg": "Our docent explained the painting in simple English."},
            {"word": "exhibit", "pos": "(n.)", "def": "an object or collection shown to the public in a museum", "zh": "展品；展覽",
             "eg": "This exhibit shows ceramics from across Asia."},
            {"word": "gallery", "pos": "(n.)", "def": "a room or hall where artworks are displayed", "zh": "展廳；藝廊",
             "eg": "Please follow me into the next gallery."},
            {"word": "collection", "pos": "(n.)", "def": "a group of objects gathered and kept together", "zh": "館藏；收藏",
             "eg": "The museum's collection comes from many Asian cultures."},
            {"word": "introduce", "pos": "(v.)", "def": "to present something to people for the first time", "zh": "介紹",
             "eg": "Let me introduce the most famous object in this room."},
            {"word": "impression", "pos": "(n.)", "def": "the feeling or opinion you form about something", "zh": "印象",
             "eg": "The building gives visitors a strong first impression."},
        ],
        "phrases": [
            {"en": "Welcome to the Southern Branch of the National Palace Museum.", "zh": "歡迎來到國立故宮博物院南部院區。"},
            {"en": "My name is ___, and I'll be your guide today.", "zh": "我叫 ___，今天由我為您導覽。"},
            {"en": "Please follow me, and feel free to ask questions.", "zh": "請跟我來，也歡迎隨時提問。"},
            {"en": "This way, please. Our first gallery is just ahead.", "zh": "這邊請，第一個展廳就在前方。"},
            {"en": "Thank you for visiting. I hope you enjoyed the tour.", "zh": "謝謝您的參觀，希望您喜歡這趟導覽。"},
        ],
        "quiz": [
            {"stem": "What kind of museum is the Southern Branch?",
             "zh": "南院是哪一種博物館？",
             "options": [{"t": "A museum of Asian art and culture", "correct": True},
                         {"t": "A museum of European paintings", "correct": False},
                         {"t": "A natural science museum", "correct": False},
                         {"t": "A museum of modern technology", "correct": False}],
             "explain_en": "The Southern Branch is positioned as an Asian Art and Culture Museum — broader than the Taipei museum's focus on Chinese treasures.",
             "explain_zh": "南院定位為「亞洲藝術文化博物館」，視野比臺北故宮的中國文物更寬廣。"},
            {"stem": "A docent is best described as someone who ___.",
             "zh": "「docent」最適合的描述是？",
             "options": [{"t": "guides visitors and explains the artworks", "correct": True},
                         {"t": "sells tickets at the entrance", "correct": False},
                         {"t": "paints the pictures in the gallery", "correct": False},
                         {"t": "cleans the museum at night", "correct": False}],
             "explain_en": "A docent is a trained guide who helps visitors understand what they are seeing.",
             "explain_zh": "docent 是受過訓練的導覽員，幫助訪客理解眼前的作品。"},
            {"stem": "Which sentence would you say to begin a tour?",
             "zh": "開始導覽時你會說哪一句？",
             "options": [{"t": "Welcome to the Southern Branch. I'll be your guide today.", "correct": True},
                         {"t": "Goodbye, and thank you for coming.", "correct": False},
                         {"t": "The museum is now closed.", "correct": False},
                         {"t": "Please pay at the counter.", "correct": False}],
             "explain_en": "You open a tour with a welcome and by introducing yourself as the guide.",
             "explain_zh": "導覽的開場是先歡迎訪客，並介紹自己是今天的導覽員。"},
            {"stem": "In which year did the Southern Branch open?",
             "zh": "南院哪一年開幕？",
             "options": [{"t": "2015", "correct": True},
                         {"t": "1965", "correct": False},
                         {"t": "2009", "correct": False},
                         {"t": "2020", "correct": False}],
             "explain_en": "The Southern Branch opened in 2015 in Taibao City, beside the high-speed rail.",
             "explain_zh": "南院於 2015 年在太保市、高鐵站旁開幕。"},
        ],
        "your_turn": {
            "title": "Introduce yourself as a guide",
            "intro_en": "Write three sentences you would say in the first minute of a tour.",
            "intro_zh": "寫下導覽第一分鐘你會說的三句話。",
            "steps": [
                "Welcome the visitors to the Southern Branch.",
                "Say your name and that you are their guide today.",
                "Invite them to follow you and to ask questions.",
            ],
        },
    },

    {
        "slug": "building",
        "num": 2,
        "title_en": "Reading the Building",
        "title_zh": "讀一棟建築",
        "tagline_en": "Before the art begins, the architecture is already speaking.",
        "tagline_zh": "在藝術開始之前，建築本身已經在說話。",
        "gallery": "Architecture · 建築 (Kris Yao / 姚仁喜)",
        "tone": "tone-jade",
        "reading": [
            {"en": 'The museum was designed by the Taiwanese architect <span class="term">Kris Yao</span> (姚仁喜). Before you see a single artwork, the building itself tells a story. Its shape was inspired by Chinese <span class="term">calligraphy</span> — the art of writing with brush and ink.',
             "zh": "南院由台灣建築師姚仁喜（Kris Yao）設計。在你看到任何一件作品之前，建築本身已在訴說故事。它的造型靈感來自中國書法——用毛筆與墨書寫的藝術。"},
            {"en": 'Yao used three brush <span class="term">techniques</span> as his design language: <em>solid ink</em> (濃墨), the heavy black stroke; <em>flying white</em> (飛白), the dry stroke that lets white show through; and <em>wash</em> (渲染), the soft, spreading tone. Three flowing volumes <span class="term">curve</span> and cross like brushstrokes frozen in glass and stone.',
             "zh": "姚仁喜以三種筆法作為設計語言：「濃墨」沉重的黑線、「飛白」乾筆中透出的白、「渲染」柔和暈開的層次。三道流動的量體彎曲、交織，宛如凝結在玻璃與石材裡的筆畫。"},
            {"en": 'The three volumes also stand for three great Asian civilisations meeting one another: the <span class="term">dragon</span> for China, the <span class="term">elephant</span> for India, and the horse for Persia. So the building is really a picture of Yung Ching’s own motto — “connect with the world.” The art inside is Asian; the architecture says why that matters.',
             "zh": "這三道量體也象徵三大亞洲文明的交會：「龍」代表中國、「象」代表印度、「馬」代表波斯。於是這棟建築其實就是永慶校訓「接國際」的具象——館內的藝術屬於亞洲，建築則說明了它為何重要。"},
        ],
        "pull_quote": {"en": "Dragon, elephant, horse — China, India, Persia. The building is three civilisations shaking hands.",
                       "zh": "龍、象、馬——中國、印度、波斯。這棟建築，是三個文明握手的瞬間。"},
        "vocab": [
            {"word": "architect", "pos": "(n.)", "def": "a person who designs buildings", "zh": "建築師",
             "eg": "The architect was inspired by Chinese calligraphy."},
            {"word": "calligraphy", "pos": "(n.)", "def": "the art of beautiful handwriting, often with a brush", "zh": "書法",
             "eg": "The roof line flows like a stroke of calligraphy."},
            {"word": "stroke", "pos": "(n.)", "def": "a single movement of a brush or pen", "zh": "筆畫；一筆",
             "eg": "Each curve of the building is like a brush stroke."},
            {"word": "curve", "pos": "(v.)", "def": "to bend in a smooth, rounded line", "zh": "彎曲；呈弧形",
             "eg": "The glass walls curve gently toward the lake."},
            {"word": "symbolise", "pos": "(v.)", "def": "to represent an idea or thing", "zh": "象徵",
             "eg": "The three volumes symbolise three Asian civilisations."},
            {"word": "civilisation", "pos": "(n.)", "def": "a society with its own culture, art, and history", "zh": "文明",
             "eg": "China, India, and Persia were three great Asian civilisations."},
            {"word": "inspire", "pos": "(v.)", "def": "to give someone the idea for something", "zh": "啟發；給予靈感",
             "eg": "Calligraphy inspired the shape of the museum."},
        ],
        "phrases": [
            {"en": "Look up at the roof — its curves come from Chinese calligraphy.", "zh": "請抬頭看屋頂——它的曲線來自中國書法。"},
            {"en": "The architect used three brush techniques: solid ink, flying white, and wash.", "zh": "建築師運用三種筆法：濃墨、飛白與渲染。"},
            {"en": "The three shapes stand for China, India, and Persia.", "zh": "這三個造型分別代表中國、印度與波斯。"},
            {"en": "Notice how the glass curves like a brushstroke.", "zh": "請注意玻璃如何像筆畫一樣彎曲。"},
            {"en": "The building itself is a symbol of meeting between cultures.", "zh": "這棟建築本身就是文化交會的象徵。"},
        ],
        "quiz": [
            {"stem": "What inspired the shape of the museum?",
             "zh": "博物館的造型靈感來自什麼？",
             "options": [{"t": "Chinese calligraphy", "correct": True},
                         {"t": "A sailing ship", "correct": False},
                         {"t": "A mountain range", "correct": False},
                         {"t": "A computer chip", "correct": False}],
             "explain_en": "Kris Yao based the design on three brush techniques of Chinese calligraphy.",
             "explain_zh": "姚仁喜以中國書法的三種筆法為設計依據。"},
            {"stem": "The three volumes of the building symbolise ___.",
             "zh": "建築的三道量體象徵？",
             "options": [{"t": "China, India, and Persia", "correct": True},
                         {"t": "Past, present, and future", "correct": False},
                         {"t": "Earth, water, and sky", "correct": False},
                         {"t": "Reading, writing, and speaking", "correct": False}],
             "explain_en": "Dragon (China), elephant (India), and horse (Persia) — three Asian civilisations meeting.",
             "explain_zh": "龍（中國）、象（印度）、馬（波斯）——三大亞洲文明的交會。"},
            {"stem": "Which word means 'the art of beautiful handwriting'?",
             "zh": "哪個字意思是「美麗書寫的藝術」？",
             "options": [{"t": "calligraphy", "correct": True},
                         {"t": "photography", "correct": False},
                         {"t": "geography", "correct": False},
                         {"t": "biology", "correct": False}],
             "explain_en": "Calligraphy is writing as a fine art, usually with brush and ink.",
             "explain_zh": "calligraphy 指作為精緻藝術的書寫，通常用毛筆與墨。"},
            {"stem": "Why does the building suit Yung Ching's motto 'connect with the world'?",
             "zh": "為什麼這棟建築呼應永慶校訓「接國際」？",
             "options": [{"t": "It pictures three civilisations meeting", "correct": True},
                         {"t": "It is the tallest building in Taiwan", "correct": False},
                         {"t": "It was built by a foreign company", "correct": False},
                         {"t": "It only displays Taiwanese art", "correct": False}],
             "explain_en": "The architecture shows different Asian cultures coming together — exactly what 'connect with the world' means.",
             "explain_zh": "建築呈現不同亞洲文化的交會，正是「接國際」的意涵。"},
        ],
        "your_turn": {
            "title": "Describe the building in three sentences",
            "intro_en": "Imagine pointing at the museum from the lake. Describe its shape to a visitor.",
            "intro_zh": "想像你在湖邊指著博物館，向訪客描述它的造型。",
            "steps": [
                "Say what inspired the shape (calligraphy).",
                "Name the three brush techniques OR the three civilisations.",
                "Use one verb of movement: curve, flow, cross, or rise.",
            ],
        },
    },

    {
        "slug": "blue-and-white",
        "num": 3,
        "title_en": "Blue-and-White",
        "title_zh": "青花——亞洲陶瓷之美",
        "tagline_en": "One colour, fired in fire, traded across an ocean.",
        "tagline_zh": "一種顏色，經火淬煉，越洋而行。",
        "gallery": "Gallery · 青花—亞洲陶瓷美學",
        "tone": "",
        "reading": [
            {"en": 'In the ceramics gallery you meet an old friend you have seen all your life: white <span class="term">porcelain</span> painted with deep blue. We call it <span class="term">blue-and-white</span>. The blue comes from a mineral called <span class="term">cobalt</span>, painted onto the clay before a clear glaze is added.',
             "zh": "在陶瓷展廳，你會遇見一位你一生都見過的老朋友：白瓷上繪著深藍的紋飾，我們稱它「青花」。那抹藍來自一種叫「鈷」的礦物，在上透明釉之前先畫於坯體上。"},
            {"en": 'The piece is then <span class="term">fired</span> in a kiln at a very high temperature. Under the heat the cobalt turns a brilliant blue and the glaze becomes glassy and smooth. A single firing can decide whether years of work become a treasure or a crack.',
             "zh": "接著作品被送入窯中以極高溫「燒製」。在高溫下，鈷轉為鮮亮的藍，釉面則變得如玻璃般光滑。一次燒製，就決定了多年心血是成為珍寶，還是化為裂痕。"},
            {"en": 'Blue-and-white was one of the great <span class="term">trade</span> goods of Asia. Ships carried it from China to Persia, India, and beyond; potters in other lands copied and changed the <span class="term">patterns</span>. So a single blue bowl can hold the whole story of this museum: many cultures, one shining object.',
             "zh": "青花曾是亞洲最重要的貿易商品之一。船隻將它從中國運往波斯、印度乃至更遠；各地的陶工臨摹、改造這些紋樣。於是一只藍色的碗，便能承載整座博物館的故事：多元文化，凝於一件閃亮的器物。"},
        ],
        "pull_quote": {"en": "A blue bowl is a small map of Asia: made in one land, loved in many.",
                       "zh": "一只青花碗，是亞洲的小地圖：產於一地，見愛於四方。"},
        "vocab": [
            {"word": "porcelain", "pos": "(n.)", "def": "a hard, white, fine type of ceramic", "zh": "瓷；瓷器",
             "eg": "The bowl is made of thin white porcelain."},
            {"word": "ceramic", "pos": "(n.)", "def": "an object made of clay and hardened by heat", "zh": "陶瓷（製品）",
             "eg": "This gallery is full of Asian ceramics."},
            {"word": "cobalt", "pos": "(n.)", "def": "a metal that gives a deep blue colour", "zh": "鈷（呈深藍色的金屬）",
             "eg": "The blue comes from cobalt under the glaze."},
            {"word": "glaze", "pos": "(n.)", "def": "a glassy coating on pottery", "zh": "釉",
             "eg": "A clear glaze covers the painted design."},
            {"word": "fire", "pos": "(v.)", "def": "to bake clay in a kiln at high heat", "zh": "燒製（陶瓷）",
             "eg": "The potter fires the vase in a hot kiln."},
            {"word": "pattern", "pos": "(n.)", "def": "a repeated decorative design", "zh": "紋樣；圖案",
             "eg": "Dragons and flowers are common patterns."},
            {"word": "trade", "pos": "(n.)", "def": "the buying and selling of goods between places", "zh": "貿易",
             "eg": "Blue-and-white was a famous trade good."},
        ],
        "phrases": [
            {"en": "This is blue-and-white porcelain. The blue comes from cobalt.", "zh": "這是青花瓷，藍色來自鈷。"},
            {"en": "The artist painted the design before firing it in a kiln.", "zh": "工匠在入窯燒製前先畫上紋飾。"},
            {"en": "Look closely at the pattern — can you find the dragon?", "zh": "仔細看這紋樣——你能找到那條龍嗎？"},
            {"en": "Pieces like this were traded across Asia by ship.", "zh": "像這樣的器物曾由船隻運送、行銷亞洲各地。"},
            {"en": "Notice how smooth and glassy the glaze is.", "zh": "請注意釉面多麼光滑、如玻璃般晶亮。"},
        ],
        "quiz": [
            {"stem": "Where does the blue colour in blue-and-white come from?",
             "zh": "青花的藍色來自什麼？",
             "options": [{"t": "A mineral called cobalt", "correct": True},
                         {"t": "Blue paint added after firing", "correct": False},
                         {"t": "The natural colour of the clay", "correct": False},
                         {"t": "Blue light in the gallery", "correct": False}],
             "explain_en": "The blue is cobalt, painted on before the glaze and turned brilliant by firing.",
             "explain_zh": "藍色是鈷，在上釉前畫上，經燒製後轉為鮮亮的藍。"},
            {"stem": "What happens to a piece in the kiln?",
             "zh": "器物在窯中會發生什麼？",
             "options": [{"t": "It is fired at high heat until hard and glassy", "correct": True},
                         {"t": "It is frozen to keep its shape", "correct": False},
                         {"t": "It is painted by a machine", "correct": False},
                         {"t": "It is dipped in cold water", "correct": False}],
             "explain_en": "Firing at high temperature hardens the clay and turns the glaze glassy.",
             "explain_zh": "高溫燒製使坯體變硬、釉面如玻璃。"},
            {"stem": "Why is blue-and-white a good symbol for this museum?",
             "zh": "為什麼青花很適合作為這座博物館的象徵？",
             "options": [{"t": "It was made in one land but loved across many Asian cultures", "correct": True},
                         {"t": "It is the cheapest object in the museum", "correct": False},
                         {"t": "It was only used in Taiwan", "correct": False},
                         {"t": "It cannot be moved or traded", "correct": False}],
             "explain_en": "Blue-and-white travelled and was copied across Asia — many cultures, one object.",
             "explain_zh": "青花流通並被亞洲各地臨摹——多元文化、一件器物。"},
            {"stem": "Which word means 'a glassy coating on pottery'?",
             "zh": "哪個字意思是「陶瓷上如玻璃的塗層」？",
             "options": [{"t": "glaze", "correct": True},
                         {"t": "kiln", "correct": False},
                         {"t": "cobalt", "correct": False},
                         {"t": "pattern", "correct": False}],
             "explain_en": "Glaze is the clear, glassy layer over the painted design.",
             "explain_zh": "glaze（釉）是覆蓋在彩繪紋飾上、透明如玻璃的塗層。"},
        ],
        "your_turn": {
            "title": "Describe one blue-and-white piece",
            "intro_en": "Pick a bowl or vase (real or imagined) and describe it to a visitor.",
            "intro_zh": "選一件碗或瓶（真實或想像），向訪客描述它。",
            "steps": [
                "Name the material (porcelain) and the colour (cobalt blue).",
                "Describe one pattern you can see (a dragon, a flower, waves).",
                "Add one fact: it was fired in a kiln OR traded across Asia.",
            ],
        },
    },

    {
        "slug": "textiles",
        "num": 4,
        "title_en": "Threads of Splendour",
        "title_zh": "至極富麗——亞洲織品",
        "tagline_en": "Cloth that took a year to weave — and a moment to take your breath away.",
        "tagline_zh": "織一年的布，奪一瞬的目光。",
        "gallery": "Gallery · 至極富麗—亞洲織品文化",
        "tone": "tone-seal",
        "reading": [
            {"en": 'The textile gallery shines. Here are robes and hangings made of <span class="term">silk</span>, <span class="term">embroidered</span> with gold and silver thread until they look like solid light. In many Asian courts, what you wore showed exactly who you were.',
             "zh": "織品展廳熠熠生輝。這裡有絲綢製成的袍服與壁掛，以金銀線「刺繡」到看似凝固的光。在許多亞洲宮廷裡，你穿什麼，就精確地說明了你是誰。"},
            {"en": 'Making such cloth was slow, patient work. A weaver might spend months at the <span class="term">loom</span>; an embroiderer added each stitch by hand. The finest pieces used real gold, so the <span class="term">fabric</span> was as valuable as jewellery — and just as carefully kept.',
             "zh": "製作這樣的布料，是緩慢而耐心的功夫。織工可能在「織布機」前耗費數月；繡工則一針一線親手添上。最精緻的作品用上真金，因此布料貴比珠寶——也同樣被珍藏。"},
            {"en": 'Look closely and you will read messages in the <span class="term">motifs</span>: dragons for the emperor, phoenixes for the empress, flowers for the seasons, cranes for long life. A robe was not only beautiful; it was a sentence you could wear.',
             "zh": "湊近細看，你會在「紋飾」中讀到訊息：龍象徵皇帝、鳳象徵皇后、花卉對應四季、仙鶴寓意長壽。一件袍服不只是美——它是一句你可以穿在身上的話。"},
        ],
        "pull_quote": {"en": "A royal robe is a sentence written in silk and gold. Learn to read it.",
                       "zh": "一件華袍，是用絲與金寫成的句子。學會去讀它。"},
        "vocab": [
            {"word": "textile", "pos": "(n.)", "def": "cloth or woven fabric", "zh": "織品；紡織品",
             "eg": "This gallery displays Asian textiles."},
            {"word": "silk", "pos": "(n.)", "def": "a soft, shiny cloth made from the thread of silkworms", "zh": "絲；絲綢",
             "eg": "The robe is woven from fine silk."},
            {"word": "embroider", "pos": "(v.)", "def": "to decorate cloth by sewing patterns with thread", "zh": "刺繡",
             "eg": "Workers embroidered dragons in gold thread."},
            {"word": "loom", "pos": "(n.)", "def": "a machine or frame used for weaving cloth", "zh": "織布機",
             "eg": "A weaver sat at the loom for months."},
            {"word": "fabric", "pos": "(n.)", "def": "cloth made by weaving or knitting", "zh": "布料；織物",
             "eg": "The fabric was as valuable as jewellery."},
            {"word": "motif", "pos": "(n.)", "def": "a repeated image or design with meaning", "zh": "（具意義的）紋飾、母題",
             "eg": "The dragon motif marked the emperor."},
            {"word": "splendour", "pos": "(n.)", "def": "magnificent, rich beauty", "zh": "富麗；華美",
             "eg": "Visitors are amazed by the splendour of the robes."},
        ],
        "phrases": [
            {"en": "These robes are made of silk, embroidered with gold thread.", "zh": "這些袍服以絲綢製成，並用金線刺繡。"},
            {"en": "A piece like this could take many months to weave.", "zh": "像這樣的作品可能要織上好幾個月。"},
            {"en": "The dragon motif tells us this robe belonged to an emperor.", "zh": "龍紋告訴我們這件袍服屬於皇帝。"},
            {"en": "Look at how the gold thread catches the light.", "zh": "看那金線如何映著光。"},
            {"en": "In the old courts, your clothing showed your rank.", "zh": "在古代宮廷，你的衣著顯示你的身分位階。"},
        ],
        "quiz": [
            {"stem": "What are the finest robes in this gallery mainly made of?",
             "zh": "本展廳最精緻的袍服主要以什麼製成？",
             "options": [{"t": "Silk, embroidered with gold and silver thread", "correct": True},
                         {"t": "Paper and bamboo", "correct": False},
                         {"t": "Plastic and glass", "correct": False},
                         {"t": "Cotton printed by machine", "correct": False}],
             "explain_en": "They are silk, hand-embroidered with precious metal thread.",
             "explain_zh": "它們以絲綢製成，並用貴金屬線手工刺繡。"},
            {"stem": "Why was the finest fabric as valuable as jewellery?",
             "zh": "為什麼最精緻的布料貴比珠寶？",
             "options": [{"t": "It used real gold and took months of skilled work", "correct": True},
                         {"t": "It was made very quickly by machines", "correct": False},
                         {"t": "It was made from cheap materials", "correct": False},
                         {"t": "It could not be worn", "correct": False}],
             "explain_en": "Real gold thread plus months of patient handwork made it precious.",
             "explain_zh": "真金線加上數月耐心的手工，使其珍貴。"},
            {"stem": "What does a dragon motif on a robe usually tell us?",
             "zh": "袍服上的龍紋通常告訴我們什麼？",
             "options": [{"t": "It belonged to the emperor", "correct": True},
                         {"t": "It was made for a child", "correct": False},
                         {"t": "It was used as a kitchen cloth", "correct": False},
                         {"t": "It came from Europe", "correct": False}],
             "explain_en": "Dragons marked the emperor; motifs carried meaning about rank.",
             "explain_zh": "龍紋代表皇帝；紋飾承載著身分位階的意義。"},
            {"stem": "Which word means 'to decorate cloth by sewing patterns with thread'?",
             "zh": "哪個字意思是「以線縫出圖案來裝飾布料」？",
             "options": [{"t": "embroider", "correct": True},
                         {"t": "fire", "correct": False},
                         {"t": "curve", "correct": False},
                         {"t": "trade", "correct": False}],
             "explain_en": "To embroider is to sew decorative patterns onto fabric.",
             "explain_zh": "embroider（刺繡）即在布料上縫出裝飾性圖案。"},
        ],
        "your_turn": {
            "title": "Read a robe like a sentence",
            "intro_en": "Choose a motif and explain what it 'says' about the person who wore the robe.",
            "intro_zh": "選一個紋飾，解釋它「說」了穿袍者的什麼。",
            "steps": [
                "Name the material and one technique (silk, embroidery, gold thread).",
                "Point out one motif (dragon, phoenix, crane, flower).",
                "Say what the motif means about the wearer.",
            ],
        },
    },

    {
        "slug": "tea",
        "num": 5,
        "title_en": "The Art of Tea",
        "title_zh": "東亞茶文化——一碗茶裡的亞洲",
        "tagline_en": "Boil water, pour, and a whole culture unfolds.",
        "tagline_zh": "燒水、傾注，整個文化便在一碗茶中展開。",
        "gallery": "Gallery · 東亞茶文化展",
        "tone": "tone-jade",
        "reading": [
            {"en": 'The tea gallery is quiet and warm. Tea began as a drink, but in East Asia it grew into an <span class="term">art</span>. Around a single cup, people built whole <span class="term">rituals</span>: how to heat the water, how to pour, how to hold the bowl, how to sit with a guest.',
             "zh": "茶展廳安靜而溫暖。茶起初只是飲品，但在東亞，它長成了一門藝術。圍繞一只茶杯，人們建立起整套「儀式」：如何燒水、如何傾注、如何捧碗、如何與客人對坐。"},
            {"en": 'The objects here are the tools of that art: <span class="term">teapots</span>, cups, kettles, and trays, each shaped with great care. A good <span class="term">utensil</span> is not only useful; it is meant to be beautiful in the hand. The same leaf, served differently in China, Japan, or Korea, tells a different story.',
             "zh": "這裡的器物，正是這門藝術的工具：茶壺、茶杯、水注與托盤，每一件都精心塑造。一件好的「器具」不只是實用——它在手中也理應是美的。同一片茶葉，在中國、日本或韓國以不同方式奉上，便訴說著不同的故事。"},
            {"en": 'For a docent, tea is a gift, because every visitor knows it. You can invite them to imagine the warmth of the cup and the smell of the leaves. Tea turns a glass case into something they can almost taste — that is the docent’s real skill: making the past feel close.',
             "zh": "對導覽員而言，茶是一份禮物，因為每位訪客都認得它。你可以邀請他們想像茶杯的溫度、茶葉的香氣。茶讓一只玻璃展櫃變得幾乎可以品嚐——這正是導覽員真正的本領：讓過去變得親近。"},
        ],
        "pull_quote": {"en": "The same leaf, poured three ways, becomes three cultures. That is the art of tea.",
                       "zh": "同一片葉，三種傾注，便是三種文化。這就是茶的藝術。"},
        "vocab": [
            {"word": "ritual", "pos": "(n.)", "def": "a set of actions always done in the same careful way", "zh": "儀式；固定的程序",
             "eg": "Making tea became a quiet ritual."},
            {"word": "utensil", "pos": "(n.)", "def": "a tool or container used for a task", "zh": "器具；用具",
             "eg": "Each tea utensil is shaped with care."},
            {"word": "teapot", "pos": "(n.)", "def": "a container with a spout for making and pouring tea", "zh": "茶壺",
             "eg": "The small clay teapot fits in one hand."},
            {"word": "pour", "pos": "(v.)", "def": "to make a liquid flow from a container", "zh": "傾注；倒",
             "eg": "She pours the tea slowly and evenly."},
            {"word": "aroma", "pos": "(n.)", "def": "a pleasant smell", "zh": "香氣",
             "eg": "Visitors can almost imagine the aroma of the leaves."},
            {"word": "ceremony", "pos": "(n.)", "def": "a formal set of actions for a special occasion", "zh": "儀典；典禮",
             "eg": "The tea ceremony welcomes an honoured guest."},
            {"word": "craft", "pos": "(n.)", "def": "skill in making things by hand", "zh": "工藝；手藝",
             "eg": "Each pot shows the maker's craft."},
        ],
        "phrases": [
            {"en": "Tea began as a drink, but it grew into an art.", "zh": "茶起初是飲品，後來成為一門藝術。"},
            {"en": "These are the tools of the tea ceremony: pots, cups, and kettles.", "zh": "這些是茶儀式的器具：壺、杯與水注。"},
            {"en": "Imagine the warmth of the cup in your hands.", "zh": "想像茶杯在你手中的溫度。"},
            {"en": "The same tea is served differently in China, Japan, and Korea.", "zh": "同一種茶，在中國、日本、韓國有不同的奉茶方式。"},
            {"en": "A good utensil is useful and beautiful at the same time.", "zh": "一件好器具，既實用又美麗。"},
        ],
        "quiz": [
            {"stem": "In East Asia, tea grew from a simple drink into ___.",
             "zh": "在東亞，茶從單純的飲品成長為？",
             "options": [{"t": "an art with its own rituals", "correct": True},
                         {"t": "a kind of medicine only", "correct": False},
                         {"t": "a type of money", "correct": False},
                         {"t": "a building material", "correct": False}],
             "explain_en": "Tea became an art, with careful rituals around making and serving it.",
             "explain_zh": "茶成為一門藝術，環繞著泡茶與奉茶的細緻儀式。"},
            {"stem": "What are the objects in this gallery mostly?",
             "zh": "本展廳的器物大多是什麼？",
             "options": [{"t": "Tea utensils such as pots, cups, and kettles", "correct": True},
                         {"t": "Weapons and armour", "correct": False},
                         {"t": "Books and maps", "correct": False},
                         {"t": "Coins and stamps", "correct": False}],
             "explain_en": "The gallery shows the tools of tea: teapots, cups, kettles, trays.",
             "explain_zh": "展廳呈現茶的工具：茶壺、茶杯、水注、托盤。"},
            {"stem": "Why is tea an easy topic for a docent?",
             "zh": "為什麼茶對導覽員是個好題材？",
             "options": [{"t": "Every visitor already knows it, so it feels close", "correct": True},
                         {"t": "It is the most expensive object", "correct": False},
                         {"t": "No one has ever seen it before", "correct": False},
                         {"t": "It cannot be described in words", "correct": False}],
             "explain_en": "Because everyone knows tea, a docent can make the past feel familiar and close.",
             "explain_zh": "因為人人都認得茶，導覽員能讓過去顯得熟悉而親近。"},
            {"stem": "Which word means 'a pleasant smell'?",
             "zh": "哪個字意思是「宜人的氣味」？",
             "options": [{"t": "aroma", "correct": True},
                         {"t": "loom", "correct": False},
                         {"t": "glaze", "correct": False},
                         {"t": "branch", "correct": False}],
             "explain_en": "Aroma is a pleasant smell — here, the smell of tea leaves.",
             "explain_zh": "aroma（香氣）指宜人的氣味——此處是茶葉的香。"},
        ],
        "your_turn": {
            "title": "Invite a visitor into the tea gallery",
            "intro_en": "Write a short, warm invitation that helps a visitor use their senses.",
            "intro_zh": "寫一段溫暖的短邀請，引導訪客運用感官。",
            "steps": [
                "Tell them tea is both a drink and an art.",
                "Name one or two utensils they can see.",
                "Invite them to imagine a smell, a warmth, or a sound.",
            ],
        },
    },

    {
        "slug": "buddha",
        "num": 6,
        "title_en": "Images of the Buddha",
        "title_zh": "佛陀形影——亞洲佛教藝術",
        "tagline_en": "Across Asia, one teacher, a thousand faces.",
        "tagline_zh": "跨越亞洲，一位導師，千種面容。",
        "gallery": "Gallery · 化身與再現—亞洲佛教藝術",
        "tone": "",
        "reading": [
            {"en": 'This gallery is full of <span class="term">sculptures</span> of the Buddha and other holy figures, made across many centuries and many lands. We approach them here as <span class="term">art</span> and history. Buddhism began in India and travelled along trade routes to Central Asia, China, Korea, Japan, and Southeast Asia.',
             "zh": "本展廳滿是佛陀與其他聖者的「造像」，跨越許多世紀、許多地方而成。在這裡，我們以藝術與歷史的角度親近它們。佛教源於印度，沿著貿易路線傳往中亞、中國、韓國、日本與東南亞。"},
            {"en": 'As the teaching travelled, the images changed. The same calm face might be carved in <span class="term">bronze</span>, stone, or wood; gilded with gold or left plain. The <span class="term">posture</span> and the position of the hands — called <em>mudra</em> — carry meaning: a raised palm can mean “do not fear.”',
             "zh": "隨著教法傳播，造像也隨之改變。同一張安詳的面容，可能以「青銅」、石材或木頭雕成；或貼金、或樸素。其「姿態」與手的位置——稱為「手印（mudra）」——都帶有意義：舉起的手掌可以表示「莫怕」。"},
            {"en": 'For a docent, the key is <span class="term">respect</span>. You can describe the material, the age, the calm expression, and the journey of an idea across Asia — and let visitors feel its peace for themselves. You are guiding their eyes, not their beliefs.',
             "zh": "對導覽員來說，關鍵是「尊重」。你可以描述材質、年代、安詳的神情，以及一個理念橫越亞洲的旅程——讓訪客自行感受那份寧靜。你引導的是他們的目光，而非他們的信仰。"},
        ],
        "pull_quote": {"en": "Follow one calm face across a continent, and you have followed an idea travelling.",
                       "zh": "循著一張安詳的面容橫越大陸，你便循著一個理念的旅程。"},
        "vocab": [
            {"word": "sculpture", "pos": "(n.)", "def": "a work of art carved or shaped from solid material", "zh": "雕塑；造像",
             "eg": "The gallery is full of Buddhist sculptures."},
            {"word": "bronze", "pos": "(n.)", "def": "a hard metal made of copper and tin", "zh": "青銅",
             "eg": "This statue is cast in bronze."},
            {"word": "posture", "pos": "(n.)", "def": "the position in which a figure sits or stands", "zh": "姿態；體態",
             "eg": "The Buddha's posture is calm and still."},
            {"word": "expression", "pos": "(n.)", "def": "the look on a face that shows feeling", "zh": "神情；表情",
             "eg": "The face has a peaceful expression."},
            {"word": "sacred", "pos": "(adj.)", "def": "connected with religion and treated with great respect", "zh": "神聖的",
             "eg": "These are sacred images, so we speak gently."},
            {"word": "respect", "pos": "(n.)", "def": "polite, careful regard for someone or something", "zh": "尊重",
             "eg": "A docent describes sacred art with respect."},
            {"word": "journey", "pos": "(n.)", "def": "the act of travelling from one place to another", "zh": "旅程",
             "eg": "We can trace the journey of Buddhism across Asia."},
        ],
        "phrases": [
            {"en": "These sculptures show the Buddha, made across many lands.", "zh": "這些造像呈現佛陀，來自許多不同的地方。"},
            {"en": "This figure is cast in bronze and was once gilded with gold.", "zh": "這尊像以青銅鑄成，曾貼有金箔。"},
            {"en": "Notice the calm expression and the gentle posture.", "zh": "請注意那安詳的神情與柔和的姿態。"},
            {"en": "The position of the hands, called a mudra, carries meaning.", "zh": "手的位置稱為「手印」，帶有意義。"},
            {"en": "Buddhism travelled from India across much of Asia.", "zh": "佛教自印度出發，傳遍亞洲大部分地區。"},
        ],
        "quiz": [
            {"stem": "How do we approach these images in this course?",
             "zh": "在這門課裡，我們如何看待這些造像？",
             "options": [{"t": "As art and history, with respect", "correct": True},
                         {"t": "As toys to play with", "correct": False},
                         {"t": "As objects for sale", "correct": False},
                         {"t": "As things to ignore", "correct": False}],
             "explain_en": "We describe them as art and history, and treat sacred objects with respect.",
             "explain_zh": "我們以藝術與歷史的角度描述，並以尊重對待神聖的物件。"},
            {"stem": "Where did Buddhism begin before travelling across Asia?",
             "zh": "佛教在傳遍亞洲之前起源於何處？",
             "options": [{"t": "India", "correct": True},
                         {"t": "Japan", "correct": False},
                         {"t": "Persia", "correct": False},
                         {"t": "Taiwan", "correct": False}],
             "explain_en": "Buddhism began in India and spread along trade routes across Asia.",
             "explain_zh": "佛教源於印度，沿貿易路線傳播至亞洲各地。"},
            {"stem": "What does the position of the hands (a mudra) do?",
             "zh": "手的位置（手印）有什麼作用？",
             "options": [{"t": "It carries a meaning, such as 'do not fear'", "correct": True},
                         {"t": "It shows the price of the statue", "correct": False},
                         {"t": "It tells the time", "correct": False},
                         {"t": "It has no meaning at all", "correct": False}],
             "explain_en": "A mudra is a meaningful hand gesture; a raised palm can mean 'do not fear.'",
             "explain_zh": "手印是有意義的手勢；舉起的手掌可表示「莫怕」。"},
            {"stem": "Which sentence is the most respectful way to guide here?",
             "zh": "在這裡，哪一句是最尊重的導覽方式？",
             "options": [{"t": "Notice the calm expression — take a quiet moment to look.", "correct": True},
                         {"t": "Hurry up, it's just an old statue.", "correct": False},
                         {"t": "You must believe what this teaches.", "correct": False},
                         {"t": "Touch the face to feel the metal.", "correct": False}],
             "explain_en": "Guide the eyes gently; describe, invite quiet looking, and never push beliefs or touch sacred art.",
             "explain_zh": "溫和地引導目光：描述、邀請靜觀，絕不強加信仰或觸碰神聖造像。"},
        ],
        "your_turn": {
            "title": "Guide one sculpture with respect",
            "intro_en": "Write three calm sentences to introduce one Buddhist sculpture.",
            "intro_zh": "寫三句平靜的話，介紹一尊佛教造像。",
            "steps": [
                "Name the material (bronze, stone, or wood).",
                "Describe the expression or posture in one phrase.",
                "Add the bigger picture: an idea that travelled across Asia.",
            ],
        },
    },

    {
        "slug": "wisdom-craft",
        "num": 7,
        "title_en": "Wisdom & Craft",
        "title_zh": "智慧與工藝——經典與近代亞洲",
        "tagline_en": "Where ideas were written down, and where East met a changing world.",
        "tagline_zh": "在思想被寫下之處，也在東方遇見變動世界之處。",
        "gallery": "Galleries · 生命的指南—亞洲經典 ＋ 西潮下的近代亞洲工藝",
        "tone": "tone-seal",
        "reading": [
            {"en": 'Two galleries close our walk through Asia. The first, “Guides to Life,” gathers the great <span class="term">classics</span> of Asian religions — Buddhist, Hindu, Islamic, and more — as <span class="term">manuscripts</span> and printed books. These are the texts by which whole civilisations chose to live.',
             "zh": "兩個展廳為我們的亞洲之旅作結。第一個「生命的指南」匯集亞洲各宗教的偉大「經典」——佛教、印度教、伊斯蘭等——以手稿與刻印書籍的形式呈現。這些正是整個文明賴以生活的典籍。"},
            {"en": 'The second gallery jumps forward in time. As Western ships and ideas reached Asia, craftsmen blended old <span class="term">techniques</span> with new tastes. You see familiar materials — lacquer, metal, glass — shaped in fresh ways. This is the moment of <span class="term">exchange</span>, when East and West began to remake each other.',
             "zh": "第二個展廳則躍向近代。當西方的船隻與思想抵達亞洲，工匠們將舊「技法」與新品味交融。你會看到熟悉的材質——漆、金屬、玻璃——以嶄新的方式成形。這正是「交流」的時刻，東方與西方開始彼此重塑。"},
            {"en": 'Together these rooms hold the museum’s big idea: Asia was never closed. <span class="term">Wisdom</span> and goods moved along roads and seas; cultures borrowed and gave back. As a docent, you can leave visitors with that single thought — connection — which is also our school’s promise to the world.',
             "zh": "這兩個展廳合起來，承載著博物館的核心理念：亞洲從不封閉。智慧與貨物沿著道路與海洋流動，文化彼此借取、又回贈。作為導覽員，你可以讓訪客帶走這一個念頭——「連結」——這也正是我們學校對世界的承諾。"},
        ],
        "pull_quote": {"en": "Asia was never a closed room. It was a crossroads — and so is this museum.",
                       "zh": "亞洲從不是一間封閉的房間，而是一處十字路口——這座博物館亦然。"},
        "vocab": [
            {"word": "classic", "pos": "(n.)", "def": "a work of the highest quality, valued for a long time", "zh": "經典（之作）",
             "eg": "The gallery holds the classics of Asian religions."},
            {"word": "manuscript", "pos": "(n.)", "def": "a book or document written by hand", "zh": "手稿；寫本",
             "eg": "Some texts survive only as fragile manuscripts."},
            {"word": "technique", "pos": "(n.)", "def": "a special way of doing or making something", "zh": "技法；技術",
             "eg": "Craftsmen blended old techniques with new ideas."},
            {"word": "exchange", "pos": "(n.)", "def": "the act of giving and receiving between people or cultures", "zh": "交流；交換",
             "eg": "This room is about cultural exchange."},
            {"word": "blend", "pos": "(v.)", "def": "to mix things together smoothly", "zh": "融合；調和",
             "eg": "Artists blended Eastern and Western styles."},
            {"word": "wisdom", "pos": "(n.)", "def": "deep knowledge and good judgement", "zh": "智慧",
             "eg": "Ancient wisdom travelled along trade routes."},
            {"word": "connection", "pos": "(n.)", "def": "a link or relationship between things", "zh": "連結；關聯",
             "eg": "The whole museum is about connection across Asia."},
        ],
        "phrases": [
            {"en": "These books are the great classics of Asian religions.", "zh": "這些書籍是亞洲各宗教的偉大經典。"},
            {"en": "Some survive only as fragile, hand-written manuscripts.", "zh": "有些僅以脆弱的手寫稿存世。"},
            {"en": "Here, craftsmen blended old techniques with new tastes.", "zh": "在這裡，工匠將舊技法與新品味融合。"},
            {"en": "This gallery is about exchange between East and West.", "zh": "這個展廳談的是東西方之間的交流。"},
            {"en": "The big idea of this museum is connection across Asia.", "zh": "這座博物館的核心理念，是橫跨亞洲的連結。"},
        ],
        "quiz": [
            {"stem": "What does the gallery 'Guides to Life' mainly display?",
             "zh": "「生命的指南」展廳主要展出什麼？",
             "options": [{"t": "Classic texts of Asian religions, as manuscripts and books", "correct": True},
                         {"t": "Modern smartphones", "correct": False},
                         {"t": "Sports equipment", "correct": False},
                         {"t": "Maps of Europe", "correct": False}],
             "explain_en": "It gathers the great religious classics of Asia in written form.",
             "explain_zh": "它以文字形式匯集亞洲偉大的宗教經典。"},
            {"stem": "What happened to craft when Western ships and ideas reached Asia?",
             "zh": "當西方船隻與思想抵達亞洲，工藝發生了什麼？",
             "options": [{"t": "Craftsmen blended old techniques with new tastes", "correct": True},
                         {"t": "All old crafts were forgotten at once", "correct": False},
                         {"t": "Nothing changed at all", "correct": False},
                         {"t": "Machines replaced every artist overnight", "correct": False}],
             "explain_en": "It was a time of exchange: old skills mixed with new tastes and ideas.",
             "explain_zh": "那是交流的時代：舊技藝與新品味、新思想相融。"},
            {"stem": "What single big idea can a docent leave visitors with?",
             "zh": "導覽員可以讓訪客帶走哪一個核心理念？",
             "options": [{"t": "Connection — Asia was never closed", "correct": True},
                         {"t": "Asia was always isolated and closed", "correct": False},
                         {"t": "Only one culture ever mattered", "correct": False},
                         {"t": "Art has no history", "correct": False}],
             "explain_en": "The museum's message is connection: cultures borrowed and gave back across Asia.",
             "explain_zh": "博物館的訊息是「連結」：亞洲各文化彼此借取、回贈。"},
            {"stem": "Which word means 'giving and receiving between cultures'?",
             "zh": "哪個字意思是「文化之間的給予與接受」？",
             "options": [{"t": "exchange", "correct": True},
                         {"t": "posture", "correct": False},
                         {"t": "glaze", "correct": False},
                         {"t": "loom", "correct": False}],
             "explain_en": "Exchange is the giving and receiving of ideas and goods between cultures.",
             "explain_zh": "exchange（交流）指文化間思想與貨物的給予與接受。"},
        ],
        "your_turn": {
            "title": "Sum up the whole museum in one idea",
            "intro_en": "Write a closing line a docent could use to end the tour.",
            "intro_zh": "寫一句導覽員可用來結尾的話。",
            "steps": [
                "Use the word 'connection' or 'exchange'.",
                "Mention that Asia was a crossroads, not a closed room.",
                "Link it to Yung Ching's motto: connect with the world.",
            ],
        },
    },

    {
        "slug": "docent",
        "num": 8,
        "title_en": "Become a Young Docent",
        "title_zh": "成為小小英語導覽員",
        "tagline_en": "Now it is your turn to open the door for someone else.",
        "tagline_zh": "現在，輪到你為別人打開那扇大門。",
        "gallery": "Capstone · 總結成果",
        "tone": "tone-seal",
        "reading": [
            {"en": 'You have walked through the whole museum: the building, blue-and-white, textiles, tea, Buddhist art, and the galleries of wisdom and craft. Now you will put it together. Your task is a <span class="term">capstone</span>: prepare and perform a two-minute English tour of <strong>one</strong> object or gallery you love.',
             "zh": "你已走過整座博物館：建築、青花、織品、茶、佛教藝術，以及智慧與工藝的展廳。現在，你要把它整合起來。你的任務是一項「總結成果」：為你最喜愛的「一件」文物或「一個」展廳，準備並演出一段兩分鐘的英語導覽。"},
            {"en": 'A good short tour has a clear shape. <span class="term">Welcome</span> your visitors and say what they are about to see. <span class="term">Describe</span> the object: its material, its look, one interesting detail. Then give it <span class="term">meaning</span> — why it matters, how it connects to the rest of Asia. Finally, invite a question and thank them.',
             "zh": "一段好的短導覽有清晰的結構。先「歡迎」訪客，說明他們將看到什麼；再「描述」文物：材質、外觀、一個有趣的細節；接著賦予它「意義」——為何重要、如何與整個亞洲相連；最後，邀請提問並道謝。"},
            {"en": 'Speak slowly, smile, and use the phrases you have collected. You do not need long words; you need clear ones. Remember the very first lesson: a docent is not someone who knows everything — a docent is someone who helps others <span class="term">see</span>.',
             "zh": "說得慢一點、保持微笑，運用你蒐集的句型。你不需要艱深的字，只需要清楚的字。記得第一課所說的：導覽員不是無所不知的人——導覽員是幫助別人「看見」的人。"},
        ],
        "pull_quote": {"en": "Speak slowly. Smile. Use clear words, not long ones. Help them see.",
                       "zh": "說慢一點，微笑，用清楚而非艱深的字。幫他們看見。"},
        "vocab": [
            {"word": "capstone", "pos": "(n.)", "def": "a final project that brings everything together", "zh": "總結性的成果（壓軸作品）",
             "eg": "Your capstone is a two-minute tour."},
            {"word": "structure", "pos": "(n.)", "def": "the way the parts of something are arranged", "zh": "結構",
             "eg": "A good tour has a clear structure."},
            {"word": "describe", "pos": "(v.)", "def": "to say what something looks or is like", "zh": "描述",
             "eg": "Describe the material and one detail."},
            {"word": "detail", "pos": "(n.)", "def": "a small particular feature of something", "zh": "細節",
             "eg": "Point out one interesting detail."},
            {"word": "audience", "pos": "(n.)", "def": "the people who watch or listen", "zh": "觀眾；聽眾",
             "eg": "Smile at your audience and speak slowly."},
            {"word": "confident", "pos": "(adj.)", "def": "sure of yourself; not nervous", "zh": "有自信的",
             "eg": "Practice makes you a confident guide."},
            {"word": "perform", "pos": "(v.)", "def": "to do something in front of an audience", "zh": "演出；表演",
             "eg": "You will perform your tour for the class."},
        ],
        "phrases": [
            {"en": "Welcome — today I'd like to show you my favourite object.", "zh": "歡迎——今天我想為您介紹我最喜愛的一件文物。"},
            {"en": "This is made of ___, and the first thing you notice is ___.", "zh": "這件由 ___ 製成，您第一眼會注意到的是 ___。"},
            {"en": "What makes it special is ___.", "zh": "它特別之處在於 ___。"},
            {"en": "It connects to the rest of Asia because ___.", "zh": "它與整個亞洲相連，因為 ___。"},
            {"en": "Do you have any questions? Thank you for joining my tour.", "zh": "您有任何問題嗎？謝謝您參加我的導覽。"},
        ],
        "quiz": [
            {"stem": "What is your capstone task in this course?",
             "zh": "這門課的總結任務是什麼？",
             "options": [{"t": "Prepare and perform a 2-minute English tour of one object or gallery", "correct": True},
                         {"t": "Write a 20-page report in Chinese", "correct": False},
                         {"t": "Memorise every object in the museum", "correct": False},
                         {"t": "Build a model of the museum", "correct": False}],
             "explain_en": "The capstone is a short, focused English tour of one thing you love.",
             "explain_zh": "總結成果是針對你喜愛的一件事物，做一段簡短聚焦的英語導覽。"},
            {"stem": "Which is the best shape for a short tour?",
             "zh": "短導覽最好的結構是？",
             "options": [{"t": "Welcome → describe → give meaning → invite a question → thank", "correct": True},
                         {"t": "Thank → leave → say nothing", "correct": False},
                         {"t": "List every date and number you can find", "correct": False},
                         {"t": "Talk only about yourself", "correct": False}],
             "explain_en": "Open, describe, give meaning, invite a question, and close with thanks.",
             "explain_zh": "開場、描述、賦予意義、邀請提問，最後以道謝收尾。"},
            {"stem": "What kind of words should a young docent use?",
             "zh": "小小導覽員該用什麼樣的字詞？",
             "options": [{"t": "Clear words, not long or difficult ones", "correct": True},
                         {"t": "As many rare, long words as possible", "correct": False},
                         {"t": "Only Chinese words", "correct": False},
                         {"t": "No words — just point", "correct": False}],
             "explain_en": "Clarity beats difficulty: clear, simple English communicates best.",
             "explain_zh": "清楚勝過艱深：清晰、簡單的英語溝通效果最好。"},
            {"stem": "From Lesson 1, a docent is someone who ___.",
             "zh": "回到第一課，導覽員是怎樣的人？",
             "options": [{"t": "helps others see", "correct": True},
                         {"t": "knows absolutely everything", "correct": False},
                         {"t": "talks the longest", "correct": False},
                         {"t": "never speaks to visitors", "correct": False}],
             "explain_en": "A docent helps others see — that has been our definition from the start.",
             "explain_zh": "導覽員幫助別人「看見」——這是我們從一開始就給的定義。"},
        ],
        "your_turn": {
            "title": "Your 2-minute tour — build it now",
            "intro_en": "Use this five-step frame to draft your capstone tour. Then practise it aloud three times.",
            "intro_zh": "用這五步框架草擬你的總結導覽，再大聲練習三次。",
            "steps": [
                "WELCOME: greet visitors and name your object.",
                "DESCRIBE: material, look, one detail.",
                "MEANING: why it matters / how it connects across Asia.",
                "QUESTION: invite one question from your visitors.",
                "THANK: close warmly and thank them.",
            ],
        },
    },
]

# Capstone rubric (rendered only on the last lesson)
RUBRIC = [
    ("Opening & welcome", "開場與歡迎", "Greets visitors and names the object clearly."),
    ("Description", "描述", "Gives material, look, and one specific detail."),
    ("Meaning & connection", "意義與連結", "Explains why it matters and links it across Asia."),
    ("Language & delivery", "語言與表達", "Clear English, slow pace, eye contact, a smile."),
    ("Closing & question", "收尾與提問", "Invites a question and thanks the audience."),
]


# ----------------------------------------------------------------------------
# TEMPLATE HELPERS
# ----------------------------------------------------------------------------

def head(title, desc, css_path, extra_class=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Lato:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_path}">
</head>
<body class="{extra_class}">"""


def topbar(css_root, active=""):
    """css_root is '' for the hub, '../' for a lesson page."""
    def cls(name):
        return ' class="is-active"' if active == name else ""
    return f"""
<header class="topbar">
  <div class="wrap topbar-inner">
    <a class="topbar-brand" href="{css_root}index.html">
      <span class="topbar-seal">YC</span>
      <span class="topbar-name">Young Docents<small>南院小小英語導覽員 · 永慶高中</small></span>
    </a>
    <nav class="topbar-nav">
      <a href="{css_root}index.html"{cls('home')}>Course Home</a>
      <a href="{css_root}index.html#lessons">8 Lessons</a>
      <a href="{css_root}docent/"{cls('docent')}>Capstone</a>
      <a href="{css_root}workshop/"{cls('workshop')}>For Teachers</a>
      <a href="{css_root}taibao-quiz/"{cls('quiz')}>Taibao Quiz</a>
    </nav>
  </div>
</header>"""


def footer():
    return """
<footer>
  <div class="wrap">
    <span>© <span class="zh">嘉義縣立永慶高級中學</span> · Yung Ching Senior High School</span>
    <span class="partner">A gift from <a href="https://www.mycultureconnect.org/">My Culture Connect 人師教育協會</a></span>
  </div>
  <div class="wrap"><span class="note">A place-based bilingual course built around the National Palace Museum · Southern Branch. Demonstration materials — gallery photos and details to be confirmed with the school and the museum.</span></div>
</footer>
<script src="ASSET_JS"></script>
</body>
</html>"""


def speak_btn(text):
    safe = text.replace('"', "&quot;")
    return f'<button class="speak" data-speak="{safe}" aria-label="Listen">🔊</button>'


def render_reading(lesson):
    parts = ['<div class="block reading"><div class="block-head"><span class="kicker">Read</span>'
             '<h2>The Story <span class="zh">展廳故事</span></h2></div>']
    for p in lesson["reading"]:
        parts.append(f'<p>{p["en"]}</p>')
        parts.append(f'<p class="zh-gloss">{p["zh"]}</p>')
    if lesson.get("pull_quote"):
        pq = lesson["pull_quote"]
        parts.append(f'<div class="pull-quote">“{pq["en"]}”<span class="zh">{pq["zh"]}</span></div>')
    parts.append("</div>")
    return "\n".join(parts)


def render_vocab(lesson):
    items = ['<div class="block"><div class="block-head"><span class="kicker">Words</span>'
             '<h2>Word of the Day <span class="zh">關鍵字</span></h2></div><div class="vocab-list">']
    for v in lesson["vocab"]:
        items.append(f"""<div class="vocab">
  <div class="v-top"><span class="word">{v['word']}</span> <span class="pos">{v['pos']}</span></div>
  <div class="def">{v['def']}</div>
  <div class="zh">{v['zh']}</div>
  <div class="eg">{speak_btn(v['eg'])}<span>“{v['eg']}”</span></div>
</div>""")
    items.append("</div></div>")
    return "\n".join(items)


def render_phrases(lesson):
    rows = ['<div class="block"><div class="block-head"><span class="kicker">Say it</span>'
            '<h2>Docent Phrase Bank <span class="zh">導覽實用句</span></h2></div>'
            '<div class="phrasebank"><p class="pb-intro">Tap 🔊 to hear each line, then say it aloud. '
            '點 🔊 聽一次，再自己大聲說一遍。</p>']
    for p in lesson["phrases"]:
        rows.append(f"""<div class="phrase">{speak_btn(p['en'])}<div class="p-text">
  <div class="p-en">{p['en']}</div><div class="p-zh">{p['zh']}</div></div></div>""")
    rows.append("</div></div>")
    return "\n".join(rows)


def render_quiz(lesson):
    out = ['<div class="block"><div class="block-head"><span class="kicker">Check</span>'
           '<h2>Quick Check <span class="zh">小測驗</span></h2></div>'
           '<div class="quiz"><p class="q-intro">Choose one answer for each question. '
           '每題選一個答案，作答後會看到解析。</p>']
    for i, q in enumerate(lesson["quiz"], 1):
        opts = []
        for o in q["options"]:
            corr = "true" if o["correct"] else "false"
            opts.append(f'<button class="q-opt" data-correct="{corr}">{o["t"]}</button>')
        opts_html = "\n".join(opts)
        out.append(f"""<div class="q-item">
  <div class="q-stem"><span class="qn">Q{i}.</span>{q['stem']}</div>
  <div class="q-zh">{q['zh']}</div>
  <div class="q-opts">
  {opts_html}
  </div>
  <div class="q-explain">{q['explain_en']}<span class="zh">{q['explain_zh']}</span></div>
</div>""")
    out.append("</div></div>")
    return "\n".join(out)


def render_your_turn(lesson):
    yt = lesson["your_turn"]
    steps = "\n".join(f"<li>{s}</li>" for s in yt["steps"])
    return f"""<div class="block"><div class="your-turn">
  <div class="yt-label">Your Turn · 換你試試</div>
  <h3>{yt['title']}</h3>
  <p>{yt['intro_en']}</p>
  <p class="zh">{yt['intro_zh']}</p>
  <ol>{steps}</ol>
</div></div>"""


def render_rubric():
    rows = []
    for crit, zh, desc in RUBRIC:
        rows.append(f'<tr><td class="crit">{crit}<span class="zh">{zh}</span></td><td>{desc}</td></tr>')
    rows_html = "\n".join(rows)
    return f"""<div class="block"><div class="block-head"><span class="kicker">Rubric</span>
  <h2>How your tour is judged <span class="zh">導覽評分表</span></h2></div>
  <table class="rubric">
    <thead><tr><th>Criterion 評分項目</th><th>What we look for 評量重點</th></tr></thead>
    <tbody>{rows_html}</tbody>
  </table></div>"""


def lesson_nav(idx):
    cur = LESSONS[idx]
    links = []
    if idx > 0:
        prev = LESSONS[idx - 1]
        links.append(f'<a class="nav-link prev" href="../{prev["slug"]}/"><span class="dir">← Previous · 上一課</span>'
                     f'<span class="t">{prev["num"]}. {prev["title_en"]}</span></a>')
    else:
        links.append('<a class="nav-link prev" href="../index.html"><span class="dir">← Course Home</span>'
                     '<span class="t">Start page · 課程首頁</span></a>')
    links.append('<a class="nav-link hub" href="../index.html#lessons"><span class="dir">All Lessons</span>'
                 '<span class="t">⊹ 八課總覽</span></a>')
    if idx < len(LESSONS) - 1:
        nxt = LESSONS[idx + 1]
        links.append(f'<a class="nav-link next" href="../{nxt["slug"]}/"><span class="dir">Next · 下一課 →</span>'
                     f'<span class="t">{nxt["num"]}. {nxt["title_en"]}</span></a>')
    else:
        links.append('<a class="nav-link next" href="../index.html"><span class="dir">Finish · 完成 →</span>'
                     '<span class="t">Back to Course Home</span></a>')
    return f'<nav class="lesson-nav"><div class="wrap">{"".join(links)}</div></nav>'


# ----------------------------------------------------------------------------
# PAGE RENDERERS
# ----------------------------------------------------------------------------

def render_lesson(idx):
    L = LESSONS[idx]
    title = f"Lesson {L['num']}: {L['title_en']} · {SITE}"
    desc = f"{L['title_en']} — {L['tagline_en']}"
    parts = [head(title, desc, "../assets/css/main.css")]
    parts.append(topbar("../", active="docent" if L["slug"] == "docent" else ""))
    parts.append(f"""
<section class="page-hero {L['tone']}">
  <div class="wrap">
    <span class="lesson-no">Lesson {L['num']} of 8</span>
    <h1>{L['title_en']}<span class="zh">{L['title_zh']}</span></h1>
    <p class="tagline">{L['tagline_en']}<span class="zh">{L['tagline_zh']}</span></p>
    <span class="gallery-pill">📍 {L['gallery']}</span>
  </div>
</section>
<div class="lesson-body"><div class="wrap"><div class="lesson-inner">""")
    parts.append(render_reading(L))
    parts.append(render_vocab(L))
    parts.append(render_phrases(L))
    if L["slug"] == "docent":
        parts.append(render_rubric())
    parts.append(render_quiz(L))
    parts.append(render_your_turn(L))
    parts.append("</div></div></div>")
    parts.append(lesson_nav(idx))
    parts.append(footer().replace("ASSET_JS", "../assets/js/app.js"))
    html = "\n".join(parts)
    out_dir = os.path.join(ROOT, L["slug"])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    return L["slug"]


def render_hub():
    title = f"{SITE} · {SCHOOL} 永慶高中"
    desc = ("A place-based bilingual course for Yung Ching Senior High School, built around the "
            "National Palace Museum · Southern Branch. Students train to give a 2-minute English gallery tour.")
    parts = [head(title, desc, "assets/css/main.css")]
    parts.append(topbar("", active="home"))

    # hero
    parts.append(f"""
<section class="title">
  <div class="wrap">
    <span class="title__eyebrow">Yung Ching Senior High School · 永慶高中 · 在地特色雙語課</span>
    <h1>Young Docents of the<br>Southern Branch</h1>
    <div class="h1-zh">南院小小英語導覽員</div>
    <hr class="title__divider">
    <p class="title__tagline">The museum at our doorstep, told in English.
      <span class="tagline-zh">用英文，介紹我們門口的那座博物館。</span></p>
    <div class="hero-cta">
      <a class="btn btn-primary" href="#lessons">Start the course ↓</a>
      <a class="btn btn-ghost" href="welcome/">Lesson 1: Welcome</a>
    </div>
  </div>
</section>""")

    # about
    parts.append("""
<section class="about">
  <div class="wrap about-grid">
    <div class="about-text">
      <h3>A world-class museum, five minutes away.</h3>
      <p class="p-en">A few minutes from Yung Ching's classrooms stands the <strong>Southern Branch of the National Palace Museum</strong> — an Asian Art and Culture Museum that draws visitors from around the world. This course turns that treasure on our doorstep into an English classroom.</p>
      <p class="p-en">Students don't just learn <em>about</em> the museum; they learn to <strong>guide others through it in English</strong> — describing an object, sharing why it matters, and answering a visitor's question. It is Yung Ching's motto in action: <em>connect with the world</em>.</p>
      <div class="zh-block">
        <p>離永慶教室幾分鐘，就是「國立故宮博物院南部院區」——一座吸引全球訪客的亞洲藝術文化博物館。這門課把門口的這份珍寶，變成一間英語教室。</p>
        <p>學生不只是「認識」博物館，更要學會「用英語帶領別人」走進它：描述一件文物、說明它為何重要、回答訪客的提問。這正是永慶校訓「接國際」的實踐。</p>
      </div>
    </div>
    <aside class="about-aside">
      <div class="label">What you'll be able to do · 學完你能</div>
      <ul>
        <li><span class="n">1</span><span>Welcome visitors and open a tour in English.<span class="zh">用英語歡迎訪客、開場導覽。</span></span></li>
        <li><span class="n">2</span><span>Describe an artwork — its material, look, and meaning.<span class="zh">描述一件作品的材質、外觀與意義。</span></span></li>
        <li><span class="n">3</span><span>Connect one object to the wider story of Asia.<span class="zh">把一件文物連結到更大的亞洲故事。</span></span></li>
        <li><span class="n">4</span><span>Give a confident 2-minute English gallery tour.<span class="zh">自信地完成兩分鐘英語展廳導覽。</span></span></li>
      </ul>
    </aside>
  </div>
</section>""")

    # how it works
    parts.append("""
<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How each lesson works</span>
      <h2>Five steps, every lesson</h2>
      <div class="h2-zh">每一課，五個固定步驟</div>
    </div>
    <div class="modules">
      <div class="module"><div class="step">Read</div><div class="glyph">📖</div><h4>The Story<span class="zh">展廳故事</span></h4></div>
      <div class="module"><div class="step">Words</div><div class="glyph">🔑</div><h4>Word of the Day<span class="zh">關鍵字 🔊</span></h4></div>
      <div class="module"><div class="step">Say it</div><div class="glyph">🗣️</div><h4>Phrase Bank<span class="zh">導覽句 🔊</span></h4></div>
      <div class="module"><div class="step">Check</div><div class="glyph">✅</div><h4>Quick Check<span class="zh">小測驗</span></h4></div>
      <div class="module"><div class="step">Do</div><div class="glyph">✍️</div><h4>Your Turn<span class="zh">換你試試</span></h4></div>
    </div>
  </div>
</section>""")

    # lessons grid
    cards = []
    for L in LESSONS:
        cap = " is-capstone" if L["slug"] == "docent" else ""
        cards.append(f"""<a class="lesson-card{cap}" href="{L['slug']}/">
      <span class="ln">{L['num']}</span>
      <div>
        <h3>{L['title_en']}<span class="zh">{L['title_zh']}</span></h3>
        <p>{L['tagline_en']}</p>
        <span class="gallery-tag">{L['gallery']}</span>
      </div>
    </a>""")
    cards_html = "\n    ".join(cards)
    parts.append(f"""
<section id="lessons">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The course · 八堂課</span>
      <h2>Eight galleries, one tour</h2>
      <div class="h2-zh">八個展廳，一段你親自完成的導覽</div>
      <p class="lede">Work through the galleries one by one. Each lesson stands on its own — start anywhere, but Lesson 8 brings it all together.</p>
    </div>
    <div class="lesson-grid">
    {cards_html}
    </div>
  </div>
</section>""")

    # for teachers
    parts.append("""
<section class="teacher-note">
  <div class="wrap tn-grid">
    <div>
      <h2>For teachers: made with AI<small>給老師：這門課是怎麼用 AI 做出來的</small></h2>
      <p>This whole course was drafted and refined with an AI assistant, then checked by a teacher. The reading, the vocabulary, the phrase bank, and the quiz all follow one repeatable template — so the same method can build a new course around <em>any</em> local landmark.</p>
      <p class="zh">這門課是先用 AI 草擬、再由老師審訂而成。文本、字彙、導覽句與測驗都依循同一套可複製的模板——同樣的方法，可以為「任何」在地景點打造一門新課。</p>
      <a class="tn-btn" href="workshop/">See the workshop page · 看工作坊頁 →</a>
    </div>
    <div class="flow">
      <div class="label">The making-of, in 5 moves · 產製五步</div>
      <ol>
        <li>Pick a local landmark and one gallery or object.</li>
        <li>Ask the AI for a bilingual reading at the right level.</li>
        <li>Generate Word-of-the-Day vocab + docent phrases.</li>
        <li>Generate an English-only quiz with explanations.</li>
        <li>A teacher reviews, corrects, and approves.</li>
      </ol>
    </div>
  </div>
</section>""")

    # visit / about the museum + footer
    parts.append("""
<section class="visit">
  <div class="wrap visit-grid">
    <div>
      <h2>The museum on our doorstep<small>門口的博物館</small></h2>
      <p>National Palace Museum · Southern Branch — an Asian Art and Culture Museum, opened 2015, beside the high-speed rail in Taibao City.</p>
      <p class="zh">國立故宮博物院南部院區——亞洲藝術文化博物館，2015 年開幕，位於太保市高鐵站旁。</p>
    </div>
    <div class="contact">
      <dl>
        <dt>The Museum</dt>
        <dd>888 Gugong Blvd, Taibao City, Chiayi County<br><span class="zh">嘉義縣太保市故宮大道 888 號</span></dd>
        <dt>The School</dt>
        <dd>Yung Ching Senior High School 永慶高中<br>信義二路 1 號, 太保市</dd>
        <dt>Course by</dt>
        <dd><a href="https://www.mycultureconnect.org/">My Culture Connect 人師教育協會</a></dd>
      </dl>
    </div>
  </div>
</section>""")

    parts.append(footer().replace("ASSET_JS", "assets/js/app.js"))
    html = "\n".join(parts)
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


# ----------------------------------------------------------------------------
# WORKSHOP PAGE (For Teachers) — the speaker's projectable one-pager
# ----------------------------------------------------------------------------

WS_FLOW = [
    ("Pick a landmark + one object",
     "選一個在地景點與一件文物",
     "Choose something near your school. For us it was the Southern Branch and, say, a blue-and-white bowl. One gallery, one object — keep the scope small.",
     "選學校附近的題材。我們選了故宮南院，再聚焦一件文物（例如一只青花碗）。一展廳、一文物，範圍要小。"),
    ("Ask AI for a bilingual reading at the right level",
     "請 AI 寫出對程度的雙語短文",
     "Tell it the students' age, the language level, and the word count. Ask for English first with a Chinese gloss underneath each paragraph.",
     "告訴它學生年齡、語言程度、字數，並要求英文在前、每段下方附中文輔助。"),
    ("Generate Word-of-the-Day vocab + docent phrases",
     "產出關鍵字與導覽實用句",
     "Ask for 6–8 key words with part of speech, a simple definition, a Chinese gloss, and an example sentence — plus 5 useful guiding sentences.",
     "請它給 6–8 個關鍵字（含詞性、簡單定義、中文、例句），再加 5 句導覽實用句。"),
    ("Generate an English-only quiz with explanations",
     "產出純英文選項的測驗＋解析",
     "Ask for 4 multiple-choice questions, English options only, with a short bilingual explanation for each answer.",
     "請它出 4 題選擇題、選項全英文，每題附簡短雙語解析。"),
    ("You review, correct, and approve",
     "老師審訂、修正、定稿",
     "The AI drafts; the teacher decides. Check facts, level, tone, and rights before it reaches a student. This human step is the most important one.",
     "AI 負責草擬，老師負責拍板。送到學生面前前，先查事實、程度、語氣與版權。這個人為步驟最關鍵。"),
]

WS_PROMPTS = [
    ("Bilingual reading", "雙語短文",
     'Write a short bilingual reading for <span class="ph">senior-high</span> students about '
     '<span class="ph">[a blue-and-white porcelain bowl at the NPM Southern Branch]</span>. '
     'English first, about <span class="ph">160</span> words, friendly and clear. After each English '
     'paragraph add a Traditional-Chinese gloss to support understanding. Bold 4–6 useful vocabulary words.'),
    ("Word of the Day", "關鍵字",
     'From that reading, list <span class="ph">7</span> key words. For each give: the word, part of speech '
     'as (n.)/(v.)/(adj.), a one-line English definition, a Traditional-Chinese gloss, and one example sentence '
     'a museum guide might say.'),
    ("Docent phrase bank", "導覽實用句",
     'Give me <span class="ph">5</span> short sentences a student docent could say while showing this object '
     'to an international visitor — welcoming, describing, and inviting a question. English with a '
     'Traditional-Chinese translation under each.'),
    ("English-only quiz", "純英文測驗",
     'Write <span class="ph">4</span> multiple-choice comprehension questions on the reading. Four options each, '
     '<span class="ph">English only</span>, one correct. Mark the answer and add a short bilingual explanation '
     '(English + Traditional Chinese) for each.'),
    ("The whole lesson, in one go", "一次生一整課",
     'Using all of the above, assemble one lesson with five parts: (1) bilingual reading, (2) Word of the Day, '
     '(3) docent phrase bank, (4) an English-only quiz with explanations, (5) a short "Your Turn" task. '
     'Keep it at <span class="ph">senior-high</span> level and culturally respectful.'),
]

WS_CHECK = [
    ("Accuracy 正確性", "Every fact about the museum, the artwork, and history is correct.",
     "博物館、文物、歷史的每個說法都正確無誤。"),
    ("Level 程度", "The English matches your students — clear words, not rare ones.",
     "英文難度符合學生——用清楚的字，不用艱深字。"),
    ("Sensitivity 文化敏感", "Sacred or cultural items (e.g. Buddhist art) are described with respect and neutrality.",
     "神聖或文化性物件（如佛教藝術）以尊重、中性的方式描述。"),
    ("Rights 版權與肖像", "Photos are licensed; student portraits have consent. When unsure, use text + gradients.",
     "圖片有授權、學生肖像有同意書；不確定時就用文字＋漸層底。"),
]


def render_workshop():
    title = f"For Teachers: Making Bilingual Materials with AI · {SITE}"
    desc = ("A teacher-workshop companion page: how this place-based bilingual course was made with AI, "
            "the 5-step production flow, copy-and-paste prompts, and a teacher review checklist.")
    parts = [head(title, desc, "../assets/css/main.css")]
    parts.append(topbar("../", active="workshop"))
    parts.append("""
<section class="page-hero tone-seal">
  <div class="wrap">
    <span class="lesson-no">For Teachers · 教師工作坊</span>
    <h1>Making Bilingual Materials with AI<span class="zh">用 AI 產出雙語／英語教材</span></h1>
    <p class="tagline">This whole course was drafted with AI and finished by a teacher. Here is exactly how — so you can do it too.
      <span class="zh">這門課由 AI 草擬、老師定稿。以下是完整作法，您也能複製。</span></p>
    <span class="gallery-pill">🎁 A gift to the teachers of Yung Ching SHS · 獻給永慶高中的英文老師</span>
  </div>
</section>""")

    # Origin
    parts.append("""
<section>
  <div class="wrap ws-lead">
    <div class="section-head" style="margin-bottom:34px;">
      <span class="eyebrow">Why this course exists</span>
      <h2>The museum became the lesson</h2>
      <div class="h2-zh">把門口的博物館，變成一堂課</div>
    </div>
    <p>Yung Ching's motto is <em>“connect with the world.”</em> A few minutes away stands a world-class Asian art museum — the National Palace Museum · Southern Branch. So instead of a generic textbook, we built a course where students learn to <strong>guide visitors through that museum in English</strong>.</p>
    <div class="zh-block">永慶的校訓是「接國際」。離學校幾分鐘，就是世界級的亞洲藝術博物館——故宮南院。於是我們不用通用課本，而是做了一門課：讓學生學會「用英語帶訪客走進那座博物館」。</div>
    <p>But the real gift is not the website — it is the <strong>method</strong>. Once you can produce one bilingual lesson with AI, you can produce twenty, about any landmark, in your own voice.</p>
    <div class="zh-block">但真正的禮物不是這個網站，而是「方法」。一旦你能用 AI 產出一課雙語教材，你就能用同樣方式、針對任何在地題材，產出二十課，且保有你自己的風格。</div>
  </div>
</section>""")

    # Flow
    steps = []
    for i, (en, zh, body_en, body_zh) in enumerate(WS_FLOW, 1):
        steps.append(f"""<div class="flow-step">
      <span class="sn">{i}</span>
      <div><h3>{en}<span class="zh">{zh}</span></h3>
      <p>{body_en}</p><p class="zh">{body_zh}</p></div>
    </div>""")
    steps_html = "\n    ".join(steps)
    parts.append(f"""
<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The making-of</span>
      <h2>Five moves, start to finish</h2>
      <div class="h2-zh">從零到一課，五個動作</div>
    </div>
    <div class="flow-steps">
    {steps_html}
    </div>
  </div>
</section>""")

    # Prompts
    cards = []
    for tag, zh, body in WS_PROMPTS:
        cards.append(f"""<div class="prompt-card">
      <div class="pc-head"><span class="pc-tag">Prompt</span><span class="pc-title">{tag}<span class="zh">{zh}</span></span></div>
      <pre>{body}</pre>
    </div>""")
    cards_html = "\n    ".join(cards)
    parts.append(f"""
<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Copy &amp; paste</span>
      <h2>Prompts you can steal</h2>
      <div class="h2-zh">可直接複製的 prompt 範例</div>
      <p class="lede">Replace the <span style="color:var(--seal-deep);font-weight:700;background:var(--seal-soft);padding:0 5px;border-radius:4px;">highlighted parts</span> with your own landmark, level, and length. Then let the teacher in you take over.</p>
    </div>
    {cards_html}
  </div>
</section>""")

    # Checklist
    checks = []
    for crit, en, zh in WS_CHECK:
        checks.append(f'<li><div><strong>{crit}</strong> — {en}<span class="zh">{zh}</span></div></li>')
    checks_html = "\n      ".join(checks)
    parts.append(f"""
<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The human step</span>
      <h2>Before it reaches a student</h2>
      <div class="h2-zh">送到學生面前之前，老師要做的事</div>
    </div>
    <ul class="checklist">
      {checks_html}
    </ul>
  </div>
</section>""")

    # Takeaway
    parts.append("""
<section>
  <div class="wrap ws-takeaway">
    <p class="big">“Pick the landmark outside your window. The lesson is already there — AI just helps you write it down.”
      <span class="zh">「選你窗外的那個地標。課程早就在那裡——AI 只是幫你把它寫下來。」</span></p>
    <div class="ws-cta">
      <a class="btn btn-primary" href="../welcome/" style="background:var(--seal);color:#fff;">See Lesson 1 in action →</a>
    </div>
  </div>
</section>""")

    parts.append(footer().replace("ASSET_JS", "../assets/js/app.js"))
    html = "\n".join(parts)
    out_dir = os.path.join(ROOT, "workshop")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def main():
    render_hub()
    built = [render_lesson(i) for i in range(len(LESSONS))]
    render_workshop()
    print("Built hub: index.html")
    print("Built lessons:", ", ".join(built))
    print("Built workshop: workshop/index.html")


if __name__ == "__main__":
    main()
