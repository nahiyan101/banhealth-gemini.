# Prompt 11: সর্দিকাশি থেকে দ্রুত সেরে উঠার উপায় কী ? / What is the fastest way to recover from a cold?
# HR=14, PR=14, NR=14

g_bn = "স্যাস্থসচেতনা"
g_en = "Health awareness"
p_bn = "সর্দিকাশি থেকে দ্রুত সেরে উঠার উপায় কী ?"
p_en = "What is the fastest way to recover from a cold?"

hr = [
    ("সর্দিকাশি থেকে দ্রুত আরোগ্য পেতে পর্যাপ্ত বিশ্রাম নিন , উষ্ণ পানি ও স্যুপ পান করুন , আদা-মধুর চা খান এবং নিয়মিত গরম পানির ভাপ নিন।", "To get fast recovery from cold , take adequate rest , drink warm water and soup , eat ginger-honey tea and take regular warm water steam."),
    ("ঈষদুষ্ণ পানিতে সামান্য লবণ মিশিয়ে দিনে তিন থেকে চার বার কুলি বা গার্গল করলে গলার খুশখুশ ভাব এবং প্রদাহ দ্রুত কমে যায়।", "Gargling with lukewarm water mixed with a little salt three to four times a day quickly reduces throat tickle and inflammation."),
    ("রোগ প্রতিরোধ ক্ষমতা বাড়াতে প্রাকৃতিকভাবে ভিটামিন সি সমৃদ্ধ খাবার যেমন লেবু , আমলকী , কমলা এবং দস্তা বা জিংক যুক্ত খাবার গ্রহণ করুন।", "To boost immunity naturally , consume vitamin C rich foods like lemon , amla , orange and zinc-rich foods."),
    ("বন্ধ নাক খুলতে মেনথল বা ইউক্যালিপটাস তেল দিয়ে গরম পানির ভাপ নিন এবং রাতে ঘুমানোর সময় নাকে নরমাল স্যালাইন নেসাল ড্রপ ব্যবহার করুন।", "To open blocked nose , take hot water steam with menthol or eucalyptus oil and use normal saline nasal drops in nose when sleeping at night."),
    ("সর্দিকাশির সময়ে অ্যালকোহল ও অতিরিক্ত ক্যাফেইন এড়িয়ে চলুন , কারণ এগুলো শরীরকে পানিশূন্য করে আরোগ্য প্রক্রিয়া ধীর করে দেয়।", "Avoid alcohol and excess caffeine during cold , because these dehydrate body and slow down recovery process."),
    ("গলার অস্বস্তি কমাতে তুলসী পাতা , আদা এবং লবঙ্গ ফুটিয়ে তৈরি কাড়া বা ভেষজ চা পান করা সর্দিকাশি নিরাময়ে অত্যন্ত কার্যকরী।", "Drinking decoction or herbal tea made by boiling basil leaves , ginger and cloves is extremely effective in curing cold."),
    ("ইনফ্লুয়েঞ্জা বা ভাইরাসের বিস্তার কমাতে ঘরবাড়ি পরিষ্কার রাখুন , রুমের শুষ্কতা দূর করতে হিউমিডিফায়ার চালান এবং হাত ভালোভাবে ধোন।", "To reduce spread of influenza or virus , keep home clean , run a humidifier to remove room dryness and wash hands thoroughly."),
    ("সর্দিকাশির শুরুতে ডাক্তারের পরামর্শে প্যারাসিটামল বা অ্যান্টিহিস্টামিন জাতীয় ওষুধ সেবন করলে হাঁচি ও সর্দি দ্রুত নিয়ন্ত্রণে আসে।", "Taking paracetamol or antihistamine medications on doctor's advice at start of cold quickly brings sneezing and runny nose under control."),
    ("শরীরের প্রাকৃতিক ইমিউন সিস্টেমকে সচল রাখতে রাতে অন্তত আট ঘণ্টা নিরবচ্ছিন্ন ঘুম এবং পুষ্টিকর নিরামিষ তরল খাবার খাওয়া প্রয়োজন।", "To keep body's natural immune system active , at least eight hours of uninterrupted sleep at night and nutritious vegetarian liquid foods are needed."),
    ("ঠান্ডা ও আইসক্রিম সম্পূর্ণ এড়িয়ে চলুন এবং শরীর উষ্ণ রাখতে সুতি বা উলের হালকা গরম পোশাক পরে বিশ্রাম নিন।", "Avoid cold items and ice cream completely and take rest wearing cotton or woolen light warm clothes to keep body warm."),
    ("কাশি ও কফ জমলে কাঁচা হলুদ এবং মধু একসাথে খেলে ফুসফুসের শ্লেষ্মা দ্রুত বের হয়ে যায় এবং শ্বাসনালী পরিষ্কার হয়।", "When cough and phlegm accumulate , eating raw turmeric and honey together quickly flushes out lung mucus and clears airways."),
    ("সর্দিকাশি হলে ধোঁয়া ও ধূলাবালিযুক্ত পরিবেশ থেকে দূরে থাকুন এবং ঘরে পর্যাপ্ত আলো-বাতাসের ব্যবস্থা নিশ্চিত করুন।", "When having a cold , stay away from smoky and dusty environments and ensure adequate light and ventilation in the room."),
    ("যদি সর্দিকাশি এক সপ্তাহের বেশি স্থায়ী হয় এবং শ্বাসকষ্ট দেখা দেয় , তবে বিলম্ব না করে একজন বক্ষব্যাধি বিশেষজ্ঞের কাছে যান।", "If cold lasts more than a week and shortness of breath appears , go to a chest specialist without delay."),
    ("হালকা তাজা খাবারের সাথে কাঁচা রসুন ও লবঙ্গ খেলে রসুনের অ্যান্টি-ভাইরাল উপাদান সর্দিকাশি দ্রুত নিরাময়ে সাহায্য করে।", "Eating raw garlic and cloves with light fresh food helps allicin anti-viral components in garlic cure cold quickly.")
]

