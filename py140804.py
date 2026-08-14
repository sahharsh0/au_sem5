'''
Write a program to reverse a list without using the built-in reverse() function.
'''
def rev(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list
lst = [1, 2, 3, 4, 5]
print("The original list is:", lst)
print("The reversed list is:", rev(lst))