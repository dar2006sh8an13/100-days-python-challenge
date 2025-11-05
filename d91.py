#student report generator(CSV result)
import pandas as pd
df = pd.read_csv("student.csv")
df["total"]=df.iloc[:,1:].sum(axis=1)
df["average"]=df["total"]/(df.shape[1]-1)
df["grade"] = df["average"].apply(lambda x:"A" if x>=85 else "B" if x>=70 else "C" if x>=50 else "fail")
df.to_csv("final_report.csv",index=False)
print("report generated")