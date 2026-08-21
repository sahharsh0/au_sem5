'''
Consider the following list a=[22,20,3,40,15,60,17,28,9] 
i. Perform Bubble sort on above array. 
ii. Perform selection sort on above array. 
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
l=[22, 20, 3, 40, 15, 60, 17, 28, 9]
print("Original list:", l)
print("List after bubble sort:", bubble_sort(l.copy()))
print("List after selection sort:", selection_sort(l.copy()))