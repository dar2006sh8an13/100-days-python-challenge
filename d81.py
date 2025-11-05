#handle missing values
import pandas as pd
import numpy as np
df = pd.read_csv("student.csv")
df_fill_zero = df.fillna(0)
print(df)