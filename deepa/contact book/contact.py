contacts = {}

def add_contact():
    name = input("Enter Name: ")
    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email
    }

    print("Contact Added Successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n----- Contact List -----")
    for name, details in contacts.items():
        print(f"Name : {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")
        print("------------------------")

def update_contact():
    name = input("Enter Contact Name to Update: ")

    if name in contacts:
        phone = input("Enter New Phone: ")
        email = input("Enter New Email: ")

        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email

        print("Contact Updated Successfully!")
    else:
        print("Contact Not Found.")

def delete_contact():
    name = input("Enter Contact Name to Delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found.")

def search_contact():
    name = input("Enter Name to Search: ")

    if name in contacts:
        print("\nContact Found")
        print("Name :", name)
        print("Phone:", contacts[name]["Phone"])
        print("Email:", contacts[name]["Email"])
    else:
        print("Contact Not Found.")

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice.")