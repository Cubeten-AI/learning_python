class Book:
    def __init__(self, name, subject, author):
        self.name = name
        self.subject = subject
        self.author = author

    def show_info(self):
        print(f"Name: {self.name} | Subject: {self.subject} | Author: {self.author}")

    def edit_name(self, new_name):
        self.name = new_name

    def edit_author_and_subject(self, new_author, new_subject):
        self.author = new_author
        self.subject = new_subject

library_books = []

def add_book():
    name = input("Enter book name: ")
    subject = input("Enter subject: ")
    author = input("Enter author: ")
    book = Book(name, subject, author)
    library_books.append(book)
    print("Book added successfully!")

def display_books():
    if not library_books:
        print("Library is empty")
        return
    print("\n--- All Books ---")
    for i, book in enumerate(library_books, 1):
        print(f"{i}. ", end="")
        book.show_info()

def search_book():
    name = input("Enter book name to search: ")
    for book in library_books:
        if book.name.lower() == name.lower():
            print("Book found:")
            book.show_info()
            return
    print("Book not found")

def update_book():
    name = input("Enter book name to update: ")
    for book in library_books:
        if book.name.lower() == name.lower():
            book.name = input("Enter new name: ")
            book.subject = input("Enter new subject: ")
            book.author = input("Enter new author: ")
            print("Book updated!")
            return
    print("Book not found")

def delete_book():
    name = input("Enter book name to delete: ")
    for book in library_books:
        if book.name.lower() == name.lower():
            library_books.remove(book)
            print("Book deleted!")
            return
    print("Book not found")

def menu():
    while True:
        print("\n========== Library Management =========")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1': add_book()
        elif choice == '2': display_books()
        elif choice == '3': search_book()
        elif choice == '4': update_book()
        elif choice == '5': delete_book()
        elif choice == '6': 
            print("Exiting... Happy reading!")
            break
        else:
            print("Invalid choice. Try again.")

menu()