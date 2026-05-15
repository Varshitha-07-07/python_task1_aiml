# Dictionary to store books
catalog = {}

# List to track borrowed books
borrowed_books = []

# Set to store unique members
members = set()


# Function to add books
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


# Function to borrow a book
def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print("Book borrowed successfully")
    else:
        print("Book not available")


# Function to return a book
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book returned successfully")
    else:
        print("Book was not borrowed")


# Function to register members
def register_member(members, member_id):
    members.add(member_id)


# Function to show available books
def show_available(catalog, borrowed_books):

    print("\nAvailable Books:")

    for book_id in catalog:
        if book_id not in borrowed_books:
            title, author, year = catalog[book_id]
            print(book_id, "-", title, "-", author, "-", year)


# Main function
def main():

    # Adding books
    add_book(catalog, 1, "Python Basics", "John", 2020)
    add_book(catalog, 2, "Data Science", "Alice", 2021)
    add_book(catalog, 3, "Machine Learning", "Bob", 2022)
    add_book(catalog, 4, "AI Fundamentals", "David", 2023)

    # Registering members
    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 103)
    register_member(members, 101)  # Duplicate ignored automatically

    # Borrow books
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 2)

    # Return one book
    return_book(borrowed_books, 1)

    # Show available books
    show_available(catalog, borrowed_books)


# Calling main function
main()