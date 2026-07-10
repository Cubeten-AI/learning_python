from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()



todos = ["Eat Food", "Wash Clothes"]
not_to_do_list = []



@app.get("/", response_class=HTMLResponse)
def home():

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Daily To-Do Management</title>

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
                width:60%;
                border-collapse:collapse;
                background:white;
            }

            th,td{
                border:1px solid #ddd;
                padding:12px;
            }

            th{
                background:#4CAF50;
                color:white;
            }

        </style>

    </head>

    <body>

        <h1>Daily To-Do Management</h1>

        <table>

            <tr>
                <th>Task No.</th>
                <th>Task</th>
            </tr>
    """

    for i, task in enumerate(todos, start=1):
        html += f"""
        <tr>
            <td>{i}</td>
            <td>{task}</td>
        </tr>
        """

    html += """
        </table>

        <br>

        <h2>Not-To-Do List</h2>

        <table>

            <tr>
                <th>No.</th>
                <th>Task</th>
            </tr>
    """

    for i, task in enumerate(not_to_do_list, start=1):
        html += f"""
        <tr>
            <td>{i}</td>
            <td>{task}</td>
        </tr>
        """

    html += """
        </table>

    </body>
    </html>
    """

    return HTMLResponse(content=html)




@app.get("/todos")
def show_all_todos():
    return todos


@app.get("/todo")
def todo():
    return {"message": "Nice"}


@app.post("/todo")
def add_todo(task: str):
    todos.append(task)

    return {
        "message": f"{task} added successfully",
        "data": todos
    }


@app.post("/notodo")
def add_notodo(name_of_task: str):
    not_to_do_list.append(name_of_task)

    return {
        "message": f"{name_of_task} added successfully",
        "data": not_to_do_list
    }


@app.delete("/delete_todo")
def delete_todo(mytask: str):

    if mytask in todos:
        todos.remove(mytask)

        return {
            "message": "Task deleted successfully",
            "data": todos
        }

    return {"message": "Task not found"}


@app.put("/edit_todo")
def edit_todo(to_be_updated: str, new_value: str):

    if to_be_updated in todos:

        index = todos.index(to_be_updated)
        todos[index] = new_value

        return {
            "message": "Task updated successfully",
            "data": todos
        }

    return {"message": "Task not found"}