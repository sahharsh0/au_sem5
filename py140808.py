'''
Consider the following lists
 a= [22,20,3,40,15,60,17,28,9]   
 b= [4,18,9,4,19,5,6,45,7] 
 Perform merge sort on to the above list. 
'''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
l1=[22, 20, 3, 40, 15, 60, 17, 28, 9]
l2=[4, 18, 9, 4, 19, 5, 6, 45, 7]
print("Original list 1:", l1)
print("List 1 after merge sort:", merge_sort(l1.copy()))
print("Original list 2:", l2)
print("List 2 after merge sort:", merge_sort(l2.copy()))