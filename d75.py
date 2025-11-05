#basic pandas: create dataframe
import pandas as pd
data = {"name":["darshanpl","abhi","rahul"],"marks":[90,90,90]}
df = pd.DataFrame(data)
print(df)