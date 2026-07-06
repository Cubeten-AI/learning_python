from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

students = {
    1: {"name": "deepa", "sem": 6},
    2: {"name": "suni", "sem": 6},
    3: {"name": "jeshmita", "sem": 6},
    4: {"name": "benhur", "sem": 4},
    5: {"name": "vivek", "sem": 6},
    6: {"name": "vedic", "sem": 6},
    7: {"name": "vedant", "sem": 6}
}

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/students")
def get_students():
    return students

@app.get("/student/{id}")
def get_student_by_id(id: int):
    if id in students:
        return students[id]
    return {"message": "Student not found"}