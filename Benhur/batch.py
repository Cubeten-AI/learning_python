from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

students = {
    1: {"name": "Benhur Heikrujam", "semester": "4"},
    2: {"name": "Denson Saikhom", "semester": "6"},
    3: {"name": "Abujam Vivek Luwang", "semester": "6"},
    4: {"name": "Vedic Soibam", "semester": "6"},
    5: {"name": "Vedant Soibam", "semester": "6"},
    6: {"name": "Angom Sunibala", "semester": "6"},
    7: {"name": "Deepa Moirangthem", "semester": "6"},
    8: {"name": "Jeshmita Yaikhom", "semester": "6"}
}


# ---------------- API ROUTES ----------------

@app.get("/students")
def get_students():
    return {"students": students}


@app.get("/students/{id}")
def get_student_by_id(id: int):
    if id in students:
        return students[id]
    return {"message": "student not found"}


# ---------------- UI ROUTE ----------------

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Dashboard</title>

        <!-- Icons -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

        <style>
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
            }}

            .header {{
                text-align: center;
                padding: 20px;
                font-size: 28px;
                font-weight: bold;
            }}

            .container {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                padding: 20px;
            }}

            .card {{
                background: rgba(255,255,255,0.1);
                border-radius: 15px;
                padding: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.3);
                backdrop-filter: blur(10px);
                transition: 0.3s;
            }}

            .card:hover {{
                transform: scale(1.05);
                background: rgba(255,255,255,0.2);
            }}

            .icon {{
                font-size: 30px;
                margin-bottom: 10px;
                color: #00ffcc;
            }}

            .id {{
                font-weight: bold;
                color: #ffd369;
            }}
        </style>
    </head>

    <body>

        <div class="header">
            <i class="fa-solid fa-graduation-cap"></i> Student Dashboard
        </div>

        <div class="container">
            {''.join([
                f'''
                <div class="card">
                    <div class="icon"><i class="fa-solid fa-user"></i></div>
                    <div class="id">ID: {sid}</div>
                    <div><i class="fa-solid fa-id-card"></i> Name: {data["name"]}</div>
                    <div><i class="fa-solid fa-layer-group"></i> Semester: {data["semester"]}</div>
                </div>
                '''
                for sid, data in students.items()
            ])}
        </div>

    </body>
    </html>
    """
    return html_content