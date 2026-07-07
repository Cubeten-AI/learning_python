from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Student Management API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],      # Allow all HTTP methods
    allow_headers=["*"],      # Allow all headers
)


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
