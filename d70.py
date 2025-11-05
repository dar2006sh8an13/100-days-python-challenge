#student marks average system
#Goal:enter marks calculate average &grade
marks = []
for i in range(5):
    marks.append(int(input(f"enter mark {i+1}:")))
avg = sum(marks)/5
if avg >=90:grade ="A"
elif avg >=75:grade ="B"
elif avg >=50: grade = "c"
else: grade = "fail"
print("avg:",avg)
print("grade:",grade)    