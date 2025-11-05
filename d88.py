#train-testsplit(ML Foundation)
from sklearn.model_selection import train_test_split
x=[[1],[2],[3],[4],[5]]
y=[2,4,6,8,10]
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2)
print("train:",X_train,Y_train)
print("test",X_test,Y_test)
