# Prompt 5 Data
# Prompt 5 (Headache): "সকালে ঘুম থেকে উঠেই মাথা ব্যাথা শুরু হয়ে গেছে , এখন কি করা উচিত আমার ?"
# HR: 24, PR: 26, NR: 20

p5_hr = [
    ("সকালে ঘুম থেকে উঠে মাথা ব্যথা হলে এক গ্লাস ইষদুষ্ণ পানি পান করুন এবং নীরব ঘরে চোখ বন্ধ করে ১০-১৫ মিনিট বিশ্রাম নিন", "If you wake up with a headache in the morning , drink a glass of lukewarm water and rest with your eyes closed in a quiet room for 10-15 minutes"),
    ("ঘুমের ঘাটতি বা পানিশূন্যতার কারণে সকালে মাথা ব্যথা হতে পারে , তাই পর্যাপ্ত পানি খেয়ে কিছুক্ষণ শান্ত থাকুন", "Morning headache can occur due to lack of sleep or dehydration , so drink enough water and stay calm for a while"),
    ("কপালে ও ঘাড়ে ঠাণ্ডা বরফের প্যাক বা হালকা গরম সেঁক দিলে সকালের মাথা ব্যথা থেকে দ্রুত আরাম মিলবে", "Applying a cold ice pack or warm compress to forehead and neck will bring quick relief from morning headache"),
    ("চোখের সমস্যা বা চশমার পাওয়ার পরিবর্তনের কারণে সকালে মাথা ব্যথা হলে একজন আই স্পেশালিস্ট দেখান", "Consult an eye specialist if morning headache is due to eye problems or changes in glasses prescription"),
    ("উচ্চ রক্তচাপের কারণে সকালে ঘুম ভাঙার পর মাথা ব্যথা হতে পারে , তাই রক্তের চাপ মেপে নিশ্চিত হন", "Morning headache after waking up can happen due to high blood pressure , so check your blood pressure to be sure"),
    ("মাইগ্রেন বা সাইনুসাইটিসের কারণে সকালে মাথা ব্যথা হলে ডাক্তারের পরামর্শ অনুযায়ী নির্দিষ্ট ব্যথানাশক বা প্যারাসিটামল সেবন করতে পারেন", "If morning headache is caused by migraine or sinusitis , you can take specific painkiller or paracetamol on doctor's advice"),
    ("সকালে চা বা ক্যাফেইন খাওয়ার অভ্যাস থাকলে এক কাপ হালকা গরম লবঙ্গ ও আদা চা পান করুন", "If you have a habit of morning tea or caffeine , drink a cup of warm clove and ginger tea"),
    ("মাথা ব্যথা কমানোর জন্য ল্যাভেন্ডার বা পুদিনা পাতা গুঁড়ো করে কপালে হালকা বাম ম্যাসাজ করুন", "Massage light balm with crushed lavender or mint leaves on the forehead to reduce headache"),
    ("সকালে উঠে মাথা ব্যথা এড়াতে অতিরিক্ত আলো বা উজ্জ্বল ডিজিটাল স্ক্রিন দেখা থেকে সাময়িক বিরত থাকুন", "Temporarily refrain from looking at harsh lights or bright digital screens to avoid worsening morning headache"),
    ("মানসিক স্ট্রেস কমাতে গভীর শ্বাস-প্রশ্বাসের ব্যায়াম এবং ধ্যানের মাধ্যমে সকালের মাথা ব্যথা শান্ত করার চেষ্টা করুন", "Try to calm morning headache through deep breathing exercises and meditation to reduce mental stress"),
    ("সকালে খালি পেটে অতিরিক্ত গ্যাস্ট্রিক বা এসিডিটি হলেও মাথা ব্যথা করতে পারে , তাই হালকা কিছু খেয়ে এন্টাসিড নিন", "Excess gastric or acidity on an empty stomach in the morning can also cause headache , so take an antacid after eating something light"),
    ("সকালে উঠেই মাথা ব্যথার সাথে বমি বমি ভাব থাকলে চিকিৎসকের পরামর্শে অ্যান্টি-এমেটিক ওষুধ সেবন করতে পারেন", "If there is nausea along with morning headache upon waking up , take anti-emetic medication on doctor's advice"),
    ("নিয়মিত সকালে মাথা ব্যথা হওয়া স্লিপ অ্যাপনিয়া বা ঘুমের মধ্যে শ্বাসকষ্টের লক্ষণ হতে পারে , তাই স্নায়ুরোগ বিশেষজ্ঞের পরামর্শ নেওয়া জরুরি", "Regular morning headaches can be a sign of sleep apnea or breathing difficulty during sleep , so consulting a neurologist is essential"),
    ("শোয়ার ঘরের তাপমাত্রা ও বায়ু চলাচল ঠিক না থাকলে সকালে মাথা ব্যথা হতে পারে , তাই ঘর বাতাসযুক্ত রাখুন", "Improper room temperature and ventilation can cause morning headache , so keep the room well ventilated"),
    ("সকালে মাথা ব্যথার জন্য কপাল ও রগের দুই পাশে বৃদ্ধাঙ্গুলি দিয়ে আলতো করে গোল গোল ঘুরিয়ে ম্যাসাজ করুন", "Gently massage the forehead and sides of temples in circular motions with thumbs for morning headache"),
    ("সকালে নাস্তা না করে দীর্ঘক্ষণ না খেয়ে থাকলে ব্লাড সুগার কমে মাথা ব্যথা বাড়ে , তাই পুষ্টিকর নাস্তা খেয়ে নিন", "Skipping morning breakfast and fasting long lowers blood sugar and increases headache , so eat a nutritious breakfast"),
    ("সকালের তীব্র মাথা ব্যথা কমাতে মাথায় ভিজে ঠাণ্ডা গামছা দিয়ে কিছুক্ষণ জড়াইয়ে রাখুন", "Wrap a cold wet towel around your head for a while to reduce severe morning headache"),
    ("দাঁত কামড়ানোর অভ্যাস বা চোয়ালের সমস্যার কারণে সকালে মাথা ব্যথা হলে ডেন্টিস্টের মতামত নিন", "Get a dentist's opinion if morning headache is due to teeth grinding habits or jaw problems"),
    ("সকালে মাথা ব্যথার সাথে ঘাড় শক্ত হয়ে গেলে অবহেলা না করে দ্রুত হাসপাতালে জরুরী চিকিৎসা নিন", "If morning headache is accompanied by a stiff neck , do not neglect it and seek emergency medical treatment at a hospital quickly"),
    ("যদি প্রতিদিন সকালে ঘুম থেকে উঠেই মাথা ব্যথা হয় , তবে কোনো বড় নিউরোলজিক্যাল সমস্যা আছে কিনা পরীক্ষা করান", "If you wake up with a headache every morning , get tested to see if there is any major neurological issue"),
    ("সকালে উঠে মাথা ব্যথা কমাতে এক গ্লাস লেবুর রসে সামান্য মধু মিশিয়ে ইষদুষ্ণ পানি পান করুন", "Drink lukewarm water mixed with a glass of lemon juice and a little honey to reduce morning headache upon waking up"),
    ("সকালে অতিরিক্ত কফি বা অ্যালকোহলের প্রভাবে মাথা ব্যথা হলে প্রচুর পানি খেয়ে বিশ্রাম নেওয়া উত্তম", "If headache occurs in the morning due to excess coffee or alcohol hangover , it is best to drink plenty of water and rest"),
    ("মাথা ব্যাথা কমাতে মাথার ত্বকে হালকা গরম নারিকেল বা বাদাম তেল দিয়ে ম্যাসাজ করতে পারেন", "You can massage the scalp with warm coconut or almond oil to reduce headache"),
    ("সকালে মাথা ব্যথা হলে ধূমপান ও অতিরিক্ত কোলাহলযুক্ত পরিবেশ পুরোপুরি এড়িয়ে চলুন", "Completely avoid smoking and excessively noisy environments if you have a morning headache")
]

