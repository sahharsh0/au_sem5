'''
9.	Design a Python program using dictionaries to maintain course registration information. 
courses = { 
    "CS101": { 
        "name": "Python Programming", 
        "credits": 4, 
        "students": 45 
    }, 
    "CS102": { 
        "name": "Data Structures", 
        "credits": 3, 
        "students": 50 
    } 
} 
Your program should provide a menu-driven system with options: 
1.	Add a new course.  
2.	Display all courses.  
3.	Search for a course.  
4.	Update course details.  
5.	Delete a course.  
6.	Find the course having maximum students.  
7.	Exit. 
'''
courses = {
    "CS101": {
        "name": "Python Programming",
        "credits": 4,
        "students": 45
    },
    "CS102": {
        "name": "Data Structures",
        "credits": 3,
        "students": 50
    }
}
while True:
    print("\n===== COURSE REGISTRATION SYSTEM =====")
    print("1. Add a new course")
    print("2. Display all courses")
    print("3. Search for a course")
    print("4. Update course details")
    print("5. Delete a course")
    print("6. Find course having maximum students")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        code = input("Enter course code: ")
        if code in courses:
            print("Course already exists.")
        else:
            name = input("Enter course name: ")
            credits = int(input("Enter credits: "))
            students = int(input("Enter number of students: "))
            courses[code] = {
                "name": name,
                "credits": credits,
                "students": students
            }
            print("Course added successfully.")
    elif choice == 2:
        if len(courses) == 0:
            print("No courses available.")
        else:
            print("\nCourse Details:")
            for code, details in courses.items():
                print("Course Code:", code)
                print("Name:", details["name"])
                print("Credits:", details["credits"])
                print("Students:", details["students"])
                print()
    elif choice == 3:
        code = input("Enter course code to search: ")
        if code in courses:
            print("Course Found:")
            print("Name:", courses[code]["name"])
            print("Credits:", courses[code]["credits"])
            print("Students:", courses[code]["students"])
        else:
            print("Course not found.")
    elif choice == 4:
        code = input("Enter course code to update: ")
        if code in courses:
            print("1. Update name")
            print("2. Update credits")
            print("3. Update number of students")
            update_choice = int(input("Enter your choice: "))
            if update_choice == 1:
                courses[code]["name"] = input("Enter new name: ")
            elif update_choice == 2:
                courses[code]["credits"] = int(input("Enter new credits: "))
            elif update_choice == 3:
                courses[code]["students"] = int(input("Enter new number of students: "))
            else:
                print("Invalid choice.")
                continue
            print("Course updated successfully.")
        else:
            print("Course not found.")
    elif choice == 5:
        code = input("Enter course code to delete: ")
        if code in courses:
            del courses[code]
            print("Course deleted successfully.")
        else:
            print("Course not found.")
    elif choice == 6:
        if len(courses) == 0:
            print("No courses available.")
        else:
            max_course = max(courses, key=lambda x: courses[x]["students"])
            print("Course with maximum students:")
            print("Course Code:", max_course)
            print("Name:", courses[max_course]["name"])
            print("Students:", courses[max_course]["students"])
    elif choice == 7:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
