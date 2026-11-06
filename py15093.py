'''
A = {1, 2, 3, 4, 5, 6} B = {2, 3, 4} C = {7, 8} Write a program to determine: 
1. Whether B is a subset of A.  2. Whether A is a superset of B.  3. Whether C is a subset of A.  
4. Whether A and C are disjoint.  5. Whether B and C are disjoint.
'''
A={1, 2, 3, 4, 5, 6}
B={2, 3, 4}
C={7, 8}

print("Set A:", A)
print("Set B:", B)
print("Set C:", C)
if B.issubset(A):
    print("B is a subset of A.")
else:
    print("B is not a subset of A.")
if A.issuperset(B):
    print("A is a superset of B.")
else:
    print("A is not a superset of B.")
if C.issubset(A):
    print("C is a subset of A.")
else:
    print("C is not a subset of A.")
if  A.isdisjoint(C):
    print("A and C are disjoint.")
else:
    print("A and C are not disjoint.")
if B.isdisjoint(C):
    print("B and C are disjoint.")
else:
    print("B and C are not disjoint.")