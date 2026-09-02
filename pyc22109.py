#class calculator to perofrm fnc: add, sub, multiply, div
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
ob = Calculator()
print("Addition:", ob.add(10, 5))
print("Subtraction:", ob.sub(10, 5))
print("Multiplication:", ob.multiply(10, 5))
print("Division:", ob.div(10, 5))