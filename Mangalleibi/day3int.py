file = "Student.txt"

while True:
    print("\n===== Student File Handling =====")
    print("1. Write Student Details")
    print("2. Read Student Details")
    print("3. Append Student Details")
    print("4. Delete File")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        course = input("Enter Course: ")

        with open(file, "w") as f:
            f.write(f"Name: {name}\n")
            f.write(f"Roll No: {roll}\n")
            f.write(f"Course: {course}\n")

        print("Student details saved successfully!")

    elif choice == "2":
        try:
            with open(file, "r") as f:
                print("\nStudent Details")
                print("----------------")
                print(f.read())
        except FileNotFoundError:
            print("File not found!")

    elif choice == "3":
        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        course = input("Enter Course: ")

        with open(file, "a") as f:
            f.write("\n")
            f.write(f"Name: {name}\n")
            f.write(f"Roll No: {roll}\n")
            f.write(f"Course: {course}\n")

        print("Student details appended successfully!")

    elif choice == "4":
        import os
        if os.path.exists(file):
            os.remove(file)
            print("File deleted successfully!")
        else:
            print("File does not exist!")

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")