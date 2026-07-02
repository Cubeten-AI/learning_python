class Book:
    
    def __init__(self, name, subject, author):
        self.name = name
        self.subject = subject
        self.author =  author
        
    def show_info(self):
        print(f"this book {self.name} is written by {self.author} under the subject of {self.subject}")
        
    def edit_name(self, new_name):
        print(f"the previous name was{self.name}")
        self.name = new_name
        print(f"the new name is {self.name}")
        
    def edit_author_and_subject(self, new_author_name, new_subject_name):
        self.author = new_author_name
        self.subject = new_subject_name
        
library_book =[]
oop_using_java = Book("opp_using_java", "CS", "john")
c_plus_plus = Book("c_plus_plus", "CS", "tom")
oop_using_java.show_info()
c_plus_plus.show_info()
c_plus_plus.edit_author_and_subject("mary", "maths")
c_plus_plus.show_info()

def add_book_to_library(book_name):
    library_book.append(book_name)
    print(f"the book was added")
add_book_to_library(c_plus_plus)
add_book_to_library(oop_using_java)

def remove_a_book(book_name):
    if book_name in library_book:
        library_book.remove(book_name)
        print(f"book removed successfully")
    else:
        print(f"book not found")
remove_a_book(c_plus_plus)

def search(book_name):
    for book in library_book:
        if book.name.lower() == book_name.name.lower():
            print("book found")
            book.show_info()
            return
    print("book not found")
search(c_plus_plus)

def display():
    if len(library_book) == 0:
        print("no book found")
    else: 
        for book in library_book:
            print("book found")
            book.show_info()
            
display()