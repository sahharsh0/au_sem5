'''
program to find repeated items in a tuple
'''
a = (1, 2, 3, 4, 5, 1, 2, 3, 4, 6, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
repeated = []
for item in a:
    if a.count(item) > 1 and item not in repeated:
        repeated.append(item)
print('Repeated items:', repeated)