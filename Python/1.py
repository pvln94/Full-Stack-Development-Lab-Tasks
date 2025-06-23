def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number! Must be 10 digits.")
        return
    
    contacts.append({"name": name, "phone": phone})
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContacts:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(contacts):
    name = input("Enter name to search: ").strip().lower()
    found = False
    for contact in contacts:
        if contact['name'].lower() == name:
            print(f"Found - Name: {contact['name']}, Phone: {contact['phone']}")
            found = True
    if not found:
        print("Contact not found.")

def main():
    contacts = []
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()