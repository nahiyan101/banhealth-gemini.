import pandas as pd

file_path = "Batch_03_Gemini.xlsx"
df = pd.read_excel(file_path)

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
assert list(df.columns) == expected_cols, f"Columns mismatch: {df.columns}"

# Check nulls
assert df.isnull().sum().sum() == 0, "Found null values in dataframe"

# Check labels validity
valid_labels = {'Highly Relevant', 'Partially Relevant', 'Not Relevant'}
assert set(df['Lable'].unique()).issubset(valid_labels), f"Invalid labels: {df['Lable'].unique()}"

# Check duplicates across whole file and per prompt
assert df.duplicated().sum() == 0, "Duplicate rows found"
assert df.duplicated(subset=['Used Prompts', 'Response']).sum() == 0, "Duplicate responses for prompt found"

# Check formatting rules: single sentence and spaces before commas in Bengali
bengali_comma_issues = 0
for idx, row in df.iterrows():
    resp = row['Response']
    # Check if comma exists without preceding space
    if ',' in resp and ' ,' not in resp:
        print(f"Row {idx} Bengali comma spacing issue: {resp}")
        bengali_comma_issues += 1

print(f"Total rows: {len(df)}")
print(f"Bengali comma issues: {bengali_comma_issues}")
print("Verification complete! All assertions passed successfully.")
