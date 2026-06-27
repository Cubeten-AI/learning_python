choice=input("Enter\n 1 for add contact,\n 2 for delete contact,\n 3 for update contact,\n 4 for view phonebook,\n 5 for search contact,\n or anything else to exit:\n")

while True:

    match choice:

        case "1":
            name = input("Enter the contact name: ")
            phone = input("Enter the contact phone number: ")
            phonebook = {
                "name": name,
                "phone": phone
            }
            print("Contact added successfully!")
        
        case "2":
            name = input("Enter the contact name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print("Contact deleted successfully!")
            else:
                print("Contact not found!")
        
        case "3":
            name = input("Enter the contact name to update: ")
            if name in phonebook:
                phone = input("Enter the new phone number: ")
                phonebook[name] = phone
                print("Contact updated successfully!")
            else:
                print("Contact not found!")

        case "4":
            if phonebook:
                print("Contacts:")
                for name, phone in phonebook.items():
                    print(f"name is: {name} phone is: {phone}")
                    print("name is: ", name, "phone is: ", phone)
            else:
                print("No contacts found!")

        case "5":
            name = input("Enter the contact name to search: ")
            if name in phonebook:
                print(f"Name: {name}, Phone: {phonebook[name]}")
            else:
                print("Contact not found!")
        
        case _:
            print("Exiting the contact book program!")
            break
            
    user_choice = input("Do you want to perform another operation? (yes/no): ")
    if user_choice != "yes":
        print("Exiting the contact book program!")
        break

    choice = input("Enter\n 1 for add contact,\n 2 for delete contact,\n 3 for update contact,\n 4 for view contact,\n 5 for search contact,\n or anything else to exit:\n")