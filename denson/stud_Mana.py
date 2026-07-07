import json

students = {}

# Grade Function
def grade(marks):
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
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    students[sid] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }
    print("Student Added Successfully!")

# Display Students
def display_students():
    if not students:
        print("No students found.")
        return

    for sid, data in students.items():
        print("-" * 30)
        print("ID:", sid)
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("Course:", data["course"])
        print("Marks:", data["marks"])
        print("Grade:", grade(data["marks"]))

# Search Student
def search_student():
    print("1. Search by ID")
    print("2. Search by Name")
    ch = input("Choose: ")

    if ch == "1":
        sid = input("Enter ID: ")
        if sid in students:
            print(students[sid])
        else:
            print("Student not found.")

    elif ch == "2":
        name = input("Enter Name: ").lower()
        found = False
        for sid, data in students.items():
            if data["name"].lower() == name:
                print("ID:", sid)
                print(data)
                found = True
        if not found:
            print("Student not found.")

# Update Student
def update_student():
    sid = input("Enter Student ID: ")

    if sid in students:
        students[sid]["name"] = input("New Name: ")
        students[sid]["age"] = int(input("New Age: "))
        students[sid]["course"] = input("New Course: ")
        students[sid]["marks"] = float(input("New Marks: "))
        print("Updated Successfully!")
    else:
        print("Student not found.")

# Delete Student
def delete_student():
    sid = input("Enter Student ID: ")

    if sid in students:
        del students[sid]
        print("Student Deleted!")
    else:
        print("Student not found.")

# Average Marks
def average_marks():
    if not students:
        print("No students.")
        return

    total = 0
    for data in students.values():
        total += data["marks"]

    print("Average Marks =", total / len(students))

# Topper
def topper():
    if not students:
        print("No students.")
        return

    top_id = max(students, key=lambda x: students[x]["marks"])
    print("Topper")
    print("ID:", top_id)
    print("Name:", students[top_id]["name"])
    print("Marks:", students[top_id]["marks"])

# Save JSON
def save():
    with open("stud_Mana.json", "w") as file:
        json.dump(students, file, indent=4)
    print("Saved Successfully!")

# Menu
while True:
    print("\n====== Student Management ======")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Average Marks")
    print("7. Topper")
    print("8. Save")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        average_marks()
    elif choice == "7":
        topper()
    elif choice == "8":
        save()
    elif choice == "9":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
