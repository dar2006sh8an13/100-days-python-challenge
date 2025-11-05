#group data
#total marks by department
import pandas as pd
df = pd.read_csv("students.csv")
print(df.groupby("branch")["marks"].sum())
