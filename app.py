from utilis import database

#DATABASE BOOK LIBARY - @MAZVREK

USER_CHOISE = '''
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choise: '''

def menu():
    database.create_book_table()
    user_input = input(USER_CHOISE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('Unknown command! Insert new command!')

        user_input = input(USER_CHOISE)


def prompt_add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")

    database.add_book(name, author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'READ' if book['status'] else 'NOT READ'
        print(f"{book['id']}. {book['name']} by {book['author']}, Status: {read}")


def prompt_read_book():
    name = input("Enter name of the book you just read: ")

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter name of the book you want to delete: ")

    database.delete_book(name)

menu()