# A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
class User:
    def __init__(self, name, library_id):
        self._name = name
        self.__library_id = library_id
        self.borrowed_books = []

    # getters and setters
        
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        # TO-DO: validation?? should I should make one method for all proper name input?
        self._name = new_name

    def get_library_id(self):
        return self.__library_id
    
    def set_library_id(self, new_id):
        # ??
        self.__library_id = new_id

