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
