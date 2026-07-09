from fastapi import FastAPI

app = FastAPI()
students={
  1:
}
    

@app.get('/student/{id}')
def get_student_by_id(id:int):
    if id in students:
        return students[id]
    return

  