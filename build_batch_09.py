import pandas as pd
import p1_data
import p2_data
import p3_data
import p4_data
import p5_data

prompts = [
    (p1_data.p1_genre_bn, p1_data.p1_genre_en, p1_data.p1_prompt_bn, p1_data.p1_prompt_en,
     p1_data.p1_highly_relevant, p1_data.p1_partially_relevant, p1_data.p1_not_relevant),
    (p2_data.p2_genre_bn, p2_data.p2_genre_en, p2_data.p2_prompt_bn, p2_data.p2_prompt_en,
     p2_data.p2_highly_relevant, p2_data.p2_partially_relevant, p2_data.p2_not_relevant),
    (p3_data.p3_genre_bn, p3_data.p3_genre_en, p3_data.p3_prompt_bn, p3_data.p3_prompt_en,
     p3_data.p3_highly_relevant, p3_data.p3_partially_relevant, p3_data.p3_not_relevant),
    (p4_data.p4_genre_bn, p4_data.p4_genre_en, p4_data.p4_prompt_bn, p4_data.p4_prompt_en,
     p4_data.p4_highly_relevant, p4_data.p4_partially_relevant, p4_data.p4_not_relevant),
    (p5_data.p5_genre_bn, p5_data.p5_genre_en, p5_data.p5_prompt_bn, p5_data.p5_prompt_en,
     p5_data.p5_highly_relevant, p5_data.p5_partially_relevant, p5_data.p5_not_relevant),
]

rows = []

for g_bn, g_en, p_bn, p_en, hr_list, pr_list, nr_list in prompts:
    # Highly Relevant
    for resp_bn, resp_en in hr_list:
        rows.append({
            'Symptoms Genres': g_bn,
            'Symptoms Genres (Translated to English)': g_en,
            'Used Prompts': p_bn,
            'Used Prompts (Translated to English)': p_en,
            'Response': resp_bn,
            'Response (Translated to English)': resp_en,
            'Lable': 'Highly Relevant'
        })
    # Partially Relevant
    for resp_bn, resp_en in pr_list:
        rows.append({
            'Symptoms Genres': g_bn,
            'Symptoms Genres (Translated to English)': g_en,
            'Used Prompts': p_bn,
            'Used Prompts (Translated to English)': p_en,
            'Response': resp_bn,
            'Response (Translated to English)': resp_en,
            'Lable': 'Partially Relevant'
        })
    # Not Relevant
    for resp_bn, resp_en in nr_list:
        rows.append({
            'Symptoms Genres': g_bn,
            'Symptoms Genres (Translated to English)': g_en,
            'Used Prompts': p_bn,
            'Used Prompts (Translated to English)': p_en,
            'Response': resp_bn,
            'Response (Translated to English)': resp_en,
            'Lable': 'Not Relevant'
        })

df = pd.DataFrame(rows)

expected_cols = [
    'Symptoms Genres',
    'Symptoms Genres (Translated to English)',
    'Used Prompts',
    'Used Prompts (Translated to English)',
    'Response',
    'Response (Translated to English)',
    'Lable'
]

df = df[expected_cols]

output_filename = 'Batch_09_Gemini.xlsx'
df.to_excel(output_filename, index=False)
print(f"Successfully generated {output_filename} with shape {df.shape}")
