from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# FIXED: Enable CORS so your browser doesn't block frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

blogs = [
    # Mock data so your page isn't blank on launch
    {"id": 1, "title": "Getting Started with FastAPI", "content": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints."}
]
blog_id = 2

class Blog(BaseModel):
    title: str
    content: str

@app.get("/", response_class=HTMLResponse)
def home():
    # Looks for templates/index.html relative to where you run your command
    file_path = "templates/index.html"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return "<h2>Error: templates/index.html not found. Place your HTML file inside a 'templates' folder.</h2>"

@app.get("/blogs")
def get_blogs():
    return blogs

# FIXED: Added endpoint to get an individual blog post when clicking "Read More"
@app.get("/blogs/{blog_id}")
def get_blog(blog_id: int):
    for item in blogs:
        if item["id"] == blog_id:
            return item
    raise HTTPException(status_code=404, detail="Blog not found")

@app.post("/blogs")
def create_blog(blog: Blog):
    global blog_id

    new_blog = {
        "id": blog_id,
        "title": blog.title,
        "content": blog.content
    }

    blogs.append(new_blog)
    blog_id += 1
    return new_blog

@app.put("/blogs/{blog_id}")
def update_blog(blog_id: int, blog: Blog):
    for item in blogs:
        if item["id"] == blog_id:
            item["title"] = blog.title
            item["content"] = blog.content
            return item
    return {"message": "Blog not found"}

@app.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int):
    global blogs
    blogs = [b for b in blogs if b["id"] != blog_id]
    return {"message": "Deleted Successfully"}