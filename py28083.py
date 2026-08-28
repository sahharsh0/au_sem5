'''
3.	Create a dictionary containing employee details: 
employee = { 
    "id": 101, 
    "name": "Rahul", 
    "salary": 45000 
} 
Perform the following: 
1.	Add "department": "CSE".  
2.	Update the salary to 50000.  
3.	Add "experience": 5.  
4.	Display the updated dictionary
'''
employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 45000
}
print("Dictionary before adding/updating values: ", employee)
employee["department"] = "CSE"
employee["salary"] = 50000
employee["experience"] = 5
print("Dictionary after adding/updating values: ", employee)