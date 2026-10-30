# Prompt 8: মূত্রত্যাগের পর বিচিতে ঝিনঝিন করে ওঠে , কি করা উচিৎ / Tingling in the vagina after urination, what should I do?
# HR=14, PR=16, NR=12

g_bn = "স্যাস্থসচেতনা"
g_en = "Health awareness"
p_bn = "মূত্রত্যাগের পর বিচিতে ঝিনঝিন করে ওঠে , কি করা উচিৎ"
p_en = "Tingling in the vagina after urination, what should I do?"

hr = [
    ("মূত্রত্যাগের পর ঝিনঝিন বা অস্বস্তি হলে প্রচুর পানি পান করুন , সুতির অন্তর্বাস পরিধান করুন এবং ইউরিন রুটিন পরীক্ষা করিয়ে ডাক্তার দেখান।", "If tingling or discomfort occurs after urination , drink plenty of water , wear cotton underwear and get a routine urine test done to see a doctor."),
    ("মূত্রনালীর সংক্রমণ বা ইনফেকশনের কারণে এমনটা হতে পারে , তাই একজন গাইনি বিশেষজ্ঞ বা ইউরোলজিস্টের পরামর্শে উপযুক্ত অ্যান্টিবায়োটিক গ্রহণ করুন।", "This can happen due to urinary tract infection or inflammation , so take appropriate antibiotics on advice of a gynecologist or urologist."),
    ("জননাঙ্গের পরিচ্ছন্নতা বজায় রাখুন , সুগন্ধযুক্ত সাবান বা ক্ষতিকর কেমিক্যাল ব্যবহার বন্ধ করুন এবং প্রস্রাব চেপে রাখা থেকে বিরত থাকুন।", "Maintain genital hygiene , stop using scented soaps or harmful chemicals and refrain from holding urine."),
    ("প্রস্রাবের পর হালকা গরম পানি দিয়ে স্থানটি পরিষ্কার করুন এবং তোয়ালে দিয়ে শুকনা রাখুন যাতে ফাঙ্গাল বা ব্যাকটেরিয়ার সংক্রমণ না বাড়ে।", "Clean the area with mild warm water after urination and keep dry with a towel so fungal or bacterial infection does not grow."),
    ("যদি ঝিনঝিন ভাব বা জ্বালাপোড়ার সাথে তলপেটে ব্যথা বা জ্বর আসে , তবে কালক্ষেপণ না করে দ্রুত চিকিৎসকের শরণাপন্ন হওয়া দরকার।", "If tingling or burning is accompanied by lower abdominal pain or fever , consulting a doctor quickly without delay is needed."),
    ("প্রস্রাবে কোনো ইনফেকশন আছে কিনা তা জানতে দ্রুত ইউরিন কালচার অ্যান্ড সংবেদনশীলতা পরীক্ষা করানো উচিত।", "To know if there is any infection in urine , a urine culture and sensitivity test should be done quickly."),
    ("শারীরিক মিলনের পর ভালোভাবে প্রস্রাব ও পরিষ্কার করার অভ্যাস গড়ে তুলুন যাতে মূত্রনালীতে সংক্রমণ ছড়িয়ে পড়তে না পারে।", "Form a habit of urinating and cleaning well after physical intimacy so infection cannot spread in urinary tract."),
    ("ক্র্যানবেরি জুস বা সিট্রাস জাতীয় পানীয় খেলে মূত্রনালীর ব্যাকটেরিয়া দূর হয় এবং মূত্রত্যাগের পর ঝিনঝিনানি কমে আসে।", "Drinking cranberry juice or citrus drinks eliminates urinary tract bacteria and reduces post-urination tingling."),
    ("মূত্রত্যাগের পর ঝিনঝিন প্রতিরোধে তীব্র সুগন্ধিযুক্ত প্যাড বা কেমিক্যাল ভেজা ওয়াইপস ব্যবহার পুরোপুরি বন্ধ রাখতে হবে।", "To prevent tingling after urination , completely stop using heavily scented pads or chemically wet wipes."),
    ("যদি লক্ষণটি কোনো যৌনবাহিত সংক্রমণের কারণে হয় , তবে অনতিবিলম্বে স্ত্রীরোগ বিশেষজ্ঞের অধীনে চিকিৎসা শুরু করা আবশ্যক।", "If symptom is due to any sexually transmitted infection , starting treatment under a gynecologist immediately is mandatory."),
    ("ডিহাইড্রেশন বা ঘন প্রস্রাবের কারণেও ঝিনঝিন হতে পারে , তাই সারাদিনে অন্তত ৩ থেকে ৪ লিটার পরিষ্কার পানি পান করুন।", "Tingling can also happen due to dehydration or concentrated urine , so drink at least 3 to 4 liters of clean water daily."),
    ("জননাঙ্গে চুলকানি বা লালচে ভাব দেখা দিলে অ্যান্টিফাঙ্গাল ক্রিম বা ডাক্তারের নির্দেশিত মলম ব্যবহার করা উপকারী।", "If itching or redness appears on genitals , using antifungal cream or doctor-directed ointment is beneficial."),
    ("টাইট বা সিন্থেটিক অন্তর্বাস পরা বন্ধ করে ঢিলেঢালা সুতি পোশাক পরলে আর্দ্রতা আটকে থাকে না এবং অনুভূতি স্বাভাবিক হয়।", "Stopping wearing tight or synthetic underwear and wearing loose cotton clothes prevents moisture trapping and normalizes sensation."),
    ("প্রস্রাব করার পর সবসময় সামন থেকে পেছনের দিকে পানি দিয়ে ধোয়ার সঠিক নিয়ম মেনে চলা অত্যন্ত জরুরি।", "Following the correct rule of washing with water from front to back always after urinating is extremely urgent.")
]

