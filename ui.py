from book import Book
import string


def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as read
        4. Add book to wishlist
        5. Search database for book
        6. Delete book by author name:
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def show_list(books):
    ''' Format and display a list of book objects'''

    if len(books) == 0:
        print ('* No books *')
        return

    for book in books:
        print(book)

    print('* {} book(s) *'.format(len(books)))


def ask_for_book_id():

    ''' Ask user for book id, validate to ensure it is a positive integer '''

    while True:
        try:
            id = int(input('Enter book id:'))
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')


def ask_for_book_title():
    """Ask the user for the author name of a specific book you want to delete"""
    author_name = input("Please enter the author name of the book: ")
    return author_name

def get_new_book_info():

    ''' Get title and author of new book from user '''

    title = input('Enter title: ')
    author = input('Enter author: ')

    return Book(title, author)


def message(msg):
    '''Display a message to the user'''
    print(msg)

def search_for_book(): # asks the User for the title of the book to search for.

    query = ""
    entry_return = {}

    while True:

        question = input("Do you wish to search by title or author? ")

        if question.lower() == "title":
            query = "title"
            break

        if question.lower() == "author":
            query = "author"
            break

        else:
            print("That is not a valid entry, try again.")

    if query == "title":

        entry = input("Please enter the FULL title of the book you want to search for: ")
        entry_return.update( { "title" : entry } )

    if query == "author":

        entry = input("Please enter FULL name of the author you want to search for: ")
        entry_return.update( { "author" : entry } )

    if entry == "":

        print("Please enter a title.")


    return entry_return
