import os

class Student:
    def __init__(self, sid, name, age, course, marks):
        self.sid = sid
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def grade(self):
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

    def __str__(self):
        return f"{self.sid},{self.name},{self.age},{self.course},{self.marks}"


class StudentManagement:
    def __init__(self):
        self.students = []
        self.load()

    # Load data from text file
    def load(self):
        if os.path.exists("students.txt"):
            with open("students.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 5: 

                        self.students.append(
                            Student(
                                data[0],
                                data[1],
                                int(data[2]),
                                data[3],
                                float(data[4])
                            )
                        )

    # Save data
    def save(self):
        with open("students.txt", "w") as file:
            for student in self.students:
                file.write(str(student) + "\n")
        print("\nData saved successfully.\n")

    # Add Student
    def add_student(self):
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        self.students.append(Student(sid, name, age, course, marks))
        print("Student Added Successfully.\n")

    # Display Students
    def display_students(self):
        if not self.students:
            print("No Records Found.\n")
            return

        print("\n========== Student List ==========")
        for s in self.students:
            print(f"ID     : {s.sid}")
            print(f"Name   : {s.name}")
            print(f"Age    : {s.age}")
            print(f"Course : {s.course}")
            print(f"Marks  : {s.marks}")
            print(f"Grade  : {s.grade()}")
            print("-" * 30)

    # Search Student
    def search_student(self):
        print("\nSearch By")
        print("1. ID")
        print("2. Name")
        ch = input("Enter Choice: ")

        if ch == "1":
            sid = input("Enter Student ID: ")
            for s in self.students:
                if s.sid == sid:
                    self.show(s)
                    return
        elif ch == "2":
            name = input("Enter Name: ").lower()
            for s in self.students:
                if s.name.lower() == name:
                    self.show(s)
                    return

        print("Student Not Found.\n")

    # Update Student
    def update_student(self):
        sid = input("Enter Student ID to Update: ")

        for s in self.students:
            if s.sid == sid:
                s.name = input("New Name: ")
                s.age = int(input("New Age: "))
                s.course = input("New Course: ")
                s.marks = float(input("New Marks: "))
                print("Student Updated Successfully.\n")
                return

        print("Student Not Found.\n")

    # Delete Student
    def delete_student(self):
        sid = input("Enter Student ID to Delete: ")

        for s in self.students:
            if s.sid == sid:
                self.students.remove(s)
                print("Student Deleted Successfully.\n")
                return

        print("Student Not Found.\n")

    # Average Marks
    def average_marks(self):
        if not self.students:
            print("No Records Found.\n")
            return

        avg = sum(s.marks for s in self.students) / len(self.students)
        print(f"\nAverage Marks = {avg:.2f}\n")

    # Topper
    def topper(self):
        if not self.students:
            print("No Records Found.\n")
            return

        top = max(self.students, key=lambda x: x.marks)
        print("\n========== Topper ==========")
        print("Name :", top.name)
        print("Marks:", top.marks)
        print("Grade:", top.grade())
        print()

    # Display Single Student
    def show(self, s):
        print("\nStudent Details")
        print("ID     :", s.sid)
        print("Name   :", s.name)
        print("Age    :", s.age)
        print("Course :", s.course)
        print("Marks  :", s.marks)
        print("Grade  :", s.grade())
        print()


# Main Program
sm = StudentManagement()

while True:
    print(" ___________Student Management ____________")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average")
    print("7. Find Topper")
    print("8. Save")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        sm.add_student()
    elif choice == "2":
        sm.display_students()
    elif choice == "3":
        sm.search_student()
    elif choice == "4":
        sm.update_student()
    elif choice == "5":
        sm.delete_student()
    elif choice == "6":
        sm.average_marks()
    elif choice == "7":
        sm.topper()
    elif choice == "8":
        sm.save()
    elif choice == "9":
        sm.save()
        print("Thank You!")
        break
    else:
        print("Invalid Choice.\n")