pr = [
    ("মহিলাদের ক্ষেত্রে ইউরিনারি ট্র্যাক্ট ইনফেকশন বা ইউটিআই অত্যন্ত পরিচিত একটি শারীরিক সমস্যা।", "In case of women , urinary tract infection or UTI is a very common physical problem."),
    ("প্রতিদিন পর্যাপ্ত পরিমাণে পানি পান করা পুরো শরীরের বিষাক্ত পদার্থ বের করে দিতে সাহায্য করে।", "Drinking adequate water daily helps flush out toxic substances from the entire body."),
    ("অপরিচ্ছন্ন শৌচাগার ব্যবহার করলে খুব সহজেই ব্যাকটেরিয়া সংক্রমণ ছড়িয়ে পড়তে পারে।", "Using unhygienic washrooms can very easily spread bacterial infection."),
    ("আমার এক বান্ধবীর তীব্র গরমের দিনে পানি কম খাওয়ার ফলে প্রস্রাবে বেশ জ্বালাপোড়া হয়েছিল।", "A friend of mine had a lot of burning in urine due to drinking less water during intense hot days."),
    ("ব্যক্তিগত স্বাস্থ্যবিধি মেনে চললে অনেক জটিল শারীরিক অসুস্থতা থেকে নিজেকে নিরাপদ রাখা যায়।", "Following personal hygiene keeps oneself safe from many complex physical illnesses."),
    ("গর্ভকালীন সময়ে মায়েদের প্রস্রাবের বিভিন্ন সমস্যা দেখা দেওয়া একটি স্বাভাবিক বিষয়।", "During pregnancy , mothers experiencing various urine issues is a normal matter."),
    ("খাদ্যাভ্যাসে অতিরিক্ত মশলা ও ঝাল কমালে পরিপাকতন্ত্র এবং মূত্রনালী ভালো থাকে।", "Reducing excess spice and chili in food habit keeps digestive system and urinary tract good."),
    ("শরীরে কোনো অস্বস্তি হলে অবহেলা না করে সময়মতো চিকিৎসকের কাছে যাওয়া বুদ্ধিমানের কাজ।", "In case of any discomfort in body , going to a doctor on time without neglecting is a wise thing."),
    ("আমাদের দেশে অনেক নারীই লজ্জা বা সংকোচের কারণে জননাঙ্গের সমস্যা গোপন করে রাখেন।", "In our country , many women keep genital problems secret due to shame or hesitation."),
    ("ঋতুস্রাবের সময় নিয়মিত প্যাড পরিবর্তন করা এবং পরিষ্কার-পরিচ্ছন্ন থাকা অত্যন্ত জরুরি।", "Changing pads regularly during menstruation and staying clean is extremely urgent."),
    ("কিডনি বা মূত্রথলিতে পাথর হলেও প্রস্রাবে নানাবিধ জটিলতা ও কষ্ট দেখা দিতে পারে।", "Even if there are stones in kidney or bladder , various complications and trouble can appear in urine."),
    ("শরীরের রক্তে শর্করার মাত্রা বেড়ে গেলে প্রস্রাবের ঘনঘন প্রবণতা ও ইনফেকশন বাড়ে।", "If blood sugar level in body increases , frequency of urination and infection increases."),
    ("পাবলিক টয়লেট ব্যবহারের পর ভালো করে হাত ধোয়া ও স্যানিটাইজার ব্যবহার করা উচিত।", "After using public toilets , washing hands well and using sanitizer should be done."),
    ("সঠিক পুষ্টিকর খাবার খেলে শরীরের স্বাভাবিক রোগ প্রতিরোধ ক্ষমতা অনেক মজবুত হয়।", "Eating proper nutritious food makes normal immunity of body much stronger."),
    ("গরমকালে অতিরিক্ত ঘাম হওয়ার কারণে শরীরে পানির অভাব দেখা দেওয়া খুব স্বাভাবিক।", "Due to excessive sweating in summer , water deficiency appearing in body is very normal."),
    ("চিকিৎসকের পরামর্শ ছাড়া কোনো ওষুধ বা অ্যান্টিবায়োটিক নিজের ইচ্ছামতো খাওয়া বিপজ্জনক।", "Taking any medicine or antibiotic according to own wish without doctor's advice is dangerous.")
]

