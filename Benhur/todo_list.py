from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

todo = ["Eat food", "Wash clothes"]
not_todo = ["Waste time"]


html = """
<!DOCTYPE html>
<html>
<head>

<title>Ben's To-do Manager</title>

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

<h1>📝 Ben's To-do Manager</h1>


<input id="task" placeholder="Enter task">

<button onclick="addTodo()">➕ Add To-do</button>
<button onclick="addNotTodo()">🚫 Add Not To-do</button>



<div class="container">


<div class="box">

<h2>✅ To-do List</h2>

<ul id="todo"></ul>

</div>



<div class="box">

<h2>❌ Not To-do List</h2>

<ul id="not"></ul>

</div>


</div>



<h2>✏️ Edit To-do</h2>


<input id="old" placeholder="Old task">

<input id="newTask" placeholder="New task">


<button onclick="edit()">🔄 Update</button>



<script>


async function load(){

    let t = await fetch("/todo");
    let n = await fetch("/not_todo");

    let todos = await t.json();
    let nots = await n.json();


    document.getElementById("todo").innerHTML="";
    document.getElementById("not").innerHTML="";


    todos.forEach(x=>{

        todo.innerHTML +=
        `<li>
        ${x}
        <button onclick="deleteTodo('${encodeURIComponent(x)}')">
        🗑️
        </button>
        </li>`;

    });



    nots.forEach(x=>{

        not.innerHTML +=
        `<li>
        ${x}
        <button onclick="deleteNotTodo('${encodeURIComponent(x)}')">
        🗑️
        </button>
        </li>`;

    });


}



async function addTodo(){

    await fetch(
    "/todo?task="+encodeURIComponent(task.value),
    {method:"POST"}
    );

    task.value="";

    load();

}




async function addNotTodo(){

    await fetch(
    "/not_todo?task="+encodeURIComponent(task.value),
    {method:"POST"}
    );

    task.value="";

    load();

}





async function deleteTodo(x){

    await fetch(
    "/todo/"+x,
    {method:"DELETE"}
    );

    load();

}





async function deleteNotTodo(x){

    await fetch(
    "/not_todo/"+x,
    {method:"DELETE"}
    );

    load();

}





async function edit(){

    let oldTask =
    document.getElementById("old").value;


    let newTask =
    document.getElementById("newTask").value;



    let response = await fetch(

    `/edit?old=${encodeURIComponent(oldTask)}&new=${encodeURIComponent(newTask)}`,

    {
        method:"PUT"
    }

    );


    console.log(await response.json());


    old.value="";
    newTask.value="";


    load();

}



load();


</script>


</body>
</html>
"""



@app.get("/", response_class=HTMLResponse)
def home():
    return html



@app.get("/todo")
def get_todo():
    return todo



@app.get("/not_todo")
def get_not_todo():
    return not_todo




@app.post("/todo")
def add_todo(task:str):

    todo.append(task)

    return {
        "message":"added"
    }




@app.post("/not_todo")
def add_not_todo(task:str):

    not_todo.append(task)

    return {
        "message":"added"
    }




@app.delete("/todo/{task}")
def delete_todo(task:str):

    task = task.lower().strip()


    for item in todo:

        if item.lower() == task:

            todo.remove(item)

            return {
                "message":"deleted"
            }


    return {
        "message":"not found"
    }





@app.delete("/not_todo/{task}")
def delete_not_todo(task:str):

    task = task.lower().strip()


    for item in not_todo:

        if item.lower() == task:

            not_todo.remove(item)

            return {
                "message":"deleted"
            }


    return {
        "message":"not found"
    }





@app.put("/edit")
def edit_todo(old:str,new:str):

    old = old.lower().strip()


    for i,item in enumerate(todo):

        if item.lower() == old:

            todo[i] = new

            return {
                "message":"updated",
                "todo":todo
            }


    return {
        "message":"not found",
        "todo":todo
    }