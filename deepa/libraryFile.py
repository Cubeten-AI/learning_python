import os

class Book:
    def __init__(self, name, subject, author):
        self.name = name
        self.subject = subject
        self.author = author

    def show_info(self):
        print(f"Name: {self.name} | Subject: {self.subject} | Author: {self.author}")
    
    def to_string(self):
        return f"{self.name},{self.subject},{self.author}"

library_books = []
FILENAME = "library.txt"

def load_books():
    """r = read mode. File must exist or it throws error"""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                name, subject, author = line.strip().split(",")
                library_books.append(Book(name, subject, author))
        print(f"Loaded {len(library_books)} books from {FILENAME}")

def save_books():
    """w = write mode. Overwrites file each time"""
    with open(FILENAME, "w") as f:
        for book in library_books:
            f.write(book.to_string() + "\n")
    print("Data saved to file")

def add_book():
    name = input("Enter book name: ")
    subject = input("Enter subject: ")
    author = input("Enter author: ")
    book = Book(name, subject, author)
    library_books.append(book)
    
    # a = append mode. Adds to end of file without deleting old data
    with open(FILENAME, "a") as f:
        f.write(book.to_string() + "\n")
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
            save_books()  # rewrite whole file after update
            print("Book updated!")
            return
    print("Book not found")

def delete_book():
    name = input("Enter book name to delete: ")
    for book in library_books:
        if book.name.lower() == name.lower():
            library_books.remove(book)
            save_books()  # rewrite whole file after delete
            print("Book deleted!")
            return
    print("Book not found")

def create_file():
    """x = create mode. Creates file, but errors if file already exists"""
    try:
        with open(FILENAME, "x") as f:
            pass
        print(f"{FILENAME} created")
    except FileExistsError:
        print(f"{FILENAME} already exists")

def menu():
    load_books()  # load existing books when program starts
    
    while True:
        print("\n========== Library Management =========")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Create New File")
        print("7. Save All")
        print("8. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1': add_book()
        elif choice == '2': display_books()
        elif choice == '3': search_book()
        elif choice == '4': update_book()
        elif choice == '5': delete_book()
        elif choice == '6': create_file()
        elif choice == '7': save_books()
        elif choice == '8': 
            save_books()
            print("Exiting... Happy reading!")
            break
        else:
            print("Invalid choice. Try again.")

menu()