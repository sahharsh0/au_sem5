'''
example to demonstrate diferrence btw append,extend and insert methods of list
and diff btw delete,remove and pop methods of list
'''
l=[1,2,3,4,5]
print("The original list is:",l)
print("The list after appending 6 is:",l.append(6))
print("The list after extending with [7,8] is:",l.extend([7,8]))
print("The list after inserting 9 at index 2 is:",l.insert(2,9))
del l[0]
print("The list after deleting the first element is:",l)
print("The list after removing 4 is:",l.remove(4))
print("The list after popping the last element is:",l.pop())
print("The final list is:",l)