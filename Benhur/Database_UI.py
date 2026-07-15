from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import psycopg2,os

load_dotenv()
DATABASE_URL=os.getenv("databaseURL")

connection=psycopg2.connect(DATABASE_URL)
cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todo(
id SERIAL PRIMARY KEY,
task TEXT NOT NULL,
type TEXT NOT NULL
)
""")
connection.commit()

app=FastAPI()

html="""

<!DOCTYPE html>
<html>
<head>
<title>Todo App</title>

<style>
body{
    font-family:Arial;
    margin:40px;
    background:#f5f5f5;
}

.container{
    display:flex;
    gap:50px;
}

.box{
    background:white;
    padding:20px;
    width:350px;
    border-radius:10px;
}

button{
    cursor:pointer;
    margin:3px;
}

li{
    margin:10px;
}

input{
    padding:8px;
}
</style>

</head>

<body>

<h1>📝Ben's To-do Manager</h1>

<input id="task" placeholder="Enter task">

<button onclick="addTodo()">➕ Add To-do</button>
<button onclick="addNotTodo()">🚫 Add Not To-do</button>


<div class="container">

<div class="box">
<h2>✅ To-do List:</h2>
<ul id="todo"></ul>
</div>


<div class="box">
<h2>❌ Not To-do List:</h2>
<ul id="not"></ul>
</div>

</div>


<h2>✏️ Edit To-do:</h2>

<input id="old" placeholder="Old task">
<input id="newTask" placeholder="New task">

<button onclick="edit()">🔄 Update</button>


<script>

async function load(){

let t = await fetch('/todo');
let n = await fetch('/not_todo');

let todos = await t.json();
let nots = await n.json();


todo.innerHTML="";
not.innerHTML="";


todos.forEach(x=>{
todo.innerHTML += 
`<li>${x}
<button onclick="delTodo('${x}')">🗑️</button>
</li>`;
});


nots.forEach(x=>{
not.innerHTML += 
`<li>${x}</li>`;
});

}



async function addTodo(){

await fetch('/todo?task='+task.value,
{method:'POST'});

task.value="";
load();

}



async function addNotTodo(){

await fetch('/not_todo?task='+task.value,
{method:'POST'});

task.value="";
load();

}



async function delTodo(x){

await fetch('/todo/'+x,
{method:'DELETE'});

load();

}



async function edit(){

await fetch(
`/edit?old=${old.value}&new=${newTask.value}`,
{method:'PUT'}
);

load();

}


load();

</script>

</body>
</html>

"""

@app.get("/",response_class=HTMLResponse)
def home():
    return html

@app.get("/todo")
def get_todo():
    cursor.execute("SELECT task FROM todo WHERE type='todo'")
    return[x[0]for x in cursor.fetchall()]

@app.get("/not_todo")
def get_not_todo():
    cursor.execute("SELECT task FROM todo WHERE type='not'")
    return[x[0]for x in cursor.fetchall()]

@app.post("/todo")
def add_todo(task:str):
    cursor.execute("INSERT INTO todo(task,type)VALUES(%s,%s)",("📌 "+task,"todo"))
    connection.commit()
    return{"message":"added"}

@app.post("/not_todo")
def add_not_todo(task:str):
    cursor.execute("INSERT INTO todo(task,type)VALUES(%s,%s)",("🚫 "+task,"not"))
    connection.commit()
    return{"message":"added"}

@app.delete("/todo/{task}")
def delete_todo(task:str):
    cursor.execute("DELETE FROM todo WHERE task=%s",(task,))
    connection.commit()
    return{"message":"deleted"}

@app.put("/edit")
def edit_todo(old:str,new:str):
    cursor.execute("UPDATE todo SET task=%s WHERE task=%s",(new,old))
    connection.commit()
    return{"message":"updated"}