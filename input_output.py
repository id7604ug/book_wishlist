import os
import datastore
import json

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

separator = '^^^'  # a string probably not in any valid data relating to a book
counter = 0


def delete_file_data(data_to_delete):
    with open(BOOKS_FILE_NAME, 'r') as book_data:
        lines = book_data.readlines()


    with open(BOOKS_FILE_NAME, 'w') as book_data:
        for line in lines:
            if line.replace("^^^", " ") != data_to_delete:
                pass
            else:
                book_data.write(line)


def setup():
    ''' Read book info from file, if file exists. '''

    global counter
    data_list = []
    try :
        with open(BOOKS_FILE_NAME) as f:
            datastore.make_book_list(json.load(f))
            data_list = datastore.sort_book_list()
    except FileNotFoundError:
        # First time program has run. Assume no books.
        pass


    try:
        with open(COUNTER_FILE_NAME) as f:
            try:
                datastore.set_counter(int(f.read()))
            except:
                datastore.set_counter(0)
    except:
        datastore.set_counter(len(data_list))


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    output_data = datastore.make_output_data()
    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as f:
        json.dump(output_data, f)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(datastore.get_counter()))
