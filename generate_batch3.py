import pandas as pd

# Define rows for Prompt 1
# Prompt 1:
# Genre: 'মানসিক বিচলতা' / 'mental disturbance'
# Prompt: 'পরীক্ষা বা ইন্টারভিউর আগে ভয় লাগে , মানসিকভাবে প্রস্তুত হওয়ার উপায় কী'
# Prompt En: 'I feel scared before an exam or interview, what is the way to prepare mentally?'
# HR: 28, PR: 36, NR: 32

p1_genre = "মানসিক বিচলতা"
p1_genre_en = "mental disturbance"
p1_prompt = "পরীক্ষা বা ইন্টারভিউর আগে ভয় লাগে , মানসিকভাবে প্রস্তুত হওয়ার উপায় কী"
p1_prompt_en = "I feel scared before an exam or interview, what is the way to prepare mentally?"

p1_data = [
    # Highly Relevant (28)
    ("পরীক্ষা বা ইন্টারভিউর আগে গভীর শ্বাস-প্রশ্বাসের ব্যায়াম করলে উদ্বেগ কমে এবং মন শান্ত হয়।", "Practicing deep breathing exercises before an exam or interview reduces anxiety and calms the mind.", "Highly Relevant"),
    ("পর্যাপ্ত প্রস্তুতি নেওয়া এবং ইতিবাচক চিন্তাভাবনা করা মানসিক চাপ কমাতে সাহায্য করে।", "Taking adequate preparation and thinking positively helps reduce mental stress.", "Highly Relevant"),
    ("পরীক্ষার আগের রাতে পর্যাপ্ত ঘুম মস্তিষ্ককে সতেজ রাখে এবং ভয় কাটাতে সাহায্য করে।", "Getting adequate sleep the night before an exam keeps the brain fresh and helps overcome fear.", "Highly Relevant"),
    ("ইন্টারভিউর আগে কাল্পনিক ভয় না পেয়ে নিজের যোগ্যতার ওপর বিশ্বাস রাখা উচিত।", "Instead of imaginary fear before an interview , one should believe in one's abilities.", "Highly Relevant"),
    ("পড়াশোনা বা উত্তরের রিহার্সাল আগে থেকে করে রাখলে আত্মবিশ্বাস বহুগুণ বৃদ্ধি পায়।", "Rehearsing studies or answers in advance increases self-confidence manifold.", "Highly Relevant"),
    ("উদ্বেগ নিয়ন্ত্রণে রাখতে পরীক্ষার কেন্দ্রে সঠিক সময়ের কিছুটা আগে পৌঁছানো বুদ্ধিমানের কাজ।", "Arriving at the exam center a bit early is smart to keep anxiety under control.", "Highly Relevant"),
    ("মনোযোগ বাড়াতে ও অস্থিরতা কমাতে ধ্যান বা মেডিটেশন করার চেষ্টা করুন।", "Try practicing meditation to increase focus and reduce restlessness.", "Highly Relevant"),
    ("ইন্টারভিউয়ের সম্ভাব্য প্রশ্নগুলো নিয়ে বন্ধুদের সাথে মক ভাইভা দিলে ভয় কেটে যায়।", "Giving mock vivas with friends about potential interview questions removes fear.", "Highly Relevant"),
    ("পরীক্ষার আগে অতিরিক্ত ক্যাফেইন বা চা-কফি খাওয়া এড়িয়ে চলা উচিত , কারণ এটি নার্ভাসনেস বাড়ায়।", "Avoid excess caffeine or tea-coffee before exams , as it increases nervousness.", "Highly Relevant"),
    ("ভয় লাগলে নিজেকে বোঝান যে আপনি আপনার সর্বোচ্চ প্রস্তুতি নিয়েছেন।", "If you feel scared , remind yourself that you have prepared your best.", "Highly Relevant"),
    ("ইন্টারভিউ বোর্ডের মুখোমুখি হওয়ার আগে ধীরস্থিরভাবে চিন্তা করার অভ্যাস গড়ে তুলুন।", "Develop the habit of thinking calmly before facing the interview board.", "Highly Relevant"),
    ("পরীক্ষার আগে পড়া পড়া নিয়ে বেশি মানসিক চাপ না নিয়ে মূল বিষয়গুলো রিভিশন দিন।", "Revise core topics without taking too much mental pressure over studying before exams.", "Highly Relevant"),
    ("অতিরিক্ত উৎকণ্ঠা হলে মৃদু হালকা গান শোনা বা বন্ধুদের সাথে হালকা গল্প করা যেতে পারে।", "Listening to soft music or chatting lightly with friends can help if there is severe anxiety.", "Highly Relevant"),
    ("পরীক্ষার সময়সূচি ও প্রয়োজনীয় জিনিসপত্র আগের রাতেই গুছিয়ে রাখা ভালো।", "It is good to organize the exam schedule and required items the night before.", "Highly Relevant"),
    ("মানসিক স্থিরতা পেতে প্রতিদিন নিয়ম করে কিছুক্ষণ হাঁটাহাঁটি বা ব্যায়াম করুন।", "Exercise or walk for a while daily to attain mental stability.", "Highly Relevant"),
    ("ইন্টারভিউর পোশাক আগে থেকে প্রস্তুত রাখলে শেষ মুহূর্তের দুশ্চিন্তা এড়ানো যায়।", "Preparing interview attire in advance avoids last-minute worry.", "Highly Relevant"),
    ("পরীক্ষার সময় জানা উত্তর আগে লেখা শুরু করলে ভয় ও অনিশ্চয়তা কেটে যায়।", "Starting with known answers during exams eliminates fear and uncertainty.", "Highly Relevant"),
    ("নিজের নেতিবাচক চিন্তাভাবনা দূর করে পজিটিভ অভিজ্ঞতা মনে করার অভ্যাস করুন।", "Eliminate negative thoughts and practice recalling positive experiences.", "Highly Relevant"),
    ("পরীক্ষার বা ভাইভার সময় বুক ভরে শ্বাস নিয়ে ধীরে ধীরে ছাড়লে স্নায়ু শান্ত হয়।", "Inhaling deeply and exhaling slowly during exams or vivas calms the nerves.", "Highly Relevant"),
    ("ভয়কে স্বাভাবিকভাবে গ্রহণ করে সেটিকে মোকাবিলার সাহসিকতা অর্জন করতে হবে।", "Accept fear naturally and acquire the courage to face it.", "Highly Relevant"),
    ("পরীক্ষার আগের দিন অতিরিক্ত রাত জেগে পড়ালেখা না করাই মানসিক সুস্থতার জন্য ভালো।", "Avoiding late-night cramming the day before an exam is good for mental well-being.", "Highly Relevant"),
    ("ইন্টারভিউতে কোনো উত্তর জানা না থাকলে সততার সাথে বলাই শ্রেয়।", "If you do not know an answer in an interview , stating it honestly is better.", "Highly Relevant"),
    ("শারীরিক ও মানসিকভাবে চাঙ্গা থাকতে পুষ্টিকর খাবার ও পর্যাপ্ত পানি পান করুন।", "Eat nutritious food and drink adequate water to stay physically and mentally fresh.", "Highly Relevant"),
    ("ভয়ের কারণে হাত-পা কাঁপলে কয়েক সেকেন্ড চোখ বন্ধ করে সোজা হয়ে বসুন।", "If hands and feet tremble due to fear , close your eyes and sit straight for a few seconds.", "Highly Relevant"),
    ("ইন্টারভিউয়ের স্থান সম্পর্কে আগেই ধারণা রাখলে সময়মতো পৌঁছানোর দুশ্চিন্তা থাকে না।", "Having a prior idea about the interview location eliminates travel delay anxiety.", "Highly Relevant"),
    ("পরীক্ষার সকালে হালকা খাবার খেয়ে পরীক্ষা কেন্দ্রে যাওয়া উচিত।", "One should eat a light meal on the morning of the exam before going to the exam center.", "Highly Relevant"),
    ("মনোবল ধরে রাখতে নিজের অতীতের সফলতার মুহূর্তগুলো স্মরণ করুন।", "Recall moments of past success to maintain morale.", "Highly Relevant"),
    ("যদি উৎকণ্ঠা দৈনন্দিন জীবনকে ব্যাহত করে , তবে কোনো সাইকোলজিস্টের পরামর্শ নেওয়া যেতে পারে।", "If anxiety disrupts daily life , consulting a psychologist may be considered.", "Highly Relevant"),

    # Partially Relevant (36)
    ("প্রতিদিন সুষম খাদ্য গ্রহণ করলে শরীরের রোগ প্রতিরোধ ক্ষমতা বাড়ে।", "Eating a balanced diet daily increases the body's immunity.", "Partially Relevant"),
    ("মানসিক স্বাস্থ্য ভালো রাখতে প্রতিদিন পর্যাপ্ত পানি পান করা প্রয়োজন।", "Drinking adequate water daily is necessary to maintain good mental health.", "Partially Relevant"),
    ("নিয়মিত শারীরিক ব্যায়াম করলে পেশি মজবুত হয় ও শরীরের ক্লান্তি দূর হয়।", "Regular physical exercise strengthens muscles and eliminates bodily fatigue.", "Partially Relevant"),
    ("অতিরিক্ত সময় মোবাইল বা ল্যাপটপ ব্যবহার করলে চোখের ওপর চাপ পড়ে।", "Using mobile phones or laptops for excessive time strains the eyes.", "Partially Relevant"),
    ("উদ্বেগ বা বিষণ্ণতা দূর করতে বন্ধু ও পরিবারের সাথে সামাজিক যোগাযোগ বজায় রাখুন।", "Maintain social contact with friends and family to relieve anxiety or depression.", "Partially Relevant"),
    ("মাথাব্যথা হলে কিছুদিন বিশ্রাম নেওয়া এবং পর্যাপ্ত ঘুমানো দরকার।", "If you have a headache , taking rest and sleeping adequately for a few days is needed.", "Partially Relevant"),
    ("কাজের ফাঁকে ফাঁকে বিরতি নিলে মস্তিষ্কের কাজ করার ক্ষমতা বৃদ্ধি পায়।", "Taking breaks in between work increases the brain's working capacity.", "Partially Relevant"),
    ("শারীরিক দুর্বলতা কাটাতে পুষ্টিকর ফলমূল ও শাকসবজি বেশি করে খাওয়া উচিত।", "Eating more nutritious fruits and vegetables is essential to overcome physical weakness.", "Partially Relevant"),
    ("অতিরিক্ত চাপ সামলাতে সুনির্দিষ্ট কাজের তালিকা বানিয়ে কাজ করা ভালো।", "Creating a specific to-do list helps in managing extra workload.", "Partially Relevant"),
    ("উচ্চ রক্তচাপ এড়াতে খাবারে অতিরিক্ত লবণ খাওয়া বন্ধ করতে হবে।", "To avoid high blood pressure , eating extra salt in food must be stopped.", "Partially Relevant"),
    ("মানসিক দুশ্চিন্তা কমাতে প্রতিদিন সকালে হাঁটার অভ্যাস করা ভালো।", "Developing a habit of morning walks helps reduce mental worry.", "Partially Relevant"),
    ("মন ভালো রাখতে নতুন শখ চর্চা করা বা বই পড়া শুরু করতে পারেন।", "You can start practicing new hobbies or reading books to uplift your mood.", "Partially Relevant"),
    ("যেকোনো প্রতিযোগিতামূলক পরীক্ষার জন্য রুটিন মেনে পড়াশোনা করা উচিত।", "One should study according to a routine for any competitive exam.", "Partially Relevant"),
    ("কাজের মান বাড়াতে কাজের জায়গায় নিরিবিলি পরিবেশ নিশ্চিত করা দরকার।", "Ensuring a quiet environment at the workplace is needed to improve work quality.", "Partially Relevant"),
    ("প্রতিদিন একই সময়ে ঘুমাতে যাওয়া এবং ঘুম থেকে ওঠার অভ্যাস করা উচিত।", "One should form a habit of sleeping and waking up at the same time daily.", "Partially Relevant"),
    ("মানসিক ক্লান্তি দূর করতে মাঝে মাঝে প্রকৃতির কাছাকাছি ঘুরতে যাওয়া ভালো।", "Traveling close to nature occasionally helps overcome mental fatigue.", "Partially Relevant"),
    ("স্মৃতিশক্তি বাড়াতে বাদাম ও ওমেগা-৩ সমৃদ্ধ খাবার খাওয়া উচিত।", "Eating nuts and omega-3 rich food helps boost memory.", "Partially Relevant"),
    ("পড়াশোনায় মনোযোগ দিতে শান্ত ও আলো-বাতাসপূর্ণ ঘর নির্বাচন করা প্রয়োজন।", "Selecting a quiet and well-ventilated room is necessary to focus on studies.", "Partially Relevant"),
    ("কাজের চাপ বেশি থাকলে সঠিক সময় ব্যবস্থাপনা শেখা অত্যন্ত জরুরি।", "Learning proper time management is extremely essential if work pressure is high.", "Partially Relevant"),
    ("শারীরিক সুস্থতার জন্য রাতে অন্তত ৭ থেকে ৮ ঘণ্টা ঘুমানো আবশ্যক।", "Sleeping at least 7 to 8 hours at night is essential for physical health.", "Partially Relevant"),
    ("অতিরিক্ত দুশ্চিন্তা করলে গ্যাস্ট্রিক বা পেটের সমস্যা দেখা দিতে পারে।", "Excessive worrying can cause gastric or stomach problems.", "Partially Relevant"),
    ("চাকরির পরীক্ষার প্রস্তুতি নিতে নিয়মিত দৈনিক পত্রিকা ও কারেন্ট অ্যাফেয়ার্স পড়ুন।", "Read daily newspapers and current affairs regularly to prepare for job exams.", "Partially Relevant"),
    ("উদ্বেগমুক্ত থাকতে সামাজিক যোগাযোগ মাধ্যমের অতিরিক্ত ব্যবহার বর্জন করুন।", "Avoid excessive use of social media to remain free from anxiety.", "Partially Relevant"),
    ("শরীরে ভিটামিনের ঘাটতি হলে দ্রুত ক্লান্তি ও অলসতা চলে আসে।", "Vitamin deficiency in the body leads to quick fatigue and laziness.", "Partially Relevant"),
    ("কাজের মাঝে রিফ্রেশমেন্টের জন্য হালকা চা পান করা যেতে পারে।", "Drinking mild tea can be enjoyed for refreshment in between work.", "Partially Relevant"),
    ("মানসিক স্বাস্থ্যের যত্ন নিতে রাগ বা ক্ষোভ জমে থাকতে দেওয়া উচিত নয়।", "To take care of mental health , anger or resentment should not be allowed to accumulate.", "Partially Relevant"),
    ("পড়াশোনার পাশাপাশি খেলাধুলা করলে শারীরিক ও মানসিক বিকাশ ঘটে।", "Participating in sports alongside studies fosters physical and mental development.", "Partially Relevant"),
    ("যেকোনো ইন্টারভিউয়ের জন্য সুন্দর পোশাক নির্বাচন করা ব্যক্তিত্ব প্রকাশ করে।", "Choosing good clothing for any interview expresses personality.", "Partially Relevant"),
    ("ধূমপান ও মাদকদ্রব্য গ্রহণ মানসিকভাবে মানুষকে অস্থির করে তোলে।", "Smoking and substance abuse make people mentally restless.", "Partially Relevant"),
    ("পরীক্ষায় ভালো ফলাফল করতে হলে বছরের শুরু থেকেই নিয়মিত পড়া পড়া উচিত।", "To score well in exams , one should study regularly right from the beginning of the year.", "Partially Relevant"),
    ("কর্মক্ষেত্রে সাফল্যের জন্য যোগাযোগের দক্ষতা বৃদ্ধি করা প্রয়োজন।", "Improving communication skills is required for success in the workplace.", "Partially Relevant"),
    ("উদ্বেগ নিরসনে নিজের অনুভূতির কথা প্রিয়জনদের সাথে শেয়ার করুন।", "Share your feelings with loved ones to alleviate anxiety.", "Partially Relevant"),
    ("শরীরে পানির ঘাটতি হলে মাথাব্যথা ও মেজাজ খিটখিটে হতে পারে।", "Dehydration in the body can cause headaches and irritable moods.", "Partially Relevant"),
    ("সময়মতো খাওয়া-দাওয়া না করলে শরীরে শর্করার মাত্রা কমে মাথা ঘোরাতে পারে।", "Not eating food on time can drop blood sugar levels and cause dizziness.", "Partially Relevant"),
    ("পড়াশোনায় ভালো করতে ছোট ছোট বিরতি দিয়ে পড়ালেখা করার পরামর্শ দেওয়া হয়।", "Studying with short intervals is recommended to perform well in studies.", "Partially Relevant"),
    ("মনোযোগ ধরে রাখতে পড়ার সময় মোবাইল ফোন দূরে রাখা ভালো।", "It is advisable to keep mobile phones away while studying to maintain concentration.", "Partially Relevant"),

    # Not Relevant (32)
    ("দাঁতের ক্ষয়রোগ প্রতিরোধ করতে প্রতিদিন রাতে ঘুমানোর আগে ব্রাশ করুন।", "Brush your teeth every night before going to sleep to prevent tooth decay.", "Not Relevant"),
    ("ত্বক উজ্জ্বল রাখতে প্রতিদিন পর্যাপ্ত পরিমাণ তাজা শাকসবজি খান।", "Eat sufficient fresh vegetables daily to keep skin glowing.", "Not Relevant"),
    ("হাঁটুর ব্যথা কমাতে প্রতিদিন হালকা ব্যায়াম এবং বরফের সেক দিন।", "Apply ice packs and do light exercises daily to reduce knee pain.", "Not Relevant"),
    ("পেটের গ্যাস কমাতে তৈলাক্ত ও মসলাযুক্ত খাবার খাওয়া বন্ধ করুন।", "Stop eating oily and spicy foods to reduce stomach gas.", "Not Relevant"),
    ("চোখ ভালো রাখতে ভিটামিন 'এ' সমৃদ্ধ খাবার বেশি করে খাওয়া প্রয়োজন।", "Eating foods rich in Vitamin 'A' is necessary to maintain good eye health.", "Not Relevant"),
    ("কাশি কমাতে গরম পানিতে মধু ও লেবুর রস মিশিয়ে পান করুন।", "Drink hot water mixed with honey and lemon juice to reduce cough.", "Not Relevant"),
    ("ব্রণ দূর করতে মুখে নিম পাতা ও কাঁচা হলুদের পেস্ট লাগান।", "Apply neem leaf and raw turmeric paste on the face to remove acne.", "Not Relevant"),
    ("কোমর ব্যথা হলে একটানা বেশিক্ষণ এক জায়গায় বসে থাকা এড়িয়ে চলুন।", "Avoid sitting continuously in one place for a long time if you have lower back pain.", "Not Relevant"),
    ("রক্তশূন্যতা দূর করতে কচু শাক ও লাল শাক বেশি করে খাওয়া উচিত।", "Eating taro greens and red amaranth is recommended to cure anemia.", "Not Relevant"),
    ("অ্যাজমা বা হাঁপানি রোগীর ঠান্ডা ও ধূলোবালি থেকে দূরে থাকা দরকার।", "Asthma patients need to stay away from cold and dust.", "Not Relevant"),
    ("কাঁচা পেঁপে ও আপেল খেলে হজমশক্তি দ্রুত বৃদ্ধি পায়।", "Eating raw papaya and apples rapidly improves digestion.", "Not Relevant"),
    ("কান চুলকালে কানে কোনো কাঠি বা শক্ত কিছু ঢুকানো বিপজ্জনক।", "Inserting sticks or hard objects into the ear when it itches is dangerous.", "Not Relevant"),
    ("হাইপারটেনশন কমাতে প্রতিদিনের খাবারে লবণের পরিমাণ সীমিত রাখুন।", "Limit the amount of salt in daily meals to reduce hypertension.", "Not Relevant"),
    ("গলা ব্যথা নিরাময়ে হালকা গরম পানিতে লবণ দিয়ে কুলকুচা করুন।", "Gargle with warm salt water to relieve throat pain.", "Not Relevant"),
    ("পায়ের গোড়ালি ফাটলে রাতে ভেসলিন বা গ্লিসারিন মেখে রাখুন।", "Apply vaseline or glycerin at night if your heels crack.", "Not Relevant"),
    ("ডায়াবেটিস নিয়ন্ত্রণে রাখতে প্রতিদিন সকালে আধঘণ্টা দ্রুত হাঁটুন।", "Walk briskly for half an hour every morning to keep diabetes under control.", "Not Relevant"),
    ("কোষ্ঠকাঠিন্য দূর করতে আঁশযুক্ত খাবার ও ইসবগুলের ভূষি পান করুন।", "Drink isabgol husk and eat fiber-rich food to cure constipation.", "Not Relevant"),
    ("হাত পরিষ্কার না করে চোখ বা মুখ স্পর্শ করা উচিত নয়।", "One should not touch eyes or face without washing hands.", "Not Relevant"),
    ("ত্বকের শুষ্কতা দূর করতে স্নানের পর অলিভ অয়েল ব্যবহার করুন।", "Use olive oil after bathing to eliminate skin dryness.", "Not Relevant"),
    ("বুকে কফ জমলে গরম পানির ভাপ বা স্টিম নিন।", "Take steam or hot water vapor if chest congestion occurs.", "Not Relevant"),
    ("পেক্টোরাল পেশি শক্তিশালী করতে পুশ-আপ ব্যায়াম অত্যন্ত কার্যকরী।", "Push-up exercises are very effective for strengthening pectoral muscles.", "Not Relevant"),
    ("নখ পরিষ্কার ও ছোট রাখলে বিভিন্ন জীবাণুর সংক্রমণ থেকে বাঁচা যায়।", "Keeping nails clean and short protects against various germ infections.", "Not Relevant"),
    ("চুলের গোড়া শক্ত করতে সপ্তাহে দুই দিন নারকেল তেল গরম করে ম্যাসাজ করুন।", "Massage warm coconut oil twice a week to strengthen hair roots.", "Not Relevant"),
    ("ইউরিক অ্যাসিডের পরিমাণ কমাতে লাল মাংস ও মসুর ডাল খাওয়া কমান।", "Reduce consumption of red meat and red lentils to decrease uric acid levels.", "Not Relevant"),
    ("পিত্তথলিতে পাথর হলে তলপেটের ডান পাশে তীব্র ব্যথা হতে পারে।", "Gallstones can cause severe pain in the right side of the lower abdomen.", "Not Relevant"),
    ("রোদে বের হওয়ার আগে মুখে ও হাতে সানস্ক্রিন ক্রিম ব্যবহার করুন।", "Use sunscreen cream on face and hands before stepping out in the sun.", "Not Relevant"),
    ("অ্যাসিডিটির সমস্যা হলে খাবার পর বেশিক্ষণ শুয়ে থাকা যাবে না।", "If you have acidity issues , avoid lying down for long after meals.", "Not Relevant"),
    ("শিশুদের নিউমোনিয়া হলে দ্রুত চিকিৎসকের পরামর্শ অনুযায়ী ওষুধ দিন।", "If children contract pneumonia , quickly administer medication according to doctor's advice.", "Not Relevant"),
    ("পায়ের মাংসপেশিতে টান ধরলে হালকা প্রসারিত বা স্ট্রেচ করুন।", "Lightly stretch the muscles if you experience leg muscle cramps.", "Not Relevant"),
    ("মুখের দুর্গন্ধ দূর করতে নিয়মিত মাউথওয়াশ ব্যবহার করা যেতে পারে।", "Regular mouthwash can be used to eliminate bad breath.", "Not Relevant"),
    ("শরীরের কোথাও কেটে গেলে দ্রুত অ্যান্টিসেপটিক দিয়ে ধুয়ে ব্যান্ডেজ করুন।", "If any part of the body is cut , quickly wash with antiseptic and bandage it.", "Not Relevant"),
    ("মাইগ্রেনের ব্যথা উঠলে আলো ও শব্দহীন অন্ধকার ঘরে বিশ্রাম নেওয়া ভালো।", "Resting in a dark room free from light and sound is beneficial during a migraine attack.", "Not Relevant"),
]

