'''
1.	Create a dictionary containing the following student information: 
•	Roll Number  
•	Name  
•	Department  
•	Semester  
•	CGPA  
Display all the key-value pairs. 
'''

student = {
    "Roll Number": "101",
    "Name": "Harsh Sah",
    "Department": "Computer Science and Engineering",
    "Semester": 5,
    "CGPA": 8.38
}
print(student.keys())
print(student.values())
for key, value in student.items():
    print(key, ":", value)
