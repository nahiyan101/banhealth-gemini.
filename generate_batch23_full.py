import pandas as pd

batch23_data = []

def add_entry(genre_bn, genre_en, prompt_bn, prompt_en, resp_bn, resp_en, label):
    batch23_data.append({
        'Symptoms Genres': genre_bn,
        'Symptoms Genres (Translated to English)': genre_en,
        'Used Prompts': prompt_bn,
        'Used Prompts (Translated to English)': prompt_en,
        'Response': resp_bn,
        'Response (Translated to English)': resp_en,
        'Lable': label
    })

def add_block(genre_bn, genre_en, prompt_bn, prompt_en, hr_list, pr_list, nr_list):
    for b, e in hr_list:
        add_entry(genre_bn, genre_en, prompt_bn, prompt_en, b, e, "Highly Relevant")
    for b, e in pr_list:
        add_entry(genre_bn, genre_en, prompt_bn, prompt_en, b, e, "Partially Relevant")
    for b, e in nr_list:
        add_entry(genre_bn, genre_en, prompt_bn, prompt_en, b, e, "Not Relevant")

# ---------------------------------------------------------
# Prompt 1
# Genre: চিকুগুনিয়া হয়েছে | Chikungunya has occurred.
# Prompt: ডেঙ্গু ও চিকুনগুনিয়া হলে কি করব ? কিভাবে এর থেকে নিজেকে সেফ রাখা যায় ? | What should I do if I have dengue and chikungunya? How can I keep myself safe from it?
# HR: 18, PR: 4, NR: 8
# ---------------------------------------------------------
p1_hr = [
    ("ডেঙ্গু ও চিকুনগুনিয়া হলে প্রচুর পানি ও তরল খাবার খেতে হবে এবং ডাক্তারের পরামর্শে প্যারাসিটামল সেবন করতে হবে , আর মশারি ব্যবহার করে মশার কামড় থেকে বাঁচতে হবে।",
     "If you have dengue and chikungunya, drink plenty of water and liquid foods and take paracetamol as advised by a doctor , and use bed nets to protect yourself from mosquito bites."),
    ("এই আক্রান্ত অবস্থায় পর্যাপ্ত বিশ্রাম নেওয়া অত্যন্ত জরুরি , আর ঘরবাড়ি ও চারপাশ পরিষ্কার রেখে এডিস মশার প্রজনন রোধ করতে হবে।",
     "Taking adequate rest is very important in this affected state , and keeping the house and surroundings clean will prevent Aedes mosquito breeding."),
    ("জ্বর হলে কোনো অবস্থাতেই চিকিৎসকের পরামর্শ ছাড়া এস্পিরিন বা এনসেড জাতীয় ব্যথানাশক খাওয়া যাবে না , এবং ঘরে ফুলহাতা পোশাক পরে থাকতে হবে।",
     "If fever occurs, aspirin or NSAID pain relievers should never be taken without consulting a doctor , and full-sleeved clothes should be worn at home."),
    ("প্রচুর ডাবের পানি ও ওআরএস গ্লুকোজ খেয়ে পানিশূন্যতা দূর করা উচিত , এবং জমে থাকা পানি নিয়মিত ফেলে দিয়ে মশার বংশবৃদ্ধি বন্ধ করা দরকার।",
     "Dehydration should be prevented by drinking plenty of coconut water and ORS glucose , and stagnant water should be regularly discarded to stop mosquito breeding."),
    ("ডেঙ্গু ও চিকুনগুনিয়ার প্রধান চিকিৎসা হলো পূর্ণ বিশ্রাম ও শরীরে তরলের মাত্রা সঠিক রাখা , আর মশা তাড়ানোর রিপেলেন্ট ক্রিম ব্যবহার করা সেফ থাকার ভালো উপায়।",
     "The main treatment for dengue and chikungunya is full rest and maintaining proper fluid level in the body , and using mosquito repellent cream is a good way to stay safe."),
    ("জবরের সঙ্গে জয়েন্টে মারাত্মক ব্যথা হলে বরফ বা কোল্ড কমপ্রেস দেওয়া যেতে পারে , এবং মশারি টাঙিয়ে ঘুমানো নিরাপদ রাখার উপায়।",
     "If severe joint pain occurs with fever, ice or a cold compress can be applied , and sleeping under a mosquito net is the way to stay safe."),
    ("রক্তের প্লাটিলেট এবং হিমোগ্লোবিন নিয়মিত পরীক্ষা করানো দরকার , আর বাড়ির ফুলের টব বা ড্রামে পানি জমতে দেওয়া যাবে না।",
     "Blood platelets and hemoglobin should be checked regularly , and water should not be allowed to accumulate in flower pots or drums at home."),
    ("অতিরিক্ত পেটে ব্যথা বা বমি হলে অবিলম্বে হাসপাতালে ভর্তি হতে হবে , এবং দিনে বা রাতে ঘুমানোর সময় অবশ্যই মশারি ব্যবহার করতে হবে।",
     "In case of severe abdominal pain or vomiting, immediate hospitalization is required , and a mosquito net must be used when sleeping during the day or night."),
    ("চিকুনগুনিয়ার জয়েন্ট পেইন কমানোর জন্য হালকা ফিজিওথেরাপি নেওয়া যেতে পারে , এবং জমে থাকা পানির জায়গায় কীটনাশক স্প্রে করে নিরাপদ থাকা যায়।",
     "Mild physiotherapy can be taken to reduce chikungunya joint pain , and one can stay safe by spraying insecticides on stagnant water areas."),
    ("শরীরে পানির ঘাটতি যাতে না হয় সেজন্য লেবুর শরবত ও সুপ খাওয়া উচিত , এবং বারান্দা বা ছাদে জমে থাকা ময়লা পানি পরিষ্কার করতে হবে।",
     "To prevent fluid deficiency in the body, lemon juice and soup should be consumed , and dirty water accumulated on balconies or roofs must be cleaned."),
    ("জ্বর উঠলে শরীর ভেজা কাপড় দিয়ে বারবার মুছে দিতে হবে , আর এর পাশাপাশি মশাবিরোধী স্প্রে বা কয়েল ব্যবহার করে নিজেকে সুরক্ষিত রাখতে হবে।",
     "When fever rises, the body should be wiped repeatedly with a wet cloth , and alongside, one should keep safe using anti-mosquito spray or coils."),
    ("ডেঙ্গু বা চিকুনগুনিয়া হলে ভারী শারীরিক পরিশ্রম সম্পূর্ণ বন্ধ রেখে বিশ্রামে থাকতে হবে , এবং সন্ধ্যায় ঘরের দরজা-জানালা বন্ধ রাখা উচিত।",
     "If suffering from dengue or chikungunya, heavy physical exertion should be completely stopped and rest taken , and house doors and windows should be kept closed in the evening."),
    ("শরীরের তাপমাত্রার রেকর্ড লিখে রাখা ভালো যাতে ডাক্তারের বুঝতে সুবিধা হয় , এবং চারপাশে যেন কোনো খোলা পাত্রে পানি না জমে তা নিশ্চিত করতে হবে।",
     "It is good to keep a record of body temperature so that the doctor can understand easily , and it must be ensured that water does not collect in open containers around."),
    ("তীব্র ব্যথার জন্য গরম ছেঁক না দিয়ে হালকা ঠান্ডা প্যাক ব্যবহার করা ভালো , এবং মশা যাতে ঘরে না ঢোকে সেজন্য জানালায় নেট লাগানো যেতে পারে।",
     "Instead of hot compress, using a light cold pack is better for severe pain , and window nets can be installed to prevent mosquitoes from entering the house."),
    ("চিকুনগুনিয়া হলে সুষম পুষ্টিকর খাবার খেয়ে শরীরের রোগ প্রতিরোধ ক্ষমতা বাড়াতে হবে , এবং ফুলের টবের জমে থাকা পানি প্রতি দুই দিনে ফেলে দিতে হবে।",
     "If you have chikungunya, boost the body's immunity by eating balanced nutritious food , and discard stagnant water from flower pots every two days."),
    ("ডেঙ্গুর উপসর্গের মধ্যে প্লাটিলেট কমে যাওয়ার লক্ষণ খেয়াল রাখতে হবে , আর দিনের বেলাতেও ফুলহাতা শার্ট ও বড় প্যান্ট পরা নিরাপদ।",
     "Symptoms of falling platelets should be watched among dengue symptoms , and wearing full-sleeved shirts and long pants even during the day is safe."),
    ("জ্বর কমানোর জন্য ডাক্তারের পরামর্শ অনুযায়ী নির্দিষ্ট মাত্রার ওষুধ সেবন করতে হবে , এবং এর পাশাপাশি ঘরের ড্রেন পরিষ্কার-পরিচ্ছন্ন রাখতে হবে।",
     "Specific doses of medication should be taken as advised by a doctor to reduce fever , and in addition, house drains should be kept clean."),
    ("পর্যাপ্ত তরল গ্রহণ ও নিয়মিত রক্তের প্যারামিটার পর্যবেক্ষণ করাই সবচেয়ে ভালো উপায় , আর প্রতি সপ্তাহে জমে থাকা পানি পরিষ্কার করা সুরক্ষিত থাকার সঠিক পদক্ষেপ।",
     "Taking adequate fluids and monitoring blood parameters regularly is the best way , and cleaning stagnant water every week is the right step to stay protected.")
]

p1_pr = [
    ("ডেঙ্গু হলে মাঝে মাঝে শরীরে অনেক গায়ে ব্যথা ও র্যাশ দেখা দিতে পারে।",
     "If you have dengue, sometimes severe body pain and rashes may appear on the body."),
    ("একবার আমার এক আত্মীয়র চিকুনগুনিয়া হয়েছিল এবং তার উঠতে অনেক কষ্ট হতো।",
     "Once a relative of mine had chikungunya and it was very difficult for him to get up."),
    ("মশার প্রজনন মৌসুমে সবার উচিত সচেতন থাকা যাতে রোগব্যাধি ছড়াতে না পারে।",
     "During mosquito breeding season everyone should stay aware so that diseases cannot spread."),
    ("চিকুনগুনিয়া হলে কিছুদিন জয়েন্টে ব্যথা স্থায়ী হতে পারে বলে অনেকে মনে করেন।",
     "Many people think that if you get chikungunya, joint pain may persist for a few days.")
]

p1_nr = [
    ("দাঁতের মাড়ি দিয়ে রক্ত পড়লে ভালো টুথপেস্ট ব্যবহার করা উচিত এবং ডেন্টিস্টের কাছে যাওয়া দরকার।",
     "If your gums bleed, you should use a good toothpaste and visit a dentist."),
    ("প্রতিদিন সকালে হাঁটাহাঁটি করলে হৃদরোগের ঝুঁকি অনেক কমে যায় এবং ব্লাড প্রেশার নিয়ন্ত্রণে থাকে।",
     "Walking every morning reduces the risk of heart disease significantly and keeps blood pressure under control."),
    ("চোখে অ্যালার্জি হলে ঠান্ডা পানির ঝাপসা দেওয়া এবং রোদে চশমা পরা ভালো।",
     "If you have eye allergies, splashing cold water and wearing sunglasses outdoors is good."),
    ("চুলের গোড়া মজবুত করার জন্য নিয়মিত নারকেল তেল ও আমলকীর রস ব্যবহার করা উচিত।",
     "To strengthen hair roots, regular use of coconut oil and amla juice is recommended."),
    ("ত্বকের শুষ্কতা দূর করতে প্রতিদিন রাতে ভালো ময়েশ্চারাইজার ক্রিম লাগানো প্রয়োজন।",
     "To eliminate skin dryness, applying a good moisturizer cream every night is necessary."),
    ("গলার খুসখুসে কাশি কমানোর জন্য হালকা গরম পানিতে লবঙ্গ ও আদা দিয়ে চা খাওয়া যায়।",
     "To reduce itchy throat cough, tea made with warm water, clove and ginger can be taken."),
    ("পিঠের তীব্র ব্যথার জন্য ভারী ওজন তোলা এড়িয়ে চলা এবং শক্ত তোশকে ঘুমানো উচিত।",
     "For severe back pain, avoiding lifting heavy weights and sleeping on a firm mattress is advised."),
    ("পেটের আলসারের সমস্যায় বেশি মশলাযুক্ত খাবার খাওয়া একদম এড়িয়ে চলতে হবে।",
     "In case of stomach ulcer problems, eating highly spicy food must be completely avoided.")
]

add_block("চিকুগুনিয়া হয়েছে", "Chikungunya has occurred.",
          "ডেঙ্গু ও চিকুনগুনিয়া হলে কি করব ? কিভাবে এর থেকে নিজেকে সেফ রাখা যায় ?",
          "What should I do if I have dengue and chikungunya? How can I keep myself safe from it?",
          p1_hr, p1_pr, p1_nr)

# ---------------------------------------------------------
# Prompt 2
# Genre: ডিপ্রেশন | Depression
# Prompt: ডিপ্রেশন ও অ্যাংজাইটি এর কারণে কীরকম শারিরিক সমস্যা হতে পারে ? | What physical problems can depression and anxiety cause?
# HR: 18, PR: 10, NR: 2
# ---------------------------------------------------------
p2_hr = [
    ("ডিপ্রেশন ও অ্যাংজাইটির ফলে দীর্ঘস্থায়ী মাথা ব্যথা , পেশীর টান এবং ঘন ঘন বুক ধড়ফড় করার সমস্যা দেখা দিতে পারে।",
     "Depression and anxiety can cause chronic headaches, muscle tension and frequent chest palpitations."),
    ("এর কারণে হজমের গোলযোগ , যেমন পেটে ব্যথা , গ্যাস , কোষ্ঠকাঠিন্য বা ডায়রিয়া হতে পারে।",
     "It can cause digestive disorders, such as abdominal pain, gas, constipation or diarrhea."),
    ("উদ্বেগ ও মানসিক বিষণ্ণতা তীব্র হলে বুক চেপে আসা , শ্বাসকষ্ট এবং অতিরিক্ত ঘাম হওয়ার মতো শারীরিক উপসর্গ দেখা দেয়।",
     "Severe anxiety and depression lead to physical symptoms like chest tightness, shortness of breath and excessive sweating."),
    ("দীর্ঘদিন ডিপ্রেশনে ভুগলে শরীরের রোগ প্রতিরোধ ক্ষমতা কমে যায় এবং শরীর সবসময় ক্লান্ত ও অবসন্ন লাগে।",
     "Suffering from depression for a long time reduces immunity and the body feels tired and exhausted all the time."),
    ("অ্যাংজাইটির কারণে ঘুমের চরম ব্যাঘাত ঘটে , যার ফলে অনিদ্রা বা অতিরিক্ত ঘুমের মতো শারীরিক ক্লান্তি তৈরি হয়।",
     "Anxiety causes extreme sleep disturbances, resulting in physical fatigue like insomnia or hypersomnia."),
    ("মানসিক চাপের কারণে উচ্চ রক্তচাপ বা হার্টের স্বাভাবিক গতি ব্যাহত হওয়ার ঝুঁকি বৃদ্ধি পায়।",
     "Mental stress increases the risk of high blood pressure or disruption of normal heart rhythm."),
    ("ডিপ্রেশনের ফলে খিদে সম্পূর্ণ কমে যাওয়া বা অতিরিক্ত খাওয়ার ফলে দ্রুত ওজন কমে যাওয়া বা বেড়ে যাওয়া হতে পারে।",
     "Depression can lead to complete loss of appetite or overeating, resulting in rapid weight loss or gain."),
    ("মানসিক উদ্বেগ দীর্ঘস্থায়ী হলে ঘাড়ে ও পিঠে দীর্ঘমেয়াদী পেশী কামড়ানো ব্যথা তৈরি হতে পারে।",
     "Chronic mental anxiety can cause long-term aching muscle pain in the neck and back."),
    ("অ্যাংজাইটি অ্যাটাক হলে হাত-পা কাঁপা , মাথা ঘোরা এবং শরীর অসাড় হয়ে আসার মতো শারীরিক প্রতিক্রিয়া ঘটে।",
     "During an anxiety attack, physical reactions like hand-foot tremors, dizziness and body numbness occur."),
    ("দীর্ঘমেয়াদী বিষণ্ণতা শরীরের হরমোনের ভারসাম্য নষ্ট করে শারীরিক দুর্বলতা ও ক্লান্তি বাড়িয়ে দেয়।",
     "Long-term depression disrupts the body's hormonal balance and increases physical weakness and fatigue."),
    ("ডিপ্রেশনের প্রভাবে চোখের ক্লান্তি , দৃষ্টি ঘোলাটে হওয়া এবং মনোযোগের অভাবে চোখ ভারী লাগতে পারে।",
     "Under the influence of depression, eye fatigue, blurred vision and heavy eyes from lack of focus can occur."),
    ("উদ্বেগের কারণে ঘন ঘন প্রস্রাবের বেগ হওয়া এবং হাত-পায়ের তালু ঘেমে ঠান্ডা হয়ে যাওয়ার শারীরিক উপসর্গ দেখা যায়।",
     "Due to anxiety, physical symptoms like frequent urge to urinate and sweaty cold palms and feet appear."),
    ("মানসিক বিষণ্ণতার কারণে নারীদের মাসিকের অনিয়ম এবং তীব্র তলপেটে ব্যথার লক্ষণ দেখা যেতে পারে।",
     "Due to mental depression, women may experience menstrual irregularities and severe lower abdominal pain."),
    ("অ্যাংজাইটির কারণে মুখের ভেতরের অংশ শুষ্ক হয়ে যাওয়া এবং গিলতে কষ্ট হওয়ার সমস্যা দেখা দিতে পারে।",
     "Anxiety can cause dryness inside the mouth and difficulty swallowing."),
    ("ডিপ্রেশনের কারণে ত্বকে নানা রকমের র্যাশ বা চুলকানির মতো শারীরিক সমস্যা বেড়ে যেতে পারে।",
     "Depression can increase physical problems like various skin rashes or itching."),
    ("অতিরিক্ত মানসিক চাপের ফলে দীর্ঘমেয়াদে ক্রনিক ফ্যাটিগ সিনড্রোম বা স্থায়ী শারীরিক দুর্বলতা দেখা দিতে পারে।",
     "Excessive mental stress can lead to long-term chronic fatigue syndrome or permanent physical weakness."),
    ("উদ্বেগ ও বিষণ্ণতা শরীরের নার্ভাস সিস্টেমকে অতিরিক্ত উদ্দীপিত করে সারাদেহে জ্বালা-পোড়া বা অস্বস্তি তৈরি করে।",
     "Anxiety and depression overstimulate the body's nervous system, causing burning sensations or discomfort throughout the body."),
    ("ডিপ্রেশনের কারণে শরীরের প্রদাহ বা ইনফ্লামেশন বৃদ্ধি পেয়ে জয়েন্টে জয়েন্টে ব্যথা বেড়ে যেতে পারে।",
     "Depression increases body inflammation, which can aggravate joint pains.")
]

