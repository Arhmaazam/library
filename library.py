class Library:
    books = None

    def __init__(self, books):
        self.books = books

    def add_book(self, add_books):
        self.books.append(add_books)

    def display_available_books(self):
        print("Available books:")
        for book in self.books:
            if book.copies > 0:
                print('Title:-', book.title, 'Author:-', book.author, 'ISBN:-', book.isbn, 'Copies:-', book.copies)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.copies > 1:
                    book.copies -= 1
                    print('Book is borrowed.')
                    return True
        if not (self.books[0].title == title or self.books[1].title == title or self.books[2].title == title or
                self.books[3].title == title):
            print('book not found in libray')

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if 20 > book.copies:
                    book.copies += 1
                    print('Book is returned.')
                    return True
                else:
                    print('This is not my book.')
                    return False

    def is_available(self, title):
        for book in self.books:
            if book.title == title:
                return True
        return False
