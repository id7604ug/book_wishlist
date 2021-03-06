import time

class Book:

    ''' Represents one book in a user's list of books'''

    NO_ID = -1

    def __init__(self, title, author, read=False, dateRead="not read", id=NO_ID, rating=0):
        '''Default book is unread, and has no ID'''
        self.title = title
        self.author = author
        self.dateRead = dateRead # attribute for the date book was marked as read.
        self.read = read
        self.id=id
        self.rating = rating


    def set_id(self, id):
        self.id = id


    def __str__(self):
        read_str = 'no'
        if self.read:
            read_str = 'yes'

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        template = 'id: {} Title: {} Author: {} Read: {} Date Read: {} Rating: {}'
        return template.format(id_str, self.title, self.author, read_str, self.dateRead, self.rating)


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.dateRead == other.dateRead and self.id==other.id

    def set_author(self, new_author_name): # Method to change the authors name
        self.author = new_author_name

    def set_title(self, new_title): # Method to change the books title
        self.title = new_title

    def get_dictionary_formatted(self): # Method to return all book data as a dictionary
        return {"Title": self.title,"Author": self.author, "Read": str(self.read), "Date Read": str(self.dateRead), "ID": str(self.id), "Rating": str(self.rating)}
