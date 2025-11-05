#Metthod Overriding
class Animal:
    def sound(self):
        print("Animals make sound")
class Dog(Animal):
    def sound(self):
        print("dog barks")
d = Dog()
d.sound()