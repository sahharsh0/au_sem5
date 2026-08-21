'''
program to replace the last value of tuples in a list. 
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)] 
'''
a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
result = []
for t in a:
    result.append(t[:-1] + (100,))
print(result)