p5_pr = [
    ("সকালে উঠে এক কাপ গরম চা খেলে মনটা বেশ সতেজ লাগে", "Drinking a cup of hot tea after waking up in the morning feels quite refreshing"),
    ("মাথা ব্যথা হলে সারাদিনের কাজের মনোযোগ সম্পূর্ণ নষ্ট হয়ে যায়", "Having a headache completely ruins focus for the entire day's work"),
    ("নিয়মিত রাতে ৮ ঘণ্টা ঘুম নিশ্চিত করা শারীরিক সুস্থতার জন্য প্রয়োজন", "Ensuring regular 8 hours of sleep at night is necessary for physical well-being"),
    ("সকালে হাঁটার অভ্যাস থাকলে শরীর ও মন দুটোই চাঙ্গা থাকে", "Habit of morning walk keeps both body and mind active"),
    ("মাথা ব্যথার জন্য অতিরিক্ত ওষুধ খাওয়া লিভারের জন্য ক্ষতিকর হতে পারে", "Taking excess painkillers for headaches can be harmful to the liver"),
    ("আমার এক সহকর্মীর প্রায়ই সকালে ঘুম থেকে ওঠার পর মাথা ব্যথার সমস্যা হতো", "A colleague of mine often had morning headaches after waking up"),
    ("অফিসের কাজের চাপ বেশি থাকলে রাতে ভালো ঘুম হতে চায় না", "High office work pressure prevents good sleep at night"),
    ("সকালে হালকা রোদে বসলে শরীরে পর্যাপ্ত ভিটামিন ডি পাওয়া যায়", "Sitting in mild morning sunlight provides adequate vitamin D to the body"),
    ("মাথা ব্যথার কারণ খুঁজে বের করতে একটি স্বাস্থ্য ডায়েরি বজায় রাখা ভালো", "Keeping a health diary is good for finding out headache causes"),
    ("চোখের যত্ন নিতে একটানা কম্পিউটারের দিকে তাকিয়ে থাকা বন্ধ করুন", "Stop staring at computers continuously to take care of eyes"),
    ("সকালের শান্ত পরিবেশ মানসিক প্রশান্তি ও ভালো মেজাজ বজায় রাখতে সাহায্য করে", "Quiet morning atmosphere helps maintain mental peace and good mood"),
    ("মাথা ব্যাথা হলে ভারী কাজ না করে আরাম করা উচিত", "When having a headache one should rest instead of doing heavy work"),
    ("শীতের সকালে হালকা গরম পানিতে গোসল করলে শরীর হালকা মনে হয়", "Taking a bath in lukewarm water on a winter morning makes body feel light"),
    ("সকালে সময়মত নাস্তা করা স্বাস্থ্যের জন্য একটি অত্যন্ত ভালো অভ্যাস", "Eating breakfast on time in the morning is a very good habit for health"),
    ("মাথা ঘোরানোর সাথে মাথা ব্যথা থাকলে সাবধানে চলাফেরা করা দরকার", "One needs to move carefully if dizziness accompanies headache"),
    ("শোবার ঘরে হালকা ও মিষ্টি সুবাস ছড়িয়ে দিলে ঘুম ভালো হয়", "Spreading light and sweet fragrance in the bedroom promotes good sleep"),
    ("সকালে মোবাইল ফোনের অ্যালার্মে হঠাৎ জেগে উঠলে মাথা ঝিমঝিম করতে পারে", "Waking up suddenly to a mobile alarm in the morning can cause dizziness"),
    ("সুস্থ ও সুন্দর জীবনের জন্য নিয়ম মেনে জীবনযাপন করা জরুরী", "Living a disciplined life is important for a healthy and beautiful life"),
    ("মাথা ব্যথার জন্য মাথায় ঠান্ডা পানি ঢাললে সাময়িক আরাম পাওয়া যায়", "Pouring cold water on head brings temporary relief for headache"),
    ("বেশি চিন্তা করলে মাথার রগ ফুলে মাথা ব্যথা হতে পারে", "Overthinking can cause head veins to swell and lead to headache"),
    ("সকালে উঠেই গান শুনলে অনেকের মন ও শরীর সতেজ থাকে", "Listening to music upon waking up keeps many people's mind and body fresh"),
    ("মাথা ব্যথার প্রাকৃতিক প্রতিকার হিসেবে বিভিন্ন ভেষজ চা জনপ্রিয়", "Various herbal teas are popular as natural remedies for headaches"),
    ("শরীরের প্রয়োজনীয় পানির অভাব হলে বিভিন্ন শারীরিক উপসর্গ দেখা দেয়", "Dehydration leads to various physical symptoms in the body"),
    ("বালিশের উচ্চতা সঠিক না হলে ঘাড়ে ব্যথা ও মাথা ব্যথা হতে পারে", "Incorrect pillow height can cause neck pain and headache"),
    ("সকালে নিয়মিত হালকা যোগব্যায়াম করলে সারা দিন ভালো কাটে", "Doing light yoga regularly in the morning makes the whole day go well"),
    ("মাথা ব্যথার প্রকোপ কমাতে পুষ্টিকর তাজা ফলমূল খাওয়া উচিত", "Fresh nutritious fruits should be eaten to reduce headache intensity")
]

