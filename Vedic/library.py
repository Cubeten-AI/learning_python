class book:

    def __init__(self, name, subject, author):
        self.name = name
        self.subject = subject
        self.author = author

    def show_info(self):
        print(f"This book {self.name} is written by {self.author} under the subject of {self.subject}")

    def edit_name(self, new_name):
        print(f"old name was {self.name}")
        self.name = new_name
        print(f"The new name is {self.name}")

    def update_subject_and_author(self, subject, author):
        self.subject = subject
        self.author = author


library_book = []

c_plus_plus = book("C++", "CS", "Hank")
library_book.append(c_plus_plus)

c_plus_plus.show_info()

c_plus_plus.update_subject_and_author("Programming", "james")

c_plus_plus.show_info()