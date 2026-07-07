from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# -------------------------
# Student Data
# -------------------------

students = {
    1: {"name": "Benhur", "age": 20, "course": "B.Tech", "sem": 4, "marks": 82},
    2: {"name": "Denson", "age": 21, "course": "B.Tech", "sem": 6, "marks": 88},
    3: {"name": "Vivek", "age": 21, "course": "B.Tech", "sem": 6, "marks": 91},
    4: {"name": "Vedic", "age": 20, "course": "B.Tech", "sem": 6, "marks": 79},
    5: {"name": "Vedant", "age": 22, "course": "B.Tech", "sem": 6, "marks": 95},
    6: {"name": "Deepa", "age": 21, "course": "B.Tech", "sem": 6, "marks": 86},
    7: {"name": "Sunibala", "age": 21, "course": "B.Tech", "sem": 6, "marks": 90},
    8: {"name": "Jesmita", "age": 20, "course": "B.Tech", "sem": 6, "marks": 84},
}

# -------------------------
# Helper: Save to File
# -------------------------

def save_to_file():
    with open("students.txt", "w") as file:
        for sid, data in students.items():
            file.write(
                f"ID: {sid}, Name: {data['name']}, Age: {data['age']}, "
                f"Course: {data['course']}, Semester: {data['sem']}, Marks: {data['marks']}\n"
            )

# =========================================================
# UI PAGE
# =========================================================

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Management System</title>
        <style>
            body { font-family: Arial; background: #f4f4f4; text-align: center; }
            table { margin: auto; border-collapse: collapse; width: 70%; background: white; }
            th, td { border: 1px solid #ddd; padding: 10px; }
            th { background: #333; color: white; }
        </style>
    </head>
    <body>
        <h1>Student Management System</h1>

        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Age</th>
                <th>Course</th>
                <th>Semester</th>
                <th>Marks</th>
            </tr>
    """

    for sid, data in students.items():
        html_content += f"""
            <tr>
                <td>{sid}</td>
                <td>{data['name']}</td>
                <td>{data['age']}</td>
                <td>{data['course']}</td>
                <td>{data['sem']}</td>
                <td>{data['marks']}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)

# =========================================================
# API ENDPOINTS
# =========================================================

@app.get("/display_students")
def get_students():
    return {"student_list": students}


@app.get("/student/{id}")
def get_student(id: int):
    return students.get(id, {"message": "Student not found"})


# -------------------------
# ADD STUDENT + SAVE FILE
# -------------------------
@app.post("/add_student")
def add_student(id: int, name: str, age: int, course: str, sem: int, marks: float):

    if id in students:
        return {"message": "Student ID already exists"}

    students[id] = {
        "name": name,
        "age": age,
        "course": course,
        "sem": sem,
        "marks": marks
    }

    save_to_file()  # 🔥 AUTO SAVE

    return {
        "message": "Student added successfully",
        "student": students[id]
    }


# -------------------------
# UPDATE STUDENT + SAVE FILE
# -------------------------
@app.put("/update_student/{id}")
def update_student(id: int, name: str, age: int, course: str, sem: int, marks: float):

    if id not in students:
        return {"message": "Student not found"}

    students[id] = {
        "name": name,
        "age": age,
        "course": course,
        "sem": sem,
        "marks": marks
    }

    save_to_file()  # 🔥 AUTO SAVE

    return {
        "message": "Student updated successfully",
        "student": students[id]
    }


# -------------------------
# DELETE STUDENT + SAVE FILE
# -------------------------
@app.delete("/delete_student/{id}")
def delete_student(id: int):

    if id not in students:
        return {"message": "Student not found"}

    deleted = students.pop(id)

    save_to_file()  # 🔥 AUTO SAVE

    return {
        "message": "Student deleted successfully",
        "student": deleted
    }


# -------------------------
# AVERAGE MARKS
# -------------------------
@app.get("/average")
def average_marks():

    if len(students) == 0:
        return {"average_marks": 0}

    total = sum(s["marks"] for s in students.values())
    return {"average_marks": total / len(students)}


# -------------------------
# TOPPER
# -------------------------
@app.get("/topper")
def topper():

    if len(students) == 0:
        return {"message": "No students available"}

    topper_id = max(students, key=lambda x: students[x]["marks"])

    return {
        "id": topper_id,
        "student": students[topper_id]
    }


# -------------------------
# MANUAL SAVE (optional)
# -------------------------
@app.get("/save")
def save_students():
    save_to_file()
    return {"message": "Student records saved successfully"}