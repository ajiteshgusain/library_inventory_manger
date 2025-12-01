# library_inventory_manger
Library Inventory Manager

Course: Programming for Problem Solving using Python

Assignment Title: Object-Oriented Design and Robust Programming in a Library Management System

Project Overview

This is a lightweight, command-line-based application designed to help manage a small library's book inventory. The application utilizes Object-Oriented Programming (OOP) principles for structured design, employs robust exception handling, and uses JSON for persistent storage of the book catalog.

Features (Tasks 1-5 Implemented)

Book Management: Add new books, issue books (set status to 'issued'), and return books (set status to 'available').

Persistent Storage: The catalog is automatically saved to and loaded from catalog.json using the json and pathlib modules.

Robust File Handling: Uses try-except blocks to gracefully handle missing or corrupted catalog.json files.

Search Functionality: Search books by Title (partial match) or by exact ISBN.

User Interface: A simple, menu-driven command-line interface (CLI) for easy staff interaction.

Logging: Integrates Python's logging module to track application events (INFO) and errors (ERROR/CRITICAL) in library_manager.log (Task 5).

Installation and Usage

Prerequisites

You need Python 3.6 or newer installed on your system.

Setup

Clone the Repository (Simulated):

# git clone library-inventory-manager-<yourname>
# cd library-inventory-manager-<yourname>


Install Dependencies:
This project uses only built-in Python libraries (json, logging, pathlib, sys). The requirements.txt file confirms this.

Run the Application:
Navigate to the project root directory and run the main file:

python cli/main.py


File Structure (Task 6)

/library-inventory-manager
├── cli/
│   └── main.py              # Main CLI execution file (Task 4)
├── library_manager/
│   ├── __init__.py          # Marks library_manager as a Python package
│   ├── book.py              # Defines the Book class (Task 1)
│   └── inventory.py         # Defines the LibraryInventory class (Task 2, 3, 5)
├── catalog.json             # Persistent data store (Task 3)
├── library_manager.log      # Log file output (Task 5)
├── README.md                # This file
├── requirements.txt         # List of dependencies
└── .gitignore               # Files to ignore
