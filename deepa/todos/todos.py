from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory data
todos = ["eat food", "wash clothes"]
not_to_do_list = []


# ----------------------------
# Pydantic Models
# ----------------------------

class TodoItem(BaseModel):
    task: str


class UpdateTodo(BaseModel):
    old_task: str
    new_task: str


# ----------------------------
# GET Routes
# ----------------------------

@app.get("/")
def home():
    return {"message": "Welcome to Todo API"}


@app.get("/todos")
def get_todos():
    return {"todos": todos}


@app.get("/notodos")
def get_notodos():
    return {"not_to_do": not_to_do_list}


# ----------------------------
# POST Routes
# ----------------------------

@app.post("/todos")
def add_todo(item: TodoItem):
    todos.append(item.task)
    return {
        "message": f"'{item.task}' added successfully.",
        "todos": todos
    }


@app.post("/notodos")
def add_notodo(item: TodoItem):
    not_to_do_list.append(item.task)
    return {
        "message": f"'{item.task}' added to not-to-do list.",
        "not_to_do": not_to_do_list
    }


# ----------------------------
# PUT Route
# ----------------------------

@app.put("/todos")
def update_todo(item: UpdateTodo):
    if item.old_task not in todos:
        raise HTTPException(status_code=404, detail="Task not found")

    index = todos.index(item.old_task)
    todos[index] = item.new_task

    return {
        "message": "Task updated successfully.",
        "todos": todos
    }


# ----------------------------
# DELETE Route
# ----------------------------

@app.delete("/todos/{task}")
def delete_todo(task: str):
    if task not in todos:
        raise HTTPException(status_code=404, detail="Task not found")

    todos.remove(task)

    return {
        "message": "Task deleted successfully.",
        "todos": todos
    }