pr = [
    ("শীতকাল এলেই আমাদের দেশে প্রায় প্রতিটি ঘরে ঘরে সর্দিকাশি ও জ্বরের প্রাদুর্ভাব অনেক বেড়ে যায়।", "Whenever winter arrives , prevalence of cold and fever increases significantly in almost every household in our country."),
    ("শরীর সুস্থ ও রোগমুক্ত রাখতে প্রতিদিন সঠিক সময়ে পুষ্টিকর খাবার খাওয়া অত্যন্ত জরুরি।", "Eating nutritious food on time every day is extremely urgent to keep body healthy and disease-free."),
    ("আমাদের দাদী-নানী আবহমানকাল থেকেই সর্দিকাশিতে মধুর সাথে কালোজিরা খাওয়ার পরামর্শ দিয়ে আসছেন।", "Our grandmothers have been suggesting eating black cumin with honey for colds since time immemorial."),
    ("সঠিক সময়ে সঠিক ওষুধ না খেলে সামান্য ঠাণ্ডা লাগাও পরবর্তীতে জটিল রূপ ধারণ করতে পারে।", "Not taking correct medicine on time can turn even a slight cold into a complex form later."),
    ("ছোট শিশুদের ক্ষেত্রে সর্দিকাশি হলে তাদের বাড়তি যত্ন নেওয়া এবং বুক উষ্ণ রাখা দরকার।", "In case of young children , taking extra care and keeping chest warm when they have cold is needed."),
    ("বাইরে বের হলে সবসময় ধুলাবালি থেকে বাঁচতে উন্নতমানের মাস্ক ব্যবহার করা ভালো স্বাস্থ্যকর অভ্যাস।", "Using high quality mask when going out to save from dust is always a good healthy habit."),
    ("নিয়মিত হাত ধোয়ার অভ্যাস আমাদের বিভিন্ন ধরণের ব্যাকটেরিয়া ও ভাইরাস সংক্রমণ থেকে রক্ষা করে।", "Regular hand washing habit protects us from various types of bacterial and viral infections."),
    ("অনেক সময় আবহাওয়া পরিবর্তনের কারণে অ্যালার্জি থেকে হাঁচি ও চোখ দিয়ে পানি পড়ার সমস্যা তৈরি হয়।", "Often due to weather changes , allergies create problems of sneezing and watery eyes."),
    ("শরীরে পানির ঘাটতি হলে যেকোনো রোগ থেকে সুস্থ হতে শরীরের অতিরিক্ত সময় লেগে যায়।", "If there is water deficiency in body , body takes extra time to recover from any disease."),
    ("আমাদের বাড়ির আশেপাশে যেন মশা না জন্মায় সেদিকে খেয়াল রাখা এবং পরিষ্কার রাখা উচিত।", "We should take care and keep clean so mosquitoes do not breed around our home."),
    ("ঠান্ডা লাগলে অনেকেই চিকিৎসকের পরামর্শ ছাড়াই যত্রতত্র অ্যান্টিবায়োটিক খেয়ে ভুল কাজ করেন।", "When catching a cold , many people make the mistake of eating antibiotics indiscriminately without doctor's advice."),
    ("সুষম খাদ্যাভ্যাস ও নিয়মিত শারীরিক পরিশ্রম মানুষকে দীর্ঘদিন সুস্থ ও কর্মক্ষম রাখতে সাহায্য করে।", "Balanced diet and regular physical work helps keep people healthy and active for long time."),
    ("বাইরের খোলা ও বাসি খাবার খেলে পেট খারাপ হওয়ার সাথে সাথে ইমিউনিটি সিস্টেমও দুর্বল হয়।", "Eating open and stale outer food causes bad stomach along with weakening immune system."),
    ("ঋতু পরিবর্তনের এই সময়ে হালকা গরম পোশাক পরা এবং শরীর ঠাণ্ডা হওয়া থেকে বাঁচানো দরকার।", "During this time of seasonal change , wearing light warm clothes and saving body from getting cold is needed.")
]

