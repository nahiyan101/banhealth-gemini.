import pandas as pd
import re
import prompt1, prompt2, prompt3, prompt4, prompt5, prompt6, prompt7, prompt8, prompt9, prompt10, prompt11

prompts_modules = [
    prompt1, prompt2, prompt3, prompt4, prompt5, prompt6, prompt7, prompt8, prompt9, prompt10, prompt11
]

rows = []

def format_commas(text):
    # Ensure proper " , " formatting
    text = re.sub(r'\s*,\s*', ' , ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

for mod in prompts_modules:
    g_bn = mod.g_bn
    g_en = mod.g_en
    p_bn = mod.p_bn
    p_en = mod.p_en

    # Highly Relevant
    for r_bn, r_en in mod.hr:
        rows.append({
            'Symptoms Genres': g_bn,
            'Symptoms Genres (Translated to English)': g_en,
            'Used Prompts': p_bn,
            'Used Prompts (Translated to English)': p_en,
            'Response': format_commas(r_bn),
            'Response (Translated to English)': format_commas(r_en),
            'Lable': 'Highly Relevant'
        })

    # Partially Relevant
    for r_bn, r_en in mod.pr:
        rows.append({
            'Symptoms Genres': g_bn,
            'Symptoms Genres (Translated to English)': g_en,
            'Used Prompts': p_bn,
            'Used Prompts (Translated to English)': p_en,
            'Response': format_commas(r_bn),
            'Response (Translated to English)': format_commas(r_en),
            'Lable': 'Partially Relevant'
        })

    # Not Relevant
    for r_bn, r_en in mod.nr:
        rows.append({
            'Symptoms Genres': g_bn,
            'Symptoms Genres (Translated to English)': g_en,
            'Used Prompts': p_bn,
            'Used Prompts (Translated to English)': p_en,
            'Response': format_commas(r_bn),
            'Response (Translated to English)': format_commas(r_en),
            'Lable': 'Not Relevant'
        })

df = pd.DataFrame(rows)

columns = [
    'Symptoms Genres',
    'Symptoms Genres (Translated to English)',
    'Used Prompts',
    'Used Prompts (Translated to English)',
    'Response',
    'Response (Translated to English)',
    'Lable'
]

df = df[columns]
df.to_excel('Batch_27_Gemini.xlsx', index=False)
print("Successfully generated Batch_27_Gemini.xlsx with", len(df), "rows.")
