# Prompt 2: জাঙ্ক ফুড খাওয়ার ক্ষতিকর প্রভাব কী ? / What are the harmful effects of eating junk food?
# HR=20, PR=20, NR=20

g_bn = "স্যাস্থসচেতনতা"
g_en = "Health awareness"
p_bn = "জাঙ্ক ফুড খাওয়ার ক্ষতিকর প্রভাব কী ?"
p_en = "What are the harmful effects of eating junk food?"

hr = [
    ("জাঙ্ক ফুড অতিরিক্ত খেলে স্থূলতা , হৃদরোগ , উচ্চ রক্তচাপ এবং টাইপ-২ ডায়াবেটিসের ঝুঁকি আশঙ্কাজনকভাবে বৃদ্ধি পায়।", "Eating excess junk food alarmingly increases the risk of obesity , heart disease , high blood pressure and type-2 diabetes."),
    ("অতিরিক্ত ফাস্টফুড গ্রহণের ফলে হজমের সমস্যা , লিভারে চর্বি জমা এবং রক্তে খারাপ কোলেস্টেরল বৃদ্ধি পায়।", "Consuming excess fast food leads to digestive problems , fat accumulation in the liver and an increase in bad cholesterol in the blood."),
    ("জাঙ্ক ফুডে থাকা উচ্চমাত্রার সোডিয়াম এবং ট্রান্স ফ্যাট ধমনীকে শক্ত করে রক্তচাপ বাড়িয়ে দেয়।", "High amounts of sodium and trans fats in junk food harden arteries and elevate blood pressure."),
    ("নিয়মিত জাঙ্ক ফুড খেলে শারীরিক অলসতা আসে , মনোযোগ কমে এবং কম বয়সে হৃদরোগের আশঙ্কা বাড়ে।", "Eating junk food regularly causes physical lethargy , decreases focus and increases the risk of heart disease at a young age."),
    ("প্রসেসড এবং জাঙ্ক ফুডে পুষ্টির অভাব থাকায় এটি নিয়মিত খেলে অপুষ্টি এবং রোগ প্রতিরোধ ক্ষমতা হ্রাস পায়।", "Since processed and junk food lacks nutrition , eating it regularly causes malnutrition and reduced immunity."),
    ("অতিরিক্ত জাঙ্ক ফুড খাওয়ার ফলে গ্যাস্ট্রিক , অ্যাসিডিটি , কোষ্ঠকাঠিন্য এবং কোলন ক্যান্সারের ঝুঁকি তৈরি হয়।", "Eating excess junk food creates risks of gastric , acidity , constipation and colon cancer."),
    ("জাঙ্ক ফুডে অতিরিক্ত চিনি থাকার কারণে দাঁতের ক্ষয় হয় এবং রক্তের শর্করার মাত্রায় ক্ষতিকর প্রভাব ফেলে।", "Excess sugar in junk food causes tooth decay and negatively impacts blood sugar levels."),
    ("ফাস্টফুড খেলে ব্রেইনের ডোপামিন মাত্রা সাময়িক বাড়লেও তা পরবর্তীতে বিষণ্ণতা এবং ক্লান্তি সৃষ্টি করে।", "While fast food temporarily increases brain dopamine levels , it later causes depression and fatigue."),
    ("জাঙ্ক ফুডে প্রচুর ক্যালোরি ও ক্ষতিকর চর্বি থাকায় এটি দ্রুত শরীরের ওজন ও মেদ বাড়িয়ে দেয়।", "Since junk food contains lots of calories and harmful fats , it rapidly increases body weight and fat."),
    ("অতিরিক্ত জাঙ্ক ফুড খেলে ছোটদের মানসিক বিকাশ ব্যাহত হয় এবং অল্প বয়সে মেদবহুলতা দেখা দেয়।", "Eating excess junk food hinders mental development in children and causes obesity at a young age."),
    ("প্রসেসড খাবারে থাকা রাসায়নিক প্রিজারভেটিভ এবং অতিরিক্ত লবণ কিডনি এবং লিভারের মারাত্মক ক্ষতি করে।", "Chemical preservatives and excess salt in processed food cause severe damage to kidneys and liver."),
    ("জাঙ্ক ফুড খাওয়ার ফলে হরমোনের ভারসাম্য নষ্ট হয় এবং ত্বকে অতিরিক্ত ব্রণ ও চর্মরোগ দেখা দিতে পারে।", "Eating junk food disrupts hormonal balance and can cause excess acne and skin diseases on the skin."),
    ("জাঙ্ক ফুড আমাদের স্বাভাবিক খিদে নষ্ট করে এবং প্রয়োজনীয় পুষ্টি উপাদানের অভাব ঘটিয়ে শরীর দুর্বল করে।", "Junk food ruins our natural appetite and weakens the body by causing a lack of necessary nutrients."),
    ("নিয়মিত ফাস্টফুড খাওয়ার কারণে রক্তনালীতে চর্বির আস্তরণ জমে স্ট্রোক এবং হার্ট অ্যাটাকের ঝুঁকি বাড়ে।", "Regular consumption of fast food causes fat deposition in blood vessels , increasing the risk of stroke and heart attack."),
    ("জাঙ্ক ফুডে অতিমাত্রায় লবণ থাকায় এটি শরীরে পানি ধরে রাখে এবং কিডনির কার্যক্ষমতা কমিয়ে দেয়।", "Excessive salt in junk food causes the body to retain water and reduces kidney function."),
    ("প্রসেসড ও তেলে ভাজা খাবার পরিপাকতন্ত্রের ক্ষতি করে এবং পেটে দীর্ঘস্থায়ী অস্বস্তি ও আলসার তৈরি করে।", "Processed and fried food damages the digestive tract and creates chronic discomfort and ulcers in the stomach."),
    ("জাঙ্ক ফুডের ক্ষতিকর কেমিক্যাল এবং কৃত্রিম রঙ শরীরের কোষের ক্ষতি করে ক্যান্সারের সম্ভাবনা বাড়ায়।", "Harmful chemicals and artificial colors in junk food damage body cells , increasing the chance of cancer."),
    ("নিয়মিত জাঙ্ক ফুড খেলে ইনসুলিন রেজিস্ট্যান্স তৈরি হয় যা সরাসরি ডায়াবেটিস রোগের জন্ম দেয়।", "Eating junk food regularly creates insulin resistance , which directly gives rise to diabetes."),
    ("জাঙ্ক ফুড খেলে শারীরিক ক্ষিপ্রতা ও কর্মক্ষমতা কমে যায় এবং অল্পতেই মানুষ ক্লান্ত হয়ে পড়ে।", "Eating junk food decreases physical agility and stamina , making people tired easily."),
    ("ফাস্টফুডে আঁশ বা ফাইবারের অভাব থাকায় এটি অন্ত্রের স্বাস্থ্য নষ্ট করে এবং তীব্র কোষ্ঠকাঠিন্য ঘটায়।", "Lack of fiber in fast food damages gut health and causes severe constipation.")
]

