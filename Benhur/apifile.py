from fastapi import FastAPI

app = FastAPI()

students = {
    1: {"name": "Benhur Heikrujam", "semester":"4"},
    1: {"name": "Denson Saikhom", "semester":"6"},
    1: {"name": "Abujam Vivek Luwang", "semester":"6"},
    1: {"name": "Vedic Soibam", "semester":"6"},
    1: {"name": "Vedant Soibam", "semester":"6"},
    1: {"name": "Angom Sunibala", "semester":"6"},
    1: {"name": "Deepa Moirangthem", "semester":"6"},
    1: {"name": "Jeshmita Yaikhom", "semester":"6"}
    }

@app.get('/students')
def root():
    return {"Student list is:": students}

@app.get('/students/{id}')
def get_student_by_id(id:int):
    
    if id in students:
        return students[id]

    return {"message":"student not found"}