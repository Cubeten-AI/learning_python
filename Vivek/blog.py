from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

# Allow all origins (development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
# =====================================================
# BLOG DATA
# =====================================================

blogs = [
    {
        "id": 1,
        "title": "FastAPI Introduction",
        "content": "Learning CRUD operations using FastAPI",
        "author": "Vivek"
    }
]


# =====================================================
# HOME PAGE
# =====================================================

@app.get("/", response_class=HTMLResponse)
def home():

    html = """

    <!DOCTYPE html>
    <html>

    <head>

        <title>Blog Management System</title>

        <style>

            body{
                font-family:Arial;
                background:#f4f4f4;
                text-align:center;
            }

            h1{
                color:#333;
            }

            table{
                margin:auto;
                width:80%;
                border-collapse:collapse;
                background:white;
            }

            th,td{
                border:1px solid #ddd;
                padding:12px;
            }

            th{
                background:#0077b6;
                color:white;
            }

            .box{
                background:white;
                width:80%;
                margin:30px auto;
                padding:20px;
                border-radius:10px;
                box-shadow:0 0 10px gray;
            }

        </style>

    </head>


    <body>


    <h1>Blog Management System</h1>


    <div class="box">


    <h2>All Blogs</h2>


    <table>


    <tr>

        <th>ID</th>
        <th>Title</th>
        <th>Content</th>
        <th>Author</th>

    </tr>


    """


    for blog in blogs:

        html += f"""

        <tr>

            <td>{blog["id"]}</td>

            <td>{blog["title"]}</td>

            <td>{blog["content"]}</td>

            <td>{blog["author"]}</td>

        </tr>

        """


    html += """

    </table>


    </div>


    </body>

    </html>

    """


    return HTMLResponse(content=html)



# =====================================================
# READ ALL BLOGS
# =====================================================

@app.get("/blogs")
def show_all_blogs():

    return blogs



# =====================================================
# READ SINGLE BLOG
# =====================================================

@app.get("/blog/{blog_id}")
def view_blog(id:int):

    for blog in blogs:

        if blog["id"] == id:

            return blog


    return {
        "message":"Blog not found"
    }



# =====================================================
# CREATE BLOG
# =====================================================

@app.post("/add_blog")
def create_blog(title:str, content:str, author:str):

    blog = {

        "id": len(blogs) + 1,

        "title": title,

        "content": content,

        "author": author

    }


    blogs.append(blog)


    return {

        "message":"Blog created successfully",

        "data":blog

    }



# =====================================================
# UPDATE BLOG
# =====================================================

@app.put("/edit_blog")
def edit_blog(
    id:int,
    new_title:str,
    new_content:str,
    new_author:str
):

    for blog in blogs:

        if blog["id"] == id:


            blog["title"] = new_title

            blog["content"] = new_content

            blog["author"] = new_author


            return {

                "message":"Blog updated successfully",

                "data":blog

            }


    return {

        "message":"Blog not found"

    }



# =====================================================
# DELETE BLOG
# =====================================================

@app.delete("/delete_blog")
def delete_blog(id:int):

    for blog in blogs:

        if blog["id"] == id:


            blogs.remove(blog)


            return {

                "message":"Blog deleted successfully",

                "data":blogs

            }


    return {

        "message":"Blog not found"

    }