# Prompt 1: প্রোটিন সমৃদ্ধ নিরামিষ খাবারের তালিকা দিন / List of protein-rich vegetarian foods
# HR=20, PR=20, NR=20

g_bn = "স্যাস্থসচেতনতা"
g_en = "Health awareness"
p_bn = "প্রোটিন সমৃদ্ধ নিরামিষ খাবারের তালিকা দিন"
p_en = "List of protein-rich vegetarian foods"

hr = [
    ("প্রোটিনের চমৎকার নিরামিষ উৎসের মধ্যে রয়েছে মসুর ডাল , ছোলা , পনির এবং সয়াবিন।", "Excellent vegetarian sources of protein include lentils , chickpeas , cottage cheese and soybeans."),
    ("আপনি দৈনন্দিন প্রোটিনের চাহিদা মেটাতে কাঠবাদাম , কাজুবাদাম , তিল এবং শিয়াবিজ খেতে পারেন।", "You can eat almonds , cashews , sesame seeds and chia seeds to meet your daily protein requirement."),
    ("মুগ ডাল , ছোলার ডাল , রাজমা এবং মটরশুঁটি নিরামিষাশীদের জন্য অত্যন্ত উৎকৃষ্ট প্রোটিনযুক্ত খাদ্য।", "Mung dal , chana dal , kidney beans and green peas are excellent protein-rich foods for vegetarians."),
    ("পনির , দই এবং দুধের মতো দুগ্ধজাত পণ্য নিরামিষ খাবারে পর্যাপ্ত প্রোটিন সরবরাহ করে।", "Dairy products like cottage cheese , yogurt and milk provide adequate protein in a vegetarian diet."),
    ("নিরামিষ খাদ্যে প্রোটিন বাড়াতে বাদাম , সূর্যমুখীর বীজ , চীনা বাদাম এবং কুমড়ার বীজ অন্তর্ভুক্ত করুন।", "Include nuts , sunflower seeds , peanuts and pumpkin seeds to increase protein in a vegetarian diet."),
    ("তোফু , সয়াবিনের বড়ি এবং সয়া দুধ হলো উদ্ভিজ্জ প্রোটিনের অন্যতম সেরা বিকল্প।", "Tofu , soybean chunks and soy milk are among the best plant-based protein alternatives."),
    ("কাঁচা কলা , কুইনোয়া , ওটস এবং চিয়া সিড থেকে শরীর ভালো পরিমাণে নিরামিষ প্রোটিন পায়।", "The body gets a good amount of vegetarian protein from raw banana , quinoa , oats and chia seeds."),
    ("প্রতিদিনের নিরামিষ আহারে বিভিন্ন ধরণের ডাল , পনীরের তরকারি এবং রাজমা খেলে প্রোটিনের ঘাটতি পূরণ হয়।", "Eating various types of lentils , cottage cheese curry and kidney beans in daily vegetarian meals fulfills protein deficiency."),
    ("নিরামিষভোজিদের জন্য সয়াবিন , মসুর ডাল , চিয়া বীজ এবং চিনা বাদাম বেশ পুষ্টিকর প্রোটিন উৎস।", "For vegetarians , soybeans , lentils , chia seeds and peanuts are quite nutritious protein sources."),
    ("বাদামী চাল এবং মসুর ডালের মিশ্রণ শরীরকে প্রয়োজনীয় সব অ্যামিনো এসিড এবং প্রোটিন যোগায়।", "A combination of brown rice and lentils supplies the body with all essential amino acids and protein."),
    ("সবুজ মটরশুঁটি , ছোলার ছাতু , তোফু এবং তিল নিরামিষ ডায়েটে প্রোটিনের মাত্রা বজায় রাখে।", "Green peas , chickpea flour , tofu and sesame seeds maintain protein levels in a vegetarian diet."),
    ("প্রোটিন সমৃদ্ধ নিরামিষ খাবারের তালিকায় মটরশুঁটি , রাজমা , মিষ্টি ভুট্টা এবং কাজুবাদাম বিশেষ উল্লেখযোগ্য।", "Green peas , kidney beans , sweet corn and cashew nuts are particularly noteworthy in the list of protein-rich vegetarian foods."),
    ("ছোলার ডাল , সয়াবিন এবং পনির নিয়মিত খেলে নিরামিষ খাদ্যে প্রোটিনের অভাব হয় না।", "Eating chana dal , soybeans and cottage cheese regularly prevents protein deficiency in a vegetarian diet."),
    ("নিরামিষ খাবারে উচ্চ প্রোটিনের জন্য পালং শাক , ব্রোকলি , ওটস এবং সূর্যমুখী বীজ খেতে পারেন।", "For high protein in vegetarian food , you can eat spinach , broccoli , oats and sunflower seeds."),
    ("মিষ্টি আলু , ওটস , তোফু এবং পনির হলো নিরামিষ খাদ্যে প্রোটিন পাওয়ার দারুণ মাধ্যম।", "Sweet potato , oats , tofu and cottage cheese are great means of getting protein in vegetarian food."),
    ("ছোলার ছাতুর শরবত এবং পনিরের তরকারি নিরামিষ খাদ্যে প্রোটিনের চাহিদা সহজে পূরণ করে।", "Chickpea flour drink and cottage cheese curry easily fulfill protein requirements in a vegetarian diet."),
    ("নিরামিষ ডায়েটে প্রোটিন পেতে প্রতিদিন বিভিন্ন ডাল , কাজুবাদাম এবং সয়া খণ্ড খাওয়া উচিত।", "To get protein in a vegetarian diet , one should eat different lentils , cashew nuts and soy chunks daily."),
    ("কুমড়োর বীজ , তিল , কাজুবাদাম এবং কাঠবাদাম খেলে নিরামিষাশীরা পর্যাপ্ত প্রোটিন পান।", "Vegetarians get adequate protein by consuming pumpkin seeds , sesame seeds , cashews and almonds."),
    ("সবুজ মটরশুঁটি , রাজমা , মসুর ডাল এবং দই উচ্চমাত্রার প্রোটিন সমৃদ্ধ নিরামিষ খাবার।", "Green peas , kidney beans , lentils and yogurt are high-protein vegetarian foods."),
    ("সয়াবিনের কিমা , তোফু , চিয়া সিড এবং ছোলার তরকারি চমৎকার নিরামিষ প্রোটিন সরবরাহ করে।", "Minced soybean , tofu , chia seeds and chickpea curry supply excellent vegetarian protein.")
]

