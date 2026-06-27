students = []
# Comment
# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Add Student
def add_student():
    sid = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    student = {
        "ID": sid,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks,
        "Grade": calculate_grade(marks)
    }

    students.append(student)
    print("Student Added Successfully!")

# Display Students
def display_students():
    if not students:
        print("No students found.")
        return

    print("\n===== Display All Students =====")
    for s in students:
        print("ID:", s["ID"])
        print("Name:", s["Name"])
        print("Age:", s["Age"])
        print("Course:", s["Course"])
        print("Marks:", s["Marks"])
        print("Grade:", s["Grade"])
        print("-------------------")

# Search Student
def search_student():
    print("\nSearch by")
    print("1. ID")
    print("2. Name")
    choice = int(input("Enter choice: "))

    if choice == 1:
        sid = int(input("Enter ID: "))
        for s in students:
            if s["ID"] == sid:
                print(s)
                return
    elif choice == 2:
        name = input("Enter Name: ")
        for s in students:
            if s["Name"].lower() == name.lower():
                print(s)
                return

    print("Student not found.")

# Update Student
def update_student():
    sid = int(input("Enter Student ID: "))

    for s in students:
        if s["ID"] == sid:
            s["Name"] = input("Enter New Name: ")
            s["Age"] = int(input("Enter New Age: "))
            s["Course"] = input("Enter New Course: ")
            s["Marks"] = int(input("Enter New Marks: "))
            s["Grade"] = calculate_grade(s["Marks"])
            print("Student Updated Successfully!")
            return

    print("Student not found.")

# Delete Student
def delete_student():
    sid = int(input("Enter Student ID to delete: "))

    for s in students:
        if s["ID"] == sid:
            students.remove(s)
            print("Student Deleted Successfully!")
            return

    print("Student not found.")

# Calculate Average
def calculate_average():
    if not students:
        print("No students available.")
        return

    total = sum(s["Marks"] for s in students)
    avg = total / len(students)
    print("Average Marks =", avg)

# Find Topper
def find_topper():
    if not students:
        print("No students available.")
        return

    topper = max(students, key=lambda x: x["Marks"])
    print("\n===== Topper =====")
    print("ID:", topper["ID"])
    print("Name:", topper["Name"])
    print("Marks:", topper["Marks"])
    print("Grade:", topper["Grade"])

# Main Menu
while True:
    print("\n========== Student Management =========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average")
    print("7. Find Topper")
    print("8. Save")
    print("9. Exit")

    choice = int(input("Enter choice: "))

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
        calculate_average()
    elif choice == 7:
        find_topper()
    elif choice == 8:
        print("Data Saved Successfully!")
    elif choice == 9:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")