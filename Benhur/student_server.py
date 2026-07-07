from fastapi import FastAPI

app = FastAPI()

def __init__(self, ID, Name, Age, Course, Marks):
        self.ID = ID
        self.Name = Name
        self.Age = Age
        self.Course = Course
        self.Marks = Marks


@app.post('/add_student')   
def add_student(self):
    student_data = {
        "ID": self.ID,
        "Name": self.Name,
        "Age": self.Age,
        "Course": self.Course,
        "Marks": self.Marks
    }
    self.student_list.append(student_data)
    print(f"Student {self.Name} added successfully!")


@app.get('/display_students')
def display_students(self):
    if self.student_list:
        print("Student List:\n")
        for student in self.student_list:
            print(f"ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Course: {student['Course']}, Marks: {student['Marks']}")
    else:
        print("No students found!")


@app.get('/search_student/{ID}')
def search_student(self, ID):
    for student in self.student_list:
        if student['ID'] == ID:
            print(f"Student found: ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Course: {student['Course']}, Marks: {student['Marks']}")
            return
    print("Student not found!")


@app.put('/update_student/{ID}')
def update_student(self, ID, Name=None, Age=None, Course=None, Marks=None):
    for student in self.student_list:
        if student['ID'] == ID:
            if Name:
                student['Name'] = Name
            if Age:
                student['Age'] = Age
            if Course:
                student['Course'] = Course
            if Marks:
                student['Marks'] = Marks
            print(f"Student {ID} updated successfully!")
            return
    print("Student not found!")


@app.delete('/delete_student/{ID}')
def delete_student(self, ID):
    for student in self.student_list:
        if student['ID'] == ID:
            self.student_list.remove(student)
            print(f"Student {ID} deleted successfully!")
            return
    print("Student not found!")

@app.get('/calculate_average_marks')
def calculate_average_marks(self):
    if self.student_list:
        total_marks = sum(student['Marks'] for student in self.student_list)
        average_marks = total_marks / len(self.student_list)
        print(f"Average Marks of all students: {average_marks}")
    else:
        print("No students found to calculate average marks!")

@app.get('/find_topper')
def find_topper(self):
    if self.student_list:
        topper = max(self.student_list, key=lambda student: student['Marks'])
        print(f"Topper: ID: {topper['ID']}, Name: {topper['Name']}, Age: {topper['Age']}, Course: {topper['Course']}, Marks: {topper['Marks']}")
    else:
        print("No students found to find the topper!")