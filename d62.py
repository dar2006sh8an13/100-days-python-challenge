#write to CSV file
#Goal:write student data to CSV 
import csv
data = [["name","usn","branch"],["darshanpl","1sv24ai010","AIML"],["abhilsh","1sv24cs001","CS"]]
with open("students.csv","w",newline="")as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("CSV file created!")  