'''
Create a list of five student names. Perform the following:  Add a new student using append().  
Insert a student at the third position using insert().  Remove a student using remove().  Display the final list.
'''
list=['Harsh','Arya','Aarav','Souvik','Argha']
print("The list of students is:", list)
list.append('Keshav')
print("The list of students after adding Keshav is:", list)
list.insert(2, 'Isha')
print("The list of students after inserting Isha at the third position is:", list)
list.remove('Arya')
print("The list of students after removing Arya is:", list)