import pandas as pd

batch_file = 'Batch_09_Gemini.xlsx'
plan_file = 'Generation_Plan.xlsx'
orig_file = 'BanHealthAIRespRelv3(All-Processed).xlsx'

df_batch = pd.read_excel(batch_file)
df_plan = pd.read_excel(plan_file, sheet_name='Prompts per Batch')
df_orig = pd.read_excel(orig_file)

b9_plan = df_plan[df_plan['Batch'] == 9]

print("=== 1. CHECK COLUMN NAMES AND ORDER ===")
expected_cols = [
    'Symptoms Genres',
    'Symptoms Genres (Translated to English)',
    'Used Prompts',
    'Used Prompts (Translated to English)',
    'Response',
    'Response (Translated to English)',
    'Lable'
]
assert list(df_batch.columns) == expected_cols, f"Columns mismatch: {df_batch.columns.tolist()}"
print("Columns match exactly!")

print("\n=== 2. CHECK EMPTY/NULL VALUES ===")
null_counts = df_batch.isnull().sum().sum()
assert null_counts == 0, f"Found {null_counts} null values!"
print("No null or empty values found!")

print("\n=== 3. CHECK ROW COUNTS PER PROMPT AND PER LABEL ===")
grouped = df_batch.groupby(['Used Prompts', 'Lable']).size().unstack(fill_value=0)
print("Grouped counts by Prompt and Label in Batch:")
print(grouped)

for _, row in b9_plan.iterrows():
    p_bn = row['Used Prompts']
    exp_hr = row['Highly Relevant']
    exp_pr = row['Partially Relevant']
    exp_nr = row['Not Relevant']
    exp_total = row['Total']

    act_hr = grouped.loc[p_bn, 'Highly Relevant'] if p_bn in grouped.index and 'Highly Relevant' in grouped.columns else 0
    act_pr = grouped.loc[p_bn, 'Partially Relevant'] if p_bn in grouped.index and 'Partially Relevant' in grouped.columns else 0
    act_nr = grouped.loc[p_bn, 'Not Relevant'] if p_bn in grouped.index and 'Not Relevant' in grouped.columns else 0
    act_total = act_hr + act_pr + act_nr

    assert act_hr == exp_hr, f"HR mismatch for prompt '{p_bn}': expected {exp_hr}, got {act_hr}"
    assert act_pr == exp_pr, f"PR mismatch for prompt '{p_bn}': expected {exp_pr}, got {act_pr}"
    assert act_nr == exp_nr, f"NR mismatch for prompt '{p_bn}': expected {exp_nr}, got {act_nr}"
    assert act_total == exp_total, f"Total mismatch for prompt '{p_bn}': expected {exp_total}, got {act_total}"

assert len(df_batch) == b9_plan['Total'].sum(), f"Total batch count mismatch: expected {b9_plan['Total'].sum()}, got {len(df_batch)}"
print(f"Total row count ({len(df_batch)}) and per-prompt class counts match plan perfectly!")

print("\n=== 4. CHECK DUPLICATES ===")
# Intra-batch duplicates in Bengali response
dup_batch_bn = df_batch['Response'].duplicated().sum()
assert dup_batch_bn == 0, f"Found {dup_batch_bn} duplicate Bengali responses in Batch!"

# Intra-batch duplicates in English response
dup_batch_en = df_batch['Response (Translated to English)'].duplicated().sum()
assert dup_batch_en == 0, f"Found {dup_batch_en} duplicate English responses in Batch!"

# Check duplicates against original dataset
orig_bn_set = set(df_orig['Response'].dropna())
batch_bn_set = set(df_batch['Response'])
overlap_bn = batch_bn_set.intersection(orig_bn_set)
assert len(overlap_bn) == 0, f"Found {len(overlap_bn)} responses overlapping with original dataset!"

print("No duplicate responses within Batch 09 and no overlap with original dataset!")

print("\n=== 5. CHECK FORMATTING (Space before comma ' , ') ===")
# Check for commas without space before them in Bengali responses
commas_without_space = df_batch[df_batch['Response'].str.contains(r'\S,')]
if len(commas_without_space) > 0:
    print(f"WARNING: Found {len(commas_without_space)} rows with commas without preceding space:")
    print(commas_without_space[['Response']])
else:
    print("All Bengali commas follow ' , ' rule!")

print("\n=== ALL VERIFICATIONS PASSED SUCCESSFULLY! ===")
