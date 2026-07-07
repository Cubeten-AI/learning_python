from fastapi import FastAPI

app = FastAPI()

# Data
todos = ["eat food", "wash clothes"]
not_to_do_list = []


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