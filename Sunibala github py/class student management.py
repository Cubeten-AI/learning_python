class Student:
    student_list = []
    
    def __init__(self, id, name, age, course, marks):
        self.id = id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
    
    def add_student(self):
        # Check if ID already exists
        for s in Student.student_list:
            if s["id"] == self.id:
                print(f"ID {self.id} already exists")
                return
        student_data = {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }
        Student.student_list.append(student_data)
        print(f"Student {self.name} added successfully.")
    
    @classmethod
    def display_all(cls):
        if not cls.student_list:
            print("No students found")
            return
        print("\n=== All Students ===")
        for s in cls.student_list:
            grade = cls.get_grade(s["marks"])
            print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']} | Marks: {s['marks']} | Grade: {grade}")
        print()
    
    @classmethod
    def search(cls):
        print("Search by: 1.ID  2.Name")
        ch = input("Enter choice: ")
        found = False
        
        if ch == "1":
            id = int(input("Enter ID: "))
            for s in cls.student_list:
                if s["id"] == id:
                    grade = cls.get_grade(s["marks"])
                    print(f"\nFound: ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}, Marks: {s['marks']}, Grade: {grade}")
                    found = True
        elif ch == "2":
            name = input("Enter Name: ").lower()
            for s in cls.student_list:
                if s["name"].lower() == name:
                    grade = cls.get_grade(s["marks"])
                    print(f"\nFound: ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}, Marks: {s['marks']}, Grade: {grade}")
                    found = True
        if not found: print("Student not found")
    
    @classmethod
    def update(cls):
        id = int(input("Enter ID to update: "))
        for s in cls.student_list:
            if s["id"] == id:
                print("Enter new details:")
                s["name"] = input("Name: ")
                s["age"] = input("Age: ")
                s["course"] = input("Course: ")
                s["marks"] = int(input("Marks: "))
                print("Student updated successfully")
                return
        print("Student not found")
    
    @classmethod
    def delete(cls):
        id = int(input("Enter ID to delete: "))
        for s in cls.student_list:
            if s["id"] == id:
                cls.student_list.remove(s)
                print("Student deleted successfully")
                return
        print("Student not found")
    
    @classmethod
    def average(cls):
        if cls.student_list:
            avg = sum(s["marks"] for s in cls.student_list) / len(cls.student_list)
            print(f"Average Marks: {round(avg, 2)}")
        else: 
            print("No students to calculate average")
    
    @classmethod
    def topper(cls):
        if cls.student_list:
            t = max(cls.student_list, key=lambda s: s["marks"])
            grade = cls.get_grade(t["marks"])
            print(f"Topper: {t['name']} | ID: {t['id']} | Marks: {t['marks']} | Grade: {grade}")
        else: 
            print("No students found")
    from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Student Management API")


class StudentData(BaseModel):
    id: int
    name: str
    age: int
    course: str
    marks: int


class Student:
    student_list = []

    @staticmethod
    def get_grade(m):
        if m >= 80:
            return "A"
        elif m >= 60:
            return "B"
        elif m >= 40:
            return "C"
        else:
            return "F"

    @classmethod
    def add_student(cls, student):
        for s in cls.student_list:
            if s["id"] == student.id:
                return {"message": "ID already exists"}

        cls.student_list.append(student.dict())
        return {"message": "Student added successfully"}

    @classmethod
    def display_all(cls):
        data = []
        for s in cls.student_list:
            item = s.copy()
            item["grade"] = cls.get_grade(s["marks"])
            data.append(item)
        return data

    @classmethod
    def search_by_id(cls, id):
        for s in cls.student_list:
            if s["id"] == id:
                item = s.copy()
                item["grade"] = cls.get_grade(s["marks"])
                return item
        return {"message": "Student not found"}

    @classmethod
    def update(cls, id, student):
        for s in cls.student_list:
            if s["id"] == id:
                s["name"] = student.name
                s["age"] = student.age
                s["course"] = student.course
                s["marks"] = student.marks
                return {"message": "Student updated successfully"}
        return {"message": "Student not found"}

    @classmethod
    def delete(cls, id):
        for s in cls.student_list:
            if s["id"] == id:
                cls.student_list.remove(s)
                return {"message": "Student deleted successfully"}
        return {"message": "Student not found"}

    @classmethod
    def average(cls):
        if not cls.student_list:
            return {"Average": 0}

        avg = sum(s["marks"] for s in cls.student_list) / len(cls.student_list)
        return {"Average": round(avg, 2)}

    @classmethod
    def topper(cls):
        if not cls.student_list:
            return {"message": "No students found"}

        t = max(cls.student_list, key=lambda x: x["marks"])

        return {
            "id": t["id"],
            "name": t["name"],
            "course": t["course"],
            "marks": t["marks"],
            "grade": cls.get_grade(t["marks"])
        }


