class Book:

    def __init__(self, name, subject, author):
        self.name = name
        self.subject = subject
        self.author = author

    def show_info(self):
        print(f"This book {self.name} is written by {self.author} under the subject of {self.subject}")

    def edit_name(self, new_name):
        print(f"previous name was {self.name}")
        self.name = new_name
        print(f"the new name is {self.name}")

    def edit_author_and_subject(self, new_author_name, new_subject_name):
        self.author = new_author_name
        self.subject = new_subject_name


library_books = []


# OOP_using_Java = Book("OOP using JAVA", "CS", "john")

C_plus_plus = Book("c plus plus", "CS", "tom")

# OOP_using_Java.show_info()

# C_plus_plus.show_info()

# C_plus_plus.edit_author_and_subject("Mary", "Maths")

# C_plus_plus.show_info()


def add_book_to_library(book_name):
    library_books.append(book_name)
    print("the book was added")


add_book_to_library(C_plus_plus)


def remove_a_book(book_name):
    for book in library_books:
        if book.name == book_name:
            library_books.remove(book)
            print("book deleted")
            return
    print("book not found")


def search(book_name):
    for book in library_books:
        if book.name == book_name:
            book.show_info()
            return
    print("book not found")


def display():
    if len(library_books) == 0:
        print("library is empty")
    else:
        for book in library_books:
            book.show_info()


def update(book_name):
    for book in library_books:
        if book.name == book_name:

            print("1. Edit Book Name")
            print("2. Edit Author and Subject")

            choice = input("Enter choice: ")

            if choice == "1":
                new_name = input("Enter new book name: ")
                book.edit_name(new_name)

            elif choice == "2":
                new_author = input("Enter new author: ")
                new_subject = input("Enter new subject: ")
                book.edit_author_and_subject(new_author, new_subject)

            else:
                print("Invalid choice")
            return

    print("book not found")


while True:

    print("\nLibrary Menu")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        subject = input("Enter subject: ")
        author = input("Enter author: ")

        new_book = Book(name, subject, author)
        add_book_to_library(new_book)

    elif choice == "2":
        display()

    elif choice == "3":
        name = input("Enter book name to search: ")
        search(name)

    elif choice == "4":
        name = input("Enter book name to update: ")
        update(name)

    elif choice == "5":
        name = input("Enter book name to delete: ")
        remove_a_book(name)

    elif choice == "6":
        break

    else:
        print("Invalid choice")