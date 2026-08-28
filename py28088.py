'''
8.	Create a nested dictionary containing information about five students. 

students = { 
    101: {"name": "Amit", "Python": 85, "Java": 78}, 
    102: {"name": "Riya", "Python": 92, "Java": 88}, 
    103: {"name": "Rahul", "Python": 76, "Java": 80} 
} 
Write a program to: 
1.	Display all student details.  
2.	Calculate the total marks of each student.  
3.	Calculate the average marks.  
4.	Find the student with the highest average.  
5.	Search for a student using roll number. 
'''
students = {
    101: {"name": "Amit", "Python": 85, "Java": 78},
    102: {"name": "Riya", "Python": 92, "Java": 88},
    103: {"name": "Rahul", "Python": 76, "Java": 80},
    104: {"name": "Sneha", "Python": 89, "Java": 94},
    105: {"name": "Ankit", "Python": 81, "Java": 85}
}

print("Student Details:")
for roll, details in students.items():
    print(roll, details)
print("\nTotal Marks:")
for roll, details in students.items():
    total = details["Python"] + details["Java"]
    print(details["name"], ":", total)
print("\nAverage Marks:")
averages = {}
for roll, details in students.items():
    average = (details["Python"] + details["Java"]) / 2
    averages[roll] = average
    print(details["name"], ":", average)
highest_roll = max(averages, key=averages.get)
print("\nStudent with Highest Average:")
print(students[highest_roll]["name"], ":", averages[highest_roll])
roll_no = int(input("\nEnter roll number to search: "))

if roll_no in students:
    print("Student Found:", students[roll_no])
else:
    print("Student not found")