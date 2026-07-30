class Student:
    def __init__(self, student_id, name, course, marks):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = marks

    def calculate_grade(self):
        #self.marks = float(self.marks)  # Ensure marks is a float for comparison
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"ID    : {self.student_id}")
        print(f"Name  : {self.name}")
        print(f"Course: {self.course}")
        print(f"Marks : {self.marks}")
        print(f"Grade : {self.calculate_grade()}")
        print("-" * 30)


class StudentManagement:
    def __init__(self):
        self.students = []

    # Add Student
    def add_student(self):
        student_id = input("Enter Student ID: ")

        # Check duplicate ID
        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists!")
                return

        name = str(input("Enter Name: "))
        course = str( input("Enter Course: "))
        marks = float(input("Enter Marks: "))

        student = Student(student_id, name, course, marks)
        self.students.append(student)

        print("Student Added Successfully!")

    # Display All Students
    def display_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n===== Student List =====")
        for student in self.students:
            student.display()

    # Search Student
    def search_student(self):
        student_id = input("Enter Student ID to Search: ")

        for student in self.students:
            if student.student_id == student_id:
                print("\nStudent Found")
                student.display()
                return

        print("Student Not Found.")

    # Update Student
    def update_student(self):
        student_id = input("Enter Student ID to Update: ")

        for student in self.students:
            if student.student_id == student_id:
                student.name = input("Enter New Name: ")
                student.course = input("Enter New Course: ")
                student.marks = float(input("Enter New Marks: "))
                print("Student Updated Successfully!")
                return

        print("Student Not Found.")

    # Delete Student
    def delete_student(self):
        student_id = int(input("Enter Student ID to Delete: "))

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found.")

    # Find Topper
    def find_topper(self):
        if not self.students:
            print("No student records found.")
            return

        topper = max(self.students, key=lambda s: s.marks)

        print("\n===== Topper =====")
        topper.display()


# Main Program
sms = StudentManagement()

while True:
    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Exit")
    try:
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            sms.add_student()

        elif choice == 2:
            sms.display_students()

        elif choice == 3:
            sms.search_student()

        elif choice == 4:
            sms.update_student()

        elif choice == 5:
            sms.delete_student()

        elif choice == 6:
            sms.find_topper()

        elif choice == 7:
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid Choice! Please try again.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")    