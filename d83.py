#sort dataframe
import pandas as pd
df = pd.read_csv("students.csv")
df = df.sort_values(by="marks",ascending=False)
print(df)