# Prompt 5: বুকের বাম পাশে ব্যাথা করে সবসময় , মনে হয় চাপ দিয়ে ধরে রেখেছে কেউ , কি করা উচিৎ / I have constant pain on the left side of my chest, it feels like someone is pressing on it, what should I do?
# HR=14, PR=14, NR=14

g_bn = "হ্যার্ট জনিত সমস্যা"
g_en = "Heart problems"
p_bn = "বুকের বাম পাশে ব্যাথা করে সবসময় , মনে হয় চাপ দিয়ে ধরে রেখেছে কেউ , কি করা উচিৎ"
p_en = "I have constant pain on the left side of my chest, it feels like someone is pressing on it, what should I do?"

hr = [
    ("বুকের বাম পাশে ক্রমাগত চাপধরা ব্যথা হৃদরোগের লক্ষণ হতে পারে , তাই অবিলম্বে কার্ডিওালজিস্ট দেখান এবং ইসিজি করান।", "Constant pressing pain on left side of chest can be a symptom of heart disease , so see a cardiologist immediately and get an ECG done."),
    ("এই ধরণের বুকে চাপ এবং ব্যথা হলে কোনো শারীরিক পরিশ্রম না করে দ্রুত নিকটস্থ হাসপাতালের জরুরি বিভাগে যান।", "If this type of chest pressure and pain occurs , go to emergency department of nearest hospital quickly without physical exertion."),
    ("ব্যথার সাথে যদি বাম হাত , ঘাড় বা চোয়ালে ব্যথা ছড়ায় এবং প্রচণ্ড ঘাম হয় , তবে এটি হার্ট অ্যাটাকের লক্ষণ হতে পারে।", "If pain spreads to left arm , neck or jaw along with pain and excessive sweating occurs , it could be a sign of heart attack."),
    ("উচ্চ রক্তচাপ বা ডায়াবেটিস থাকলে বুকের এ ধরণের চাপকে কোনোভাবেই অবহেলা করা উচিত নয় এবং দ্রুত ডাক্তারের পরামর্শ নেওয়া দরকার।", "If you have high blood pressure or diabetes , this kind of chest pressure should never be neglected and doctor's advice is needed quickly."),
    ("বুকের বাম পাশে তীব্র অস্বস্তি হলে জিহ্বার নিচে রাখা যায় এমন নাইট্রোট্যাব ব্যবহারের জন্য জরুরি ডাক্তারের সাহায্য নিন।", "If severe discomfort occurs on left side of chest , seek emergency doctor help for using nitrotab that can be placed under tongue."),
    ("হৃদযন্ত্রের সমস্যা নিশ্চিত হতে কালক্ষেপণ না করে দ্রুত ট্রপোনিন-আই রক্ত পরীক্ষা এবং ইসিজি করিয়ে নেওয়া আবশ্যক।", "To confirm heart issues , getting a Troponin-I blood test and ECG done quickly without wasting time is mandatory."),
    ("বুকে অতিরিক্ত চাপ অনুভব করলে সোজা হয়ে বিশ্রাম নিন , টাইট পোশাক ঢিলে করুন এবং সাথে সাথে অ্যাম্বুলেন্স ডাকুন।", "If extra chest pressure is felt , rest straight , loosen tight clothing and call an ambulance immediately."),
    ("ক্রমাগত বুকের বাম পাশে ব্যথা হলে একজন হৃদরোগ বিশেষজ্ঞের অধীনে ইকোকার্ডিওগ্রাম ও টিএমএক্স পরীক্ষা করানো দরকার।", "If there is constant pain on left side of chest , getting an echocardiogram and TMX test under a cardiologist is needed."),
    ("বুকে চাপের সাথে শ্বাসকষ্ট এবং মাথা ঘোরা দেখা দিলে রোগীকে দ্রুত অক্সিজেন সহায়তা দিতে হাসপাতালে নেওয়া জরুরি।", "If shortness of breath and dizziness appear with chest pressure , taking patient to hospital quickly to provide oxygen support is urgent."),
    ("ধূমপানের অভ্যাস থাকলে বা কোলেস্টেরল বেশি থাকলে বুকের বাম পাশের এ ধরণের চাপ ধরা ব্যথায় অবহেলা করা বিপজ্জনক।", "If you have a smoking habit or high cholesterol , neglecting this kind of pressing pain on left side of chest is dangerous."),
    ("বুকের ব্যথা বাম বাহুতে ছড়িয়ে পড়লে অনতিবিলম্বে কার্ডিয়াক সিসিইউ সুবিধাযুক্ত হাসপাতালে যোগাযোগ করা উচিত।", "If chest pain spreads to left arm , contact a hospital with cardiac CCU facility immediately."),
    ("বুকের মাঝখান বা বাম পাশের ভারি ভাব কমায় এমন জরুরি হার্টের ওষুধ ডাক্তারের পরামর্শ ছাড়া খাওয়া যাবে না।", "Emergency heart medicine that reduces heavy feeling in middle or left side of chest should not be taken without doctor's advice."),
    ("পারিবারিক হৃদরোগের ইতিহাস থাকলে বুকের বাম পাশের постоян চাপ ধরা ব্যথা গুরুত্ব সহকারে পরীক্ষা করা আবশ্যক।", "If there is a family history of heart disease , constant pressing pain on left side of chest must be examined seriously."),
    ("লক্ষণ দেখা দেওয়ার সাথে সাথে রোগীকে শান্ত রেখে অতি দ্রুত হৃদরোগ ক্লিনিকে নিয়ে যাওয়া জীবন রক্ষাকারী হতে পারে।", "Keeping patient calm as soon as symptoms appear and taking them very quickly to a heart clinic can be life-saving.")
]

