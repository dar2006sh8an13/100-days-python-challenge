#Mini Project: Student Information System(OOP Version)
class Student:
    def __init__(self,name,usn,branch,sem,gender):
        self.name = name
        self.usn = usn
        self.branch = branch
        self.sem = sem
        self.gender = gender
    def display(self):
        print(f"name:",self.name)
        print(f"usn:",self.usn)
        print(f"branch:",self.branch)
        print(f"semster:",self.sem)
        print(f"gender:",self.gender)

s = Student("darshan","1sv24ai010","aiml",3,"male")
s.display()