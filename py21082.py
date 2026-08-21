'''
program to create tuple with different data types
'''
a = (1, "Hello", 3.4)
print("Tuple a is:", a)
a=()
for i in range(1, 6):
    a = a + (input("Enter a value: "),)
print("Tuple a is:", a)