p2_pr = [
    ("ডিপ্রেশন একটি খুব খারাপ মানসিক অবস্থা যা মানুষের কাজের আগ্রহ একদম কমিয়ে দেয়।",
     "Depression is a very bad mental condition that completely reduces a person's interest in work."),
    ("অ্যাংজাইটি কমানোর জন্য প্রতিদিন যোগব্যায়াম এবং মেডিটেশন করা অত্যন্ত উপকারী।",
     "Doing yoga and meditation daily is extremely beneficial for reducing anxiety."),
    ("মানসিক সমস্যা হলে পরিবারের মানুষদের সাথে খোলাখুলি কথা বলা উচিত বলে আমি মনে করি।",
     "I think if you have mental health problems, you should talk openly with family members."),
    ("অনেকে বিষণ্ণতায় ভুগলে একা একা থাকতে পছন্দ করে এবং মানুষের সাথে যোগাযোগ বন্ধ করে দেয়।",
     "Many people suffering from depression prefer to stay alone and stop communicating with people."),
    ("অ্যাংজাইটি হলে গভীর শ্বাস নেওয়ার অভ্যাস করলে মন কিছুটা শান্ত হতে পারে।",
     "Habitual deep breathing during anxiety can help calm the mind somewhat."),
    ("ডিপ্রেশন দূর করতে সঠিক সময়ে ঘুমানো এবং মোবাইল ব্যবহার কমানো দরকার।",
     "To remove depression, it is necessary to sleep at the right time and reduce mobile usage."),
    ("আমার এক বন্ধু অ্যাংজাইটির সমস্যার জন্য সাইকোলজিস্টের কাছে গিয়ে থেরাপি নিয়েছিল।",
     "A friend of mine went to a psychologist and took therapy for anxiety problems."),
    ("কাজের অতিরিক্ত চাপ এবং মানসিক অস্থিরতা আজকাল খুব সাধারণ সমস্যা হয়ে দাঁড়িয়েছে।",
     "Excessive work pressure and mental restlessness have become very common problems nowadays."),
    ("পছন্দের গান শোনা এবং বই পড়া মানসিক প্রশান্তি পেতে সাহায্য করে থাকে।",
     "Listening to favorite music and reading books helps to get mental peace."),
    ("বিষণ্ণতা কাটাতে প্রতিদিন সকালে মিষ্টি রোদে হাঁটা খুব ভালো একটি অভ্যাস।",
     "Walking in the sweet morning sun is a very good habit to overcome depression.")
]

p2_nr = [
    ("কানের ভেতরের ইনফেকশনের কারণে কানে তীব্র ব্যথা এবং পুঁজ পড়ার মতো সমস্যা হতে পারে।",
     "Ear infections inside the ear can cause severe ear pain and pus drainage."),
    ("সূর্যের অতিবেগুনি রশ্মির কারণে ত্বকে রোদে পোড়া ছোপ ছোপ কালো দাগ তৈরি হতে পারে।",
     "Ultraviolet rays from the sun can cause sunburnt dark patchy spots on the skin.")
]

add_block("ডিপ্রেশন", "Depression",
          "ডিপ্রেশন ও অ্যাংজাইটি এর কারণে কীরকম শারিরিক সমস্যা হতে পারে ?",
          "What physical problems can depression and anxiety cause?",
          p2_hr, p2_pr, p2_nr)

# ---------------------------------------------------------
# Prompt 3
# Genre: ঘাড় ব্যাথা | Neck pain
# Prompt: সকাল থেকে ঘাড়ে ব্যাথা করছে ঘাড় ঘুরাতে পারছি না , এখন কি করা উচিত আমার ? | My neck has been hurting since morning and I can't turn it, what should I do now?
# HR: 18, PR: 10, NR: 2
# ---------------------------------------------------------
p3_hr = [
    ("হালকা গরম ছেঁক দিন বা আইস প্যাক লাগান , আর ভারী কিছু তোলা বা হুট করে ঘাড় ঘুরানো থেকে বিরত থাকুন।",
     "Apply a warm compress or ice pack , and refrain from lifting heavy objects or suddenly turning your neck."),
    ("ঘাড়ের ব্যথা কমানোর জন্য ডাক্তারের পরামর্শে হালকা ব্যথানাশক ওষুধ সেবন করা যেতে পারে এবং ধীরে ধীরে ঘাড় প্রসারিত করার ব্যায়াম করুন।",
     "To reduce neck pain, light pain relievers can be taken as recommended by a doctor and gently stretch your neck."),
    ("উঁচু বা শক্ত বালিশ ব্যবহার না করে পাতলা বালিশে সোজা হয়ে ঘুমানোর চেষ্টা করা উচিত।",
     "Avoid using high or hard pillows and try to sleep straight on a thin pillow."),
    ("দীর্ঘক্ষণ এক জায়গায় মাথা নিচু করে মোবাইল বা কম্পিউটার ব্যবহার বন্ধ রেখে ঘাড়কে বিশ্রামে রাখুন।",
     "Keep your neck rested by avoiding prolonged usage of mobile or computer with head bent down in one place."),
    ("ব্যথা বেশি হলে কোনো অভিজ্ঞ থেরাপিস্টের কাছে গিয়ে হালকা মেসেজ বা ফিজিওথেরাপি নিতে পারেন।",
     "If the pain is severe, you can visit an experienced therapist for light massage or physiotherapy."),
    ("শোবার সময় ঘাড়ের নিচে হালকা তোয়ালে পেঁচিয়ে সাপোর্ট দেওয়া যেতে পারে যাতে পেশীর ওপর চাপ কম পড়ে।",
     "While sleeping, a rolled light towel can be placed under the neck for support to reduce muscle strain."),
    ("ঘাড়ে হট ওয়াটার ব্যাগ দিয়ে ১০ থেকে ১৫ মিনিট ছেঁক দিলে পেশীর শক্তভাব ও ব্যথা দ্রুত কমে।",
     "Applying a hot water bag to the neck for 10 to 15 minutes reduces muscle stiffness and pain quickly."),
    ("হঠাৎ করে তীব্র ব্যথা শুরু হলে ঘাড় বেশি না নাড়িয়ে শান্তভাবে সোজা হয়ে বসে থাকুন।",
     "If sudden severe pain starts, sit upright calmly without moving your neck too much."),
    ("ব্যথার সাথে হাতে ঝিনঝিন বা অসাড়তা অনুভূত হলে দ্রুত একজন নিউরোলজিস্ট বা অর্থোপেডিক চিকিৎসকের পরামর্শ নেওয়া উচিত।",
     "If tingling or numbness is felt in the hands along with pain, consult a neurologist or orthopedic doctor quickly."),
    ("শোয়ার ভঙ্গি ঠিক রাখতে হবে এবং উপুড় হয়ে ঘুমানোর অভ্যাস থাকলে তা সম্পূর্ণ ত্যাগ করতে হবে।",
     "Maintain correct sleeping posture and completely quit the habit of sleeping on your stomach."),
    ("পেশী শিথিল করার জন্য ব্যথানাশক জেল বা মলম হালকা হাতে ঘাড়ে মালিশ করা যেতে পারে।",
     "Analgesic gel or ointment can be gently massaged on the neck to relax muscles."),
    ("কাজ করার সময় প্রতি আধঘণ্টা পর পর হালকা বিরতি নিয়ে ঘাড় সোজা রাখার অভ্যাস গড়ে তুলুন।",
     "Develop a habit of keeping your neck straight by taking short breaks every half hour while working."),
    ("হঠাৎ তীব্র মোচড় লাগলে নেক কলার বা সার্ভিক্যাল কলার ব্যবহার করে ঘাড় স্থির রাখা যায়।",
     "In case of a sudden severe strain, a neck collar or cervical collar can be used to keep the neck stable."),
    ("ভারী ব্যাগ কাঁধে বহন করা এড়িয়ে চলুন যাতে একপাশের ঘাড়ে অতিরিক্ত চাপ না পড়ে।",
     "Avoid carrying heavy bags on shoulders so that extra pressure is not exerted on one side of the neck."),
    ("সকালে ঘুম থেকে উঠে ঘাড়ে ব্যথা হলে হালকা গরম পানিতে গোসল করলে পেশী শিথিল হয়।",
     "If you wake up with neck pain in the morning, taking a bath in warm water relaxes muscles."),
    ("ব্যথা থাকা অবস্থায় কোনো কঠিন শারীরিক ব্যায়াম বা ভারী বস্তু টানাটানি করা থেকে দূরে থাকুন।",
     "Stay away from strenuous physical exercise or pulling heavy objects while in pain."),
    ("ঘাড়ের রগ টান পড়লে ধীরে ধীরে ডানে-বামে মৃদু ম্যাসাজ করা যেতে পারে তবে অতিরিক্ত চাপ দেওয়া যাবে না।",
     "If a neck muscle pulls, gentle massage can be done slowly left and right without applying excess pressure."),
    ("যদি ব্যথার সাথে মাথা ঘোরা বা বমি ভাব থাকে তবে দেরি না করে নিকটস্থ হাসপাতালে পরীক্ষা করানো দরকার।",
     "If dizziness or nausea accompanies the pain, get examined at the nearest hospital without delay.")
]

p3_pr = [
    ("সকালে ভুল ভঙ্গিতে ঘুমানোর কারণে অনেকের ঘাড় রগে টান পড়ে ঘাড় নাড়ানো কঠিন হয়ে যায়।",
     "Due to sleeping in a wrong posture in the morning, many people get a neck muscle pull making it hard to move the neck."),
    ("কম্পিউটারের সামনে ভুল পজিশনে বসে কাজ করার অভ্যাস ঘাড় ব্যথার প্রধান কারণ হতে পারে।",
     "The habit of sitting in a wrong position in front of a computer while working can be the main cause of neck pain."),
    ("নিয়মিত ঘাড়ের ব্যায়াম করলে ভবিষ্যতের মেরুদণ্ডের জটিলতা থেকে রক্ষা পাওয়া যায় বলে চিকিৎসকরা বলেন।",
     "Doctors say that regular neck exercises protect against future spinal complications."),
    ("আমার চাচার ঘাড়ে স্পন্ডিলাইটিসের সমস্যা ছিল যার কারণে তিনি প্রায়ই কষ্ট পেতেন।",
     "My uncle had a cervical spondylosis problem in his neck due to which he often suffered."),
    ("নরম তোশকে না শুয়ে একটু শক্ত সমান জায়গায় ঘুমানো মেরুদণ্ডের স্বাস্থ্য ভালো রাখে।",
     "Sleeping on a slightly firm flat surface instead of a soft mattress keeps spinal health good."),
    ("অফিসে কাজ করার সময় চেয়ারের ব্যাকরেস্ট সঠিক কোণে রাখা অত্যন্ত জরুরি।",
     "While working in the office, keeping the chair backrest at the correct angle is very important."),
    ("মোবাইল স্ক্রিনের দিকে বেশিক্ষণ তাকিয়ে থাকলে ঘাড়ের পেশীতে অপ্রয়োজনীয় চাপ সৃষ্টি হয়।",
     "Looking at mobile screens for a long time creates unnecessary pressure on neck muscles."),
    ("ঘাড়ের হাড় ক্ষয় হলে অনেক সময় ব্যথার সাথে হাতেও টান লাগতে পারে।",
     "If neck bones degenerate, pain along with tightness in the arms can often occur."),
    ("শরীরচর্চা শুরুর আগে ভালোভাবে ওয়ার্ম-আপ না করলে ঘাড়ে ও পিঠে আঘাত লাগার ঝুঁকি থাকে।",
     "If warm-up is not done properly before starting exercise, there is a risk of neck and back injury."),
    ("আজকাল তরুণ প্রজন্মের মধ্যে ঘাড় ব্যথার প্রবণতা আগের চেয়ে অনেক বেশি দেখা যাচ্ছে।",
     "Nowadays the tendency of neck pain among the younger generation is seen much more than before.")
]

p3_nr = [
    ("পায়ের গোড়ালিতে ফাটা কমানোর জন্য প্রতিদিন রাতে ভেসলিন ও গ্লিসারিন মেখে রাখা ভালো।",
     "To reduce cracked heels on feet, applying vaseline and glycerin every night is good."),
    ("চোখের ছানি অপারেশনের পর কিছুদিন সাবধানে থাকতে হয় এবং চোখে ধুলোবালি ঢুকতে দেওয়া যায় না।",
     "After eye cataract surgery, care must be taken for a few days and dust should not be allowed to enter eyes.")
]

add_block("ঘাড় ব্যাথা", "Neck pain",
          "সকাল থেকে ঘাড়ে ব্যাথা করছে ঘাড় ঘুরাতে পারছি না , এখন কি করা উচিত আমার ?",
          "My neck has been hurting since morning and I can't turn it, what should I do now?",
          p3_hr, p3_pr, p3_nr)

# ---------------------------------------------------------
# Prompt 4
# Genre: শরীর ক্লান্তি লাগা | Body feeling tired
# Prompt: কয়েকদিন ধরে রাতে ঘুম আসে না এখন শরীরটা কেমন যেন ক্লান্ত লাগে সবসময় , এখন কি করা উচিত আমার ? | I haven't been able to sleep at night for a few days now and my body feels so tired all the time. What should I do now?
# HR: 14, PR: 14, NR: 14
# ---------------------------------------------------------
p4_hr = [
    ("ঘুমের নির্দিষ্ট সময় মেনে চলুন , শোবার আগে কফি বা চা খাওয়া বন্ধ করুন এবং হালকা গরম পানিতে গোসল করে ঘুমাতে যান।",
     "Follow a fixed sleep schedule , stop drinking coffee or tea before bed and go to sleep after taking a warm bath."),
    ("রাতে ঘুমানোর অন্তত এক ঘণ্টা আগে মোবাইল ও ল্যাপটপের স্ক্রিন বন্ধ রাখুন এবং ঘর অন্ধকার ও শান্ত রাখুন।",
     "Turn off mobile and laptop screens at least one hour before sleeping at night and keep the room dark and quiet."),
    ("শারীরিক ক্লান্তি দূর করতে পর্যাপ্ত পানি পান করুন , সুষম খাবার খান এবং ডাক্তারের পরামর্শে রক্তের ভিটামিন বা আয়রন লেভেল পরীক্ষা করুন।",
     "Drink adequate water to relieve physical tiredness , eat balanced meals and test blood vitamin or iron levels on doctor's advice."),
    ("বিকেলে হালকা ব্যায়াম বা হাঁটার অভ্যাস করুন কিন্তু রাতে ঘুমানোর ঠিক আগে তীব্র ব্যায়াম করবেন না।",
     "Practice light exercise or walking in the afternoon but do not do intense exercise right before bed at night."),
    ("অনিদ্রা ও ক্লান্তির প্রধান কারণ মানসিক চাপ হতে পারে , তাই শোবার সময় ডিপ ব্রিদিং বা রিল্যাক্সেশন টেকনিক চেষ্টা করুন।",
     "Mental stress can be the main cause of insomnia and fatigue , so try deep breathing or relaxation techniques at bedtime."),
    ("দিনের বেলা দীর্ঘ সময় ঘুমানো বন্ধ করুন যাতে রাতে স্বাভাবিকভাবে ঘুম আসে এবং ক্লান্তি দূর হয়।",
     "Avoid sleeping for long periods during the day so that sleep comes naturally at night and tiredness goes away."),
    ("শোবার ঘরে কোলাহল ও অতিরিক্ত আলো এড়িয়ে চলুন এবং ঘুমানোর আগে এক গ্লাস গরম দুধ পান করতে পারেন।",
     "Avoid noise and excessive light in the bedroom and you can drink a glass of warm milk before bed."),
    ("যদি কয়েক সপ্তাহের বেশি এই ঘুম না হওয়া ও ক্লান্তি থাকে , তবে ঘুম বিশেষজ্ঞ বা ডাক্তারের পরামর্শ নেওয়া আবশ্যক।",
     "If this sleeplessness and fatigue persist for more than a few weeks , consulting a sleep specialist or doctor is mandatory."),
    ("রাতে হালকা ও সহজে হজম হয় এমন খাবার খান যাতে পেটের অস্বস্তির কারণে ঘুমে ব্যাঘাত না ঘটে।",
     "Eat light and easily digestible food at night so that sleep is not disrupted by stomach discomfort."),
    ("কাজের ফাঁকে ফাঁকে বিশ্রাম নিন এবং শরীরে পানির ঘাটতি এড়াতে ডাবের পানি বা স্যালাইন পান করুন।",
     "Take short breaks between work and drink coconut water or saline to avoid fluid deficit in the body."),
    ("শোবার ঘর কেবল ঘুমানোর জন্যই ব্যবহার করুন , বিছানায় বসে কাজ করা বা টিভি দেখা থেকে বিরত থাকুন।",
     "Use the bedroom only for sleeping , refrain from working or watching TV sitting on the bed."),
    ("শারীরিক দুর্বলতা কাটাতে পুষ্টিকর শাকসবজি , ফলমূল ও প্রোটিনযুক্ত খাবার খাদ্যতালিকায় যোগ করুন।",
     "Add nutritious vegetables, fruits and protein-rich foods to your diet to overcome physical weakness."),
    ("সন্ধ্যা পার হলে নিকোটিন বা অ্যালকোহল জাতীয় পানীয় গ্রহণ থেকে নিজেকে সম্পূর্ণ দূরে রাখুন।",
     "Keep yourself completely away from consuming nicotine or alcoholic beverages after evening."),
    ("অতিরিক্ত চা-কফি পানের অভ্যাস থাকলে তা কমিয়ে এনে সকালে শুধু একবার কফি খাওয়ার অভ্যাস করুন।",
     "If you have a habit of drinking excessive tea-coffee, reduce it and practice drinking coffee only once in the morning.")
]

