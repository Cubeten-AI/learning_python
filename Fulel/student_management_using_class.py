class Student:
    def __init__(self, roll, name, age, course, marks):
        self.roll = roll
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

# Calculate Grade
    def calculate_grade(self):
        if 90 <= self.marks <= 100:
            return "A+"
        elif 80 <= self.marks < 90:
            return "A"
        elif 70 <= self.marks < 80:
            return "B"
        elif 60 <= self.marks < 70:
            return "C"
        elif 50 <= self.marks < 60:
            return "D"
        else:
            return "F"

# Display Student Details
    def display(self):
        print("-" * 35)
        print(f"Roll Number : {self.roll}")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Course      : {self.course}")
        print(f"Marks       : {self.marks}")
        print(f"Grade       : {self.calculate_grade()}")
        print("-" * 35)


class StudentManagementSystem:

    def __init__(self):
        self.students = []

# Add Student
    def add_student(self):
        try:
            roll = input("Enter Roll Number: ")

           
            for student in self.students:
                if student.roll == roll:
                    print("Roll Number already exists!")
                    return

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))

            if marks < 0 or marks > 100:
                print("Marks should be between 0 and 100.")
                return

            student = Student(roll, name, age, course, marks)
            self.students.append(student)

            print("Student added successfully!")

        except ValueError:
            print("Invalid Input!")

# Display Students
    def display_students(self):

        if len(self.students) == 0:
            print("No student records found!")
            return

        print("\nStudent Records")

        for student in self.students:
            student.display()

# Search Student
    def search_student(self):

        roll = input("Enter Roll Number to search: ")

        for student in self.students:
            if student.roll == roll:
                print("\nStudent Found")
                student.display()
                return

        print("Student not found!")

# Update Student
    def update_student(self):

        roll = input("Enter Roll Number to update: ")

        for student in self.students:

            if student.roll == roll:

                try:
                    student.name = input("Enter New Name: ")
                    student.age = int(input("Enter New Age: "))
                    student.course = input("Enter New Course: ")
                    student.marks = float(input("Enter New Marks: "))

                    if student.marks < 0 or student.marks > 100:
                        print("Marks should be between 0 and 100.")
                        return

                    print("Student updated successfully!")

                except ValueError:
                    print("Invalid Input!")

                return

        print("Student not found!")

# Delete Student
    def delete_student(self):

        roll = input("Enter Roll Number to delete: ")

        for student in self.students:

            if student.roll == roll:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found!")

# Calculate Average 
    def calculate_average(self):

        if len(self.students) == 0:
            print("No student records available!")
            return

        total = 0

        for student in self.students:
            total += student.marks

        average = total / len(self.students)

        print("Average Marks =", round(average, 2))

# Find Topper
    def find_topper(self):

        if len(self.students) == 0:
            print("No student records available!")
            return

        topper = max(self.students, key=lambda x: x.marks)

        print("\nTopper Details")
        topper.display()

    def menu(self):

        while True:

            print("\n========== Student Management System ==========")
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

                if choice == 1:
                    self.add_student()

                elif choice == 2:
                    self.display_students()

                elif choice == 3:
                    self.search_student()

                elif choice == 4:
                    self.update_student()

                elif choice == 5:
                    self.delete_student()

                elif choice == 6:
                    self.calculate_average()

                elif choice == 7:
                    self.find_topper()

                elif choice == 8:
                    print("Exiting... Student Management System!")
                    break

                else:
                    print("Please enter a number between 1 and 8.")

            except ValueError:
                print("Invalid input! Please enter a valid number.")


s = StudentManagementSystem()
s.menu()

