''' 
Create a list containing 10 integers and:  Display the list.  Find the length of the list.  
Find the maximum and minimum values.  Calculate the sum and average of all elements. 
 Find out the mean ,median  and mode  of the lists item without using any library functions
'''
def length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count
def maximum(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val
def minimum(lst):
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val
def sum(lst):
    total = 0
    for num in lst:
        total += num
    return total
def average(lst):
    total = sum(lst)
    length_of_list = length(lst)
    return total / length_of_list
def mean(lst):
    return average(lst)
def median(lst):
    sorted_lst = sorted(lst)
    n = length(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
def mode(lst):
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes
list = [12, 45, 23, 67, 34, 89, 10, 56, 78, 90]
print("The list is:", list)
print("Length of the list:", length(list))
print("Maximum value in the list:", maximum(list))
print("Minimum value in the list:", minimum(list))
print("Sum of all elements in the list:", sum(list))
print("Average of all elements in the list:", average(list))
print("Mean of the list:", mean(list))
print("Median of the list:", median(list))
print("Mode of the list:", mode(list))

