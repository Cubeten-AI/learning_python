students = {}

def grade(m):
    if m >= 90: return "A+"
    elif m >= 80: return "A"
    elif m >= 70: return "B"
    elif m >= 60: return "C"
    elif m >= 50: return "D"
    return "F"

def show(i):
    s = students[i]
    print(f"\nID: {i}")
    print("Name:", s["Name"])
    print("Age:", s["Age"])
    print("Course:", s["Course"])
    print("Marks:", s["Marks"])
    print("Grade:", grade(s["Marks"]))

while True:
    print("\n===== Student Management =====")
    print("1.Add 2.Display 3.Search 4.Update")
    print("5.Delete 6.Average 7.Topper 8.Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        i = input("ID: ")
        students[i] = {
            "Name": input("Name: "),
            "Age": input("Age: "),
            "Course": input("Course: "),
            "Marks": float(input("Marks: "))
        }
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
        i = input("Enter ID: ")
        if i in students:
            students[i]["Name"] = input("New Name: ")
            students[i]["Age"] = input("New Age: ")
            students[i]["Course"] = input("New Course: ")
            students[i]["Marks"] = float(input("New Marks: "))
            print("Updated!")
        else:
            print("Student Not Found!")

    elif ch == "5":
        i = input("Enter ID: ")
        if i in students:
            del students[i]
            print("Deleted!")
        else:
            print("Student Not Found!")

    elif ch == "6":
        if students:
            avg = sum(s["Marks"] for s in students.values()) / len(students)
            print("Average Marks:", round(avg, 2))
        else:
            print("No Records!")

    elif ch == "7":
        if students:
            t = max(students, key=lambda x: students[x]["Marks"])
            print("\nTopper:")
            show(t)
        else:
            print("No Records!")

    elif ch == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")