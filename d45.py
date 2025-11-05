#Constructor Overriding
class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name,usn):
        super().__init__(name)
        self.usn = usn

    def display(self):
        print("name:",self.name)
        print("usn:",self.usn)
s = Student("Darshan","1sv24ai010")
s.display()