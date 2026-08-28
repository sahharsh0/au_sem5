'''
Develop a complete Student Result Analysis System using dictionaries. 
For each student, store marks in five subjects: 
students = { 
    101: { 
        "name": "Amit", 
        "marks": { 
            "Python": 85,             "DBMS": 78, 
            "OS": 92, 
            "CN": 80, 
            "AI": 88 
        } 
    } 
} 

The program should: 
•	Calculate total and average marks.  
•	Assign grades.  
•	Find the class topper.  
•	Find subject-wise highest marks.  
•	Find subject-wise average marks.  
•	Display students who failed in any subject.  
•	Search student by roll number.  
•	Sort students according to average marks.  
•	Display the complete result in a formatted manner. 
'''
students = {101: {"name": "Amit", "marks": {"Python": 85, "DBMS": 78, "OS": 92, "CN": 80, "AI": 88}}, 102: {"name": "Riya", "marks": {"Python": 92, "DBMS": 85, "OS": 88, "CN": 95, "AI": 90}}, 103: {"name": "Rahul", "marks": {"Python": 65, "DBMS": 72, "OS": 58, "CN": 70, "AI": 60}}, 104: {"name": "Sneha", "marks": {"Python": 95, "DBMS": 91, "OS": 94, "CN": 89, "AI": 96}}}

subjects = ["Python", "DBMS", "OS", "CN", "AI"]

def total(marks):
    return sum(marks.values())

def average(marks):
    return total(marks) / 5

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def complete_result():
    for roll, student in students.items():
        avg = average(student["marks"])
        print(roll, student["name"], "Total:", total(student["marks"]), "Average:", avg, "Grade:", grade(avg))

def topper():
    roll = max(students, key=lambda x: average(students[x]["marks"]))
    print("Topper:", students[roll]["name"], "Average:", average(students[roll]["marks"]))

def highest_marks():
    for subject in subjects:
        roll = max(students, key=lambda x: students[x]["marks"][subject])
        print(subject, ":", students[roll]["marks"][subject], students[roll]["name"])

def subject_average():
    for subject in subjects:
        avg = sum(s["marks"][subject] for s in students.values()) / len(students)
        print(subject, ":", round(avg, 2))

def failed_students():
    for roll, student in students.items():
        failed = [s for s, m in student["marks"].items() if m < 40]
        if failed:
            print(student["name"], "Failed in:", failed)

def search():
    roll = int(input("Enter roll number: "))
    if roll in students:
        print(students[roll])
    else:
        print("Student not found")

def sort_students():
    result = sorted(students.items(), key=lambda x: average(x[1]["marks"]), reverse=True)
    for roll, student in result:
        print(roll, student["name"], "Average:", average(student["marks"]))

while True:
    print("\n1. Complete Result")
    print("2. Class Topper")
    print("3. Subject Highest")
    print("4. Subject Average")
    print("5. Failed Students")
    print("6. Search Student")
    print("7. Sort by Average")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        complete_result()
    elif choice == 2:
        topper()
    elif choice == 3:
        highest_marks()
    elif choice == 4:
        subject_average()
    elif choice == 5:
        failed_students()
    elif choice == 6:
        search()
    elif choice == 7:
        sort_students()
    elif choice == 8:
        break
    else:
        print("Invalid choice")