from fastapi import FastAPI

app = FastAPI()

students = {
    1: {"name": "ben", "sem": 4},
    2: {"name": "deepa", "sem": 6},
    3: {"name": "jeshmita", "sem": 6},
    4: {"name": "sunibala", "sem": 6},
    5: {"name": "vivek", "sem": 6},
    6: {"name": "denson", "sem": 6},
    7: {"name": "vedic", "sem": 6},
    8: {"name": "vedant", "sem": 6}
}

@app.get("/")
def root():
    return {"message": "wow"}

@app.get("/student")
def get_students():
    return students

@app.get("/student/{id}")
def get_student_by_id(id: int):
    if id in students:
        return students[id]
    return {"message": "Student not found"}