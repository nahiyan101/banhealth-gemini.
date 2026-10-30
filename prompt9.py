# Prompt 9: পানি কম খেলে শরীরে কি ধরনের সমস্যা হয় ? / What kind of problems does drinking less water cause in the body?
# HR=14, PR=14, NR=14

g_bn = "স্যাস্থসচেতনা"
g_en = "Health awareness"
p_bn = "পানি কম খেলে শরীরে কি ধরনের সমস্যা হয় ?"
p_en = "What kind of problems does drinking less water cause in the body?"

hr = [
    ("পানি কম খেলে ডিহাইড্রেশন বা পানিশূন্যতা দেখা দেয় , যার ফলে কিডনিতে পাথর , কোষ্ঠকাঠিন্য এবং মূত্রনালীর ইনফেকশনের ঝুঁকি তৈরি হয়।", "Drinking less water causes dehydration , resulting in risks of kidney stones , constipation and urinary tract infections."),
    ("শরীরে পানির অভাব হলে ত্বক শুষ্ক হয়ে যায় , মাথাব্যথা ও মাথা ঘোরা শুরু হয় এবং রক্তচাপ হঠাৎ কমে যেতে পারে।", "If there is lack of water in body , skin becomes dry , headache and dizziness start and blood pressure can drop suddenly."),
    ("পর্যাপ্ত পানি না খেলে হজম প্রক্রিয়া ব্যাহত হয়ে অ্যাসিডিটি বা গ্যাস্ট্রিকের সমস্যা বাড়ে এবং প্রস্রাবের রঙ গাঢ় হলুদ হয়।", "Not drinking adequate water disrupts digestion , increasing acidity or gastric issues and making urine color dark yellow."),
    ("কম পানি পান করলে শরীরের বিষাক্ত টক্সিন দূর হতে পারে না , ফলে কিডনির ওপর অতিরিক্ত ধকল পড়ে এবং কিডনি বিকল হতে পারে।", "Consuming less water prevents toxic substances from flushing out of body , putting extra strain on kidneys and causing kidney failure."),
    ("পানিশূন্যতার কারণে শরীরের ইলেক্ট্রোলাইটের ভারসাম্য নষ্ট হয়ে পেশীতে টান ধরা বা মাসল ক্র্যাম্পের সমস্যা দেখা দেয়।", "Due to dehydration , body's electrolyte balance gets disrupted causing muscle cramps or tightness."),
    ("পানি কম খেলে শরীর দ্রুত ক্লান্ত হয়ে পড়ে , কাজ করার শক্তি ও মনোযোগ কমে যায় এবং মেজাজ খিটখিটে হয়ে ওঠে।", "Drinking less water makes body tired quickly , reduces stamina and focus to work and makes mood irritable."),
    ("শরীরে পানির ঘাটতি হলে মুখের লালা উৎপাদন কমে যায় , যার ফলে মুখে দুর্গন্ধ এবং মাড়ির ইনফেকশন বাড়ে।", "If water deficiency occurs in body , mouth saliva production decreases , causing bad breath and gum infection to rise."),
    ("কম পানি পানের অভ্যাস থাকলে জয়েন্ট বা হাড়ের জোড়ের লুব্রিকেশন কমে গিয়ে জয়েন্ট পেইন বা বাতের ব্যথা বৃদ্ধি পায়।", "Having a habit of drinking less water reduces lubrication of joints or bones , increasing joint pain or arthritis pain."),
    ("শরীরে পানির অভাব দেখা দিলে মস্তিষ্কের কার্যক্ষমতা কমে যায় এবং মনোযোগ ধরে রাখতে চরম অসুবিধা হয়।", "When water shortage appears in body , brain functioning decreases and holding concentration becomes extremely difficult."),
    ("পানি কম খেলে রক্তের ঘনত্ব বেড়ে যায় , যা হৃদযন্ত্রের ওপর বাড়তি চাপ সৃষ্টি করে এবং হৃদরোগের ঝুঁকি বাড়ায়।", "Drinking less water increases blood viscosity , which creates extra pressure on heart and increases heart disease risk."),
    ("শরীরে পর্যাপ্ত পানি না থাকলে থার্মোরেনুয়লেশন ব্যাহত হয় , ফলে সামান্য গরমেও শরীর অতিরিক্ত উত্তপ্ত হয়ে হিট স্ট্রোক হতে পারে।", "Without adequate water in body , thermoregulation gets disrupted , so even in slight heat body overheats and heat stroke can happen."),
    ("কম পানি পান করার ফলে পাচনতন্ত্রের বাওয়েল মুভমেন্ট ধীর হয়ে যায় এবং দীর্ঘস্থায়ী কোষ্ঠকাঠিন্য তৈরি হয়।", "Drinking less water slows down digestive tract bowel movements and creates chronic constipation."),
    ("শরীরে পানিশূন্যতা তৈরি হলে শরীরের ভারসাম্য বজায় রাখতে কোষগুলো পানি ধরে রাখে , ফলে ওজন বেড়ে ফোলানো দেখায়।", "If dehydration is created in body , cells retain water to maintain body balance , making weight gain look bloated."),
    ("পানি কম খেলে চোখের অশ্রু উৎপাদন হ্রাস পায় , ফলে চোখ শুষ্ক হয়ে চুলকানি ও জ্বালাপোড়ার সৃষ্টি হতে পারে।", "Drinking less water decreases eye tear production , making eyes dry and creating itching and burning.")
]