nr = [
    ("নাক থেকে রক্ত পড়লে মাথা সোজা রেখে নাকের নরম অংশ ১০ মিনিট চেপে ধরে রাখুন।", "If blood flows from nose , keep head straight and pinch soft part of nose for 10 minutes."),
    ("বাম চোখের পাতা কাঁপলে ল্যাপটপের ব্যবহার কমান এবং চোখে গরম সেঁক দিন।", "If left eyelid twitches , reduce laptop use and apply warm compress to eyes."),
    ("বুকের বাম পাশে চাপ ধরে তীব্র ব্যথা হলে দেরি না করে দ্রুত ইমার্জেন্সিতে যান।", "If there is severe pressing pain on left side of chest , go to emergency quickly without delay."),
    ("দাঁত ক্ষয়ে শিরশির করলে মিষ্টি খাবার বন্ধ করুন এবং সেনসেটিভ টুথপেস্ট ব্যবহার করুন।", "If teeth decay and tingle , stop sweet food and use sensitive toothpaste."),
    ("সকালে উঠে পিঠ ও কোমর ব্যথা হলে শক্ত তোষকে ঘুমানোর অভ্যাস গড়ে তুলুন।", "If back and waist pain occurs after waking up in morning , form habit of sleeping on firm mattress."),
    ("মূত্রত্যাগের পর ঝিনঝিন করলে বেশি করে পানি পান করুন এবং ডাক্তার দেখান।", "If tingling occurs after urination , drink more water and see a doctor."),
    ("প্রোটিনের চাহিদা মেটাতে প্রতিদিন মসুর ডাল , সয়াবিন এবং তোফু খাওয়া ভালো।", "To fulfill protein requirement , eating lentils , soybeans and tofu daily is good."),
    ("জাঙ্ক ফুড বর্জন করলে মেদ কমানো এবং ডায়াবেটিস প্রতিরোধ করা সহজ হয়।", "Avoiding junk food makes it easy to reduce fat and prevent diabetes."),
    ("পানি কম খেলে শরীর পানিশূন্য হয়ে পড়তে পারে এবং কিডনিতে পাথর হওয়ার ঝুঁকি বাড়ে।", "Drinking less water can make body dehydrated and increases risk of kidney stones."),
    ("ত্বকে ফুসকুড়ি বা অ্যালার্জি হলে অ্যালকোহলমুক্ত ময়েশ্চারাইজার ব্যবহার করা উচিত।", "If skin rash or allergy occurs , alcohol-free moisturizer should be used."),
    ("মাথাব্যথা অতিরিক্ত হলে অন্ধকার ঘরে চোখ বন্ধ করে কিছুক্ষণ বিশ্রাম নিন।", "If headache is excessive , take rest closing eyes in a dark room for a while."),
    ("গোড়ালি মচকে গেলে বরফের সেঁক দিন এবং পা উঁচুতে তুলে রাখুন।", "If ankle gets sprained , apply ice compress and elevate foot."),
    ("কানের ইনফেকশন এড়াতে গোসলের সময় কানে পানি ঢুকতে দেওয়া যাবে না।", "To avoid ear infection , water should not be allowed to enter ear during bath."),
    ("মাড়ি থেকে রক্ত পড়লে ভিটামিন সি যুক্ত শাকসবজি ও ফলমূল বেশি করে খান।", "If bleeding occurs from gums , eat more vitamin C rich vegetables and fruits.")
]
