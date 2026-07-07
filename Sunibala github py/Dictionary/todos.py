from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Data
todos = ["eat food", "wash clothes"]
not_to_do_list = []


# ---------------- UI ----------------

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>To Do App</title>

<style>
body{
font-family:Arial;
background:#f4f4f4;
margin:0;
padding:20px;
}

.container{
width:700px;
margin:auto;
background:white;
padding:20px;
border-radius:10px;
box-shadow:0 0 10px gray;
}

h1{
text-align:center;
color:#003366;
}

input{
width:70%;
padding:10px;
margin:5px;
}

button{
padding:10px 20px;
margin:5px;
border:none;
border-radius:5px;
cursor:pointer;
color:white;
}

.add{background:green;}
.update{background:orange;}
.delete{background:red;}
.refresh{background:#0066cc;}

li{
padding:8px;
font-size:18px;
}
</style>

</head>

<body>

<div class="container">

<h1>To Do List</h1>

<input id="task" placeholder="Enter Task">
<button class="add" onclick="addTask()">Add</button>
<button class="refresh" onclick="loadTodos()">Refresh</button>

<hr>

<h2>Tasks</h2>

<ul id="todoList"></ul>

<hr>

<h2>Edit Task</h2>

<input id="oldtask" placeholder="Old Task">

<input id="newtask" placeholder="New Task">

<button class="update" onclick="updateTask()">Update</button>

<hr>

<h2>Delete Task</h2>

<input id="deleteTaskName" placeholder="Task Name">

<button class="delete" onclick="deleteTask()">Delete</button>

</div>

<script>

async function loadTodos(){

let response=await fetch("/todos");
let data=await response.json();

let list=document.getElementById("todoList");

list.innerHTML="";

data.forEach(task=>{
list.innerHTML+=`<li>${task}</li>`;
});

}

async function addTask(){

let task=document.getElementById("task").value;

await fetch("/todo?task="+encodeURIComponent(task),{
method:"POST"
});

document.getElementById("task").value="";

loadTodos();

}

async function updateTask(){

let oldtask=document.getElementById("oldtask").value;
let newtask=document.getElementById("newtask").value;

await fetch("/edit_todo?to_be_updated="+encodeURIComponent(oldtask)+"&new_value="+encodeURIComponent(newtask),{
method:"PUT"
});

document.getElementById("oldtask").value="";
document.getElementById("newtask").value="";

loadTodos();

}

async function deleteTask(){

let task=document.getElementById("deleteTaskName").value;

await fetch("/delete_todo?mytask="+encodeURIComponent(task),{
method:"DELETE"
});

document.getElementById("deleteTaskName").value="";

loadTodos();

}

loadTodos();

</script>

</body>
</html>
"""


# ---------------- GET ----------------

@app.get("/todos")
def show_all_todos():
    return todos


@app.get("/todo")
def hello():
    return {"message": "nice"}


# ---------------- POST ----------------

@app.post("/todo")
def add_todo(task: str):
    message = f"You want to add '{task}' to your to-do list"
    todos.append(task)
    return {
        "data": todos,
        "message": message
    }


@app.post("/notodo")
def not_to_do(name_of_task: str):
    not_to_do_list.append(name_of_task)
    return not_to_do_list


# ---------------- DELETE ----------------

@app.delete("/delete_todo")
def delete_a_todo(mytask: str):
    if mytask in todos:
        todos.remove(mytask)
        return {"message": "success"}

    return {"message": "task not found"}


# ---------------- PUT ----------------

@app.put("/edit_todo")
def edit_a_todo(to_be_updated: str, new_value: str):

    if to_be_updated in todos:
        index = todos.index(to_be_updated)
        todos[index] = new_value

        return {
            "message": "Task updated successfully",
            "data": todos
        }

    return {"message": "Task not found"}