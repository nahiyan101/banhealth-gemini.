import pandas as pd

plan_df = pd.read_excel('Generation_Plan.xlsx', sheet_name='Prompts per Batch')
batch6_plan = plan_df[plan_df['Batch'] == 6]

out_df = pd.read_excel('Batch_06_Gemini.xlsx')

print("1. Column verification:")
expected_cols = [
    'Symptoms Genres',
    'Symptoms Genres (Translated to English)',
    'Used Prompts',
    'Used Prompts (Translated to English)',
    'Response',
    'Response (Translated to English)',
    'Lable'
]
assert list(out_df.columns) == expected_cols, f"Columns do not match!\nFound: {list(out_df.columns)}"
print("  Columns match expected order exactly.")

print("\n2. Empty cells check:")
assert out_df.isnull().sum().sum() == 0, "Found null/empty cells!"
print("  No null/empty cells found.")

print("\n3. Duplicate response check:")
assert out_df['Response'].duplicated().sum() == 0, "Found duplicate Bengali responses!"
assert out_df['Response (Translated to English)'].duplicated().sum() == 0, "Found duplicate English responses!"
print("  No duplicate responses found.")

print("\n4. Row count verification per prompt and class:")
total_plan_rows = batch6_plan['Total'].sum()
print(f"  Total plan rows: {total_plan_rows}, Actual output rows: {len(out_df)}")
assert len(out_df) == total_plan_rows, f"Total row count mismatch: {len(out_df)} vs {total_plan_rows}"

for idx, plan_row in batch6_plan.iterrows():
    p_bn = plan_row['Used Prompts']
    expected_hr = plan_row['Highly Relevant']
    expected_pr = plan_row['Partially Relevant']
    expected_nr = plan_row['Not Relevant']

    prompt_df = out_df[out_df['Used Prompts'] == p_bn]
    actual_hr = len(prompt_df[prompt_df['Lable'] == 'Highly Relevant'])
    actual_pr = len(prompt_df[prompt_df['Lable'] == 'Partially Relevant'])
    actual_nr = len(prompt_df[prompt_df['Lable'] == 'Not Relevant'])

    print(f"  Prompt: '{p_bn[:30]}...'")
    print(f"    HR: Expected {expected_hr}, Actual {actual_hr}")
    print(f"    PR: Expected {expected_pr}, Actual {actual_pr}")
    print(f"    NR: Expected {expected_nr}, Actual {actual_nr}")

    assert actual_hr == expected_hr, f"HR mismatch for prompt {p_bn}"
    assert actual_pr == expected_pr, f"PR mismatch for prompt {p_bn}"
    assert actual_nr == expected_nr, f"NR mismatch for prompt {p_bn}"

print("\n5. Label values check:")
valid_labels = {'Highly Relevant', 'Partially Relevant', 'Not Relevant'}
actual_labels = set(out_df['Lable'].unique())
assert actual_labels.issubset(valid_labels), f"Invalid labels found: {actual_labels}"
print(f"  Labels present: {actual_labels}")

print("\nALL VERIFICATION CHECKS PASSED SUCCESSFULLY!")
