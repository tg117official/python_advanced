from library.book import Book
from library.member import Member
from library.transaction import Transaction
from library.utils import save_data, load_data


def main():
    books = []
    members = []

    while True:
        print("\n--- Library Management ---")
        print("1. Add a Book")
        print("2. Register a Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Display Library Data")
        print("6. Save Data")
        print("7. Load Data")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Add a new book
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, copies)
            books.append(book)
            print(f"Book '{title}' added successfully!")

        elif choice == "2":
            # Register a new member
            name = input("Enter member name: ")
            member_id = int(input("Enter member ID: "))
            try:
                member = Member.register_member(name, member_id)
                members.append(member)
                print(f"Member '{name}' registered successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            # Borrow a book
            if not books or not members:
                print("No books or members available!")
                continue

            member_id = int(input("Enter member ID: "))
            book_title = input("Enter book title to borrow: ")

            member = next((m for m in members if m.member_id == member_id), None)
            book = next((b for b in books if b.title == book_title), None)

            if member and book:
                Transaction.borrow(member, book)
            else:
                print("Invalid member ID or book title!")

        elif choice == "4":
            # Return a book
            if not books or not members:
                print("No books or members available!")
                continue

            member_id = int(input("Enter member ID: "))
            book_title = input("Enter book title to return: ")

            member = next((m for m in members if m.member_id == member_id), None)
            book = next((b for b in books if b.title == book_title), None)

            if member and book:
                Transaction.return_book(member, book)
            else:
                print("Invalid member ID or book title!")

        elif choice == "5":
            # Display library data
            print("\n--- Books ---")
            for book in books:
                print(book.display_info())
            print("\n--- Members ---")
            for member in members:
                print(member.display_info())

        elif choice == "6":
            # Save data
            books_data = "\n".join(book.display_info() for book in books)
            members_data = "\n".join(member.display_info() for member in members)
            save_data("data/books.txt", books_data)
            save_data("data/members.txt", members_data)
            print("Library data saved successfully!")

        elif choice == "7":
            # Load data
            print("Books Data:")
            print(load_data("data/books.txt"))
            print("Members Data:")
            print(load_data("data/members.txt"))

        elif choice == "8":
            # Exit the program
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again!")


if __name__ == "__main__":
    main()
