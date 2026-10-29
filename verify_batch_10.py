import pandas as pd
import os

filename = "Batch_10_Gemini.xlsx"
plan_filename = "Generation_Plan.xlsx"

# 1. Check file existence
if not os.path.exists(filename):
    raise FileNotFoundError(f"{filename} does not exist!")

df_batch = pd.read_excel(filename)
df_plan = pd.read_excel(plan_filename, sheet_name="Prompts per Batch")
batch_10_plan = df_plan[df_plan["Batch"] == 10]

# 2. Check column names and order
expected_columns = [
    'Symptoms Genres',
    'Symptoms Genres (Translated to English)',
    'Used Prompts',
    'Used Prompts (Translated to English)',
    'Response',
    'Response (Translated to English)',
    'Lable'
]

print("Checking columns...")
assert list(df_batch.columns) == expected_columns, f"Columns mismatch! Got {list(df_batch.columns)}"

# 3. Check for empty cells
print("Checking for null/empty cells...")
null_counts = df_batch.isnull().sum().sum()
assert null_counts == 0, f"Found {null_counts} null values!"

# 4. Check for duplicates in Responses
print("Checking for duplicate responses...")
bn_dups = df_batch['Response'].duplicated().sum()
en_dups = df_batch['Response (Translated to English)'].duplicated().sum()
assert bn_dups == 0, f"Found {bn_dups} duplicate Bengali responses!"
assert en_dups == 0, f"Found {en_dups} duplicate English responses!"

# 5. Check labels spelling
expected_labels = {'Highly Relevant', 'Partially Relevant', 'Not Relevant'}
actual_labels = set(df_batch['Lable'].unique())
assert actual_labels.issubset(expected_labels), f"Unexpected labels found: {actual_labels - expected_labels}"

# 6. Check counts per prompt and class against Generation_Plan.xlsx
print("Checking counts against plan...")
total_plan_rows = batch_10_plan['Total'].sum()
assert len(df_batch) == total_plan_rows, f"Total rows mismatch! Expected {total_plan_rows}, got {len(df_batch)}"

for idx, plan_row in batch_10_plan.iterrows():
    prompt_bn = plan_row['Used Prompts']
    prompt_df = df_batch[df_batch['Used Prompts'] == prompt_bn]

    expected_hr = plan_row['Highly Relevant']
    expected_pr = plan_row['Partially Relevant']
    expected_nr = plan_row['Not Relevant']
    expected_tot = plan_row['Total']

    actual_hr = len(prompt_df[prompt_df['Lable'] == 'Highly Relevant'])
    actual_pr = len(prompt_df[prompt_df['Lable'] == 'Partially Relevant'])
    actual_nr = len(prompt_df[prompt_df['Lable'] == 'Not Relevant'])
    actual_tot = len(prompt_df)

    assert actual_tot == expected_tot, f"Prompt '{prompt_bn[:20]}...' total mismatch: expected {expected_tot}, got {actual_tot}"
    assert actual_hr == expected_hr, f"Prompt '{prompt_bn[:20]}...' HR mismatch: expected {expected_hr}, got {actual_hr}"
    assert actual_pr == expected_pr, f"Prompt '{prompt_bn[:20]}...' PR mismatch: expected {expected_pr}, got {actual_pr}"
    assert actual_nr == expected_nr, f"Prompt '{prompt_bn[:20]}...' NR mismatch: expected {expected_nr}, got {actual_nr}"

# 7. Check formatting rules (single sentence, space before comma if comma exists)
print("Checking sentence and punctuation formatting...")
for idx, row in df_batch.iterrows():
    bn_resp = str(row['Response'])
    en_resp = str(row['Response (Translated to English)'])

    # Check space before comma in BN if comma is present
    if ',' in bn_resp:
        # check that every comma is preceded by space
        parts = bn_resp.split(',')
        for p in parts[:-1]:
            assert p.endswith(' '), f"Row {idx} Bengali response comma missing space before it: '{bn_resp}'"

    if ',' in en_resp:
        parts = en_resp.split(',')
        for p in parts[:-1]:
            assert p.endswith(' '), f"Row {idx} English response comma missing space before it: '{en_resp}'"

print("ALL INTEGRITY CHECKS PASSED SUCCESSFULLY!")
print(f"Total verified rows: {len(df_batch)}")
