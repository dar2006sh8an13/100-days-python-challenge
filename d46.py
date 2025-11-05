#Inheritance Example
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def show(self):
        print("brand:",self.brand)

class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    def display(self):
        self.show()
        print("model:",self.model)

c1 = Car("telsa","model s")
c1.display()