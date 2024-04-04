# A class representing book authors with attributes like name and biography.
class Author:
    def __init__(self, name):
        self._name = name
        self._biography = f"{name} is an author."

    # getters and setters
        
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        # ??
        self._name = new_name

    def get_biography(self):
        return self._biography
    
    def set_name(self, new_biography):
        # ??
        self._biography = new_biography