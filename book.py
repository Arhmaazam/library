class Book:
    title = None
    author = None
    isbn = None
    copies = None

    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def is_available(self):
        if self.copies > 0:
            return True
        return False

    def borrow_book(self):
        if self.is_available():
            self.copies -= 1
            return True
        return False

    def return_book(self):
        self.copies += 1
