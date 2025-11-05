#class with class variable
class Student:
    college = "SVCE"
    def __init__(self,name,usn):
        self.name = name
        self.usn = usn
s1 = Student("darshan","1sv24ai010")
s1 = Student("abhilash","1sv24cs001")

print(s1.usn,"-",Student.college)
print(s1.usn,"-",Student.college)