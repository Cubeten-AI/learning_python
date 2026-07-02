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


# Add book (a)
def add_book_to_library(book):
    library_books.append(book)

    with open("file.txt", "a") as library_book_store:
        library_book_store.write(f"{book.name},{book.subject},{book.author}\n")
         print("added book to book store")
    print("Book added successfully.")


# Remove book (w)
def remove_a_book(book_name):
    for book in library_books:
        if book.name.lower() == book_name.lower():
            library_books.remove(book)

            with open("file.txt", "w") as file:
                for b in library_books:
                    file.write(f"{b.name},{b.subject},{b.author}\n") 
            print("Book removed successfully.")
            return
    print("Book not found.")


# Search book (r)
def search_a_book(book_name):
    with open("file.txt", "r") as file:
        for line in file:
            name, subject, author = line.strip().split(",")

            if name.lower() == book_name.lower():
                print("Book found:")
                print("Book Name:", name)
                print("Subject:", subject)
                print("Author:", author)
                return        
    print("Book not found.")
 

# Display books (r)
def display_books():
    try:
        with open("file.txt", "r") as file:
            print("\n===== BOOKS =====")
            print(file.read())
    except FileNotFoundError:
        print("Library is empty.")


# Update book (w)
def update_book(book_name):
    for book in library_books:
        if book.name.lower() == book_name.lower():
            new_author = input("Enter new author: ")
            new_subject = input("Enter new subject: ")
            book.edit_author_and_subject(new_author, new_subject)

            with open("file.txt", "w") as file:
                for b in library_books:
                    file.write(f"{b.name},{b.subject},{b.author}\n")
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