pr = [
    ("আমি মাঝে মাঝে বন্ধুদের সাথে বাইরে গেলে বার্গার অথবা ফ্রেঞ্চ ফ্রাই খেয়ে থাকি।", "Sometimes when I go out with friends , I eat burgers or french fries."),
    ("আজকাল শহরের অলিতে গলিতে অসংখ্য ফাস্টফুডের দোকান গড়ে উঠেছে।", "Nowadays countless fast food shops have sprung up in every lane of the city."),
    ("আমার ছোট ভাই বাড়ির সাধারণ খাবারের চেয়ে রেস্তোরাঁর খাবার বেশি পছন্দ করে।", "My younger brother prefers restaurant food over simple home-cooked food."),
    ("বাইরের খোলা খাবারের চেয়ে ঘরে তৈরি সুষম খাবার নিশ্চিত করা অত্যন্ত গুরুত্বপূর্ণ।", "Ensuring balanced homemade food is far more important than eating open food outside."),
    ("বাচ্চাদের সুস্বাস্থ্য নিশ্চিত করতে প্রতিদিন পর্যাপ্ত ফল ও শাকসবজি দেওয়া উচিত।", "To ensure good health for children , adequate fruits and vegetables should be given daily."),
    ("সপ্তাহান্তে একবার হালকা ফাস্টফুড খেলে সাধারণত শরীরের বড় কোনো সমস্যা হয় না।", "Eating light fast food once a week generally does not cause major body issues."),
    ("অতিরিক্ত ভাজা পোড়া খাবার খেলে পেটে সামান্য গ্যাস বা অস্বস্তি অনুভূত হতে পারে।", "Eating too much fried food may cause slight gas or discomfort in the stomach."),
    ("খাবার সবসময় পরিষ্কার ও স্বাস্থ্যকর পরিবেশে তৈরি করা দরকার।", "Food should always be prepared in a clean and hygienic environment."),
    ("আমাদের প্রতিদিনের খাদ্যাভ্যাসে তেলের পরিমাণ কম রাখা শরীরের জন্য খুবই ভালো।", "Keeping the amount of oil low in our daily diet is very good for the body."),
    ("রেস্তোরাঁর খাবারে অনেক সময় ভালো মানের তেল ব্যবহার করা হয় না।", "Restaurants often do not use good quality oil in their food."),
    ("স্বাস্থ্যকর জীবনধারা বজায় রাখতে প্রতিদিন নিয়ম করে হাঁটার অভ্যাস করা উচিত।", "To maintain a healthy lifestyle , one should make a habit of walking regularly every day."),
    ("আমি বিকেলের নাস্তায় তেল ছাড়া সেদ্ধ চানাচুর বা মুড়ি খেতে স্বাচ্ছন্দ্য বোধ করি।", "I feel comfortable eating boiled chickpeas or puffed rice without oil for afternoon snacks."),
    ("বাইরের খাবারে কৃত্রিম মসলা ও সোডিয়াম বেশি থাকায় তৃষ্ণা একটু বেশি পায়।", "Because outer food contains more artificial spices and sodium , thirst increases slightly."),
    ("স্বাস্থ্য সচেতন মানুষ সবসময় প্রক্রিয়াজাত খাবার এড়িয়ে চলার চেষ্টা করেন।", "Health-conscious people always try to avoid processed foods."),
    ("টিনজাত এবং প্রক্রিয়াজাত খাবারের মেয়াদ দেখে কেনা অত্যন্ত জরুরি।", "It is extremely important to check the expiration date when buying canned and processed foods."),
    ("আমাদের বাড়ির খাবার অনেক সুস্বাদু এবং পুষ্টিকর হয়।", "Our home food is very delicious and nutritious."),
    ("খাবারে অতিরিক্ত চিনি ব্যবহার করলে মেদ বাড়ার সম্ভাবনা থেকে যায়।", "Using excess sugar in food leaves a possibility of gaining fat."),
    ("ছোটবেলা থেকেই সঠিক খাবারের অভ্যাস তৈরি করা বাবা-মায়ের দায়িত্ব।", "Developing correct food habits from childhood is the responsibility of parents."),
    ("দুপুরের খাবারে বেশি তেলযুক্ত মাছ বা মাংস এড়িয়ে চলাই বুদ্ধিমানের কাজ।", "It is wise to avoid greasy fish or meat during lunch."),
    ("হালকা এবং তাজা খাবার আমাদের শরীরকে দিনভর সতেজ রাখতে সাহায্য করে।", "Light and fresh food helps keep our body refreshed throughout the day.")
]

