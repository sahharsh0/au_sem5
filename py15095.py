'''
.python = {"Amit", "Riya", "Rahul", "Sneha"} java = {"Rahul", "Priya", "Karan", "Sneha"} 
sql = {"Amit", "Rahul", "Priya", "Ankit"} Determine: 
1. Employees who know all three technologies.  2. Employees who know Python and Java. 
 3. Employees who know Python but not Java.  
 4. Employees who know at least one technology.  5. Employees who know exactly two technologies. 
'''
python = {"Amit", "Riya", "Rahul", "Sneha"}
java = {"Rahul", "Priya", "Karan", "Sneha"}
sql = {"Amit", "Rahul", "Priya", "Ankit"}
print("Employees who know all three technologies:", python.intersection(java, sql))
print("Employees who know Python and Java:", python.intersection(java))
print("Employees who know Python but not Java:", python.difference(java))
print("Employees who know at least one technology:", python.union(java, sql))
print("Employees who know exactly two technologies:", python.intersection(java).union(python.intersection(sql)).union(java.intersection(sql)))