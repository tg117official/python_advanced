class Member:
    """Class to represent a library member."""
    all_members = []  # Class-level attribute

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = []  # Private attribute

    @staticmethod
    def is_valid_id(member_id):
        """Static method to validate member IDs."""
        return isinstance(member_id, int) and member_id > 0

    @classmethod
    def register_member(cls, name, member_id):
        """Class method to register a new member."""
        if cls.is_valid_id(member_id):
            member = cls(name, member_id)
            cls.all_members.append(member)
            return member
        else:
            raise ValueError("Invalid member ID!")

    def borrow_book(self, book):
        """Borrow a book."""
        try:
            book.lend()
            self.__borrowed_books.append(book.title)
        except ValueError as e:
            raise e

    def return_book(self, book):
        """Return a borrowed book."""
        if book.title in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book.title)
        else:
            raise ValueError("Book not borrowed!")

    def display_info(self):
        """Display member details."""
        return f"Member {self.member_id}: {self.name} (Borrowed: {', '.join(self.__borrowed_books)})"
