# Prompt 7: সকালে ঘুম থেকে উঠার পর পীঠে এবং কমরে ব্যাথা করে / Pain in the back and waist after waking up in the morning
# HR=14, PR=14, NR=14

g_bn = "স্যাস্থসচেতনা"
g_en = "Health awareness"
p_bn = "সকালে ঘুম থেকে উঠার পর পীঠে এবং কমরে ব্যাথা করে"
p_en = "Pain in the back and waist after waking up in the morning"

hr = [
    ("সকালের পিঠ ও কোমর ব্যথা কমাতে শক্ত ও সমান তোষকে ঘুমান , অতিরিক্ত নরম বিছানা ত্যাগ করুন এবং উঠে হালকা স্ট্রেচিং ব্যায়াম করুন।", "To reduce morning back and waist pain , sleep on a firm and flat mattress , abandon extra soft beds and do light stretching exercises upon rising."),
    ("ঘুম থেকে ওঠার সময় হঠাৎ সোজা না উঠে প্রথমে একপাশে কাত হয়ে হাতে ভর দিয়ে ধীরে ধীরে উঠুন।", "When waking up from sleep , do not get up straight suddenly , get up slowly first by turning to one side and taking hand support."),
    ("ঘুমানোর সঠিক পজিশন মেনে চলুন ; কাত হয়ে ঘুমানোর সময় দুই হাঁটুর মাঝে একটি নরম বালিশ রাখলে কোমরের ওপর চাপ কমে।", "Follow correct sleeping positions ; placing a soft pillow between two knees when sleeping on one side reduces pressure on the waist."),
    ("ব্যথার স্থানে দিনে দুইবার হালকা গরম পানির সেঁক দিন এবং একজন ফিজিওথেরাপিস্টের কাছ থেকে কোমর ব্যথার ব্যায়াম শিখে নিন।", "Apply mild warm water compress to the painful area twice daily and learn waist pain exercises from a physiotherapist."),
    ("শরীরে ভিটামিন ডি এবং ক্যালসিয়ামের ঘাটতি থাকলে সকালে কোমর ব্যথা হতে পারে , তাই রোদে বসুন ও রক্ত পরীক্ষা করান।", "If there is a lack of vitamin D and calcium in the body , morning waist pain can occur , so sit in the sun and get blood tests."),
    ("অফিস বা বাড়িতে দীর্ঘ সময় একটানা বসে কাজ না করে প্রতি ঘণ্টা পর দাঁড়িয়ে কিছুক্ষণ হাঁটার অভ্যাস গড়ে তুলুন।", "Instead of sitting continuously for long hours at office or home , form a habit of standing and walking a bit every hour."),
    ("মেরুদণ্ডের স্বাস্থ্য ভালো রাখতে ওজন নিয়ন্ত্রণে রাখুন এবং পিঠের পেশী শক্তিশালী করার জন্য নিয়মিত অ্যারোবিক এক্সারসাইজ করুন।", "To keep spine health good , keep weight in control and do regular aerobic exercise to strengthen back muscles."),
    ("সকালে কোমর ও পিঠের আড়ষ্টতা দূর করতে ঈষদুষ্ণ পানিতে গোসল করা এবং হালকা ফিজিওথেরাপি নেওয়া বেশ ফলপ্রসূ।", "To remove stiffness of waist and back in the morning , bathing in lukewarm water and taking light physiotherapy is quite fruitful."),
    ("যদি ব্যথা পায়ের দিকে ছড়িয়ে যায় বা অবশ ভাব অনুভুত হয় , তবে মেরুদণ্ডের এমআরআই করানোর জন্য নিউরো-মেডিসিন বিশেষজ্ঞ দেখান।", "If pain spreads towards legs or numbness is felt , see a neurologist for a spinal MRI."),
    ("উঁচু হিলের জুতো পরা এড়িয়ে চলুন এবং হাঁটাচলা ও কাজের সময় সবসময় মেরুদণ্ড সোজা রাখার চেষ্টা করুন।", "Avoid wearing high-heeled shoes and always try to keep the spine straight while walking and working."),
    ("কোমর ব্যথার জন্য চিকিৎসকের পরামর্শ ছাড়া তীব্র ব্যথানাশক ওষুধ দীর্ঘদিন খাওয়া থেকে বিরত থাকা অত্যন্ত জরুরি।", "Refraining from taking severe painkiller medications for long terms without doctor's advice for waist pain is extremely urgent."),
    ("পিঠের ব্যথা থেকে মুক্তি পেতে ভারী জিনিস নিচু হয়ে কোমর বাঁকিয়ে তুলবেন না , হাঁটু মুড়ে নামুন।", "To get relief from back pain , do not lift heavy objects by bending the waist down , bend at the knees."),
    ("সকালে ঘুম ভাঙার পর বিছানায় শুয়েই সোজা হয়ে বুক ও পা আলতো করে প্রসারিত করলে মেরুদণ্ড নমনীয় থাকে।", "After waking up in the morning , stretching chest and legs gently while lying straight in bed keeps the spine flexible."),
    ("কোমর ব্যথা তীব্র হলে বরফ ও গরমের অল্টারনেট সেঁক দিন এবং দ্রুত একজন অর্থোপেডিক চিকিৎসকের শরণাপন্ন হন।", "If waist pain is severe , give alternate ice and hot compresses and quickly consult an orthopedic doctor.")
]

