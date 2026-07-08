from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

blogs = []

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "blogs": blogs, "edit": None}
    )

@app.post("/add")
def add_blog(title: str = Form(...), content: str = Form(...)):
    blogs.append({"title": title, "content": content})
    return RedirectResponse("/", status_code=303)

@app.get("/edit/{id}")
def edit_blog(id: int, request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "blogs": blogs, "edit": id}
    )

@app.post("/update/{id}")
def update_blog(id: int, title: str = Form(...), content: str = Form(...)):
    blogs[id]["title"] = title
    blogs[id]["content"] = content
    return RedirectResponse("/", status_code=303)

@app.get("/delete/{id}")
def delete_blog(id: int):
    blogs.pop(id)
    return RedirectResponse("/", status_code=303)