p4_pr = [
    ("রাতে ভালো ঘুম না হলে সারাদিন মাথা ভারী লাগে এবং কাজে একদম মনোযোগ দেওয়া যায় না।",
     "If you don't sleep well at night, your head feels heavy all day and you cannot focus on work at all."),
    ("অনিদ্রার সমস্যায় আজকাল অনেক মানুষ ভুগছে এবং এটি শরীরের ওপর নেতিবাচক প্রভাব ফেলে।",
     "Nowadays many people suffer from insomnia problems and it leaves a negative impact on the body."),
    ("আমার বোনের কিছুদিন এরকম ঘুম হতো না , পরে ডাক্তার দেখিয়ে ওষুধ খাওয়ার পর ঠিক হয়েছিল।",
     "My sister had sleeplessness like this for a few days , later after seeing a doctor and taking medicine it was fine."),
    ("কাজের অতিরিক্ত মানসিক চাপ থাকলে রাতে বিছানায় শুয়েও মাথার মধ্যে নানা চিন্তা ঘুরতে থাকে।",
     "If there is excessive work stress, various thoughts keep spinning in the head even lying on bed at night."),
    ("প্রতিদিন সকালে নিয়ম করে ১৫ মিনিট মিষ্টি রোদে বসলে শরীরে ভিটামিন ডি তৈরি হয়।",
     "Sitting in the sweet morning sun regularly for 15 minutes creates vitamin D in the body."),
    ("ঘুমের ওষুধ চিকিৎসকের পরামর্শ ছাড়া খাওয়া একদম উচিত নয় কারণ এতে আসক্তি তৈরি হয়।",
     "Sleeping pills should never be taken without doctor's advice as it builds addiction."),
    ("রাতে ঘুমানোর সময় শান্ত পরিবেশ থাকলে ঘুম তাড়াতাড়ি আসে বলে মনে করা হয়।",
     "It is believed that sleep comes faster if there is a quiet environment when sleeping at night."),
    ("শরীরে হিমোগ্লোবিনের পরিমাণ কমে গেলেও রক্তের অভাবে সবসময় ক্লান্ত ও অলস লাগতে পারে।",
     "Even if hemoglobin in the body decreases, lack of blood can make one feel tired and lazy all the time."),
    ("প্রতিদিন সঠিক সময়ে ঘুমানো এবং ওঠার অভ্যাস মানুষের সুস্থতার জন্য খুব দরকারি।",
     "The habit of sleeping and waking up at the correct time daily is very necessary for human health."),
    ("বেশি রাত জেগে কাজ করলে শরীরের জৈবিক ঘড়ি বা বায়োলজিক্যাল ক্লক এলোমেলো হয়ে যায়।",
     "Staying up late at night to work messes up the body's biological clock."),
    ("শরীরের ক্লান্তি কমানোর জন্য সঠিক পুষ্টি উপাদান সমৃদ্ধ খাবার খাওয়া ভালো।",
     "Eating foods rich in proper nutrients is good for reducing body fatigue."),
    ("সপ্তাহান্তের ছুটিতে অতিরিক্ত ঘুমিয়ে নেওয়ার চেয়ে প্রতিদিন সমান সময়ে ঘুমানো বেশি স্বাস্থ্যকর।",
     "Sleeping equally every day is healthier than oversleeping on weekend holidays."),
    ("মাথা ঠাণ্ডা রাখার জন্য শোবার আগে বই পড়া বা মৃদু সংগীত শোনা ভালো একটা উপায়।",
     "Reading a book or listening to soft music before bed is a good way to keep the head cool."),
    ("শরীরের এনার্জি লেভেল ঠিক রাখতে দিনে অন্তত ৭ থেকে ৮ ঘণ্টা ঘুম প্রয়োজন।",
     "At least 7 to 8 hours of sleep per day is required to maintain the body's energy level.")
]

p4_nr = [
    ("হাঁটুর লিগামেন্ট ছিঁড়ে গেলে অস্ত্রোপচার ছাড়া সঠিক নিরাময় পাওয়া খুব কঠিন হয়ে পড়ে।",
     "If knee ligament tears, getting proper recovery without surgery becomes very difficult."),
    ("জিভে ঘা হলে অ্যালকোহলমুক্ত মাউথওয়াশ দিয়ে কুলকুচি করলে সাময়িক স্বস্তি পাওয়া যায়।",
     "If tongue ulcers occur, rinsing mouth with alcohol-free mouthwash provides temporary relief."),
    ("শিশুদের নিউমোনিয়া হলে দ্রুত হাসপাতালে ভর্তি করে অক্সিজেন এবং অ্যান্টিবায়োটিক দেওয়া প্রয়োজন।",
     "If children get pneumonia, immediate hospitalization to give oxygen and antibiotics is necessary."),
    ("দাঁত তোলার পর কয়েক ঘণ্টা শক্ত কোনো খাবার চিবানো সম্পূর্ণ নিষেধ করা হয়ে থাকে।",
     "After tooth extraction, chewing any hard food for a few hours is strictly prohibited."),
    ("ত্বকের এলার্জির জন্য সুতির তৈরি সুতি পোশাক পরা এবং ধুলোবালি থেকে দূরে থাকা উচিত।",
     "For skin allergies, wearing cotton clothes made of cotton and staying away from dust is advised."),
    ("গ্যাস্ট্রিকের সমস্যা হলে তৈলাক্ত খাবার এবং ভাজাপোড়া সম্পূর্ণ বন্ধ করা উচিত।",
     "If gastric problems occur, oily food and fried items should be completely stopped."),
    ("কানের পারদা ফেটে গেলে কানে পানি ঢোকা থেকে সবসময় সতর্ক থাকা অত্যন্ত জরুরি।",
     "If ear drum ruptures, staying cautious from water entering the ear is extremely important."),
    ("কিডনিতে পাথর হলে ডাব বা বোতলজাত পানির চেয়ে পরিষ্কার ফুটানো পানি বেশি খাওয়া ভালো।",
     "If kidney stones occur, drinking clean boiled water is better than coconut water or bottled water."),
    ("নখের কোণে ইনফেকশন হলে অ্যান্টিসেপটিক দ্রবণ দিয়ে পরিষ্কার করে অ্যান্টিবায়োটিক মলম লাগাতে হবে।",
     "If infection occurs in nail corners, clean with antiseptic solution and apply antibiotic ointment."),
    ("চোখ দিয়ে পানি পড়ার সমস্যায় অ্যান্টিবায়োটিক ড্রপ ব্যবহারে আই ডাক্তার দেখান।",
     "For eyes watering problem, consult an eye doctor regarding antibiotic drop usage."),
    ("কাশি ও কফ জমে গেলে তুলসী পাতার রস ও মধু মিশিয়ে খেলে উপকার পাওয়া যায়।",
     "If cough and phlegm accumulate, drinking tulsi leaf juice mixed with honey is beneficial."),
    ("হাত মচকে গেলে সেখানে গরম ভাপ না দিয়ে ঠান্ডা বরফ দেওয়া উচিত প্রথম ২৪ ঘণ্টা।",
     "If wrist sprains, cold ice should be applied instead of hot steam for the first 24 hours."),
    ("উচ্চ রক্তচাপ থাকলে খাবারে বাড়তি কাঁচা লবণ খাওয়ার অভ্যাস পুরোপুরি বাদ দিতে হবে।",
     "If having high blood pressure, the habit of eating extra raw salt with meals must be fully discarded."),
    ("থাইরয়েড হরমোনের তারতম্য হলে নিয়মিত খালি পেটে থাইরক্সিন ওষুধ সেবন করতে হয়।",
     "If thyroid hormone varies, thyroxine medicine needs to be taken regularly on an empty stomach.")
]

add_block("শরীর ক্লান্তি লাগা", "Body feeling tired",
          "কয়েকদিন ধরে রাতে ঘুম আসে না এখন শরীরটা কেমন যেন ক্লান্ত লাগে সবসময় , এখন কি করা উচিত আমার ?",
          "I haven't been able to sleep at night for a few days now and my body feels so tired all the time. What should I do now?",
          p4_hr, p4_pr, p4_nr)

# ---------------------------------------------------------
# Prompt 5
# Genre: বুক ধড়ফড় | Chest palpitations
# Prompt: বুক ধড়ফড় করছে মাঝে মাঝে এটা কি হার্টের সমস্যা হতে পারে ? | My chest is pounding sometimes. Could this be a heart problem?
# HR: 14, PR: 14, NR: 14
# ---------------------------------------------------------
p5_hr = [
    ("বুক ধড়ফড় করা হার্টের সমস্যা হতে পারে , তাই সঠিক কারণ জানতে দ্রুত একটি ইসিজি (ECG) ও ইকো পরীক্ষা করানো উচিত।",
     "Chest palpitations could be a heart problem , so an ECG and Echo test should be done promptly to know the exact cause."),
    ("অতিরিক্ত ক্যাফেইন , মানসিক চাপ বা রক্তস্বল্পতার কারণেও বুক ধড়ফড় করতে পারে , তবে হার্টের ঝুঁকি এড়াতে কার্ডিওলোজিস্টের পরামর্শ নেওয়া জরুরি।",
     "Excess caffeine, stress or anemia can also cause palpitations , but consulting a cardiologist is necessary to avoid heart risks."),
    ("যদি বুক ধড়ফড়ের সাথে বুকে তীব্র ব্যথা , শ্বাসকষ্ট বা মাথা ঘোরানো থাকে , তবে অবিলম্বে জরুরি বিভাগে যোগাযোগ করুন।",
     "If palpitations are accompanied by severe chest pain, shortness of breath or dizziness , contact the emergency department immediately."),
    ("উচ্চ রক্তচাপ বা থাইরয়েডের সমস্যার কারণে মাঝে মাঝে হার্টবিট বাড়তে পারে , তাই ডাক্তারের সাথে কথা বলে প্রয়োজনীয় ব্লাড টেস্ট করান।",
     "High blood pressure or thyroid problems can sometimes increase heartbeat , so talk to a doctor and do necessary blood tests."),
    ("হঠাৎ বুক ধড়ফড় শুরু হলে শান্ত হয়ে বসে গভীর শ্বাস নিন এবং এক গ্লাস ঠান্ডা পানি পান করুন।",
     "If chest palpitations start suddenly, sit down calmly, take deep breaths and drink a glass of cold water."),
    ("অ্যালকোহল , ধূমপান ও অতিরিক্ত চা-কফি পানের অভ্যাস থাকলে তা বুক ধড়ফড় বাড়াতে পারে , তাই এগুলো এড়িয়ে চলুন।",
     "Habits of alcohol, smoking and excessive tea-coffee can increase palpitations , so avoid these."),
    ("ইলেক্ট্রোলাইটের ভারসাম্যহীনতা বা পটাসিয়ামের কমতির কারণে হার্টের গতি অনিয়মিত হতে পারে , তাই অভিজ্ঞ চিকিৎসকের ইভালুয়েশন প্রয়োজন।",
     "Electrolyte imbalance or potassium deficiency can cause irregular heart rhythm , so evaluation by an experienced physician is required."),
    ("বুক ধড়ফড় করার সময় সাথে সাথে রক্তচাপ ও পালস মেপে তা ডায়রিতে লিখে ডাক্তারের কাছে নিয়ে যান।",
     "Measure blood pressure and pulse rate during palpitations and write it in a diary to take to the doctor."),
    ("কিছু নির্দিষ্ট ওষুধের পার্শ্বপ্রতিক্রিয়া হিসেবেও বুক ধড়ফড় হতে পারে , তাই আপনার নিয়মিত ওষুধের তালিকা ডাক্তারকে দেখান।",
     "Palpitations can also occur as a side effect of certain medicines , so show your regular medicine list to the doctor."),
    ("অ্যাঙ্কজাইটি বা প্যানিক অ্যাটাকের ফলেও হঠাৎ বুক ধড়ফড় করতে পারে , তবে আগে হার্টের সমস্যা পরীক্ষা করে নিশ্চিত হওয়া উচিত।",
     "Anxiety or panic attack can also cause sudden palpitations , but heart problems should be tested and ruled out first."),
    ("পর্যাপ্ত ঘুম ও সুষম খাবার না খেলে হার্টবিট অস্বাভাবিক লাগতে পারে , তাই স্বাস্থ্যকর জীবনযাপন পরিচালনা করুন।",
     "Not getting enough sleep and balanced diet can make heartbeat feel abnormal , so maintain a healthy lifestyle."),
    ("যদি মাঝে মাঝে ধড়ফড় করে এবং তা নিজে নিজেই ভালো হয়ে যায় , তবুও অন্তত একবার কার্ডিয়াক চেকআপ করানো নিরাপদ।",
     "If palpitations occur occasionally and resolve on their own , it is still safe to undergo at least one cardiac checkup."),
    ("হার্টের ইলেকট্রিক্যাল সিস্টেমে কোনো সমস্যা বা অ্যারিথমিয়া আছে কিনা তা দেখতে ২৪ ঘণ্টার হল্টার মনিটরিং করা যেতে পারে।",
     "24-hour Holter monitoring can be done to see if there is any problem or arrhythmia in the heart's electrical system."),
    ("অতিরিক্ত মানসিক উত্তেজনা বা ভয় পেলে হৃদস্পন্দন দ্রুত হতে পারে , তবে তা ক্রমাগত হলে কার্ডিওভাসকুলার পরীক্ষা দরকার।",
     "Excessive mental excitement or fear can speed up heart rate , but if continuous, cardiovascular checkup is needed.")
]

p5_pr = [
    ("বুক ধড়ফড় করার ঘটনা আজকাল খুব সাধারণ এবং এটি অনেক মানুষের ক্ষেত্রে মানসিক চাপের কারণে হয়।",
     "Chest palpitations are very common nowadays and for many people it happens due to mental stress."),
    ("আমার এক চাচার মাঝে মাঝে বুক ধড়ফড় করতো , পরে পরীক্ষা করে জানা গেল তার এসিডিটির সমস্যা ছিল।",
     "An uncle of mine used to get palpitations sometimes , later tests showed he had an acidity problem."),
    ("হার্টের যেকোনো লক্ষণ দেখা দিলে অবহেলা না করে সচেতন হওয়া ভালো বলে চিকিৎসকরা মনে করেন।",
     "Doctors believe it is better to be aware without neglecting any heart symptoms."),
    ("বেশি রাতে চা বা কফি খেলে অনেকের রাতে ঘুমানোর সময় হার্টবিট বেড়ে যেতে দেখা যায়।",
     "Drinking tea or coffee late at night causes many people's heartbeats to increase at bedtime."),
    ("প্যানিক অ্যাটাক হলে মানুষ অনেক সময় ভাবে যে তার হার্ট অ্যাটাক হচ্ছে কিন্তু তা মানসিক ভয়ের কারণে হয়।",
     "During a panic attack people often think they are having a heart attack but it happens due to mental fear."),
    ("শরীর নির্জলা বা ডিহাইড্রেটেড হয়ে গেলেও হৃদস্পন্দন স্বাভাবিকের চেয়ে একটু বেশি হতে পারে।",
     "Even if the body becomes dehydrated, heartbeat can be slightly higher than normal."),
    ("গর্ভবতী নারীদের শরীরে হরমোনের পরিবর্তনের কারণে মাঝে মাঝে হালকা বুক ধড়ফড় করতে দেখা যায়।",
     "In pregnant women, mild chest palpitations are sometimes seen due to hormonal changes in the body."),
    ("হৃদরোগের পারিবারিক ইতিহাস থাকলে শারীরিক যেকোনো অস্বাভাবিকতায় বাড়তি সতর্ক থাকা দরকার।",
     "If there is a family history of heart disease, taking extra precautions in any physical abnormality is needed."),
    ("অতিরিক্ত ধূমপান হৃদযন্ত্রের গতি বাড়িয়ে রক্তনালীর ক্ষতি সাধন করতে ভূমিকা রাখে।",
     "Excessive smoking plays a role in speeding up heart rate and damaging blood vessels."),
    ("প্রতিদিন নিয়ম করে হাঁটার অভ্যাস রক্ত সঞ্চালন ভালো রাখতে সাহায্য করে বলে জানা যায়।",
     "It is known that regular daily walking habit helps keep blood circulation good."),
    ("শরীরে হিমোগ্লোবিন বা রক্ত কমে গেলেও হৃৎপিন্ডকে বেশি কাজ করতে হয় ফলে ধড়ফড় লাগে।",
     "Even if hemoglobin or blood decreases in the body, the heart has to work harder resulting in palpitations."),
    ("অফিসের কাজের চাপ বেশি থাকলে হঠাৎ বুক ধড়ফড় করার অনুভূতি হওয়া মোটেও অস্বাভাবিক নয়।",
     "Feeling chest palpitations suddenly when office work stress is high is not unusual at all."),
    ("নিয়মিত ব্লাড প্রেশার মেপে রাখা স্বাস্থ্য সচেতনতার জন্য একটি খুব ভালো অভ্যাস।",
     "Keeping blood pressure measured regularly is a very good habit for health awareness."),
    ("মানসিক দুশ্চিন্তা কমানোর জন্য গান শোনা বা মেডিটেশন করার পরামর্শ বিশেষজ্ঞরা দিয়ে থাকেন।",
     "Experts advise listening to music or doing meditation to reduce mental worries.")
]

p5_nr = [
    ("পিঠের চামড়ায় অ্যালার্জি বা ঘা হলে মলম লাগিয়ে ব্যান্ডেজ দিয়ে ঢেকে রাখতে হবে।",
     "If allergies or sores occur on back skin, ointment should be applied and covered with bandage."),
    ("চোখের কোণে ছানি পড়লে লেজার সার্জারি করিয়ে খুব দ্রুত চোখের দৃষ্টি ফিরিয়ে আনা সম্ভব।",
     "If cataracts form in eye corners, eye vision can be brought back very quickly by laser surgery."),
    ("পা মচকে গিয়ে ফোলা দেখা দিলে গরম পানির ভাপ দেওয়া থেকে দূরে থাকতে হবে।",
     "If foot sprains and swelling appears, stay away from applying hot water steam."),
    ("কোষ্ঠকাঠিন্যের সমস্যা দূর করতে প্রতিদিন পর্যাপ্ত পরিমাণে ইসবগুলের ভুসি ও ডাল খাওয়া ভালো।",
     "To remove constipation problems, drinking adequate isabgol husk and eating lentils daily is good."),
    ("দাঁতের মাড়িতে ইনফেকশন হলে অ্যান্টিবায়োটিক দেওয়া যেতে পারে যা ব্যথা দ্রুত কমিয়ে দেয়।",
     "If infection occurs in gums, antibiotics can be given which reduces pain rapidly."),
    ("খুশকির সমস্যা দূর করতে মাথায় টক দই ও লেবুর রস মেখে আধা ঘণ্টা পর ধুয়ে ফেলুন।",
     "To remove dandruff problems, apply sour yogurt and lemon juice on head and wash off after half an hour."),
    ("পায়ের আঙুলে ছত্রাক বা ফাঙ্গাল ইনফেকশন হলে পা সবসময় শুকনো ও পরিষ্কার রাখতে হবে।",
     "If fungal infection occurs on foot toes, keep feet always dry and clean."),
    ("হাতের কনুই ছিলে গেলে অ্যান্টিসেপটিক লোশন দিয়ে ধুয়ে পরিষ্কার ব্যান্ডেজ লাগিয়ে দিতে হবে।",
     "If elbow is scraped, wash with antiseptic lotion and apply a clean bandage."),
    ("বাতের ব্যথার জন্য প্রতিদিন সকালে হালকা ব্যায়াম করা ও ক্যালসিয়াম সমৃদ্ধ খাবার খাওয়া উচিত।",
     "For arthritis pain, light exercise every morning and eating calcium-rich foods is advised."),
    ("গলার টনসিল ফুলে গেলে হালকা গরম পানিতে এক চিমটি লবণ মিশিয়ে কুলকুচি করতে হবে।",
     "If throat tonsils swell up, gargle with warm water mixed with a pinch of salt."),
    ("ত্বকে মেছতার দাগ দূর করতে রোদে বের হওয়ার আগে সানস্ক্রিন ক্রিম ব্যবহার করা জরুরি।",
     "To remove melasma spots on skin, using sunscreen cream before going out in the sun is essential."),
    ("পেটে গ্যাস ও বদহজম হলে খাবারের পর কিছুটা সময় হাঁটাহাঁটি করা উপকারী।",
     "If gas and indigestion occur in stomach, walking for some time after meals is beneficial."),
    ("ঘন ঘন পেটের ডায়রিয়া হলে ডাবের পানি এবং খাওয়ার স্যালাইন পান করে পানিশূন্যতা রোধ করতে হবে।",
     "If frequent stomach diarrhea occurs, prevent dehydration by drinking coconut water and ORS."),
    ("হাঁপানি বা অ্যাজমার সমস্যা বাড়লে ডাক্তারের দেওয়া ইনহেলার সঠিক নিয়মে ব্যবহার করা উচিত।",
     "If asthma problem worsens, inhaler prescribed by doctor should be used in proper way.")
]

