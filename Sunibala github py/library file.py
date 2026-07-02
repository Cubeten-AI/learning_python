import json
import os

class Book:
    def __init__(self, name, subject, author):
        self.name = name
        self.subject = subject
        self.author = author
    
    def show_info(self):
        return f"This book {self.name} is written by {self.author} under the subject of {self.subject}"
    
    def edit_name(self, new_name):
        print(f"previous name was {self.name}")
        self.name = new_name
        print(f"the new name is {self.name}")
    
    def edit_author_and_subject(self, new_author_name, new_subject_name):
        self.author = new_author_name
        self.subject = new_subject_name
    
    def to_dict(self):  # Convert object to dict for JSON
        return {"name": self.name, "subject": self.subject, "author": self.author}

library_books = []
FILE_NAME = "library.json"

# ---------- FILE FUNCTIONS ----------
def save_to_file():
    """Mode 'w' = write/overwrite entire file"""
    with open(FILE_NAME, 'w') as f:
        data = [book.to_dict() for book in library_books]
        json.dump(data, f, indent=4)
    print("Data saved to file")

def load_from_file():
    """Mode 'r' = read file"""
    global library_books
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            data = json.load(f)
            library_books = [Book(item['name'], item['subject'], item['author']) for item in data]
        print(f"Loaded {len(library_books)} books from file")
    else:
        print("No save file found. Starting empty library")

def create_file_if_missing():
    """Mode 'x' = create new file, error if exists"""
    try:
        with open(FILE_NAME, 'x') as f:
            json.dump([], f)  # Start with empty list
        print("Created new library file")
    except FileExistsError:
        print("Library file already exists")

def append_log(message):
    """Mode 'a' = append to end of file"""
    with open("library_log.txt", 'a') as f:
        f.write(f"{message}\n")

# ---------- LIBRARY FUNCTIONS ----------
def add_book_to_library(book_obj):
    library_books.append(book_obj)
    save_to_file()  # Auto-save after adding
    append_log(f"Added: {book_obj.name}")
    print("the book was added")

def remove_a_book(book_name):
    for book in library_books:
        if book.name.lower() == book_name.lower():
            library_books.remove(book)
            save_to_file()  # Auto-save after deleting
            append_log(f"Removed: {book_name}")
            print(f"{book_name} removed")
            return
    print("Book not found")

def search_a_book(book_name):
    for book in library_books:
        if book.name.lower() == book_name.lower():
            print(f"Found: {book.show_info()}")
            return
    print("Book not found")

def display():
    if not library_books:
        print("Library is empty")
    else:
        print("\n=== Library Books ===")
        for book in library_books:
            print(book.show_info())

def update_book(book_name):
    for book in library_books:
        if book.name.lower() == book_name.lower():
            print("Enter new details:")
            new_name = input("New name: ")
            new_author = input("New author: ")
            new_subject = input("New subject: ")
            if new_name: book.name = new_name
            if new_author: book.author = new_author
            if new_subject: book.subject = new_subject
            save_to_file()  # Auto-save after update
            append_log(f"Updated: {book_name}")
            print("Book updated successfully")
            return
    print("Book not found")

# ---------- PROGRAM START ----------
create_file_if_missing()  # 'x' mode: create file if it doesn't exist
load_from_file()          # 'r' mode: load existing data

# Testing your objects - only add if library is empty
if not library_books:
    OOP_using_JAVA = Book("OOP using JAVA", "CS", "John")
    C_plus_plus = Book("c plus plus", "CS", "tom")
    add_book_to_library(C_plus_plus)
    add_book_to_library(OOP_using_JAVA)

# Main menu
while True:
    print("\n========== Library Management ==========")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        name = input("Enter book name: ")
        subject = input("Enter subject: ")
        author = input("Enter author: ")
        new_book = Book(name, subject, author)
        add_book_to_library(new_book)
    elif choice == "2": display()
    elif choice == "3": 
        name = input("Enter book name to search: ")
        search_a_book(name)
    elif choice == "4":
        name = input("Enter book name to update: ")
        update_book(name)
    elif choice == "5":
        name = input("Enter book name to delete: ")
        remove_a_book(name)
    elif choice == "6":
        print("Exiting...")
        break
    else: print("Invalid choice")