'''
2.	Consider: student = { 
    "name": "Amit", 
    "roll": 101, 
    "department": "CSE", 
    "cgpa": 8.5 
} 
Write a program to: 
1.	Display the student's name.  
2.	Display the CGPA.  
3.	Display the department using the get() method.  
4.	Check whether "email" exists as a key. 

'''

student = {
    "name": "Amit",
    "roll": 101,
    "department": "CSE",
    "cgpa": 8.5
}
print("Name:", student["name"])
print("CGPA:", student["cgpa"])
print("Department:", student.get("department"))
if "email" in student:
    print("Email key exists")
else:
    print("Email key does not exist")