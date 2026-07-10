from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Portfolio Blog API")

# Allow JavaScript to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store blogs in memory
blogs = []


# Model
class Blog(BaseModel):
    title: str
    content: str


# Home
@app.get("/")
def home():
    return {"message": "Portfolio Blog API is Running 🚀"}


# ---------------- CREATE ----------------
@app.post("/blogs")
def create_blog(blog: Blog):
    new_blog = {
        "id": len(blogs) + 1,
        "title": blog.title,
        "content": blog.content
    }

    blogs.append(new_blog)

    return {
        "message": "Blog created successfully",
        "blog": new_blog
    }


# ---------------- READ ALL ----------------
@app.get("/blogs")
def get_blogs():
    return blogs


# ---------------- READ ONE ----------------
@app.get("/blogs/{blog_id}")
def get_blog(blog_id: int):
    for blog in blogs:
        if blog["id"] == blog_id:
            return blog

    raise HTTPException(status_code=404, detail="Blog not found")


# ---------------- UPDATE ----------------
@app.put("/blogs/{blog_id}")
def update_blog(blog_id: int, updated_blog: Blog):

    for blog in blogs:
        if blog["id"] == blog_id:
            blog["title"] = updated_blog.title
            blog["content"] = updated_blog.content

            return {
                "message": "Blog updated successfully",
                "blog": blog
            }

    raise HTTPException(status_code=404, detail="Blog not found")


# ---------------- DELETE ----------------
@app.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int):

    for i, blog in enumerate(blogs):
        if blog["id"] == blog_id:
            deleted = blogs.pop(i)

            return {
                "message": "Blog deleted successfully",
                "blog": deleted
            }

    raise HTTPException(status_code=404, detail="Blog not found")