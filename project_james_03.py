# James Carlson
# Coding Temple - SE FT-144
# Module 4: Mini-Project | Contact Management System

# format constants
F_UNDERLINE = "\033[4m"
F_RED = "\033[91m"
F_YELLOW = "\033[93m"
F_GREEN = "\033[92m"
F_RESET = "\033[0m"

# A class representing individual books with attributes such as title, author, ISBN, genre, publication date, and availability status.
class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availability):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__publication_date = publication_date
        self._availability = availability   # I made this protected instead of private because it would be changed regularly, whereas the other fields would theoretically be totally static
    # just a thought here... does the fields title, author, isbn, genre, or publication date ever need to be changed? for now I may just create get methods
        
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author # I guess author names do change like Yusef Stevens and The Chicks, so maybe I should just make the dang setter classes
    
    def get_isbn(self):
        return self.__isbn
    
    def get_genre(self):
        return self.__genre
    
    def get_publication_date(self):
        return self.__publication_date
    
    def get_availability(self):
        return self._availability
    
    def set_availability(self, updated_availability):
        # TO-DO: add validation?
        self._availability = updated_availability


# A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.borrowed_books = []

    # getters and setters
        
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        # TO-DO: validation?? should I should make one method for all proper name input?
        self.__name = new_name

    def get_library_id(self):
        return self.__library_id
    
    def set_library_id(self, new_id):
        # ??
        self.__library_id = new_id

    # okay but hold up; it would be so nice to interact with the list directly... to get append, remove, etc. setting a new list every time would be such a pain-- it's okay to have some public variables, yeah??

# A class representing book authors with attributes like name and biography.
class Author:
    def __init__(self, name):
        self.__name = name
        self._biography = f"{name} is an author."

    # getters and setters
        
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        # ??
        self.__name = new_name

    def get_biography(self):
        return self._biography
    
    def set_name(self, new_biography):
        # ??
        self._biography = new_biography

# legend has it there was a genre class?? And it may get me bonus points??
class Genre:
    def __init__(self):
        pass
    # tbh I don't know if a genre class makes that much sense to me; what kinds of things would we store in genre? name, list of books, description?


    
def menu_main():
    '''
    Display and handle main menu operations.
    '''

    while True:
        # print menu to terminal
        print(f"\n{F_UNDERLINE}Main Menu:{F_RESET}")
        print(f"{F_YELLOW}1{F_RESET}. Book Operations")
        print(f"{F_YELLOW}2{F_RESET}. User Operations")
        print(f"{F_YELLOW}3{F_RESET}. Author Operations")
        print(f"{F_YELLOW}4{F_RESET}. Quit")

        # get and handle user input
        menu_input = input("Make a selection: ").casefold()
        if menu_input == "1" or menu_input.startswith("book"):
            menu_book_operations()
        elif menu_input == "2" or menu_input.startswith("user"):
            menu_user_operations()
        elif menu_input == "3" or menu_input.startswith("author"):
            menu_author_operations()
        elif menu_input == "4" or menu_input.startswith("quit"):
            print("Thank you for using the Library Management System!")
            return
        else:
            print("Invalid input. Please make a selection from the menu.")

def menu_book_operations():
    '''
    Display and handle book menu operations.
    '''

    while True:
        # print menu to terminal
        print(f"\n{F_UNDERLINE}Book Operations:{F_RESET}")
        print(f"{F_YELLOW}1{F_RESET}. Add a new book")
        print(f"{F_YELLOW}2{F_RESET}. Borrow a book")
        print(f"{F_YELLOW}3{F_RESET}. Return a book")
        print(f"{F_YELLOW}4{F_RESET}. Search for a book")
        print(f"{F_YELLOW}5{F_RESET}. Display all books")
        print(f"{F_YELLOW}6{F_RESET}. Return to main menu")

        # get and handle user input
        menu_input = input("Make a selection: ").casefold()
        if menu_input == "1" or menu_input.startswith("add"):
            pass
        elif menu_input == "2" or menu_input.startswith("borrow"):
            pass
        elif menu_input == "3" or menu_input.startswith("return"):
            pass
        elif menu_input == "4" or menu_input.startswith("search"):
            pass
        elif menu_input == "5" or menu_input.startswith("display"):
            pass
        elif menu_input == "6" or menu_input.startswith("return"):
            return
        else:
            print("Invalid input. Please make a selection from the menu.")

def menu_user_operations():
    '''
    Display and handle user menu operations.
    '''

    while True:
        # print menu to terminal
        print(f"\n{F_UNDERLINE}User Operations:{F_RESET}")
        print(f"{F_YELLOW}1{F_RESET}. Add a new user")
        print(f"{F_YELLOW}2{F_RESET}. View user details")
        print(f"{F_YELLOW}3{F_RESET}. Display all users")
        print(f"{F_YELLOW}4{F_RESET}. Return to main menu")

        # get and handle user input
        menu_input = input("Make a selection: ").casefold()
        if menu_input == "1" or menu_input.startswith("add"):
            pass
        elif menu_input == "2" or menu_input.startswith("view"):
            pass
        elif menu_input == "3" or menu_input.startswith("display"):
            pass
        elif menu_input == "4" or menu_input.startswith("return"):
            return
        else:
            print("Invalid input. Please make a selection from the menu.")

def menu_author_operations():
    '''
    Display and handle author menu operations.
    '''

    while True:
        # print menu to terminal
        print(f"\n{F_UNDERLINE}Author Operations:{F_RESET}")
        print(f"{F_YELLOW}1{F_RESET}. Add a new author")
        print(f"{F_YELLOW}2{F_RESET}. View author details")
        print(f"{F_YELLOW}3{F_RESET}. Display all authors")
        print(f"{F_YELLOW}4{F_RESET}. Return to main menu")

        # get and handle user input
        menu_input = input("Make a selection: ").casefold()
        if menu_input == "1" or menu_input.startswith("add"):
            pass
        elif menu_input == "2" or menu_input.startswith("view"):
            pass
        elif menu_input == "3" or menu_input.startswith("display"):
            pass
        elif menu_input == "4" or menu_input.startswith("return"):
            return
        else:
            print("Invalid input. Please make a selection from the menu.")

# Computer, run program!
print("\nWelcome to the Library Management System!")
menu_main()