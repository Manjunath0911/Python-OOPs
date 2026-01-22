# Task 1:
# Create a Parent class and a Child class. Access parent method.

class Parent:

    def display(self):
        print("its a parent class")
class Child(Parent):
    def show(self):
        print("its a child class ")
c = Child()


# Task 2:
# Use constructor inheritance with super().

class Parent:

    def __init__(self,name , age):
        self.name = name
        self.age = age

    def display(self):
        print("its a parent class",self.name," ",self.age)
class Child(Parent):

    def __init__(self,name , age):
        super().__init__(name,age)

    def show(self):
        print("its a child class ",self.name," ",self.age)
c = Child("dev",24)

