# Prompt 4: বাম চোখের পাতা কাঁপছে দিনের বেশিরভাগ সময় , কি করা উচিৎ / My left eyelid is twitching most of the day, what should I do?
# HR=14, PR=14, NR=14

g_bn = "চোখ জনিত সমস্যা"
g_en = "Eye problems"
p_bn = "বাম চোখের পাতা কাঁপছে দিনের বেশিরভাগ সময় , কি করা উচিৎ"
p_en = "My left eyelid is twitching most of the day, what should I do?"

hr = [
    ("চোখের পাতা কাঁপা বন্ধ করতে পর্যাপ্ত ঘুম নিশ্চিত করুন , কম্পিউটার ও মোবাইলের স্ক্রিন টাইম কমান এবং মানসিক চাপমুক্ত থাকুন।", "To stop eyelid twitching , ensure adequate sleep , reduce computer and mobile screen time and stay stress-free."),
    ("অতিরিক্ত চা বা কফি খাওয়া কমান এবং চোখের পাতায় হালকা গরম পানির সেঁক দিলে চোখের পেশী শিথিল হয়ে কাঁপা কমে।", "Reduce excess tea or coffee intake and applying mild warm water compress on eyelids relaxes eye muscles and reduces twitching."),
    ("চোখের শুষ্কতা এড়াতে চিকিৎসকের পরামর্শে লুব্রিকেটিং আই ড্রপ ব্যবহার করুন এবং চোখকে মাঝেমধ্যে বিশ্রাম দিন।", "To avoid eye dryness , use lubricating eye drops on doctor's advice and give rest to eyes intermittently."),
    ("যদি চোখের পাতা কাঁপা কয়েক সপ্তাহের বেশি স্থায়ী হয় বা চোখ পুরোপুরি বন্ধ হয়ে যায় , তবে অবশ্যই চক্ষু বিশেষজ্ঞ দেখান।", "If eyelid twitching lasts more than a few weeks or the eye closes completely , definitely see an ophthalmologist."),
    ("শরীরে ম্যাগনেসিয়াম এবং ভিটামিন বি-১২ এর ঘাটতি চোখের পাতা কাঁপাতে পারে , তাই পুষ্টিকর খাবার গ্রহণ করুন।", "Lack of magnesium and vitamin B-12 in the body can cause eyelid twitching , so eat nutritious food."),
    ("চোখের ওপর অতিরিক্ত ধকল এড়াতে প্রতি ২০ মিনিট পর স্ক্রিন থেকে চোখ সরিয়ে ২০ ফুট দূরের কোন বস্তুর দিকে তাকান।", "To avoid extra strain on eyes , move eyes away from screen every 20 minutes and look at an object 20 feet away."),
    ("চোখের পাতা কাঁপলে চোখ ঘষা থেকে বিরত থাকুন এবং চোখে পর্যাপ্ত আলো বাতাসের ব্যবস্থা রাখুন।", "If eyelid twitches , refrain from rubbing the eyes and ensure adequate light and ventilation for eyes."),
    ("দিনের বেশিরভাগ সময় চোখের পাতা কাঁপলে ক্যাফেইন সমৃদ্ধ পানীয় এড়িয়ে চলাই সবচেয়ে ভালো পদক্ষেপ।", "If the eyelid twitches most of the day , avoiding caffeine-rich beverages is the best step."),
    ("চোখের অতিরিক্ত ক্লান্তি দূর করতে রাতে অন্তত ৭ থেকে ৮ ঘণ্টা নিরবচ্ছিন্ন ঘুম নিশ্চিত করা প্রয়োজন।", "To remove extra fatigue of eyes , ensuring at least 7 to 8 hours of uninterrupted sleep at night is necessary."),
    ("চোখের পেশীর ক্লান্তি কমাতে মৃদু হাতে চোখের চারপাশের অংশে আলতো করে ম্যাসাজ করতে পারেন।", "To reduce eye muscle fatigue , you can gently massage the area around the eyes with mild hands."),
    ("যদি চোখের পাতা কাঁপার সাথে মুখমন্ডলের অন্যান্য পেশী লাফাতে থাকে , তবে নিউরোলজিস্টের সাথে দ্রুত যোগাযোগ করুন।", "If along with eyelid twitching other facial muscles twitch , contact a neurologist quickly."),
    ("ডিজিটাল ডিসপ্লে ব্যবহার করার সময় অ্যান্টি-গ্লেয়ার চশমা ব্যবহার করলে চোখের ওপর চাপ কমে এবং পাতা কাঁপা বন্ধ হয়।", "Using anti-glare glasses while using digital displays reduces eye strain and stops eyelid twitching."),
    ("চোখে পানির ঘাটতি দূর করতে সারাদিনে পর্যাপ্ত পানি পান করুন এবং চোখের শুষ্কতা প্রতিরোধ করুন।", "Drink sufficient water throughout the day to remove water deficiency in eyes and prevent eye dryness."),
    ("চোখের স্বাস্থ্য ভালো রাখতে নিয়মিত পুষ্টিকর শাকসবজি ও ফল খাওয়ার পাশাপাশি চোখে ঠাণ্ডা পানির ঝাপটা দিন।", "To keep eye health good , eat nutritious vegetables and fruits regularly alongside splashing cold water on eyes.")
]

