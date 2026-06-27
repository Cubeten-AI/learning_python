s={}

def grade(m):
    if m>=80:return "A"
    elif m>=60:return "B"
    elif m>=40:return "C"
    else:return "F"

def add():
    id=input("Enter ID: ")
    if id in s:print("ID already exists");return
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    course=input("Enter Course: ")
    marks=int(input("Enter Marks: "))
    s[id]=[name,age,course,marks]
    print("Student Added")

def display():
    if not s:print("No students");return
    for id,d in s.items():
        print(f"ID: {id}\nName: {d[0]}\nAge: {d[1]}\nCourse: {d[2]}\nMarks: {d[3]}\nGrade: {grade(d[3])}\n")

def search():
    print("Search by\n1.ID\n2.Name")
    ch=input("Choice: ")
    found=0
    if ch=="1":
        id=input("Enter ID: ")
        if id in s:
            d=s[id]
            print(f"ID: {id}\nName: {d[0]}\nAge: {d[1]}\nCourse: {d[2]}\nMarks: {d[3]}\nGrade: {grade(d[3])}")
            found=1
    elif ch=="2":
        name=input("Enter Name: ")
        for id,d in s.items():
            if d[0].lower()==name.lower():
                print(f"ID: {id}\nName: {d[0]}\nAge: {d[1]}\nCourse: {d[2]}\nMarks: {d[3]}\nGrade: {grade(d[3])}\n")
                found=1
    if not found:print("Not found")

def update():
    id=input("Enter ID: ")
    if id in s:
        s[id][3]=int(input("Enter New Marks: "))
        print("Updated")
    else:print("Not found")

def delete():
    id=input("Enter ID: ")
    if id in s:del s[id];print("Deleted")
    else:print("Not found")

def average():
    if s:print("Average Marks:",round(sum(d[3] for d in s.values())/len(s),2))
    else:print("No students")

def topper():
    if s:
        t=max(s.items(),key=lambda x:x[1][3])
        print(f"Topper: {t[1][0]} ID:{t[0]} Marks:{t[1][3]} Grade:{grade(t[1][3])}")
    else:print("No students")

def save():
    f=open("students.txt","w")
    for id,d in s.items():f.write(f"{id},{d[0]},{d[1]},{d[2]},{d[3]}\n")
    f.close()
    print("Saved to students.txt")

while True:
    print("\n========== Student Management =========")
    print("1. Add Student")
    print("2. Display Students") 
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average")
    print("7. Find Topper")
    print("8. Save")
    print("9. Exit")
    
    ch=input("Enter choice: ")
    if ch=="1":add()
    elif ch=="2":display()
    elif ch=="3":search()
    elif ch=="4":update()
    elif ch=="5":delete()
    elif ch=="6":average()
    elif ch=="7":topper()
    elif ch=="8":save()
    elif ch=="9":print("Exiting...");break
    else:print("Invalid choice")