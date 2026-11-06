'''
python_students = {"Amit", "Riya", "Rahul", "Sneha", "Ankit"} java_students = {"Riya", "Rahul", "Priya", "Ankit", "Karan"} 
Write a program to find: 1. Students enrolled in both courses.  2. Students enrolled only in Python. 
 3. Students enrolled only in Java.  4. Students enrolled in either Python or Java but not both.  
 5. Total number of unique students. 
'''
python_students = {"Amit", "Riya", "Rahul", "Sneha", "Ankit"}
java_students = {"Riya", "Rahul", "Priya", "Ankit", "Karan"}
print("Python Students:", python_students)
print("Java Students:", java_students)
print("Students enrolled in both courses:", python_students.intersection(java_students))
print("Students enrolled only in Python:", python_students.difference(java_students))
print("Students enrolled only in Java:", java_students.difference(python_students))
print("Students enrolled in either Python or Java but not both:", python_students.symmetric_difference(java_students))
print("Total number of unique students:", len(python_students.union(java_students)))
