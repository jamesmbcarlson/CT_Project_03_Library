# James Carlson
# Coding Temple - SE FT-144
# Module 4: Mini-Project | Contact Management System

import re
from library_classes.book import Book
from library_classes.user import User
from library_classes.author import Author

# format constants
F_UNDERLINE = "\033[4m"
F_RED = "\033[91m"
F_YELLOW = "\033[93m"
F_GREEN = "\033[92m"
F_RESET = "\033[0m"

# our database! 
library_books = []
library_users = []
library_authors = []
user_id_increment = 1


    
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
    author_add_via_book_add(new_book.get_author(), new_book)

    while(new_book.get_isbn() == None):
        new_book.set_isbn(input("What is the ISBN for this book? "))

    while(new_book.get_genre() == None):
        new_book.set_genre(input("What genre is this book? "))

    while(new_book.get_publication_date() == None):
        new_book.set_publication_date(input("What is the date this book was published? (MM/DD/YYYY) "))

    library_books.append(new_book)

    print(f"\"{new_book.get_title()}\" by {new_book.get_author()} has been added to the library!")

def book_borrow_via_input():
    '''
    Prompt user for book to borrow. If available, the book can be loaned out to a user.
    '''
    # exit function if books list is empty
    if is_library_books_empty():
        return
    
    # search for book to borrow
    book_to_borrow = search_books_by_keyword(input("Which book is being checked out? "))

    # escape if book not found
    if book_to_borrow == None:
        print("Sorry! Returning to Main Menu.")
        return
    
    # if book is found
    else:
        book_title = f"\"{Book(book_to_borrow).get_title()}\""

        # book is found and available to borrow
        if Book(book_to_borrow).get_is_available():
            print(f"\n{book_title} is available to borrow!");
            book_borrow(book_to_borrow)

        # book is found, but not available to borrow
        else:
            print(f"{book_title} is unavailable to borrow. Sorry for the inconvenience!")
            print("Returning to Main Menu.")

def book_borrow(book):
    '''
    Prompt for library user to borrow given book. If available, handle loaning out of book.
    '''

    # get user to loan book to
    user = search_users_by_keyword(input("Which user would like to borrow this book? "))

    # user not found
    if user == None:
        print("User not found. Returning to Main Menu.")

    # book successfully loaned out to specified user
    else:
        User(user).add_to_borrowed_books(book)
        Book(book).set_is_available(False)
        Book(book).set_borrower(user)
        print(f"\"{book}\" has been loaned out to {User(user).get_name()}!")

def book_return_via_input():
    '''
    Return a borrowed book to the library.
    '''
    # exit function if books list is empty
    if is_library_books_empty():
        return
    
    # search for book to return
    book_to_return = search_books_by_keyword(input("Which book is being returned? "))

    # escape if book not found
    if book_to_return == None:
        print("No books have been returned. Returning to Main Menu.")
        return
    
    # if book is found
    else:

        # book is found and is checked out
        if not Book(book_to_return).get_is_available():
            book_return(book_to_return)

        # book is found, but is already available
        else:
            print(f"{Book(book_to_return).get_title()} is already available to borrow. It may have already been returned.")
            print("Returning to Main Menu.") 

def book_return(book):
    '''
    Return given book to library system.
    '''
    user = User(Book(book).get_borrower())
    user.remove_from_borrowed_books(Book(book).get_title())
    book.set_borrower = None
    book.set_is_available(True)
    print(f"\"{Book(book).get_title()}\" has been returned from user {User(user).get_name()}")

def book_search():
    '''
    Search for a book in the library.
    '''
    # exit function if books list is empty
    if is_library_books_empty():
        return
    
    while True:
        # get search term for book from user input
        search_input = input("Which book would you like to search for? ")

        # handle search cancel - return to main menu
        if search_input == "quit":
            break

        # ensure we are not searching with empty strings
        elif re.match(r"^\s+$", search_input): # or search_input == ""
            print("Error. Cannot search for empty term")

        # search for book
        else:
            book = search_books_by_keyword(search_input)
            if book != None:
                while True:
                    book_display_one(book)

                    if Book(book).get_is_available():
                        print(f"\n{F_YELLOW}1{F_RESET}. Borrow book")
                    else:
                        print(f"\n{F_YELLOW}1{F_RESET}. Return book")
                    print(f"{F_YELLOW}2{F_RESET}. View author details")
                    print(f"{F_YELLOW}3{F_RESET}. Quit to main menu")

                    # get and handle user input
                    menu_input = input("What would you like to do? ").casefold()
                    book_available = Book(book).get_is_available()
                    if menu_input == "1" or (book_available and menu_input.startswith("borrow")) or (not book_available and menu_input.startswith("return")):
                        if book_available:
                            book_borrow(book)
                        else:
                            book_return(book)
                        return
                    elif menu_input == "2" or menu_input.startswith("view"):
                        author = search_authors_by_name(Book(book).get_author(), False)
                        author_details(author)
                        return
                    elif menu_input == "3" or menu_input.startswith("quit"):
                        return
                    else:
                        print("Invalid input. Please make a selection from the menu.")
                    # return to main menu after function call
                    break

            # handle contact not found
            else:
                print("Enter a different search term or enter \"cancel\" to return to the main menu.")