print("P1 count:", len(p1_data))

# Prompt 2:
# Genre: 'ঘুমজনিত সমস্যা' / 'Sleep problems'
# Prompt: 'ঘুমের ঘাটতির কারণে সারাদিন রাগ লাগে , সমাধান কী ?'
# Prompt En: 'I feel angry all day due to lack of sleep, what is the solution?'
# HR: 28, PR: 36, NR: 32

p2_genre = "ঘুমজনিত সমস্যা"
p2_genre_en = "Sleep problems"
p2_prompt = "ঘুমের ঘাটতির কারণে সারাদিন রাগ লাগে , সমাধান কী ?"
p2_prompt_en = "I feel angry all day due to lack of sleep, what is the solution?"

p2_data = [
    # Highly Relevant (28)
    ("প্রতিদিন একই সময়ে ঘুমাতে যাওয়া এবং নির্দিষ্ট সময়ে ঘুম থেকে ওঠার নিয়ম মেনে চলুন।", "Follow the rule of going to sleep and waking up at a specific time every day.", "Highly Relevant"),
    ("ঘুমের ঘাটতি মেটাতে রাতে অন্তত ৭ থেকে ৮ ঘণ্টা নিবিড় ঘুমানোর চেষ্টা করুন।", "Try to sleep soundly for at least 7 to 8 hours at night to make up for sleep deficit.", "Highly Relevant"),
    ("ঘুমানোর অন্তত এক ঘণ্টা আগে মোবাইল , ল্যাপটপ বা টিভির স্ক্রিন দেখা বন্ধ করুন।", "Stop looking at mobile , laptop or TV screens at least one hour before sleeping.", "Highly Relevant"),
    ("বিকালে বা সন্ধ্যায় চা-কফি বা ক্যাফেইন জাতীয় পানীয় খাওয়া এড়িয়ে চলুন।", "Avoid drinking tea , coffee or caffeinated drinks in the afternoon or evening.", "Highly Relevant"),
    ("মেজাজ শান্ত রাখতে দিনের বেলা মেডিটেশন বা হালকা শ্বাস-প্রশ্বাসের ব্যায়াম করুন।", "Practice meditation or light breathing exercises during the day to keep your mood calm.", "Highly Relevant"),
    ("শোবার ঘর শান্ত , অন্ধকার এবং শীতল রাখলে রাতে দ্রুত ও ভালো ঘুম হয়।", "Keeping the bedroom quiet , dark and cool ensures fast and good sleep at night.", "Highly Relevant"),
    ("দিনের বেলা ঘুমানোর অভ্যাস থাকলে তা পরিহার করুন বা ২০ মিনিটের বেশি ঘুমাবেন না।", "If you have a habit of sleeping during the day , avoid it or do not sleep more than 20 minutes.", "Highly Relevant"),
    ("মানসিক দুশ্চিন্তা এড়াতে ঘুমানোর আগে বই পড়ার অভ্যাস গড়ে তুলতে পারেন।", "You can form a habit of reading books before sleeping to avoid mental anxiety.", "Highly Relevant"),
    ("রাগ নিয়ন্ত্রণের জন্য রাগ উঠলে মনে মনে এক থেকে দশ পর্যন্ত গুণতে পারেন।", "To control anger , you can count mentally from one to ten when anger arises.", "Highly Relevant"),
    ("শোবার আগে হালকা গরম পানিতে গোসল করলে স্নায়ু শিথিল হয় এবং ঘুম ভালো হয়।", "Taking a warm bath before bedtime relaxes the nerves and improves sleep.", "Highly Relevant"),
    ("রাতে ভারী বা অতিরিক্ত মসলাযুক্ত খাবার এড়িয়ে চলা ঘুমের মান বজায় রাখতে সহায়ক।", "Avoiding heavy or excessively spicy meals at night helps maintain sleep quality.", "Highly Relevant"),
    ("নিয়মিত সকালে সূর্যালোকে কিছুক্ষণ হাঁটলে শরীরে মেলাটোনিন হরমোনের সামঞ্জস্য বজায় থাকে।", "Walking in sunlight for a while every morning maintains melatonin hormone balance in the body.", "Highly Relevant"),
    ("অনিদ্রার কারণে মেজাজ খিটখিটে হলে কাজের ফাঁকে সংক্ষিপ্ত বিরতি নিয়ে বিশ্রাম নিন।", "If insomnia makes you irritable , take short breaks in between work to rest.", "Highly Relevant"),
    ("ঘুমানোর আগে এক গ্লাস হালকা গরম দুধ পান করলে সহজে ঘুম আসতে পারে।", "Drinking a glass of warm milk before bed can help you fall asleep easily.", "Highly Relevant"),
    ("মানসিক চাপ কমাতে নিজের ভালো লাগার কাজগুলো করার জন্য দিনে কিছুটা সময় রাখুন।", "Keep some time during the day for activities you enjoy to reduce mental stress.", "Highly Relevant"),
    ("অতিরিক্ত রাগ উঠলে সাথে সাথে স্থান পরিবর্তন করুন এবং এক গ্লাস ঠান্ডা পানি পান করুন।", "If you feel excessively angry , immediately change your place and drink a glass of cold water.", "Highly Relevant"),
    ("ঘুমের সমস্যার স্থায়ী সমাধানের জন্য কোনো নির্দিষ্ট ঘুমের রুটিন মেনে চলুন।", "Follow a set sleep schedule for a permanent solution to sleep issues.", "Highly Relevant"),
    ("ব্যায়াম বা শারীরিক পরিশ্রম সন্ধ্যার আগেই শেষ করা ঘুমের জন্য ভালো।", "Ending exercise or physical effort before evening is good for sleep.", "Highly Relevant"),
    ("রাগ কমাতে ও শারীরিক ক্লান্তি কাটাতে মনকে অন্যদিকে ঘুরিয়ে নেওয়ার চেষ্টা করুন।", "Try shifting your focus to reduce anger and overcome physical fatigue.", "Highly Relevant"),
    ("শোবার ঘরে ঘড়ির টিকটিক শব্দ বা অপ্রয়োজনীয় আলো থাকলে তা দূর করার ব্যবস্থা নিন।", "Take steps to eliminate ticking clock sounds or unnecessary light in the bedroom.", "Highly Relevant"),
    ("ঘুমের জন্য অ্যালকোহল বা তামাকজাত দ্রব্য সেবন বর্জন করা অত্যন্ত জরুরি।", "Abstaining from alcohol or tobacco products is crucial for sleep.", "Highly Relevant"),
    ("দিনের বেলা শারীরিক পরিশ্রম বাড়ালে রাতে দ্রুত ও গভীর ঘুম আসে।", "Increasing physical exertion during the day brings quick and deep sleep at night.", "Highly Relevant"),
    ("রাগ লাগলে নিজেকে বোঝান যে ঘুমের অভাবই এর মূল কারণ এবং শান্ত থাকুন।", "When angry , remind yourself that lack of sleep is the main cause and stay calm.", "Highly Relevant"),
    ("ঘুমানোর বিছানা শুধুমাত্র ঘুমের জন্য ব্যবহার করুন , অন্য কাজের জন্য নয়।", "Use the sleeping bed only for sleep , not for other activities.", "Highly Relevant"),
    ("নিয়মিত ঘুমের নিয়ম মানার পরও অনিদ্রা না কমলে নিউরোলজিস্টের পরামর্শ নিন।", "If insomnia persists despite following sleep routines , consult a neurologist.", "Highly Relevant"),
    ("রাতের খাবার ঘুমানোর অন্তত দুই থেকে তিন ঘণ্টা আগে শেষ করা উচিত।", "Dinner should be completed at least two to three hours before sleeping.", "Highly Relevant"),
    ("মানসিক উত্তেজনা বা ক্ষোভ দূর করতে আপনার অনুভূতি কারো সাথে শেয়ার করুন।", "Share your feelings with someone to vent mental tension or resentment.", "Highly Relevant"),
    ("ক্রনিক ঘুম না হওয়ার সমস্যা থাকলে ঘুম সম্পর্কিত চিকিৎসকের কাছে যাওয়া প্রয়োজন।", "If you have chronic insomnia , visiting a sleep specialist doctor is necessary.", "Highly Relevant"),

    # Partially Relevant (36)
    ("প্রতিদিন সুষম খাবার খেলে শরীরের রোগ প্রতিরোধ ক্ষমতা শক্তিশালী হয়।", "Eating balanced food daily strengthens the body's immune system.", "Partially Relevant"),
    ("শরীরে পানির অভাব হলে মাথা ঘোরা ও শারীরিক দুর্বলতা দেখা দিতে পারে।", "Lack of water in the body can cause dizziness and physical weakness.", "Partially Relevant"),
    ("চোখের দৃষ্টিশক্তি ভালো রাখতে প্রতিদিন তাজা শাকসবজি ও ফল খাওয়া দরকার।", "Eating fresh vegetables and fruits daily is needed to keep eyesight good.", "Partially Relevant"),
    ("উচ্চ রক্তচাপ নিয়ন্ত্রণে রাখতে খাবারে কাঁচা লবণ খাওয়া থেকে বিরত থাকুন।", "Refrain from eating raw salt in meals to keep high blood pressure under control.", "Partially Relevant"),
    ("শরীরের হাড় মজবুত করার জন্য ভিটামিন 'ডি' ও ক্যালসিয়ামযুক্ত খাবার খান।", "Eat foods rich in Vitamin 'D' and calcium to strengthen body bones.", "Partially Relevant"),
    ("অতিরিক্ত মোবাইল ফোন ব্যবহারের ফলে গর্ভবতী নারীদের চোখের ক্ষতি হতে পারে।", "Excessive mobile phone use can harm the eyes of pregnant women.", "Partially Relevant"),
    ("প্রতিদিন সকালে নিয়ম করে হাঁটাহাঁটি করলে হৃদরোগের ঝুঁকি অনেকটা কমে যায়।", "Walking regularly every morning greatly reduces the risk of heart disease.", "Partially Relevant"),
    ("কাজের চাপ বেশি থাকলে সঠিক সময় ব্যবস্থাপনা শেখা অত্যন্ত প্রয়োজন।", "Learning proper time management is very necessary if work pressure is high.", "Partially Relevant"),
    ("স্মৃতিশক্তি সতেজ রাখতে নিয়মিত নতুন বিষয় শেখার অভ্যাস গড়ে তুলুন।", "Develop a habit of learning new things regularly to keep memory sharp.", "Partially Relevant"),
    ("ওজন নিয়ন্ত্রণে রাখতে অতিরিক্ত চর্বিযুক্ত খাবার এড়িয়ে চলা উচিত।", "Avoiding high-fat foods is essential to keep body weight under control.", "Partially Relevant"),
    ("রক্তে শর্করার মাত্রা বজায় রাখতে মিষ্টি জাতীয় খাবার সীমিত পরিমানে খান।", "Eat sweet foods in limited quantities to maintain blood sugar levels.", "Partially Relevant"),
    ("মন সুস্থ রাখতে নিজের পছন্দের গান শোনা বা বই পড়া একটি ভালো উপায়।", "Listening to favorite music or reading books is a good way to keep the mind healthy.", "Partially Relevant"),
    ("কর্মক্ষেত্রে মনোযোগ বাড়াতে পরিবেশ পরিষ্কার ও শান্ত রাখা দরকার।", "Keeping the environment clean and quiet is needed to boost concentration at work.", "Partially Relevant"),
    ("শারীরিক ক্লান্তি দূর করতে নিয়মিত তাজা ডাবের পানি পান করতে পারেন।", "You can drink fresh green coconut water regularly to relieve physical tiredness.", "Partially Relevant"),
    ("অতিরিক্ত ধূমপান করলে ফুসফুসের কার্যক্ষমতা আশঙ্কাজনকভাবে হ্রাস পায়।", "Excessive smoking dangerously decreases lung capacity.", "Partially Relevant"),
    ("শরীরে রক্তস্বল্পতা থাকলে চিকিৎসকের পরামর্শ অনুযায়ী আয়রন সাপ্লিমেন্ট নিন।", "If you have anemia in the body , take iron supplements as recommended by a doctor.", "Partially Relevant"),
    ("হজমের সমস্যা দূর করতে প্রতিদিন পর্যাপ্ত পরিমাণে শসা ও ফলমূল খান।", "Eat sufficient cucumbers and fruits daily to get rid of digestive issues.", "Partially Relevant"),
    ("দাঁতের সুস্থতা বজায় রাখতে প্রতি ছয় মাস পর পর ডেন্টিস্টের কাছে যাওয়া উচিত।", "One should visit a dentist every six months to maintain dental health.", "Partially Relevant"),
    ("মানসিক ভারসাম্য বজায় রাখতে পরিবারকে পর্যাপ্ত সময় দেওয়া অত্যন্ত জরুরি।", "Giving adequate time to family is extremely vital to maintain mental balance.", "Partially Relevant"),
    ("একটানা কাজ না করে মাঝে মাঝে হাত-পা প্রসারিত করার ব্যায়াম করুন।", "Instead of working continuously , do stretching exercises for hands and legs occasionally.", "Partially Relevant"),
    ("ত্বক ভালো রাখতে পরিষ্কার-পরিচ্ছন্ন থাকা এবং নিয়মিত সাবান ব্যবহার করা দরকার।", "Staying clean and using soap regularly is necessary to keep skin good.", "Partially Relevant"),
    ("শরীরে আয়োডিনের অভাব হলে থাইরয়েডের নানা সমস্যা সৃষ্টি হতে পারে।", "Iodine deficiency in the body can cause various thyroid problems.", "Partially Relevant"),
    ("উদ্বেগমুক্ত জীবনযাপন করতে ইতিবাচক মনোভাব বজায় রাখার চেষ্টা করুন।", "Try to maintain a positive attitude to live an anxiety-free life.", "Partially Relevant"),
    ("দীর্ঘদিন বসে কাজ করলে পিঠ ও কোমর ব্যথার ঝুঁকি বেড়ে যায়।", "Working seated for long durations increases the risk of back and lower back pain.", "Partially Relevant"),
    ("প্রতিদিন সকালে ইসবগুলের ভূষি খেলে কোষ্ঠকাঠিন্য থেকে রক্ষা পাওয়া যায়।", "Drinking isabgol husk every morning protects against constipation.", "Partially Relevant"),
    ("শরীরের বিষাক্ত পদার্থ বের করে দিতে প্রচুর পানি পান করা উচিত।", "Plenty of water should be consumed to flush out toxins from the body.", "Partially Relevant"),
    ("শিশুদের সঠিকভাবে মানসিক বিকাশের জন্য মাঠে খেলাধুলার সুযোগ দেওয়া উচিত।", "Children should be given opportunities to play in fields for proper mental development.", "Partially Relevant"),
    ("অতিরিক্ত চা বা কফি পান করলে পেটে অ্যাসিডিটির মাত্রা বাড়তে পারে।", "Drinking excessive tea or coffee can increase acidity levels in the stomach.", "Partially Relevant"),
    ("ফুসফুস সুস্থ রাখতে প্রতিদিন কিছুক্ষণ দীর্ঘ শ্বাস নেওয়ার ব্যায়াম করুন।", "Do deep breathing exercises for a while daily to keep lungs healthy.", "Partially Relevant"),
    ("বয়স বাড়ার সাথে সাথে শরীরচর্চার ধরন পরিবর্তন করা অত্যন্ত জরুরি।", "Changing the style of exercise as age advances is extremely important.", "Partially Relevant"),
    ("রক্তচাপ স্বাভাবিক রাখতে খাবারে পটাশিয়াম সমৃদ্ধ খাবার যোগ করুন।", "Add potassium-rich foods to your diet to keep blood pressure normal.", "Partially Relevant"),
    ("মানসিক প্রশান্তির জন্য ধর্মীয় বা আধ্যাত্মিক চর্চা ফলপ্রসূ হতে পারে।", "Religious or spiritual practice can be fruitful for mental peace.", "Partially Relevant"),
    ("ত্বকের খসখসে ভাব দূর করতে নিয়মিত ময়শ্চারাইজার ব্যবহার করা উচিত।", "Moisturizer should be used regularly to eliminate skin roughness.", "Partially Relevant"),
    ("মাংসপেশির টান কমাতে হালকা গরম পানির সেক বা ম্যাসাজ নেওয়া যায়।", "Warm compresses or massages can be taken to reduce muscle strain.", "Partially Relevant"),
    ("রোগ মুক্ত থাকতে প্রক্রিয়াজাত বা ফাস্টফুড জাতীয় খাবার ত্যাগ করা শ্রেয়।", "It is better to avoid processed or fast food to stay free from disease.", "Partially Relevant"),
    ("কাজের দক্ষতা বৃদ্ধি করতে প্রতিদিনের কাজের একটি তালিকা তৈরি করুন।", "Create a daily task list to increase work efficiency.", "Partially Relevant"),

    # Not Relevant (32)
    ("চুল পড়া বন্ধ করতে সপ্তাহে দুই দিন পেঁয়াজের রস মাথার তালুতে লাগান।", "Apply onion juice on the scalp twice a week to stop hair fall.", "Not Relevant"),
    ("খুশকি দূর করতে লেবুর রস ও টকদইয়ের পেস্ট চুলে ব্যবহার করুন।", "Use a paste of lemon juice and sour curd on hair to remove dandruff.", "Not Relevant"),
    ("গলা ব্যথা কমাতে হালকা গরম পানিতে আদা ও মধু মিশিয়ে সেবন করুন।", "Consume warm water mixed with ginger and honey to reduce throat pain.", "Not Relevant"),
    ("ব্রণ হলে বারবার সেখানে হাত দেওয়া বা খুঁটানো সম্পূর্ণ নিষেধ।", "Touching or picking acne repeatedly is strictly prohibited.", "Not Relevant"),
    ("হাঁটুর বাত বা জয়েন্টের ব্যথা উপশমে সরিষার তেল দিয়ে হালকা ম্যাসাজ করুন।", "Lightly massage with mustard oil to relieve knee arthritis or joint pain.", "Not Relevant"),
    ("রোদে ত্বক পুড়ে গেলে সেখানে আলুর রস বা অ্যালোভেরা জেল ব্যবহার করুন।", "Apply potato juice or aloe vera gel if skin gets sunburned.", "Not Relevant"),
    ("কাশি ও কফ দূর করতে তুলসী পাতার রস অত্যন্ত কার্যকরী একটি ভেষজ।", "Tulsi leaf juice is an extremely effective herb to cure cough and phlegm.", "Not Relevant"),
    ("পায়ের গোড়ালি ফেটে গেলে রাতে শোবার আগে গ্লিসারিন মেখে সুতির মোজা পরুন।", "If heels crack , apply glycerin and wear cotton socks before going to sleep at night.", "Not Relevant"),
    ("কানের ইনফেকশন এড়াতে কানে পানি ঢোকা থেকে সাবধানে থাকা প্রয়োজন।", "Care is needed to prevent water from entering ears to avoid ear infection.", "Not Relevant"),
    ("পেক্টোরাল বা বুকের পেশি গঠন করতে নিয়মিত ডাম্বেল এক্সারসাইজ করুন।", "Do regular dumbbell exercises to build pectoral or chest muscles.", "Not Relevant"),
    ("ইউরিক অ্যাসিড কমাতে লাল মাংস এবং চিংড়ি মাছ খাওয়া বন্ধ করতে হবে।", "Eating red meat and prawns must be stopped to reduce uric acid.", "Not Relevant"),
    ("ঠোঁট ফেটে গেলে দিনে কয়েকবার ভালো মানের লিপবাম বা পেট্রোলিয়াম জেলি লাগান।", "Apply good quality lip balm or petroleum jelly several times a day if lips crack.", "Not Relevant"),
    ("অ্যাজমা অ্যাটাক হলে সাথে সাথে চিকিৎসকের দেওয়া ইনহেলার ব্যবহার করুন।", "Use the inhaler prescribed by the doctor immediately during an asthma attack.", "Not Relevant"),
    ("চোখের ছানি পড়া প্রতিরোধ করতে সূর্যের বেগুনি রশ্মি থেকে চোখ বাঁচান।", "Protect eyes from ultraviolet sun rays to prevent cataract formation.", "Not Relevant"),
    ("পেটের মেদ কমাতে প্রতিদিন খালি পেটে হালকা গরম পানিতে লেবুর রস পান করুন।", "Drink warm water with lemon juice on an empty stomach daily to reduce belly fat.", "Not Relevant"),
    ("নখের কোণে ইনফেকশন হলে কুসুম গরম পানিতে লবণ দিয়ে পা ভিজিয়ে রাখুন।", "Soak feet in lukewarm salt water if there is an infection at the nail corner.", "Not Relevant"),
    ("মুখের দুর্গন্ধ কাটাতে খাওয়ার পর ভালো করে কুলি করা ও ফ্লস করা উচিত।", "Rinsing mouth well and flossing after meals is recommended to avoid bad breath.", "Not Relevant"),
    ("দাঁতের মাড়ি দিয়ে রক্ত পড়লে ভিটামিন 'সি' সমৃদ্ধ ফল বেশি করে খান।", "Eat more fruits rich in Vitamin 'C' if your gums bleed.", "Not Relevant"),
    ("পিত্তথলিতে পাথর ধরা পড়লে অবিলম্বে বিশেষজ্ঞ সার্জনের পরামর্শ নিন।", "Consult a specialist surgeon immediately if gallstones are detected.", "Not Relevant"),
    ("মাইগ্রেনের তীব্র ব্যথা হলে আলো ও শব্দবিহীন অন্ধকার ঘরে চোখ বন্ধ করে শুয়ে থাকুন।", "Lie down with eyes closed in a dark room without light and sound during severe migraine pain.", "Not Relevant"),
    ("একজিমা বা চর্মরোগ হলে সাবান ব্যবহারে সতর্ক হওয়া অত্যন্ত জরুরি।", "Being cautious with soap use is extremely important in case of eczema or skin diseases.", "Not Relevant"),
    ("শরীরের কোথাও মচকে গেলে বরফের সেক দিন এবং নড়াচড়া বন্ধ রাখুন।", "Apply ice and restrict movement if any part of the body is sprained.", "Not Relevant"),
    ("কিডনি ভালো রাখতে অতিরিক্ত লবণ ও অতিরিক্ত প্রোটিন গ্রহণ এড়িয়ে চলুন।", "Avoid excess salt and excess protein intake to keep kidneys healthy.", "Not Relevant"),
    ("কাঁচা পেঁপেতে থাকা এনজাইম পেটের হজমপ্রক্রিয়াকে ত্বরান্বিত করে।", "Enzymes in raw papaya accelerate the stomach digestion process.", "Not Relevant"),
    ("হাত-পায়ের চামড়া উঠলে রাতে পুষ্টিকর তেল বা ভেসলিন ব্যবহার করুন।", "Use nutritious oil or vaseline at night if skin peels from hands and feet.", "Not Relevant"),
    ("শিশুদের কৃমির সমস্যা হলে নির্দিষ্ট বয়সে কৃমিনাশক ওষুধ খাওয়ানো দরকার।", "Deworming medication needs to be given at a specific age if children have worms.", "Not Relevant"),
    ("জ্বর বা শরীর ব্যথায় সাধারণ প্যারাসিটামল জাতীয় ওষুধ সেবন করা যেতে পারে।", "General paracetamol medication can be taken for fever or body pain.", "Not Relevant"),
    ("ত্বকের পোড়া দাগ দূর করতে কাঁচা হলুদের রস ব্যবহার করে দেখতে পারেন।", "You can try using raw turmeric juice to remove skin burn marks.", "Not Relevant"),
    ("সাইনাসাইটিসের সমস্যায় গরম পানির ভাপ বা স্টিম নিলে বেশ আরাম পাওয়া যায়।", "Taking warm water vapor or steam provides great relief in sinusitis problems.", "Not Relevant"),
    ("পেটের গ্যাস হলে রাতে খাবার পর কিছুক্ষণ পাইচারি করা ভালো।", "Walking around for a while after dinner is good if you have stomach gas.", "Not Relevant"),
    ("কানের ভেতরের ময়লা পরিষ্কার করতে ড্রপ ব্যবহার করা নিরাপদ।", "Using drops is safe to clean inside earwax.", "Not Relevant"),
    ("রক্তশূন্যতা দূর করতে পালং শাক ও খেজুর খাদ্য তালিকায় অন্তর্ভুক্ত করুন।", "Include spinach and dates in your diet to overcome anemia.", "Not Relevant"),
]

