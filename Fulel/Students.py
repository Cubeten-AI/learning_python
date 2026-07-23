
FILE_NAME = "Students.txt"


# Function to calculate grade
def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks < 80:
        return "B"
    elif 60 <= marks < 70:
        return "C"
    elif 50 <= marks < 60:
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

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Enter numbers between 1 and 8.")
        continue

    # Add student 
    if choice == 1:
        try:
            roll = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))

            # Check duplicate roll number
            duplicate = False
            try:
                with open(FILE_NAME, "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        if data[0] == roll:
                            duplicate = True
                            break
            except FileNotFoundError:
                pass

            if duplicate:
                print("Roll Number already exists!")
            else:
                with open(FILE_NAME, "a") as file:
                    file.write(f"{roll},{name},{age},{course},{marks}\n")

                print("Student added successfully!")

        except ValueError:
            print("Invalid input!")

    # Display Students 
    elif choice == 2:
        try:
            with open(FILE_NAME, "r") as file:
                lines = file.readlines()

                if len(lines) == 0:
                    print("No records found!")
                else:
                    print("\nStudent Records")
                    print("-" * 40)

                    for line in lines:
                        roll, name, age, course, marks = line.strip().split(",")

                        print("Roll   :", roll)
                        print("Name   :", name)
                        print("Age    :", age)
                        print("Course :", course)
                        print("Marks  :", marks)
                        print("Grade  :", calculate_grade(float(marks)))
                        print("-" * 40)

        except FileNotFoundError:
            print("No records found!")

    # Search Student 
    elif choice == 3:
        roll_search = input("Enter Roll Number to search: ")

        found = False

        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    roll, name, age, course, marks = line.strip().split(",")

                    if roll == roll_search:
                        print("\nStudent Found")
                        print("Roll   :", roll)
                        print("Name   :", name)
                        print("Age    :", age)
                        print("Course :", course)
                        print("Marks  :", marks)
                        print("Grade  :", calculate_grade(float(marks)))

                        found = True
                        break

            if not found:
                print("Student not found!")

        except FileNotFoundError:
            print("No records found!")

    # Update Student
    elif choice == 4:
        roll_update = input("Enter Roll Number to update: ")

        records = []
        found = False

        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    roll, name, age, course, marks = line.strip().split(",")

                    if roll == roll_update:
                        found = True

                        name = input("Enter New Name: ")
                        age = input("Enter New Age: ")
                        course = input("Enter New Course: ")
                        marks = input("Enter New Marks: ")

                    records.append(f"{roll},{name},{age},{course},{marks}\n")

            if found:
                with open(FILE_NAME, "w") as file:
                    file.writelines(records)

                print("Student updated successfully!")

            else:
                print("Student not found!")

        except FileNotFoundError:
            print("No records found!")

    # Delete Student 
    elif choice == 5:
        roll_delete = input("Enter Roll Number to delete: ")

        records = []
        found = False

        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    roll = line.split(",")[0]

                    if roll == roll_delete:
                        found = True
                    else:
                        records.append(line)

            if found:
                with open(FILE_NAME, "w") as file:
                    file.writelines(records)

                print("Student deleted successfully!")

            else:
                print("Student not found!")

        except FileNotFoundError:
            print("No records found!")

    # Calculate Average 
    elif choice == 6:
        total = 0
        count = 0

        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    total += float(data[4])
                    count += 1

            if count == 0:
                print("No student records available!")
            else:
                average = total / count
                print("Average Marks =", round(average, 2))

        except FileNotFoundError:
            print("No student records available!")

    #  Find Topper 
    elif choice == 7:
        topper = None

        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    roll, name, age, course, marks = line.strip().split(",")

                    if topper is None or float(marks) > float(topper[4]):
                        topper = [roll, name, age, course, marks]

            if topper:
                print("\nTopper Details")
                print("Roll   :", topper[0])
                print("Name   :", topper[1])
                print("Age    :", topper[2])
                print("Course :", topper[3])
                print("Marks  :", topper[4])
                print("Grade  :", calculate_grade(float(topper[4])))
            else:
                print("No student records available!")

        except FileNotFoundError:
            print("No student records available!")

    # Exit
    elif choice == 8:
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid Choice! Please select a number between 1 and 8.")
