class Student:
    """Represents a single student record."""
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentManagementSystem:
    """Manages a collection of students."""
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, age, grade):
        # Check for duplicate roll number
        if any(s.roll_no == roll_no for s in self.students):
            print(f"Error: Roll No {roll_no} already exists.")
            return
        self.students.append(Student(roll_no, name, age, grade))
        print(" Student added successfully.")

    def display_students(self):
        if not self.students:
            print("No student records found.")
            return
        print("\n--- Student Records ---")
        for student in self.students:
            print(student)

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(" Student found:")
                print(student)
                return student
        print(f" No student found with Roll No {roll_no}.")
        return None

    def update_student(self, roll_no, name=None, age=None, grade=None):
        student = self.search_student(roll_no)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            print(" Student record updated.")

    def delete_student(self, roll_no):
        student = self.search_student(roll_no)
        if student:
            self.students.remove(student)
            print(" Student record deleted.")


def main():
    sms = StudentManagementSystem()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            try:
                roll_no = int(input("Enter Roll No: "))
                name = input("Enter Name: ").strip()
                age = int(input("Enter Age: "))
                grade = input("Enter Grade: ").strip()
                sms.add_student(roll_no, name, age, grade)
            except ValueError:
                print(" Invalid input. Please enter correct data types.")

        elif choice == "2":
            sms.display_students()

        elif choice == "3":
            try:
                roll_no = int(input("Enter Roll No to search: "))
                sms.search_student(roll_no)
            except ValueError:
                print(" Invalid Roll No.")

        elif choice == "4":
            try:
                roll_no = int(input("Enter Roll No to update: "))
                name = input("Enter new Name (leave blank to skip): ").strip() or None
                age_input = input("Enter new Age (leave blank to skip): ").strip()
                age = int(age_input) if age_input else None
                grade = input("Enter new Grade (leave blank to skip): ").strip() or None
                sms.update_student(roll_no, name, age, grade)
            except ValueError:
                print(" Invalid input.")

        elif choice == "5":
            try:
                roll_no = int(input("Enter Roll No to delete: "))
                sms.delete_student(roll_no)
            except ValueError:
                print(" Invalid Roll No.")

        elif choice == "6":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print(" Invalid choice. Please select between 1-6.")


if __name__ == "__main__":
    main()