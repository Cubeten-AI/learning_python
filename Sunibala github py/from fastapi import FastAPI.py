from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students = [
    {"id": 1, "name": "Ben", "age": 20, "course": "CS", "marks": 85},
    {"id": 2, "name": "Suni", "age": 21, "course": "IT", "marks": 92},
    {"id": 3, "name": "Deepa", "age": 20, "course": "CS", "marks": 78},
    {"id": 4, "name": "Denson", "age": 22, "course": "ECE", "marks": 88},
    {"id": 5, "name": "Vedict", "age": 21, "course": "IT", "marks": 95},
    {"id": 6, "name": "Vedant", "age": 20, "course": "CS", "marks": 67},
    {"id": 7, "name": "Jeshmita", "age": 21, "course": "ECE", "marks": 90},
    {"id": 8, "name": "Vivek", "age": 22, "course": "IT", "marks": 82}
]

def get_grade(marks):
    if marks >= 90: return "A"
    elif marks >= 80: return "B"
    elif marks >= 70: return "C"
    elif marks >= 60: return "D"
    else: return "F"

@app.get("/")
def home():
    return {"message": "Student API is running"}

@app.get("/students")
def get_students():
    # Add grade to each student
    result = []
    for s in students:
        s_copy = s.copy()
        s_copy["grade"] = get_grade(s["marks"])
        result.append(s_copy)
    return {"students": result}

@app.get("/average")
def get_average():
    avg = sum(s["marks"] for s in students) / len(students)
    return {"average_marks": round(avg, 2)}

@app.get("/topper")
def get_topper():
    topper = max(students, key=lambda x: x["marks"])
    topper["grade"] = get_grade(topper["marks"])
    return {"topper": topper}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)