add_block("বুক ধড়ফড়", "Chest palpitations",
          "বুক ধড়ফড় করছে মাঝে মাঝে এটা কি হার্টের সমস্যা হতে পারে ?",
          "My chest is pounding sometimes. Could this be a heart problem?",
          p5_hr, p5_pr, p5_nr)

# ---------------------------------------------------------
# Prompt 6
# Genre: বুক ধড়ফড় | Chest palpitations
# Prompt: হঠাৎ করেই হার্টবিট বেড়ে যায় , বুক ধড়ফড় করে এটা কি স্বাভাবিক ? | My heart rate suddenly increases, my chest feels pounding. Is this normal?
# HR: 16, PR: 14, NR: 12
# ---------------------------------------------------------
p6_hr = [
    ("হঠাৎ হার্টবিট বেড়ে যাওয়া ও বুক ধড়ফড় করা সব সময় স্বাভাবিক নয় , তাই এটি হৃদরোগ নাকি মানসিক চাপের কারণে হচ্ছে তা ডাক্তারের মাধ্যমে পরীক্ষা করা উচিত।",
     "Suddenly increasing heart rate and chest pounding is not always normal , so whether it is due to heart disease or stress should be tested by a doctor."),
    ("তীব্র ভয় , দুশ্চিন্তা বা অতিরিক্ত ক্যাফেইন পানের কারণে হঠাৎ হার্টবিট বাড়তে পারে , তবে এটি প্রায়ই হলে চিকিৎসকের পরামর্শে ইসিজি করান।",
     "Severe fear, anxiety or excessive caffeine consumption can suddenly speed up heart rate , but if it happens often consult a doctor for an ECG."),
    ("যদি হার্টবিট বাড়ার সাথে মাথা ঘুরে ওঠা , বুকে চাপ লাগা বা শ্বাসকষ্ট অনুভব হয় , তবে অবিলম্বে নিকটস্থ হাসপাতালের জরুরি বিভাগে যান।",
     "If increased heart rate is accompanied by dizziness, chest pressure or shortness of breath , go to the nearest hospital emergency room immediately."),
    ("রক্তে থাইরয়েড হরমোন বৃদ্ধি বা রক্তস্বল্পতার কারণে হঠাৎ বুক ধড়ফড় হতে পারে , তাই রক্তের প্র প্রয়োজনীয় পরীক্ষা করানো দরকার।",
     "Increased thyroid hormone in blood or anemia can cause sudden chest pounding , so necessary blood tests are needed."),
    ("হঠাৎ হৃদস্পন্দন দ্রুত হলে বসে পড়ুন , চোখ বন্ধ করে ধীরে ধীরে গভীর শ্বাস গ্রহণ ও ত্যাগ করুন যাতে গতি স্বাভাবিক হয়।",
     "If heartbeat speeds up suddenly, sit down, close eyes and slowly inhale and exhale deeply to normalize the rate."),
    ("অ্যালকোহল , ধূমপান এবং প্রক্রিয়াজাত ক্যাফেইনযুক্ত পানীয় হঠাৎ হার্টবিট বাড়িয়ে দিতে পারে , তাই এগুলো এড়িয়ে চলা নিরাপদ।",
     "Alcohol, smoking and processed caffeinated drinks can suddenly increase heart rate , so avoiding them is safe."),
    ("রক্তে শর্করার মাত্রা হঠাৎ কমে গেলে (হাইপোগ্লাইসেমিয়া) বুক ধড়ফড় করতে পারে , তাই মিষ্টি কিছু খেয়ে দেখতে পারেন।",
     "If blood sugar level suddenly drops (hypoglycemia), chest can pound , so eating something sweet can be tried."),
    ("শারীরিক ডিহাইড্রেশন বা পানির ঘাটতি হৃদস্পন্দন হঠাৎ বাড়িয়ে দিতে পারে , তাই দিনে পর্যাপ্ত পানি ও তরল গ্রহণ করুন।",
     "Physical dehydration or lack of water can suddenly increase heartbeat , so drink adequate water and fluids during the day."),
    ("কিছু নির্দিষ্ট ওষুধের অ্যালার্জি বা পার্শ্বপ্রতিক্রিয়ার কারণে হৃদগতি হঠাৎ বাড়তে পারে , তাই সেবনকৃত ওষুধ ডাক্তারকে দেখান।",
     "Certain medicine allergies or side effects can cause sudden heart rate increases , so show your ingested medicines to doctor."),
    ("যদি হঠাৎ করে পালস রেট ১০০ এর উপরে চলে যায় এবং বেশ কিছুক্ষণ স্থায়ী হয় , তবে দ্রুত কার্ডিওলোজিস্টের শরণাপন্ন হওয়াই ভালো।",
     "If pulse rate suddenly goes above 100 and persists for a while , consulting a cardiologist quickly is best."),
    ("প্যানিক অ্যাটাক বা প্যানিক ডিজঅর্ডারের প্রধান লক্ষণ হলো হঠাৎ হার্টবিট তীব্র হওয়া , তবে হৃদযন্ত্রের পরীক্ষা ছাড়া সিদ্ধান্ত নেওয়া উচিত নয়।",
     "The main symptom of panic attack or panic disorder is sudden intense heartbeat , but decisions should not be made without heart tests."),
    ("অতিরিক্ত শারীরিক পরিশ্রম বা হঠাৎ ভারী কাজ শুরু করলেও হার্টবিট দ্রুত হতে পারে , তাই ভারী কাজের আগে ওয়ার্ম-আপ করুন।",
     "Excessive physical exertion or starting heavy work suddenly can speed up heartbeat , so warm up before heavy work."),
    ("শরীরে পটাসিয়াম বা ম্যাগনেসিয়ামের মাত্রা কমে গেলে হৃদস্পন্দনে এই অস্থিরতা দেখা দেয় , তাই চিকিৎসকের পরামর্শে ডায়েট বা সাপ্লিমেন্ট নিন।",
     "Decreased potassium or magnesium levels in body cause this instability in heartbeat , so take diet or supplements on doctor's advice."),
    ("হঠাৎ ধড়ফড় করা এড়াতে মানসিক চাপ নিয়ন্ত্রণ করুন , পর্যাপ্ত ঘুমান এবং প্রতিদিন নিয়মিত হালকা ইয়োগা বা প্রাণায়াম অনুশীলন করুন।",
     "To avoid sudden pounding manage mental stress, sleep adequately and practice light yoga or pranayama regularly every day."),
    ("ইসিজি বা হল্টার মনিটরিং টেস্ট করে নিলে হৃদযন্ত্রের রিদম বা স্পন্দনের গঠন সম্পর্কে নিশ্চিত হওয়া সম্ভব।",
     "Getting an ECG or Holter monitoring test makes it possible to confirm heart rhythm and beating pattern."),
    ("বারবার এমন ঘটনা ঘটলে এটিকে স্বাভাবিক ভেবে অবহেলা না করে বিশেষজ্ঞ ডাক্তারের তত্ত্বাবধানে সঠিক চিকিৎসা নেওয়া উচিত।",
     "If such events occur repeatedly, instead of ignoring it as normal, proper treatment under a specialist doctor should be taken.")
]

p6_pr = [
    ("হঠাৎ হার্টবিট বেড়ে যাওয়া অনেক সময় সাময়িক ভয় পাওয়ার কারণে ঘটে থাকে।",
     "Sudden increase in heart rate often happens due to temporary fear."),
    ("আমার এক সহকর্মীর হঠাৎ বুক ধড়ফড় শুরু হতো কিন্তু পরে দেখা গেল সে অনেক বেশি কফি খেতো।",
     "A colleague of mine had sudden chest pounding start but later it was found he drank too much coffee."),
    ("হৃদস্পন্দনের গতি বাড়লে মাথা শান্ত রেখে একটু জিরিয়ে নেওয়া ভালো উপায়।",
     "If heartbeat rate increases, keeping head cool and resting a bit is a good way."),
    ("আজকাল অতিরিক্ত দুশ্চিন্তার কারণে অনেকেরই হৃদস্পন্দন হঠাৎ অনিয়মিত হয়ে পড়তে দেখা যায়।",
     "Nowadays due to excessive worry, many people's heartbeats are seen to suddenly become irregular."),
    ("হঠাৎ শরীরের তাপমাত্রা বেড়ে গেলে বা জ্বর হলে হার্টবিট কিছুটা বৃদ্ধি পাওয়া খুব স্বাভাবিক।",
     "If body temperature suddenly rises or during fever, heart rate increasing somewhat is very normal."),
    ("যেকোনো শারীরিক সমস্যা বারবার হতে থাকলে চিকিৎসকের কাছে যাওয়া সচেতনতার লক্ষণ।",
     "If any physical problem recurs, visiting a doctor is a sign of awareness."),
    ("অফিসে হঠাৎ কোনো খারাপ খবর শুনলে বুক ধড়ফড় শুরু হতে পারে মানসিক আঘাতের কারণে।",
     "Hearing bad news suddenly at office can start chest pounding due to emotional shock."),
    ("প্রতিদিন সকালে কিছুক্ষণ খোলা বাতাসে হাঁটাহাঁটি করলে মন ও শরীর দুই-ই শান্ত থাকে।",
     "Walking in open air for a while every morning keeps both mind and body calm."),
    ("ঘুম ভালো না হলে পরদিন কাজের সময় হৃদস্পন্দন স্বাভাবিকের চেয়ে একটু দ্রুত হতে পারে।",
     "If sleep is not good, the next day during work heartbeat can be slightly faster than normal."),
    ("ধূমপান ছেড়ে দিলে হৃদযন্ত্রের গতি স্বাভাবিক রাখতে দারুণ সহায়তা পাওয়া যায়।",
     "Quitting smoking provides great assistance in maintaining normal heart rate."),
    ("উচ্চ রক্তচাপের রোগীদের নিয়মিত তাদের রক্তচাপ ও স্পন্দন পর্যবেক্ষণ করা দরকার।",
     "High blood pressure patients need to regularly monitor their blood pressure and pulse."),
    ("শরীরে হরমোনের তারতম্যের জন্য নারীদের প্রায়শই এমন হঠাৎ হার্টবিট বেড়ে যেতে দেখা যায়।",
     "Due to hormonal variations in the body, women often experience such sudden heart rate increases."),
    ("একটানা কাজ না করে মাঝে মাঝে বিরতি নিলে শরীরের ওপর বাড়তি চাপ কম পড়ে।",
     "Taking breaks occasionally instead of working continuously reduces extra strain on the body."),
    ("হৃৎপিন্ড সুস্থ রাখতে প্রতিদিন স্বাস্থ্যকর খাবার এবং পর্যাপ্ত পানি পান করা উচিত।",
     "To keep heart healthy, healthy food and adequate water should be consumed daily.")
]

p6_nr = [
    ("কোমর ব্যথার সমস্যায় ভারী জিনিস তোলা বাদ দিয়ে সোজা হয়ে বসার অভ্যাস করতে হবে।",
     "For waist pain problems, practice sitting straight avoiding lifting heavy objects."),
    ("পায়ের নখে ছত্রাক হলে হালকা গরম পানিতে লবণ দিয়ে পা ডুবিয়ে পরিষ্কার করা ভালো।",
     "If nail fungus occurs on foot, soaking feet in warm salt water to clean is good."),
    ("চোখের চুলকানি কমানোর জন্য চিকিৎসকের পরামর্শে অ্যান্টি-অ্যালার্জি আই ড্রপ ব্যবহার করতে হয়।",
     "To reduce eye itching, anti-allergy eye drops should be used on doctor's advice."),
    ("দাঁতের ক্ষয়রোধ করতে প্রতি রাতে খাওয়ার পর ভালোভাবে ব্রাশ করার নিয়ম মেনে চলুন।",
     "To prevent tooth decay, follow the rule of brushing thoroughly every night after eating."),
    ("পেটে অতিরিক্ত গ্যাস হলে ভাজাভুজি ও অতিরিক্ত মশলাযুক্ত খাবার খাওয়া এড়িয়ে চলুন।",
     "If excessive gas occurs in stomach, avoid eating fried and excessively spicy foods."),
    ("চুলের রুক্ষতা দূর করতে সপ্তাহে দুই দিন আমলকী ও শিকাকাই গুঁড়ো প্যাক চুলে লাগান।",
     "To remove hair dryness, apply amla and shikakai powder pack on hair two days a week."),
    ("হাত কেটে গেলে রক্তপাত বন্ধ করতে পরিচ্ছন্ন সুতি কাপড় দিয়ে চেপে ধরে রাখতে হবে।",
     "If hand is cut, press firmly with a clean cotton cloth to stop bleeding."),
    ("গলার খুসখুসে কাশির জন্য গরম পানিতে মধু ও লেবুর রস মিশিয়ে খেলে আরাম লাগে।",
     "For throat tickling cough, drinking warm water mixed with honey and lemon juice feels comfortable."),
    ("হাঁটুর ব্যথার জন্য অতিরিক্ত সিঁড়ি ভাঙা এড়িয়ে চলা এবং চিকিৎসকের পরামর্শে পেইনকিলার নেওয়া উচিত।",
     "For knee pain, avoiding extra stair climbing and taking painkillers on doctor's advice is recommended."),
    ("ত্বকের রোদে পোড়া দাগ দূর করতে কাঁচা দুধ ও শসার রস মুখে মেখে রাখলে উপকার পাওয়া যায়।",
     "To remove sunburn spots on skin, applying raw milk and cucumber juice on face is beneficial."),
    ("কানে তালা লাগলে গিলে খাওয়ার চেষ্টা করুন বা চুইংগাম চিবিয়ে কানের চাপ কমান।",
     "If ears feel clogged, try swallowing or chew gum to reduce ear pressure."),
    ("কোষ্ঠকাঠিন্য কমানোর জন্য খাদ্যতালিকায় আঁশযুক্ত শাকসবজি ও ফলমূল বেশি রাখা প্রয়োজন।",
     "To reduce constipation, keeping fiber-rich vegetables and fruits more in diet is necessary.")
]

add_block("বুক ধড়ফড়", "Chest palpitations",
          "হঠাৎ করেই হার্টবিট বেড়ে যায় , বুক ধড়ফড় করে এটা কি স্বাভাবিক ?",
          "My heart rate suddenly increases, my chest feels pounding. Is this normal?",
          p6_hr, p6_pr, p6_nr)

# Save progress to check script
print("Processed prompts 1 through 6.")

# ---------------------------------------------------------
# Prompt 7
# Genre: পেটে গ্যাস | Gas in the stomach
# Prompt: পেটে সবসময় গ্যাস ধরে থাকে কি করলে এই সমস্যা কমবে ? | I always have gas in my stomach. What can I do to reduce this problem?
# HR: 14, PR: 16, NR: 14
# ---------------------------------------------------------
p7_hr = [
    ("পেটে গ্যাস কমানোর জন্য ভাজাপোড়া ও অতিরিক্ত মশলাযুক্ত খাবার পুরোপুরি এড়িয়ে চলুন এবং প্রতিদিন অন্তত ৮ থেকে ১০ গ্লাস পানি পান করুন।",
     "To reduce stomach gas, completely avoid fried and excessively spicy food and drink at least 8 to 10 glasses of water daily."),
    ("খাবার খাওয়ার পরপরই শুয়ে না পড়ে ১৫-২০ মিনিট হাঁটার অভ্যাস করুন এবং ধীরে ধীরে খাবার চিবিয়ে খান।",
     "Form a habit of walking for 15-20 minutes after meals instead of lying down immediately, and chew food slowly."),
    ("পেটে গ্যাস ধরে থাকা কমাতে ধূমপান ও কোমল পানীয় (সফট ড্রিংকস) পান সম্পূর্ণ বন্ধ করতে হবে।",
     "To reduce trapped stomach gas, smoking and drinking soft drinks must be stopped completely."),
    ("খাদ্যতালিকায় আঁশযুক্ত খাবার ও শাকসবজি বাড়ান , এবং পেট খালি না রেখে অল্প অল্প করে বারবার খাওয়ার অভ্যাস করুন।",
     "Increase fiber foods and vegetables in your diet , and form a habit of eating small meals frequently without keeping stomach empty."),
    ("অ্যান্টাসিড বা গ্যাস্ট্রিকের ওষুধ ডাক্তারের পরামর্শ অনুযায়ী নির্দিষ্ট সময়ে সেবন করুন।",
     "Take antacids or gastric medicines at specific times according to doctor's advice."),
    ("প্রসেসড ফুড , ডুবো তেলে ভাজা নাস্তা ও অতিরিক্ত চা-কফি পানের অভ্যাস পেটে গ্যাস বাড়ায় , তাই এগুলো এড়িয়ে চলা উচিত।",
     "Processed food, deep fried snacks and excessive tea-coffee consumption increase stomach gas , so these should be avoided."),
    ("শোবার অন্তত দুই থেকে তিন ঘণ্টা আগে রাতের খাবার শেষ করুন যাতে হজম প্রক্রিয়া সঠিকভাবে সম্পন্ন হতে পারে।",
     "Finish dinner at least two to three hours before bedtime so that digestion process can be completed properly."),
    ("খাবার খাওয়ার সময় অতিরিক্ত কথা বলবেন না যাতে পেটে বাতাস না ঢোকে , এবং বাইরের খোলা বা বাসি খাবার এড়িয়ে চলুন।",
     "Do not talk excessively while eating to prevent air entering stomach , and avoid outside open or stale food."),
    ("আদা চা বা হালকা গরম পানিতে লেবুর রস মিশিয়ে খেলে পেটের অসস্তি ও গ্যাস দ্রুত হ্রাস পায়।",
     "Drinking ginger tea or lemon juice mixed in warm water rapidly decreases stomach discomfort and gas."),
    ("যদি পেটে গ্যাসের সাথে তীব্র ব্যথা , বমি বা ওজন কমার মতো সমস্যা থাকে , তবে বিলম্ব না করে একজন গ্যাস্ট্রোএন্টারোলজিস্টকে দেখান।",
     "If stomach gas is accompanied by severe pain, vomiting or weight loss, consult a gastroenterologist without delay."),
    ("প্রতিদিন নিয়মিত সময়ের ব্যবধানে খাবার খান এবং দীর্ঘক্ষণ না খেয়ে পেট খালি রাখার অভ্যাস ত্যাগ করুন।",
     "Eat meals at regular intervals every day and quit the habit of keeping stomach empty by not eating for long periods."),
    ("দই বা প্রোবায়োটিক জাতীয় খাবার খান যা পেটের ভালো ব্যাকটেরিয়া বাড়াতে এবং হজমশক্তি উন্নত করতে সাহায্য করে।",
     "Eat yogurt or probiotic foods which help increase good stomach bacteria and improve digestion."),
    ("চিবিয়ে চুইংগাম খাওয়ার অভ্যাস বাদ দিন কারণ এতে পেটে অতিরিক্ত বাতাস ঢুকে গ্যাস ও পেট ফোলা তৈরি করে।",
     "Quit the habit of chewing gum because it allows excess air into stomach creating gas and bloating."),
    ("শারীরিকভাবে সক্রিয় থাকুন , কারণ প্রতিদিন নিয়মিত হাঁটা বা ব্যায়াম করলে পরিপাকতন্ত্র সক্রিয় থাকে এবং গ্যাস কমে।",
     "Stay physically active , because daily regular walking or exercise keeps the digestive system active and reduces gas.")
]

