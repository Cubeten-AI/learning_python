class Student:
    student_list = []
    
    def __init__(self, id, name, age, course, marks):
        self.id = id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
    
    def add_student(self):
        student_data = {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }
        Student.student_list.append(student_data)
        print(f"Student {self.name} added successfully.")

s1 = Student(1, "Alice", 20, "Math", 95)
s1.add_student()
s2 = Student(2, "Bob", 22, "Science", 88)
s2.add_student()

print(Student.student_list)