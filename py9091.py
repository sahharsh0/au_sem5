'''
1.	College Student Information System: Store student details using dictionaries.(user input) 
Store subject marks using lists. 
Store fixed information using tuples. 
Use sets to identify students participating in multiple activities. 
Generate student performance reports. 
'''
def student_info():
    student = {}
    student['name'] = input("Enter student name: ")
    student['age'] = int(input("Enter student age: "))
    student['roll_number'] = input("Enter roll number: ")
    
    subjects = []
    num_subjects = int(input("Enter number of subjects: "))
    for i in range(num_subjects):
        subject_name = input(f"Enter name of subject {i+1}: ")
        marks = float(input(f"Enter marks for {subject_name}: "))
        subjects.append((subject_name, marks))
    
    student['subjects'] = subjects
    
    activities = set()
    num_activities = int(input("Enter number of activities participated in: "))
    for i in range(num_activities):
        activity_name = input(f"Enter name of activity {i+1}: ")
        activities.add(activity_name)
    
    student['activities'] = activities
    
    return student
def generate_report(student):
    print("\nStudent Performance Report")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Roll Number: {student['roll_number']}")
    
    total_marks = 0
    for subject, marks in student['subjects']:
        print(f"Subject: {subject}, Marks: {marks}")
        total_marks += marks
    
    average_marks = total_marks / len(student['subjects']) if student['subjects'] else 0
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    
    print("Activities Participated In:", ", ".join(student['activities']) if student['activities'] else "None")
print("Student Information System")
students = []
num_students = int(input("Enter number of students: "))
for i in range(num_students):
    print(f"\nEntering details for student {i+1}:")
    student = student_info()
    students.append(student)

for student in students:
    generate_report(student)