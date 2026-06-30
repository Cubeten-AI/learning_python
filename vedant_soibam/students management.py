students = []

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

while True:
    print("\n===== Student Management =====")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Average Marks")
    print("7. Topper")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        marks = int(input("Enter Marks: "))

        students.append([id, name, age, course, marks])

    elif choice == "2":
        if len(students) == 0:
            print("No Students")
        else:
            for s in students:
                print("ID:", s[0])
                print("Name:", s[1])
                print("Age:", s[2])
                print("Course:", s[3])
                print("Marks:", s[4])
                print("Grade:", grade(s[4]))
                print()

    elif choice == "3":
        id = input("Enter ID: ")

        for s in students:
            if s[0] == id:
                print("ID:", s[0])
                print("Name:", s[1])
                print("Age:", s[2])
                print("Course:", s[3])
                print("Marks:", s[4])
                print("Grade:", grade(s[4]))

    elif choice == "4":
        id = input("Enter ID: ")

        for s in students:
            if s[0] == id:
                s[1] = input("New Name: ")
                s[2] = input("New Age: ")
                s[3] = input("New Course: ")
                s[4] = int(input("New Marks: "))
                print("Student Updated")

    elif choice == "5":
        id = input("Enter ID: ")

        for s in students:
            if s[0] == id:
                students.remove(s)
                print("Student Deleted")
                break

    elif choice == "6":
        if len(students) > 0:
            total = 0
            for s in students:
                total = total + s[4]

            average = total / len(students)
            print("Average Marks =", average)
        else:
            print("No Students")

    elif choice == "7":
        if len(students) > 0:
            top = students[0]

            for s in students:
                if s[4] > top[4]:
                    top = s

            print("Topper")
            print("Name:", top[1])
            print("Marks:", top[4])
        else:
            print("No Students")

    elif choice == "8":
        break