import re

# A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
class User:
    def __init__(self):
        self._name = None
        self.__library_id = None
        self._borrowed_books = []

    # getters and setters
        
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if re.search(r"^[A-Za-z][A-Za-z\.\-\s]+[A-Za-z]$", new_name):
            self._name = new_name
        else:
            print("Error: Name field must begin and end with letters, and cannot include numbers or special characters other than the following: . -")

    def get_library_id(self):
        return self.__library_id
    
    def set_library_id(self, new_id):
        # ?? maybe just an int?
        try:
            check_for_int = int(new_id)
            if check_for_int <= 0:
                give_me_an_error = check_for_int/0 # just trying a different validation method other than regex haha
        except:
            print("Error: Library ID must be a whole number greater than 0.")
        else:
            self.__library_id = new_id

    def get_borrowed_books(self):
        return self._borrowed_books

    def add_to_borrowed_books(self, book):
        self._borrowed_books.append(book)

    def remove_from_borrowed_books(self, book):
        self._borrowed_books.remove(book)