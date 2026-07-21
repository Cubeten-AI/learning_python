from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

@app.get("/",response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Ben's Portfolio</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}
body{background:#f4f7fb;color:#333}
header{background:#2563eb;color:#fff;text-align:center;padding:50px}
nav{display:flex;justify-content:center;gap:30px;background:#fff;padding:15px;box-shadow:0 2px 10px rgba(0,0,0,.1)}
nav a{text-decoration:none;color:#2563eb;font-weight:bold}
section{max-width:900px;margin:30px auto}
.card{background:#fff;padding:25px;border-radius:12px;box-shadow:0 2px 10px rgba(0,0,0,.15);margin-bottom:25px}
.skills{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:15px}
.skill{background:#2563eb;color:#fff;padding:15px;border-radius:10px;text-align:center}
.icons{text-align:center;font-size:30px;margin-top:15px}
.icons a{color:#2563eb;margin:0 10px}
.btn{display:inline-block;margin-top:15px;background:#2563eb;color:#fff;text-decoration:none;padding:12px 20px;border-radius:8px}
footer{text-align:center;background:#2563eb;color:#fff;padding:20px}
</style>
</head>

<body>

<header>
<h1>👨‍💻 Benhur Heikrujam</h1>
<p>Python | FastAPI | Web Developer</p>
</header>

<nav>
<a href="#about">About</a>
<a href="#skills">Skills</a>
<a href="#vlog">Vlog</a>
<a href="#contact">Contact</a>
</nav>

<section id="about">
<div class="card">
<h2><i class="fa-solid fa-user"></i> About Me</h2>
<p>Hello! I'm Ben. I enjoy building websites and APIs using Python, FastAPI, HTML, CSS and JavaScript. I love learning new technologies and creating useful software.</p>
</div>

<div class="card" id="skills">
<h2><i class="fa-solid fa-code"></i> Skills</h2>
<div class="skills">
<div class="skill"><i class="fa-brands fa-python"></i><br>Python</div>
<div class="skill"><i class="fa-solid fa-server"></i><br>FastAPI</div>
<div class="skill"><i class="fa-brands fa-html5"></i><br>HTML</div>
<div class="skill"><i class="fa-brands fa-css3-alt"></i><br>CSS</div>
<div class="skill"><i class="fa-brands fa-js"></i><br>JavaScript</div>
<div class="skill"><i class="fa-solid fa-database"></i><br>SQL</div>
</div>
</div>

<div class="card" id="vlog">
<h2><i class="fa-solid fa-book-open"></i> Latest Vlog</h2>
<p>Read my latest coding journey, projects and experiences.</p>
<a class="btn" href="/vlog"><i class="fa-solid fa-book"></i> Read My Vlog</a>
</div>

<div class="card" id="contact">
<h2><i class="fa-solid fa-address-card"></i> Contact</h2>
<div class="icons">
<a href="https://github.com/Benhur-Heikrujam"><i class="fa-brands fa-github"></i></a>
<a href="https://in.linkedin.com/in/benhur-heikrujam-973449295"><i class="fa-brands fa-linkedin"></i></a>
<a href="mailto:heikrujambenhur@gmail.com?subject=Portfolio Inquiry"><i class="fa-solid fa-envelope"></i></a>
</div>
</div>

</section>

<footer>
© 2026 Benhur Heikrujam. All rights reserved.
</footer>

</body>
</html>
"""

@app.get("/vlog",response_class=HTMLResponse)
def vlog():
    return """
<!DOCTYPE html>
<html>
<head>
<title>My Vlog</title>
<style>
body{font-family:Arial;background:#f4f7fb;padding:40px;max-width:800px;margin:auto}
.card{background:white;padding:30px;border-radius:12px;box-shadow:0 2px 10px rgba(0,0,0,.15)}
a{text-decoration:none;color:#2563eb}
</style>
</head>
<body>

<div class="card">

<h1>📝 My First Vlog</h1>

<p><b>Date:</b> July 2026</p>

<p>
Today I continued learning FastAPI and built a portfolio website.
I also created a To-do List web application with features such as
adding, editing, deleting and displaying tasks through a web interface.
Building projects like these helps me become more confident in backend
development and web programming.
</p>

<br>

<a href="/">⬅ Back to Portfolio</a>

</div>

</body>
</html>
"""