print("P2 count:", len(p2_data))

# Prompt 3:
# Genre: 'চুল জনিত' / 'Hairy'
# Prompt: 'মাথায় খুশকি বেড়েছে , চুল পড়ে যাচ্ছে , সমাধান কি'
# Prompt En: 'Dandruff has increased on my head, my hair is falling out, what is the solution?'
# HR: 28, PR: 36, NR: 32

p3_genre = "চুল জনিত"
p3_genre_en = "Hairy"
p3_prompt = "মাথায় খুশকি বেড়েছে , চুল পড়ে যাচ্ছে , সমাধান কি"
p3_prompt_en = "Dandruff has increased on my head, my hair is falling out, what is the solution?"

p3_data = [
    # Highly Relevant (28)
    ("মাথার খুশকি কমাতে সপ্তাহে দুই দিন কিটোকোনাজলযুক্ত অ্যান্টি-ড্যানড্রফ শ্যাম্পু ব্যবহার করুন।", "Use a ketoconazole anti-dandruff shampoo twice a week to reduce scalp dandruff.", "Highly Relevant"),
    ("চুল পড়া রোধে মাথার তালু সর্বদা পরিষ্কার এবং অতিরিক্ত ঘাম মুক্ত রাখা জরুরি।", "Keeping the scalp clean and free from excess sweat is vital to prevent hair loss.", "Highly Relevant"),
    ("খুশকি তাড়াতে লেবুর রস ও টকদই মিশিয়ে মাথার তালুতে মেখে ২০ মিনিট পর ধুয়ে ফেলুন।", "Mix lemon juice and sour curd , apply on the scalp and rinse off after 20 minutes to eliminate dandruff.", "Highly Relevant"),
    ("চুলের গোড়া মজবুত করতে প্রোটিন ও ভিটামিন 'ই' সমৃদ্ধ খাবার বেশি করে গ্রহণ করুন।", "Eat more foods rich in protein and Vitamin 'E' to strengthen hair roots.", "Highly Relevant"),
    ("খুশকি ও চুল পড়া কমাতে তোয়ালে , চিরুনি বা বালিশের কভার কারো সাথে শেয়ার করবেন না।", "Do not share towels , combs or pillow covers with anyone to reduce dandruff and hair fall.", "Highly Relevant"),
    ("মাথার চুল ভেজা অবস্থায় আঁচড়ানো বন্ধ করুন , কারণ এতে চুলের গোড়া আলগা হয়ে যায়।", "Stop combing wet hair , as it loosens the hair roots.", "Highly Relevant"),
    ("নিম পাতা সেদ্ধ পানি দিয়ে চুল ধুলে মাথার খুশকি ও জীবাণুর সংক্রমণ দ্রুত দূর হয়।", "Rinsing hair with neem leaf boiled water quickly removes scalp dandruff and germ infections.", "Highly Relevant"),
    ("চুল পড়া কমাতে প্রতিদিন পর্যাপ্ত পানি এবং শাকসবজি খাদ্য তালিকায় রাখা প্রয়োজন।", "Including sufficient water and vegetables in the daily diet is required to reduce hair fall.", "Highly Relevant"),
    ("চুলের অতিরিক্ত রুক্ষতা কাটাতে ও খুশকি প্রতিরোধে সপ্তাহে একদিন মেথি বাটা ব্যবহার করুন।", "Use fenugreek paste once a week to eliminate excessive hair dryness and prevent dandruff.", "Highly Relevant"),
    ("কেমিক্যালযুক্ত হেয়ার ডাই বা স্ট্রেইটনার ব্যবহার বন্ধ করলে চুল পড়া অনেক কমে যায়।", "Stopping the use of chemical hair dyes or straighteners greatly reduces hair fall.", "Highly Relevant"),
    ("খুশকির সমস্যা বেশি হলে চিকিৎসকের পরামর্শে নির্দিষ্ট অ্যান্টি-ফাঙ্গাল লোশন ব্যবহার করুন।", "If dandruff problem is severe , use specific anti-fungal lotion advised by a doctor.", "Highly Relevant"),
    ("চুলের গোড়ায় রক্ত সঞ্চালন বাড়াতে হালকা গরম নারকেল তেল দিয়ে তালু ম্যাসাজ করুন।", "Massage scalp with warm coconut oil to increase blood circulation in hair roots.", "Highly Relevant"),
    ("চুল পড়া কমাতে মানসিক দুশ্চিন্তা এড়িয়ে চলুন এবং রাতে ৮ ঘণ্টা ঘুমান।", "Avoid mental stress and sleep 8 hours at night to reduce hair fall.", "Highly Relevant"),
    ("অ্যালোভেরা জেল সরাসরি মাথায় মেখে ৩০ মিনিট রাখলে খুশকি কমে এবং চুল নরম হয়।", "Applying aloe vera gel directly on head and keeping it for 30 minutes reduces dandruff and softens hair.", "Highly Relevant"),
    ("চুলে ক্ষতিকর শ্যাম্পুর বদলে মাইল্ড বা ভেষজ শ্যাম্পু ব্যবহার করা নিরাপদ।", "Using mild or herbal shampoo instead of harsh shampoo on hair is safe.", "Highly Relevant"),
    ("ভিটামিন ও জিংকের অভাবজনিত চুল পড়া বন্ধে ডাক্তারের পরামর্শে ভিটামিন ট্যাবলেট নিন।", "Take vitamin tablets on doctor's advice to stop hair loss caused by vitamin and zinc deficiency.", "Highly Relevant"),
    ("মাথার চুল অতিরিক্ত গরম পানি দিয়ে ধুলে খুশকি বাড়ে , তাই হালকা ঠান্ডা পানি ব্যবহার করুন।", "Washing hair with excessively hot water increases dandruff , so use lukewarm or cool water.", "Highly Relevant"),
    ("পেঁয়াজের রস মাথার তালুতে লাগিয়ে ২০ মিনিট রাখলে নতুন চুল গজাতে সাহায্য করে।", "Applying onion juice on the scalp for 20 minutes helps grow new hair.", "Highly Relevant"),
    ("খুশকির জন্য মাথার ত্বকে চুলকানি হলে নক দিয়ে না চুলকে আঙ্গুলের মাথা ব্যবহার করুন।", "If scalp itches due to dandruff , use fingertips instead of scratching with nails.", "Highly Relevant"),
    ("চুলের পুষ্টি যোগাতে ডিমে থাকা প্রোটিন ও কাস্টর অয়েল দিয়ে প্যাক তৈরি করে লাগান।", "Prepare and apply a hair pack with egg protein and castor oil to nourish hair.", "Highly Relevant"),
    ("রোদ ও ধুলোবালি থেকে চুলকে রক্ষা করতে বাইরে বের হওয়ার সময় ক্যাপ ব্যবহার করুন।", "Use a cap when going outside to protect hair from sun and dust.", "Highly Relevant"),
    ("চুলের গোড়া শক্ত করতে ডিমের কুসুম ও আমলকীর রস একসাথে মেখে ধুয়ে ফেলুন।", "Mix egg yolk and amla juice together and wash off to strengthen hair roots.", "Highly Relevant"),
    ("খুশকি ও চুল পড়ার স্থায়ী সমাধানের জন্য নিয়মিত হেয়ার কেয়ার রুটিন মেনে চলুন।", "Follow a regular hair care routine for a permanent solution to dandruff and hair fall.", "Highly Relevant"),
    ("চুলের আর্দ্রতা বজায় রাখতে কেমিক্যাল শ্যাম্পু ব্যবহারের পর কন্ডিশনার প্রয়োগ করুন।", "Apply conditioner after using chemical shampoo to maintain hair moisture.", "Highly Relevant"),
    ("মাথার ত্বক শুষ্ক হয়ে খুশকি হলে সপ্তাহে দুইবার নারিকেল তেল হালকা গরম করে ব্যবহার করুন।", "If scalp becomes dry causing dandruff , use warm coconut oil twice a week.", "Highly Relevant"),
    ("অতিরিক্ত হেয়ার ড্রায়ার দিয়ে চুল শুকালে চুল ভেঙে যাওয়া ও পড়ার প্রবণতা বাড়ে।", "Drying hair with excessive hair dryers increases hair breakage and falling tendency.", "Highly Relevant"),
    ("শরীরে আয়রনের ঘাটতি চুল পড়ার অন্যতম কারণ , তাই আয়রনযুক্ত খাবার বেশি করে খান।", "Iron deficiency in the body is a key cause of hair fall , so eat more iron-rich foods.", "Highly Relevant"),
    ("যদি কোনো কিছুতেই খুশকি ও চুল পড়া না কমে , তবে ডার্মাটোলজিস্টের পরামর্শ নিন।", "If nothing reduces dandruff and hair fall , consult a dermatologist.", "Highly Relevant"),

    # Partially Relevant (36)
    ("ত্বকের সৌন্দর্য ধরে রাখতে প্রতিদিন প্রচুর পরিমাণে বিশুদ্ধ পানি পান করা উচিত।", "Drinking plenty of pure water daily is essential to preserve skin beauty.", "Partially Relevant"),
    ("নিয়মিত শারীরিক এক্সারসাইজ করলে শরীরের রক্ত সঞ্চালন বৃদ্ধি পায়।", "Doing regular physical exercise increases blood circulation in the body.", "Partially Relevant"),
    ("ত্বক উজ্জ্বল রাখতে ভিটামিন 'সি' সমৃদ্ধ ফলমূল নিয়মিত খাদ্য তালিকায় রাখুন।", "Keep Vitamin 'C' rich fruits in daily diet regularly to maintain bright skin.", "Partially Relevant"),
    ("উচ্চ রক্তচাপ এড়াতে অতিরিক্ত চর্বি ও লবণযুক্ত খাবার বর্জন করা জরুরি।", "Avoiding excessive fat and salty food is essential to prevent high blood pressure.", "Partially Relevant"),
    ("চোখের সুরক্ষায় রোদ চশমা ব্যবহার করা এবং কম আলোতে কাজ না করা ভালো।", "Using sunglasses and avoiding work in low light is good for eye protection.", "Partially Relevant"),
    ("হজমের সমস্যা সমাধানে খাবারের সাথে কাঁচা সালাদ ও আঁশযুক্ত খাবার খান।", "Eat raw salad and fiber-rich food with meals to solve digestive issues.", "Partially Relevant"),
    ("দাঁত মজবুত রাখতে সকালে ও রাতে ঘুমানোর আগে ব্রাশ করার অভ্যাস করুন।", "Form a habit of brushing teeth in the morning and before sleeping at night to keep them strong.", "Partially Relevant"),
    ("শারীরিক দুর্বলতা দূর করতে প্রতিদিন দুধে খেজুর মিশিয়ে সেবন করতে পারেন।", "You can consume dates mixed in milk daily to overcome physical weakness.", "Partially Relevant"),
    ("ত্বকের খসখসে ভাব কাটাতে গোসলের পর ভালো মানের লোশন ব্যবহার করুন।", "Use a good quality lotion after bath to eliminate skin roughness.", "Partially Relevant"),
    ("মানসিক স্বাস্থ্যের জন্য প্রতিদিন অন্তত ৭ ঘণ্টা ঘুমানো অত্যন্ত দরকার।", "Sleeping at least 7 hours daily is extremely necessary for mental health.", "Partially Relevant"),
    ("ওজন কমাতে হালকা গরম পানিতে মধু ও লেবুর রস মিশিয়ে পান করুন।", "Drink warm water mixed with honey and lemon juice to lose weight.", "Partially Relevant"),
    ("কাশি দূর করতে তুলসী পাতার রস ও মধু খাওয়া বেশ প্রাচীন ও জনপ্রিয় উপায়।", "Drinking tulsi leaf juice and honey is an ancient and popular remedy for cough.", "Partially Relevant"),
    ("হাড় সুস্থ রাখতে নিয়মিত রোদে কিছুক্ষণ বসা ও ক্যালসিয়াম খাবার গ্রহণ করা উচিত।", "One should sit in the sun for a while and intake calcium food regularly for healthy bones.", "Partially Relevant"),
    ("মন সতেজ রাখতে পরিবারের সাথে সময় কাটানো বা ভ্রমণ করা ভালো।", "Spending time with family or traveling is good to keep the mind fresh.", "Partially Relevant"),
    ("কোষ্ঠকাঠিন্য প্রতিরোধ করতে রাতে ঘুমানোর আগে ইসবগুলের ভূষি খাওয়া ভালো।", "Eating isabgol husk before bed at night is good for preventing constipation.", "Partially Relevant"),
    ("কাজের দক্ষতা ও মনোযোগ বাড়াতে কাজের জায়গায় নিরিবিলি পরিবেশ বজায় রাখুন।", "Maintain a quiet environment at the workplace to boost work efficiency and focus.", "Partially Relevant"),
    ("অ্যাসিডিটির সমস্যা হলে অতিরিক্ত তেল ও মসলাজাতীয় খাবার খাওয়া বাদ দিন।", "Avoid eating excess oil and spicy foods if you have acidity problems.", "Partially Relevant"),
    ("হাত পরিষ্কার না করে মুখমণ্ডল স্পর্শ করলে ত্বকে ব্যাকটেরিয়ার সংক্রমণ ঘটে।", "Bacterial infection occurs on skin if face is touched without cleaning hands.", "Partially Relevant"),
    ("শরীরে ভিটামিনের ঘাটতি হলে দ্রুত ক্লান্তি অনুভব হতে পারে।", "Feeling tired quickly can happen if there is a vitamin deficiency in the body.", "Partially Relevant"),
    ("মাথাব্যথা কমাতে কিছুক্ষণ চোখ বন্ধ করে অন্ধকার স্থানে বিশ্রাম নিন।", "Rest in a dark place with eyes closed for a while to relieve headache.", "Partially Relevant"),
    ("ব্রণ এড়াতে মুখে অতিরিক্ত কেমিক্যালযুক্ত প্রসাধনী ব্যবহার করা বন্ধ করুন।", "Stop using excessive chemical cosmetics on the face to avoid acne.", "Partially Relevant"),
    ("হৃদরোগ এড়াতে ধূমপান ও অ্যালকোহল জাতীয় পানীয় সম্পূর্ণ পরিহার করুন।", "Completely avoid smoking and alcohol to prevent heart disease.", "Partially Relevant"),
    ("নখ পরিষ্কার ও ছোট রাখলে খাদ্যের মাধ্যমে রোগজীবাণু পেটে প্রবেশ করে না।", "Keeping nails clean and short prevents disease germs from entering stomach through food.", "Partially Relevant"),
    ("বয়স অনুযায়ী শারীরিক ব্যায়াম নির্বাচন করা শরীর সুস্থ রাখার জন্য উত্তম।", "Selecting physical exercises according to age is best to keep the body healthy.", "Partially Relevant"),
    ("উদ্বেগমুক্ত থাকতে নিয়মিত ধ্যান করা বা ধর্মীয় বই পড়া উপকারী।", "Practicing regular meditation or reading religious books is beneficial to remain anxiety-free.", "Partially Relevant"),
    ("দাঁতের মাড়ি শক্ত করতে ভিটামিন 'সি' যুক্ত ফল যেমন পেয়ারা ও লেবু খান।", "Eat Vitamin 'C' rich fruits like guava and lemon to strengthen gums.", "Partially Relevant"),
    ("শরীরের ভারসাম্য বজায় রাখতে সকালের নাশতা কখনোই বাদ দেওয়া উচিত নয়।", "Morning breakfast should never be skipped to maintain body balance.", "Partially Relevant"),
    ("হাত-পায়ের পেশিতে টান ধরলে হালকা গরম পানি দিয়ে ধুয়ে ম্যাসাজ করুন।", "Wash with warm water and massage if you get cramps in hand-leg muscles.", "Partially Relevant"),
    ("রোগ মুক্ত জীবন কাটাতে খাবারে কৃত্রিম রঙ বা প্রিজারভেটিভ ব্যবহার করবেন না।", "Do not use artificial color or preservatives in food to live a disease-free life.", "Partially Relevant"),
    ("শরীরে জমে থাকা দূষিত উপাদান বের করতে দৈনিক সবুজ শাকসবজি খান।", "Eat green vegetables daily to flush out toxic elements accumulated in the body.", "Partially Relevant"),
    ("ডায়াবেটিস রোগীদের প্রতিদিন নির্দিষ্ট সময় ধরে হাঁটার পরামর্শ দেওয়া হয়।", "Diabetic patients are advised to walk for a set duration every day.", "Partially Relevant"),
    ("চোখের লালচে ভাব কমাতে পরিষ্কার ঠাণ্ডা পানি দিয়ে চোখ ধুয়ে নিন।", "Wash eyes with clean cold water to reduce eye redness.", "Partially Relevant"),
    ("অতিরিক্ত চাপ থেকে মুক্ত থাকতে কোনো বিনোদনমূলক কাজে অংশ নিন।", "Take part in recreational activities to free yourself from extra stress.", "Partially Relevant"),
    ("শরীরের পেশি সুস্থ রাখতে নিয়মিত প্রোটিনযুক্ত খাদ্য গ্রহণ করুন।", "Consume protein-rich foods regularly to keep body muscles healthy.", "Partially Relevant"),
    ("ঠান্ডা লাগলে আদা চা পান করলে গলায় বেশ আরাম অনুভব হয়।", "Drinking ginger tea gives great comfort in the throat when affected by cold.", "Partially Relevant"),
    ("স্মৃতিশক্তি বৃদ্ধিতে সাহায্য করতে বাদাম ও ওমেগা সমৃদ্ধ খাবার ভালো।", "Nuts and omega-rich foods are good for helping improve memory.", "Partially Relevant"),

    # Not Relevant (32)
    ("গলা ব্যথা নিরাময়ে কুসুম গরম পানিতে লবণ মিশিয়ে কুলকুচা করুন।", "Gargle with lukewarm salt water to relieve throat pain.", "Not Relevant"),
    ("পায়ের গোড়ালি ফেটে গেলে প্রতি রাতে ভালো পেট্রোলিয়াম জেলি মাখুন।", "Apply good petroleum jelly every night if your heels crack.", "Not Relevant"),
    ("কাশি ও কফ দূর করতে গরম পানিতে ভাপ বা স্টিম নেওয়া কার্যকরী।", "Taking warm water vapor or steam is effective in clearing cough and phlegm.", "Not Relevant"),
    ("পেক্টোরাল পেশি মজবুত করতে জিমে গিয়ে নির্দিষ্ট চেস্ট এক্সারসাইজ করুন।", "Go to the gym and do specific chest exercises to strengthen pectoral muscles.", "Not Relevant"),
    ("পিত্তথলির পাথর এড়াতে মেদবহুল শরীর নিয়ন্ত্রণ করা অত্যন্ত জরুরি।", "Controlling overweight body is extremely vital to avoid gallstones.", "Not Relevant"),
    ("অ্যাজমা থাকলে ধুলাবালি ও ধোঁয়াযুক্ত পরিবেশ থেকে দূরত্ব বজায় রাখুন।", "Maintain distance from dusty and smoky environments if you have asthma.", "Not Relevant"),
    ("ইউরিক অ্যাসিড বৃদ্ধি পেলে লাল মাংস ও মসুর ডাল খাওয়া বন্ধ করুন।", "Stop eating red meat and red lentils if uric acid increases.", "Not Relevant"),
    ("হাইপারটেনশন কমাতে খাবারে অতিরিক্ত কাঁচা লবণ যোগ করা থেকে বিরত থাকুন।", "Refrain from adding extra raw salt to food to reduce hypertension.", "Not Relevant"),
    ("হাঁটুর ব্যথা কমাতে প্রতিদিন হাঁটুর নিচে বালিশ দিয়ে বিশ্রাম নিন।", "Rest with a pillow under knees daily to reduce knee pain.", "Not Relevant"),
    ("মাইগ্রেন উঠলে অন্ধকার ঘরে চোখ বন্ধ করে শান্ত হয়ে বসে থাকুন।", "Sit quietly with eyes closed in a dark room during a migraine attack.", "Not Relevant"),
    ("কোষ্ঠকাঠিন্যের সমস্যায় প্রতিদিন পর্যাপ্ত আঁশযুক্ত খাবার গ্রহণ করা উচিত।", "Adequate fiber-rich food should be consumed daily for constipation problems.", "Not Relevant"),
    ("চোখের পাওয়ার বা চশমার জটিলতায় বিশেষজ্ঞ চক্ষু ডাক্তারের পরামর্শ নিন।", "Consult a specialist eye doctor for eye power or glasses complications.", "Not Relevant"),
    ("কানে বেশি ময়লা জমলে কান পরিষ্কারের ড্রপ ব্যবহার করা ভালো।", "It is good to use ear cleaning drops if excess wax accumulates in ears.", "Not Relevant"),
    ("ত্বকে এলার্জি বা র‍্যাশ হলে সাবানের ব্যবহার সাময়িকভাবে বন্ধ রাখুন।", "Temporarily stop using soap if skin has allergies or rashes.", "Not Relevant"),
    ("নখে ইনফেকশন দেখা দিলে অ্যান্টিসেপটিক দিয়ে পরিষ্কার করে শুকনো রাখুন।", "Clean with antiseptic and keep dry if an infection appears on nails.", "Not Relevant"),
    ("পেটের গ্যাস ও পেট ফাঁপা কমাতে খাওয়ার সাথে সাথে পানি খাবেন না।", "Do not drink water immediately with meals to reduce stomach gas and bloating.", "Not Relevant"),
    ("শিশুদের নিউমোনিয়া প্রতিরোধ করতে সঠিক সময়ে সব টিকা দেওয়া নিশ্চিত করুন।", "Ensure all vaccinations are given on time to prevent pneumonia in children.", "Not Relevant"),
    ("মুখের দুর্গন্ধ এড়াতে প্রতিদিন জিহ্বা পরিষ্কার করার অভ্যাস গড়ে তুলুন।", "Develop a habit of cleaning tongue daily to avoid bad mouth odor.", "Not Relevant"),
    ("শরীরের কেটে যাওয়া স্থানে লবণের পানি বা ময়লা ঢুকতে দেবেন না।", "Do not allow salt water or dirt to enter cuts on the body.", "Not Relevant"),
    ("গ্যাস্ট্রিকের ব্যথায় খালি পেটে আদা চিবিয়ে খেলে দ্রুত উপশম মিলতে পারে।", "Chewing ginger on an empty stomach can yield quick relief in gastric pain.", "Not Relevant"),
    ("পায়ের পেশিতে খিঁচ লাগলে বরফের সেক দেওয়া ভালো উপায়।", "Applying ice compresses is a good way if leg muscles cramp.", "Not Relevant"),
    ("ডায়াবেটিস রোগীদের মিষ্টি ও চিনিযুক্ত শরবত খাওয়া একদম নিষেধ।", "Diabetic patients are strictly forbidden from drinking sweet and sugary syrups.", "Partially Relevant" if False else "Not Relevant"),
    ("রক্তশূন্যতা দূর করতে প্রতিদিনের খাবারে মেথি ও কচু শাক রাখুন।", "Keep fenugreek and taro greens in daily meals to cure anemia.", "Not Relevant"),
    ("সর্দি-কাশি হলে তুলসী পাতা ও গোলমরিচ ফুটিয়ে চা বানিয়ে পান করুন।", "Boil tulsi leaves and black pepper to make tea and drink if you have a cold-cough.", "Not Relevant"),
    ("কোমর ব্যথা বাড়লে সোজা হয়ে ঘুমানোর এবং শক্ত তোশক ব্যবহারের অভ্যাস করুন।", "Practice sleeping straight and using a firm mattress if back pain increases.", "Not Relevant"),
    ("ত্বকের কালচে দাগ দূর করতে শসার রস ও গোলাপ জল ব্যবহার করুন।", "Use cucumber juice and rose water to remove skin dark spots.", "Not Relevant"),
    ("দাঁতের ক্ষয় কাটাতে অতিরিক্ত মিষ্টি ও কোল্ড ড্রিংকস পান পরিহার করুন।", "Avoid drinking excess sweets and cold drinks to overcome tooth decay.", "Not Relevant"),
    ("অ্যাসিডিটি হলে খাবারের সাথে সাথে অতিরিক্ত পানি পান করা অনুচিত।", "Drinking excess water along with meals is inappropriate during acidity.", "Not Relevant"),
    ("শরীরের হাড়ের জোড়ায় ব্যথা হলে গরম শেক দিলে বেশ আরাম লাগে।", "Applying warm compresses gives great comfort if there is pain in body joints.", "Not Relevant"),
    ("কাঁচা পেঁপে সালাদ হিসেবে খেলে হজমশক্তি ও লিভারের ক্ষমতা বৃদ্ধি পায়।", "Eating raw papaya as salad increases digestive power and liver function.", "Not Relevant"),
    ("কানের ড্রাম বা পর্দায় ফুটো থাকলে চিকিৎসকের পরামর্শ ছাড়া ড্রপ দেবেন না।", "Do not give drops without a doctor's advice if there is a hole in ear drum.", "Not Relevant"),
    ("সানবার্ন প্রতিরোধ করতে কড়া রোদে বের হওয়ার সময় ছাতা বা হ্যাট ব্যবহার করুন।", "Use an umbrella or hat when going out in harsh sun to prevent sunburn.", "Not Relevant"),
]

