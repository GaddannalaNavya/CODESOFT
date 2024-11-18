import pickle

class ContactBook:
    def _init_(self, filename="contacts.pkl"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from file."""
        try:
            with open(self.filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return {}
def save_contacts(self):
        """Save contacts to file."""
        with open(self.filename, "wb") as file:
            pickle.dump(self.contacts, file)
def add_contact(self):
        """Add a new contact."""
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email: ")
        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()
        print(f"Contact {name} added successfully!")

def view_contacts(self):
        """View all contacts."""
        if not self.contacts:
            print("No contacts found!")
        else:
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
def search_contact(self):
        """Search for a contact by name."""
        name = input("Enter the name to search: ")
        if name in self.contacts:
            info = self.contacts[name]
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            print("Contact not found.")
def update_contact(self):
        """Update an existing contact."""
        name = input("Enter the name of the contact to update: ")
        if name in self.contacts:
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email: ")
            self.contacts[name] = {"phone": phone, "email": email}
            self.save_contacts()
            print(f"Contact {name} updated successfully!")
        else:
            print("Contact not found.")
def menu(self):
        """Display the main menu."""
        while True:
            print("\n--- Contact Book ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Update Contact")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                self.update_contact()
            elif choice == "6":
                print("Exiting contact book...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()

