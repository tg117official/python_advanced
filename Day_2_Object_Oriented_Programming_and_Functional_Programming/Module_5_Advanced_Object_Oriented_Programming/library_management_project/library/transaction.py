class Transaction:
    """Class to manage borrowing and returning books."""

    @staticmethod
    def borrow(member, book):
        """Handle book borrowing."""
        try:
            member.borrow_book(book)
            print(f"{member.name} borrowed '{book.title}'.")
        except ValueError as e:
            print(f"Error: {e}")

    @staticmethod
    def return_book(member, book):
        """Handle book returning."""
        try:
            member.return_book(book)
            print(f"{member.name} returned '{book.title}'.")
        except ValueError as e:
            print(f"Error: {e}")
