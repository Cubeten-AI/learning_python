# Student Management System using TXT File

FILENAME = "students.txt"

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
# ---------------- Add Student ----------------
def add_student():
    sid = int(input("Enter Student ID: "))
    name = str(input("Enter Student Name: "))
    age = int(input("Enter Age: "))
    marks = int(input("Enter mark: "))
    grade = calculate_grade(marks)
    with open(FILENAME, "a") as file:
        file.write(f"{sid},{name},{age},{grade},{marks}\n")

    print("Student added successfully!\n")


# ---------------- Display Students ----------------
def display_students():
    try:
        with open(FILENAME, "r") as file:
            records = file.readlines()

            if len(records) == 0:
                print("No student records found.\n")
                return

            print("\n------ Student Records ------")
            print("{:<10}{:<20}{:<10}{:<10}{:<10}".format("ID", "Name", "Age","mark","Grade"))
            print("-" * 50)

            for line in records:
                sid, name, age, marks, grade = line.strip().split(",")
                print("{:<10}{:<20}{:<10}{:<10}{:<10}".format(sid, name, age, marks, grade))

    except FileNotFoundError:
        print("File not found.\n")


# ---------------- Search Student ----------------
def search_student():
    sid = input("Enter Student ID to Search: ")

    try:
        with open(FILENAME, "r") as file:
            found = False

            for line in file:
                data = line.strip().split(",")

                if data[0] == sid:
                    print("\nStudent Found")
                    print("ID    :", data[0])
                    print("Name  :", data[1])
                    print("Age   :", data[2])
                    print("Grade :", data[3])
                    found = True
                    break

            if not found:
                print("Student ID not found.")

    except FileNotFoundError:
        print("File not found.")


# ---------------- Update Student ----------------
def update_student():
    sid = input("Enter Student ID to Update: ")

    try:
        with open(FILENAME, "r") as file:
            records = file.readlines()

        found = False

        with open(FILENAME, "w") as file:
            for line in records:
                data = line.strip().split(",")

                if data[0] == sid:
                    print("Enter New Details")
                    name = input("New Name: ")
                    age = input("New Age: ")
                    marks = int(input("enter the marks:"))
                    grade = calculate_grade(marks)
                    
                    file.write(f"{sid},{name},{age},{grade},{marks}\n")
                    found = True
                else:
                    file.write(line)

        if found:
            print("Student updated successfully!")
        else:
            print("Student ID not found.")

    except FileNotFoundError:
        print("File not found.")


# ---------------- Delete Student ----------------
def delete_student():
    sid = input("Enter Student ID to Delete: ")

    try:
        with open(FILENAME, "r") as file:
            records = file.readlines()

        found = False

        with open(FILENAME, "w") as file:
            for line in records:
                data = line.strip().split(",")

                if data[0] != sid:
                    file.write(line)
                else:
                    found = True

        if found:
            print("Student deleted successfully!")
        else:
            print("Student ID not found.")

    except FileNotFoundError:
        print("File not found.")


# ---------------- Main Menu ----------------
while True:
    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: "))

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
            print("Thank You!")
            break

        else:
            print("Invalid Choice. Try Again.")
    except ValueError:
        print("inavlid choice")