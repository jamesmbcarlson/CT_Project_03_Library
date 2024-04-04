# James Carlson
# Coding Temple - SE FT-144
# Module 4: Mini-Project | Contact Management System

from library_classes.book import Book
from library_classes.user import User
from library_classes.author import Author

# format constants
F_UNDERLINE = "\033[4m"
F_RED = "\033[91m"
F_YELLOW = "\033[93m"
F_GREEN = "\033[92m"
F_RESET = "\033[0m"

# legend has it there was a genre class?? And it may get me bonus points??
class Genre:
    def __init__(self):
        # self.genre?
        # self.description
        # self.list_of_books = []
        pass
    # tbh I don't know if a genre class makes that much sense to me
# I could also make a library class... but the driver code is probably fine

# our database! 
library_books = []
library_users = []
library_authors = []



    
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
            book_add()
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

def book_add():
    '''
    Add a book to the library.
    '''

    # create new book and set its values with the input below
    new_book = Book()

    print()
    while(new_book.get_title() == None):
        new_book.set_title(input("What is the title of the book? "))

    while(new_book.get_author() == None):
        new_book.set_author(input("Who is the author of this book? "))
        # TO-DO: add author to list of authors if not already in library

    while(new_book.get_isbn() == None):
        new_book.set_isbn(input("What is the ISBN for this book? "))

    while(new_book.get_genre() == None):
        new_book.set_genre(input("What genre is this book? "))

    while(new_book.get_publication_date() == None):
        new_book.set_publication_date(input("What is the date this book was published? (MM/DD/YYYY) "))

    library_books.append(new_book)

    print(f"\"{new_book.get_title()}\" by {new_book.get_author()} has been added to the library!")

def book_borrow():
    '''
    Borrow an available, existing book from the library.
    '''
    # need book title or other search term
        # share search_function like I did in contact project?
    # verify that book is in library
    # verify book is available
    # if yes, add borrowed book to user's list, mark book unavailable
    pass

def book_return():
    '''
    Return a borrowed book to the library.
    '''
    # take book title (search function?)
    # verify book is in library
    # verify book is on loan
    # set availability to available, remove from user's borrowed list
    pass

def book_search():
    '''
    Search for a book in the library.
    '''
    # search by title... author? Any other fields?
    pass

def book_display_all():
    '''
    Display all books in the library.
    '''
    
    print("\nHere are all the books available at our library: ")

    # print all books in library, looping through list
    for b in library_books:
        print(f"\nTitle: {F_GREEN}{Book(b).get_title()}{F_RESET}")
        print(f"Author: {Book(b).get_author()}")
        print(f"ISBN: {Book(b).get_isbn()}")
        print(f"Genre: {Book(b).get_genre()}")
        print(f"Publication Date: {Book(b).get_publication_date()}")
        print(f"Availability Status: {Book(b).get_availability().title()}")

def user_add():
    '''
    Add a user to the library system.
    '''
    pass

def user_details():
    '''
    View details for a user in the library system.
    '''
    pass

def user_display_all():
    '''
    Display all users in the library system.
    '''
    pass

def author_add():
    '''
    Add an author to the library system.
    '''
    # TO-DO: call this when adding a book; check if author is in system and add if not
    pass

def author_details():
    '''
    View details for an author in the library system.
    '''
    pass

def authors_display_all():
    '''
    Display all authors in the library system.
    '''
    pass

# Computer, run program!
print("\nWelcome to the Library Management System!")
menu_main()