pr = [
    ("আমি স্বাস্থ্যসম্মত জীবনযাপন বজায় রাখতে প্রতিদিন অন্তত আট গ্লাস পরিষ্কার পানি পানের চেষ্টা করি।", "I try to drink at least eight glasses of clean water daily to maintain a healthy lifestyle."),
    ("গ্রীষ্মকালে রোদে বের হলে সাথে সবসময় পানির বোতল রাখা এবং প্রচুর তরল খাবার খাওয়া ভালো।", "When going out in sun during summer , keeping a water bottle always with oneself and consuming plenty of liquid food is good."),
    ("আমার এক সহকর্মী কাজের চাপে পড়ে সারাদিন পানি পান করতে একদম ভুলে যায়।", "A colleague of mine gets so caught up in work pressure that he completely forgets to drink water all day."),
    ("শরীরের স্বাস্থ্য ভালো রাখতে কলার জুস , ডাবের পানি এবং লেবুর শরবত খাওয়া বেশ উপকারী।", "To keep body health good , eating banana juice , coconut water and lemon juice is very beneficial."),
    ("সকালে ঘুম থেকে উঠে খালি পেটে এক গ্লাস কুসুম গরম পানি পান করা স্বাস্থ্যের জন্য ভালো।", "Drinking a glass of lukewarm water on empty stomach after waking up in morning is good for health."),
    ("যেকোনো ধরণের শারীরিক অসুস্থতা এড়াতে সুষম খাবারের পাশাপাশি নিরাপদ পানীয় জল নিশ্চিত করা উচিত।", "To avoid any type of physical illness , ensuring safe drinking water along with balanced food should be done."),
    ("খেলাধুলা বা ভারী ব্যায়াম করার সময় শরীর থেকে প্রচুর ঘাম বের হয়ে পানিশূন্যতা তৈরি হয়।", "While playing sports or doing heavy exercise , plenty of sweat leaves body creating dehydration."),
    ("ছোট বাচ্চাদের খেলার ছলে পানি খাওয়ানোর অভ্যাস গড়ে তোলা বাবা-মায়ের দায়িত্ব।", "Developing habit of making young children drink water playfully is parents' responsibility."),
    ("খাবার খাওয়ার ঠিক পরপরই প্রচুর পানি পান করলে পরিপাক এনজাইমগুলো পাতলা হয়ে যেতে পারে।", "Drinking lots of water right after eating food can dilute digestive enzymes."),
    ("বাজারের কৃত্রিম মিষ্টিযুক্ত কোমল পানীয়ের চেয়ে সাধারণ বিশুদ্ধ পানি পানের অভ্যাস অনেক ভালো।", "Having habit of drinking plain pure water is much better than market artificial sweetened soft drinks."),
    ("বয়স্ক মানুষদের তৃষ্ণা পাওয়ার অনুভূতি কমে যায় , তাই তাদের নিয়মিত পানি পানের কথা মনে করিয়ে দেওয়া দরকার।", "Elderly people's sense of thirst decreases , so reminding them to drink water regularly is needed."),
    ("আমাদের শরীরে প্রায় ৬০ শতাংশ পানি থাকে , তাই পানিকে জীবনের অপর নাম বলা হয়ে থাকে।", "Our body consists of about 60 percent water , so water is called another name for life."),
    ("শরীর ডিহাইড্রেটেড কিনা তা বোঝার সবচেয়ে সহজ উপায় হলো প্রস্রাবের রঙ পর্যবেক্ষণ করা।", "The easiest way to understand if body is dehydrated is observing urine color."),
    ("অফিস ডেস্কে সবসময় চোখের সামনে রিফিল করা পানির বোতল রেখে দিলে পানি পানের কথা মনে থাকে।", "Keeping a refilled water bottle always in front of eyes on office desk reminds of drinking water.")
]

