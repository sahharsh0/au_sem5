'''
Write a Python program demonstrating the following set methods: 
 add()  and update()   remove()  and discard()   pop()  and clear() 
'''
a={1, 2, 3, 4, 5}
print("Original set:", a)
a.add(6)
print("Set after adding 6:", a)
a.update([7, 8, 9])
print("Set after updating with [7, 8, 9]:", a)
a.remove(3)
print("Set after removing 3:", a)
a.discard(4)
print("Set after discarding 4:", a)
a.pop()
print("Set after popping an element:", a)
a.clear()
print("Set after clearing all elements:", a)