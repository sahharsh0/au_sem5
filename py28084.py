'''
4.	Create a dictionary containing five subject marks. Write a program to: 
•	Delete one subject using del.  
•	Remove another subject using pop().  
•	Remove the last inserted item using popitem().  
•	Display the remaining dictionary.  
'''
marks = {
    "English": 85,
    "Mathematics": 90,
    "Physics": 88,
    "Chemistry": 92,
    "Computer": 95
}
del marks["English"]
marks.pop("Mathematics")
marks.popitem()
print("Remaining dictionary:", marks)