#line chart
import matplotlib.pyplot as plt
days = [1,2,3,4,5]
sales= [100,120,90,150,180]
plt.plot(days,sales,marker="0")
plt.title("sales growth")
plt.xlabel("day")
plt.ylabel("sales")
plt.show()