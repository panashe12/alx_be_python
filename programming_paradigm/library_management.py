class Book:
    """Represents a book with a title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book to the library."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """Represents a collection of books with functions to manage them."""

    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Attempt to check out a book by title."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"Book titled '{title}' not found.")

    def return_book(self, title):
        """Attempt to return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book titled '{title}' not found.")

    def list_available_books(self):
        """Print a list of all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
