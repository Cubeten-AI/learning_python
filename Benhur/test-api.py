from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

student_list = []

# Home Page
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Management System</title>

        <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

        <style>
            body{
                font-family: Arial, sans-serif;
                background:#f2f2f2;
                margin:0;
                padding:0;
            }

            .container{
                width:70%;
                margin:40px auto;
                background:white;
                padding:20px;
                border-radius:10px;
                box-shadow:0 0 10px gray;
            }

            h1{
                text-align:center;
                color:#007bff;
            }

            table{
                width:100%;
                border-collapse:collapse;
                margin-top:20px;
            }

            th,td{
                border:1px solid #ddd;
                padding:10px;
                text-align:center;
            }

            th{
                background:#007bff;
                color:white;
            }

            .menu{
                margin-top:20px;
            }

            .menu p{
                font-size:18px;
                padding:8px;
            }

            i{
                color:#007bff;
                margin-right:10px;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1><i class="fa-solid fa-user-graduate"></i> Student Management System</h1>

            <div class="menu">
                <p><i class="fa-solid fa-plus"></i> POST /add_student</p>
                <p><i class="fa-solid fa-list"></i> GET /display_students</p>
                <p><i class="fa-solid fa-magnifying-glass"></i> GET /search_student/{ID}</p>
                <p><i class="fa-solid fa-pen"></i> PUT /update_student/{ID}</p>
                <p><i class="fa-solid fa-trash"></i> DELETE /delete_student/{ID}</p>
                <p><i class="fa-solid fa-chart-line"></i> GET /calculate_average_marks</p>
                <p><i class="fa-solid fa-trophy"></i> GET /find_topper</p>
            </div>

        </div>

    </body>
    </html>
    """


@app.post("/add_student")
def add_student(ID: int, Name: str, Age: int, Course: str, Marks: float):

    student = {
        "ID": ID,
        "Name": Name,
        "Age": Age,
        "Course": Course,
        "Marks": Marks
    }

    student_list.append(student)

    return {"message": "Student added successfully", "student": student}


@app.get("/display_students")
def display_students():

    if len(student_list) == 0:
        return {"message": "No students found"}

    return student_list


@app.get("/search_student/{ID}")
def search_student(ID: int):

    for student in student_list:
        if student["ID"] == ID:
            return student

    return {"message": "Student not found"}


@app.put("/update_student/{ID}")
def update_student(ID: int,
                   Name: str = None,
                   Age: int = None,
                   Course: str = None,
                   Marks: float = None):

    for student in student_list:

        if student["ID"] == ID:

            if Name is not None:
                student["Name"] = Name

            if Age is not None:
                student["Age"] = Age

            if Course is not None:
                student["Course"] = Course

            if Marks is not None:
                student["Marks"] = Marks

            return {"message": "Student updated successfully"}

    return {"message": "Student not found"}


@app.delete("/delete_student/{ID}")
def delete_student(ID: int):

    for student in student_list:

        if student["ID"] == ID:
            student_list.remove(student)
            return {"message": "Student deleted successfully"}

    return {"message": "Student not found"}


@app.get("/calculate_average_marks")
def calculate_average_marks():

    if len(student_list) == 0:
        return {"message": "No students found"}

    total = 0

    for student in student_list:
        total += student["Marks"]

    average = total / len(student_list)

    return {"Average Marks": average}


@app.get("/find_topper")
def find_topper():

    if len(student_list) == 0:
        return {"message": "No students found"}

    topper = student_list[0]

    for student in student_list:
        if student["Marks"] > topper["Marks"]:
            topper = student

    return topper


# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)