nr = [
    ("নাক থেকে রক্ত পড়া শুরু হলে সোজা হয়ে বসে নাকের ডগা চেপে ধরুন।", "If a nosebleed starts , sit up straight and pinch the tip of the nose."),
    ("চোখের পাতা ঘন ঘন কাঁপলে পর্যাপ্ত ঘুমানো এবং স্ক্রিন থেকে দূরে থাকা দরকার।", "If the eyelid twitches frequently , it is necessary to sleep adequately and stay away from screens."),
    ("বুকের মাঝখানে বা বাম পাশে তীব্র ব্যথা হলে সাথে সাথে জরুরি বিভাগে যোগাযোগ করুন।", "If there is severe pain in the middle or left side of the chest , contact the emergency department immediately."),
    ("দাঁত শিরশির করলে ঠাণ্ডা ও গরম খাবার এড়িয়ে চলুন এবং দাঁতের ডাক্তারের সাথে পরামর্শ করুন।", "If teeth tingle , avoid cold and hot foods and consult a dentist."),
    ("সকালে উঠে কোমর ব্যথা হলে সঠিক ভঙ্গিতে ঘুমানোর চেষ্টা করুন এবং ভারী কাজ এড়িয়ে চলুন।", "If waist pain occurs after waking in the morning , try to sleep in proper posture and avoid heavy work."),
    ("মূত্রত্যাগের পর অস্বস্তি হলে দিনে অন্তত তিন থেকে চার লিটার পানি পান করা আবশ্যক।", "If discomfort occurs after urination , it is mandatory to drink at least three to four liters of water daily."),
    ("দেহে পানিশূন্যতা দেখা দিলে মাথা ব্যথা এবং কিডনিতে সমস্যা হতে পারে।", "If dehydration occurs in the body , headaches and kidney issues can happen."),
    ("কাশি বেশ কিছুদিন ধরে থাকলে ডাক্তারের কাছে গিয়ে বুকের এক্স-রে করানো ভালো।", "If cough persists for quite a few days , it is good to go to a doctor and get a chest X-ray."),
    ("সর্দিকাশি দ্রুত কমাতে গরম ভাপ বা স্টিম নিন এবং ঈষদুষ্ণ পানি পান করুন।", "To quickly reduce a cold , take hot steam and drink lukewarm water."),
    ("প্রোটিনের জন্য প্রতিদিন ডাল , পনীরের তরকারি এবং ভেজানো বাদাম খাওয়া স্বাস্থ্যকর।", "For protein , eating lentils , cottage cheese curry and soaked nuts daily is healthy."),
    ("চোখে ধুলাবালি পড়লে পরিষ্কার পানি দিয়ে চোখ ভালো করে ধুয়ে ফেলুন।", "If dust falls in the eye , wash the eye thoroughly with clean water."),
    ("দাঁত ক্ষয় রোধ করতে রাতে ঘুমানোর আগে অবশ্যই দাঁত ব্রাশ করা দরকার।", "To prevent tooth decay , it is definitely necessary to brush teeth before going to sleep at night."),
    ("পিঠের তীব্র ব্যথার জন্য ফিজিওথেরাপিস্টের দেখানো ব্যায়াম নিয়মিত অনুশীলন করা উচিত।", "For severe back pain , exercises shown by a physiotherapist should be practiced regularly."),
    ("হঠাৎ রক্তচাপ আশঙ্কাজনকভাবে বেড়ে গেলে দ্রুত চিকিৎসকের কাছে যেতে হবে।", "If blood pressure suddenly rises alarmingly , one must quickly go to a doctor."),
    ("মূত্রনালীর প্রদাহ এড়াতে সুতি কাপড়ের পোশাক পরা এবং পরিচ্ছন্ন থাকা দরকার।", "To avoid urinary tract inflammation , it is necessary to wear cotton clothes and stay clean."),
    ("পানি কম খেলে শরীর দুর্বল লাগে এবং কোষ্ঠকাঠিন্যের সমস্যা স্থায়ী হতে পারে।", "Drinking less water makes the body feel weak and constipation issues may become permanent."),
    ("গলার খুশখুশে ভাব দূর করতে মধু ও লেবুর রস একসাথে মিশিয়ে খান।", "To remove throat tickle , mix honey and lemon juice together and eat."),
    ("ঠাণ্ডা লাগলে হালকা গরম পানিতে দুই ফোঁটা ইউক্যালিপটাস তেল দিয়ে ভাপ নিলে আরাম মিলবে।", "If you catch a cold , taking steam in lukewarm water with two drops of eucalyptus oil brings relief."),
    ("নিরামিষ খাদ্যে পর্যাপ্ত প্রোটিন পেতে সয়াবিন ও তোফু বেশ উপকারী খাদ্য।", "To get adequate protein in a vegetarian diet , soybeans and tofu are very useful foods."),
    ("চোখের দৃষ্টিশক্তি ভালো রাখতে প্রতিদিন গাজর ও শাকসবজি খাওয়া উচিত।", "To keep eye vision good , carrots and vegetables should be eaten daily.")
]
