# Prompt 6: দাঁত ক্ষয়ে গেছে হাল্কা শিরশির করে কিন্তু ব্যথা নেই , কি করব / My tooth has decayed, I have a slight tingling sensation but no pain, what should I do?
# HR=14, PR=14, NR=14

g_bn = "দাঁতের সমস্যা"
g_en = "Dental problems"
p_bn = "দাঁত ক্ষয়ে গেছে হাল্কা শিরশির করে কিন্তু ব্যথা নেই , কি করব"
p_en = "My tooth has decayed, I have a slight tingling sensation but no pain, what should I do?"

hr = [
    ("দাঁতের ক্ষয় বাড়ার আগেই একজন ডেন্টিস্টের কাছে গিয়ে ফিলিং করিয়ে নিন এবং শিরশিরানি কমাতে সেনসেটিভ টুথপেস্ট ব্যবহার করুন।", "Get a filling done by visiting a dentist before tooth decay increases , and use sensitive toothpaste to reduce tingling."),
    ("অতিরিক্ত ঠান্ডা বা মিষ্টি খাবার ও পানীয় খাওয়া এড়িয়ে চলুন এবং ফ্লোরাইডযুক্ত মাউথওয়াশ দিয়ে নিয়মিত কুলি করুন।", "Avoid eating extra cold or sweet foods and drinks , and gargle regularly with fluoride mouthwash."),
    ("নরম ব্রিসলের টুথব্রাশ দিয়ে আলতো করে দাঁত ব্রাশ করুন এবং ক্ষয়ে যাওয়া অংশে শক্ত খাবার চিবানো বন্ধ রাখুন।", "Brush teeth gently with a soft-bristle toothbrush and stop chewing hard food on decayed parts."),
    ("দাঁতের ক্ষয় যাতে স্নায়ু পর্যন্ত না পৌঁছায় , তার জন্য বিলম্ব না করে দ্রুত ফিলিং বা রেস্টোরেশন করানো উচিত।", "So that tooth decay does not reach the nerve , filling or restoration should be done quickly without delay."),
    ("খাবার খাওয়ার পর প্রতিবার হালকা গরম পানিতে লবণ মিশিয়ে কুলকুচি করলে দাঁতের শিরশির অনুভূতি হ্রাস পায়।", "Rinsing mouth with mild warm water mixed with salt every time after eating food reduces tooth tingling sensation."),
    ("ডেন্টিস্টের পরামর্শ নিয়ে এনামেল পুনর্গঠনে সাহায্যকারী ফ্লোরাইড জেল বা পেস্ট ব্যবহার করা বেশ কার্যকরী সমাধান।", "Taking dentist's advice and using fluoride gel or paste that helps rebuild enamel is a very effective solution."),
    ("ক্ষয়প্রাপ্ত দাঁতের যত্ন নিতে রাতে ঘুমানোর আগে এবং সকালে খাবারের পর সঠিক নিয়মে ফ্লোরাইড টুথপেস্ট দিয়ে দাঁত মাজুন।", "To care for decayed teeth , brush teeth with fluoride toothpaste in proper rules before sleeping at night and after food in morning."),
    ("অতিরিক্ত অম্লীয় বা এসিডিক খাবার যেমন লেবু ও কোল্ড ড্রিংকস খাওয়া কমান , কারণ এগুলো এনামেল ক্ষয় বাড়িয়ে দেয়।", "Reduce eating extra acidic foods like lemon and cold drinks , because these increase enamel decay."),
    ("ব্যথা না থাকলেও ক্ষয়িষ্ণু দাঁত অবহেলা করলে পরবর্তীতে রুট ক্যানেল চিকিৎসার প্রয়োজন হতে পারে , তাই এখনই ডেন্টিস্ট দেখান।", "Even if there is no pain , neglecting decaying tooth may require root canal treatment later , so see a dentist right now."),
    ("দাঁতের সংবেদনশীলতা ও ক্ষয় রোধে প্রতি ছয় মাস পর পর একজন দন্ত চিকিৎসকের কাছে গিয়ে দাঁত স্কেলিং ও চেকআপ করান।", "To prevent tooth sensitivity and decay , go to a dentist every six months for tooth scaling and checkup."),
    ("শিরশিরানি কমাতে পটাসিয়াম নাইট্রেট বা আরজিনিনযুক্ত বিশেষ টুথপেস্ট আঙুল দিয়ে ক্ষয়ে যাওয়া অংশে আলতো করে লাগিয়ে রাখুন।", "To reduce tingling , gently apply special toothpaste containing potassium nitrate or arginine on decayed area with finger."),
    ("দাঁতের ক্যাভিটি পরিষ্কার করে স্থায়ী ক্যাভিটি ফিলিং করালে ক্ষয় হওয়া বন্ধ হবে এবং শিরশির ভাব স্থায়ীভাবে দূর হবে।", "Cleaning tooth cavity and doing permanent cavity filling will stop decay and eliminate tingling permanently."),
    ("খাবার আটকে থাকলে দাঁতের ক্ষয় দ্রুত বাড়ে , তাই খাবারের পর ডেন্টাল ফ্লস ব্যবহার করে দাঁতের ফাঁক পরিষ্কার রাখুন।", "If food gets stuck , tooth decay increases rapidly , so use dental floss after food to keep teeth gaps clean."),
    ("মিষ্টি জাতীয় খাবার খাওয়ার পরপরই পানি দিয়ে মুখ ধুয়ে ফেললে দাঁতের ব্যাকটেরিয়া সংক্রমণ ও শিরশিরানি কমে।", "Washing mouth with water right after eating sweet food reduces tooth bacterial infection and tingling.")
]

