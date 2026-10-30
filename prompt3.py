# Prompt 3: নাক থেকে রক্ত ঝরে পড়ছে হঠাৎ করেই হয় , কি করা উচিৎ / Blood is coming out of the nose suddenly, what should I do?
# HR=14, PR=14, NR=14

g_bn = "প্রাথমিক চিকিংসা"
g_en = "Primary Chikingsa"
p_bn = "নাক থেকে রক্ত ঝরে পড়ছে হঠাৎ করেই হয় , কি করা উচিৎ"
p_en = "Blood is coming out of the nose suddenly, what should I do?"

hr = [
    ("হঠাৎ নাক থেকে রক্ত পড়লে মাথা সামনের দিকে সামান্য ঝুঁকিয়ে নাকের নরম অংশ আঙুল দিয়ে ১০ মিনিট চেপে ধরে রাখুন।", "If blood suddenly comes out of the nose , tilt your head slightly forward and pinch the soft part of the nose with fingers for 10 minutes."),
    ("নাক দিয়ে রক্ত পড়ার সময় কখনো মাথা পিছনের দিকে হেলানো যাবে না , কারণ রক্ত পেটে বা শ্বাসনালীতে যেতে পারে।", "While bleeding from the nose , never tilt your head backward , as blood may go into the stomach or airway."),
    ("নাকের ওপর বা কপালের পেছনের অংশে বরফের প্যাক ধরে রাখলে রক্তনালী সংকুচিত হয়ে রক্ত পড়া দ্রুত বন্ধ হয়।", "Holding an ice pack on the nose or back of the forehead constricts blood vessels and stops bleeding quickly."),
    ("নাক চেপে ধরে রাখার সময় মুখ দিয়ে শ্বাস নিন এবং রক্ত মুখের ভেতরে এলে তা গিলে না ফেলে থুতু দিয়ে ফেলে দিন।", "Breathe through your mouth while pinching the nose , and if blood comes into the mouth , spit it out without swallowing."),
    ("রক্ত পড়া বন্ধ হওয়ার পর অন্তত কয়েক ঘণ্টা নাক ঝাড়বেন না বা নাকে আঙুল দেবেন না।", "After bleeding stops , do not blow your nose or put fingers in the nose for at least a few hours."),
    ("যদি ২০ মিনিটের বেশি সময় ধরে ক্রমাগত নাক থেকে রক্ত পড়তে থাকে , তবে অবিলম্বে নিকটস্থ হাসপাতালে যান।", "If nosebleeding continues continuously for more than 20 minutes , go to the nearest hospital immediately."),
    ("উচ্চ রক্তচাপের কারণে নাক থেকে রক্ত পড়লে দ্রুত রক্তচাপ মেপে চিকিৎসকের পরামর্শ অনুযায়ী ওষুধ খাবেন।", "If nosebleeding occurs due to high blood pressure , measure blood pressure quickly and take medication according to doctor's advice."),
    ("শুকনো আবহাওয়া বা নাকের শুষ্কতা দূর করতে নাকে স্যালাইন ড্রপ বা পেট্রোলিয়াম জেলি ব্যবহার করা যেতে পারে।", "To remove dry weather or nose dryness , saline drops or petroleum jelly can be used in the nose."),
    ("নাক দিয়ে হঠাৎ রক্ত পড়লে শান্ত থাকুন , কারণ ভয় পেলে রক্তচাপ বেড়ে রক্ত পড়ার পরিমাণ বৃদ্ধি পেতে পারে।", "Stay calm if blood suddenly comes out of the nose , because getting scared increases blood pressure and bleeding amount."),
    ("প্রাথমিক অবস্থায় নাক চেপে রাখার পাশাপাশি ঘাড়ে বা কপালে ঠাণ্ডা পানির সেঁক দিলে রক্তক্ষরণ কমে।", "In initial stages , besides pinching the nose , applying cold water compress on neck or forehead reduces bleeding."),
    ("নাক দিয়ে অতিরিক্ত রক্ত পড়লে এবং মাথা ঘোরা বা দুর্বলতা দেখা দিলে সাথে সাথে ডাক্তার দেখানো দরকার।", "If excessive blood bleeds from the nose and dizziness or weakness appears , seeing a doctor immediately is needed."),
    ("নাক থেকে রক্ত পড়া বন্ধ করার জন্য একটি পরিষ্কার তুলা দিয়ে নাকের ছিদ্র হালকা চেপে রাখা যেতে পারে।", "To stop nosebleeding , a clean cotton ball can be used to lightly press the nostril."),
    ("নাক দিয়ে রক্ত পড়ার সময় রক্ত জমাট বাঁধা নিশ্চিত করতে নিচু হয়ে বসা সবচেয়ে নিরাপদ প্রাথমিক চিকিৎসা।", "Sitting down low while bleeding from the nose is the safest first aid to ensure blood clotting."),
    ("বারবার একই নাক থেকে রক্ত পড়লে নাকের ভেতরের রক্তনালী পরীক্ষার জন্য নাক-কান-গলা বিশেষজ্ঞের সাথে যোগাযোগ করুন।", "If blood comes out of the same nostril repeatedly , contact an ENT specialist for examination of internal blood vessels.")
]