nr = [
    ("নাক দিয়ে রক্ত পড়লে মাথা সামান্য সামনে ঝুঁকিয়ে নাকের নরম অংশ ১০ মিনিট চেপে রাখুন।", "If blood falls from nose , tilt head slightly forward and pinch soft part of nose for 10 minutes."),
    ("বাম চোখের পাতা কাঁপলে স্ক্রিন টাইম কমান এবং রাতে পর্যাপ্ত ঘুমানোর চেষ্টা করুন।", "If left eyelid twitches , reduce screen time and try to sleep adequately at night."),
    ("বুকের বাম পাশে চাপ ধরা তীব্র ব্যথা হলে দেরি না করে দ্রুত ইমার্জেন্সিতে নিয়ে যান।", "If there is severe pressing pain on left side of chest , take to emergency quickly without delay."),
    ("দাঁত ক্ষয়ে শিরশির করলে মিষ্টি খাবার কমান এবং ফ্লোরাইড যুক্ত টুথপেস্ট ব্যবহার করুন।", "If teeth decay and tingle , reduce sweet food and use fluoride toothpaste."),
    ("সকালে উঠে পিঠ ও কোমর ব্যথা হলে শক্ত তোষকে ঘুমানোর অভ্যাস গড়ে তুলুন।", "If back and waist pain occurs after waking up in morning , form habit of sleeping on firm mattress."),
    ("নিরামিষ খাদ্যে প্রোটিন বাড়াতে মসুর ডাল , সয়াবিন এবং তোফু বেশি করে খান।", "To increase protein in vegetarian diet , eat lentils , soybeans and tofu more."),
    ("জাঙ্ক ফুড বর্জন করলে মেদ কমানো এবং ডায়াবেটিস প্রতিরোধ করা বেশ সহজ হয়।", "Avoiding junk food makes it quite easy to reduce fat and prevent diabetes."),
    ("পানি কম খেলে শরীর পানিশূন্য হয়ে পড়তে পারে এবং কিডনিতে জটিলতা তৈরি হয়।", "Drinking less water can make body dehydrated and create complications in kidneys."),
    ("ক্রমাগত কাশি থাকলে ফুসফুস পরীক্ষার জন্য একজন বক্ষব্যাধি বিশেষজ্ঞের কাছে যান।", "If having persistent cough , go to a pulmonologist for lung examination."),
    ("সর্দিকাশি হলে উষ্ণ পানি পান করুন এবং গরম পানিতে লবঙ্গ দিয়ে ভাপ নিন।", "If having cold , drink warm water and take steam with cloves in warm water."),
    ("ত্বকে অ্যালার্জি হলে অ্যালকোহলমুক্ত লোশন ব্যবহার করুন এবং সাবান কম লাগান।", "If having skin allergy , use alcohol-free lotion and apply less soap."),
    ("মাথাব্যথার তীব্রতা কমাতে শান্ত ও অন্ধকার ঘরে চোখ বন্ধ করে বিশ্রাম নিন।", "To reduce severity of headache , take rest closing eyes in a quiet and dark room.")
]
