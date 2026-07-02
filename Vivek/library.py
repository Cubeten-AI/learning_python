FILE_NAME = "file.txt"


class Book:
    def __init__(self, name, subject, author):
        self.name = name
        self.subject = subject
        self.author = author

    def show_info(self):
        print(f"Book Name : {self.name}")
        print(f"Subject   : {self.subject}")
        print(f"Author    : {self.author}")
        print("-" * 30)


def add_book():
    name = input("Enter book name: ")
    subject = input("Enter subject: ")
    author = input("Enter author: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{subject},{author}\n")

    print("Book added successfully.")


def display_books():
    with open(FILE_NAME, "r") as file:
        books = file.readlines()

    if len(books) == 0:
        print("No books found.")
        return

    print("\n----- Library Books -----")
    for line in books:
        name, subject, author = line.strip().split(",")
        book = Book(name, subject, author)
        book.show_info()


def search_book():
    name = input("Enter book name to search: ")

    with open(FILE_NAME, "r") as file:
        for line in file:
            book_name, subject, author = line.strip().split(",")

            if book_name.lower() == name.lower():
                print("\nBook Found")
                book = Book(book_name, subject, author)
                book.show_info()
                return

    print("Book not found.")


def remove_book():
    name = input("Enter book name to remove: ")

    with open(FILE_NAME, "r") as file:
        books = file.readlines()

    found = False

    with open(FILE_NAME, "w") as file:
        for line in books:
            book_name, subject, author = line.strip().split(",")

            if book_name.lower() != name.lower():
                file.write(line)
            else:
                found = True

    if found:
        print("Book removed successfully.")
    else:
        print("Book not found.")


def edit_book():
    name = input("Enter book name to edit: ")

    with open(FILE_NAME, "r") as file:
        books = file.readlines()

    found = False

    with open(FILE_NAME, "w") as file:
        for line in books:
            book_name, subject, author = line.strip().split(",")

            if book_name.lower() == name.lower():
                found = True

                print("\n1. Edit Book Name")
                print("2. Edit Subject")
                print("3. Edit Author")

                choice = input("Enter your choice: ")

                if choice == "1":
                    book_name = input("Enter new book name: ")

                elif choice == "2":
                    subject = input("Enter new subject: ")

                elif choice == "3":
                    author = input("Enter new author: ")

                else:
                    print("Invalid choice.")

            file.write(f"{book_name},{subject},{author}\n")

    if found:
        print("Book updated successfully.")
    else:
        print("Book not found.")


while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Edit Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        remove_book()

    elif choice == "5":
        edit_book()

    elif choice == "6":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")