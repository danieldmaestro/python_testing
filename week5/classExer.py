class Square:
    def __init__(self, length):
        self.length = length
    
    def area(self):
        area = self.length * self.length
        return area

    def perimeter(self):
        perimeter = 4 * self.length
        return perimeter 

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        return area
    
    def perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        return perimeter
    

square1 = Square(7)
print("Area of Square is", square1.area())
print("Perimter of Square is", square1.perimeter())

rectangle1 = Rectangle(15,5)
print("Area of Rectangle is", rectangle1.area())
print("Perimeter of rectangle is", rectangle1.perimeter())
