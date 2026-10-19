
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print("Book added successfully!")

    def register_member(self, name, member_id):
        self.members.append(Member(name, member_id))
        print("Member registered successfully!")

    def borrow_book(self, title, member_id):
        for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.title == title and book.available:
                        book.available = False
                        print("Book borrowed successfully!")
                        return
                print("Book not available!")
                return
        print("Member not registered!")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print("Book returned successfully!")
                return
        print("Book not found or already available!")

    def display_books(self):
        print("\nAvailable Books:")
        found = False
        for book in self.books:
            if book.available:
                print(book.title, "-", book.author)
                found = True
        if not found:
            print("No books available.")


library = Library()

while True:
    print("\n1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)

    elif choice == "2":
        name = input("Enter member name: ")
        member_id = input("Enter member ID: ")
        library.register_member(name, member_id)

    elif choice == "3":
        title = input("Enter book title: ")
        member_id = input("Enter member ID: ")
        library.borrow_book(title, member_id)

    elif choice == "4":
        title = input("Enter book title: ")
        library.return_book(title)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Exiting Library Management System.")
        break

    else:
        print("Invalid choice! Try again.")
