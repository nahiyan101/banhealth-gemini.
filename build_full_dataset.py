import pandas as pd
from create_data_p1 import p1_hr, p1_pr, p1_nr
from create_data_p2 import p2_hr, p2_pr, p2_nr
from create_data_p3 import p3_hr, p3_pr, p3_nr
from create_data_p4 import p4_hr, p4_pr, p4_nr
from create_data_p5 import p5_hr, p5_pr, p5_nr

prompts_info = [
    {
        "genre_bn": "ঠান্ডা জনিত",
        "genre_en": "Cold-related",
        "prompt_bn": "পায়ের আঙুল ঠান্ডা হলেও রক্ত চলাচল স্বাভাবিক মনে হয় না , সমাধান কি",
        "prompt_en": "Even though my toes are cold, blood circulation does not seem normal, what is the solution?",
        "hr": p1_hr, "pr": p1_pr, "nr": p1_nr
    },
    {
        "genre_bn": "ঘুম জনিত সমস্যা",
        "genre_en": "Sleep problems",
        "prompt_bn": "রাতে বারবার প্রস্রাবের বেগ আসে , ঘুম নষ্ট হয়ে যায় , সমাধান কি",
        "prompt_en": "Frequent urge to urinate at night, sleep is disturbed, what is the solution?",
        "hr": p2_hr, "pr": p2_pr, "nr": p2_nr
    },
    {
        "genre_bn": "অম্লতা জনিত",
        "genre_en": "Acidic",
        "prompt_bn": "খাবারের পর মুখে জ্বালা শুরু হয় , বিশেষ করে খিচুড়ি বা ভাত খেলে , সমাধান কি",
        "prompt_en": "My mouth starts burning after eating, especially after eating khichdi or rice, what is the solution?",
        "hr": p3_hr, "pr": p3_pr, "nr": p3_nr
    },
    {
        "genre_bn": "গলা জনিত",
        "genre_en": "Throat-related",
        "prompt_bn": "গলায় কাঁটার মতো কিছু আটকে আছে মনে হয় , সমাধান কি",
        "prompt_en": "I feel like I have a thorn in my throat, what is the solution?",
        "hr": p4_hr, "pr": p4_pr, "nr": p4_nr
    },
    {
        "genre_bn": "মাথা ব্যথা",
        "genre_en": "Headache",
        "prompt_bn": "সকালে ঘুম থেকে উঠেই মাথা ব্যাথা শুরু হয়ে গেছে , এখন কি করা উচিত আমার ?",
        "prompt_en": "I woke up this morning with a headache, what should I do now?",
        "hr": p5_hr, "pr": p5_pr, "nr": p5_nr
    }
]

rows = []
for p in prompts_info:
    for resp_bn, resp_en in p["hr"]:
        rows.append({
            "Symptoms Genres": p["genre_bn"],
            "Symptoms Genres (Translated to English)": p["genre_en"],
            "Used Prompts": p["prompt_bn"],
            "Used Prompts (Translated to English)": p["prompt_en"],
            "Response": resp_bn,
            "Response (Translated to English)": resp_en,
            "Lable": "Highly Relevant"
        })
    for resp_bn, resp_en in p["pr"]:
        rows.append({
            "Symptoms Genres": p["genre_bn"],
            "Symptoms Genres (Translated to English)": p["genre_en"],
            "Used Prompts": p["prompt_bn"],
            "Used Prompts (Translated to English)": p["prompt_en"],
            "Response": resp_bn,
            "Response (Translated to English)": resp_en,
            "Lable": "Partially Relevant"
        })
    for resp_bn, resp_en in p["nr"]:
        rows.append({
            "Symptoms Genres": p["genre_bn"],
            "Symptoms Genres (Translated to English)": p["genre_en"],
            "Used Prompts": p["prompt_bn"],
            "Used Prompts (Translated to English)": p["prompt_en"],
            "Response": resp_bn,
            "Response (Translated to English)": resp_en,
            "Lable": "Not Relevant"
        })

df_output = pd.DataFrame(rows)
print("Total rows generated:", len(df_output))
print(df_output.head(2))
