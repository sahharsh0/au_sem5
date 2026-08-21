'''
16.	Consider the following tuple: 
students = ( 
    ("Amit", "CSE", (85, 78, 92, 88)), 
    ("Riya", "CSE", (90, 88, 95, 91)), 
    ("Rahul", "ECE", (70, 75, 68, 72)), 
    ("Sneha", "CSE", (92, 91, 89, 94)), 
    ("Arjun", "ECE", (82, 79, 85, 88)) 
) 
Write a Python program to: 
a.	Display the name and department of every student. 
b.	Calculate the total marks of every student. 
c.	Calculate the average marks of every student. 
d.	Find the student with the highest average. 
e.	Find the student with the lowest average. 
f.	Display all students whose average is greater than 85. 
g.	Find the average marks of all CSE students. 

'''
students = (
    ("Amit", "CSE", (85, 78, 92, 88)),
    ("Riya", "CSE", (90, 88, 95, 91)),
    ("Rahul", "ECE", (70, 75, 68, 72)),
    ("Sneha", "CSE", (92, 91, 89, 94)),
    ("Arjun", "ECE", (82, 79, 85, 88))
)
cse_total = 0
cse_count = 0
highest_avg = -1
lowest_avg = 101
highest_student = ""
lowest_student = ""
print("Student Details:")
for student in students:
    name = student[0]
    department = student[1]
    marks = student[2]
    total = sum(marks)
    average = total / len(marks)
    print(name, "-", department)
    print("Total:", total)
    print("Average:", average)
    if average > highest_avg:
        highest_avg = average
        highest_student = name
    if average < lowest_avg:
        lowest_avg = average
        lowest_student = name
    if average > 85:
        print("Average greater than 85")
    if department == "CSE":
        cse_total += total
        cse_count += len(marks)
    print()
print("Highest Average:", highest_student, highest_avg)
print("Lowest Average:", lowest_student, lowest_avg)
cse_average = cse_total / cse_count
print("Average marks of all CSE students:", cse_average)