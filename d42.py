#class with constructor
class Student:
    def __init__(self,name,usn):
        self.name = name
        self.usn = usn
    def show(self):
        print("Name:",self.name)
        print("usn:",self.usn)
s1 = Student("darshanpl","1sv24ai010")
s1.show()
