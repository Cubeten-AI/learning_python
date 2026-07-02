class Book:
    def __init__(self,name,subject,author):
        self.name = name
        self. subject = subject
        self. author = author

    def show_info(self):
        print(f"This book {self.name} is written by {self.author} under the subject of {self.subject}")

    def edit_name(self, new_name):
        print(f"previous name was {self.name}")
        self.name = new_name
        print(f"new name is {self.name}")

    def edit_author_and_subject(self,new_author_name,new_subject_name):
        self.author = new_author_name
        self.author = new_subject_name


OOP_using_JAVA = BOOK("OOP using JAVA",CS,"John")
C_plus_plus = BOOK("C plus plus","CS",,"tom")
# OOP_using_JAVA.show_info()

C_plus_plus.show_info()
C_plus_plus.edit_author_and_subject("Maths","Mary")
C_plus_plus.show_info()


def add_book_to_library(book_name):
    library_books =append(book_name)
    print("the book was added")

add_book_to library(C_plus_plus)

def remove_a_book(book_name):
    pass
def search_a_book(book_name):
    pass
def display():
    pass
def update_book(book_name):
    pass
for book in library_books:
    print(book.show_info())
    new_name = input("C plus plus programming language")
    new_author = input("tonny")
    new_subject = input("programming")

    book.name = new_name
    book.author = new_author
    book.subject = new_subject
    print("Book updated successsfully")
    return
print("Book not found")



