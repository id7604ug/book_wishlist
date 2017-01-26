#Main program

import ui, datastore
from book import Book
import input_output


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        show_search()

    elif choice == '6':
        delet_book_by_title()

    elif choice == '7': # Edit book title
        edit_title_by_author()

    elif choice == '8': # Edit book author
        edit_author_by_title()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)

def show_search(): # Searchs the database for a User entered title.
    ''' Fetch and show all books based on User search '''

    search = ui.search_for_book()

    search_key = ""
    search_value = ""

    for key in search.keys(): # loops over dictionary and assigns the key and value
        for value in search.values():

            search_key = key
            search_value = value


    if search_key == "title":

        book = datastore.get_books(title=search_value) # returns search list for title
        ui.show_list(book)

    if search_key == "author":

        book = datastore.get_books(author=search_value) # returns search list for author
        ui.show_list(book)


def delet_book_by_title():
    """Get the choice from user and delete the book"""
    book_title = ui.ask_for_booktitle()
    datastore.delete_book(book_title)

def edit_author_by_title(): # Edit the author by book title
    book_title = ui.ask_for_booktitle()
    new_author = ui.ask_for_new_author()
    datastore.edit_author(book_title, new_author)

def edit_title_by_author(): # Method to edit the title by author
    author = ui.ask_for_authorname()
    new_title = ui.ask_for_new_title()
    datastore.edit_title(author, new_title)

def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    if datastore.set_read(book_id, True):
        rating = ui.get_book_rating()
        datastore.set_read(book_id, True, rating)
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info()
    datastore.add_book(new_book)
    ui.message('Book added: ' + str(new_book))


def quit():
    '''Perform shutdown tasks'''
    input_output.shutdown()
    ui.message('Bye!')


def main():

    input_output.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)



if __name__ == '__main__':
    main()
