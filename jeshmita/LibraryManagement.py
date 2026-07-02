class Books:
    def __init__(self, name, subject, author):
        self.name = name
        self.subject = subject
        self.author = author

    def edit_name(self, new_name):
        print(f"Previous name was: {self.name}")
        self.name = new_name
        print(f"New name is: {self.name}")

    def edit_author_and_subject(self, new_author, new_subject):
        self.author = new_author
        self.subject = new_subject

    def show_info(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Subject: {self.subject}")
        print("----------------------")


# Library list
library_books = []

# Sample books
OOP_using_Python = Books("OOP using Python", "CS", "John")
C_plus_plus = Books("C++", "CS", "Tom")


# Add book
def add_book_to_library(book):
    library_books.append(book)
    print("Book added successfully.")


# Remove book
def remove_a_book(book_name):
    for book in library_books:
        if book.name.lower() == book_name.lower():
            library_books.remove(book)
            print("Book removed successfully.")
            return
    print("Book not found.")


# Search book
def search_a_book(book_name):
    for book in library_books:
        if book.name.lower() == book_name.lower():
            print("Book found:")
            book.show_info()
            return
    print("Book not found.")


# Display all books
def display_books():
    if not library_books:
        print("Library is empty.")
    else:
        for book in library_books:
            book.show_info()


# Update book
def update_book(book_name):
    for book in library_books:
        if book.name.lower() == book_name.lower():
            new_author = input("Enter new author: ")
            new_subject = input("Enter new subject: ")
            book.edit_author_and_subject(new_author, new_subject)
            print("Book updated successfully.")
            return
    print("Book not found.")


# Add sample books
add_book_to_library(OOP_using_Python)
add_book_to_library(C_plus_plus)


# Menu
while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Update Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        subject = input("Enter subject: ")
        author = input("Enter author: ")
        new_book = Books(name, subject, author)
        add_book_to_library(new_book)

    elif choice == "2":
        name = input("Enter book name to remove: ")
        remove_a_book(name)

    elif choice == "3":
        name = input("Enter book name to search: ")
        search_a_book(name)

    elif choice == "4":
        display_books()

    elif choice == "5":
        name = input("Enter book name to update: ")
        update_book(name)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")