p7_pr = [
    ("পেটে গ্যাস হওয়ার প্রধান কারণ হলো অস্বাস্থ্যকর খাদ্যাভ্যাস ও প্রক্রিয়াজাত খাবার খাওয়া।",
     "The main reason for stomach gas is unhealthy food habits and eating processed foods."),
    ("আমার এক আত্মীয় দীর্ঘদিন ধরে গ্যাস্ট্রিকের সমস্যায় ভুগছিলেন এবং তিনি নিয়মিত পুদিনা পাতার রস খেতেন।",
     "A relative of mine suffered from gastric problems for a long time and used to drink mint leaf juice regularly."),
    ("গ্যাসের কারণে বুক জ্বালাপোড়া করা এবং অস্বস্তি হওয়া খুব সাধারণ ঘটনা।",
     "Heartburn and discomfort due to gas are very common occurrences."),
    ("ফাস্টফুড বা অতিরিক্ত চর্বিযুক্ত খাবার খেলে হজমে দেরি হয় যা পেটে অতিরিক্ত গ্যাস তৈরি করে।",
     "Eating fast food or overly fatty food delays digestion which generates excess gas in stomach."),
    ("রাতের খাবার দেরি করে খেলে হজম প্রক্রিয়া ধীর হয়ে যায় এবং গ্যাস্ট্রিকের সমস্যা বাড়তে দেখা যায়।",
     "Eating dinner late slows down digestion process and gastric problems are seen to increase."),
    ("পেটের সমস্যা দূর করতে নিয়মিত ভালো ঘুম এবং মানসিক চাপমুক্ত থাকা খুব দরকার।",
     "To remove stomach problems, regular good sleep and staying stress-free are very necessary."),
    ("অনেকে গ্যাস কমানোর জন্য ঘরোয়া উপাদান হিসেবে জিরা পানি পান করে উপকার পেয়ে থাকেন।",
     "Many people get relief by drinking cumin water as a home remedy to reduce gas."),
    ("প্যাকেটজাত স্ন্যাকস বা চিপস খাওয়ার অভ্যাস গ্যাস্ট্রিকের লক্ষণ বাড়াতে ভূমিকা রাখে।",
     "Habit of eating packaged snacks or chips plays a role in increasing gastric symptoms."),
    ("সকালে খালি পেটে এক গ্লাস কুসুম গরম পানি পান করা স্বাস্থ্যের জন্য বেশ ভালো একটি অভ্যাস।",
     "Drinking a glass of lukewarm water on empty stomach in morning is quite a good habit for health."),
    ("অফিসে একটানা এক জায়গায় বসে কাজ করলেও হজম ভালো হয় না এবং পেটে গ্যাস জমা হতে পারে।",
     "Sitting and working in one place continuously at office also hinders digestion and gas can accumulate in stomach."),
    ("আজকাল ফাস্টফুড সংস্কৃতির কারণে কমবয়সী তরুণদের মধ্যেও পেটের গ্যাস খুব বেশি দেখা যায়।",
     "Nowadays due to fast food culture, stomach gas is seen very much among young youth too."),
    ("অতিরিক্ত অতিরিক্ত মসলা দেওয়া তরকারি খাওয়ার পর অনেকেরই পেট ভার হয়ে থাকে।",
     "After eating curry with excessive spices, many people's stomach feels heavy."),
    ("সঠিক সময়ে খাবার খাওয়া শারীরিক সুস্থতার জন্য অত্যন্ত জরুরি একটি দিক।",
     "Eating food at the right time is an extremely important aspect for physical well-being."),
    ("খাবারে কাঁচা পেঁয়াজ বা শসা বেশি খেলে কিছু কিছু মানুষের গ্যাস্ট্রিকের সমস্যা হতে দেখা যায়।",
     "Eating excess raw onion or cucumber in meals is seen to cause gastric problems in some people."),
    ("প্যাক করা ঠাণ্ডা জুস বা কার্বোনেটেড ড্রিংকস পেটের হজমক্ষমতা কমিয়ে দেয়।",
     "Packaged cold juice or carbonated drinks reduce stomach digestion capacity."),
    ("হজমশক্তি ভালো রাখতে প্রতিদিন পর্যাপ্ত পানি পান করা সবচেয়ে দরকারি কাজ।",
     "Drinking adequate water every day is the most necessary work to keep digestive power good.")
]

p7_nr = [
    ("চোখের ছানি অপারেশনের পর ধুলোবালি থেকে চোখকে রক্ষা করতে কাল চশমা ব্যবহার করা উচিত।",
     "After eye cataract surgery, dark glasses should be used to protect eyes from dust."),
    ("পায়ের গোড়ালির হাড় বাড়লে চিকিৎসকের পরামর্শে বিশেষ প্যাডযুক্ত জুতো ব্যবহার করতে হয়।",
     "If heel bone expands, special padded shoes should be used on doctor's advice."),
    ("মাথার চুল অতিরিক্ত পড়তে থাকলে আয়ুর্বেদিক আমলকীর তেল ব্যবহার করা যেতে পারে।",
     "If head hair falls excessively, ayurvedic amla oil can be used."),
    ("চামড়ায় দাউদ বা ফাঙ্গাল ইনফেকশন হলে নিয়মিত অ্যান্টিফাঙ্গাল সাবান ও ক্রিম ব্যবহার করা দরকার।",
     "If ringworm or fungal infection occurs on skin, regular antifungal soap and cream should be used."),
    ("কানের ভেতরের ময়লা পরিষ্কার করার জন্য কখনো মেছ বা কটন বাড ঢুকানো উচিত নয়।",
     "Matches or cotton buds should never be inserted to clean dirt inside ears."),
    ("হাতের কব্জির হাড় মচকে গেলে ব্যান্ডেজ বেঁধে হাতকে বিশ্রামে রাখা উচিত।",
     "If wrist bone sprains, tie a bandage and keep the hand at rest."),
    ("মাইগ্রেনের মাথাব্যথা শুরু হলে অন্ধকার ঘরে শান্ত হয়ে শুয়ে থাকা ভালো।",
     "If migraine headache starts, lying down calmly in a dark room is good."),
    ("দাঁত আঁকাবাঁকা হলে ডেন্টিস্টের কাছে গিয়ে ব্রেসেস লাগিয়ে সোজা করা যায়।",
     "If teeth are crooked, visit dentist and straighten them by applying braces."),
    ("তীব্র হাঁপানির সমস্যায় ডাক্তারের দেওয়া ইনহেলার পকেটে রাখা আবশ্যক।",
     "In severe asthma problems, keeping doctor-prescribed inhaler in pocket is mandatory."),
    ("হাঁটুর ক্ষয়রোধ করতে প্রতিদিন নিয়মিত সায়কেলিং বা সাঁতার কাটার পরামর্শ দেওয়া হয়।",
     "To prevent knee degeneration, regular cycling or swimming daily is advised."),
    ("ঠোঁট ফেটে গেলে গ্লিসারিন বা ভেসলিন ব্যবহার করলে বেশ দ্রুত আরাম পাওয়া যায়।",
     "If lips chaps, using glycerin or vaseline provides relief quite rapidly."),
    ("গলার খুসখুসে কাশির জন্য গরম পানিতে মধু ও তুলসী পাতার রস খাওয়া যেতে পারে।",
     "For throat tickling cough, honey and tulsi leaf juice in warm water can be taken."),
    ("ত্বকে রোদে পোড়া দাগ দূর করতে অ্যালোভেরা জেল রাতে মুখে মেখে রাখলে উপকার মেলে।",
     "To remove sunburn spots on skin, applying aloe vera gel on face at night yields benefits."),
    ("কানের ভেতরের ইনফেকশনের জন্য চিকিৎসকের পরামর্শ নিয়ে অ্যান্টিবায়োটিক ড্রপ দেওয়া প্রয়োজন।",
     "For internal ear infections, taking doctor's advice to apply antibiotic drops is necessary.")
]

add_block("পেটে গ্যাস", "Gas in the stomach",
          "পেটে সবসময় গ্যাস ধরে থাকে কি করলে এই সমস্যা কমবে ?",
          "I always have gas in my stomach. What can I do to reduce this problem?",
          p7_hr, p7_pr, p7_nr)

# ---------------------------------------------------------
# Prompt 8
# Genre: দাঁত ব্যাথা | Toothache
# Prompt: কিছুদিন হলো দাঁতের মধ্যে ঝনঝন ব্যথা হয় বিশেষ করে ঠান্ডা পানিতে , এখন কি করা উচিত আমার ? | I have been experiencing a tingling pain in my teeth for the past few days, especially with cold water. What should I do now?
# HR: 14, PR: 16, NR: 14
# ---------------------------------------------------------
p8_hr = [
    ("দাঁতে ঝনঝন ব্যথা বা সেনসিটিভিটি হলে দ্রুত একজন ডেন্টিস্ট দেখান এবং চিকিৎসকের পরামর্শ অনুযায়ী সেনসিটিভ দাঁতের টুথপেস্ট ব্যবহার করুন।",
     "If you experience tooth tingling pain or sensitivity, quickly visit a dentist and use sensitive toothpaste as recommended by the doctor."),
    ("অতিরিক্ত ঠান্ডা বা খুব গরম পানীয় খাওয়া বন্ধ রাখুন এবং নরম ব্রিসলের টুথব্রাশ দিয়ে দিনে দুবার হালকা হাতে দাঁত ব্রাশ করুন।",
     "Stop consuming extremely cold or very hot drinks and brush teeth gently twice a day with a soft-bristled toothbrush."),
    ("মিষ্টি ও এসিডিক খাবার খাওয়া কমান এবং খাওয়ার পর ভালো করে কুসুম গরম পানিতে লবণ মিশিয়ে কুলকুচি করুন।",
     "Reduce eating sweet and acidic foods and gargle thoroughly with lukewarm salt water after eating."),
    ("দাঁতের ক্ষয় (ক্যাভিটি) বা মাড়ির সমস্যা আছে কিনা তা নিশ্চিত হতে ডেন্টিস্টের কাছে গিয়ে এনামেল পরীক্ষা ও ফিলিং করান।",
     "To confirm whether there is tooth decay (cavity) or gum problems, visit dentist for enamel examination and filling."),
    ("জোরালো শক্ত ব্রাশ দিয়ে দাঁত ঘষা বন্ধ করুন , কারণ এতে দাঁতের সুরক্ষাকারী এনামেল ক্ষয়ে সেনসিটিভিটি বা ঝনঝনানি বাড়ে।",
     "Stop scrubbing teeth with a hard brush , as it wears down tooth protecting enamel and increases sensitivity or tingling."),
    ("সাময়িক ব্যথা কমানোর জন্য লবঙ্গ বা লবঙ্গের তেল হালকা তুলোয় নিয়ে আক্রান্ত দাঁতের গোড়ায় চেপে ধরে রাখতে পারেন।",
     "For temporary pain relief, clove or clove oil can be lightly taken on cotton and pressed against the affected tooth root."),
    ("খাবারের কণা যাতে দাঁতের ফাঁকে জমে না থাকে সেজন্য ডেন্টাল ফ্লস ব্যবহার করে দাঁত পরিষ্কার রাখুন।",
     "Use dental floss to keep teeth clean so that food particles do not get trapped between teeth."),
    ("আইসক্রিম , কোল্ড ড্রিংকস বা ফ্রিজের ঠান্ডা পানি সরাসরি খাওয়া সম্পূর্ণ বন্ধ করতে হবে।",
     "Eating ice cream, cold drinks or direct refrigerated cold water must be completely stopped."),
    ("মাড়ির কোনো ইনফেকশন থাকলে ডাক্তার অ্যান্টিসেপটিক মাউথওয়াশ ব্যবহার করার পরামর্শ দিতে পারেন যা নিয়মিত ব্যবহার করা উচিত।",
     "If there is any gum infection, doctor may advise using an antiseptic mouthwash which should be used regularly."),
    ("যদি ব্যথার সাথে মাড়ি ফুলে যাওয়া বা রক্ত পড়ার লক্ষণ থাকে , তবে বিলম্ব না করে ডেন্টাল ক্লিনিকে যান।",
     "If pain is accompanied by gum swelling or bleeding symptoms, go to a dental clinic without delay."),
    ("দাঁতের এনামেল ক্ষয় প্রতিরোধে ক্যালসিয়াম ও ভিটামিন সি যুক্ত খাবার খাদ্যতালিকায় অন্তর্ভুক্ত করুন।",
     "Include foods rich in calcium and vitamin C in your diet to prevent tooth enamel erosion."),
    ("রাতে ঘুমানোর আগে অবশ্যই দাঁত ব্রাশ করার অভ্যাস করুন যাতে দাঁতে ব্যাকটেরিয়ার আক্রমণ না ঘটে।",
     "Must make a habit of brushing teeth before sleeping at night so that bacterial attack does not occur on teeth."),
    ("অতিরিক্ত শক্ত খাবার যেমন সুপারি বা হাড় দাঁত দিয়ে চাবানো থেকে বিরত থাকুন।",
     "Refrain from chewing extremely hard foods like betel nut or bones with teeth."),
    ("ডাক্তারের পরামর্শ ছাড়া দোকান থেকে এলোমেলো ব্যথানাশক ওষুধ কিনে সেবন করা বন্ধ করুন।",
     "Stop buying random painkiller medicines from shops and consuming them without doctor's advice.")
]

p8_pr = [
    ("ঠান্ডা পানি খেলে দাঁত শিরশির করা বা ঝনঝন করা দাঁতের ক্ষয়ের অন্যতম প্রধান লক্ষণ।",
     "Teeth tingling or sensitivity when drinking cold water is one of the main symptoms of tooth decay."),
    ("আমার ভাইয়ের কিছুদিন দাঁতের এনামেল নষ্ট হয়ে গিয়ে ঠান্ডা ও মিষ্টি খাবার খেলে খুব ব্যথা হতো।",
     "My brother had tooth enamel damaged for a few days and experienced severe pain when eating cold and sweet food."),
    ("দাঁতের সুরক্ষায় সঠিক নিয়ম মেনে দৈনিক দুইবার ব্রাশ করা অত্যন্ত জরুরি বলে ডেন্টিস্টরা জানান।",
     "Dentists state that brushing twice daily following correct rules is extremely important for tooth protection."),
    ("লবঙ্গের তেল দাঁতের ব্যথা কমাতে বেশ কার্যকর একটি প্রাচীন ঘরোয়া পদ্ধতি হিসেবে পরিচিত।",
     "Clove oil is known as quite an effective ancient home remedy for reducing toothache."),
    ("ফ্রিজের ঠান্ডা পানি হঠাৎ করে পান করলে দাঁতের নার্ভে তীব্র ঝাঁকুনি অনুভূত হতে পারে।",
     "Drinking refrigerated cold water suddenly can cause severe shock feeling in tooth nerves."),
    ("দাঁতে ক্যাভিটি বা গর্ত তৈরি হলে সেখানে খাবার জমে ইনফেকশন তৈরি হতে দেখা যায়।",
     "When cavities or holes form in teeth, food particles get trapped there creating infection."),
    ("টুথব্রাশ প্রতি তিন মাস পর পর পরিবর্তন করা মুখের স্বাস্থ্য ভালো রাখার নিয়ম।",
     "Changing toothbrush every three months is a rule to keep mouth health good."),
    ("মাড়ির রোগ অবহেলা করলে পরবর্তীতে দাঁত নড়ে যাওয়া বা পড়ে যাওয়ার ঝুঁকি থাকে।",
     "Neglecting gum disease runs the risk of teeth loosening or falling out later."),
    ("বেশি মিষ্টি বা চকলেট খেলে বাচ্চাদের দাঁতে পোকা লাগার সমস্যা বেশি হয়।",
     "Eating excess sweets or chocolates causes more tooth decay problems in children."),
    ("দাঁতের যত্নে ভালো মানের ফ্লোরাইড যুক্ত টুথপেস্ট ব্যবহার করার পরামর্শ বিশেষজ্ঞদের।",
     "Experts advise using good quality fluoride toothpaste for tooth care."),
    ("খাবার খাওয়ার পর পানি দিয়ে ভালো করে কুলকুচি না করলে মুখে দুর্গন্ধ ও দাঁতের ক্ষতি হতে পারে।",
     "Not gargling properly with water after eating meals can cause bad breath and tooth damage."),
    ("দাঁতের সংবেদনশীলতা কমানোর জন্য নির্দিষ্ট মেডিকেটেড টুথপেস্ট বেশ উপকারী।",
     "Specific medicated toothpaste is quite beneficial for reducing tooth sensitivity."),
    ("ডেন্টাল চেকাআপ বছরে অন্তত একবার করানো মুখের সুস্থতার জন্য খুব ভালো।",
     "Getting a dental checkup at least once a year is very good for mouth health."),
    ("দাঁত দিয়ে বোতলের ক্যাপ খোলা বা শক্ত জিনিস কামড়ানো দাঁতের মারাত্বক ক্ষতি করতে পারে।",
     "Opening bottle caps or biting hard objects with teeth can cause severe damage to teeth."),
    ("ঠান্ডা বাতাসে মুখ খোলা রাখলেও অনেক সময় সেনসিটিভ দাঁতে হালকা ঝনঝনানি অনুভব হতে পারে।",
     "Keeping mouth open in cold air can also sometimes make sensitive teeth feel mild tingling."),
    ("দাঁতের সমস্যা দীর্ঘদিন জিইয়ে রাখলে পরবর্তীতে রুট ক্যানেল করার প্রয়োজন পড়ে।",
     "Persisting tooth problems for long term creates need for root canal treatment later.")
]

