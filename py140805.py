'''
Write a program to find the occurrence/frequency of a given element in a list. 
'''
def freq(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count
l = [1, 2, 3, 4, 2, 5, 1, 6, 3]
element = 2
print("The original list is:", l)
print(f"The frequency of {element} in the list is:", freq(l, element))