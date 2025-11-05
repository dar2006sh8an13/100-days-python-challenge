#drop missing values
import pandas as pd
df = pd.read_csv("student.csv")
df.dropna(inplace=True)
print(df)