pr = [
    ("ইদানীং অনেকেরই দীর্ঘক্ষণ কম্পিউটারে বসে কাজ করার কারণে পিঠ ও ঘাড়ে ব্যথা দেখা দিচ্ছে।", "Nowadays many people are experiencing back and neck pain due to sitting and working at computers for long hours."),
    ("আমাদের প্রতিদিনের জীবনযাত্রায় সঠিকPosture বজায় রাখা শরীর সুস্থ রাখার অন্যতম চাবিকাঠি।", "Maintaining proper posture in our daily lifestyle is one of the keys to keeping the body healthy."),
    ("আমার বড় ভাইয়ের ভারী জিমে ব্যায়াম করার পর কোমর সামান্য মচকে গিয়েছিল।", "My elder brother had his waist slightly sprained after working out heavily at the gym."),
    ("নিয়মিত সকালে হাঁটার অভ্যাস করলে শরীর সতেজ থাকে এবং পেশীর শক্তভাব দূর হয়।", "Having a habit of walking regularly in the morning keeps the body fresh and removes muscle stiffness."),
    ("বৃদ্ধ বয়সে হাড় ক্ষয় এবং রিউম্যাটয়েড আর্থ্রাইটিসের কারণে শরীরে বিভিন্ন জোড়ায় ব্যথা হতে পারে।", "In old age , bone decay and rheumatoid arthritis can cause pain in various body joints."),
    ("একটানা গাড়ি বা মোটরবাইক চালালে কোমর ও পিঠের পেশীতে বেশ টান পড়ে।", "Driving a car or motorbike continuously puts a lot of strain on waist and back muscles."),
    ("উচ্চমানের বালিশ ও ম্যাট্রেস ব্যবহার করলে ঘুমের কোয়ালিটি অনেক উন্নত হয়।", "Using high quality pillows and mattresses improves sleep quality significantly."),
    ("শরীরের যেকোনো ব্যথায় হালকা সরিষার তেল বা পেইন রিলিফ বাম দিয়ে মালিশ করলে স্বস্তি মেলে।", "In any body pain , massaging with light mustard oil or pain relief balm brings comfort."),
    ("সপ্তাহে অন্তত পাঁচ দিন হালকা যোগব্যায়াম করলে পেশীর নমনীয়তা অনেক বাড়ে।", "Doing light yoga at least five days a week increases muscle flexibility significantly."),
    ("কাজ করার মাঝে ছোট বিরতি নিলে শরীরের ওপর শারীরিক ও মানসিক চাপ কমে আসে।", "Taking small breaks in between work reduces physical and mental strain on the body."),
    ("মেদ বা ভুঁড়ি বেড়ে গেলে শরীরের ভরকেন্দ্রে পরিবর্তন এসে কোমরে চাপ বাড়ে।", "If fat or belly increases , the center of gravity of the body changes and increases pressure on the waist."),
    ("সঠিক নিয়মে হাঁটাহাঁটি করা এবং দৌড়ানো স্বাস্থ্য রক্ষায় দারুণ ভূমিকা রাখে।", "Walking and running in proper rules plays a great role in preserving health."),
    ("দুপুরের খাবারের পর কিছুক্ষণ বিশ্রাম নেওয়া এবং আরামদায়ক চেয়ারে বসা দরকার।", "Taking rest for a while after lunch and sitting in a comfortable chair is needed."),
    ("শরীর অতিরিক্ত ক্লান্ত থাকলে রাতে গভীর ঘুম হয় কিন্তু সকালে উঠতে কষ্ট হতে পারে।", "If the body is extra tired , deep sleep happens at night but getting up in the morning can be tough.")
]

