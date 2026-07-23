f = open("Student.txt", "a")

name = input("Enter Name: ")
roll = input("Enter Roll No: ")
course = input("Enter Course: ")


f.write(f"Name: {name}\n")
f.write(f"Roll: {roll}\n")
f.write(f"Course: {course}\n")

f.close()
print("Data added  Successfully")