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
        self.author = new_author_name      # FIXED: was new_subject_name
        self.subject = new_subject_name

library_books = []

def add_book_to_library(book_obj):
    library_books.append(book_obj)  # FIXED: =append typo
    print("the book was added")

def remove_a_book(book_name):
    for book in library_books:
        if book.name.lower() == book_name.lower():
            library_books.remove(book)
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
            book.name = new_name
            book.author = new_author
            book.subject = new_subject
            print("Book updated successfully")
            return
    print("Book not found")

# Testing your objects
OOP_using_JAVA = Book("OOP using JAVA", "CS", "John")
C_plus_plus = Book("c plus plus", "CS", "tom")

add_book_to_library(C_plus_plus)
add_book_to_library(OOP_using_JAVA)

C_plus_plus.show_info()  # This will print None unless you change show_info to return
C_plus_plus.edit_author_and_subject("Mary", "Maths")  # FIXED: Correct order
print(C_plus_plus.show_info())

display()
search_a_book("c plus plus")
remove_a_book("OOP using JAVA")
display()

# Main menu like your Student program
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

