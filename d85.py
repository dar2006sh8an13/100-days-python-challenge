#bar chart using matplotlib
import matplotlib.pyplot as plt

students = ["darshan","abhi","rahul"]
marks = [85,90,78]
plt.bar(students,marks)
plt.title("student marks")
plt.xlabel("students")
plt.ylabel("marks")
plt.show()