p8_nr = [
    ("পায়ের তালু ফোলা কমানোর জন্য রাতে ঘুমানোর সময় পায়ের নিচে বালিশ দিয়ে রাখা ভালো।",
     "To reduce foot sole swelling, placing a pillow under feet while sleeping at night is good."),
    ("চোখে রোদ লাগলে চোখ দিয়ে পানি পড়লে রোদে বের হওয়ার সময় ছাতা ব্যবহার করা উচিত।",
     "If eyes water due to sunlight, an umbrella should be used when going out in the sun."),
    ("পাতে কাঁচা লবণ বেশি খেলে উচ্চ রক্তচাপের ঝুঁকি বহুগুণ বেড়ে যায়।",
     "Eating excess raw salt with meals increases risk of high blood pressure many times."),
    ("গলার আওয়াজ বসে গেলে আদা ও মধু দিয়ে ফোটানো পানি খেলে গলার স্বর ফিরে আসে।",
     "If voice sits down, drinking water boiled with ginger and honey restores voice."),
    ("হাতে অ্যাকজিমা হলে ক্ষারযুক্ত সাবান না মেখে আর্দ্রতাদায়ক লোশন দেওয়া দরকার।",
     "If hand eczema occurs, apply moisturizing lotion instead of using alkaline soap."),
    ("হাঁটুর লিগামেন্ট ব্যথা দূর করতে নিয়ম করে বরফ থেরাপি দেওয়া উত্তম।",
     "To eliminate knee ligament pain, giving regular ice therapy is best."),
    ("পেটে আলসারের ব্যথা কমানোর জন্য ভাজাপোড়া ও তেলযুক্ত খাবার ত্যাগ করা প্রয়োজন।",
     "To reduce stomach ulcer pain, quitting fried and oily food is necessary."),
    ("চুলের শুষ্কতা দূর করতে নারিকেল তেল গরম করে মাথার ত্বকে ম্যাসাজ করুন।",
     "To remove hair dryness, warm coconut oil and massage into scalp."),
    ("পিঠের তীব্র ব্যথার জন্য শক্ত তোশকে সোজা হয়ে ঘুমানোর অভ্যাস গড়ে তুলুন।",
     "For severe back pain, develop habit of sleeping straight on a firm mattress."),
    ("অ্যাজমা পেশেন্টদের ধুলোবালি ও ঠান্ডা বাতাস থেকে নিজেদের বাঁচিয়ে রাখা উচিত।",
     "Asthma patients should protect themselves from dust and cold air."),
    ("কিডনিতে পাথর হওয়া প্রতিরোধে প্রতিদিন প্রচুর পরিমাণে পানি পান করা প্রয়োজন।",
     "Drinking plenty of water daily is necessary to prevent kidney stones."),
    ("ত্বকে ছুলি বা সাদা দাগ হলে ডার্মাটোলজিস্ট দেখিয়ে ভালো অ্যান্টিফাঙ্গাল সাবান ব্যবহার করুন।",
     "If tinea or white spots appear on skin, consult dermatologist and use good antifungal soap."),
    ("কোষ্ঠকাঠিন্য দূর করতে শাকসবজি ও আঁশযুক্ত ফল নিয়মিত খাদ্যতালিকায় রাখুন।",
     "Include vegetables and fiber-rich fruits regularly in diet to remove constipation."),
    ("কানের ভেতরের ড্রাম ফেটে গেলে কান শুকনো রাখা ও পানি না ঢুকানো জরুরি।",
     "If inner ear drum ruptures, keeping ear dry and not letting water enter is essential.")
]

add_block("দাঁত ব্যাথা", "Toothache",
          "কিছুদিন হলো দাঁতের মধ্যে ঝনঝন ব্যথা হয় বিশেষ করে ঠান্ডা পানিতে , এখন কি করা উচিত আমার ?",
          "I have been experiencing a tingling pain in my teeth for the past few days, especially with cold water. What should I do now?",
          p8_hr, p8_pr, p8_nr)

print("Processed prompts 7 and 8.")

# ---------------------------------------------------------
# Prompt 9
# Genre: ঘাড় শক্ত | Stiff neck
# Prompt: ঘাড়ের ডান পাশে শক্ত হয়ে গেছে , ঘোরাতে পারছি না ভালোভাবে , এখন কি করা উচিত আমার ? | The right side of my neck is stiff, I can't move it properly, what should I do now?
# HR: 14, PR: 18, NR: 14
# ---------------------------------------------------------
p9_hr = [
    ("ঘাড়ের ডানপাশে ১০-১৫ মিনিট হালকা গরম পানির ভাপ বা আইস প্যাক দিন , এবং হুট করে জোর করে ঘাড় ঘুরানোর চেষ্টা করবেন না।",
     "Apply light warm water steam or ice pack on the right side of the neck for 10-15 minutes , and do not try to forcibly turn the neck suddenly."),
    ("পেশীর শক্তভাব ও ব্যথা কমানোর জন্য চিকিৎসকের পরামর্শ নিয়ে ব্যথানাশক বা মাসল রিল্যাক্স্যান্ট ওষুধ সেবন করা যেতে পারে।",
     "Painkillers or muscle relaxants can be taken on doctor's advice to reduce muscle stiffness and pain."),
    ("উঁচু বা শক্ত বালিশ বাদ দিয়ে পাতলা বালিশে সোজা হয়ে ঘুমানোর অভ্যাস করুন যাতে ঘাড়ে বাড়তি চাপ না পড়ে।",
     "Form a habit of sleeping straight on a thin pillow discarding high or hard pillows so that extra pressure is not exerted on neck."),
    ("আক্রান্ত স্থানে হালকা হাতে ব্যথানাশক জেল ম্যাসাজ করুন , তবে জাবড়ে অতিরিক্ত চাপ দেওয়া থেকে বিরত থাকুন।",
     "Gently massage pain relieving gel on affected area , but refrain from applying heavy pressure."),
    ("একটানা মাথা নিচু করে মোবাইল বা ল্যাপটপ ব্যবহার সম্পূর্ণ বন্ধ রেখে ঘাড়কে পর্যাপ্ত বিশ্রাম দিন।",
     "Give neck adequate rest by completely stopping usage of mobile or laptop with head bent down continuously."),
    ("যদি তীব্র ব্যথার সাথে জ্বর , প্রচণ্ড মাথাব্যথা বা বমি থাকে , তবে অবহেলা না করে দ্রুত হাসপাতালে যোগাযোগ করুন।",
     "If severe pain is accompanied by fever, severe headache or vomiting, contact hospital quickly without neglect."),
    ("ধীরে ধীরে ঘাড় ডানে-বামে হালকা প্রসারণ বা স্ট্রেচিং ব্যায়াম করার চেষ্টা করুন যদি তাতে অতিরিক্ত ব্যথা না হয়।",
     "Try slowly doing light stretching exercises right-left with neck if it does not cause severe pain."),
    ("ভারী কাঁধের ব্যাগ বা ওজন বহন করা থেকে একদম দূরে থাকুন যাতে ডানপাশের পেশীতে টান না লাগে।",
     "Stay completely away from carrying heavy shoulder bags or weights so that right side muscle is not strained."),
    ("শোবার সময় ঘাড়ের নিচে পেঁচানো তোয়ালে দিয়ে ব্যাক সাপোর্ট দিন যাতে ঘুমন্ত অবস্থায় পেশী শিথিল থাকে।",
     "Give back support with a rolled towel under neck while sleeping so that muscles stay relaxed during sleep."),
    ("ঘাড়ের ডানপাশের তীব্র পেশী সংকোচনের জন্য সাময়িকভাবে সফট সার্ভিক্যাল কলার ব্যবহার করে ঘাড় স্থির রাখা যায়।",
     "Soft cervical collar can be used temporarily to keep neck stable for severe muscle spasms on right side of neck."),
    ("সকালে কুসুম গরম পানিতে গোসল করলে ঘাড়ের শক্ত হয়ে থাকা পেশীগুলো শিথিল হয়ে ব্যথা কমতে সাহায্য করে।",
     "Showering in lukewarm water in morning helps relax stiff neck muscles and reduces pain."),
    ("যদি ব্যথা হাতের আঙুল পর্যন্ত ছড়িয়ে পড়ে বা ঝিনঝিন করে , তবে একজন নিউরো বিশেষজ্ঞকে দিয়ে নিউরোলজিক্যাল পরীক্ষা করান।",
     "If pain radiates to fingers or causes tingling, undergo a neurological exam with a neurologist."),
    ("গাড়ি চালানো বা ভ্রমণের সময় ঘাড় অতিরিক্ত ঝাঁকুনি থেকে রক্ষা করতে ঘাড়ের বিশেষ পিলো বা সাপোর্ট ব্যবহার করুন।",
     "Use special neck pillow or support while driving or traveling to protect neck from excessive jerks."),
    ("কয়েকদিন পার হওয়ার পরও যদি ঘাড়ে এই শক্তভাব স্থায়ী থাকে , তবে কোনো ফিজিওথেরাপিস্টের কাছে গিয়ে ফিজিওথেরাপি নিন।",
     "If this stiffness in neck persists even after a few days, visit a physiotherapist for physiotherapy.")
]

p9_pr = [
    ("রাতে ঘুমানোর সময় ভুল ভঙ্গিতে ঘাড় বেঁকে থাকলে সকালে ঘাড় শক্ত হয়ে যাওয়ার সমস্যা দেখা দেয়।",
     "If neck stays bent in wrong posture while sleeping at night, neck stiffness problem appears in morning."),
    ("এসি বা ঠান্ডা বাতাসের মধ্যে বেশিক্ষণ থাকলে ঘাড়ের পেশী শক্ত হয়ে গিয়ে নাড়াতে কষ্ট হতে পারে।",
     "Staying in AC or cold air for too long can stiffen neck muscles and make movement difficult."),
    ("ল্যাপটপের সামনে ঠিকমতো না বসে কাজ করলে ঘাড়ের একপাশে টান লেগে শক্ত হয়ে যেতে পারে।",
     "Working in front of laptop without sitting properly can strain and stiffen one side of neck."),
    ("ঘাড় শক্ত হলে বেশি টানাটানি বা জোর করে ম্যাসাজ করলে পেশীর ক্ষতি হতে পারে বলে চিকিৎসকরা জানান।",
     "Doctors state that if neck is stiff, pulling too much or forceful massaging can damage muscles."),
    ("সোজা হয়ে বসার অভ্যাস এবং কাজের মাঝে মাঝেই হালকা ঘাড় ঘোরানো স্বাস্থ্যের জন্য বেশ ভালো।",
     "Habit of sitting upright and lightly rotating neck between work is quite good for health."),
    ("মানসিক চাপের কারণেও অনেক সময় শরীরের ঘাড় ও কাঁধের পেশীগুলো শক্ত ও সংকুচিত হয়ে থাকে।",
     "Mental stress often causes body's neck and shoulder muscles to become stiff and contracted."),
    ("বালিশ ছাড়া ঘুমানো নাকি একটি উঁচু বালিশে ঘুমানো ভালো তা নিয়ে একেক জনের একেক মতামত রয়েছে।",
     "There are differing opinions among people on whether sleeping without pillow or on one high pillow is better."),
    ("পেশীতে হঠাৎ টান লাগলে সেখানে দ্রুত আরাম পেতে ঘরোয়া হিসেবে গরম শেক দেওয়ার নিয়ম প্রচলিত।",
     "Giving hot compress as a home remedy rule is common to get quick relief when muscle suddenly pulls."),
    ("প্রতিদিন নিয়ম করে শরীরচর্চা করলে শরীর নমনীয় থাকে এবং ঘাড় শক্ত হওয়ার ঝুঁকি কমে যায়।",
     "Exercising regularly every day keeps body flexible and reduces risk of stiff neck."),
    ("যানবাহনে ভ্রমণের সময় বা বাসে ঘুমিয়ে পড়লে অনেকেরই ঘাড় বাঁকা হয়ে রগে চোট লাগে।",
     "While traveling in vehicles or sleeping on bus, many people get neck bent and muscle injured."),
    ("মাথা নিচু করে বেশিক্ষণ মোবাইল স্ক্রোল করার অভ্যাস টেক-নেক সমস্যার জন্ম দিচ্ছে।",
     "Habit of scrolling mobile with head bent down for a long time gives birth to tech-neck problem."),
    ("ঘাড়ের হাড় ক্ষয়ের সমস্যার কারণে বয়স বাড়লে ঘাড়ের নড়াচড়া সীমিত ও শক্ত হয়ে পড়ে।",
     "Due to neck bone degeneration problems with aging, neck movement becomes limited and stiff."),
    ("ঘাড় শক্ত হলে তাড়াহুড়ো না করে ধীরে ধীরে মাথা নড়াচড়া করা উচিত যাতে আঘাত না পায়।",
     "If neck is stiff, move head slowly without rushing so that it does not get injured."),
    ("দীর্ঘদিন ধরে কাজ করার সময় কম্পিউটারের স্ক্রিনের উচ্চতা চোখের লেভেলে রাখা জরুরি।",
     "While working for long hours, keeping computer screen height at eye level is essential."),
    ("অফিস চেয়ারের সাপোর্ট সঠিক না হলে ঘাড়ে ও পিঠে দীর্ঘমেয়াদী পেশী ব্যাথা ও শক্তভাব হতে পারে।",
     "If office chair support is not correct, long-term muscle pain and stiffness can occur in neck and back."),
    ("শোবার ঘর অতিরিক্ত ঠান্ডা থাকলে ঘুমানোর আগে গলার কাছে পাতলা চাদর দিয়ে রাখা ভালো।",
     "If bedroom is excessively cold, covering near throat with a thin sheet before sleeping is good."),
    ("সকালে উঠে মৃদু হালকা ফিজিক্যাল স্ট্রেচিং সুস্থ জীবনযাপনের একটি গুরুত্বপূর্ণ অংশ।",
     "Waking up in morning and doing mild light physical stretching is an important part of healthy living."),
    ("যেকোনো হঠাৎ আঘাত বা দুর্ঘটনার পর ঘাড় শক্ত হয়ে গেলে তাৎক্ষণিক এক্স-রে করানো দরকার।",
     "If neck becomes stiff after any sudden injury or accident, immediate X-ray needs to be done.")
]

p9_nr = [
    ("পায়ের নখে চুলকানি ও ইনফেকশন হলে অ্যান্টিফাঙ্গাল ক্রিম দিনে দুবার মেখে রাখতে হবে।",
     "If itching and infection occur on foot nails, apply antifungal cream twice daily."),
    ("চোখে রোদ লাগলে চোখ লাল হওয়া প্রতিরোধে বাইরে যাওয়ার সময় সানগ্লাস ব্যবহার করা ভালো।",
     "To prevent red eyes when exposed to sunlight, wearing sunglasses when going outdoors is good."),
    ("দাঁতের মাড়ি দিয়ে রক্ত পড়ার সমস্যায় ভিটামিন সি সমৃদ্ধ পেয়ারা ও লেবু খাওয়া উচিত।",
     "For gum bleeding problems, eating guava and lemon rich in vitamin C is advised."),
    ("কানের ভেতরের পর্দা ফুটো হলে পানিতে সাঁতার কাটা বা কানে পানি দেওয়া সম্পূর্ণ বন্ধ করতে হবে।",
     "If inner ear drum is perforated, swimming in water or getting water into ears must be stopped completely."),
    ("হাতে অ্যাকজিমা বা চর্মরোগ হলে খারের সাবান ব্যবহার না করে ভেসলিন মাখা উচিত।",
     "If eczema or skin disease occurs on hands, apply vaseline instead of using alkaline soap."),
    ("পেটে আলসারের ব্যথায় অতিরিক্ত মশলা ও ভাজা খাবার খাওয়া একদম বাদ দিতে হবে।",
     "For stomach ulcer pain, eating excess spices and fried food must be dropped completely."),
    ("হাঁটুর ক্ষয়রোধ করার জন্য নিয়মিত দুধ ও ক্যালসিয়াম ট্যাবলেট খাওয়া উপকারী।",
     "Eating milk and calcium tablets regularly is beneficial to prevent knee degeneration."),
    ("গলার খুসখুসে কাশির জন্য গরম পানিতে মধু ও লবঙ্গ মিশিয়ে পান করলে ভালো আরাম পাওয়া যায়।",
     "For throat tickling cough, drinking warm water mixed with honey and cloves yields good relief."),
    ("ত্বকের রোদে পোড়া ছোপ দাগ দূর করতে রাতে অ্যালোভেরা জেল ব্যবহার করা দরকার।",
     "To remove sunburn patchy spots on skin, using aloe vera gel at night is necessary."),
    ("কোষ্ঠকাঠিন্যের সমস্যায় ইসবগুলের ভুসি পানিতে ভিজিয়ে দ্রুত পান করা দরকার।",
     "For constipation problems, soaking isabgol husk in water and drinking quickly is necessary."),
    ("চুলের রুক্ষতা কমানোর জন্য নারকেল তেলের সাথে মেথি গুঁড়ো মিশিয়ে মাথায় মাখুন।",
     "To reduce hair dryness, mix fenugreek powder with coconut oil and apply on scalp."),
    ("গোড়ালি ফাটা রোধ করতে ভেসলিন ও গ্লিসারিন পা ধুয়ে মেখে রাখা অত্যন্ত কার্যকর।",
     "To prevent cracked heels, washing feet and applying vaseline and glycerin is highly effective."),
    ("হাই প্রেশারের রোগীদের দৈনিক খাবারে কাঁচা লবণ খাওয়ার অভ্যাস বর্জন করা দরকার।",
     "High pressure patients need to abandon habit of eating raw salt in daily meals."),
    ("কিডনিতে পাথর হওয়া এড়াতে প্রতিদিন অন্তত ৩ লিটার পরিষ্কার পানি পান করা প্রয়োজন।",
     "To avoid kidney stones, drinking at least 3 liters of clean water daily is necessary.")
]

add_block("ঘাড় শক্ত", "Stiff neck",
          "ঘাড়ের ডান পাশে শক্ত হয়ে গেছে , ঘোরাতে পারছি না ভালোভাবে , এখন কি করা উচিত আমার ?",
          "The right side of my neck is stiff, I can't move it properly, what should I do now?",
          p9_hr, p9_pr, p9_nr)