pr = [
    ("খাবার খাওয়ার পর পেটে অতিরিক্ত গ্যাস জমে বুক জ্বালাপোড়া এবং অস্বস্তি হতে পারে।", "After eating food , excess gas accumulating in stomach can cause heartburn and discomfort."),
    ("বুকের পেশীতে হঠাৎ টান লাগলে বা ভারী জিনিস তুললে সামান্য ব্যথা অনুভব হতে পারে।", "If chest muscles suddenly get strained or heavy objects are lifted , slight pain can be felt."),
    ("অতিরিক্ত মানসিক চিন্তা এবং দুশ্চিন্তার কারণে প্যানিক অ্যাটাক হয়ে বুকে ধড়ফড় করতে পারে।", "Due to excessive mental worry and anxiety , panic attack can occur causing heart palpitations."),
    ("পাজরের হাড়ে বা কার্টিলেজে প্রদাহ হলে বুক স্পর্শ করলে বা কাশার সময় ব্যথা বাড়ে।", "If there is inflammation in rib bones or cartilage , pain increases when touching chest or coughing."),
    ("আমার এক পরিচিত ব্যক্তি গ্যাস্ট্রিকের ওষুধ খেয়ে বুকের ব্যথা কমে গেছে বলে জানিয়েছিলেন।", "An acquaintance of mine informed that chest pain reduced after taking gastric medicine."),
    ("প্রতিদিন সকালে নিয়ম করে হাঁটাহাঁটি করলে শরীরের রক্ত সঞ্চালন ভালো থাকে।", "Walking regularly every morning keeps blood circulation in body good."),
    ("যেকোনো ধরণের বুক ব্যথায় ভীতি না পেয়ে শান্ত থাকা এবং পরিবেশ ঠাণ্ডা রাখা দরকার।", "In any type of chest pain , one should stay calm without panicking and keep environment cool."),
    ("তৈলাক্ত ও মশলাদার খাবার খেলে অনেক সময় বুকে অস্বস্তি এবং টক ঢেকুর ওঠে।", "Eating oily and spicy food often causes discomfort in chest and sour belching."),
    ("মেরুদণ্ডের বা পিঠের ব্যথার ভাব অনেক সময় বুকের দিকে ছড়িয়ে পড়তে পারে।", "Spine or back pain feeling can often spread towards the chest."),
    ("ফুসফুসের সাধারণ সংক্রমণের কারণেও বুক ভারী লাগতে পারে এবং কাশি হতে পারে।", "Due to general lung infection also , chest may feel heavy and cough can occur."),
    ("বয়স্ক মানুষের শরীর খারাপ লাগলে সবসময় পরিবারের সদস্যদের সাথে নিয়ে হাসপাতালে যাওয়া উচিত।", "When elderly people feel unwell , they should always go to hospital with family members."),
    ("নিয়মিত ব্লাড প্রেসার মেপে একটা খাতায় লিখে রাখা চিকিৎসার জন্য সুবিধাজনক।", "Measuring blood pressure regularly and writing it in a notebook is convenient for treatment."),
    ("ঠাণ্ডা লাগলে বুকের ভেতর কফ জমে হালকা ব্যথা ও চাপ অনুভূত হওয়া অস্বাভাবিক নয়।", "If catching a cold , phlegm accumulating inside chest causing slight pain and pressure is not unusual."),
    ("স্বাস্থ্যকর জীবনধারা বজায় রাখলে হৃদরোগসহ অন্যান্য শারীরিক জটিলতা এড়ানো যায়।", "Maintaining a healthy lifestyle helps avoid heart disease and other physical complications.")
]

