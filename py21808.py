'''
program to remove an item from a tuple. 
'''
a = (1, 2, 3, 4, 5)
item = 3
a = tuple(x for x in a if x != item)
print(a)