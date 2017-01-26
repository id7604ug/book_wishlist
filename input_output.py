import os
import datastore
import json

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.json')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

separator = '^^^'  # a string probably not in any valid data relating to a book
counter = 0



def delete_books_from_json(data_to_delete):
    try:
        load_json_file = json.load(open(BOOKS_FILE_NAME, 'r'))
        for data_dictionary in load_json_file:
            dictionary_keys = data_dictionary.keys()
            if data_to_delete in dictionary_keys:
                data_dictionary.pop(data_to_delete)
            write_data_back_file = open(BOOKS_FILE_NAME, "w")
            json.dump(data_dictionary, write_data_back_file)
    except FileExistsError:
        print("Error reading file")



def setup():
    ''' Read book info from file, if file exists. '''

    global counter
    data_list = []
    try :
        with open(BOOKS_FILE_NAME) as f:
            datastore.make_book_list(json.load(f))
            book_sorted = datastore.sort_book_list()
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
        datastore.set_counter(len(book_sorted))


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    output_data = datastore.make_output_data()
    print(json.dumps(output_data))
    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as f:
        json.dump(output_data, f)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(datastore.get_counter()))
