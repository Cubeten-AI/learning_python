from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

app = FastAPI(title="Todo App")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    cursor.execute("SELECT * FROM todo ORDER BY id")
    todos = cursor.fetchall()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "todos": todos
        }
    )


@app.post("/add")
def add_todo(
    name: str = Form(...),
    work: str = Form(...)
):

    cursor.execute(
        """
        INSERT INTO todo(name, work)
        VALUES(%s,%s)
        """,
        (name, work)
    )

    connection.commit()

    return RedirectResponse("/", status_code=303)


@app.get("/delete/{id}")
def delete_todo(id: int):

    cursor.execute(
        "DELETE FROM todo WHERE id=%s",
        (id,)
    )

    connection.commit()

    return RedirectResponse("/", status_code=303)


@app.get("/edit/{id}", response_class=HTMLResponse)
def edit_page(id: int, request: Request):

    cursor.execute(
        "SELECT * FROM todo WHERE id=%s",
        (id,)
    )

    todo = cursor.fetchone()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "edit": todo,
            "todos": get_all()
        }
    )


@app.post("/update/{id}")
def update_todo(
    id: int,
    name: str = Form(...),
    work: str = Form(...)
):

    cursor.execute(
        """
        UPDATE todo
        SET name=%s,
            work=%s
        WHERE id=%s
        """,
        (
            name,
            work,
            id
        )
    )

    connection.commit()

    return RedirectResponse("/", status_code=303)


@app.get("/search", response_class=HTMLResponse)
def search(id: int, request: Request):

    cursor.execute(
        "SELECT * FROM todo WHERE id=%s",
        (id,)
    )

    todo = cursor.fetchone()

    if todo:
        todos = [todo]
    else:
        todos = []

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "todos": todos
        }
    )


def get_all():

    cursor.execute(
        "SELECT * FROM todo ORDER BY id"
    )

    return cursor.fetchall()
