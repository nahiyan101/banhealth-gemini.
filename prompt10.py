# Prompt 10: ক্রমাগত কাশি হচ্ছে , কিন্তু জ্বর নেই এটা কি চিন্তার বিষয় ? / Is it a cause for concern if you have a persistent cough but no fever?
# HR=14, PR=14, NR=14

g_bn = "স্যাস্থসচেতনা"
g_en = "Health awareness"
p_bn = "ক্রমাগত কাশি হচ্ছে , কিন্তু জ্বর নেই এটা কি চিন্তার বিষয় ?"
p_en = "Is it a cause for concern if you have a persistent cough but no fever?"

hr = [
    ("জ্বর ছাড়া ক্রমাগত কাশি হাঁপানি , অ্যালার্জি , অ্যাসিড রিফ্লাক্স বা পোস্ট-নাসাল ড্রিপের লক্ষণ হতে পারে , তবে এটি তিন সপ্তাহের বেশি স্থায়ী হলে ডাক্তার দেখানো উচিত।", "Persistent cough without fever can be a symptom of asthma , allergies , acid reflux or post-nasal drip , but if it lasts more than three weeks a doctor should be consulted."),
    ("দীর্ঘস্থায়ী কাশি যদি তিন সপ্তাহের বেশি থাকে বা কাশির সাথে রক্ত , শ্বাসকষ্ট ও ওজন কমা দেখা দেয় , তবে অবশ্যই বুকের এক্স-রে করানো দরকার।", "If persistent cough lasts more than three weeks or is accompanied by blood , shortness of breath and weight loss , getting a chest X-ray done is definitely needed."),
    ("অ্যালার্জিজনিত কাশির কারণে জ্বর নাও থাকতে পারে , তাই ধূলাবালি , ধোঁয়া এবং অ্যালার্জেন এড়িয়ে চলুন এবং অ্যান্টিহিস্টামিন সেবন করুন।", "Allergy-related cough may not cause fever , so avoid dust , smoke and allergens and take antihistamines."),
    ("গ্যাস্ট্রিক বা এসিড রিফ্লাক্সের কারণে কাশির উদ্রেক হতে পারে , তাই শোবার আগে ভারী খাবার খাওয়া বন্ধ করুন এবং বালিশ উঁচু করে ঘুমান।", "Gastric or acid reflux can trigger cough , so stop eating heavy meals before bedtime and sleep with an elevated pillow."),
    ("ধূমপায়ীদের ক্ষেত্রে জ্বর ছাড়াই স্থায়ী কাশি হতে পারে , যা ব্রঙ্কাইটিস বা ফুসফুসের মারাত্মক ক্ষতির ইঙ্গিত দেয় , তাই অনতিবিলম্বে ধূমপান ছাড়ুন।", "In smokers , a permanent cough without fever can occur , indicating bronchitis or severe lung damage , so quit smoking immediately."),
    ("পরিবেশগত দূষণ বা রাসায়নিক ধোঁয়ার সংস্পর্শে আসার কারণে জ্বর ছাড়া খুশখুশে কাশি হতে পারে , এজন্য বাইরে বের হলে মাস্ক ব্যবহার করুন।", "Exposure to environmental pollution or chemical smoke can cause ticklish cough without fever , so use a mask when going outside."),
    ("উচ্চ রক্তচাপের কিছু ওষুধ যেমন এসিই ইনহিবিটর গ্রহণের ফলে পার্শ্বপ্রতিক্রিয়া হিসেবে জ্বর ছাড়া শুষ্ক কাশি হতে পারে , সেক্ষেত্রে ডাক্তারের সাথে কথা বলুন।", "Taking certain high blood pressure medicines like ACE inhibitors can cause dry cough without fever as a side effect , so talk to your doctor in that case."),
    ("টিবি বা যক্ষ্মা রোগের প্রাথমিক অবস্থায় জ্বর ছাড়াও ক্রমাগত কাশি হতে পারে , তাই কফ পরীক্ষা করিয়ে নিশ্চিত হওয়া অত্যন্ত প্রয়োজন।", "In early stages of TB or tuberculosis , persistent cough can occur even without fever , so getting phlegm tested is extremely necessary."),
    ("কাশি তিন সপ্তাহের বেশি দীর্ঘ হলে ফুসফুসের প্রদাহ বা টিউমার পরীক্ষার জন্য একজন বক্ষব্যাধি বিশেষজ্ঞ চিকিৎসকের শরণাপন্ন হওয়া উচিত।", "If cough persists for more than three weeks , consulting a chest specialist for lung inflammation or tumor testing is proper."),
    ("জ্বর না থাকলেও দীর্ঘদিনের শুকনো কাশির চিকিৎসায় চিকিৎসকের পরামর্শে ব্রঙ্কোডাইলেটর বা কফ সিরাপ ব্যবহার করা যেতে পারে।", "Even if there is no fever , bronchodilators or cough syrup can be used on doctor's advice for treating long-term dry cough."),
    ("গলার শুষ্কতা ও অ্যালার্জিজনিত কফ দূর করতে গরম পানির ভাপ বা স্টিম নেওয়া এবং ঈষদুষ্ণ পানিতে লবণ মিশিয়ে কুলকুচি করা বেশ কার্যকর।", "Taking warm water steam and gargling with lukewarm salt water is quite effective in removing throat dryness and allergic cough."),
    ("হাঁপানি বা অ্যাজমার কারণে জ্বর ছাড়া রাতে কাশির তীব্রতা বাড়তে পারে , ইনহেলার ব্যবহারের জন্য ডাক্তারের মতামত নিন।", "Due to asthma or allergy , cough severity without fever can increase at night , take doctor's opinion for using inhalers."),
    ("সাইনাসের সমস্যার কারণে নাকের সর্দি গলায় পড়ে খুশখুশে কাশির সৃষ্টি করে , যা সারাতে নেসাল স্প্রে ব্যবহার করা যেতে পারে।", "Due to sinus issues , nasal discharge falling into throat creates ticklish cough , which can be treated using nasal spray."),
    ("জ্বর না থাকলেও কাশি যদি দিনের স্বাভাবিক কাজকর্ম ও ঘুমে ব্যাঘাত ঘটায় , তবে বিলম্ব না করে ক্লিনিকাল পরীক্ষা করানো জরুরি।", "Even without fever , if cough disrupts daily normal work and sleep , getting clinical examination done without delay is urgent.")
]

