# library_manager/inventory.py

import json
import logging
from pathlib import Path
from typing import List, Optional
from book import Book

logger = logging.getLogger(__name__)

class LibraryInventory:
    def __init__(self, data_file: Path):
        self.data_file = data_file
        self.books: List[Book] = []
        self.load_books()

    def load_books(self) -> None:
        if not self.data_file.exists():
            logger.info("Data file does not exist. Starting with empty inventory.")
            self.books = []
            return
        try:
            with self.data_file.open("r", encoding="utf-8") as f:
                data = json.load(f)
            self.books = [Book.from_dict(item) for item in data]
            logger.info("Loaded %d books from file.", len(self.books))
        except (json.JSONDecodeError, OSError) as e:
            logger.error("Failed to load books: %s", e)
            self.books = []

    def save_books(self) -> None:
        try:
            with self.data_file.open("w", encoding="utf-8") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=2)
            logger.info("Saved %d books to file.", len(self.books))
        except OSError as e:
            logger.error("Failed to save books: %s", e)

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info("Added book: %s", book.title)
        self.save_books()

    def search_by_title(self, title: str) -> List[Book]:
        title_lower = title.lower()
        return [b for b in self.books if title_lower in b.title.lower()]

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self) -> List[Book]:
        return list(self.books)

    def issue_book(self, isbn: str) -> bool:
        book = self.search_by_isbn(isbn)
        if book and book.issue():
            logger.info("Issued book: %s", isbn)
            self.save_books()
            return True
        logger.info("Could not issue book with ISBN: %s", isbn)
        return False

    def return_book(self, isbn: str) -> bool:
        book = self.search_by_isbn(isbn)
        if book and book.return_book():
            logger.info("Returned book: %s", isbn)
            self.save_books()
            return True
        logger.info("Could not return book with ISBN: %s", isbn)
        return False