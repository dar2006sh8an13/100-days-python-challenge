#Multiple Inheritance
class Person:
    def info(self):
        print("this is a person class")
class Student:
    def study(self):
        print("this is a student class")
class CollegeMember():
    def show(self):
        print("this is a college member")

c = CollegeMember()
c.info()
c.study()
c.show()
        