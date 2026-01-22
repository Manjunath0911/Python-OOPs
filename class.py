class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        print("addition of two number is : ", self.a + self.b)
    
    def sub(self):
        print("subtraction of two number is : ", self.a - self.b)

    def mul(self):
        print("multiplication of two number is : ", self.a * self.b)

    def div(self):
        try:
            result = self.a / self.b
        except ZeroDivisionError:
            print("Cannot divide by zero")
        else:
            print("Division result:", result)

# Create a Student class with marks of 3 subjects and a method to calculate average.

class Student:
    def __init__(self,sub1,sub2,sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def score_avg(self):
        average_score = (self.sub1 + self.sub2 + self.sub3)/3
        print("Average score of a student is : ",average_score)
s = Student(89,92,96)

# Create a Car class with brand and mileage. Create 3 objects.

class Car:
    count_objects = 0
    all_cars = []  
    def __init__(self,brand,mileage):
        self.brand = brand
        self.mileage = mileage
        Car.count_objects += 1
        Car.all_cars.append(self)

    def display(self):
        print(self.brand," : ",self.mileage)
toyoto = Car("toyoto",32)
mahindra = Car("mahindra",22)
benz = Car("benz",12)
for cars in Car.all_cars:
    cars.display()