pr = [
    ("টানা কাজ করার কারণে ইদানীং আমারও মাঝে মাঝে ডান চোখের পাতা হালকা কাঁপে।", "Due to continuous work , my right eyelid also twitches lightly sometimes nowadays."),
    ("চোখের যেকোনো সমস্যা হলে নিজে নিজে ওষুধ ব্যবহার না করে সতর্কতা অবলম্বন করা ভালো।", "In case of any eye problem , it is good to exercise caution without using medicines by oneself."),
    ("প্রতিদিন সকালে উঠে ঠান্ডা পানি দিয়ে চোখ ধুলে চোখ বেশ পরিষ্কার ও সতেজ থাকে।", "Washing eyes with cold water every morning keeps eyes quite clean and refreshed."),
    ("অনেকক্ষণ ধরে বই পড়লে বা কম্পিউটারে কাজ করলে চোখ লাল হয়ে যেতে পারে।", "Reading books or working on computer for a long time can make eyes red."),
    ("আমাদের চোখের দৃষ্টিশক্তি সচল রাখতে নিয়মিত ভিটামিন এ যুক্ত খাবার খাওয়া উচিত।", "To keep our eyesight active , vitamin A rich food should be eaten regularly."),
    ("চোখে অ্যালার্জি হলে চুলকানি এবং পানি পড়ার সমস্যা দেখা দিতে পারে।", "If there is eye allergy , itching and watery eyes problems can appear."),
    ("অন্ধকার ঘরে মোবাইল ব্যবহার করলে চোখের ক্ষতি হওয়ার আশঙ্কা অনেক বেশি থাকে।", "Using mobile in a dark room carries a much higher risk of eye damage."),
    ("বয়স বাড়ার সাথে সাথে মানুষের চোখের পাওয়ার পরিবর্তন হওয়া একটি স্বাভাবিক বিষয়।", "With increasing age , change in people's eye power is a normal matter."),
    ("রোদ থেকে চোখকে বাঁচাতে বাইরে বের হলে সানগ্লাস ব্যবহার করা উপকারী।", "To save eyes from sunlight , using sunglasses when going out is beneficial."),
    ("চোখের যেকোনো অপারেশনের পর অতিরিক্ত যত্ন ও ডাক্তারের পরামর্শ মেনে চলতে হয়।", "After any eye surgery , extra care and doctor's advice must be followed."),
    ("আমি প্রতিদিন কাজ শেষ করে চোখে সুতি কাপড় দিয়ে বিশ্রাম দিতে পছন্দ করি।", "After finishing work daily , I prefer to give rest to eyes with a cotton cloth."),
    ("চোখে ধূলিবালি ঢুকলে তা কখনোই হাত দিয়ে জোরে ঘষা উচিত নয়।", "If dust enters eyes , it should never be rubbed hard with hands."),
    ("কম্পিউটারের ব্রাইটনেস সঠিক মাত্রায় রাখলে চোখের ওপর ধকল অনেকটা কম পড়ে।", "Keeping computer brightness at proper levels reduces strain on eyes significantly."),
    ("চোখে কোন অস্বস্তি হলে পরিষ্কার তোয়ালে ব্যবহার করে মুখ মোছা ভালো।", "If there is any discomfort in eyes , it is good to wipe face using a clean towel.")
]