pr = [
    ("দাঁত ও মাড়ি সুস্থ রাখতে প্রতিদিন রাতে ঘুমানোর আগে দাঁত ব্রাশ করার অভ্যাস গড়ে তোলা ভালো।", "To keep teeth and gums healthy , forming a habit of brushing teeth every night before sleeping is good."),
    ("আমার এক সহকর্মীর গত মাসে প্রচণ্ড দাঁত ব্যথা হওয়ায় তাকে দাঁত তুলে ফেলতে হয়েছিল।", "A colleague of mine had severe toothache last month and had to get a tooth extracted."),
    ("শিশুদের ক্ষেত্রে অতিরিক্ত চকলেট বা ক্যান্ডি খেলে খুব সহজেই দাঁতে পোকা লেগে ক্যাভিটি হয়।", "In case of children , eating excess chocolate or candy easily causes tooth decay and cavities."),
    ("দাঁত দিয়ে শক্ত কোনো কিছুর বোতলের মুখ খোলা দাঁতের স্বাস্থ্যের জন্য অত্যন্ত ক্ষতিকর।", "Opening bottle caps of hard things with teeth is extremely harmful for tooth health."),
    ("ক্যালসিয়াম এবং ভিটামিন ডি সমৃদ্ধ খাবার খেলে হাড়ের পাশাপাশি দাঁতের গঠনও মজবুত হয়।", "Eating foods rich in calcium and vitamin D strengthens tooth structure alongside bones."),
    ("আজকাল বাজারে দাঁতের চিকিৎসার জন্য উন্নতমানের প্রযুক্তি ও নানাবিধ উপকরণ পাওয়া যায়।", "Nowadays advanced technology and various materials are available in market for dental treatment."),
    ("অতিরিক্ত পান সুপারি ও জর্দা খেলে দাঁতের ছোপ ছোপ দাগ পড়ে এবং মাড়ির ক্ষতি হয়।", "Eating excess betel leaf , betel nut and jarda causes spotty stains on teeth and damages gums."),
    ("মুখের দুর্গন্ধ দূর করতে নিয়মিত জিভ পরিষ্কার করা এবং মাউথওয়াশ ব্যবহার করা উপকারী।", "To remove bad breath , cleaning tongue regularly and using mouthwash is beneficial."),
    ("অনেকে দাঁতের কোনো ছোটখাটো সমস্যা হলে প্রাথমিক অবস্থায় তেমন গুরুত্ব দিতে চান না।", "Many people do not want to give much importance in initial stages when any minor tooth issue happens."),
    ("দাঁতের মাড়ি থেকে রক্ত পড়লে ভিটামিন সি যুক্ত শাকসবজি ও ফলমূল বেশি করে খাওয়া ভালো।", "If bleeding occurs from tooth gums , eating more vitamin C rich vegetables and fruits is good."),
    ("আমি সকালে উঠে সবসময় কম ক্ষারযুক্ত টুথপেস্ট দিয়ে দাঁত পরিষ্কার করতে পছন্দ করি।", "I always prefer to clean teeth with low-alkaline toothpaste after waking up in morning."),
    ("দাঁতের সৌন্দর্য বজায় রাখতে সময়মতো ডেন্টিস্টের কাছে গিয়ে স্কেলিং করানো বেশ দরকার।", "To maintain dental beauty , going to a dentist on time for scaling is quite needed."),
    ("আকাঁচা বা অতিরিক্ত শক্ত খাবার চিবানোর সময় দাঁতে হঠাৎ চিড় ধরতে পারে।", "While chewing uncooked or extra hard food , sudden cracks can occur in teeth."),
    ("মাড়িতে কোনো ইনফেকশন বা ফোলা ভাব দেখা দিলে হালকা গরম পানি দিয়ে কুলি করা উচিত।", "If any infection or swelling appears in gums , gargling with mild warm water should be done.")
]

