# export modified data to csv
import os
import pandas as pd

# Use script-relative path and the correct filename (students.csv)
csv_path = os.path.join(os.path.dirname(__file__), "students.csv")

# Read markdown-style table (pipes) robustly
df = pd.read_csv(csv_path, sep='|', engine='python')
df.columns = df.columns.str.replace(r"\|", "", regex=True).str.strip()
df = df.loc[:, df.columns.str.len() > 0]
df = df.dropna(axis=1, how='all')

# Reset index to ensure clean consecutive indexing for rank assignment
df = df.dropna(how='all')
df = df.reset_index(drop=True)

# Create a rank column that matches the dataframe length
df['rank'] = list(range(1, len(df) + 1))

out_path = os.path.join(os.path.dirname(__file__), "update_students.csv")
df.to_csv(out_path, index=False)
print(f"data exported to: {out_path}")