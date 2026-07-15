from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

app = FastAPI(title="To-Do App")

# ---------------- DATA ----------------

todos = ["eat food", "wash clothes"]
not_to_do_list = []

# ---------------- UI ----------------

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>FastAPI To-Do App</title>

<style>

body{
    font-family:Arial;
    background:#f2f2f2;
}

.container{
    width:600px;
    margin:50px auto;
    background:white;
    padding:30px;
    border-radius:10px;
    box-shadow:0 0 10px gray;
}

h2{
    text-align:center;
}

input{
    width:80%;
    padding:10px;
    font-size:18px;
}

button{
    padding:10px 20px;
    margin:8px;
    font-size:16px;
    cursor:pointer;
}

ul{
    list-style:none;
    padding:0;
}

li{
    background:#eeeeee;
    margin:8px 0;
    padding:12px;
    border-radius:5px;
    cursor:pointer;
}

li:hover{
    background:#d8d8d8;
}

.selected{
    background:#aee1ff;
}

</style>

</head>

<body>

<div class="container">

<h2>FastAPI To-Do App</h2>

<input type="text" id="task" placeholder="Enter task">

<br><br>

<button onclick="addTodo()">Add</button>
<button onclick="editTodo()">Edit</button>
<button onclick="deleteTodo()">Delete</button>

<hr>

<h3>Todo List</h3>

<ul id="todoList"></ul>

</div>

<script>

let selectedTask="";

async function loadTodos(){

    let response=await fetch("/todos");
    let data=await response.json();

    let list=document.getElementById("todoList");
    list.innerHTML="";

    data.todos.forEach(function(item){

        let li=document.createElement("li");
        li.innerText=item;

        li.onclick=function(){

            selectedTask=item;
            document.getElementById("task").value=item;

            let all=document.querySelectorAll("li");
            all.forEach(x=>x.classList.remove("selected"));

            li.classList.add("selected");
        };

        list.appendChild(li);

    });

}

async function addTodo(){

    let task=document.getElementById("task").value.trim();

    if(task==""){
        alert("Enter a task");
        return;
    }

    await fetch("/todo?task="+encodeURIComponent(task),{
        method:"POST"
    });

    document.getElementById("task").value="";
    selectedTask="";

    loadTodos();

}

async function editTodo(){

    if(selectedTask==""){
        alert("Select a task first");
        return;
    }

    let newTask=document.getElementById("task").value.trim();

    if(newTask==""){
        alert("Enter new task");
        return;
    }

    await fetch("/edit_todo?to_be_updated="+encodeURIComponent(selectedTask)+"&new_value="+encodeURIComponent(newTask),{
        method:"PUT"
    });

    document.getElementById("task").value="";
    selectedTask="";

    loadTodos();

}

async function deleteTodo(){

    if(selectedTask==""){
        alert("Select a task first");
        return;
    }

    await fetch("/delete_todo?mytask="+encodeURIComponent(selectedTask),{
        method:"DELETE"
    });

    document.getElementById("task").value="";
    selectedTask="";

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
    return {
        "count": len(todos),
        "todos": todos
    }


@app.get("/todo")
def hello():
    return {"message": "Nice"}


# ---------------- POST ----------------

@app.post("/todo")
def add_todo(task: str = Query(...)):

    if task in todos:
        return {"message": "Task already exists"}

    todos.append(task)

    return {
        "message": "Task added successfully",
        "todos": todos
    }


@app.post("/notodo")
def add_not_to_do(name_of_task: str = Query(...)):

    not_to_do_list.append(name_of_task)

    return {
        "not_to_do_list": not_to_do_list
    }


# ---------------- DELETE ----------------

@app.delete("/delete_todo")
def delete_a_todo(mytask: str = Query(...)):

    if mytask in todos:

        todos.remove(mytask)

        return {
            "message": "Task deleted successfully",
            "todos": todos
        }

    return {"message": "Task not found"}


# ---------------- PUT ----------------

@app.put("/edit_todo")
def edit_a_todo(
    to_be_updated: str = Query(...),
    new_value: str = Query(...)
):

    if to_be_updated in todos:

        index = todos.index(to_be_updated)

        todos[index] = new_value

        return {
            "message": "Task updated successfully",
            "todos": todos
        }

    return {"message": "Task not found"}