nr = [
    ("নাক থেকে হঠাৎ রক্ত পড়লে মাথা নিচু করে নাকের নরম অংশ ১০ মিনিট চেপে রাখুন।", "If blood suddenly falls from nose , tilt head low and pinch soft part of nose for 10 minutes."),
    ("চোখের পাতা কাঁপলে স্ক্রিন টাইম কমান এবং রাতে পর্যাপ্ত ঘুমানোর চেষ্টা করুন।", "If eyelid twitches , reduce screen time and try to sleep adequately at night."),
    ("দাঁতে শিরশিরানি থাকলে সংবেদনশীল দাঁতের পেস্ট ব্যবহার করুন এবং মিষ্টি কম খান।", "If there is tooth sensitivity , use sensitive tooth paste and eat less sweets."),
    ("সকালে উঠে পিঠ ও কোমর ব্যথা হলে সঠিক ভঙ্গিতে ঘুম থেকে ওঠার অভ্যাস করুন।", "If back and waist pain occurs after waking up in morning , habituate getting up in correct posture."),
    ("মূত্রত্যাগের পর ঝিনঝিন করলে বেশি করে পানি পান করুন এবং ব্যক্তিগত স্বাস্থ্যবিধি মানুন।", "If tingling occurs after urination , drink more water and observe personal hygiene."),
    ("নিরামিষ খাদ্যে প্রোটিনের উৎস হিসেবে ছোলার ডাল , তোফু এবং পনির আদর্শ খাবার।", "As protein source in vegetarian diet , chana dal , tofu and cottage cheese are ideal foods."),
    ("জাঙ্ক ফুড অতিরিক্ত খেলে স্থূলতা এবং লিভারে চর্বি জমার ঝুঁকি বৃদ্ধি পায়।", "Eating excess junk food increases risk of obesity and fat accumulation in liver."),
    ("পানি কম খেলে ডিহাইড্রেশন , কোষ্ঠকাঠিন্য এবং কিডনিতে পাথর হওয়ার ঝুঁকি বাড়ে।", "Drinking less water increases risk of dehydration , constipation and kidney stones."),
    ("কাশি দীর্ঘস্থায়ী হলে কফ পরীক্ষা ও বুকের এক্স-রে করানো অত্যন্ত প্রয়োজন।", "If cough is persistent , phlegm test and chest X-ray are extremely needed."),
    ("সর্দিকাশি হলে লবঙ্গ ও আদা চা পান করলে গলার কষ্ট দ্রুত কমে যায়।", "If having cold , drinking clove and ginger tea quickly reduces throat discomfort."),
    ("পায়ের থাইয়ের পেশীতে টান লাগলে গরম পানির সেঁক দিলে স্বস্তি মিলবে।", "If muscle cramp occurs in leg thigh , applying warm water compress brings relief."),
    ("ত্বকের চুলকানি ও অ্যালার্জি কমাতে চিকিৎসকের পরামর্শে অ্যান্টিহিস্টামিন খান।", "To reduce skin itching and allergy , take antihistamines on doctor's advice."),
    ("চুলের গোড়া শক্ত করতে নিয়মিত নারকেল তেল দিয়ে স্কাল্প ম্যাসাজ করা ভালো।", "To make hair roots strong , massaging scalp regularly with coconut oil is good."),
    ("কানের ভেতরের প্রদাহ কমাতে কানে পানি ঢোকা থেকে সবসময় সতর্ক থাকা দরকার।", "To reduce internal ear inflammation , always cautioning against water entering ear is needed.")
]
