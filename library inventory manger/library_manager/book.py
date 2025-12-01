# library_manager/book.py

class Book:
    def __init__(self, title: str, author: str, isbn: str, status: str = "available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status.lower()

    def __str__(self) -> str:
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(
            title=data.get("title", ""),
            author=data.get("author", ""),
            isbn=data.get("isbn", ""),
            status=data.get("status", "available"),
        )

    def is_available(self) -> bool:
        return self.status == "available"

    def issue(self) -> bool:
        if self.is_available():
            self.status = "issued"
            return True
        return False

    def return_book(self) -> bool:
        if not self.is_available():
            self.status = "available"
            return True
        return False