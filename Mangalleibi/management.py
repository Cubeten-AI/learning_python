students = {}

def grade(m):
    if m >= 90:
        return "A+"
    elif m >= 80:
        return "A"
    elif m >= 70:
        return "B"
    elif m >= 60:
        return "C"
    elif m >= 50:
        return "D"
    return "F"

def show(i):
    s = students[i]
    print(f"\nID: {i}")
    print("Name: ", s["Name"])
    print("Age:", s["Age"])
    print("Course:", s["Course"])
    print("Marks:", s["Marks"])
    print("Grade:", grade(s["Marks"]))

def save():
    f = open("management.txt", "w")
    for i in students:
        s = students[i]
        f.write(f"ID: {i}\n")
        f.write(f"Name: {s['Name']}\n")
        f.write(f"Age: {s['Age']}\n")
        f.write(f"Course: {s['Course']}\n")
        f.write(f"Marks: {s['Marks']}\n")
        f.write(f"Grade: {grade(s['Marks'])}\n")
        f.write("-" * 30 + "\n")
    f.close()

while True:
    print("\n===== Student Management =====")
    print("1.Add 2.Display 3.Search 4. Search student by Name  5.Update")
    print("6.Delete 7.Average 8.Topper 9.Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        i = input("ID: ")
        students[i] = {
            "Name": input("Name: "),
            "Age": input("Age: "),
            "Course": input("Course: "),
            "Marks": float(input("Marks: "))
        }
        save()
        print("Student Added!")

    elif ch == "2":
        if students:
            for i in students:
                show(i)
        else:
            print("No Records!")

    elif ch == "3":
        i = input("Enter ID: ")
        if i in students:
            show(i)
        else:
            print("Student Not Found!")
    elif ch == "4": 
        name = input("Enter Name: ").lower()
       
        for i in students:
            if students[i]["Name"].lower()==name:
                show(i)    
            else:
                    print("student not found")

    elif ch == "5":
        i = input("Enter ID: ")
        if i in students:
            students[i]["Name"] = input("New Name: ")
            students[i]["Age"] = input("New Age: ")
            students[i]["Course"] = input("New Course: ")
            students[i]["Marks"] = float(input("New Marks: "))
            save()
            print("Updated!")
        else:
            print("Student Not Found!")

    elif ch == "6":
        i = input("Enter ID: ")
        if i in students:
            del students[i]
            save()
            print("Deleted!")
        else:
            print("Student Not Found!")

    elif ch == "7":
        if students:
            avg = sum(s["Marks"] for s in students.values()) / len(students)
            print("Average Marks:", round(avg, 2))
        else:
            print("No Records!")

    elif ch == "8":
        if students:
            t = max(students[x]["Marks"] for x in students)
            print("\nTopper:")
            for i in students:
                if students[i]["Marks"] == t:
                    show(i)
        else:
            print("No Records!")

    elif ch == "9":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")