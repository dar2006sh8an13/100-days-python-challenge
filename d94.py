#create excel file &write data
from openpyxl import workbook

wb=workbook()
sheet=wb.active
sheet["a1"]="name"
sheet["b1"]="marks"
sheet["a2"]="darshan"
sheet["b2"]=95
wb.save("students.xlsx")
print("excel file created")