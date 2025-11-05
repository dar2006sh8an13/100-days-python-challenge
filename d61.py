#read CSV file
#Goal:read a CSV and display records
import csv 
with open("student.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)