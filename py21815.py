'''
program to calculate the average value of the numbers in a given tuple of tuples. 
Original Tuple: 
((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)) Average value of the numbers of the said tuple of tuples: 
[30.5, 34.25, 27.0, 23.25] 
'''
a = ((10, 10, 10, 12),
     (30, 45, 56, 45),
     (81, 80, 39, 32),
     (1, 2, 3, 4))
result = []
for t in a:
    average = sum(t) / len(t)
    result.append(average)

print("Average values:", result)