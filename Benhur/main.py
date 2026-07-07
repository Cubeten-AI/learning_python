from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

student_list = []

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Student Management System</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<style>
body{font-family:Arial;background:#f2f2f2;margin:0}
.container{width:70%;margin:40px auto;background:#fff;padding:20px;border-radius:10px;box-shadow:0 0 10px gray}
h1{text-align:center;color:#007bff}
form{margin-top:20px}
label{font-weight:bold}
input{width:100%;padding:10px;margin:5px 0 15px;border:1px solid #ccc;border-radius:5px;box-sizing:border-box}
button{background:#007bff;color:#fff;border:none;padding:12px 20px;border-radius:5px;cursor:pointer}
button:hover{background:#0056b3}
table{width:100%;border-collapse:collapse;margin-top:20px}
th,td{border:1px solid #ddd;padding:10px;text-align:center}
th{background:#007bff;color:#fff}
.menu p{font-size:18px;padding:4px}
i{color:#007bff;margin-right:8px}
</style>
</head>
<body>
<div class="container">
<h1><i class="fa-solid fa-user-graduate"></i> Student Management System</h1>
<h2>Add Student</h2>
<form action="/add_student_form" method="post">
<label>ID</label><input type="number" name="ID" required>
<label>Name</label><input type="text" name="Name" required>
<label>Age</label><input type="number" name="Age" required>
<label>Course</label><input type="text" name="Course" required>
<label>Marks</label><input type="number" step="0.01" name="Marks" required>
<button type="submit"><i class="fa-solid fa-plus"></i>Add Student</button>
</form>
<hr>
<div class="menu">
<p><i class="fa-solid fa-list"></i> GET /display_students</p>
<p><i class="fa-solid fa-magnifying-glass"></i> GET /search_student/{ID}</p>
<p><i class="fa-solid fa-pen"></i> PUT /update_student/{ID}</p>
<p><i class="fa-solid fa-trash"></i> DELETE /delete_student/{ID}</p>
<p><i class="fa-solid fa-chart-line"></i> GET /calculate_average_marks</p>
<p><i class="fa-solid fa-trophy"></i> GET /find_topper</p>
</div>
</div>
</body>
</html>"""

@app.post("/add_student")
def add_student(ID:int,Name:str,Age:int,Course:str,Marks:float):
    student={"ID":ID,"Name":Name,"Age":Age,"Course":Course,"Marks":Marks}
    student_list.append(student)
    with open("students.txt","a") as f:
        f.write(f"ID: {ID}, Name: {Name}, Age: {Age}, Course: {Course}, Marks: {Marks}\n")
    return {"message":"Student added successfully","student":student}

@app.post("/add_student_form",response_class=HTMLResponse)
def add_student_form(ID:int=Form(...),Name:str=Form(...),Age:int=Form(...),Course:str=Form(...),Marks:float=Form(...)):
    add_student(ID,Name,Age,Course,Marks)
    return "<h2 style='font-family:Arial;color:green;text-align:center'>Student added successfully!</h2><p style='text-align:center'><a href='/'>Back Home</a></p>"

@app.get("/display_students")
def display_students():
    return student_list if student_list else {"message":"No students found"}

@app.get("/search_student/{ID}")
def search_student(ID:int):
    for s in student_list:
        if s["ID"]==ID:return s
    return {"message":"Student not found"}

@app.put("/update_student/{ID}")
def update_student(ID:int,Name:str=None,Age:int=None,Course:str=None,Marks:float=None):
    for s in student_list:
        if s["ID"]==ID:
            if Name is not None:s["Name"]=Name
            if Age is not None:s["Age"]=Age
            if Course is not None:s["Course"]=Course
            if Marks is not None:s["Marks"]=Marks
            return {"message":"Student updated successfully"}
    return {"message":"Student not found"}

@app.delete("/delete_student/{ID}")
def delete_student(ID:int):
    for s in student_list:
        if s["ID"]==ID:
            student_list.remove(s)
            return {"message":"Student deleted successfully"}
    return {"message":"Student not found"}

@app.get("/calculate_average_marks")
def calculate_average_marks():
    if not student_list:return {"message":"No students found"}
    return {"Average Marks":sum(s["Marks"] for s in student_list)/len(student_list)}

@app.get("/find_topper")
def find_topper():
    if not student_list:return {"message":"No students found"}
    return max(student_list,key=lambda s:s["Marks"])

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
