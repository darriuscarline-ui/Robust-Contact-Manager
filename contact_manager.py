
"""
Robust Contact Manager

A command-line application for adding, finding, and deleting
contacts while handling common errors gracefully.
"""


class DuplicateContactError(Exception):
    """Raised when a contact name already exists."""


# Dictionary used to store contact names and phone numbers.
contacts = {}


def add_contact(name, phone):
    """Add a new contact unless the name already exists."""
    if name in contacts:
        # Raise a custom exception for duplicate contact names.
        raise DuplicateContactError(
            f"{name} already exists in contacts."
        )

    contacts[name] = phone
    print(f"Added {name} to contacts.")


def find_contact(name):
    """Find a contact and return the phone number if it exists."""
    try:
        phone_number = contacts[name]
        print(f"{name}: {phone_number}")
        return phone_number
    except KeyError:
        # Handle a missing dictionary key without crashing.
        print("Contact not found.")
        return None


def delete_contact(name):
    """Delete a contact if it exists."""
    try:
        del contacts[name]
        print(f"Deleted {name}.")
        return True
    except KeyError:
        # Handle attempts to delete missing contacts.
        print("Contact not found.")
        return False


def main():
    """Display the menu and process the user's choices."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")

        try:
            # Convert the user's menu choice into an integer.
            choice = int(input("Enter your choice: "))
        except ValueError:
            # Handle letters or other non-integer input.
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()

            try:
                add_contact(name, phone)
            except DuplicateContactError as error:
                # Display the custom exception's message.
                print(f"Error: {error}")

        elif choice == 2:
            name = input("Enter name to find: ").strip()
            find_contact(name)

        elif choice == 3:
            name = input("Enter name to delete: ").strip()
            delete_contact(name)

        elif choice == 4:
            print("Exiting Contact Manager.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
