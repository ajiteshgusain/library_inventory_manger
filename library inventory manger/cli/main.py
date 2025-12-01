# cli/main.py

import logging
from pathlib import Path

from library_manager.inventory import LibraryInventory
from library_manager.book import Book

LOG_FILE = Path("app.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

def print_menu():
    print("\nLibrary Inventory Manager")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def add_book_ui(inventory: LibraryInventory):
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    isbn = input("Enter ISBN: ").strip()
    if not title or not author or not isbn:
        print("All fields are required.")
        return
    book = Book(title=title, author=author, isbn=isbn)
    inventory.add_book(book)
    print("Book added.")

def issue_book_ui(inventory: LibraryInventory):
    isbn = input("Enter ISBN to issue: ").strip()
    if inventory.issue_book(isbn):
        print("Book issued.")
    else:
        print("Book not available or not found.")

def return_book_ui(inventory: LibraryInventory):
    isbn = input("Enter ISBN to return: ").strip()
    if inventory.return_book(isbn):
        print("Book returned.")
    else:
        print("Book not found or already available.")

def view_all_ui(inventory: LibraryInventory):
    books = inventory.display_all()
    if not books:
        print("No books in inventory.")
        return
    for b in books:
        print(b)

def search_book_ui(inventory: LibraryInventory):
    print("Search by:")
    print("1. Title")
    print("2. ISBN")
    choice = input("Choose option: ").strip()
    if choice == "1":
        title = input("Enter title to search: ").strip()
        results = inventory.search_by_title(title)
        if not results:
            print("No books found.")
        else:
            for b in results:
                print(b)
    elif choice == "2":
        isbn = input("Enter ISBN to search: ").strip()
        book = inventory.search_by_isbn(isbn)
        if book:
            print(book)
        else:
            print("No book found.")
    else:
        print("Invalid choice.")

def main():
    data_file = Path("books.json")
    inventory = LibraryInventory(data_file=data_file)

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                add_book_ui(inventory)
            elif choice == "2":
                issue_book_ui(inventory)
            elif choice == "3":
                return_book_ui(inventory)
            elif choice == "4":
                view_all_ui(inventory)
            elif choice == "5":
                search_book_ui(inventory)
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
        except Exception as e:
            logging.error("Unexpected error: %s", e)
            print("An error occurred. Check log file for details.")

if __name__ == "__main__":
    main()