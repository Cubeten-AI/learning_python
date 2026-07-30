class Student:
    def __init__(self):
        self.students = {}

    def grade(self, m):
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

    def show(self, i):
        s = self.students[i]
        print("\nID:", i)
        print("Name:", s["Name"])
        print("Age:", s["Age"])
        print("Course:", s["Course"])
        print("Marks:", s["Marks"])
        print("Grade:", self.grade(s["Marks"]))

    def add(self):
        i = input("ID: ")
        self.students[i] = {
            "Name": input("Name: "),
            "Age": input("Age: "),
            "Course": input("Course: "),
            "Marks": float(input("Marks: "))
        }
        print("Student Added!")

    def display(self):
        if self.students:
            for i in self.students:
                self.show(i)
        else:
            print("No Records!")

    def search(self):
        i = input("Enter ID: ")
        if i in self.students:
            self.show(i)
        else:
            print("Student Not Found!")

    def update(self):
        i = input("Enter ID: ")
        if i in self.students:
            self.students[i]["Name"] = input("New Name: ")
            self.students[i]["Age"] = input("New Age: ")
            self.students[i]["Course"] = input("New Course: ")
            self.students[i]["Marks"] = float(input("New Marks: "))
            print("Updated!")
        else:
            print("Student Not Found!")

    def delete(self):
        i = input("Enter ID: ")
        if i in self.students:
            del self.students[i]
            print("Deleted!")
        else:
            print("Student Not Found!")

    def average(self):
        if self.students:
            avg = sum(s["Marks"] for s in self.students.values()) / len(self.students)
            print("Average Marks:", round(avg, 2))
        else:
            print("No Records!")

    def topper(self):
        if self.students:
            t = max(self.students[x]["Marks"] for x in self.students)
            print("\nTopper:")
            for i in self.students:
             if self.students[i]["Marks"] == t:
                              
              self.show(t)
        else:
            print("No Records!")



obj = Student()

while True:
    print("\n===== Student Management =====")
    print("1.Add 2.Display 3.Search 4.Update")
    print("5.Delete 6.Average 7.Topper 8.Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        obj.add()
    elif ch == "2":
        obj.display()
    elif ch == "3":
        obj.search()
    elif ch == "4":
        obj.update()
    elif ch == "5":
        obj.delete()
    elif ch == "6":
        obj.average()
    elif ch == "7":
        obj.topper()
    elif ch == "8":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")