nr = [
    ("নাক দিয়ে হঠাৎ রক্ত পড়লে সোজা হয়ে বসে নাকের ডগা ১০ মিনিট চেপে ধরে রাখুন।", "If blood suddenly flows from nose , sit straight and pinch tip of nose for 10 minutes."),
    ("বাম চোখের পাতা কাঁপলে ল্যাপটপের ব্রাইটনেস কমান এবং চোখে গরম সেঁক দিন।", "If left eyelid twitches , reduce laptop brightness and apply warm compress to eyes."),
    ("বুকের বাম পাশে চাপ ধরে তীব্র ব্যথা হলে দেরি না করে দ্রুত ইমার্জেন্সিতে যান।", "If there is severe pressing pain on left side of chest , go to emergency quickly without delay."),
    ("দাঁত ক্ষয়ে শিরশির করলে মিষ্টি খাবার কমান এবং সেনসেটিভ টুথপেস্ট ব্যবহার করুন।", "If teeth decay and tingle , reduce sweet food and use sensitive toothpaste."),
    ("সকালে উঠে পিঠ ও কোমর ব্যথা হলে শক্ত তোষকে ঘুমানোর অভ্যাস গড়ে তুলুন।", "If back and waist pain occurs after waking up in morning , form habit of sleeping on firm mattress."),
    ("মূত্রত্যাগের পর ঝিনঝিন করলে সুতির অন্তর্বাস পরুন এবং ডাক্তারের পরামর্শ নিন।", "If tingling occurs after urination , wear cotton underwear and consult a doctor."),
    ("প্রোটিনের চাহিদা মেটাতে প্রতিদিন মসুর ডাল , সয়াবিন এবং তোফু খাওয়া অত্যন্ত ভালো।", "To fulfill protein requirement , eating lentils , soybeans and tofu daily is extremely good."),
    ("জাঙ্ক ফুড অতিরিক্ত খেলে স্থূলতা এবং উচ্চ রক্তচাপের ঝুঁকি বহুগুণ বেড়ে যায়।", "Eating excess junk food increases risk of obesity and high blood pressure manifold."),
    ("ক্রমাগত কাশি থাকলে ফুসফুস পরীক্ষার জন্য একজন বক্ষব্যাধি বিশেষজ্ঞের কাছে যান।", "If having persistent cough , go to a pulmonologist for lung examination."),
    ("সর্দিকাশি হলে উষ্ণ পানি পান করুন এবং গরম পানিতে লবঙ্গ দিয়ে ভাপ নিন।", "If having cold , drink warm water and take steam with cloves in warm water."),
    ("ত্বকে ফুসকুড়ি বা অ্যালার্জি হলে অ্যালকোহলমুক্ত ময়েশ্চারাইজার ব্যবহার করা উচিত।", "If skin rash or allergy occurs , alcohol-free moisturizer should be used."),
    ("মাথাব্যথা অতিরিক্ত হলে অন্ধকার ঘরে চোখ বন্ধ করে কিছুক্ষণ বিশ্রাম নিন।", "If headache is excessive , take rest closing eyes in a dark room for a while."),
    ("গোড়ালি মচকে গেলে বরফের সেঁক দিন এবং পা উঁচুতে তুলে রাখুন।", "If ankle gets sprained , apply ice compress and elevate foot."),
    ("কানের ইনফেকশন এড়াতে গোসলের সময় কানে পানি ঢুকতে দেওয়া যাবে না।", "To avoid ear infection , water should not be allowed to enter ear during bath.")
]
