class Book:
    def __init__(self, title, author, subject):
        self.title = title
        self.author = author
        self.subject = subject

    def edit_details(self, title=None, author=None, subject=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if subject:
            self.subject = subject

    def add_a_book(book_list, title, author, subject):
        new_book = Book(title, author, subject)
        book_list.append(new_book)
        print(f"Book '{title}' has been added to the library.")

    def remove_a_book(book_list, title):
        for book in book_list:
            if book.title == title:
                book_list.remove(book)
                print(f"Book '{title}' has been removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def search_a_book(book_list, title):
        for book in book_list:
            if book.title == title:
                print(f"Book '{title}' found in the library.")
                return book
        print(f"Book '{title}' not found in the library.")
        return None
    
    def list_all_books(book_list):
        if not book_list:
            print("No books available in the library.")
            return
        print("Books available in the library:")
        for book in book_list:
            book.show_details()
        