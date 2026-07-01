contacts = {}
while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. View Contacts")
    print("5. Search Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")  
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact added successfully.")
    elif choice == "2":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            number = input("Enter new phone number: ")
            contacts[name] = number
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
    elif choice == "4":
        if contacts:
            print("\nContacts List:")
            for name, number in contacts.items():
                print(name, ":", number)
        else:
            print("No contacts available.")
    elif choice == "5":
        name = input("Enter name to search: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found.")
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")