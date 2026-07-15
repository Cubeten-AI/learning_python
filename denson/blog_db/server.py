from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from openai import OpenAI

from dotenv import load_dotenv

import psycopg2
import os

# -----------------------
# Load Environment
# -----------------------

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

# -----------------------
# Database
# -----------------------

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

# -----------------------
# Profile
# -----------------------

with open("profile.txt", "r", encoding="utf-8") as file:
    profile_data = file.read()

profile = {
    "name": "Denson",
    "role": "Python & FastAPI Developer",
    "about": "I love Python, FastAPI, HTML, CSS and building web applications."
}

# -----------------------
# AI Client
# -----------------------

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=NVIDIA_API_KEY
)

# -----------------------
# FastAPI
# -----------------------

app = FastAPI(title="AI Portfolio")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# -----------------------
# Home
# -----------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    cursor.execute(
        "SELECT * FROM blogs ORDER BY id"
    )

    blogs = cursor.fetchall()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "profile": profile,
            "blogs": blogs,
            "answer": "",
            "question": "",
            "edit": None
        }
    )


# -----------------------
# Add Blog
# -----------------------

@app.post("/add")
def add_blog(
    title: str = Form(...),
    content: str = Form(...)
):

    cursor.execute(
        """
        INSERT INTO blogs(title,content)
        VALUES(%s,%s)
        """,
        (title, content)
    )

    connection.commit()

    return RedirectResponse("/", status_code=303)


# -----------------------
# Delete Blog
# -----------------------

@app.get("/delete/{blog_id}")
def delete(blog_id: int):

    cursor.execute(
        "DELETE FROM blogs WHERE id=%s",
        (blog_id,)
    )

    connection.commit()

    return RedirectResponse("/", status_code=303)


# -----------------------
# Edit Page
# -----------------------

@app.get("/edit/{blog_id}", response_class=HTMLResponse)
def edit_page(
    blog_id: int,
    request: Request
):

    cursor.execute(
        "SELECT * FROM blogs WHERE id=%s",
        (blog_id,)
    )

    edit = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM blogs ORDER BY id"
    )

    blogs = cursor.fetchall()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "profile": profile,
            "blogs": blogs,
            "answer": "",
            "question": "",
            "edit": edit
        }
    )


# -----------------------
# Update Blog
# -----------------------

@app.post("/update/{blog_id}")
def update_blog(
    blog_id: int,
    title: str = Form(...),
    content: str = Form(...)
):

    cursor.execute(
        """
        UPDATE blogs
        SET title=%s,
            content=%s
        WHERE id=%s
        """,
        (
            title,
            content,
            blog_id
        )
    )

    connection.commit()

    return RedirectResponse("/", status_code=303)


# -----------------------
# Search
# -----------------------

@app.get("/search", response_class=HTMLResponse)
def search(
    request: Request,
    q: str = ""
):

    cursor.execute(
        """
        SELECT *
        FROM blogs
        WHERE LOWER(title)
        LIKE LOWER(%s)
        ORDER BY id
        """,
        (f"%{q}%",)
    )

    blogs = cursor.fetchall()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "profile": profile,
            "blogs": blogs,
            "answer": "",
            "question": "",
            "edit": None
        }
    )


# -----------------------
# AI Assistant
# -----------------------

@app.post("/ask", response_class=HTMLResponse)
def ask_ai(
    request: Request,
    question: str = Form(...)
):

    system_prompt = f"""
You are Denson's AI assistant.

Profile:

{profile_data}

Rules:

1. Answer questions about Denson only using the profile.

2. If information is missing say:

"I don't have that information about Denson."

3. General questions may be answered normally.

4. Never invent personal information.
"""

    try:

        completion = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": question
                }
            ],

            temperature=0.7,

            max_tokens=1024
        )

        answer = completion.choices[0].message.content

    except Exception as e:

        answer = str(e)

    cursor.execute(
        "SELECT * FROM blogs ORDER BY id"
    )

    blogs = cursor.fetchall()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "profile": profile,
            "blogs": blogs,
            "question": question,
            "answer": answer,
            "edit": None
        }
    )
