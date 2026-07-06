from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students = {
    1: {"name": "Ben", "sem": 4},
    2: {"name": "Suni", "sem": 6},
    3: {"name": "Deepa", "sem": 6},
    4: {"name": "Denson", "sem": 6},
    5: {"name": "Vedict", "sem": 6},
    6: {"name": "Vedant", "sem": 6},
    7: {"name": "Jeshmita", "sem": 6},
    8: {"name": "Vivek", "sem": 6}
}

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/student")
def get_students():
    return {"Student_list": students}

@app.get("/student/{id}")
def get_student_by_id(id: int):
    if id in students:
        return students[id]
    return {"message": "Student not found"}