nr = [
    ("নাক দিয়ে হঠাৎ রক্ত পড়া শুরু হলে সোজা হয়ে বসে নাকের ছিদ্র বন্ধ রাখুন।", "If blood suddenly starts falling from nose , sit straight and keep nostril closed."),
    ("চোখের পাতা ঘন ঘন কাঁপলে ল্যাপটপ ব্যবহার কমান এবং চোখে গরম সেঁক দিন।", "If eyelid twitches frequently , reduce laptop use and apply warm compress to eyes."),
    ("বুকের বাম পাশে চাপ ধরে তীব্র ব্যথা হলে দেরি না করে দ্রুত ইসিজি করান।", "If there is severe pressing pain on left side of chest , get an ECG done quickly without delay."),
    ("দাঁত ক্ষয়ে শিরশির করলে মিষ্টি খাবার বন্ধ করুন এবং সেনসেটিভ টুথপেস্ট ব্যবহার করুন।", "If teeth decay and tingle , stop sweet food and use sensitive toothpaste."),
    ("মূত্রত্যাগের পর ঝিনঝিন করলে বেশি করে পানি পান করুন এবং ডাক্তার দেখান।", "If tingling occurs after urination , drink more water and see a doctor."),
    ("নিরামিষ খাদ্যে প্রোটিন বাড়াতে মসুর ডাল , সয়াবিন এবং তোফু বেশি করে খান।", "To increase protein in vegetarian diet , eat lentils , soybeans and tofu more."),
    ("জাঙ্ক ফুড বর্জন করলে মেদ কমানো এবং ডায়াবেটিস প্রতিরোধ করা বেশ সহজ হয়।", "Avoiding junk food makes it quite easy to reduce fat and prevent diabetes."),
    ("পানি কম খেলে শরীর পানিশূন্য হয়ে পড়তে পারে এবং কিডনিতে জটিলতা তৈরি হয়।", "Drinking less water can make the body dehydrated and create complications in kidneys."),
    ("ক্রমাগত কাশি থাকলে ফুসফুস পরীক্ষার জন্য একজন বক্ষব্যাধি বিশেষজ্ঞের কাছে যান।", "If having persistent cough , go to a pulmonologist for lung examination."),
    ("সর্দিকাশি হলে উষ্ণ পানি পান করুন এবং গরম পানিতে লবঙ্গ দিয়ে ভাপ নিন।", "If having cold , drink warm water and take steam with cloves in warm water."),
    ("ত্বকে অ্যালার্জি হলে অ্যালকোহলমুক্ত লোশন ব্যবহার করুন এবং সাবান কম লাগান।", "If having skin allergy , use alcohol-free lotion and apply less soap."),
    ("মাথাব্যথার তীব্রতা কমাতে শান্ত ও অন্ধকার ঘরে চোখ বন্ধ করে বিশ্রাম নিন।", "To reduce severity of headache , take rest closing eyes in a quiet and dark room."),
    ("গ্যাস্ট্রিকের সমস্যায় ভাজাপোড়া খাবার এড়িয়ে চলা এবং সময়মতো খাওয়া উচিত।", "In gastric problems , avoiding fried food and eating on time should be done."),
    ("কানের ইনফেকশন এড়াতে কানে যেকোনো কাঠি বা কটন বাড দেওয়া বন্ধ করুন।", "To avoid ear infection , stop putting any sticks or cotton buds in the ear.")
]
