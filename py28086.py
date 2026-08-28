'''
Consider marks = { 
  	 	   "Amit": 85, 
    	 	 "Riya": 92, 
     	 	   "Rahul": 76, 
  	 	   "Sneha": 95, 
   	 	  "Ankit": 88 
} 
Write programs to: 
1.	Sort the dictionary by student name.  
2.	Sort the dictionary by marks in ascending order.  
3.	Sort the dictionary by marks in descending order. 

'''
marks = {
    "Amit": 85,
    "Riya": 92,
    "Rahul": 76,
    "Sneha": 95,
    "Ankit": 88
}
sorted_by_name = dict(sorted(marks.items()))
print("Sorted by student name:", sorted_by_name)
sorted_ascending = dict(sorted(marks.items(), key=lambda x: x[1]))
print("Sorted by marks (Ascending):", sorted_ascending)
sorted_descending = dict(sorted(marks.items(), key=lambda x: x[1], reverse=True))
print("Sorted by marks (Descending):", sorted_descending)