pr = [
    ("নিরামিষ খাবারে সাধারণত আমিষের তুলনায় প্রোটিনের ঘনত্ব কিছুটা কম থাকে।", "Vegetarian food generally has a slightly lower protein density compared to non-vegetarian food."),
    ("সুস্বাস্থ্য বজায় রাখতে প্রতিদিন প্রোটিনযুক্ত খাবার খাওয়া শরীরের জন্য বেশ উপকারী।", "Eating protein-rich food daily is very beneficial for the body to maintain good health."),
    ("আমি সবসময় দুপুরের খাবারে এক বাটি সাধারণ মসুর ডাল খেতে পছন্দ করি।", "I always prefer to eat a bowl of plain lentils for lunch."),
    ("মাংস বা ডিম না খেলেও প্রোটিনের অন্যান্য উৎস নিয়ে সচেতন থাকা দরকার।", "Even if you do not eat meat or eggs , it is necessary to be conscious of other protein sources."),
    ("আমার এক বন্ধু শুধুমাত্র সবুজ শাকসবজি খেয়ে ওজন কমানোর চেষ্টা করছে।", "A friend of mine is trying to lose weight by eating only green vegetables."),
    ("প্রতিদিনের খাদ্যতালিকায় স্বাস্থ্যকর শাকসবজি রাখা শরীরের রোগ প্রতিরোধ ক্ষমতা বাড়ায়।", "Keeping healthy vegetables in the daily diet increases body immunity."),
    ("শরীরের পেশী গঠনে প্রোটিনের গুরুত্ব অপরিসীম হলেও সুষম খাদ্য খাওয়া বেশি জরুরি।", "Although protein is immensely important for muscle building , eating a balanced diet is more important."),
    ("আমি রাতের বেলা হালকা নিরামিষ খাবার খেয়ে সহজেই ঘুমিয়ে পড়ি।", "I fall asleep easily at night after eating a light vegetarian meal."),
    ("সকালের নাস্তায় প্রোটিন সমৃদ্ধ খাবার খেলে সারা দিন শরীরে শক্তি বজায় থাকে।", "Eating protein-rich food for breakfast maintains energy in the body all day."),
    ("সুষম খাদ্যাভ্যাস গড়ে তুলতে সব ধরণের শাকসবজি এবং ফলমূল খাওয়া ভালো।", "To develop a balanced eating habit , it is good to eat all types of vegetables and fruits."),
    ("নিরামিষ খাবার খেলে হজম প্রক্রিয়া ভালো থাকে এবং পেটের সমস্যা কম হয়।", "Eating vegetarian food keeps the digestive system good and reduces stomach problems."),
    ("আজকাল অনেকেই স্বাস্থ্য সচেতন হয়ে নিরামিষ খাদ্যাভ্যাসের দিকে ঝুঁকছেন।", "Nowadays many people are becoming health conscious and turning towards a vegetarian diet."),
    ("আমাদের পরিবারে সপ্তাহে অন্তত দুই দিন পুরোপুরি নিরামিষ রান্না করা হয়।", "In our family , completely vegetarian food is cooked at least two days a week."),
    ("শিশুদের শারীরিক বৃদ্ধির জন্য সঠিক পরিমাণে খাদ্য উপাদান নিশ্চিত করা দরকার।", "It is necessary to ensure the right amount of food elements for the physical growth of children."),
    ("আমি নিরামিষ তরকারিতে বেশি করে মশলা ব্যবহার না করে হালকা রান্না পছন্দ করি।", "I prefer light cooking without using too many spices in vegetarian curries."),
    ("কাজুবাদাম এবং কাঠবাদাম খেলে শরীর ভালো থাকে কিন্তু এগুলো বেশ দামি।", "Eating cashews and almonds keeps the body good , but they are quite expensive."),
    ("নিয়মিত ব্যায়াম করার পাশাপাশি সঠিক পুষ্টি গ্রহণ করা সুস্থ জীবনের চাবিকাঠি।", "Along with regular exercise , getting proper nutrition is the key to a healthy life."),
    ("আমাদের বাড়িতে প্রতিদিন সকালে ডাল এবং রুটি দিয়ে নাস্তা করার অভ্যাস আছে।", "In our home , there is a habit of having breakfast with lentils and bread every morning."),
    ("নিরামিষ খাবারে পর্যাপ্ত ভিটামিন এবং মিনারেল থাকলেও প্রোটিন খুঁজে নিতে হয়।", "Although vegetarian food has adequate vitamins and minerals , one has to find protein sources."),
    ("ফলমূল এবং শাকসবজি তাজা খেলে শরীর সতেজ থাকে এবং ক্লান্তি ভাব দূর হয়।", "Eating fresh fruits and vegetables keeps the body fresh and removes fatigue.")
]

