students = []
courses = []
enrollments = {}
marks = {}

def add_student():
    while True:
        try:
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (dd/mm/yyyy): ")
            students.append((id, name, dob))
            print("Student added successfully!")
            break
        except:
            print("Invalid input, please try again.")
    

def add_course():
    while True:
        try:
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            courses.append({'id': id, 'name': name})
            print("Course added successfully!")
            break
        except:
            print("Invalid input, please try again.")


def enroll_student():
    while True:
        try:
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            if course_id not in enrollments:
                enrollments[course_id] = []
            enrollments[course_id].append(student_id)
            print("Student enrolled successfully!")
            break
        except:
            print("Invalid input, please try again.")


def input_marks():
    if not students:
        print("No students added yet.")
        return
    
    if not courses:
        print("No courses added yet.")
        return
    
    print("\nEnter course ID to input marks for:")
    list_courses()
    course_id = input()
    

    course_exists = False
    for course in courses:
        if course[0] == course_id:
            course_exists = True
            break
    
    if not course_exists:
        print(f"Course with ID {course_id} doesn't exist.")
        return
    
    print("\nEnter student ID to input marks for:")
    list_students()
    student_id = input()
    

    student_exists = False
    student_enrolled = False
    for student in students:
        if student[0] == student_id:
            student_exists = True
            for enrolled_course in student[2]:
                if enrolled_course[0] == course_id:
                    student_enrolled = True
                    break
            break
    
    if not student_exists:
        print(f"Student with ID {student_id} doesn't exist.")
        return
    elif not student_enrolled:
        print(f"Student with ID {student_id} hasn't enrolled in course with ID {course_id}.")
        return
    
    print("\nEnter marks for the student (out of 100):")
    marks = input()
    

    try:
        marks = float(marks)
    except ValueError:
        print("Invalid marks value.")
        return
    
    if marks < 0 or marks > 20:
        print("Marks should be between 0 and 20.")
        return
    

    for student in students:
        if student[0] == student_id:
            for enrolled_course in student[2]:
                if enrolled_course[0] == course_id:
                    enrolled_course[1] = marks
                    print(f"Marks {marks} for student with ID {student_id} in course with ID {course_id} have been updated.")
                    return


def get_marks():
    while True:
        try:
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            if course_id in marks and student_id in marks[course_id]:
                print(f"Student {student_id} scored {marks[course_id][student_id]} marks in {course_id}.")
            else:
                print("Marks not found for this student in this course.")
            break
        except:
            print("Invalid input, please try again.")


def list_students():
    print("List of students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")


def list_courses():
    print("List of courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")


def list_student_marks():
    student_id = input("Enter student ID: ")
    print(f"Marks for student {student_id}:")
    for course_id in marks:
        if student_id in enrollments.get(course_id, []):
            print(f"{course_id}: {marks[course_id][student_id]}")


while True:
    print("\nMenu:")
    print("0 - Exit")
    print("1 - Add a new student")
    print("2 - Add a new course")
    print("3 - Enroll a student in a course")
    print("4 - Input marks for a student in a course")
    print("5 - Get a student's marks for a course")
    print("6 - List all students")
    print("7 - List all courses")
    print("8 - List a student's marks for all courses")

    choice = input("\nEnter your choice: ")

    if choice == "0":
        print("Goodbye!")
        break
    elif choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        enroll_student()
    elif choice == "4":
        input_marks()
    elif choice == "5":
        get_marks()
    elif choice == "6":
        list_students()
    elif choice == "7":
        list_courses()
    elif choice == "8":
        list_student_marks()
    else:
        print("Invalid choice, please try again.")