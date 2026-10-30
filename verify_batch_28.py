import pandas as pd
import re

print("=== Starting Verification for Batch 28 ===")

# 1. Load files
batch_df = pd.read_excel('Batch_28_Gemini.xlsx')
plan_df = pd.read_excel('Generation_Plan.xlsx', sheet_name='Prompts per Batch')
orig_df = pd.read_excel('BanHealthAIRespRelv3(All-Processed).xlsx')

# 2. Columns check
expected_cols = [
    'Symptoms Genres',
    'Symptoms Genres (Translated to English)',
    'Used Prompts',
    'Used Prompts (Translated to English)',
    'Response',
    'Response (Translated to English)',
    'Lable'
]
assert list(batch_df.columns) == expected_cols, f"Columns mismatch: {batch_df.columns.tolist()}"
print("✓ Columns and column order match required schema.")

# 3. Check empty cells
assert batch_df.isnull().sum().sum() == 0, "Found null/empty values!"
print("✓ No empty cells found.")

# 4. Total count check
b28_plan = plan_df[plan_df['Batch'] == 28].reset_index(drop=True)
expected_total = b28_plan['Total'].sum()
assert len(batch_df) == expected_total, f"Expected total {expected_total}, got {len(batch_df)}"
print(f"✓ Total row count matches plan: {len(batch_df)}")

# 5. Check per-prompt per-label counts
for idx, p_row in b28_plan.iterrows():
    p_bn = p_row['Used Prompts']
    sub = batch_df[batch_df['Used Prompts'] == p_bn]

    hr_count = len(sub[sub['Lable'] == 'Highly Relevant'])
    pr_count = len(sub[sub['Lable'] == 'Partially Relevant'])
    nr_count = len(sub[sub['Lable'] == 'Not Relevant'])

    assert hr_count == p_row['Highly Relevant'], f"HR mismatch for '{p_bn}': expected {p_row['Highly Relevant']}, got {hr_count}"
    assert pr_count == p_row['Partially Relevant'], f"PR mismatch for '{p_bn}': expected {p_row['Partially Relevant']}, got {pr_count}"
    assert nr_count == p_row['Not Relevant'], f"NR mismatch for '{p_bn}': expected {p_row['Not Relevant']}, got {nr_count}"
    assert len(sub) == p_row['Total'], f"Total mismatch for '{p_bn}': expected {p_row['Total']}, got {len(sub)}"

print("✓ Per-prompt per-label counts match Generation_Plan.xlsx exactly.")

# 6. Check duplicates
dup_resp_bn = batch_df['Response'].duplicated().sum()
dup_resp_en = batch_df['Response (Translated to English)'].duplicated().sum()
assert dup_resp_bn == 0, f"Found {dup_resp_bn} duplicate Bengali responses in Batch 28"
assert dup_resp_en == 0, f"Found {dup_resp_en} duplicate English responses in Batch 28"

# Check duplicates against original dataset
orig_responses_bn = set(orig_df['Response'].dropna().tolist())
orig_responses_en = set(orig_df['Response (Translated to English)'].dropna().tolist())

batch_responses_bn = set(batch_df['Response'].tolist())
batch_responses_en = set(batch_df['Response (Translated to English)'].tolist())

overlap_bn = batch_responses_bn.intersection(orig_responses_bn)
overlap_en = batch_responses_en.intersection(orig_responses_en)

assert len(overlap_bn) == 0, f"Bengali responses overlap with original dataset: {overlap_bn}"
assert len(overlap_en) == 0, f"English responses overlap with original dataset: {overlap_en}"
print("✓ All responses are unique and none overlap with the original dataset.")

# 7. Check spaces before commas (" , ")
bad_comma_bn = []
bad_comma_en = []
for idx, row in batch_df.iterrows():
    bn = str(row['Response'])
    en = str(row['Response (Translated to English)'])

    # Check if there is a comma without leading space
    if re.search(r'\S,', bn):
        bad_comma_bn.append((idx, bn))
    if re.search(r'\S,', en):
        bad_comma_en.append((idx, en))

assert len(bad_comma_bn) == 0, f"Found Bengali commas without leading space: {bad_comma_bn}"
assert len(bad_comma_en) == 0, f"Found English commas without leading space: {bad_comma_en}"
print("✓ Space before commas (' , ') formatting rule is satisfied for all responses.")

# 8. Check single sentence (no sentence terminators mid-text)
bad_sentence_bn = []
bad_sentence_en = []

for idx, row in batch_df.iterrows():
    bn = str(row['Response']).strip()
    en = str(row['Response (Translated to English)']).strip()

    # Check if '।' appears anywhere except at the end of Bengali sentence
    if '।' in bn[:-1]:
        bad_sentence_bn.append((idx, bn))

    # Check if '.' appears anywhere except at the end of English sentence
    if '.' in en[:-1]:
        bad_sentence_en.append((idx, en))

assert len(bad_sentence_bn) == 0, f"Found mid-sentence Bengali period/dari: {bad_sentence_bn}"
assert len(bad_sentence_en) == 0, f"Found mid-sentence English period: {bad_sentence_en}"
print("✓ Single sentence rule is satisfied for all responses.")

# 9. Valid labels check
valid_labels = {'Highly Relevant', 'Partially Relevant', 'Not Relevant'}
invalid_labels = set(batch_df['Lable'].tolist()) - valid_labels
assert len(invalid_labels) == 0, f"Invalid labels found: {invalid_labels}"
print("✓ All labels are valid.")

print("=== ALL VERIFICATION CHECKS PASSED SUCCESSFULLY ===")
