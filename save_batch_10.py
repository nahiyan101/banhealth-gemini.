import pandas as pd
from build_full_dataset import df_output

output_filename = "Batch_10_Gemini.xlsx"
df_output.to_excel(output_filename, index=False)
print(f"Successfully saved {len(df_output)} rows to {output_filename}")
