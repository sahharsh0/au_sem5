'''
Consider 
      dict1 = {"A": 10, "B": 20, "C": 30}      dict2 = {"D": 40, "E": 50, "F": 60} 
Write a program to merge the two dictionaries. 
Then create another example where both dictionaries contain some common keys and demonstrate how duplicate keys are handled. 

'''
dict1 = {"A": 10, "B": 20, "C": 30}
dict2 = {"D": 40, "E": 50, "F": 60}

dict1.update(dict2)
print("Merged Dictionary:", dict1)

dict3 = {"A": 10, "B": 20, "C": 30}
dict4 = {"B": 50, "C": 60, "D": 40}

dict3.update(dict4)
print("Dictionary with Common Keys:", dict3)