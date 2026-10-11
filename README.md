# Robust-Contact-Manager

Project Overview

The robust contact manager is a python command-line application that allows users to add, find, and delete contacts. This project focuses on exception handling, debugging, and automated testing to make the program more reliable.

Features

1. Add new contacts with a name and phone number.
2. Find existing contacts.
3. Delete contacts from the contact list.
4. Handle missing contacts without crashing.
5. Validate menu input and handle invalid entries.
6. Prevent duplicate contacts using a custom exception.
7. Run automated tests using Python's unittest framwork. 

Bugs Fixed and Improvements

The original code could crash when a user attempted to find or delete a contact that did not exist. I added try/except blocks to catch KeyError exceptions and display a helpful message. I also added input validation to handle non-integer menu choices using ValueError. To prevent duplication contacts, I created a custom DuplicateContactError exception and used the raise statement when a contact name already exists. 

Project Files

1. buggy_contacts.py (The original starter code)
2. contact_manager.py (The corrected contact management program)
3. test_contact_manager.py (automated unit tests)

How to run the program 

Make sure python is installed. Open a terminal in the project folder and run: contact_manager.py.
Follow the menu instructions to add, find, or delete contacts.

How to run the unit test

Run the following command from the folder: test_contact_manager.py
The tests check adding a contact, finding an existing contact, handling a missing contact, deleting an existing contact, handling deletion of a missing contact, and rejecting duplicate contacts.

Video Demo: https://www.loom.com/share/5d5b9a6b0eca450c84721c707b044f6e
