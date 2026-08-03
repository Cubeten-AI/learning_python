file = "Student.txt"

while True:
    print("\n===== Student File Handling =====")
    print("1. Add Student Details")
    print("2. Read Student Details")
    print("3. Update Student Details")
    print("4. Delete Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
            name = input("Enter Name: ")
            roll = input("Enter Roll No: ")
            course = input("Enter Course: ")
    
            with open(file, "a") as f:
                f.write("\n")
                f.write(f"Name: {name}\n")
                f.write(f"Roll No: {roll}\n")
                f.write(f"Course: {course}\n")
    
            print("Student details appended successfully!")
    elif choice == "2":
        try:
            with open(file, "r") as f:
                print("\nStudent Details")
                print("----------------")
                print(f.read())
        except FileNotFoundError:
            print("File not found!")

    

    elif choice == "3":
         f = open("Student.txt", "r")
         data = f.read()
         f.close()

         old_name = input("Enter old name: ")
         new_name = input("Enter new name: ")

         old_roll = input("Enter old roll no: ")
         new_roll = input("Enter new roll no: ")

         old_course = input("Enter old course: ")
         new_course = input("Enter new course: ")

         data = data.replace(old_name, new_name)
         data = data.replace(old_course, new_course)
         data = data.replace(old_roll, new_roll)

         f = open("Student.txt", "w")
         f.write(data)
         f.close()

         print("Data Updated Successfully")    

    elif choice == "4":
        
       name = input("Enter the Name to delete: ")
  
    
       with open(file, "r") as f:
            data = f.read()

            records = data.strip().split("\n\n")
            found = False

            with open(file, "w") as f:
             for record in records:
                if f"Name: {name}" not in record:
                    f.write(record + "\n\n")
                else:
                    found = True

            if found:
             print("Student record deleted successfully!")
            else:
             print("Student not found!")

        

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")