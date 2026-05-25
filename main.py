import json
import os

JSON_FILE = "contacts.json"

if os.path.exists(JSON_FILE) and os.path.getsize(JSON_FILE) > 0:
    with open(JSON_FILE, "r") as file:
        contacts_list = json.load(file)
else:
    contacts_list = []


def add_contact(contacts_list):
    print("---- Add a contact ----\n")

    contact_name = input("Enter the contact name: ")
    contact_number = int(input(f"Enter {contact_name}'s number: "))

    new_contact = {
        "name": contact_name,
        "number": contact_number
    }

    contacts_list.append(new_contact)
    print(f"{contact_name} has been added to your contact list!")

    with open (JSON_FILE, "w") as file:
        json.dump(contacts_list, file ,indent=4)
    
    return contacts_list


def view_contact(contacts_list):
    print("---- View contacts ----\n")

    for index, current_contact in enumerate(contacts_list, start= 1):
        print(f"{index}. {current_contact['name']}: {current_contact['number']}\n")
       
    




def serach_contact():
    pass

def update_contact():
    pass

def delete_contact():
    pass


def main(contacts_list):
    
    print("*************\nContact Book\n*************") 

    print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit\n") 

    option = int(input("Enter an option: "))

    if option == 1:
        contacts_list = add_contact(contacts_list)
    elif option == 2:
        view_contact(contacts_list)
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        pass


if __name__ == "__main__":
    main(contacts_list)
