import pandas as pd
from batch28_p1 import p1_hr, p1_pr, p1_nr
from batch28_p2 import p2_hr, p2_pr, p2_nr
from batch28_p3 import p3_hr, p3_pr, p3_nr
from batch28_p4 import p4_hr, p4_pr, p4_nr
from batch28_p5 import p4_hr_5 as p5_hr, p4_pr_5 as p5_pr, p4_nr_5 as p5_nr
from batch28_p6 import p6_hr, p6_pr, p6_nr
from batch28_p7 import p7_hr, p7_pr, p7_nr
from batch28_p8 import p8_hr, p8_pr, p8_nr
from batch28_p9 import p9_hr, p9_pr, p9_nr

# Load plan metadata
plan_df = pd.read_excel('Generation_Plan.xlsx', sheet_name='Prompts per Batch')
b28_plan = plan_df[plan_df['Batch'] == 28].reset_index(drop=True)

prompts_data = [
    (b28_plan.iloc[0], p1_hr + p1_pr + p1_nr),
    (b28_plan.iloc[1], p2_hr + p2_pr + p2_nr),
    (b28_plan.iloc[2], p3_hr + p3_pr + p3_nr),
    (b28_plan.iloc[3], p4_hr + p4_pr + p4_nr),
    (b28_plan.iloc[4], p5_hr + p5_pr + p5_nr),
    (b28_plan.iloc[5], p6_hr + p6_pr + p6_nr),
    (b28_plan.iloc[6], p7_hr + p7_pr + p7_nr),
    (b28_plan.iloc[7], p8_hr + p8_pr + p8_nr),
    (b28_plan.iloc[8], p9_hr + p9_pr + p9_nr),
]

rows = []
for plan_row, resp_list in prompts_data:
    genre_bn = plan_row['Symptoms Genres']
    genre_en = plan_row['Symptoms Genres (Translated to English)']
    prompt_bn = plan_row['Used Prompts']
    prompt_en = plan_row['Used Prompts (Translated to English)']

    for resp_bn, resp_en, lable in resp_list:
        rows.append({
            'Symptoms Genres': genre_bn,
            'Symptoms Genres (Translated to English)': genre_en,
            'Used Prompts': prompt_bn,
            'Used Prompts (Translated to English)': prompt_en,
            'Response': resp_bn,
            'Response (Translated to English)': resp_en,
            'Lable': lable
        })

df_out = pd.DataFrame(rows)

columns_order = [
    'Symptoms Genres',
    'Symptoms Genres (Translated to English)',
    'Used Prompts',
    'Used Prompts (Translated to English)',
    'Response',
    'Response (Translated to English)',
    'Lable'
]

df_out = df_out[columns_order]
df_out.to_excel('Batch_28_Gemini.xlsx', index=False)
print("Successfully generated Batch_28_Gemini.xlsx with", len(df_out), "rows.")
