from fastapi import FastAPI, HTTPException

app = FastAPI(title="To-Do API")

# ---------------- DATA ----------------

todos = [
    "eat food",
    "wash clothes"
]

not_to_do_list = []


# ---------------- HOME ----------------

@app.get("/")
def home():
    return {"message": "Welcome to To-Do API"}


# ---------------- GET ----------------

@app.get("/todos")
def get_all_todos():
    return {
        "count": len(todos),
        "todos": todos
    }


@app.get("/todo/{task}")
def get_single_todo(task: str):
    if task in todos:
        return {"task": task}
    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/notodos")
def get_not_to_do():
    return {
        "count": len(not_to_do_list),
        "not_to_do": not_to_do_list
    }


# ---------------- POST ----------------

@app.post("/todo")
def add_todo(task: str):
    if task in todos:
        raise HTTPException(status_code=400, detail="Task already exists")

    todos.append(task)

    return {
        "message": "Task added successfully",
        "todos": todos
    }


@app.post("/notodo")
def add_not_todo(task: str):
    if task in not_to_do_list:
        raise HTTPException(status_code=400, detail="Task already exists")

    not_to_do_list.append(task)

    return {
        "message": "Task added to Not-To-Do list",
        "not_to_do": not_to_do_list
    }


# ---------------- PUT ----------------

@app.put("/todo")
def edit_todo(old_task: str, new_task: str):
    if old_task not in todos:
        raise HTTPException(status_code=404, detail="Task not found")

    index = todos.index(old_task)
    todos[index] = new_task

    return {
        "message": "Task updated successfully",
        "todos": todos
    }


# ---------------- DELETE ----------------

@app.delete("/todo")
def delete_todo(task: str):
    if task not in todos:
        raise HTTPException(status_code=404, detail="Task not found")

    todos.remove(task)

    return {
        "message": "Task deleted successfully",
        "todos": todos
    }


@app.delete("/notodo")
def delete_not_todo(task: str):
    if task not in not_to_do_list:
        raise HTTPException(status_code=404, detail="Task not found")

    not_to_do_list.remove(task)

    return {
        "message": "Task deleted successfully",
        "not_to_do": not_to_do_list
    }