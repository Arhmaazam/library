from book import Book
from library import Library
from user import Student, Staff

book1 = Book(**{'title': 'maths', 'author': 'Ali', 'isbn': 11, 'copies': 20})
book2 = Book(**{'title': 'comp', 'author': 'Hamza', 'isbn': 22, 'copies': 20})
book3 = Book(**{'title': 'phy', 'author': 'Hagi', 'isbn': 33, 'copies': 20})
book4 = Book(**{'title': 'chem', 'author': 'Rina', 'isbn': 44, 'copies': 20})
library = Library([book1, book2, book3, book4])

print('------------------------------')
print('hello!!')
print('Hi! sir who are you?')
print('You are a student or a staff.')
print('press 1 for student.')
print('press 2 for staff.')
you = input('Please enter:- ')
if you == 1:
    name = input("Enter your name:- ")
    roll_no = input("Enter your roll_no:- ")
    user_id = 123
    student = Student(name, user_id, roll_no)
    num = 1
    while num != 0:
        if num == 1 or num == 2 or num == 3 or num == 4:
            print('--------------------------------------------------')
            print('Choose a number in 1-4 which you want.')
            print('Press 1 to display available books.')
            print('press 2 to check the book is available or not.')
            print('Press 3 to return a book.')
            print('Press 4 to borrow a book.')
            print('Press 0 to exit.')
            num = int(input('Enter a number:- '))
            print('---------------------------------------------------')
            if num == 1:
                library.display_available_books()
            elif num == 2:
                title = input('Enter a book_tittle:- ')
                if library.is_available(title):
                    print(title, 'book is available.')
                else:
                    print(title, 'book is not available.')
            elif num == 3:
                title = input('Enter book_title to return: ')
                library.return_book(title)
                student.borrowed_list.remove(title)
                print(student.borrowed_list)
            elif num == 4:
                title = input('Enter a book_title to borrow:- ')
                if len(student.borrowed_list) < student.max_borrow_limit:
                    if library.borrow_book(title):
                        student.borrowed_list.append(title)
                        print(student.borrowed_list)
                else:
                    print('Student cannot borrow more than 3 books.')

elif you == 2:
    name = input("Enter your name:- ")
    user_id = 3344
    employee_id = input("Enter your employee_id:- ")
    staff = Staff(name, user_id, employee_id)
    num = 1
    while num != 0:
        if num == 1 or num == 2 or num == 3 or num == 4 or num == 5:
            print('--------------------------------------------------')
            print('Choose a number in 1-5 which you want.')
            print('Press 1 to display available books.')
            print('press 2 to check the book is available or not.')
            print('Press 3 to return a book.')
            print('Press 4 to add book in book_list.')
            print('Press 5 to borrow a book.')
            print('Press 0 to exit.')
            num = int(input('Enter a number:- '))
            print('---------------------------------------------------')
            if num == 1:
                library.display_available_books()
            elif num == 2:
                title = input('Enter a book_tittle:- ')
                if library.is_available(title):
                    print(title, 'book is available.')
                else:
                    print(title, 'book is not available.')
            elif num == 3:
                title = input('Enter book_title to return: ')
                library.return_book(title)
                staff.borrowed_list.remove(title)

            elif num == 4:
                book = Book(
                    title=input("Enter a book_title:- "),
                    author=input("Enter a book_author:- "),
                    isbn=int(input("Enter a book_isbn:- ")),
                    copies=int(input("Enter a book_copies:- "))
                )
                library.add_book(book)
                print('Book added to library.')
            elif num == 5:
                title = input('Enter a book_title to borrow:- ')
                if len(staff.borrowed_list) < staff.max_borrow_limit:
                    if library.borrow_book(title):
                        staff.borrowed_list.append(title)
                        print(staff.borrowed_list)
                else:
                    print('Staff cannot borrow more than 5 books.')