import matplotlib.pyplot as plt
labels = ["python","java","c++","js"]
percent = [40,25,20,15]
plt.pie(percent,labels=labels,autopct="%1.1f%%")
plt.title("programing language prefernce")
plt.show()