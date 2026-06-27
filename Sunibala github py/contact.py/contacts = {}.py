contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
    print("Added")

def delete_contact():
    name = input("Name: ")
    if name in contacts:
        del contacts[name]
        print("Deleted")
    else:
        print("Not found")

def update_contact():
    name = input("Name: ")
    if name in contacts:
        phone = input("New phone: ")
        contacts[name] = phone
        print("Updated")
    else:
        print("Not found")

def view_contact():
    if not contacts:
        print("Empty")
    else:
        for name, phone in contacts.items():
            print(name, phone)

def search_contact():
    name = input("Name: ")
    if name in contacts:
        print(name, contacts[name])
    else:
        print("Not found")

while True:
    print("\n1.Add 2.Name 3.contacts 4.View 5.Search 6.Exit")
    choice = input("Choice: ")

    if choice == "1": add_contact()
    elif choice == "2": delete_contact()
    elif choice == "3": update_contact()
    elif choice == "4": view_contact()
    elif choice == "5": search_contact()
    elif choice == "6": break
    else: print("Wrong choice")