Student.student_list = [
    {"id": 1, "name": "Deepa", "age": 20, "course": "CSE", "marks": 92},
    {"id": 2, "name": "Suni", "age": 21, "course": "CSE", "marks": 88},
    {"id": 3, "name": "Jes", "age": 20, "course": "IT", "marks": 75},
    {"id": 4, "name": "Vivek", "age": 22, "course": "ECE", "marks": 65},
    {"id": 5, "name": "Ben", "age": 21, "course": "CSE", "marks": 55},
    {"id": 6, "name": "Den", "age": 23, "course": "MBA", "marks": 35},
]


@app.get("/")
def home():
    return {"message": "Student Management API"}


@app.get("/students")
def get_students():
    return Student.display_all()


@app.get("/students/{id}")
def get_student(id: int):
    return Student.search_by_id(id)


@app.post("/students")
def add_student(student: StudentData):
    return Student.add_student(student)


@app.put("/students/{id}")
def update_student(id: int, student: StudentData):
    return Student.update(id, student)


@app.delete("/students/{id}")
def delete_student(id: int):
    return Student.delete(id)


@app.get("/average")
def average_marks():
    return Student.average()


@app.get("/topper")
def topper():
    return Student.topper()
    @classmethod
    def save_to_file(cls):
        with open("students.txt", "w") as f:
            for s in cls.student_list:
                f.write(f"{s['id']},{s['name']},{s['age']},{s['course']},{s['marks']}\n")
        print("Data saved to students.txt")
    
    @classmethod
    def load_from_file(cls):
        try:
            with open("students.txt", "r") as f:
                cls.student_list = []
                for line in f:
                    id, name, age, course, marks = line.strip().split(",")
                    cls.student_list.append({
                        "id": int(id), "name": name, "age": age, 
                        "course": course, "marks": int(marks)
                    })
            print("Data loaded from file")
        except FileNotFoundError:
            print("No saved file found")
    
    @staticmethod
    def get_grade(m):
        if m >= 80: return "A"
        elif m >= 60: return "B"
        elif m >= 40: return "C"
        else: return "F"

# Load existing data on start
Student.load_from_file()

# Main Menu
while True:
    print("\n========== Student Management System =========")
    print("1. Add Student")
    print("2. Display All Students") 
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Find Topper")
    print("8. Save to File")
    print("9. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        marks = int(input("Enter Marks: "))
        s = Student(id, name, age, course, marks)
        s.add_student()
    elif choice == "2": 
        Student.display_all()
    elif choice == "3": 
        Student.search()
    elif choice == "4": 
        Student.update()
    elif choice == "5": 
        Student.delete()
    elif choice == "6": 
        Student.average()
    elif choice == "7": 
        Student.topper()
    elif choice == "8": 
        Student.save_to_file()
    elif choice == "9": 
        Student.save_to_file()
        print("Exiting... Data saved")
        break
    else: 
        print("Invalid choice")