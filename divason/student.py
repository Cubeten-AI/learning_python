# Student Management System

students = []

def calculate_grade(marks):
    grade = ""
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    return grade

# Add Student
def add_student():
    student_id = input("Enter Student ID: ")
    name = str(input("Enter Name: "))
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    mark = int(input("enter the mark:"))
    grade = calculate_grade(mark)

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": mark,
        "Grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


# Display All Students
def display_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\n------------------- Student Records -------------------")
        print("ID\tName\tAge\tCourse\tMarks\tGrade")
        print("-------------------------------------------------------")

        for student in students:
            print(f"{student['ID']}\t{student['Name']}\t{student['Age']}\t{student['Course']}\t{student['Marks']}\t{student['Grade']}")


# Search Student
def search_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["ID"] == student_id:
            print("\nStudent Found")
            print("ID     :", student["ID"])
            print("Name   :", student["Name"])
            print("Age    :", student["Age"])
            print("Course :", student["Course"])
            print("Marks  :", student["Marks"])
            print("Grade  :", student["Grade"])
            return

    print("Student not found.\n")


# Update Student
def update_student():
    student_id = input("Enter Student ID to Update: ")

    for student in students:
        if student["ID"] == student_id:
            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            student["Course"] = input("Enter New Course: ")

            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


# Delete Student
def delete_student():
    student_id = input("Enter Student ID to Delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


# Calculate Grade



# Find Topper
def find_topper():
    if len(students) == 0:
        print("No student records found.")
        return

    topper = students[0]

    for student in students:
        if student["Marks"] > topper["Marks"]:
            topper = student

    print("\n========== TOPPER ==========")
    print("Student ID :", topper["ID"])
    print("Name       :", topper["Name"])
    print("Age        :", topper["Age"])
    print("Course     :", topper["Course"])
    print("Marks      :", topper["Marks"])
    print("Grade      :", topper["Grade"])
    print("============================")


# Main Program
while True:

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Grade")
    print("7. Find Topper")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice (1-8): "))

        if choice == 1:
             add_student()

        elif choice == 2:
             display_students()

        elif choice == 3:
             search_student()

        elif choice == 4:
             update_student()

        elif choice == 5:
             delete_student()

        elif choice == 6:
             calculate_grade()

        elif choice == 7:
             find_topper()

        elif choice == 8:
             print("Thank you for using Student Management System.")
             break

        else:
             print("Invalid choice! Please try again.")
    except ValueError:
         print("inavid choice")