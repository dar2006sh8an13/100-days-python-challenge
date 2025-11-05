# filter data in pandas
# show student with marks > 80
import os
import pandas as pd

# Build path to the CSV next to this script so the script works when run from any cwd
csv_path = os.path.join(os.path.dirname(__file__), "students.csv")

# The provided CSV is formatted like a markdown table (pipes and a separator row).
# Read it using '|' as separator, then clean column names and values.
df = pd.read_csv(csv_path, sep='|', engine='python')

# Clean up column names and trim whitespace
df.columns = df.columns.str.replace(r"\|", "", regex=True).str.strip()

# Convert Marks to numeric where possible; non-numeric (like the ----- row) become NaN
df['Marks'] = pd.to_numeric(df.get('Marks'), errors='coerce')

# Drop rows that don't have a valid numeric Marks value
df = df.dropna(subset=['Marks'])

# Trim text columns
if 'Name' in df.columns:
	df['Name'] = df['Name'].astype(str).str.strip()
if 'USN' in df.columns:
	df['USN'] = df['USN'].astype(str).str.strip()

# Show students with Marks > 80
result = df.loc[df['Marks'] > 80, ['Name', 'USN', 'Marks']]
print(result)