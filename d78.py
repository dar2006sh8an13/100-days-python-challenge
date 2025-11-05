#add new colum in pandas
import os
import pandas as pd

# Read the students.csv which is formatted like a markdown table (pipes)
csv_path = os.path.join(os.path.dirname(__file__), "students.csv")
df = pd.read_csv(csv_path, sep='|', engine='python')

# Clean column names and normalize to lowercase for consistent access
df.columns = df.columns.str.replace(r"\|", "", regex=True).str.strip().str.lower()

# Remove any empty/unnamed columns that result from leading/trailing separators
df = df.loc[:, df.columns.str.len() > 0]

# Drop columns where all values are NaN (these come from the outer pipes in the markdown table)
df = df.dropna(axis=1, how='all')

# Coerce marks to numeric and drop rows without a valid numeric mark (e.g., separator row)
df['marks'] = pd.to_numeric(df.get('marks'), errors='coerce')
df = df.dropna(subset=['marks'])

# Convert marks to integers and compute result
df['marks'] = df['marks'].astype(int)
df['result'] = ['Pass' if x >= 50 else 'Fail' for x in df['marks']]

print(df)
