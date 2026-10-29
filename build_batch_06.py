import pandas as pd
from gen_b6 import b6_p1_genre_bn, b6_p1_genre_en, b6_p1_prompt_bn, b6_p1_prompt_en, p1_hr, p1_pr, p1_nr
from gen_b6 import b6_p2_genre_bn, b6_p2_genre_en, b6_p2_prompt_bn, b6_p2_prompt_en, p2_hr, p2_pr, p2_nr
from gen_p3 import b6_p3_genre_bn, b6_p3_genre_en, b6_p3_prompt_bn, b6_p3_prompt_en, p3_hr, p3_pr, p3_nr
from gen_p4 import b6_p4_genre_bn, b6_p4_genre_en, b6_p4_prompt_bn, b6_p4_prompt_en, p4_hr, p4_pr, p4_nr
from gen_p5 import b6_p5_genre_bn, b6_p5_genre_en, b6_p5_prompt_bn, b6_p5_prompt_en, p5_hr, p5_pr, p5_nr

rows = []

def add_prompt_data(genre_bn, genre_en, prompt_bn, prompt_en, hr_list, pr_list, nr_list):
    # HR
    for bn, en in hr_list:
        rows.append({
            'Symptoms Genres': genre_bn,
            'Symptoms Genres (Translated to English)': genre_en,
            'Used Prompts': prompt_bn,
            'Used Prompts (Translated to English)': prompt_en,
            'Response': bn,
            'Response (Translated to English)': en,
            'Lable': 'Highly Relevant'
        })
    # PR
    for bn, en in pr_list:
        rows.append({
            'Symptoms Genres': genre_bn,
            'Symptoms Genres (Translated to English)': genre_en,
            'Used Prompts': prompt_bn,
            'Used Prompts (Translated to English)': prompt_en,
            'Response': bn,
            'Response (Translated to English)': en,
            'Lable': 'Partially Relevant'
        })
    # NR
    for bn, en in nr_list:
        rows.append({
            'Symptoms Genres': genre_bn,
            'Symptoms Genres (Translated to English)': genre_en,
            'Used Prompts': prompt_bn,
            'Used Prompts (Translated to English)': prompt_en,
            'Response': bn,
            'Response (Translated to English)': en,
            'Lable': 'Not Relevant'
        })

add_prompt_data(b6_p1_genre_bn, b6_p1_genre_en, b6_p1_prompt_bn, b6_p1_prompt_en, p1_hr, p1_pr, p1_nr)
add_prompt_data(b6_p2_genre_bn, b6_p2_genre_en, b6_p2_prompt_bn, b6_p2_prompt_en, p2_hr, p2_pr, p2_nr)
add_prompt_data(b6_p3_genre_bn, b6_p3_genre_en, b6_p3_prompt_bn, b6_p3_prompt_en, p3_hr, p3_pr, p3_nr)
add_prompt_data(b6_p4_genre_bn, b6_p4_genre_en, b6_p4_prompt_bn, b6_p4_prompt_en, p4_hr, p4_pr, p4_nr)
add_prompt_data(b6_p5_genre_bn, b6_p5_genre_en, b6_p5_prompt_bn, b6_p5_prompt_en, p5_hr, p5_pr, p5_nr)

df_out = pd.DataFrame(rows)
df_out.to_excel('Batch_06_Gemini.xlsx', index=False)
print("Successfully generated Batch_06_Gemini.xlsx with shape:", df_out.shape)
