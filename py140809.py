'''
Consider the following list: students = [ ["Amit", 85, 78, 92], ["Riya", 90, 88, 95], ["Rahul", 70, 75, 68], ["Sneha", 92, 91, 89] ]
Calculate total marks of each student.  Calculate average marks.  Find the student with the highest average.  
Find the student with the lowest average. 
 Display students having an average greater than 80.  Sort students according to their average marks. 
'''
def calculate_total_and_average(students):
    for student in students:
        total = sum(student[1:])
        average = total / (len(student) - 1)
        student.append(total)
        student.append(average)
def find_highest_and_lowest_average(students):
    highest_avg= max(students, key=lambda x: x[-1])
    lowest_avg= min(students, key=lambda x: x[-1])
    return highest_avg, lowest_avg
def students_above_average(students, threshold=80):
    return [student for student in students if student[-1] > threshold]
def sort_students_by_average(students):
    return sorted(students, key=lambda x: x[-1], reverse=True)
students = [ ["Amit", 85, 78, 92], ["Riya", 90, 88, 95], ["Rahul", 70, 75, 68], ["Sneha", 92, 91, 89] ]
calculate_total_and_average(students)
highest_student, lowest_student = find_highest_and_lowest_average(students)
above_average_students = students_above_average(students)
sorted_students = sort_students_by_average(students)
print("Students with total and average marks:", students)
print("Student with the highest average:", highest_student)
print("Student with the lowest average:", lowest_student)
print("Students with average greater than 80:", above_average_students)
print("Students sorted by average marks:", sorted_students)

