
import os
from book import Book
import time
import input_output
import json

import operator

separator = '\n'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0


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
    """Find the book by the title so that we can be able to delete the book from the wishlist"""

    global book_list
    book_exist = find_book_by_title(author_name)
    if book_exist is not None:
        book_index = book_list.index(book_exist)
        book_deleted = book_list.pop(book_index)
        print(str(book_deleted).replace(" ", "^^^"))
        print("{} has been successfully deleted".format(book_deleted))
    else:
        print("{} is not in our database".format(author_name))


def find_book_by_title(book_title):
    """Search for the title in the booklist, if author is found, return the author. Otherwise, return None"""
    global book_list
    for i in range(len(book_list)):
        if book_title.lower() == str(book_list[i].title).lower():
            input_output.delete_file_data(str(book_list[i].title))
            author_exist = book_list[i]
            return author_exist
    else:

        return None

def edit_author(book_title, new_author): # Method to edit the author of the book
    global book_list
    book_exists = False
    book_not_found = True
    for i in range(len(book_list)):
        if book_title == book_list[i].title:
            book_exists = True
            book_not_found = False
        if book_exists:
            book_list[i].set_author(new_author)
            book_exists = False
        elif i == (len(book_list) - 1) & book_not_found:
            print("This author does not exist in your collection.")

def edit_title(book_author, new_title): # Method to edit the book title
    global book_list
    author_exists = False
    author_not_found = True
    for i in range(len(book_list)):
        if book_author == book_list[i].author:
            author_exists = True
            author_not_found = False
        if author_exists:
            book_list[i].set_title(new_title)
            author_exists = False
        elif i == (len(book_list) - 1) & author_not_found:
            print("This book does not exist in your collection.")

def generate_id():
    global counter
    counter += 1
    return counter


def set_read(book_id, read, rating=0):
    '''Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in book_list:

        if book.id == book_id:
            book.read = True
            book.dateRead = time.strftime("%x")
            book.rating = rating
            return True

    return False # return False if book id is not found


def make_book_list(json_data):

    ''' turn the string from the file into a list of Book objects'''

    global book_list
    book_dictionaries = json_data
    book_data = []
    for book in book_dictionaries:
        single_book = []
        for value in book.values():
            single_book.append(value)
        book_data.append(single_book)

    for data in book_data:
        # print(data) # Debugging
        book = Book(data[0], data[1], data[2] == 'True', data[3], int(data[4]), int(data[5]))
        book_list.append(book)


def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    output_data = []

    for book in book_list:
        output = book.get_dictionary_formatted()
        output_data.append(output)

    # all_books_string = '\n'.join(output_data)

    return output_data


def sort_book_list(): # Sorts book_list alphabetically

    global book_list

    book_list.sort(key=operator.attrgetter("title"), reverse=False) # learned abour operator from StackSocial.

    return book_list

def set_counter(new_counter): # Sets the counter
    global counter
    counter = new_counter
