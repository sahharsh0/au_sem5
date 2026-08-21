'''
How to create 2D,3D,4D,5D Lists in Python and access their values
'''
l2=[[1,2,3],[4,5,6],[7,8,9]]
print("The original 2D list is:",l2)
print("The element at row 1, column 2 is:",l2[1][2])
print("The element at row 0, column 1 is:",l2[0][1])
l3=[[[1,2],[3,4]],[[5,6],[7,8]]]
print("The original 3D list is:",l3)
print("The element at row 1, column 0, depth 1 is:",l3[1][0][1])
l4=[[[[1,2],[3,4]],[[5,6],[7,8]]],[[[9,10],[11,12]],[[13,14],[15,16]]]]
print("The original 4D list is:",l4)
print("The element at row 1, column 0, depth 1, dimension 0 is:",l4[1][0][1][0])
l5 = [[[[[1, 2], [3, 4]]]]]
print("The original 5D list is:",l5)
print("The element at row 0, column 0, depth 0, dimension 0, hyperdimension 0 is:",l5[0][0][0][1][0])

