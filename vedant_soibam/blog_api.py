from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import sqlite3
import shutil
import os

app = FastAPI(title="Full-Stack Portfolio API")

# --- 1. SETUP FOLDERS AND CORS ---
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. SQLITE DATABASE INITIALIZATION ---
DB_NAME = "portfolio_data.db"

def init_db():
    """Creates the database file and table if they don't exist yet."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS blogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL
            )
        """)
        conn.commit()

# Run the database setup immediately when the server starts
init_db() 

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row # This lets us read data like a dictionary
    return conn

# --- 3. DATA MODELS ---
class Blog(BaseModel):
    title: str
    description: str

class BlogResponse(Blog):
    id: int

# --- 4. API ROUTES (Now talking to the database!) ---

@app.get("/blogs", response_model=List[BlogResponse])
def get_blogs():
    conn = get_db_connection()
    # Read all rows from the database
    db_blogs = conn.execute("SELECT * FROM blogs ORDER BY id DESC").fetchall()
    conn.close()
    
    # Convert SQL rows into JSON format
    return [{"id": row["id"], "title": row["title"], "description": row["description"]} for row in db_blogs]

@app.post("/add_blog", response_model=BlogResponse)
def add_blog(blog: Blog):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Insert new data into the database
    cursor.execute("INSERT INTO blogs (title, description) VALUES (?, ?)", (blog.title, blog.description))
    conn.commit()
    new_id = cursor.lastrowid # Get the ID that SQLite automatically generated
    conn.close()
    
    return {"id": new_id, "title": blog.title, "description": blog.description}

@app.put("/edit_blog/{blog_id}", response_model=BlogResponse)
def edit_blog(blog_id: int, updated_blog: Blog):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Update the specific row that matches the ID
    cursor.execute("UPDATE blogs SET title = ?, description = ? WHERE id = ?", 
                   (updated_blog.title, updated_blog.description, blog_id))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Blog not found")
        
    conn.close()
    return {"id": blog_id, "title": updated_blog.title, "description": updated_blog.description}

@app.delete("/delete_blog/{blog_id}")
def delete_blog(blog_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Permanently delete the row matching the ID
    cursor.execute("DELETE FROM blogs WHERE id = ?", (blog_id,))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Blog not found")
        
    conn.close()
    return {"message": "Blog permanently deleted from database"}

# --- 5. IMAGE UPLOAD ROUTE ---
@app.post("/upload_profile")
async def upload_profile_image(file: UploadFile = File(...)):
    file_location = f"static/profile_image.jpg"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    return {"info": "File saved", "url": f"http://127.0.0.1:8000/{file_location}"}