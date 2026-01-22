# decorator

def my_decorator(func):
    def wrapper(self):
        self.length = 10
        self.breadth = 20
        return func(self)
    return wrapper

class Rectangle:

    @my_decorator
    def perimeter(self):
        print("Perimeter of a reactangle is : ",2*(self.length + self.breadth))


    
    def area(self):
        print("Area of a reactangle is : ",self.length * self.breadth)

    
obj = Rectangle()
obj.perimeter()