# ---------------------------------------------------------
# Prompt 10
# Genre: হাতপা অবশ | Paralysis
# Prompt: হাতপা অবশ হয়ে আসে মাঝেমাঝে , বিশেষ করে রাতে , এখন কি করা উচিত আমার ? | My hands and feet go numb sometimes, especially at night. What should I do now?
# HR: 14, PR: 18, NR: 14
# ---------------------------------------------------------
p10_hr = [
    ("মাঝেমাঝে হাত-পা অবশ হওয়া স্নায়ুর সমস্যা , ডায়াবেটিস বা রক্ত সঞ্চালনের ব্যাঘাতের ইঙ্গিত হতে পারে , তাই দ্রুত একজন চিকিৎসকের পরামর্শ নিন।",
     "Hands-feet going numb sometimes can indicate nerve problems, diabetes or blood circulation disruption, so consult a doctor quickly."),
    ("ঘুমানোর ভঙ্গি পরীক্ষা করুন যাতে হাতের ওপর চাপ পড়ে রক্ত চলাচল বন্ধ না হয় এবং রাতে সোজা হয়ে ঘুমানোর চেষ্টা করুন।",
     "Check sleeping posture so that pressure on hands does not stop blood circulation and try to sleep straight at night."),
    ("রক্তে শর্করার মাত্রা (ডায়াবেটিস) এবং ভিটামিন বি১২ এর পরিমাণ পরীক্ষা করান এবং ডাক্তারের পরামর্শে নিউরোপ্যাথির ওষুধ বা ভিটামিন সাপ্লিমেন্ট সেবন করুন।",
     "Test blood sugar level (diabetes) and vitamin B12 amount and take neuropathy medicine or vitamin supplements on doctor's advice."),
    ("রাতে ঘুমানোর আগে হাত-পা হালকা গরম তেল বা লোশন দিয়ে মৃদু ম্যাসাজ করলে রক্ত সঞ্চালন বাড়ে এবং অবশভাব কমে।",
     "Lightly massaging hands-feet with warm oil or lotion before sleeping at night increases blood circulation and reduces numbness."),
    ("যদি অবশ হওয়ার সাথে হাত-পায়ে তীব্র দুর্বলতা , মুখ বেঁকে যাওয়া বা কথা জড়িয়ে যাওয়ার লক্ষণ থাকে , তবে তাৎক্ষণিক স্ট্রোকের জরুরি চিকিৎসা নিন।",
     "If numbness is accompanied by severe weakness in limbs, facial drooping or slurred speech, take immediate emergency stroke treatment."),
    ("ঘুমানোর সময় খুব টাইট জামাকাপড় , হাতঘড়ি বা হাতের গহনা খুলে রাখুন যাতে স্নায়ু ও রক্তনালীতে চাপ না পড়ে।",
     "Remove very tight clothes, wristwatches or hand jewelry at bedtime so that pressure is not put on nerves and blood vessels."),
    ("হাত ও পায়ের আঙুলগুলোর জন্য শোবার আগে হালকা স্ট্রেচিং ব্যায়াম করার অভ্যাস গড়ে তুলুন।",
     "Form a habit of doing light stretching exercises for fingers and toes before bed."),
    ("মেরুদণ্ডের বা ঘাড়ের নার্ভের সমস্যার কারণে এমন হচ্ছে কিনা তা জানতে মেরুদণ্ডের এমআরআই বা এক্স-রে করান।",
     "Undergo a spine MRI or X-ray to find out if it is happening due to spinal or neck nerve problems."),
    ("উচ্চ রক্তচাপ বা কোলেস্টেরল থাকলে তা নিয়ন্ত্রণে আনুন কারণ রক্তনালী সরু হয়ে হাত-পায়ে রক্ত প্রবাহ কমে যেতে পারে।",
     "Control high blood pressure or cholesterol if present because narrowed blood vessels can decrease blood flow to limbs."),
    ("ধূমপানের অভ্যাস থাকলে তা রক্তনালী সংকুচিত করে স্নায়ুর ক্ষতি করে , তাই ধূমপান সম্পূর্ণ বর্জন করুন।",
     "If you have a smoking habit, it constricts blood vessels damaging nerves, so completely quit smoking."),
    ("রাতে ঘুমানোর সময় হাত-পা অতিরিক্ত ঠান্ডা হয়ে গেলে হাতমোজা বা পামোজা ব্যবহার করে শরীর গরম রাখুন।",
     "If hands-feet get excessively cold while sleeping at night, keep body warm using hand gloves or socks."),
    ("কার্পাল টানেল সিনড্রোমের সমস্যা থাকলে রাতে কব্জি সোজা রাখতে রিস্ট স্প্লিন্ট বা ব্রেস ব্যবহার করা যেতে পারে।",
     "If carpal tunnel syndrome is present, wrist splint or brace can be used to keep wrist straight at night."),
    ("সারাদিন দীর্ঘক্ষণ এক ভঙ্গিতে বসে কাজ করা বন্ধ রেখে মাঝে মাঝে হাত-পা নড়াচড়া ও হাঁটাহাঁটি করুন।",
     "Stop sitting and working in one posture continuously all day and move limbs and walk occasionally."),
    ("প্রতিদিন সকালে অন্তত ৩০ মিনিট হালকা হাঁটার অভ্যাস গড়ে তুলুন যা সারাদেহে রক্ত প্রবাহ ভালো রাখতে সাহায্য করে।",
     "Develop a habit of light walking for at least 30 minutes every morning which helps keep blood flow good throughout the body.")
]

p10_pr = [
    ("রাতে হাতের ওপর মাথা রেখে ঘুমালে সাময়িকভাবে হাতের নার্ভে চাপ পড়ে হাত অসাড় বা অবশ হয়ে যায়।",
     "Sleeping with head placed on hand at night temporarily puts pressure on hand nerve making hand numb."),
    ("অনিয়ন্ত্রিত ডায়াবেটিসের কারণে ডায়াবেটিক নিউরোপ্যাথি হয়ে হাত-পায় চাবানো ও অবশ ভাব হওয়া খুবই সাধারণ।",
     "Diabetic neuropathy due to uncontrolled diabetes causing tingling and numbness in limbs is very common."),
    ("ভিটামিনের অভাবে বিশেষ করে ভিটামিন বি কমপ্লেক্সের ঘাটতি হলে শরীরে নার্ভের কার্যক্ষমতা কমে যেতে পারে।",
     "Lack of vitamins especially vitamin B complex deficiency can reduce nerve functional capacity in body."),
    ("মেরুদণ্ডের ডিক্স সরে গেলে বা নার্ভ রুট চেপে গেলে পায়ে নামার রাস্তায় অবশ অনুভব হতে পারে।",
     "If spinal disc slips or nerve root gets compressed, numbness can be felt along the leg path."),
    ("অনেকে রাতে হাত ঝাকি দিলে বা হাত নাড়ালে সাময়িক অবশভাব কমে যায় বলে অভিজ্ঞতা জানান।",
     "Many people share experience that shaking hands or moving hands at night reduces temporary numbness."),
    ("অতিরিক্ত ঠান্ডা আবহাওয়ায় হাত ও পায়ের রক্তনালী সংকুচিত হয়ে আঙুল অবশ লাগে।",
     "In excessively cold weather, blood vessels of hands and feet constrict making fingers feel numb."),
    ("কম্পিউটারে কিবোর্ড ও মাউস একটানা টাইপ করার কাজ করলে কব্জির স্নায়ুতে চাপ পড়ে কার্পাল টানেল হতে পারে।",
     "Working on computer keyboard and mouse continuous typing puts pressure on wrist nerves causing carpal tunnel."),
    ("শারীরিক দুর্বলতা ও রক্তস্বল্পতা থাকলেও হাত-পা ভারী ও অবশ লাগার অনুভূতি হতে দেখা যায়।",
     "Even with physical weakness and anemia, feeling hands-feet heavy and numb can be seen."),
    ("শারীরিক যে কোনো জটিলতার জন্য চিকিৎসকের পরামর্শ মেনে সঠিক পরীক্ষা করানো বুদ্ধিমানের কাজ।",
     "Following doctor's advice and doing proper tests for any physical complication is a wise work."),
    ("বয়স বাড়ার সাথে সাথে মানুষের নার্ভের দুর্বলতা বেড়ে হাত-পা অবশ হওয়ার ঝুকি বাড়ে।",
     "With increasing age, human nerve weakness increases elevating risk of limb numbness."),
    ("দৈনন্দিন খাদ্যতালিকায় সবুজ শাকসবজি ও ফলমূল রাখলে নার্ভের স্বাস্থ্য ভালো থাকে।",
     "Keeping green vegetables and fruits in daily diet keeps nerve health good."),
    ("অফিসে দীর্ঘক্ষণ চেয়ারে বসে কাজ করার সময় পা ঝুলিয়ে রাখা নার্ভ ও রক্ত প্রবাহের জন্য ক্ষতিকর।",
     "Dangling feet while sitting in office chair for long hours working is harmful for nerve and blood flow."),
    ("পর্যাপ্ত পানি পান না করলে পেশীতে ক্র্যাম্প বা অবশ ভাব দেখা দেওয়ার সম্ভাবনা বাড়ে।",
     "Not drinking adequate water increases chance of muscle cramps or numbness appearing."),
    ("হাত-পায়ে ঝিনঝিন করা এবং অবশ হওয়া স্নায়ুতন্ত্রের অসঙ্গতির একটি সুস্পষ্ট প্রাথমিক উপসর্গ।",
     "Tingling and numbness in limbs is a clear early symptom of nervous system abnormality."),
    ("মানসিক উৎকণ্ঠা ও উদ্বেগের কারণেও হঠাৎ করে হাত-পায়ের তালু অসাড় মনে হতে পারে।",
     "Mental anxiety and worries can also cause sudden numb feeling in palms and soles."),
    ("নিয়মিত হালকা ম্যাসাজ শারীরিক রক্ত সঞ্চালন সচল রাখতে সাহায্য করতে পারে।",
     "Regular light massage can help keep physical blood circulation active."),
    ("গর্ভবতী নারীদের শেষ তিনমাসে পানি জমে হাত-পা ফোলা ও অবশ হওয়ার সমস্যা হতে দেখা যায়।",
     "In pregnant women in last trimester, water retention causes limb swelling and numbness problems."),
    ("শোবার পরিবেশ আরামদায়ক রাখা এবং শরীরের সঠিক পজিশন ঘুম ভালো হতে সাহায্য করে।",
     "Keeping sleeping environment comfortable and correct body position helps sleep be good.")
]

p10_nr = [
    ("চোখে ছানি পড়লে অপারেশনের মাধ্যমে লেন্স বসিয়ে দৃষ্টি সম্পূর্ণ ঠিক করা সম্ভব।",
     "If cataracts form in eyes, vision can be completely corrected by placing a lens through surgery."),
    ("দাঁতের ক্ষয়ে তীব্র ব্যথা হলে ডেন্টিস্টের পরামর্শে রুট ক্যানেল ফিলিং করানো ভালো।",
     "If severe pain occurs in tooth decay, getting root canal filling on dentist's advice is good."),
    ("ত্বকে ব্রণের সমস্যা দূর করতে রাতে ভালো ফেসওয়াশ দিয়ে মুখ ধুয়ে পরিষ্কার রাখা জরুরি।",
     "To remove skin acne problems, keeping face clean by washing with a good facewash at night is essential."),
    ("গলার টনসিল ইনফেকশন হলে গরম পানিতে লবণ দিয়ে রোজ কয়েকবার কুলকুচি করতে হয়।",
     "If throat tonsil infection occurs, gargle with warm salt water several times daily."),
    ("পেটে গ্যাস ও বদহজম কমাতে তেল-মশলাযুক্ত ভাজা খাবার খাওয়া ছেড়ে দেওয়া উচিত।",
     "To reduce stomach gas and indigestion, quitting eating oily-spicy fried food is recommended."),
    ("কানের ভেতরের ময়লা পরিষ্কার করতে কটন বাড ব্যবহার করা কান ও পর্দার জন্য ক্ষতিকর।",
     "Using cotton buds to clean dirt inside ears is harmful for ears and eardrum."),
    ("কোষ্ঠকাঠিন্যের উপশমে রাতে ঘুমানোর আগে ইসবগুলের ভুসি ইসবগুলের শরবত খাওয়া উপকারী।",
     "For constipation relief, eating isabgol husk or isabgol drink before bed at night is beneficial."),
    ("হাঁটুর লিগামেন্ট ক্ষতিগ্রস্ত হলে চিকিৎসকের দেওয়া নি-ক্যাপ ব্যবহার করে হাঁটা উচিত।",
     "If knee ligament is damaged, walk using knee-cap prescribed by doctor."),
    ("চুলের খুশকি দূর করতে লেবুর রস ও টক দই স্ক্যাল্পে মেখে ২০ মিনিট পর ধুয়ে ফেলুন।",
     "To remove hair dandruff, apply lemon juice and sour yogurt on scalp and wash off after 20 minutes."),
    ("গোড়ালি ফাটা বন্ধ করতে রাতে ভেসলিন মেখে সুতির মোজা পরে ঘুমাতে যাওয়া ভালো।",
     "To stop cracked heels, applying vaseline and wearing cotton socks before sleeping at night is good."),
    ("হাই প্রেশার নিয়ন্ত্রণে রাখতে কাঁচা লবণ এবং চর্বিযুক্ত মাংশ খাওয়া বন্ধ করা দরকার।",
     "To keep high pressure controlled, stopping eating raw salt and fatty meat is necessary."),
    ("গ্যাস্ট্রিকের আলসারে বমির ভাব হলে হালকা গরম পানিতে আদার রস মিশিয়ে খান।",
     "If vomiting feeling occurs in gastric ulcer, drink ginger juice mixed in warm water."),
    ("ত্বকের মেছতার দাগ কমাতে দিনের বেলা বের হওয়ার আগে সানস্ক্রিন লোশন ব্যবহার করুন।",
     "To reduce skin melasma spots, use sunscreen lotion before going out during daytime."),
    ("কাশি ও কফ কমানোর জন্য বাসক পাতার রস ও মধু মিশিয়ে সেবন করা একটি প্রাচীন উপায়।",
     "Drinking vasaka leaf juice mixed with honey is an ancient remedy to reduce cough and phlegm.")
]

add_block("হাতপা অবশ", "Paralysis",
          "হাতপা অবশ হয়ে আসে মাঝেমাঝে , বিশেষ করে রাতে , এখন কি করা উচিত আমার ?",
          "My hands and feet go numb sometimes, especially at night. What should I do now?",
          p10_hr, p10_pr, p10_nr)

print("Processed prompts 9 and 10.")

# ---------------------------------------------------------
# Prompt 11
# Genre: শরীর কাঁপুনি | Body shaking
# Prompt: শরীর হঠাৎ ঠান্ডা হয়ে যায় , আর কাঁপুনি দেয় , এখন কি করা উচিত আমার ? | My body suddenly becomes cold and shivers, what should I do now?
# HR: 12, PR: 16, NR: 12
# ---------------------------------------------------------
p11_hr = [
    ("শরীর হঠাৎ ঠান্ডা হয়ে কাঁপুনি দিলে গরম চাদর বা কম্বল দিয়ে শরীর ঢেকে রাখুন , হালকা গরম পানি বা সুপ পান করুন এবং ঘরের ফ্যান বন্ধ রাখুন।",
     "If body suddenly gets cold and shivers, cover body with a warm sheet or blanket, drink warm water or soup and turn off room fan."),
    ("এটি শরীরে তীব্র জ্বর (যেমন ডেঙ্গু বা গলার ইনফেকশন) , ইনফেকশন বা রক্তে শর্করার মাত্রা কমে যাওয়ার (হাইপোগ্লাইসেমিয়া) লক্ষণ হতে পারে , তাই থার্মোমিটার দিয়ে তাপমাত্রা মেপে দেখুন।",
     "This can be a sign of high fever (like dengue or throat infection), infection or drop in blood sugar (hypoglycemia), so measure temperature with a thermometer."),
    ("যদি ব্লাড সুগার কমে যায় , তবে অবিলম্বে এক গ্লাস চিনি বা গ্লুকোজের পানি পান করুন যা শরীরের তাপমাত্রা ও এনার্জি স্বাভাবিক করতে সাহায্য করবে।",
     "If blood sugar drops, drink a glass of sugar or glucose water immediately which will help normalize body temperature and energy."),
    ("হঠাৎ কাঁপুনি সহ তীব্র জ্বর উঠলে ডাক্তার দেখিয়ে প্যারাসিটামল সেবন করুন , তবে ডাক্তারের পরামর্শ ছাড়া থার্মোমিটার না দেখে অপ্রয়োজনীয় অ্যান্টিবায়োটিক খাবেন না।",
     "If high fever arises with sudden shivering, consult doctor and take paracetamol, but do not eat unnecessary antibiotics without thermometer reading on doctor's advice."),
    ("যদি কাঁপুনির সাথে তীব্র বুকে ব্যথা , শ্বাসকষ্ট বা চেতনা হারানোর মতো অবস্থা হয় , তবে অবহেলা না করে দ্রুত হাসপাতালের জরুরি বিভাগে যান।",
     "If shivering is accompanied by severe chest pain, shortness of breath or loss of consciousness, go to hospital emergency department quickly without neglect."),
    ("শরীরে থাইরয়েডের সমস্যা বা হরমোনের তারতম্যের কারণে অতিরিক্ত ঠান্ডা লাগা ও কাঁপুনি হতে পারে , তাই থাইরয়েড টেস্ট করান।",
     "Severe cold feelings and shivering can happen due to thyroid problems or hormonal variations in body, so get thyroid tested."),
    ("মানসিক অতিরিক্ত আতঙ্ক বা তীব্র প্যানিক অ্যাটাকের ফলেও শরীর হঠাৎ ঠান্ডা হয়ে কাঁপুনি দিতে পারে , তাই শান্ত হয়ে বসার চেষ্টা করুন।",
     "Body can also suddenly get cold and shiver due to extreme mental panic or intense panic attack, so try to sit down calmly."),
    ("ভেজা জামাকাপড় পরা থাকলে তা দ্রুত বদলে শুকনো আরামদায়ক গরম পোশাক পরে নিন।",
     "If wearing wet clothes, change them quickly and wear dry comfortable warm clothing."),
    ("রক্তচাপ হঠাৎ কমে গেলে (লো প্রেসার) শরীর ঠান্ডা ও কাঁপুনি হতে পারে , তাই ডাবের পানি বা খাওয়ার স্যালাইন পান করে বিশ্রাম নিন।",
     "If blood pressure suddenly drops (low pressure), body can become cold and shiver, so drink coconut water or ORS and rest."),
    ("শরীরে পানির মারাত্মক ঘাটতি বা ডিহাইড্রেশন থাকলেও তাপমাত্রা নিয়ন্ত্রণে ব্যাঘাত ঘটে , তাই পর্যাপ্ত তরল খাবার গ্রহণ করুন।",
     "Severe water deficiency or dehydration in body disrupts temperature control, so consume adequate liquid foods."),
    ("বারবার এমন শরীর ঠান্ডা হয়ে কাঁপুনি দেওয়ার ঘটনা ঘটলে রক্তের সম্পূর্ণ গণনা (CBC) ও ইউরিন টেস্ট করানো আবশ্যক।",
     "If such events of body getting cold and shivering recur, full blood count (CBC) and urine test are mandatory."),
    ("অ্যালকোহল সেবন করা থেকে বিরত থাকুন এবং রাতে পর্যাপ্ত ঘুম ও পুষ্টিকর সুষম খাবার খেয়ে শরীর চাঙ্গা রাখুন।",
     "Refrain from consuming alcohol and keep body energized by getting adequate sleep at night and eating nutritious balanced food.")
]