pr = [
    ("শীতকালে আবহাওয়া পরিবর্তনের কারণে অনেকেরই গলায় খুশখুশ ভাব এবং হালকা কাশি দেখা দেয়।", "In winter , due to weather changes , many people experience throat tickle and mild cough."),
    ("আমাদের প্রতিদিনের খাদ্যাভ্যাসে আদা ও মধুর চা যুক্ত করলে গলার স্বস্তি অনেক বৃদ্ধি পায়।", "Adding ginger and honey tea to our daily food habits increases throat comfort significantly."),
    ("আমার এক বড় ভাই অনেক দিন ধরে শুষ্ক কাশিতে ভুগে পরবর্তীতে ওষুধ খেয়ে ভালো হয়েছেন।", "An elder brother of mine suffered from dry cough for a long time and later recovered after taking medicine."),
    ("ধূলিবালিমুক্ত তাজা বাতাসে হাঁটাহাঁটি করা ফুসফুসের স্বাস্থ্যের জন্য অত্যন্ত উপকারী।", "Walking in dust-free fresh air is extremely beneficial for lung health."),
    ("শরীর সুস্থ রাখতে পর্যাপ্ত ঘুমানো এবং পুষ্টিকর খাবার খাওয়া অত্যন্ত গুরুত্বপূর্ণ।", "Sleeping adequately and eating nutritious food is extremely important to keep body healthy."),
    ("বাইরে বের হওয়ার সময় মুখ ও নাক ঢেকে রাখা রোগ জীবাণু প্রতিরোধে সাহায্য করে।", "Covering mouth and nose while going out helps prevent disease germs."),
    ("গলার যেকোনো সমস্যায় ঠাণ্ডা পানি পান করা থেকে বিরত থাকা বুদ্ধিমানের কাজ।", "In any throat problem , refraining from drinking cold water is a wise thing."),
    ("ছোট বাচ্চাদের কাশি হলে ঘরোয়া টোটকা হিসেবে তুলসী পাতার রস খাওয়ানো হয়।", "When young children get cough , basil leaf juice is fed as a home remedy."),
    ("ঋতু পরিবর্তনের সময় শরীরের রোগ প্রতিরোধ ক্ষমতা কিছুটা কমে যেতে দেখা যায়।", "During seasonal changes , body immunity is seen to decrease slightly."),
    ("ধূমপান স্বাস্থ্যের জন্য অত্যন্ত ক্ষতিকর এবং এটি মানবদেহের নানা অঙ্গ নষ্ট করে।", "Smoking is extremely harmful for health and damages various organs of human body."),
    ("ঠাণ্ডা বাতাসে কাজ করলে গলার পেশী শক্ত হয়ে অস্বস্তি এবং কাশি অনুভূত হতে পারে।", "Working in cold air can stiffen throat muscles causing discomfort and felt cough."),
    ("আমাদের বাড়ির আশেপাশে পরিষ্কার-পরিচ্ছন্ন পরিবেশ বজায় রাখা সবার দায়িত্ব।", "Maintaining a clean environment around our home is everyone's responsibility."),
    ("নিয়মিত গরম তরল খাবার খেলে শ্বাসনালী সতেজ থাকে এবং কফ জমে থাকে না।", "Eating warm liquid food regularly keeps airways fresh and prevents phlegm accumulation."),
    ("যেকোনো অসুখ দীর্ঘস্থায়ী রূপ নেওয়ার আগেই চিকিৎসকের মতামত নেওয়া ভালো।", "Taking doctor's opinion before any illness takes a long-term form is good.")
]

