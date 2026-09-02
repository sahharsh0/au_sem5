#python code to perform function overriding & function overloading
class Shape:
    def area(self):
        return 0
    def perimeter(self):
        return 0
class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius
    def perimeter(self, radius):
        return 2 * 3.14 * radius
class Rectangle(Shape):
    def area(self, length, width):
        return length * width
    def perimeter(self, length, width):
        return 2 * (length + width)
class Calculator:
    def add(self,*args):
        return sum(args)
ob_calc = Calculator()
print("Addition of 2 numbers:", ob_calc.add(5, 10))
print("Addition of 3 numbers:", ob_calc.add(5, 10, 15))
print("Addition of 4 numbers:", ob_calc.add(5, 10, 15, 20))
ob_circle = Circle()
print("Circle Area:", ob_circle.area(5))
print("Circle Perimeter:", ob_circle.perimeter(5))
ob_rectangle = Rectangle()
print("Rectangle Area:", ob_rectangle.area(5, 10))
print("Rectangle Perimeter:", ob_rectangle.perimeter(5, 10))
