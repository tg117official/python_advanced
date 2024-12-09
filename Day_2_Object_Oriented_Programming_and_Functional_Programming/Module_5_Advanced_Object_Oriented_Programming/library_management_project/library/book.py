class Book:
    """Class to represent a book in the library."""

    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.__copies = copies  # Private attribute

    @property
    def copies(self):
        return self.__copies

    @copies.setter
    def copies(self, value):
        if value >= 0:
            self.__copies = value
        else:
            raise ValueError("Copies cannot be negative.")

    def display_info(self):
        """Display book details."""
        return f"{self.title} by {self.author} - {self.copies} copies available"

    def lend(self):
        """Reduce copies by 1 if available."""
        if self.__copies > 0:
            self.__copies -= 1
        else:
            raise ValueError("No copies available!")

    def return_book(self):
        """Increase copies by 1."""
        self.__copies += 1