nr = [
    ("নাক দিয়ে রক্ত পড়লে মাথা নিচু করে নাকের ছিদ্র ১০ মিনিট চেপে ধরে রাখুন।", "If blood flows from nose , keep head low and pinch nostril for 10 minutes."),
    ("দাঁতে পোকা লাগলে এবং তীব্র ব্যথা হলে দ্রুত ডেন্টিস্টের কাছে যাওয়া উচিত।", "If there is tooth decay and severe pain , going to dentist quickly is proper."),
    ("বুকের বাম পাশে চাপ ধরা ব্যথা হলে কালক্ষেপণ না করে দ্রুত হাসপাতালে যান।", "If there is pressing pain on left side of chest , go to hospital quickly without delay."),
    ("সকালে উঠে ব্যাক পেইন হলে শক্ত তোষকে ঘুমানোর অভ্যাস গড়ে তুলুন।", "If back pain occurs after waking up in morning , form a habit of sleeping on firm mattress."),
    ("মূত্রত্যাগের পর ঝিনঝিন করলে বেশি করে পানি ও তরল খাবার গ্রহণ করুন।", "If tingling occurs after urination , consume more water and liquid foods."),
    ("নিরামিষ খাবারে পর্যাপ্ত প্রোটিন পেতে সয়াবিন ও ছোলার ডাল খাওয়া স্বাস্থ্যকর।", "To get adequate protein in vegetarian food , eating soybeans and chana dal is healthy."),
    ("জাঙ্ক ফুড এড়িয়ে চললে স্থূলতা ও উচ্চ রক্তচাপ নিয়ন্ত্রণ করা সম্ভব হয়।", "Avoiding junk food makes it possible to control obesity and high blood pressure."),
    ("দেহে পানিশূন্যতা থাকলে কিডনিতে পাথর ও মাথা ব্যথার লক্ষণ দেখা দেয়।", "If dehydration exists in body , symptoms of kidney stones and headache appear."),
    ("ক্রমাগত কাশি থাকলে ফুসফুস পরীক্ষার জন্য ডাক্তারের কাছে যান।", "If there is continuous cough , go to doctor for lung examination."),
    ("সর্দিকাশি থেকে দ্রুত আরাম পেতে গরম চা ও স্টিম নেওয়া বেশ কার্যকরী।", "To get quick relief from cold , taking hot tea and steam is quite effective."),
    ("পায়ের পেশীতে টান লাগলে গরম সেঁক দিন এবং হালকা ম্যাসাজ করুন।", "If muscle cramp occurs in leg , apply warm compress and light massage."),
    ("হজমের সমস্যা দূর করতে প্রতিদিন পর্যাপ্ত আঁশযুক্ত শাকসবজি খাওয়া উচিত।", "To eliminate digestive problems , adequate fiber-rich vegetables should be eaten daily."),
    ("ত্বকে ফুসকুড়ি দেখা দিলে অ্যালার্জি প্রতিরোধক মলম ব্যবহার করতে পারেন।", "If skin rash appears , anti-allergy ointment can be used."),
    ("মাথাব্যথা তীব্র হলে অন্ধকার ঘরে বিশ্রাম নেওয়া ও পর্যাপ্ত পানি পান করা দরকার।", "If headache is severe , taking rest in a dark room and drinking adequate water is needed.")
]