print("P3 count:", len(p3_data))

# Prompt 4:
# Genre: 'শীত জনিত সমস্যা' / 'Winter-related problems'
# Prompt: 'ঠান্ডা লাগলে আমার ঠোঁট ফেটে যায় এবং মুখের ত্বক রুক্ষ হয়ে যায় , যার ফলে প্রতিদিন লিপবাম ব্যবহার করলেও আরাম পাওয়া আমার পক্ষে কঠিন হয়ে পড়ে'
# Prompt En: 'When I get cold, my lips crack and my skin becomes rough, making it difficult for me to find comfort even if I use lip balm every day.'
# HR: 24, PR: 36, NR: 32

p4_genre = "শীত জনিত সমস্যা"
p4_genre_en = "Winter-related problems"
p4_prompt = "ঠান্ডা লাগলে আমার ঠোঁট ফেটে যায় এবং মুখের ত্বক রুক্ষ হয়ে যায় , যার ফলে প্রতিদিন লিপবাম ব্যবহার করলেও আরাম পাওয়া আমার পক্ষে কঠিন হয়ে পড়ে"
p4_prompt_en = "When I get cold, my lips crack and my skin becomes rough, making it difficult for me to find comfort even if I use lip balm every day."

p4_data = [
    # Highly Relevant (24)
    ("শীতকালে ত্বক ও ঠোঁট আর্দ্র রাখতে পেট্রোলিয়াম জেলি বা প্রাকৃতিক ঘি ব্যবহার করুন।", "Use petroleum jelly or natural ghee to keep skin and lips moisturized during winter.", "Highly Relevant"),
    ("ঠোঁট ফাটা ও রুক্ষতা কমাতে লিপবাম ব্যবহারের পাশাপাশি প্রচুর পানি পান করুন।", "Drink plenty of water alongside using lip balm to reduce cracked lips and dryness.", "Highly Relevant"),
    ("মুখের ত্বক খসখসে হলে গোসলের পর ত্বকে ভালো মানের ময়েশ্চারাইজার প্রয়োগ করুন।", "Apply a good quality moisturizer on skin after bath if face skin becomes rough.", "Highly Relevant"),
    ("ঠোঁটের শুষ্কতা দূর করতে রাতে ঘুমানোর আগে গ্লিসারিন ও গোলাপ জল মাখুন।", "Apply glycerin and rose water before sleeping at night to eliminate lip dryness.", "Highly Relevant"),
    ("শীতের ঠান্ডা বাতাসে বাইরে যাওয়ার সময় মুখ ও ঠোঁট স্কার্ফ দিয়ে ঢেকে রাখুন।", "Cover face and lips with a scarf when stepping outside in cold winter winds.", "Highly Relevant"),
    ("ঠোঁট বারবার জিব দিয়ে ভিজানোর অভ্যাস ত্যাগ করুন , এতে ঠোঁট আরও বেশি ফাটে।", "Abandon the habit of constantly licking lips , as it makes lips crack even more.", "Highly Relevant"),
    ("ত্বকের শুষ্কতা কমাতে অতিরিক্ত গরম পানি দিয়ে মুখ বা শরীর ধোয়া বন্ধ করুন।", "Stop washing face or body with excessively hot water to reduce skin dryness.", "Highly Relevant"),
    ("ঠোঁটের মরা চামড়া তুলতে হালকা হাতে চিনি ও নারকেল তেলের স্ক্রাব ব্যবহার করুন।", "Use a gentle sugar and coconut oil scrub to remove dead skin from lips.", "Highly Relevant"),
    ("শীতকালে মুখে সাবান কম ব্যবহার করে মাইল্ড ক্লিঞ্জার বা ফেসওয়াশ ব্যবহার করুন।", "Use less soap on face during winter and use a mild cleanser or facewash.", "Highly Relevant"),
    ("ত্বকের গভীর আর্দ্রতার জন্য রাতে ঘুমানোর আগে অ্যালোভেরা জেল ও ভিটামিন 'ই' ক্যাপসুল লাগান।", "Apply aloe vera gel and Vitamin 'E' capsules before bed for deep skin moisture.", "Highly Relevant"),
    ("শীতের দিনে ঘরে হিউমিডিফায়ার ব্যবহার করলে বাতাসের আর্দ্রতা ও ত্বকের কোমলতা বজায় থাকে।", "Using a humidifier in room during winter days maintains air moisture and skin softness.", "Highly Relevant"),
    ("ঠোঁট ফাটা বন্ধ করতে শিয়া বাটার যুক্ত প্রাকৃতিক লিপবাম বা অলিম্পাস বাম ব্যবহার করুন।", "Use natural lip balm containing shea butter to stop lip cracking.", "Highly Relevant"),
    ("অতিরিক্ত ঠান্ডা আবহাওয়ায় ত্বক ও ঠোঁটের ময়েশ্চার ধরে রাখতে অলিভ অয়েল দিয়ে ম্যাসাজ করুন।", "Massage with olive oil to retain skin and lip moisture in extremely cold weather.", "Highly Relevant"),
    ("শীতকালে শরীরে ভিটামিন 'বি' ও জিংকের ঘাটতি ঠোঁট ফাটার কারণ হতে পারে , তাই পুষ্টিকর খাবার খান।", "Deficiency of Vitamin 'B' and zinc in winter can cause cracked lips , so eat nutritious food.", "Highly Relevant"),
    ("ঠোঁট থেকে চামড়া উঠে রক্ত পড়লে কোনো অ্যান্টিসেপটিক অয়েল বা বোরিক বাম লাগান।", "Apply an antiseptic oil or boric balm if skin peels from lips and bleeds.", "Highly Relevant"),
    ("মুখের রুক্ষতা দূর করতে সপ্তাহে দুই দিন মধু ও টকদইয়ের ফেসপ্যাক ব্যবহার করুন।", "Use a honey and sour curd face pack twice a week to remove face dryness.", "Highly Relevant"),
    ("শীতের তীব্রতায় সাধারণ লিপবামে কাজ না হলে ডার্মাটোলজিস্টের দেওয়া মেডিকেল লিপ বাম ব্যবহার করুন।", "Use medical lip balm prescribed by a dermatologist if general lip balm fails in harsh cold.", "Highly Relevant"),
    ("ঠান্ডায় ত্বক অতিরিক্ত শুষ্ক হলে স্নানের পানিতে কয়েক ফোঁটা বাদাম তেল মেশান।", "Mix a few drops of almond oil in bath water if skin becomes extremely dry in cold.", "Highly Relevant"),
    ("ঠোঁট ও ত্বকের স্বাস্থ্য ভালো রাখতে শীতকালীন তাজা ফল ও শাকসবজি খাদ্য তালিকায় রাখুন।", "Include winter fresh fruits and vegetables in your diet to keep lips and skin healthy.", "Highly Relevant"),
    ("মুখের ত্বক কোমল রাখতে ক্ষতিকর ক্যামিক্যালমুক্ত প্রাকৃতিক ময়েশ্চারাইজিং ক্রিম পছন্দ করুন।", "Choose natural moisturizing creams free from harmful chemicals to keep face skin soft.", "Highly Relevant"),
    ("শীতে ঠোঁট ফেটে জ্বলুনি হলে কাঁচা দুধ ও হলুদ বাটা হালকাভাবে চুলে ও ঠোঁটে মাখুন।", "Gently apply raw milk and turmeric paste on lips if cracked lips burn in winter.", "Highly Relevant"),
    ("রোদে যাওয়ার আগে সানস্কিন যুক্ত লিপবাম ও লোশন ব্যবহার করলে ঠান্ডা ও রোদের ক্ষতি এড়ানো যায়।", "Using sunscreen-enabled lip balm and lotion before sun exposure prevents cold and sun damage.", "Highly Relevant"),
    ("শীতের রাতে ত্বকে সরিষার তেল না মেখে হালকা কোনো অ-চটচটে ময়েশ্চারাইজিং তেল ব্যবহার করুন।", "Use a light non-sticky moisturizing oil on skin at winter night instead of mustard oil.", "Highly Relevant"),
    ("যদি তীব্র শুষ্কতা ও ঠোঁট ফাটা কোনোভাবেই না কমে , তবে চর্মরোগ বিশেষজ্ঞের কাছে যান।", "If severe dryness and lip cracking do not improve by any means , visit a dermatologist.", "Highly Relevant"),

    # Partially Relevant (36)
    ("শীতকালে ঠান্ডা লাগা ও সর্দি-কাশি এড়াতে পর্যাপ্ত গরম কাপড় পরিধান করুন।", "Wear adequate warm clothes in winter to avoid catching cold and cough.", "Partially Relevant"),
    ("শরীরের রোগ প্রতিরোধ ক্ষমতা বাড়াতে নিয়মিত তাজা ফলমূল গ্রহণ করা জরুরি।", "Eating fresh fruits regularly is essential to boost body's immunity.", "Partially Relevant"),
    ("প্রতিদিন নিয়ম করে অন্তত ৭ থেকে ৮ ঘণ্টা ঘুমানো শারীরিক সুস্থতার জন্য প্রয়োজন।", "Sleeping at least 7 to 8 hours regularly daily is needed for physical health.", "Partially Relevant"),
    ("উচ্চ রক্তচাপ নিয়ন্ত্রণে রাখতে প্রতিদিনের খাবারে লবণের পরিমাণ সীমিত রাখুন।", "Limit the amount of salt in daily food to keep high blood pressure under control.", "Partially Relevant"),
    ("চুলের স্বাস্থ্য ভালো রাখতে সপ্তাহে দুই দিন উষ্ণ তেল দিয়ে মাথার তালু ম্যাসাজ করুন।", "Massage scalp with warm oil twice a week to keep hair healthy.", "Partially Relevant"),
    ("শারীরিক দুর্বলতা দূর করতে প্রতিদিন সকালে ভিজানো বাদাম ও কিশমিশ খান।", "Eat soaked almonds and raisins every morning to overcome physical weakness.", "Partially Relevant"),
    ("অ্যাসিডিটি বা গ্যাস্ট্রিকের সমস্যা এড়াতে বেশি মসলাযুক্ত খাবার খাওয়া কমান।", "Reduce eating excessively spicy food to avoid acidity or gastric problems.", "Partially Relevant"),
    ("চোখ সুস্থ রাখতে নিয়মিত সবুজ শাকসবজি ও ছোট মাছ খাওয়া উচিত।", "One should regularly eat green leafy vegetables and small fish to keep eyes healthy.", "Partially Relevant"),
    ("দাঁত ও মাড়ি মজবুত করতে দিনে দুইবার সঠিকভাবে ব্রাশ করার অভ্যাস করুন।", "Practice brushing correctly twice a day to strengthen teeth and gums.", "Partially Relevant"),
    ("অতিরিক্ত মোবাইল ও কম্পিউটার ব্যবহারে চোখের ওপর যে চাপ পড়ে তা কমাতে বিরতি নিন।", "Take breaks to lessen the stress placed on eyes from excessive mobile and computer use.", "Partially Relevant"),
    ("হজমের জন্য খাবারের পর কিছুক্ষণ হাঁটার অভ্যাস অত্যন্ত ফলপ্রসূ।", "The habit of walking for a while after meals is very effective for digestion.", "Partially Relevant"),
    ("শরীরে পানির ঘাটতি হলে মাথাব্যথা ও দুর্বলতা দেখা দিতে পারে।", "Headache and weakness can occur if there is dehydration in the body.", "Partially Relevant"),
    ("মানসিক উৎকণ্ঠা কাটাতে নিয়মিত যোগব্যায়াম বা মেডিটেশন করার চেষ্টা করুন।", "Try practicing regular yoga or meditation to relieve mental anxiety.", "Partially Relevant"),
    ("হাড় শক্তিশালী রাখতে ক্যালসিয়াম ও ভিটামিন 'ডি' সমৃদ্ধ খাদ্য গ্রহণ করুন।", "Intake foods rich in calcium and Vitamin 'D' to keep bones strong.", "Partially Relevant"),
    ("কাজের দক্ষতা বৃদ্ধি করতে প্রতিদিন কাজের সুস্পষ্ট রুটিন তৈরি করুন।", "Create a clear daily routine of work to increase working efficiency.", "Partially Relevant"),
    ("শরীরের ক্ষতিকর বিষাক্ত পদার্থ দূর করতে প্রতিদিন প্রচুর পানি পান করুন।", "Drink plenty of water daily to flush out harmful toxic substances from the body.", "Partially Relevant"),
    ("দাঁতের ক্ষয়রোগ এড়াতে অতিরিক্ত মিষ্টি জাতীয় খাবার খাওয়া পরিহার করা উচিত।", "Eating excessive sweet foods should be avoided to prevent tooth decay.", "Partially Relevant"),
    ("কর্মক্ষেত্রে কাজের চাপ কমাতে সঠিক সময় ব্যবস্থাপনার দিকে নজর দিন।", "Pay attention to proper time management to reduce work stress in workplace.", "Partially Relevant"),
    ("শরীরে রক্তস্বল্পতা দূর করতে ডালিম , লাল শাক ও লিভার খাওয়া উপকারী।", "Eating pomegranates , red amaranth and liver is beneficial to cure anemia in the body.", "Partially Relevant"),
    ("ওজন নিয়ন্ত্রণে রাখতে প্রতিদিনের খাবারের ক্যালরি মেপে খাবার খান।", "Eat food measuring daily calories to keep weight under control.", "Partially Relevant"),
    ("হৃদরোগের ঝুঁকি কমাতে ধূমপান ও অ্যালকোহল সেবন থেকে বিরত থাকুন।", "Refrain from smoking and alcohol consumption to decrease heart disease risk.", "Partially Relevant"),
    ("শরীরের ক্লান্তি কাটাতে হালকা পুষ্টিকর খাবার ও তাজা ডাবের পানি পান করুন।", "Eat light nutritious food and drink fresh green coconut water to relieve bodily fatigue.", "Partially Relevant"),
    ("শিশুদের শারীরিক বিকাশের জন্য প্রতিদিন খোলা মাঠে খেলাধুলার ব্যবস্থা করুন।", "Arrange daily open field sports for physical development of children.", "Partially Relevant"),
    ("মন সুস্থ রাখতে নিজের ভালো লাগার বই পড়া বা গান শোনার অভ্যাস গড়ে তুলুন।", "Develop a habit of reading favorite books or listening to music to keep the mind healthy.", "Partially Relevant"),
    ("নখ পরিষ্কার রাখলে খাবারে রোগজীবাণু মিশে পেটে যাওয়ার আশঙ্কা থাকে না।", "Keeping nails clean avoids the risk of disease germs mixing with food and entering stomach.", "Partially Relevant"),
    ("শরীরে ইমিউনিটি বাড়াতে টক জাতীয় ফল যেমন কমলা ও লেবু বেশি খান।", "Eat more citrus fruits like oranges and lemons to boost body immunity.", "Partially Relevant"),
    ("একটানা বসে কাজ না করে কিছুক্ষণ পর পর উঠে দাঁড়ানো শরীর ও পিঠের জন্য ভালো।", "Standing up every once in a while instead of sitting continuously is good for body and back.", "Partially Relevant"),
    ("স্মৃতিশক্তি সতেজ রাখতে নিয়মিত নতুন দক্ষতা বা ভাষা শেখার চেষ্টা করুন।", "Try learning new skills or languages regularly to keep memory sharp.", "Partially Relevant"),
    ("ত্বকে যেকোনো ক্ষতিকর সাবান ব্যবহার থেকে দূরে থাকা শারীরিক সুরক্ষার অংশ।", "Staying away from using any harmful soap on skin is part of physical protection.", "Partially Relevant"),
    ("অ্যাজমা রোগীদের শীতকালে অতিরিক্ত ধুলাবালি থেকে বাঁচতে মাস্ক পরা দরকার।", "Asthma patients need to wear masks in winter to escape excessive dust.", "Partially Relevant"),
    ("সুস্থ থাকতে প্রতিদিন সময়মতো সকালের টিফিন ও রাতের খাবার গ্রহণ করুন।", "Eat morning breakfast and dinner on time daily to stay healthy.", "Partially Relevant"),
    ("কোষ্ঠকাঠিন্য সমস্যা কমাতে প্রতিদিনের খাবারে ইসবগুলের ভূষি যোগ করতে পারেন।", "You can add isabgol husk to daily meals to reduce constipation problems.", "Partially Relevant"),
    ("মনোযোগ বাড়াতে ও দুশ্চিন্তা কমাতে প্রতিদিন সকালে কিছুক্ষণ ব্যায়াম করুন।", "Exercise for a while every morning to boost focus and reduce worry.", "Partially Relevant"),
    ("হাঁটুর ব্যথা বা জয়েন্টের সমস্যা থাকলে চিকিৎসকের পরামর্শ অনুযায়ী শরীরচর্চা করুন।", "Do exercise as advised by a doctor if you have knee pain or joint problems.", "Partially Relevant"),
    ("ফুসফুস সতেজ রাখতে প্রতিদিন ধূলিমুক্ত পরিবেশে বুক ভরে শ্বাস নিন।", "Take deep breaths daily in a dust-free environment to keep lungs fresh.", "Partially Relevant"),
    ("শরীরের মেদ কমাতে রাতে রুটি খাওয়ার অভ্যাস বেশ কার্যকরী হতে পারে।", "Developing a habit of eating handmade flatbreads at night can be very effective to cut body fat.", "Partially Relevant"),

    # Not Relevant (32)
    ("মাথায় প্রচুর খুশকি হলে কিটোকোনাজল শ্যাম্পু সপ্তাহে দুইবার ব্যবহার করুন।", "Use ketoconazole shampoo twice a week if there is a lot of dandruff on head.", "Not Relevant"),
    ("চুল পড়া বন্ধ করতে চুলে পেঁয়াজের রস মেখে ২০ মিনিট পর ধুয়ে ফেলুন।", "Apply onion juice on hair and wash after 20 minutes to stop hair fall.", "Not Relevant"),
    ("গলা ব্যথা নিরাময়ে হালকা গরম পানিতে লবণ মিশিয়ে নিয়মিত কুলকুচা করুন।", "Gargle regularly with lukewarm salt water to relieve throat pain.", "Not Relevant"),
    ("কাশি কমাতে এক চামচ মধুর সাথে আদার রস মিশিয়ে প্রতিদিন খান।", "Eat one spoon of honey mixed with ginger juice daily to reduce cough.", "Not Relevant"),
    ("ব্রণ হলে বারবার মুখ স্পর্শ করা এবং ব্রণ খোঁটা সম্পূর্ণ বন্ধ করুন।", "Completely stop touching face repeatedly and picking acne if acne appears.", "Not Relevant"),
    ("পেক্টোরাল বুকের পেশি মজবুত করতে প্রতিদিন নিয়ম করে পুশ-আপ করুন।", "Do push-ups regularly every day to strengthen pectoral chest muscles.", "Not Relevant"),
    ("পিত্তথলিতে পাথর হলে পেটের ডান পাশে প্রচণ্ড ব্যথা ও বমি হতে পারে।", "Gallstones can cause severe right-side abdominal pain and vomiting.", "Not Relevant"),
    ("ইউরিক অ্যাসিড মাত্রাতিরিক্ত বাড়লে লাল মাংস খাওয়া সম্পূর্ণ বন্ধ রাখা দরকার।", "Eating red meat must be stopped completely if uric acid rises excessively.", "Not Relevant"),
    ("চোখে ছানি পড়লে যত দ্রুত সম্ভব বিশেষজ্ঞ ডাক্তারের চিকিৎসা নেওয়া উচিত।", "Specialist doctor treatment should be taken as quickly as possible if cataracts form in eyes.", "Not Relevant"),
    ("কানে কোনো কিছু ঢুকলে নিজে না বের করে ইএনটি ডাক্তারের সাহায্য নিন।", "Take help from an ENT doctor without removing objects yourself if something enters the ear.", "Not Relevant"),
    ("পায়ের গোড়ালি ফেটে গেলে রাতে শোবার আগে ভালোভাবে ধুয়ে ক্রিম মাখুন।", "Wash feet well and apply cream before bed if heels crack.", "Not Relevant"),
    ("নখে ছত্রাক বা ফাঙ্গাস ইনফেকশন হলে পা সবসময় শুকনো রাখা ভালো।", "It is good to keep feet dry always if there is a fungal infection in nails.", "Not Relevant"),
    ("মাইগ্রেনের তীব্র আক্রমণ হলে অন্ধকার নিস্তব্ধ ঘরে শুয়ে থাকা দরকার।", "Lying down in a dark quiet room is needed during a severe migraine attack.", "Not Relevant"),
    ("অ্যাজমা রোগীর হঠাৎ শ্বাসকষ্ট উঠলে ইমার্জেন্সি ইনহেলার প্রয়োগ করুন।", "Apply emergency inhaler if an asthma patient suffers sudden breathing difficulty.", "Not Relevant"),
    ("কাঁচা পেঁপে খেলে লিভারের স্বাস্থ্য ভালো থাকে এবং বদহজম দূর হয়।", "Eating raw papaya keeps liver health good and eliminates indigestion.", "Not Relevant"),
    ("হাইপারটেনশন এড়াতে নিয়মিত রক্তচাপ মেপে চিকিৎসকের পরামর্শ মানুন।", "Measure blood pressure regularly and follow doctor's advice to avoid hypertension.", "Not Relevant"),
    ("দাঁতের ক্ষয় রুখতে রাতে খাবার পর নিয়মিত ফ্লস ও ব্রাশ করুন।", "Floss and brush regularly after dinner to prevent tooth decay.", "Not Relevant"),
    ("পায়ের পেশিতে টান ধরলে শক্ত জায়গায় পা সোজা করে প্রসারিত করুন।", "Straighten and stretch leg on a firm surface if leg muscles cramp.", "Not Relevant"),
    ("মুখের দুর্গন্ধ দূর করতে লবঙ্গ চিবানো বা মাউথওয়াশ ব্যবহার করা যায়।", "Chewing cloves or using mouthwash can be done to eliminate bad breath.", "Not Relevant"),
    ("শরীরের কোথাও কেটে গেলে রক্ত পড়া বন্ধ করতে পরিচ্ছন্ন কাপড় দিয়ে চেপে ধরুন।", "Press with a clean cloth to stop bleeding if any part of body is cut.", "Not Relevant"),
    ("রক্তশূন্যতা দূর করতে পালং শাক ও কলিজা খাদ্য তালিকায় অন্তর্ভুক্ত করুন।", "Include spinach and liver in diet to overcome anemia.", "Not Relevant"),
    ("শিশুদের ঠান্ডা ও নিউমোনিয়ার লক্ষণ দেখা দিলে ডাক্তারের পরামর্শে ওষুধ দিন।", "Give medication on doctor's advice if cold and pneumonia symptoms appear in children.", "Not Relevant"),
    ("দাঁতের মাড়ি দিয়ে পুঁজ পড়লে তা মারাত্মক ইনফেকশনের লক্ষণ হতে পারে।", "Pus oozing from gums can be a sign of severe infection.", "Not Relevant"),
    ("কানের ভেতরের অংশ কখনো কটন বাড বা কাঠি দিয়ে চুলকানো অনুচিত।", "The inner part of ears should never be scratched with cotton buds or sticks.", "Not Relevant"),
    ("পেটের অতিরিক্ত গ্যাস কমাতে খাওয়ার পর জলদি শুয়ে পড়া থেকে বিরত থাকুন।", "Refrain from lying down immediately after meals to lessen excessive stomach gas.", "Not Relevant"),
    ("ত্বকে এলার্জির চুলকানি বাড়লে ঠান্ডা পানি বা বরফের সেক দেওয়া যায়।", "Cold water or ice compresses can be applied if skin allergy itching increases.", "Not Relevant"),
    ("কোমর ব্যথা তীব্র হলে ভারি জিনিস বহনের মতো কাজ থেকে দূরে থাকুন।", "Stay away from tasks like lifting heavy objects if back pain is severe.", "Not Relevant"),
    ("ডায়াবেটিস ধরা পড়লে প্রতিদিন চিনি ও মিষ্টি খাবার বর্জন করা জরুরি।", "Abstaining from sugar and sweet food daily is crucial if diabetes is diagnosed.", "Not Relevant"),
    ("বুকে জমে থাকা কফ নরম করতে গরম পানির বাষ্প বা স্টিম নেওয়া ভালো।", "Taking warm water vapor or steam is good to soften chest congestion.", "Not Relevant"),
    ("সানবার্ন হলে পোড়া স্থানে আলু বা শসার থকথকে পেস্ট মেখে রাখুন।", "Apply mashed potato or cucumber paste on sunburned spots if sunburn occurs.", "Not Relevant"),
    ("হাঁটুর বাত ব্যথায় সরিষার তেল ও রসুন গরম করে ম্যাসাজ করলে উপকার পাওয়া যায়।", "Relief is found by massaging warm mustard oil and garlic on knee arthritis pain.", "Not Relevant"),
    ("একজিমা রোগ হলে ক্ষারযুক্ত সাধারণ সাবান ব্যবহার পরিহার করা শ্রেয়।", "Avoiding alkaline general soap is preferable if affected by eczema disease.", "Not Relevant"),
]

