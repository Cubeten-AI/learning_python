from fastapi import FastAPI, Form

from fastapi.responses import HTMLResponse, RedirectResponse

app=FastAPI()

students=[]

def page(body):
 return f"""<html><head><style>body{{font-family:Arial;background:#f2f2f2}}.c{{width:800px;margin:20px auto;background:#fff;padding:20px}}table,th,td{{border:1px solid #ccc;border-collapse:collapse;padding:8px}}a,button{{padding:8px 12px;margin:4px;display:inline-block;background:#0d6efd;color:#fff;text-decoration:none;border:none}}</style></head><body><div class='c'><h1>Student Management</h1>{body}</div></body></html>"""

@app.get("/",response_class=HTMLResponse)
def home():
 return page("""<form method=post action=/add><input name=ID placeholder=ID required><input name=Name placeholder=Name required><input name=Age placeholder=Age required><input name=Course placeholder=Course required><input name=Marks placeholder=Marks required><button>Add Student</button></form><hr><a href='/display'>Display Students</a><a href='/search'>Search</a><a href='/update'>Update</a><a href='/delete'>Delete</a><a href='/average'>Average</a><a href='/topper'>Topper</a>""")

@app.post("/add")
def add(ID:int=Form(...),Name:str=Form(...),Age:int=Form(...),Course:str=Form(...),Marks:float=Form(...)):
 students.append({"ID":ID,"Name":Name,"Age":Age,"Course":Course,"Marks":Marks});return RedirectResponse("/",303)

@app.get("/display", response_class=HTMLResponse)
def disp():

    sorted_students = sorted(students, key=lambda s: s["ID"])

    rows = "".join(
        f"""
        <tr>
            <td>{s['ID']}</td>
            <td>{s['Name']}</td>
            <td>{s['Age']}</td>
            <td>{s['Course']}</td>
            <td>{s['Marks']}</td>
        </tr>
        """
        for s in sorted_students
    )

    if not rows:
        rows = "<tr><td colspan='5'>No students found.</td></tr>"

    return page(f"""
        <a href="/">Home</a>

        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Age</th>
                <th>Course</th>
                <th>Marks</th>
            </tr>

            {rows}
        </table>
    """)

@app.get("/search",response_class=HTMLResponse)
def sf(): return page("<a href='/'>Home</a><form action='/search_result'><input name=ID><button>Search</button></form>")

@app.get("/search_result",response_class=HTMLResponse)
def sr(ID:int):
 s=next((x for x in students if x["ID"]==ID),None);return page(f"<a href='/'>Home</a><pre>{s if s else 'Not found'}</pre>")

@app.get("/update",response_class=HTMLResponse)
def uf(): return page("<a href='/'>Home</a><form method=post action='/update'><input name=ID placeholder=ID><input name=Name placeholder='New Name'><input name=Age placeholder='New Age'><input name=Course placeholder='New Course'><input name=Marks placeholder='New Marks'><button>Update</button></form>")

@app.post("/update")
def up(ID:int=Form(...),Name:str=Form(None),Age:str=Form(None),Course:str=Form(None),Marks:str=Form(None)):
 for s in students:
  if s["ID"]==ID:
   if Name:s["Name"]=Name
   if Age:s["Age"]=int(Age)
   if Course:s["Course"]=Course
   if Marks:s["Marks"]=float(Marks)
 return RedirectResponse("/display",303)

@app.get("/delete",response_class=HTMLResponse)
def df(): return page("<a href='/'>Home</a><form method=post action='/delete'><input name=ID><button>Delete</button></form>")

@app.post("/delete")
def dd(ID:int=Form(...)):
 global students;students=[s for s in students if s["ID"]!=ID];return RedirectResponse("/display",303)

@app.get("/average",response_class=HTMLResponse)
def avg():
 a=sum(s["Marks"] for s in students)/len(students) if students else 0;return page(f"<a href='/'>Home</a><h2>Average: {a:.2f}</h2>")

@app.get("/topper",response_class=HTMLResponse)
def top():
 t=max(students,key=lambda x:x["Marks"]) if students else None;return page(f"<a href='/'>Home</a><pre>{t}</pre>")