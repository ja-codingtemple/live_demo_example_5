# BASE CLASS (PARENT CLASS / SUPERCLASS)
class Animal:
    def __init__(self, name):
        self.name = name
        self.living = True
        self.legCount = 4
        self.location = "Home"
        print(f"{self.name} has been created.")
    
    def walk(self, destination):
        self.location = destination
        print(f"{self.name} walks to {self.location}")
        
# SUBCLASSES (CHILD CLASSES) -- These inherit from the parent class Animal.
class Dog(Animal):
    def bark(self, target):
        print(f"{self.name} barks at {target}")
        
class Cat(Animal):
    def highjump(self, target):
        print(f"{self.name} does a very high jump onto {target}")


animal1 = Dog("Opal")
animal2 = Dog("Luna")
animal3 = Cat("Eclipse")

animal1.walk("the dog park")
animal2.walk("the dog park")
animal3.walk("home")


animal1.bark("the mailman")
animal3.highjump("the kitchen counter")

