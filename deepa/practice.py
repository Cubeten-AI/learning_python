# # age=int(input("what is your age:"))
# # print("your age is ",(age))

# num=[1,2,3,99,67,56]
# idx=0
# while idx < len(num):
#     print(num[idx])
#     idx += 1


#menu driven program --student management
student=[]

def add_student():
    roll = int(input("enter rool number: "))
    name = str(input("enter your name: "))
    student.append({"roll": roll, "name": name})
    print("student added successfully!!")

def display_student():
    if not student:
        print("no student to display.")
        return
    print("\n---student list---")
    for s in student:
        print(f"roll: {s["rool"]}, name: {s["name"]}")

def search_student():
    roll = input("enter roll number to search: ")
    for s in student:
        if s["roll"]== roll:
            print(f"found: roll: {s["roll"]},name:{s["name"]}")
            return
        print("student not found")

def update_student():
    roll = input("enter roll no. to update: ")
    for s in student:
        if s["roll"] == roll:
            s["name"] == input("enter  new name: ")
            print("student updated!!")
            return
        print("student not found. ")

def delete_student():
    roll = input("enter roll no. to delete: ")
    for s in student:
        if s["roll"] == roll:
            student.remove(s)
            print("student deleted!!")
            return
        print("student not found. ")

def menu():
    while True:
    print("1.add student.")
    print("2.display student.")
    print("3.search student. ")
    print("4.update student. ")
    print("5.delete student. ")
    print("6.exit")

    choice = input("enter your choice: ")

    if choice =='1': add_student()
    elif choice =='2': display_student()
    elif choice =='3': search_student()
    elif choice =='4': update_student()
    elif choice =='5': delete_student()
    elif choice =='6':
        print("exiting...")
        break
    else:

        print("invalid choice ..try again. ")
menu()
