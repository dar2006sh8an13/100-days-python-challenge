#real linear regression project
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("study.csv") # columns: Hours,Marks
X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

hours = float(input("Hours studied: "))
print("Predicted Marks =", model.predict([[hours]]))
