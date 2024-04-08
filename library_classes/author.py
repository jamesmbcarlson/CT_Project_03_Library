import re

# A class representing book authors with attributes like name and biography.
class Author:
    def __init__(self):
        self._name = None
        self._biography = None
        self._books_in_library = []

    # getters and setters
        
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if re.search(r"^[A-Za-z][A-Za-z\.\-\&+\s]+[A-Za-z]$", new_name):
            self._name = new_name
        else:
            print("Error: Author name must begin and end with letters, and cannot include numbers or special characters other than the following: . - & + ")

    def get_biography(self):
        return self._biography
    
    def set_biography(self, new_biography):
        # no validation for biographies; can be empty, or can have as much as the user wants to add!
        self._biography = new_biography

    def get_books_in_library(self):
        return self._books_in_library
    
    def set_books_in_library(self, list_of_books):
        self._books_in_library = list_of_books

    def add_to_books_in_library(self, book):
        self._books_in_library.append(book)