nr = [
    ("নাক থেকে রক্ত পড়লে মাথা সোজা রেখে নাকের ডগা আঙুল দিয়ে চাপ দিয়ে ধরুন।", "If blood flows from nose , keep head straight and press tip of nose with fingers."),
    ("চোখের পাতা ঘন ঘন কাঁপলে ল্যাপটপের ব্যবহার কমিয়ে পর্যাপ্ত বিশ্রাম নেওয়ার চেষ্টা করুন।", "If eyelid twitches frequently , try to reduce laptop use and take adequate rest."),
    ("বুকের বাম পাশে চাপ ধরা ব্যথা হলে কালক্ষেপণ না করে ইমার্জেন্সিতে গিয়ে ইসিজি করান।", "If there is pressing pain on left side of chest , go to emergency and get ECG done without delay."),
    ("সকালে উঠে কোমর ব্যথা হলে মেরুদণ্ড সোজা রেখে বসার ও ঘুমানোর অভ্যাস গড়ে তুলুন।", "If waist pain occurs after waking up in morning , form habit of sitting and sleeping keeping spine straight."),
    ("মূত্রত্যাগের পর ঝিনঝিন করলে বেশি করে পানি পান করুন এবং ইউটিআই পরীক্ষা করান।", "If tingling occurs after urination , drink more water and get UTI test done."),
    ("নিরামিষ খাদ্যে প্রোটিনের অভাব মেটাতে মসুর ডাল , তোফু এবং বাদাম নিয়মিত খান।", "To fulfill lack of protein in vegetarian diet , eat lentils , tofu and nuts regularly."),
    ("জাঙ্ক ফুড খাওয়া বন্ধ করলে শরীরের ওজন ও রক্তচাপ নিয়ন্ত্রণে রাখা সহজ হয়।", "Stopping eating junk food makes it easy to keep body weight and blood pressure in control."),
    ("শরীরে পানিশূন্যতা থাকলে কিডনিতে পাথর তৈরি হওয়ার ঝুঁকি বহুগুণ বেড়ে যায়।", "If dehydration exists in body , risk of forming kidney stones increases manifold."),
    ("দীর্ঘদিন ধরে কাশি থাকলে ডাক্তারের কাছে গিয়ে বুকের এক্স-রে এবং কফ পরীক্ষা করান।", "If having cough for a long time , go to doctor and get chest X-ray and phlegm test done."),
    ("সর্দিকাশি কমাতে গরম ভাপ নেওয়া এবং মধু ও তুলসী পাতার রস খাওয়া দরকার।", "To reduce cold , taking warm steam and eating honey and basil leaf juice is needed."),
    ("হাঁটুর জোড়ায় জোড়ায় ব্যথা হলে চিকিৎসকের পরামর্শে এক্স-রে করিয়ে ওষুধ খান।", "If pain occurs in knee joints , take medication getting X-ray done on doctor's advice."),
    ("ত্বকের র্যাশ বা এলার্জির জন্য সুতি সুতার পোশাক পরা ও সাবান কম ব্যবহার করা উচিত।", "For skin rash or allergy , wearing cotton clothes and using less soap should be done."),
    ("মাথা ঘোরার সমস্যা থাকলে রক্তের হিমোগ্লোবিন এবং প্রেশার মেপে দেখা জরুরি।", "If having dizziness issues , measuring blood hemoglobin and pressure is urgent."),
    ("কানে তালা লাগলে বা হালকা ব্যথা হলে কানে সর্ষের তেল দেওয়া থেকে বিরত থাকুন।", "If ear gets blocked or light pain occurs , refrain from putting mustard oil in ear.")
]
