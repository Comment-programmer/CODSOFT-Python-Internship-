# TASK-5-Contact Book

'''Contact Information: Store name, phone number, email, and address for each contact.'''

contacts = []

# Displaying the choices for user

def display_menu():
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Function for Adding Contacts

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print(f'Contact "{name}" added.')

# Function for Viewing Contacts

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

# Function for Searching Contacts

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            return
    print("No contact found.")

# Function for Updating Contacts

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated.")
            return
    print("Contact not found.")

# Function for Deleting Contacts

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("Contact deleted.")
            return
    print("Contact not found.")

# main fn for the choice input from user

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run

if __name__ == "__main__":
    main()
