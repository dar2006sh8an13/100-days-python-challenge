#OOP:Employee Salary Example
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(f"Employee:{self.name},salary{self.salary}")
e1 =  Employee("Darshan PL",10000)
e1.show