pr = [
    ("গরমের দিনে রোদে বেশি সময় কাটানোর কারণে অনেকের নাক দিয়ে রক্ত পড়তে দেখা যায়।", "During hot days , many people are seen to have nosebleeds due to spending too much time in the sun."),
    ("আমার এক দূর সম্পর্কের ভাইয়ের ছোটবেলায় প্রায়ই হঠাৎ করে নাক দিয়ে রক্ত পড়ত।", "A distant cousin of mine used to have sudden nosebleeds frequently during childhood."),
    ("নাক সবসময় পরিষ্কার রাখা এবং শক্ত করে খোঁচা না দেওয়া স্বাস্থ্যের জন্য ভালো।", "Keeping the nose always clean and not poking it hard is good for health."),
    ("উচ্চ রক্তচাপ থাকলে শরীরে বিভিন্ন রকমের জটিলতা এবং অস্বস্তি দেখা দিতে পারে।", "If there is high blood pressure , various complexities and discomforts may appear in the body."),
    ("শীতকালে বাতাসে আর্দ্রতা কম থাকায় নাক এবং ত্বক অনেক বেশি শুষ্ক হয়ে যায়।", "In winter , due to low humidity in the air , nose and skin become much drier."),
    ("মাথায় আঘাত লাগলে বা হঠাৎ কোনো দুর্ঘটনা ঘটলে রক্তক্ষরণ হওয়া স্বাভাবিক ঘটনা।", "If there is a head injury or a sudden accident occurs , bleeding is a normal event."),
    ("ছোট বাচ্চাদের নাকে কোনো ছোট জিনিস ঢুকে গেলে সেখান থেকে রক্ত আসতে পারে।", "If a small object enters a child's nose , blood can come from there."),
    ("হঠাৎ শরীর খারাপ লাগলে কিছুক্ষণ বিশ্রাম নেওয়া এবং প্রচুর পানি পান করা উচিত।", "If you feel suddenly unwell , taking rest for a while and drinking plenty of water is proper."),
    ("যে কোনো ধরণের রক্তপাত দেখলে সাধারণ মানুষ কিছুটা আতঙ্কিত হয়ে পড়েন।", "Seeing any type of bleeding , general people become somewhat panicked."),
    ("নাকের অ্যালার্জি থাকলে হাঁচি এবং সর্দির সমস্যা দীর্ঘ সময় ধরে কষ্ট দিতে পারে।", "If there is nasal allergy , sneezing and cold problems can cause distress for a long time."),
    ("আমাদের ঘরের ফার্স্ট এইড বক্সে তুলা এবং অ্যান্টিসেপটিক ব্যান্ডেজ থাকা দরকার।", "Our home first aid box needs to have cotton and antiseptic bandages."),
    ("রক্তে প্লাটিলেট বা জমাট বাঁধার উপাদান কমে গেলে শরীর থেকে সহজে রক্ত বের হয়।", "If platelets or clotting factors decrease in blood , blood easily flows out of the body."),
    ("নাকের মেমব্রেন খুব পাতলা হওয়ায় সামান্য ঘষা লাগলেই ছিলে যেতে পারে।", "Because the nasal membrane is very thin , even a slight friction can scrape it."),
    ("শরীরে ভিটামিন সি এবং কে-এর অভাব থাকলেও মাঝেমধ্যে রক্তক্ষরণের প্রবণতা দেখা যায়।", "Even if there is a lack of vitamin C and K in the body , bleeding tendencies are seen sometimes.")
]