print("P4 count:", len(p4_data))

# Prompt 5:
# Genre: 'রোদ জনিত সমস্যা' / 'Sun-related problems'
# Prompt: 'যখন আমি রোদে বের হই , তখন আমার মাথা ভারী হয়ে যায় এবং আমার দৃষ্টি ঝাপসা হয়ে যায় , যার ফলে কিছুক্ষণের জন্য হাঁটা কঠিন হয়ে পড়ে'
# Prompt En: 'When I go out in the sun, my head gets heavy and my vision gets blurry, making it difficult to walk for a while.'
# HR: 26, PR: 36, NR: 32

p5_genre = "রোদ জনিত সমস্যা"
p5_genre_en = "Sun-related problems"
p5_prompt = "যখন আমি রোদে বের হই , তখন আমার মাথা ভারী হয়ে যায় এবং আমার দৃষ্টি ঝাপসা হয়ে যায় , যার ফলে কিছুক্ষণের জন্য হাঁটা কঠিন হয়ে পড়ে"
p5_prompt_en = "When I go out in the sun, my head gets heavy and my vision gets blurry, making it difficult to walk for a while."

p5_data = [
    # Highly Relevant (26)
    ("রোদে বের হওয়ার আগে পর্যাপ্ত পানি বা ওরস্যালাইন পান করে শরীরকে হাইড্রেটেড রাখুন।", "Keep body hydrated by drinking sufficient water or ORS before stepping out in the sun.", "Highly Relevant"),
    ("রোদের তীব্রতা থেকে চোখ ও মাথা বাঁচাতে ভালো মানের রোদচশমা এবং চওড়া হ্যাট বা ছাতা ব্যবহার করুন।", "Use good quality sunglasses and a wide hat or umbrella to protect eyes and head from severe sun.", "Highly Relevant"),
    ("রোদে মাথা ভারী বা দৃষ্টি ঝাপসা লাগলে সাথে সাথে কোনো ছায়াযুক্ত বা ঠান্ডা স্থানে বসে বিশ্রাম নিন।", "Sit and rest in a shady or cool place immediately if head feels heavy or vision blurred in the sun.", "Highly Relevant"),
    ("সূর্যের অতিরিক্ত তাপ ও হিট স্ট্রোক এড়াতে দুপুর ১২টা থেকে বিকেল ৩টা পর্যন্ত রোদে বের হওয়া এড়িয়ে চলুন।", "Avoid going out in the sun between 12 PM and 3 PM to avoid excess sun heat and heat stroke.", "Highly Relevant"),
    ("রোদে বের হওয়ার সময় মাথায় ভেজা বা সুতির হালকা রুমাল দিয়ে ঢেকে রাখা ভালো।", "It is good to cover head with a wet or light cotton handkerchief when stepping out in the sun.", "Highly Relevant"),
    ("রোদে মাথা ঘুরলে বা ঝাপসা দেখলে মুখে ও ঘাড়ে ঠান্ডা পানির ঝাপটা দিন।", "Splash cold water on face and neck if dizzy or experiencing blurry vision in the sun.", "Highly Relevant"),
    ("শরীর থেকে অতিরিক্ত ঘাম বের হয়ে পানিশূন্যতা হলে ওরস্যালাইন বা ডাবের পানি পান করুন।", "Drink ORS or green coconut water if dehydration occurs due to excess body sweating.", "Highly Relevant"),
    ("রোদে বের হওয়ার আগে সুতির পাতলা ও হালকা রঙের ঢিলেঢালা পোশাক পরিধান করা উচিত।", "One should wear light-colored thin and loose cotton clothes before going out in the sun.", "Highly Relevant"),
    ("রোদে মাথা ভারী হওয়ার সমস্যায় গ্লুকোজের পানি পান করলে তাৎক্ষণিক শক্তি পাওয়া যায়।", "Drinking glucose water yields instant energy in the problem of head heaviness in the sun.", "Highly Relevant"),
    ("হিট একজশন বা হিট স্ট্রোকের প্রাথমিক লক্ষণ হিসেবে মাথা ভারী ও ঝাপসা দৃষ্টি হতে পারে।", "Head heaviness and blurry vision can be early signs of heat exhaustion or heat stroke.", "Highly Relevant"),
    ("রোদে বেশিক্ষণ হাঁটাহাঁটি না করে মাঝে মাঝে কোনো ছায়ায় দাঁড়িয়ে বিশ্রাম নেওয়া প্রয়োজন।", "It is necessary to take breaks standing in shade occasionally instead of walking long in the sun.", "Highly Relevant"),
    ("রোদে চোখের ক্লান্তি ও ঝাপসা ভাব কমাতে চোখে ঠান্ডা পানির সিক্ত তুলো বা কাপড়ের সেক দিন।", "Apply cold water soaked cotton or cloth compresses to eyes to reduce eye fatigue and blurriness in the sun.", "Highly Relevant"),
    ("যদি সানগ্লাস ব্যবহারের পরও চোখে ঝাপসা লাগে , তবে চশমার পাওয়ার বা চোখের ডাক্তার দেখান।", "Consult an eye doctor or check glasses power if vision stays blurry despite using sunglasses.", "Highly Relevant"),
    ("রোদে অতিরিক্ত সময় কাজ করতে হলে সাথে সবসময় পানির বোতল ও ক্যাপ সঙ্গে রাখুন।", "Always keep a water bottle and a cap with you if you have to work long hours in the sun.", "Highly Relevant"),
    ("প্রচণ্ড রোদে হাঁটাহাঁটির সময় মাথা ঝুলিয়ে না রেখে সোজা হয়ে হাঁটার চেষ্টা করুন।", "Try walking upright without drooping head when walking in intense sun.", "Highly Relevant"),
    ("রোদে রক্তচাপ হঠাৎ কমে মাথা ভারী লাগলে কিছুটা লবণ-পানির শরবত পান করুন।", "Drink some salt-water solution if blood pressure drops suddenly in the sun causing heavy head.", "Highly Relevant"),
    ("সূর্যের ক্ষতিকর অতিবেগুনি রশ্মি এড়াতে চোখে ইউভি-প্রটেক্টেড রোদচশমা ব্যবহার করা জরুরি।", "Using UV-protected sunglasses on eyes is essential to avoid harmful solar ultraviolet rays.", "Highly Relevant"),
    ("রোদে বের হওয়ার পর অতিরিক্ত মাথা ঘুরালে বা বমি ভাব হলে সাথে সাথে নিকটস্থ হাসপাতালে যান।", "Go to the nearest hospital immediately if severe dizziness or nausea occurs after sun exposure.", "Highly Relevant"),
    ("অতিরিক্ত তাপে মাথা গরম হওয়া কমাতে মাথায় ঠান্ডা পানি দিয়ে ভিজিয়ে নিতে পারেন।", "You can wet head with cold water to reduce head heating from excessive heat.", "Highly Relevant"),
    ("রোদে বাইরে যাওয়ার আধঘণ্টা আগে মুখে ও প্রকাশ্য ত্বকে সানস্ক্রিন লোশন মাখুন।", "Apply sunscreen lotion on face and exposed skin half an hour before going outside in the sun.", "Highly Relevant"),
    ("সান স্ট্রোকের হাত থেকে বাঁচতে রোদে দীর্ঘ সময় একটানা দৌড়াদৌড়ি বা পরিশ্রম পরিহার করুন।", "Avoid continuous running or heavy exertion in the sun for long durations to stay safe from sunstroke.", "Highly Relevant"),
    ("রোদে যাওয়ার সময় খালি পেটে না বের হয়ে হালকা কিছু খেয়ে পানি পান করে বের হন।", "Do not go out on an empty stomach when going into the sun ; eat something light and drink water before leaving.", "Highly Relevant"),
    ("মাইগ্রেনের রোগীদের রোদের আলোয় মাথা ভারী হতে পারে , তাই অন্ধকার বা কম আলোর ঘরে বিশ্রাম নিন।", "Migraine patients may experience heavy head in sunlight , so rest in a dark or low-light room.", "Highly Relevant"),
    ("রোদে শরীর থেকে সোডিয়াম ও পটাশিয়াম বের হয়ে গেলে স্যালাইন খাওয়া অত্যন্ত উপকারী।", "Consuming saline is extremely beneficial if sodium and potassium leave body in the sun.", "Highly Relevant"),
    ("দীর্ঘদিন রোদে বের হলেই মাথা ধরা ও ঝাপসা দেখার সমস্যা থাকলে চিকিৎসকের কাছে গিয়ে প্রেশার মাপান।", "Visit a doctor to get blood pressure checked if head heaviness and blurry vision happen every time you go out in sun for long.", "Highly Relevant"),
    ("যদি সানগ্লাস , ছাতা এবং পানি পানের পরও উপসর্গ না কমে , তবে নিউরোলজিস্টের পরামর্শ নিন।", "If symptoms do not lessen even after using sunglasses , umbrella and drinking water , consult a neurologist.", "Highly Relevant"),

    # Partially Relevant (36)
    ("সুস্থ থাকতে প্রতিদিন পর্যাপ্ত পানি ও সুষম খাবার গ্রহণ করা দরকার।", "Eating balanced food and adequate water daily is needed to stay healthy.", "Partially Relevant"),
    ("মানসিক উৎকণ্ঠা কাটাতে প্রতিদিন অন্তত ২০ মিনিট মেডিটেশন করা ভালো।", "Practicing meditation for at least 20 minutes daily is good to relieve mental anxiety.", "Partially Relevant"),
    ("শরীরের হাড় শক্ত রাখতে প্রতিদিন সকালে কিছুক্ষণ হালকা রোদে থাকা ভালো।", "Staying in mild morning sun for a while daily is good to keep body bones strong.", "Partially Relevant"),
    ("রাতে নিয়ম করে অন্তত ৭ থেকে ৮ ঘণ্টা ভালো ঘুম হলে শরীর চাঙ্গা থাকে।", "Body remains fresh if you sleep soundly for at least 7 to 8 hours regularly at night.", "Partially Relevant"),
    ("উচ্চ রক্তচাপ নিয়ন্ত্রণে রাখতে খাবারে অতিরিক্ত লবণ খাওয়া বন্ধ করা দরকার।", "Stopping extra salt intake in meals is needed to keep high blood pressure under control.", "Partially Relevant"),
    ("হজমের সমস্যা এড়াতে অতিরিক্ত তেল ও মসলাযুক্ত খাবার বর্জন করুন।", "Avoid excess oil and spicy foods to prevent digestion problems.", "Partially Relevant"),
    ("শারীরিক ক্লান্তি দূর করতে কাজের ফাঁকে সংক্ষিপ্ত বিরতি নেওয়া অত্যন্ত কার্যকর।", "Taking short breaks in between work is extremely effective to overcome physical fatigue.", "Partially Relevant"),
    ("চোখের দৃষ্টিশক্তি ভালো রাখতে প্রতিদিন ডালিম ও লাল ফলমূল খাওয়া উচিত।", "One should eat pomegranates and red fruits daily to keep eyesight good.", "Partially Relevant"),
    ("রোগ মুক্ত জীবনযাপন করতে ধুলোবালি ও ধূমপান থেকে দূরে থাকা শ্রেয়।", "Staying away from dust and smoking is preferable to live a disease-free life.", "Partially Relevant"),
    ("ওজন সমতায় রাখতে প্রতিদিন নিয়ম করে সকালে হাঁটাহাঁটি করার অভ্যাস গড়ে তুলুন।", "Develop a habit of morning walks regularly every day to maintain balanced weight.", "Partially Relevant"),
    ("শরীরে ভিটামিনের ঘাটতি হলে দ্রুত মেজাজ খিটখিটে ও শরীর দুর্বল হতে পারে।", "Irritable mood and body weakness can quickly happen if there is a vitamin deficiency in the body.", "Partially Relevant"),
    ("দাঁতের সুস্থতায় সকালে খাবারের পর এবং রাতে ঘুমানোর আগে ব্রাশ করুন।", "Brush after meals in the morning and before sleeping at night for dental health.", "Partially Relevant"),
    ("হৃদরোগ এড়াতে প্রতিদিনের খাদ্য তালিকায় তাজা শাকসবজি অন্তর্ভুক্ত করুন।", "Include fresh green vegetables in daily diet to avoid heart disease.", "Partially Relevant"),
    ("স্মৃতিশক্তি সতেজ ও প্রখর রাখতে প্রতিদিন নতুন তথ্য শেখার চেষ্টা করুন।", "Try to learn new information every day to keep memory fresh and sharp.", "Partially Relevant"),
    ("কর্মক্ষেত্রে সাফল্যের জন্য কাজের সুনির্দিষ্ট পরিকল্পনা বানিয়ে এগোতে হয়।", "One needs to proceed by making a specific work plan for success in the workplace.", "Partially Relevant"),
    ("শরীরে পানির অভাব কাটাতে তাজা ফলের রস ও শসা খাওয়া যেতে পারে।", "Fresh fruit juices and cucumbers can be consumed to overcome body water shortage.", "Partially Relevant"),
    ("মন সুস্থ রাখতে নিজের বন্ধু ও স্বজনদের সাথে চমৎকার সময় কাটান।", "Spend wonderful time with your friends and relatives to keep the mind healthy.", "Partially Relevant"),
    ("কোষ্ঠকাঠিন্য সমস্যা কমাতে আঁশযুক্ত খাবার ও প্রচুর পানি পান করা দরকার।", "Eating fiber-rich food and drinking plenty of water is needed to lessen constipation issues.", "Partially Relevant"),
    ("অতিরিক্ত চা বা কফি সেবন বুকজ্বালা ও গ্যাস্ট্রিকের কারণ হতে পারে।", "Excessive consumption of tea or coffee can cause heartburn and gastric issues.", "Partially Relevant"),
    ("নখ পরিষ্কার ও সঠিক মাপে ছোট রাখলে হাত পরিষ্কার রাখা সহজ হয়।", "Keeping nails clean and short to exact proportions makes keeping hands clean easy.", "Partially Relevant"),
    ("শারীরিক সামর্থ্য বৃদ্ধি করতে প্রোটিনজাতীয় খাবার যেমন ডিম ও মাছ খান।", "Eat protein foods like eggs and fish to increase physical stamina.", "Partially Relevant"),
    ("অতিরিক্ত মানসিক চাপের ফলে রাতে সময়মতো ঘুম না আসার সমস্যা ঘটে।", "Excessive mental pressure results in problems with not falling asleep on time at night.", "Partially Relevant"),
    ("ত্বক পরিষ্কার রাখতে নিয়মিত সাবান ও পরিষ্কার পানি দিয়ে মুখ ধুয়ে নিন।", "Wash face with clean water and regular soap to keep skin clean.", "Partially Relevant"),
    ("একটানা বেশিক্ষণ কম্পিউটারের দিকে তাকিয়ে কাজ করলে চোখ ক্লান্ত হয়ে পড়ে।", "Looking at the computer for long continuously makes eyes tired.", "Partially Relevant"),
    ("শরীরে রক্তস্বল্পতা থাকলে চিকিৎসকের পরামর্শ মেনে আয়রনযুক্ত খাবার বাড়ান।", "Increase iron-rich food intake according to a doctor's advice if you have anemia.", "Partially Relevant"),
    ("বয়স বাড়ার সাথে সাথে শরীরে ক্যালসিয়ামের চাহিদা পূরণে নজর দিন।", "Pay attention to meeting calcium demands in the body as age advances.", "Partially Relevant"),
    ("উদ্বেগ এড়াতে সামাজিক যোগাযোগ মাধ্যমে অতিরিক্ত সময় ব্যয় করা থেকে দূরে থাকুন।", "Stay away from spending excessive time on social media to avoid anxiety.", "Partially Relevant"),
    ("হাঁটুর ব্যথায় একটানা দীর্ঘক্ষণ দাঁড়িয়ে থেকে কাজ করা বন্ধ করা উচিত।", "Standing continuously for long while working should be stopped if you have knee pain.", "Partially Relevant"),
    ("শরীরের দূষিত বর্জ্য দূর করতে সাহায্য করতে কিডনি সুস্থ রাখা জরুরি।", "Keeping kidneys healthy is essential to help flush out body waste products.", "Partially Relevant"),
    ("দাঁতের মাড়ি সুস্থ রাখতে টকজাতীয় ফল নিয়মিত খাবারের তালিকায় রাখুন।", "Keep citrus fruits regularly in meal plans to keep tooth gums healthy.", "Partially Relevant"),
    ("অ্যাজমা থেকে সুরক্ষায় যেকোনো ধোঁয়া ও ধুলাবালি এড়িয়ে চলার চেষ্টা করুন।", "Try avoiding any smoke and dust for protection from asthma.", "Partially Relevant"),
    ("সুস্থ জীবনের প্রয়োজনে রাত জেগে কাজ করার অভ্যাস বর্জন করা দরকার।", "Abstaining from late-night work habits is necessary for a healthy life.", "Partially Relevant"),
    ("কাজের দক্ষতা বৃদ্ধি করতে সময় অনুযায়ী অগ্রাধিকার নির্ধারণ করুন।", "Set priorities according to time to increase work efficiency.", "Partially Relevant"),
    ("পেশির টান দূর করতে হালকা গরম পানির সেক ব্যবহার করতে পারেন।", "You can use warm water compresses to relieve muscle cramps.", "Partially Relevant"),
    ("রোগ প্রতিরোধ করতে খাবারে ভেজাল ও রাসায়নিক এড়িয়ে ভালো পুষ্টিকর খাদ্য বেছে নিন।", "Choose good nutritious food avoiding food adulteration and chemicals to prevent disease.", "Partially Relevant"),
    ("শরীরের ক্লান্তি কাটাতে প্রতিদিন হালকা ব্যায়াম করা অত্যন্ত উপকারী।", "Doing light exercise daily is extremely beneficial to relieve bodily fatigue.", "Partially Relevant"),

    # Not Relevant (32)
    ("মাথায় প্রচুর খুশকি হলে কিটোকোনাজল শ্যাম্পু সপ্তাহে দুইবার ব্যবহার করুন।", "Use ketoconazole shampoo twice a week if there is a lot of dandruff on head.", "Not Relevant"),
    ("চুল পড়া বন্ধ করতে চুলে পেঁয়াজের রস মেখে ২০ মিনিট পর ধুয়ে ফেলুন।", "Apply onion juice on hair and wash after 20 minutes to stop hair fall.", "Not Relevant"),
    ("গলা ব্যথা নিরাময়ে হালকা গরম পানিতে লবণ মিশিয়ে নিয়মিত কুলকুচা করুন।", "Gargle regularly with lukewarm salt water to relieve throat pain.", "Not Relevant"),
    ("কাশি কমাতে এক চামচ মধুর সাথে আদার রস মিশিয়ে প্রতিদিন খান।", "Eat one spoon of honey mixed with ginger juice daily to reduce cough.", "Not Relevant"),
    ("ব্রণ হলে বারবার মুখ স্পর্শ করা এবং ব্রণ খোঁটা সম্পূর্ণ বন্ধ করুন।", "Completely stop touching face repeatedly and picking acne if acne appears.", "Not Relevant"),
    ("পেক্টোরাল বুকের পেশি মজবুত করতে প্রতিদিন নিয়ম করে পুশ-আপ করুন।", "Do push-ups regularly every day to strengthen pectoral chest muscles.", "Not Relevant"),
    ("পিত্তথলিতে পাথর হলে পেটের ডান পাশে প্রচণ্ড ব্যথা ও বমি হতে পারে।", "Gallstones can cause severe right-side abdominal pain and vomiting.", "Not Relevant"),
    ("ইউরিক অ্যাসিড মাত্রাতিরিক্ত বাড়লে লাল মাংস খাওয়া সম্পূর্ণ বন্ধ রাখা দরকার।", "Eating red meat must be stopped completely if uric acid rises excessively.", "Not Relevant"),
    ("চোখে ছানি পড়লে যত দ্রুত সম্ভব বিশেষজ্ঞ ডাক্তারের চিকিৎসা নেওয়া উচিত।", "Specialist doctor treatment should be taken as quickly as possible if cataracts form in eyes.", "Not Relevant"),
    ("কানে কোনো কিছু ঢুকলে নিজে না বের করে ইএনটি ডাক্তারের সাহায্য নিন।", "Take help from an ENT doctor without removing objects yourself if something enters the ear.", "Not Relevant"),
    ("পায়ের গোড়ালি ফেটে গেলে রাতে শোবার আগে ভালোভাবে ধুয়ে ক্রিম মাখুন।", "Wash feet well and apply cream before bed if heels crack.", "Not Relevant"),
    ("নখে ছত্রাক বা ফাঙ্গাস ইনফেকশন হলে পা সবসময় শুকনো রাখা ভালো।", "It is good to keep feet dry always if there is a fungal infection in nails.", "Not Relevant"),
    ("মাইগ্রেনের তীব্র আক্রমণ হলে অন্ধকার নিস্তব্ধ ঘরে শুয়ে থাকা দরকার।", "Lying down in a dark quiet room is needed during a severe migraine attack.", "Not Relevant"),
    ("অ্যাজমা রোগীর হঠাৎ শ্বাসকষ্ট উঠলে ইমার্জেন্সি ইনহেলার প্রয়োগ করুন।", "Apply emergency inhaler if an asthma patient suffers sudden breathing difficulty.", "Not Relevant"),
    ("কাঁচা পেঁপে খেলে লিভারের স্বাস্থ্য ভালো থাকে এবং বদহজম দূর হয়।", "Eating raw papaya keeps liver health good and eliminates indigestion.", "Not Relevant"),
    ("হাইপারটেনশন এড়াতে নিয়মিত রক্তচাপ মেপে চিকিৎসকের পরামর্শ মানুন।", "Measure blood pressure regularly and follow doctor's advice to avoid hypertension.", "Not Relevant"),
    ("দাঁতের ক্ষয় রুখতে রাতে খাবার পর নিয়মিত ফ্লস ও ব্রাশ করুন।", "Floss and brush regularly after dinner to prevent tooth decay.", "Not Relevant"),
    ("পায়ের পেশিতে টান ধরলে শক্ত জায়গায় পা সোজা করে প্রসারিত করুন।", "Straighten and stretch leg on a firm surface if leg muscles cramp.", "Not Relevant"),
    ("মুখের দুর্গন্ধ দূর করতে লবঙ্গ চিবানো বা মাউথওয়াশ ব্যবহার করা যায়।", "Chewing cloves or using mouthwash can be done to eliminate bad breath.", "Not Relevant"),
    ("শরীরের কোথাও কেটে গেলে রক্ত পড়া বন্ধ করতে পরিচ্ছন্ন কাপড় দিয়ে চেপে ধরুন।", "Press with a clean cloth to stop bleeding if any part of body is cut.", "Not Relevant"),
    ("রক্তশূন্যতা দূর করতে পালং শাক ও কলিজা খাদ্য তালিকায় অন্তর্ভুক্ত করুন।", "Include spinach and liver in diet to overcome anemia.", "Not Relevant"),
    ("শিশুদের ঠান্ডা ও নিউমোনিয়ার লক্ষণ দেখা দিলে ডাক্তারের পরামর্শে ওষুধ দিন।", "Give medication on doctor's advice if cold and pneumonia symptoms appear in children.", "Not Relevant"),
    ("দাঁতের মাড়ি দিয়ে পুঁজ পড়লে তা মারাত্মক ইনফেকশনের লক্ষণ হতে পারে।", "Pus oozing from gums can be a sign of severe infection.", "Not Relevant"),
    ("কানের ভেতরের অংশ কখনো কটন বাড বা কাঠি দিয়ে চুলকানো অনুচিত।", "The inner part of ears should never be scratched with cotton buds or sticks.", "Not Relevant"),
    ("পেটের অতিরিক্ত গ্যাস কমাতে খাওয়ার পর জলদি শুয়ে পড়া থেকে বিরত থাকুন।", "Refrain from lying down immediately after meals to lessen excessive stomach gas.", "Not Relevant"),
    ("ত্বকে এলার্জির চুলকানি বাড়লে ঠান্ডা পানি বা বরফের সেক দেওয়া যায়।", "Cold water or ice compresses can be applied if skin allergy itching increases.", "Not Relevant"),
    ("কোমর ব্যথা তীব্র হলে ভারি জিনিস বহনের মতো কাজ থেকে দূরে থাকুন।", "Stay away from tasks like lifting heavy objects if back pain is severe.", "Not Relevant"),
    ("ডায়াবেটিস ধরা পড়লে প্রতিদিন চিনি ও মিষ্টি খাবার বর্জন করা জরুরি।", "Abstaining from sugar and sweet food daily is crucial if diabetes is diagnosed.", "Not Relevant"),
    ("বুকে জমে থাকা কফ নরম করতে গরম পানির বাষ্প বা স্টিম নেওয়া ভালো।", "Taking warm water vapor or steam is good to soften chest congestion.", "Not Relevant"),
    ("সানবার্ন হলে পোড়া স্থানে আলু বা শসার থকথকে পেস্ট মেখে রাখুন।", "Apply mashed potato or cucumber paste on sunburned spots if sunburn occurs.", "Not Relevant"),
    ("হাঁটুর বাত ব্যথায় সরিষার তেল ও রসুন গরম করে ম্যাসাজ করলে উপকার পাওয়া যায়।", "Relief is found by massaging warm mustard oil and garlic on knee arthritis pain.", "Not Relevant"),
    ("একজিমা রোগ হলে ক্ষারযুক্ত সাধারণ সাবান ব্যবহার পরিহার করা শ্রেয়।", "Avoiding alkaline general soap is preferable if affected by eczema disease.", "Not Relevant"),
]

print("P5 count:", len(p5_data))

# Assembly
all_rows = []

def add_prompt_data(genre, genre_en, prompt, prompt_en, data_list):
    for resp, resp_en, label in data_list:
        all_rows.append({
            'Symptoms Genres': genre,
            'Symptoms Genres (Translated to English)': genre_en,
            'Used Prompts': prompt,
            'Used Prompts (Translated to English)': prompt_en,
            'Response': resp,
            'Response (Translated to English)': resp_en,
            'Lable': label
        })

add_prompt_data(p1_genre, p1_genre_en, p1_prompt, p1_prompt_en, p1_data)
add_prompt_data(p2_genre, p2_genre_en, p2_prompt, p2_prompt_en, p2_data)
add_prompt_data(p3_genre, p3_genre_en, p3_prompt, p3_prompt_en, p3_data)
add_prompt_data(p4_genre, p4_genre_en, p4_prompt, p4_prompt_en, p4_data)
add_prompt_data(p5_genre, p5_genre_en, p5_prompt, p5_prompt_en, p5_data)

df = pd.DataFrame(all_rows)
output_filename = "Batch_03_Gemini.xlsx"
df.to_excel(output_filename, index=False)
print(f"Saved {len(df)} rows to {output_filename}")