nr = [
    ("চোখে ঘোলা দেখলে বা দৃষ্টিশক্তি কমে গেলে অবিলম্বে চক্ষু চিকিৎসকের পরামর্শ নেওয়া উচিত।", "If you see blurry or if your eyesight decreases , you should consult an eye doctor immediately."),
    ("দাঁতে পোকা লাগলে বা তীব্র ব্যথা হলে দ্রুত ডেন্টিস্টের কাছে যাওয়া প্রয়োজন।", "If there is tooth decay or severe pain , it is necessary to go to a dentist quickly."),
    ("হঠাৎ করে নাক দিয়ে রক্ত পড়লে মাথা সামান্য সামনের দিকে ঝুঁকি রাখা ভালো।", "If blood suddenly comes out of the nose , it is good to tilt the head slightly forward."),
    ("বুকের বাম পাশে তীব্র চাপ এবং ব্যথা হলে দ্রুত হাসপাতালে যাওয়া উচিত।", "If there is severe pressure and pain on the left side of the chest , one should go to the hospital quickly."),
    ("সকালে ঘুম থেকে উঠার পর কোমর ব্যথা হলে নরম বিছানা পরিবর্তন করা দরকার।", "If there is waist pain after waking up in the morning , it is necessary to change the soft bed."),
    ("মূত্রত্যাগের সময় জ্বালাপোড়া বা ঝিনঝিন করলে প্রচুর পরিমাণে পানি পান করুন।", "If there is burning or tingling during urination , drink plenty of water."),
    ("পানি কম খেলে বৃক্কে পাথর এবং কোষ্ঠকাঠিন্যের মতো নানা জটিলতা তৈরি হয়।", "Drinking less water causes various complications like kidney stones and constipation."),
    ("কাশি দীর্ঘস্থায়ী হলে ফুসফুসের পরীক্ষা করিয়ে নেওয়া অত্যন্ত জরুরী।", "If cough is persistent , it is extremely urgent to get a lung examination done."),
    ("সর্দিকাশি থেকে মুক্তি পেতে হালকা গরম পানিতে লবণ মিশিয়ে কুলি করুন।", "To get relief from a cold , gargle with mild warm water mixed with salt."),
    ("জাঙ্ক ফুড অতিরিক্ত খেলে উচ্চ রক্তচাপ এবং হৃদরোগের ঝুঁকি বৃদ্ধি পায়।", "Eating excess junk food increases the risk of high blood pressure and heart disease."),
    ("চোখের পাতা ঘন ঘন কাঁপলে বিশ্রাম নেওয়া এবং স্ক্রিন টাইম কমানো উচিত।", "If the eyelid twitches frequently , one should rest and reduce screen time."),
    ("দাঁতের শিরশিরানি কমাতে সংবেদনশীল দাঁতের জন্য বিশেষ পেস্ট ব্যবহার করা যেতে পারে।", "To reduce tooth sensitivity , a special paste for sensitive teeth can be used."),
    ("কোমর এবং পিঠের ব্যথা কমাতে প্রতিদিন সকালে হালকা শারীরিক ব্যায়াম করা উপকারী।", "To reduce waist and back pain , doing light physical exercise every morning is beneficial."),
    ("নাক দিয়ে রক্ত পড়া বন্ধ করতে নাকের নরম অংশ আঙুল দিয়ে চেপে রাখুন।", "To stop nosebleeding , pinch the soft part of the nose with fingers."),
    ("বুকের চাপ অনুভব হলে অবহেলা না করে দ্রুত হৃদরোগ বিশেষজ্ঞের শরণাপন্ন হন।", "If chest pressure is felt , consult a cardiologist quickly without neglecting it."),
    ("মূত্রনালীর সংক্রমণ এড়াতে সবসময় ব্যক্তিগত পরিচ্ছন্নতা বজায় রাখা উচিত।", "To avoid urinary tract infection , one should always maintain personal hygiene."),
    ("দেহে পানিশূন্যতা দেখা দিলে মাথা ঘোরা এবং ক্লান্তি ভাব বৃদ্ধি পেতে পারে।", "If dehydration occurs in the body , dizziness and tiredness may increase."),
    ("কাশি তিন সপ্তাহের বেশি স্থায়ী হলে ডাক্তারের সাথে কথা বলে কফ পরীক্ষা করান।", "If cough lasts more than three weeks , talk to a doctor and test the phlegm."),
    ("ঠাণ্ডা লাগলে আদা এবং তুলসী পাতার চা খেলে বেশ আরাম পাওয়া যায়।", "If you catch a cold , drinking ginger and basil tea provides great comfort."),
    ("ফাস্টফুড বর্জন করে ঘরে তৈরি তাজা খাবার খাওয়া স্বাস্থ্যের জন্য অত্যন্ত ভালো।", "Avoiding fast food and eating fresh homemade food is extremely good for health.")
]