nr = [
    ("দাঁতের মাড়ি থেকে রক্ত পড়লে লবণ পানিতে কুলি করুন এবং ডেন্টিস্টের পরামর্শ নিন।", "If bleeding occurs from tooth gums , gargle with salt water and take a dentist's advice."),
    ("চোখের পাতা কাঁপলে চোখকে বিশ্রাম দিন এবং কম্পিউটার ব্যবহার কমান।", "If the eyelid twitches , give rest to eyes and reduce computer usage."),
    ("বুকের বাম পাশে ব্যথা হলে দেরি না করে দ্রুত ইসিজি পরীক্ষা করানো উচিত।", "If there is pain on the left side of the chest , an ECG test should be done quickly without delay."),
    ("সকালে কোমর ব্যথা হলে নিয়মিত হালকা ব্যায়াম করুন এবং শক্ত তোষকে ঘুমান।", "If waist pain occurs in the morning , exercise lightly regularly and sleep on a firm mattress."),
    ("মূত্রত্যাগের সময় জ্বালা করলে প্রচুর পানি পান করুন এবং ডাক্তারের পরামর্শ নিন।", "If there is burning during urination , drink plenty of water and consult a doctor."),
    ("শরীরে প্রোটিনের চাহিদা মেটাতে প্রতিদিন ছোলার ডাল , তোফু এবং পনির খান।", "To meet protein needs in the body , eat chana dal , tofu and cottage cheese daily."),
    ("জাঙ্ক ফুড অতিরিক্ত খেলে স্থূলতা এবং ডায়াবেটিসের ঝুঁকি আশঙ্কাজনকভাবে বাড়ে।", "Eating excess junk food alarmingly increases the risk of obesity and diabetes."),
    ("পানি কম খেলে কোষ্ঠকাঠিন্য এবং কিডনিতে পাথর হওয়ার বড় ধরনের ঝুঁকি থাকে।", "Drinking less water carries a major risk of constipation and kidney stones."),
    ("কাশি দীর্ঘ স্থায়ী হলে ডাক্তারের পরামর্শে বুকের এক্স-রে করানো দরকার।", "If cough lasts long , a chest X-ray needs to be done on doctor's advice."),
    ("সর্দিকাশি থেকে মুক্তি পেতে নিয়মিত গরম পানির ভাপ নেওয়া অত্যন্ত কার্যকর।", "Taking regular warm water steam is very effective for relief from colds."),
    ("পায়ের গোড়ালি মচকে গেলে সেখানে বরফের সেঁক দিন এবং পা উঁচুতে রাখুন।", "If the ankle gets sprained , apply ice compress there and keep the foot elevated."),
    ("স্কাল্পে খুশকি দূর করতে ভালো মানের অ্যান্টি-ড্যান্ড্রফ শ্যাম্পু ব্যবহার করুন।", "To remove scalp dandruff , use a good quality anti-dandruff shampoo."),
    ("পেটে তীব্র গ্যস্ট্রিকের ব্যথা হলে তেল-মশলাযুক্ত খাবার সম্পূর্ণ বন্ধ রাখতে হবে।", "If severe gastric pain occurs in the stomach , oily-spicy food must be completely stopped."),
    ("ত্বকের এলার্জি কমাতে ডাব্লিউএইচও অনুমোদিত লোশন ব্যবহার করা যেতে পারে।", "To reduce skin allergy , WHO-approved lotion can be used.")
]