nr = [
    ("নাক থেকে হঠাৎ রক্ত পড়া শুরু হলে সোজা হয়ে বসে নাকের ডগা ১০ মিনিট চেপে ধরুন।", "If blood suddenly starts falling from nose , sit straight and pinch tip of nose for 10 minutes."),
    ("বাম চোখের পাতা কাঁপলে ল্যাপটপের ব্যবহার কমান এবং চোখে গরম সেঁক দিন।", "If left eyelid twitches , reduce laptop use and apply warm compress to eyes."),
    ("বুকের বাম পাশে চাপ ধরে তীব্র ব্যথা হলে দেরি না করে দ্রুত ইমার্জেন্সিতে যান।", "If there is severe pressing pain on left side of chest , go to emergency quickly without delay."),
    ("দাঁত ক্ষয়ে শিরশির করলে মিষ্টি খাবার বন্ধ করুন এবং সেনসেটিভ টুথপেস্ট ব্যবহার করুন।", "If teeth decay and tingle , stop sweet food and use sensitive toothpaste."),
    ("সকালে উঠে পিঠ ও কোমর ব্যথা হলে শক্ত তোষকে ঘুমানোর অভ্যাস গড়ে তুলুন।", "If back and waist pain occurs after waking up in morning , form habit of sleeping on firm mattress."),
    ("মূত্রত্যাগের পর ঝিনঝিন করলে বেশি করে পানি পান করুন এবং ডাক্তার দেখান।", "If tingling occurs after urination , drink more water and see a doctor."),
    ("প্রোটিনের চাহিদা মেটাতে প্রতিদিন মসুর ডাল , সয়াবিন এবং তোফু খাওয়া ভালো।", "To fulfill protein requirement , eating lentils , soybeans and tofu daily is good."),
    ("জাঙ্ক ফুড বর্জন করলে মেদ কমানো এবং ডায়াবেটিস প্রতিরোধ করা সহজ হয়।", "Avoiding junk food makes it easy to reduce fat and prevent diabetes."),
    ("পানি কম খেলে শরীর পানিশূন্য হয়ে পড়তে পারে এবং কিডনিতে পাথর হওয়ার ঝুঁকি বাড়ে।", "Drinking less water can make body dehydrated and increases risk of kidney stones."),
    ("পায়ের গোড়ালি মচকে গেলে সেখানে বরফের সেঁক দিন এবং পা উঁচুতে তুলে রাখুন।", "If ankle gets sprained , apply ice compress there and keep foot elevated."),
    ("ত্বকে ফুসকুড়ি বা অ্যালার্জি হলে অ্যালকোহলমুক্ত ময়েশ্চারাইজার ব্যবহার করা উচিত।", "If skin rash or allergy occurs , alcohol-free moisturizer should be used."),
    ("মাথাব্যথা অতিরিক্ত হলে অন্ধকার ঘরে চোখ বন্ধ করে কিছুক্ষণ বিশ্রাম নিন।", "If headache is excessive , take rest closing eyes in a dark room for a while."),
    ("কানের ইনফেকশন এড়াতে গোসলের সময় কানে পানি ঢুকতে দেওয়া যাবে না।", "To avoid ear infection , water should not be allowed to enter ear during bath."),
    ("মাড়ি থেকে রক্ত পড়লে ভিটামিন সি যুক্ত শাকসবজি ও ফলমূল বেশি করে খান।", "If bleeding occurs from gums , eat more vitamin C rich vegetables and fruits.")
]