def book_display_one(book):
    '''
    Display details of a single book, "book."
    '''
    # display all details for given book
    print(f"\nTitle: {F_GREEN}{Book(book).get_title()}{F_RESET}")
    print(f"Author: {Book(book).get_author()}")
    print(f"ISBN: {Book(book).get_isbn()}")
    print(f"Genre: {Book(book).get_genre()}")
    print(f"Publication Date: {Book(book).get_publication_date()}")
    if Book(book).get_is_available():
        print("Availability Status: Available")
    else:
        print("Availability Status: Currently Unavailable")
        print(f"Borrowed by User: {User(Book(book).get_borrower()).get_name()}, {User(Book(book).get_borrower()).get_library_id()}")

def book_display_all():
    '''
    Display all books in the library.
    '''
    # exit function if books list is empty
    if is_library_books_empty():
        return

    print("\nHere are all the books available at our library: ")

    # print all books in library, looping through list
    for b in library_books:
        book_display_one(b)

def user_add():
    '''
    Add a user to the library system.
    '''
    # create new user and set thier values with prompts below
    new_user = User()

    print()
    while(new_user.get_name() == None):
        new_user.set_title(input("What is the user's name? "))

    global user_id_increment
    new_user.set_library_id(user_id_increment)
    user_id_increment += 1

    library_users.append(new_user)

    print(f"{new_user.get_name()} has been added to the library system!")

def user_details():
    '''
    View details for a user in the library system.
    '''
    user_to_view = search_users_by_keyword(input("Which user would you like to view details for? "))
    if user_to_view:
        user_display_one(user_to_view)

def user_display_one(user):
    '''
    Display details of a given user
    '''
    print(f"\nName: {F_GREEN}{User(user).get_name()}{F_RESET}")
    print(f"Library ID: {str(User(user).get_library_id()).zfill(8)}")
    books_list = User(user).get_borrowed_books()
    books_list_output = ""
    if books_list == []:
        books_list_output = "None"
    else:
        for book in books_list:
            if books_list.index(book) == len(books_list) - 1:
                books_list_output += Book(book).get_title()
            else:
                books_list_output += f"{Book(book).get_title()}, "
    print(f"Borrowed Books: {books_list_output}")

def user_display_all():
    '''
    Display all users in the library system.
    '''
    # exit function if users list is empty
    if is_library_users_empty():
        return

    print("\nHere are all the users in our library system: ")

    # print all users in library, looping through list
    for u in library_users:
        user_display_one(u)

def author_add_via_input():
    '''
    Add an author to the library system through user input.
    '''
    # create new author and set thier values with prompts below
    new_author = Author()

    print()
    while(new_author.get_name() == None):
        new_author.set_name(input("What is the authors's name? "))

    new_author.set_biography(input(f"Enter a biography for {new_author}: "))

    library_authors.append(new_author)

    print(f"{new_author.get_name()} has been added to the library system!")

def author_add_via_book_add(author, book):
    '''
    Add an author to the library system from book addition, if they are not already in the system. Either way, add book to a list of their works.
    '''
    # create new author if they do not already exist in library system
    if search_authors_by_name(author, False) == None:
        new_author = Author()
        new_author.set_name(author)
        library_authors.append(new_author)

    # add given book to list of their works
    new_author.add_to_books_in_library(book)

def author_details():
    '''
    View details for an author in the library system.
    '''
    author_to_view = search_authors_by_name(input("Which author would you like to view details for? "), True)
    if author_to_view:
        author_display_one(author_to_view)

