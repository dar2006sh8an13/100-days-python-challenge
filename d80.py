# Mini project: student marks analyzer
# Read marks, calculate average & save result
import os
import pandas as pd

# Read markdown-style table with pipes
csv_path = os.path.join(os.path.dirname(__file__), "students.csv")
df = pd.read_csv(csv_path, sep='|', engine='python')

# Clean column names and data
df.columns = df.columns.str.replace(r"\|", "", regex=True).str.strip()
df = df.loc[:, df.columns.str.len() > 0]  # Remove empty columns
df = df.dropna(axis=1, how='all')         # Remove all-NaN columns

# Drop separator row (contains dashes)
df = df[~df['Name'].str.contains('---', na=False)]

# Convert test scores to numeric, removing any whitespace
for col in ['Test1', 'Test2', 'Test3']:
    df[col] = pd.to_numeric(df[col].str.strip(), errors='coerce')

# Calculate average of test scores
df['Average'] = df[['Test1', 'Test2', 'Test3']].mean(axis=1)

# Determine pass/fail status (>= 40 is pass)
df['Status'] = df['Average'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

# Save results
out_path = os.path.join(os.path.dirname(__file__), "final_result.csv")
df.to_csv(out_path, index=False)

print("\nAnalysis complete. Results saved to:", out_path)
print("\nStudent Results:")
print(df[['Name', 'USN', 'Test1', 'Test2', 'Test3', 'Average', 'Status']])