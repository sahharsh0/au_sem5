'''
1. A = {10, 20, 30, 40, 50} B = {30, 40, 50, 60, 70} 
Perform and display: 1. Union  2. Intersection  3. Difference A - B  4. Difference B - A  
5. Symmetric difference  6. Check whether 30 exists in set A.
'''
A={10, 20, 30, 40, 50}
B={30, 40, 50, 60, 70}

print("Set A:", A)
print("Set B:", B)
print("Union of A and B:", A.union(B))
print("Intersection of A and B:", A.intersection(B))
print("Difference of A and B (A - B):", A.difference(B))
print("Difference of B and A (B - A):", B.difference(A))
print("Symmetric difference of A and B:", A.symmetric_difference(B))
if 30 in A:
    print("30 exists in set A.")
else:
    print("30 does not exist in set A.")