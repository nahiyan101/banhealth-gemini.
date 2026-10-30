import pandas as pd
import re

# 1. Load generated batch 27 and plan
df_gen = pd.read_excel('Batch_27_Gemini.xlsx')
df_plan = pd.read_excel('Generation_Plan.xlsx', sheet_name='Prompts per Batch')
b27_plan = df_plan[df_plan['Batch'] == 27]

print("=== VERIFICATION REPORT FOR BATCH 27 ===")

# Check columns
expected_cols = [
    'Symptoms Genres',
    'Symptoms Genres (Translated to English)',
    'Used Prompts',
    'Used Prompts (Translated to English)',
    'Response',
    'Response (Translated to English)',
    'Lable'
]
assert list(df_gen.columns) == expected_cols, f"Columns mismatch: {df_gen.columns}"
print("✓ Column names and order are exact.")

# Check nulls
assert not df_gen.isnull().any().any(), "Found empty cells!"
print("✓ No empty cells found.")

# Check total rows
assert len(df_gen) == 498, f"Expected 498 total rows, got {len(df_gen)}"
print("✓ Total row count matches expected 498 rows.")

# Check counts per prompt and label
for idx, p_row in b27_plan.iterrows():
    p_bn = p_row['Used Prompts']
    hr_exp = p_row['Highly Relevant']
    pr_exp = p_row['Partially Relevant']
    nr_exp = p_row['Not Relevant']
    tot_exp = p_row['Total']

    sub = df_gen[df_gen['Used Prompts'] == p_bn]
    assert len(sub) == tot_exp, f"Prompt '{p_bn}': expected total {tot_exp}, got {len(sub)}"

    hr_act = len(sub[sub['Lable'] == 'Highly Relevant'])
    pr_act = len(sub[sub['Lable'] == 'Partially Relevant'])
    nr_act = len(sub[sub['Lable'] == 'Not Relevant'])

    assert hr_act == hr_exp, f"Prompt '{p_bn}': HR expected {hr_exp}, got {hr_act}"
    assert pr_act == pr_exp, f"Prompt '{p_bn}': PR expected {pr_exp}, got {pr_act}"
    assert nr_act == nr_exp, f"Prompt '{p_bn}': NR expected {nr_exp}, got {nr_act}"

print("✓ Per-prompt row counts and label distributions match Generation_Plan.xlsx exactly.")

# Check duplicate responses
duplicates_bn = df_gen[df_gen.duplicated(subset=['Used Prompts', 'Response'], keep=False)]
duplicates_en = df_gen[df_gen.duplicated(subset=['Used Prompts', 'Response (Translated to English)'], keep=False)]
assert len(duplicates_bn) == 0, f"Found duplicate BN responses:\n{duplicates_bn}"
assert len(duplicates_en) == 0, f"Found duplicate EN responses:\n{duplicates_en}"
print("✓ No duplicate responses found for any prompt.")

# Check comma formatting: every comma must have a space before it
comma_errors_bn = []
comma_errors_en = []
for i, row in df_gen.iterrows():
    # Check BN response: if there's a comma not preceded by space
    # Matches any non-space followed immediately by comma
    if re.search(r'\S,', row['Response']):
        comma_errors_bn.append((i, row['Response']))
    if re.search(r'\S,', row['Response (Translated to English)']):
        comma_errors_en.append((i, row['Response (Translated to English)']))

assert len(comma_errors_bn) == 0, f"BN comma errors: {comma_errors_bn}"
assert len(comma_errors_en) == 0, f"EN comma errors: {comma_errors_en}"
print("✓ All commas have spaces before them (' , ').")

# Check single-sentence constraint (no daria । or period . in the middle)
sentence_errors = []
for i, row in df_gen.iterrows():
    # Check if there are multiple sentence terminators
    bn_resp = row['Response'].strip()
    en_resp = row['Response (Translated to English)'].strip()

    # Remove trailing terminator
    if bn_resp.endswith('।') or bn_resp.endswith('?'):
        bn_mid = bn_resp[:-1]
    else:
        bn_mid = bn_resp

    if en_resp.endswith('.') or en_resp.endswith('?'):
        en_mid = en_resp[:-1]
    else:
        en_mid = en_resp

    if '।' in bn_mid:
        sentence_errors.append((i, 'BN middle daria', bn_resp))
    if '.' in en_mid:
        # allow e.g. ACE inhibitor, type-2, etc if not period
        # check if period is followed by space/capital or ends sentence
        if re.search(r'\.\s+[A-Z]', en_mid):
            sentence_errors.append((i, 'EN multiple sentences', en_resp))

assert len(sentence_errors) == 0, f"Sentence errors found: {sentence_errors}"
print("✓ All responses are single sentences.")

# Compare against original dataset to ensure no exact matches
df_orig = pd.read_excel('BanHealthAIRespRelv3(All-Processed).xlsx')
orig_responses = set(df_orig['Response'].dropna().tolist())
gen_responses = set(df_gen['Response'].tolist())
overlap = orig_responses.intersection(gen_responses)
assert len(overlap) == 0, f"Overlap with original dataset found: {overlap}"
print("✓ Zero overlap with original dataset responses.")

print("=== ALL CHECKS PASSED SUCCESSFULLY ===")