p5_nr = [
    ("পায়ের আঙুলে রক্ত চলাচল স্বাভাবিক রাখতে গরম পানিতে পা ডুবিয়ে রাখুন", "Soak feet in warm water to keep blood circulation normal in toes"),
    ("রাতে বারবার প্রস্রাবের সমস্যা হলে ঘুমানোর ২ ঘণ্টা আগে পানি খাওয়া কম জানান", "Reduce drinking water 2 hours before bed if you have frequent nighttime urination"),
    ("খাবারের পর মুখে এসিডিটির জ্বালা হলে অতিরিক্ত মসলাযুক্ত খাবার বাদ দিন", "Avoid excessively spicy food if you experience acidity burning in mouth after meals"),
    ("গলায় কাঁটার মতো কিছু আটকে মনে হলে শুকনো ভাতের দলা গিলে চেষ্টা করুন", "Try swallowing a lump of dry rice if you feel something stuck like a thorn in throat"),
    ("হাঁটুর জোড়ায় তীব্র ব্যথা থাকলে ডাক্তারের পরামর্শে ফিজিওথেরাপি চিকিৎসা নিন", "Take physiotherapy treatment on doctor's advice if there is severe pain in knee joints"),
    ("দাঁতের মাড়ি ফোলা ও রক্ত পড়া রোধে ভালো টুথপেস্ট ব্যবহার করা প্রয়োজন", "Good toothpaste needs to be used to prevent gum swelling and bleeding"),
    ("পিঠের ব্যথা কাটাতে শক্ত বিছানায় শোওয়া ও সঠিক সোজা ভঙ্গিতে বসা দরকার", "Sleeping on a firm bed and sitting in correct upright posture are needed for back pain"),
    ("কানের ভেতরের ইনফেকশন ও পুঁজ অপসারণ করতে নাক-কান-গলা ডাক্তার দেখান", "Consult an ENT doctor to remove inner ear infection and pus"),
    ("ত্বকে এলার্জির চুলকানি ও র্যাশ দেখা দিলে সাবান ব্যবহার বন্ধ করুন", "Stop using soap if allergic itching and rashes appear on skin"),
    ("পায়ের গোড়ালি ফেটে গেলে প্রতি রাতে নিয়মিত ভ্যাসলিন লাগান", "Apply vaseline regularly every night if heels crack"),
    ("বুকে জমে থাকা ঘন কফ বের করতে গরম পানির ভাপ বা স্টিম নিন", "Take warm water steam to clear thick phlegm accumulated in chest"),
    ("হাতের কড়াইতে ফুসকুড়ি উঠলে ডাক্তারের পরামর্শে লোশন ব্যবহার করুন", "Use lotion on doctor's advice if rashes appear on finger knuckles"),
    ("কোমর ব্যথা কমাতে প্রতিদিন কিছু হালকা কোমর স্ট্র্যাচিং ব্যায়াম করুন", "Do some light waist stretching exercises daily to reduce back pain"),
    ("নাকের এলার্জি ও অনবরত হাঁচি এড়াতে ধুলোবালি ও ধোঁয়া থেকে বাঁচুন", "Stay away from dust and smoke to avoid nasal allergy and continuous sneezing"),
    ("চোখে অ্যালার্জি বা লালচে ভাব হলে ঠান্ডা পরিষ্কার পানি দিয়ে ধুয়ে নিন", "Wash with cold clean water if eyes get allergic or red"),
    ("শরীরে পানির ঘাটতি কাটাতে প্রচুর ওরসেলাইন ও ডাবের পানি পান করুন", "Drink plenty of ORS and coconut water to overcome body dehydration"),
    ("চুলের গোড়া মজবুত করতে নারিকেল তেলের সাথে পেঁয়াজের রস মিশিয়ে মাখুন", "Mix onion juice with coconut oil and apply to strengthen hair roots"),
    ("কনুইয়ের ত্বক শুষ্ক ও খসখসে হয়ে গেলে কোল্ড ক্রিম ব্যবহার করুন", "Use cold cream if elbow skin becomes dry and rough"),
    ("পা মুচকে ফুলেই রক্ত জমে গেলে বরফের সেঁক দেওয়া অত্যন্ত দরকার", "Applying ice packs is very necessary if foot twists and swells with blood clot"),
    ("মাড়ির দুর্গন্ধ কাটাতে দিনে দুইবার দাঁত ব্রাশ ও ফ্লসিং করুন", "Brush and floss teeth twice daily to eliminate gum odor")
]

print("P5 count:", len(p5_hr), len(p5_pr), len(p5_nr))
