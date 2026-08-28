'''
Consider  data = {     "A": 10, 
    "B": 20, 
    "C": 10, 
    "D": 30, 
    "E": 20 
} 
Write a program to find and display all duplicate values. 
'''
data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}
duplicates = []
for value in data.values():
    if list(data.values()).count(value) > 1 and value not in duplicates:
        duplicates.append(value)
print("Duplicate values:", duplicates)