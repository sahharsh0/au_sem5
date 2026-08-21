'''
Write a program to remove duplicate elements from a list.
'''
l = [1, 2, 3, 4, 2, 5, 1, 6, 3]
uni=[]
for i in l:
    if i not in uni:
        uni.append(i)
print("The original list is:", l)
print("The list after removing duplicates is:", uni)