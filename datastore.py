
import os
from book import Book
import time
import operator

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0

def setup():
    ''' Read book info from file, if file exists. '''

    global counter

    try :
        with open(BOOKS_FILE_NAME) as f:
            data = f.read()
            make_book_list(data)
            sort_book_list()
    except FileNotFoundError:
        # First time program has run. Assume no books.
        pass


    try:
        with open(COUNTER_FILE_NAME) as f:
            try:
                counter = int(f.read())
            except:
                counter = 0
    except:
        counter = len(book_list)


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    output_data = make_output_data()

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as f:
        f.write(output_data)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))


def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''

    global book_list

    sort_book_list()

    if len(kwargs) == 0:
        return book_list

    if 'read' in kwargs:
        read_books = [ book for book in book_list if book.read == kwargs['read'] ]
        return read_books

    if 'title' in kwargs:

        search_results = [ book for book in book_list if book.title == kwargs['title'] ]

        return search_results

    if 'author' in kwargs:

        search_results = [ book for book in book_list if book.author == kwargs['author'] ]

        return search_results


def add_book(book):
    ''' Add to db, set id value, return Book '''
    global book_list
    book.id = generate_id()
    book_list.append(book)
    sort_book_list() # sorts books to keep them in proper order.


def delete_book(author_name):
    """Find the book by the author name so that we can be able to delete the book from the wishlist"""

    global book_list
    book_exist = find_book_by_author(author_name)
    if book_exist is not None:
        book_index = book_list.index(book_exist)
        book_deleted = book_list.pop(book_index)
        print("{} has been successfully deleted".format(book_deleted))
    else:
        print("{} is not in our database".format(author_name))


def find_book_by_author(author_name):
    """Search for the author in the booklist, if author is found, return the author. Otherwise, return None"""
    global book_list
    for i in range(len(book_list)):
        if author_name == book_list[i].author:
            author_exist = book_list[i]
            return author_exist
        else:
            return None

def edit_author(book_title, new_author): # Method to edit the author of the book
    global book_list
    author_exists = False
    for i in range(len(book_list)):
        if book_title == book_list[i].title:
            book_exists = True
        if book_exists:
            book_list[i].set_author(new_author)
        elif i == (len(book_list) - 1):
            print("This author does not exist in your collection.")

def edit_title(book_author, new_title): # Method to edit the book title
    global book_list
    author_exists = False
    for i in range(len(book_list)):
        if book_author == book_list[i].author:
            author_exists = True
        if author_exists:
            book_list[i].set_title(new_title)
        elif i == (len(book_list) - 1):
            print("This book does not exist in your collection.")

def generate_id():
    global counter
    counter += 1
    return counter


def set_read(book_id, read):
    '''Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in book_list:

        if book.id == book_id:
            book.read = True
            book.dateRead = time.strftime("%x")
            return True

    return False # return False if book id is not found



def make_book_list(string_from_file):
    ''' turn the string from the file into a list of Book objects'''

    global book_list

    books_str = string_from_file.split('\n')

    for book_str in books_str:
        data = book_str.split(separator)
        book = Book(data[0], data[1], data[2] == 'True', data[3], int(data[4]))
        book_list.append(book)


def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    output_data = []

    for book in book_list:
        output = [ book.title, book.author,str(book.read), str(book.dateRead), str(book.id) ]
        output_str = separator.join(output)
        output_data.append(output_str)

    all_books_string = '\n'.join(output_data)

    return all_books_string


def sort_book_list(): # Sorts book_list alphabetically

    global book_list

    book_list.sort(key=operator.attrgetter("title"), reverse=False) # learned abour operator from StackSocial.

    return book_list
