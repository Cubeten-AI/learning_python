import os

contacts = {}

menu = (
    "1. Add Contact",
    "2. View Contact",
    "3. Search Contact",
    "4. Update Contact",
    "5. Delete Contact",
    "6. Exit"
)

categories = {"Friend", "Family", "Work"}


def add():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    category = input("Enter Category: ")

    if category not in categories:
        category = "Friend"

    contacts[name] = {"Phone": phone, "Category": category}
    print("Contact Added")


def view():
    if len(contacts) == 0:
        print("No Contacts")
    else:
        names = [name for name in contacts]     

        for name in names:                       
            for key, value in contacts[name].items():
                print(name, "-", key, ":", value)
            print()


def search(name):                              
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact Not Found")


def update(name):
    if name in contacts:
        phone = input("Enter New Phone: ")

        if phone.isdigit():                     
            contacts[name]["Phone"] = phone
            print("Updated")
        else:
            print("Invalid Phone")
    else:
        print("Contact Not Found")


def delete(name):
    if name in contacts:
        del contacts[name]
        print("Deleted")
    else:
        print("Contact Not Found")


while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("CONTACT BOOK")
    for item in menu:
        print(item)

    choice = input("Enter Choice: ")

    if choice == "1":
        add()

    elif choice == "2":
        view()

    elif choice == "3":
        name = input("Enter Name: ")
        search(name)

    elif choice == "4":
        name = input("Enter Name: ")
        update(name)

    elif choice == "5":
        name = input("Enter Name: ")
        delete(name)

    elif choice == "6":
        print("Exit")
        break

    else:
        print("Invalid Choice")

    input("Press Enter...")