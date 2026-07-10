from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from google import genai
from google.genai import types

with open("profile.txt", "r", encoding="utf-8") as file:
    profile_data = file.read()

app = FastAPI(title="My AI Portfolio")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ==========================
# Gemini API
# ==========================

client = genai.Client(
    api_key="AQ.Ab8RN6Ic9it1QZWD-ZapOWpbQH5l6M7-aGigSt6b_EbDPPSvVg"
)

# ==========================
# Profile
# ==========================

profile = {
    "name": "Denson",
    "role": "Python & FastAPI Developer",
    "about": "I love Python, FastAPI, HTML, CSS and building web applications."
}

# ==========================
# Blog Data
# ==========================

blogs = [
    {
        "id":1,
        "title":"Learning Python",
        "content":"Python is one of the easiest languages to learn."
    },
    {
        "id":2,
        "title":"FastAPI",
        "content":"FastAPI is a modern Python web framework."
    }
]

# ==========================
# Home
# ==========================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request":request,
            "profile":profile,
            "blogs":blogs,
            "answer":""
        }
    )

# ==========================
# Add Blog
# ==========================

@app.post("/add")
def add_blog(
    title:str=Form(...),
    content:str=Form(...)
):

    blogs.append({
        "id":len(blogs)+1,
        "title":title,
        "content":content
    })

    return RedirectResponse("/",303)

# ==========================
# Delete Blog
# ==========================

@app.get("/delete/{blog_id}")
def delete(blog_id:int):

    for blog in blogs:

        if blog["id"]==blog_id:
            blogs.remove(blog)
            break

    return RedirectResponse("/",303)

# ==========================
# Edit Blog
# ==========================

@app.post("/edit/{blog_id}")
def edit(
    blog_id:int,
    title:str=Form(...),
    content:str=Form(...)
):

    for blog in blogs:

        if blog["id"]==blog_id:

            blog["title"]=title
            blog["content"]=content

    return RedirectResponse("/",303)

# ==========================
# Search
# ==========================

@app.get("/search",response_class=HTMLResponse)
def search(
    request:Request,
    q:str=""
):

    result=[]

    for blog in blogs:

        if q.lower() in blog["title"].lower():

            result.append(blog)

    return templates.TemplateResponse(
        "index.html",
        {
            "request":request,
            "profile":profile,
            "blogs":result,
            "answer":""
        }
    )

# ==========================
# AI Assistant
# ==========================

@app.post("/ask", response_class=HTMLResponse)
def ask_ai(
    request: Request,
    question: str = Form(...)
):

    response = client.models.generate_content(

        model="gemini-flash-lite-latest",

        contents=question,

        config=types.GenerateContentConfig(

            system_instruction=f"""
You are Denson's AI assistant.

Here is Denson's profile:

{profile_data}

Instructions:

1. If the user asks about Denson, answer ONLY using the profile above.
2. If the profile does not contain the answer, reply:
   "I don't have that information about Denson."
3. If the user asks a general question (for example Python, FastAPI, history, science, programming, math, geography, etc.), answer normally using your own knowledge.
4. Never invent personal information about Denson.
5. Be friendly and professional.
"""

        )

    )

    return templates.TemplateResponse(

        "index.html",

        {
            "request": request,
            "profile": profile,
            "blogs": blogs,
            "question": question,
            "answer": response.text
        }

    )
