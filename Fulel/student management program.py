students = []

# Function to calculate grade
def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A+"
    elif 80 <= marks <= 89:
        return "A"
    elif 70 <= marks <= 79:
        return "B"
    elif 60 <= marks <= 69:
        return "C"
    elif 50 <= marks <= 59:
        return "D"
    else:
        return "F"


while True:
    print("\n========== Student Management ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average")
    print("7. Find Topper")
    print("8. Exit")

    # Exception Handling for Menu Choice
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number from 1 to 8.")
        continue

    # Add Student
    if choice == 1:
        try:
            roll = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course Name: ")
            marks = float(input("Enter Marks: "))

            student = {
                "Roll": roll,
                "Name": name,
                "Age": age,
                "Course": course,
                "Marks": marks
            }

            students.append(student)
            print("Student added successfully!")

        except ValueError:
            print("Invalid input! Age must be an integer and Marks must be a number.")

    # Display Students
    elif choice == 2:
        if len(students) == 0:
            print("No records found!")
        else:
            print("\nStudent Records:")
            for s in students:
                print(f"Roll   : {s['Roll']}")
                print(f"Name   : {s['Name']}")
                print(f"Age    : {s['Age']}")
                print(f"Course : {s['Course']}")
                print(f"Marks  : {s['Marks']}")
                print("-" * 30)

    # Search Student
    elif choice == 3:
        roll = input("Enter Roll Number to search: ")
        found = False

        for s in students:
            if s["Roll"] == roll:
                grade = calculate_grade(s["Marks"])

                print("\nStudent Found:")
                print(f"Roll   : {s['Roll']}")
                print(f"Name   : {s['Name']}")
                print(f"Age    : {s['Age']}")
                print(f"Course : {s['Course']}")
                print(f"Marks  : {s['Marks']}")
                print(f"Grade  : {grade}")

                found = True
                break

        if not found:
            print("Student not found!")

    # Update Student
    elif choice == 4:
        roll = input("Enter Roll Number to update: ")

        for s in students:
            if s["Roll"] == roll:
                try:
                    s["Name"] = input("Enter New Name: ")
                    s["Age"] = int(input("Enter New Age: "))
                    s["Course"] = input("Enter New Course: ")
                    s["Marks"] = float(input("Enter New Marks: "))

                    print("Student updated successfully!")

                except ValueError:
                    print("Invalid input! Age must be integer and Marks must be numeric.")

                break
        else:
            print("Student not found!")

    # Delete Student
    elif choice == 5:
        roll = input("Enter Roll Number to delete: ")

        for s in students:
            if s["Roll"] == roll:
                students.remove(s)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found!")

    # Calculate Average
    elif choice == 6:
        if len(students) == 0:
            print("No student records available!")
        else:
            total = sum(s["Marks"] for s in students)
            average = total / len(students)
            print("Average Marks =", round(average, 2))

    # Find Topper
    elif choice == 7:
        if len(students) == 0:
            print("No student records available!")
        else:
            topper = max(students, key=lambda x: x["Marks"])

            print("\nTopper Details:")
            print(f"Roll   : {topper['Roll']}")
            print(f"Name   : {topper['Name']}")
            print(f"Age    : {topper['Age']}")
            print(f"Course : {topper['Course']}")
            print(f"Marks  : {topper['Marks']}")
            print(f"Grade  : {calculate_grade(topper['Marks'])}")

    # Exit
    elif choice == 8:
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid Choice! Please select a number between 1 and 8.")