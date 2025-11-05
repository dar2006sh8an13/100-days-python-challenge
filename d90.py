#predict student score
from sklearn.linear_model import LinearRegression
hours = [[1],[2],[3],[4],[5]]
marks = [40,50,60,70,85]
model = LinearRegression()
model.fit(hours,marks)
h = float(input("enter study hours:"))
print("predicted score:",model.predict([[h]]))