def author_display_one(author):
    '''
    Display details of a given author
    '''
    print(f"\nAuthor: {F_GREEN}{Author(author).get_name()}{F_RESET}")
    print(f"Biography: {Author(author).get_biography()}")
    books_list = Author(author).get_books_in_library()
    books_list_output = ""
    if books_list == []:
        books_list_output = "None"
    else:
        for book in books_list:
            if books_list.index(book) == len(books_list) - 1:
                books_list_output += Book(book).get_title()
            else:
                books_list_output += f"{Book(book).get_title()}, "
    print(f"Books in Library: {books_list_output}")

def author_display_all():
    '''
    Display all authors in the library system.
    '''
    # exit function if users list is empty
    if is_library_authors_empty():
        return

    print("\nHere are all the authors in our library system: ")

    # print all users in library, looping through list
    for a in library_authors:
        author_display_one(a)

def search_books_by_keyword(keyword):
    '''
    Loop through title, author, genre, and ISBN in all books looking for given search term. Returns book if found. Otherwise returns None.
    '''
    # compare search term with all values in books
    for book in library_books:
        book_details = [Book(book).get_title(), Book(book).get_author(), Book(book).get_isbn(), Book(book).get_genre()]
        for value in book_details:
            if keyword.casefold() in str(value).casefold():
                print(f"{F_YELLOW}Found the following book:{F_RESET}")
                book_display_one(book)
                while True:
                    confirm_input = input("Is this the book you are looking for? (yes/no): ").casefold()                
                    if confirm_input == "yes" or confirm_input == "y":
                        return book
                    # otherwise, keep searching!
                    elif confirm_input == "no" or confirm_input == "n":
                        break
                    else:
                        print("Invalid input. Please enter \"yes\" or \"no\"")
    # if no books found:
    print(f"No book found with search term \"{keyword}\"")
    return None

def search_users_by_keyword(keyword):
    '''
    Loop through name and library_id in all users looking for given search term. Returns user if found. Otherwise returns None.
    '''
    # compare search term with values in user
    for user in library_users:
        user_details = [User(user).get_name(), User(user).get_library_id()]
        for value in user_details:
            if keyword.casefold() in str(value).casefold():
                print(f"{F_YELLOW}Found the following user:{F_RESET}")
                user_display_one(user)
                while True:
                    confirm_input = input("Is this the user you are looking for? (yes/no): ").casefold()                
                    if confirm_input == "yes" or confirm_input == "y":
                        return user
                    # otherwise, keep searching!
                    elif confirm_input == "no" or confirm_input == "n":
                        break
                    else:
                        print("Invalid input. Please enter \"yes\" or \"no\"")
    # if no one found:
    print(f"No user found with search term \"{keyword}\"")
    return None

def search_authors_by_name(name, ask_for_confirmation):
    '''
    Loop through names of all users looking for given search term. Returns author if found. Otherwise returns None.
    '''
    # search through list of authors by name
    for author in library_authors:
        if name.casefold() in str(Author(author).get_name()).casefold():
            if ask_for_confirmation:
                print(f"{F_YELLOW}Found the following author:{F_RESET}")
                author_display_one(author)
                while True:
                    confirm_input = input("Is this the author you are looking for? (yes/no): ").casefold()      
                    # return author if found          
                    if confirm_input == "yes" or confirm_input == "y":
                        return author
                    # otherwise, keep searching!
                    elif confirm_input == "no" or confirm_input == "n":
                        break
                    else:
                        print("Invalid input. Please enter \"yes\" or \"no\"")
            else:
                return author
    # if no one found:
    print(f"No author found with search term \"{name}\"")
    return None

def is_library_books_empty():
    '''
    Check if there are any books in library. Return True if empty; otherwise, return False.
    '''
    if library_books == []:
        print("There are no books in the library! Please add some books!")
        return True
    else:
        return False

def is_library_users_empty():
    '''
    Check if there are any users in the library system. Return True if empty; otherwise, return False.
    '''
    if library_users == []:
        print("There are no users in the library system! Please register some users!")
        return True
    else:
        return False
    
def is_library_authors_empty():
    '''
    Check if there are any authors in the library system. Return True if empty; otherwise, return False.
    '''
    if library_authors == []:
        print("There are no authors in the library system! Please add some authors!")
        return True
    else:
        return False

# Computer, run program!
print("\nWelcome to the Library Management System!")
menu_main()