import os

class Student:
    FILE_NAME = "school.txt"

    def __init__(self, student_id, name, course, marks):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
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

    def save(self):
        with open(Student.FILE_NAME, "a") as file:
            file.write(f"{self.student_id},{self.name},{self.course},{self.marks},{self.grade}\n")

    @staticmethod
    def display_all():
        if not os.path.exists(Student.FILE_NAME):
            print("\nNo student records found.")
            return

        with open(Student.FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("\nNo student records found.")
            return

        print("\n---------------- Student Records ----------------")
        print("ID\tName\tCourse\tMarks\tGrade")
        print("-------------------------------------------------")

        for line in records:
            student = line.strip().split(",")
            print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}")

    @staticmethod
    def search(student_id):
        if not os.path.exists(Student.FILE_NAME):
            print("File not found.")
            return

        found = False

        with open(Student.FILE_NAME, "r") as file:
            for line in file:
                student = line.strip().split(",")

                if student[0] == student_id:
                    print("\nStudent Found")
                    print("ID     :", student[0])
                    print("Name   :", student[1])
                    print("Course :", student[2])
                    print("Marks  :", student[3])
                    print("Grade  :", student[4])
                    found = True
                    break

        if not found:
            print("Student not found.")

     
    



    @staticmethod
    def update(student_id):
        if not os.path.exists(Student.FILE_NAME):
            print("File not found.")
            return

        records = []
        updated = False

        with open(Student.FILE_NAME, "r") as file:
            for line in file:
                student = line.strip().split(",")

                if student[0] == student_id:
                    print("\nEnter New Details")
                    name = input("Enter Name: ")
                    course = input("Enter Course: ")
                    marks = float(input("Enter Marks: "))

                    temp = Student(student_id, name, course, marks)

                    records.append(
                        f"{temp.student_id},{temp.name},{temp.course},{temp.marks},{temp.grade}\n"
                    )
                    updated = True
                else:
                    records.append(line)

        with open(Student.FILE_NAME, "w") as file:
            file.writelines(records)

        if updated:
            print("Student Updated Successfully.")
        else:
            print("Student ID not found.")

    @staticmethod
    def delete(student_id):
        if not os.path.exists(Student.FILE_NAME):
            print("File not found.")
            return

        records = []
        deleted = False

        with open(Student.FILE_NAME, "r") as file:
            for line in file:
                student = line.strip().split(",")

                if student[0] == student_id:
                    deleted = True
                else:
                    records.append(line)

        with open(Student.FILE_NAME, "w") as file:
            file.writelines(records)

        if deleted:
            print("Student Deleted Successfully.")
        else:
            print("Student ID not found.")

    @staticmethod
    def topper():
        if not os.path.exists(Student.FILE_NAME):
            print("No student records found.")
            return

        highest = -1
        topper = None

        with open(Student.FILE_NAME, "r") as file:
            for line in file:
                student = line.strip().split(",")
                marks = float(student[3])

                if marks > highest:
                    highest = marks
                    topper = student

        if topper:
            print("\n---------- Topper ----------")
            print("ID     :", topper[0])
            print("Name   :", topper[1])
            print("Course :", topper[2])
            print("Marks  :", topper[3])
            print("Grade  :", topper[4])


def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Find Topper")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))

            student = Student(student_id, name, course, marks)
            student.save()
            print("Student Added Successfully.")

        elif choice == "2":
            Student.display_all()

        elif choice == "3":
            student_id = input("Enter Student ID: ")
            Student.search(student_id)

        elif choice == "4":
            student_id = input("Enter Student ID to Update: ")
            Student.update(student_id)

        elif choice == "5":
            student_id = input("Enter Student ID to Delete: ")
            Student.delete(student_id)

        elif choice == "6":
            Student.topper()

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


menu()