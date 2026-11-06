'''
menu driven using fnc to perform fibonacci and factorial of a number, if negative handle invalid input using exception handling and loop
until user wants to exit the program
'''
def fibonacci(n):
    if n < 0: 
        raise ValueError("Negative number")
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
def factorial(n):
    if n < 0: 
        raise ValueError("Negative number")
    f = 1
    for i in range(1, n + 1): 
        f *= i
    return f
while True:
    print("\n1. Fibonacci\n2. Factorial\n3. Exit")
    try:
        ch = int(input("Choice: "))
        if ch == 3:
            break
        n = int(input("Number: "))
        if ch == 1:
            fibonacci(n)
        elif ch == 2:
            print("Factorial =", factorial(n))
        else:
            print("Invalid choice")
    except ValueError as e:
        print("Invalid input:", e)