p11_pr = [
    ("হঠাৎ করে জ্বর আসার আগে অনেক সময় শরীর ঠান্ডা হয়ে প্রচণ্ড কাঁপুনি দিয়ে শিহরণ জাগে।",
     "Before fever comes suddenly, body often gets cold and experiences severe shivering chills."),
    ("আমার দাদুর একবার প্রস্রাবের ইনফেকশনের কারণে রাতে শরীর ঠান্ডা হয়ে খুব কাঁপুনি দিয়েছিল।",
     "My grandfather once had severe shivering with cold body at night due to urine infection."),
    ("ঠান্ডা বাতাসে বেশিক্ষণ কাজ করলে বা বৃষ্টিতে ভিজলে শরীর হঠাৎ ঠান্ডা হয়ে কাঁপুনি উঠতে পারে।",
     "Working in cold air for too long or getting wet in rain can cause body to suddenly become cold and shiver."),
    ("শরীরে রক্তের অভাব বা এনিমিয়া থাকলে শীত শীত লাগা এবং হাত-পা ঠান্ডা হয়ে কাঁপুনি হওয়া সাধারণ।",
     "If there is lack of blood or anemia in body, feeling chilly and cold extremities with shivering is common."),
    ("প্যানিক অ্যাটাক হলে হাত-পা ঠান্ডা হয়ে কাঁপুনি ওঠা একটি বহুল পরিচিত মানসিক শারীরিক উপসর্গ।",
     "Hands-feet getting cold and shivering during panic attack is a widely known mental-physical symptom."),
    ("হঠাৎ ভয় পেলে বা কোনো দুঃসংবাদ শুনলে মানুষের শরীর ঠান্ডা হয়ে রক্তচাপ কমে যেতে পারে।",
     "Getting suddenly scared or hearing bad news can cause human body to get cold and blood pressure to drop."),
    ("ম্যালেরিয়া বা টাইফয়েড রোগের প্রধান লক্ষণ হলো কাপুনি দিয়ে তীব্র জ্বর আসা।",
     "The main symptom of malaria or typhoid disease is high fever with shivering."),
    ("শরীর ঠান্ডা হলে এক কাপ গরম চা বা কফি পান করা সাময়িক স্বস্তি দিতে বেশ সাহায্য করে।",
     "Drinking a cup of warm tea or coffee when body gets cold helps quite a bit in giving temporary relief."),
    ("শীতকালে বয়স্ক মানুষদের শরীর দ্রুত ঠান্ডা হয়ে যাওয়ার ঝুঁকি বেশি থাকে বলে যত্ন নেওয়া দরকার।",
     "Elderly people run higher risk of body getting cold quickly in winter so care needs to be taken."),
    ("খালি পেটে অনেকক্ষণ কাজ করার পর সুগার কমে গেলেও শরীর ঠান্ডা ও দুর্বল অনুভূত হতে পারে।",
     "After working on empty stomach for long, sugar drop can also make body feel cold and weak."),
    ("শরীর অস্বাভাবিক ঠান্ডা হয়ে গেলে উষ্ণ ঘরে কিছুক্ষণ বিশ্রাম নেওয়া উচিত।",
     "If body gets abnormally cold, resting in a warm room for some time is advised."),
    ("যেকোনো সংক্রামক ব্যাধির শুরুর দিকে কাঁপুনি দেওয়া একটি স্বাভাবিক প্রতিরোধমূলক শারীরিক সাড়া।",
     "Shivering at the onset of any infectious disease is a normal protective physical response."),
    ("প্রতিদিন সকালে ইষদুষ্ণ পানিতে গোসল করা শরীরের রক্ত চলাচল স্বাভাবিক রাখতে সহায়তা করে।",
     "Showering in lukewarm water every morning helps keep body blood circulation normal."),
    ("শরীর খারাপ লাগলে সবসময় থার্মোমিটার দিয়ে তাপমাত্রা মেপে নিশ্চিত হওয়া স্বাস্থ্য সচেতনতার লক্ষণ।",
     "Measuring temperature with a thermometer when feeling unwell to confirm is a sign of health awareness."),
    ("ডায়াবেটিক রোগীদের সাথে সবসময় মিষ্টি বা চকলেট রাখা উচিত সুগার কমে যাওয়ার ঝুঁকি এড়াতে।",
     "Diabetic patients should always keep sweets or chocolates with them to avoid risk of sugar drop."),
    ("অতিরিক্ত এসির ঠান্ডায় ঘুমালে সকালে উঠে হঠাৎ গায়ে কাঁপুনি দেওয়ার অনুভূতি হতে পারে।",
     "Sleeping in excessive AC cold can cause feeling of sudden body shivering upon waking up in morning.")
]

p11_nr = [
    ("চোখের কোণে ছানি পড়লে অপারেশনের মাধ্যমে লেন্স প্রতিস্থাপন করানো সবচেয়ে নিরাপদ উপায়।",
     "If cataract forms in eye corner, replacing lens through surgery is the safest way."),
    ("দাঁতের মাড়িতে ইনফেকশন হলে চিকিৎসকের পরামর্শে অ্যান্টিবায়োটিক মাউথওয়াশ ব্যবহার করুন।",
     "If infection occurs in teeth gums, use antibiotic mouthwash on doctor's advice."),
    ("মাথার চুল পড়ার সমস্যা কমাতে পেঁয়াজের রস ও নারকেল তেল মেখে আধঘণ্টা পর ধুয়ে ফেলুন।",
     "To reduce head hair falling problems, apply onion juice and coconut oil and wash after half an hour."),
    ("কানের ভেতরের ময়লা পরিষ্কারের জন্য শক্ত বাড বা কাঠি ব্যবহার করা বিপজ্জনক।",
     "Using hard buds or sticks to clean dirt inside ears is dangerous."),
    ("পেটে অতিরিক্ত গ্যাস্ট্রিকের সমস্যা কমানোর জন্য তৈলাক্ত খাবার খাওয়া সম্পূর্ণ বন্ধ রাখা দরকার।",
     "To reduce excessive gastric problems in stomach, stopping eating oily food completely is necessary."),
    ("গোড়ালি ফাটা রোধ করতে প্রতিদিন রাতে ধুয়ে ভেসলিন মেখে রাখা দরকার।",
     "To prevent cracked heels, washing and applying vaseline every night is necessary."),
    ("পিঠের মেরুদণ্ডের ব্যথার জন্য সোজা হয়ে ঘুমানো এবং শক্ত তোশক ব্যবহার করা উচিত।",
     "For spinal back pain, sleeping straight and using firm mattress is advised."),
    ("ত্বকে মেছতার ছাপ কমাতে দিনের বেলা বাইরে বের হওয়ার সময় সানস্ক্রিন লোশন ব্যবহার করুন।",
     "To reduce melasma spots on skin, use sunscreen lotion when going outdoors during daytime."),
    ("কোষ্ঠকাঠিন্যের সমস্যা এড়াতে খাদ্যতালিকায় সবুজ শাকসবজি ও ফলমূল বেশি রাখা উচিত।",
     "To avoid constipation problems, keeping more green vegetables and fruits in diet is advised."),
    ("হাঁটুর লিগামেন্টে ব্যাথা হলে চিকিৎসকের পরামর্শে নি-ক্যাপ পরে চলাফেরা করা ভালো।",
     "If knee ligament hurts, walking wearing knee-cap on doctor's advice is good."),
    ("গলার খুসখুসে কাশিতে গরম পানিতে মধু ও লবঙ্গ ফোটানো চা খেলে আরাম লাগে।",
     "In throat tickling cough, drinking tea boiled with honey and cloves in warm water feels comfortable."),
    ("ত্বকের রোদে পোড়া কালো দাগ দূর করতে অ্যালোভেরা জেল হালকা হাতে মেখে রাখুন।",
     "To remove sunburn dark spots on skin, gently apply aloe vera gel.")
]

add_block("শরীর কাঁপুনি", "Body shaking",
          "শরীর হঠাৎ ঠান্ডা হয়ে যায় , আর কাঁপুনি দেয় , এখন কি করা উচিত আমার ?",
          "My body suddenly becomes cold and shivers, what should I do now?",
          p11_hr, p11_pr, p11_nr)

# ---------------------------------------------------------
# Prompt 12
# Genre: অতিরিক্ত চা পান | Drink extra tea
# Prompt: আমি দিনে ৫৬ কাপ চা খাই এতে কি কোনো ক্ষতি হয় ? | I drink 56 cups of tea a day, is there any harm in it?
# HR: 12, PR: 12, NR: 12
# ---------------------------------------------------------
p12_hr = [
    ("দিনে ৫-৬ কাপ বা অতিরিক্ত চা খাওয়া স্বাস্থ্যের জন্য বেশ ক্ষতিকর , কারণ এতে থাকা ক্যাফেইন অতিরিক্ত হলে অনিদ্রা , মানসিক অস্থিরতা এবং বুক ধড়ফড় করার কারণ হতে পারে।",
     "Drinking 5-6 cups or extra tea daily is quite harmful to health , because excessive caffeine in it can cause insomnia, mental restlessness and chest palpitations."),
    ("অতিরিক্ত চা পানের ফলে পাকস্থলীতে অতিরিক্ত অ্যাসিড তৈরি হয় , যা গ্যাস্ট্রিক , পেটে জ্বালাপোড়া এবং কোষ্ঠকাঠিন্যের সমস্যা বহুগুণ বাড়িয়ে দেয়।",
     "Excessive tea drinking generates excess acid in stomach , which increases gastric, heartburn and constipation problems many times."),
    ("চায়ে থাকা ট্যানিন খাদ্য থেকে আয়রন শোষণে বাধা দেয় , যার ফলে রক্তস্বল্পতা বা এনিমিয়ার ঝুঁকি অনেক বৃদ্ধি পায়।",
     "Tannin present in tea hinders iron absorption from food , resulting in greatly increased risk of anemia."),
    ("প্রতিদিন চায়ের পরিমাণ কমিয়ে সর্বোচ্চ ১ থেকে ২ কাপে নিয়ে আসুন , এবং মূল খাবারের ঠিক পরপরই চা পান করার অভ্যাস বাদ দিন।",
     "Reduce daily tea quantity to a maximum of 1 to 2 cups , and quit the habit of drinking tea right after main meals."),
    ("চায়ের সাথে অতিরিক্ত চিনি খেলে স্থূলতা , ডায়াবেটিস এবং দাঁতের এনামেল ক্ষয়ের ঝুঁকি তৈরি হয় , তাই চিনি ছাড়া লিকার চা খাওয়ার চেষ্টা করুন।",
     "Eating extra sugar with tea creates risks of obesity, diabetes and tooth enamel erosion , so try drinking liquor tea without sugar."),
    ("অতিরিক্ত ক্যাফেইন আসক্তির সৃষ্টি করে , তাই হুট করে চা না পেলে তীব্র মাথাব্যথা , মেজাজ খিটখিটে হওয়া এবং ক্লান্তি অনুভব হতে পারে।",
     "Excessive caffeine creates addiction , so not getting tea suddenly can cause severe headache, irritable mood and fatigue."),
    ("চা একটি প্রস্বাববর্ধক (ডায়ুরেটিক) পানীয় হওয়ায় অতিরিক্ত চা পান করলে শরীর থেকে দ্রুত পানি বের হয়ে গিয়ে পানিশূন্যতা বা ডিহাইড্রেশন হতে পারে।",
     "Since tea is a diuretic drink, drinking excess tea causes rapid water loss from body leading to dehydration."),
    ("সন্ধ্যা বা রাতের বেলা চা পান করা সম্পূর্ণ বন্ধ করুন যাতে আপনার রাতের স্বাভাবিক ঘুম ব্যাহত না হয়।",
     "Completely stop drinking tea in evening or night time so that your normal night sleep is not disrupted."),
    ("চায়ের পরিবর্তে ডাবের পানি , লেবুর শরবত বা গ্রিন টি খাওয়ার অভ্যাস গড়ে তুলুন যা শরীরের রোগ প্রতিরোধ ক্ষমতা বাড়াতে বেশি সহায় হতে পারে।",
     "Form a habit of drinking coconut water, lemon juice or green tea instead of tea which can be more helpful in boosting body immunity."),
    ("অতিরিক্ত দুধ-চা পান করলে হজমক্ষমতা কমে যায় এবং পেট ফোলা বা গ্যাসের সমস্যা তীব্র রূপ ধারণ করে।",
     "Drinking excessive milk-tea reduces digestion capacity and severe bloating or gas problems take form."),
    ("হৃৎপিণ্ডের রোগীদের জন্য অতিরিক্ত চা পানের ক্যাফেইন রক্তচাপ বাড়িয়ে ঝুঁকিপূর্ণ পরিস্থিতি তৈরি করতে পারে।",
     "For heart patients, caffeine from excessive tea drinking can raise blood pressure creating risky situations."),
    ("গর্ভাবস্থায় অতিরিক্ত চা পান করা বাচ্চার ওজন কমা এবং গর্ভপাতের ঝুঁকি বাড়িয়ে দেয় , তাই গর্ভবতী নারীদের দিনে ১ কাপের বেশি চা খাওয়া একদম উচিত নয়।",
     "Drinking excess tea during pregnancy increases risk of low birth weight and miscarriage , so pregnant women should never drink more than 1 cup of tea daily.")
]

p12_pr = [
    ("আমাদের দেশে অনেকেই সারাদিনে কাজের ফাঁকে অনেকবার চা পানের অভ্যাসে অভ্যস্ত।",
     "In our country many people are accustomed to habit of drinking tea many times during work throughout the day."),
    ("আমার এক বড় ভাই দিনে সাত-আট কাপ চা খেতেন এবং পরবর্তীতে তার দীর্ঘমেয়াদী গ্যাসের সমস্যা হয়েছিল।",
     "An elder brother of mine used to drink seven-eight cups of tea daily and subsequently developed long-term gas problems."),
    ("অফিসে কাজের মানসিক চাপ কমানোর জন্য বারবার কাপের পর কাপ চা খাওয়ার প্রবণতা দেখা যায়।",
     "A tendency of drinking cup after cup of tea repeatedly is seen to reduce work stress at office."),
    ("চা পানের অভ্যাস হুট করে একদিনে ছেড়ে দেওয়া খুব কঠিন কিন্তু ধীরে ধীরে কমানো সম্ভব।",
     "Habit of drinking tea is very hard to quit suddenly in one day but reducing gradually is possible."),
    ("লিকার চায়ের তুলনায় দুধ-চা বেশি খেলে পেটের মধ্যে ভার ভার লাগার অনুভূতি হতে পারে।",
     "Drinking milk-tea more compared to liquor tea can cause feeling of heaviness inside stomach."),
    ("অনেকে মনে করেন বিকেলের চা মেজাজ সতেজ রাখতে এবং মাথা ঝিমঝিম ভাব দূর করতে সাহায্য করে।",
     "Many people think afternoon tea helps keep mood fresh and remove head grogginess."),
    ("অতিরিক্ত চা পানের অভ্যাসের ফলে দাঁতের ওপর হলুদ ছোপ ছোপ দাগ পড়ে যেতে দেখা যায়।",
     "As a result of excessive tea drinking habit, yellow patchy spots are seen to form on teeth."),
    ("চা পানের পাশাপাশি পর্যাপ্ত পরিষ্কার পানি পান করার অভ্যাস না থাকলে শরীরে তরলের ঘাটতি দেখা দেয়।",
     "If habit of drinking adequate clean water alongside tea drinking is not present, fluid deficiency appears in body."),
    ("খালি পেটে সকালে উঠে কড়া চা খাওয়া পাকস্থলীর মিউকাস লেয়ারের জন্য ক্ষতিকর হতে পারে।",
     "Waking up in morning and drinking strong tea on empty stomach can be harmful for stomach mucous layer."),
    ("আজকাল লাল চায়ের চেয়ে আদা চা বা তুলসী চা শারীরিক প্রশান্তির জন্য বেশি জনপ্রিয় হচ্ছে।",
     "Nowadays ginger tea or tulsi tea is becoming more popular for physical peace than black tea."),
    ("কাজের বিরতিতে বন্ধুদের সাথে চা আড্ডা আমাদের সংস্কৃতির একটি জনপ্রিয় সামাজিক অনুষঙ্গ।",
     "Tea chats with friends during work breaks is a popular social aspect of our culture."),
    ("যেকোনো খাবার বা পানীয় অতিরিক্ত গ্রহণ করা শারীরিক সুস্থতার জন্য কখনোই ভালো নয়।",
     "Taking any food or drink in excess is never good for physical health.")
]

p12_nr = [
    ("চোখে ছানি পড়লে তা লেজার সার্জারির মাধ্যমে অপসারণ করে দৃষ্টি সচ্ছ করা সহজ।",
     "If cataract forms in eye, removing it through laser surgery to clear vision is easy."),
    ("পায়ের গোড়ালির ব্যথা কমাতে নিয়ম করে বরফ সেক দেওয়া এবং নরম জুতো পরা উচিত।",
     "To reduce heel pain, giving regular ice compress and wearing soft shoes is advised."),
    ("কানের ড্রাম ফুটো হলে কানে পানি ঢুকতে না দেওয়া এবং অ্যান্টিবায়োটিক ব্যবহার করা আবশ্যক।",
     "If ear drum is perforated, not letting water enter ear and using antibiotics is mandatory."),
    ("পিঠের তীব্র মেরুদণ্ডের ব্যথার জন্য সোজা হয়ে ঘুমানোর অভ্যাস গড়ে তোলা দরকার।",
     "For severe spinal back pain, developing habit of sleeping straight is needed."),
    ("ত্বকের রোদে পোড়া দাগ দূর করতে অ্যালোভেরা জেল মুখে মেখে রাতে রাখা কার্যকর।",
     "To remove sunburn spots on skin, applying aloe vera gel on face at night is effective."),
    ("হাঁটুর ক্ষয়রোধ করার জন্য নিয়ম করে ক্যালসিয়াম ট্যাবলেট ও দুধ খাওয়া দরকার।",
     "To prevent knee degeneration, eating calcium tablets and milk regularly is needed."),
    ("গলার খুসখুসে কাশির জন্য গরম পানিতে আদা ও মধু মিশিয়ে চা পান করা উপকারী।",
     "For throat tickling cough, drinking tea mixed with ginger and honey in warm water is beneficial."),
    ("কোষ্ঠকাঠিন্য কমানোর জন্য প্রতিদিন ইসবগুলের ভুসি পানিতে ভিজিয়ে নিয়মিত পান করা স্বাস্থ্যকর।",
     "To reduce constipation, soaking isabgol husk in water and drinking regularly is healthy."),
    ("চুলের রুক্ষতা দূর করার জন্য নারিকেল তেলের সাথে মেথি দানা ফুটিয়ে মাথায় মাখুন।",
     "To remove hair dryness, boil fenugreek seeds with coconut oil and apply on scalp."),
    ("ত্বকে ব্রণের সমস্যা কমানোর জন্য ফেসওয়াশ দিয়ে মুখ ধুয়ে পরিষ্কার রাখা জরুরি।",
     "To reduce skin acne problems, keeping face clean by washing with facewash is essential."),
    ("হাই প্রেশারের রোগীদের দৈনিক কাঁচা লবণ খাওয়ার অভ্যাস বর্জন করা অত্যন্ত প্রয়োজন।",
     "High pressure patients extremely need to abandon habit of eating raw salt daily."),
    ("কিডনিতে পাথর হওয়া এড়াতে প্রতিদিন অন্তত ৩ লিটার পরিষ্কার পানি পান করা দরকার।",
     "To avoid kidney stones, drinking at least 3 liters of clean water daily is needed.")
]

add_block("অতিরিক্ত চা পান", "Drink extra tea",
          "আমি দিনে ৫৬ কাপ চা খাই এতে কি কোনো ক্ষতি হয় ?",
          "I drink 56 cups of tea a day, is there any harm in it?",
          p12_hr, p12_pr, p12_nr)

# Save dataframe to Excel file
df_batch23 = pd.DataFrame(batch23_data)
df_batch23.to_excel("Batch_23_Gemini.xlsx", index=False)
print("Batch_23_Gemini.xlsx successfully generated!")
print(f"Total rows generated: {len(df_batch23)}")
