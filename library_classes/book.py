import re

# A class representing individual books with attributes such as title, author, ISBN, genre, publication date, and availability status.
class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availability="available"):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__publication_date = publication_date
        self._availability = availability
        # I made availability protected instead of private because it would be changed regularly,
        # whereas the other fields should theoretically be totally static

    def __init__(self): # TO-DO: this actually makes the one above defunct; I can't access it from my library 
        self.__title = None
        self.__author = None
        self.__isbn = None
        self.__genre = None
        self.__publication_date = None
        self._availability = "available"
        
    def get_title(self):
        return self.__title
    
    def set_title(self, new_title):
        if re.search(r"^(?!\s*$).+", new_title):
            self.__title = new_title
        else:
            print("Error: Book title cannot be empty. Book title was not set.")
    
    def get_author(self):
        return self.__author
    
    def set_author(self, new_name):
        if re.search(r"^[A-Za-z][A-Za-z\.\-\&+\s]+[A-Za-z]$", new_name):
            self.__author = new_name
        else:
            print("Error: Author field must begin and end with letters, and cannot include numbers or special characters other than the following: . - & + ")

    def get_isbn(self):
        return self.__isbn
    
    # I looked up how to actually determine ISBNs (https://en.wikipedia.org/wiki/ISBN), and it's crazy, so I just went with this:
    def set_isbn(self, new_isbn):
        if re.search(r"^(978|979)[\d]{10}$", new_isbn):
            self.__isbn = new_isbn
        else:
            print("Error: ISBN must be 13 digits and begin with either 978 or 979.")
    
    def get_genre(self):
        return self.__genre
    
    def set_genre(self, new_genre):
        if re.search(r"^[A-Za-z][A-Za-z\-\&+\s]+[A-Za-z]$", new_genre):
            self.__genre = new_genre
        else:
            print("Error: Genre field must begin and end with letters, and cannot include numbers or special characters other than the following: - & + ")
    
    def get_publication_date(self):
        return self.__publication_date
    
    def set_publication_date(self, new_date):
        if re.search(r"^\d{2}/?\-?\d{2}/?\-?\d{4}$", new_date):
            self.__publication_date = new_date
        else:
            print("Error: Publication date must be in format MM/DD/YYYY")
    
    def get_availability(self):
        return self._availability
    
    def set_availability(self, updated_availability):
        # TO-DO: add validation?
        self._availability = updated_availability