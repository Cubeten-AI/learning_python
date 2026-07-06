from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# ✅ Fixed dictionary (added commas)
students = {
    1: {"name": "Benhur", "sem": 4},
    2: {"name": "Denson", "sem": 6},
    3: {"name": "Vivek", "sem": 6},
    4: {"name": "Vedic", "sem": 6},
    5: {"name": "Vedant", "sem": 6},
    6: {"name": "Deepa", "sem": 6},
    7: {"name": "Sunibala", "sem": 6},
    8: {"name": "Jesmita", "sem": 6},
}

# -------------------------
# API ENDPOINTS
# -------------------------

@app.get("/students")
def get_students():
    return {"student_list": students}


@app.get("/student/{id}")
def get_student_by_id(id: int):
    if id in students:
        return {"id": id, "student": students[id]}
    return {"message": "student not found"}

# -------------------------
# UI PAGE
# -------------------------

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student List</title>
        <style>
            body {
                font-family: Arial;
                background: #f4f4f4;
                text-align: center;
            }
            table {
                margin: auto;
                border-collapse: collapse;
                width: 60%;
                background: white;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 10px;
            }
            th {
                background: #333;
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>Student List</h1>

        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Semester</th>
            </tr>
    """

    for sid, data in students.items():
        html_content += f"""
            <tr>
                <td>{sid}</td>
                <td>{data['name']}</td>
                <td>{data['sem']}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)