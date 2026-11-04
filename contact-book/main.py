import json
import os
import re

JSON_FILE = "contacts.json"

if os.path.exists(JSON_FILE) and os.path.getsize(JSON_FILE) > 0:
    with open(JSON_FILE, "r") as file:
        contacts_list = json.load(file)
else:
    contacts_list = []


def display_all_contacts(contacts_list):
    if not contacts_list:
        print("There are no contacts!")
        return False  

    for index, current_contact in enumerate(contacts_list, start=1):
        print(f"{index}.Name:{current_contact['name']}\nNumber:{current_contact['number']}\nEmail:{current_contact['email']}\n")
    
    return True  


def add_contact(contacts_list):
    print("---- Add a contact ----\n")

    contact_name = input("Enter the contact name: ").capitalize()

    if contact_name == "<":
        return contacts_list

    while True:
        num_input = input(f"Enter {contact_name}'s number: ")
        if num_input == "<":
            return contacts_list
        if num_input.isdigit():
            
            contact_number = num_input
            break
        print("Invalid number! Please enter digits only.\n")
    
    while True:
        contact_email = input(f"Enter {contact_name}'s email (e.g., name@email.com): ")
        if contact_email == "<":
            return contacts_list
        
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(email_pattern, contact_email):
            break
        print("Invalid email format! Please try again.\n")

    new_contact = {
        "name": contact_name,
        "number": contact_number,
        "email": contact_email
    }

    contacts_list.append(new_contact)
    print(f"{contact_name} has been added to your contact list!")

    with open(JSON_FILE, "w") as file:
        json.dump(contacts_list, file, indent=4)
    
    return contacts_list


def view_contact(contacts_list):
    print("---- View contacts ----\n")
    display_all_contacts(contacts_list)


def search_contact(contacts_list):
    print("---- Search contacts ----\n")

    if not contacts_list:
        print("There are no contacts!")
        return
    
    search_name = input("Enter the contact you want to look up: ").capitalize()
    found = False

    if search_name == "<":
        return
    
    for index, contact in enumerate(contacts_list, start=1):
        if search_name in contact['name']:
            print(f"\n{index}.Name:{contact['name']}\nNumber:{contact['number']}\nEmail:{contact['email']}\n")
            found = True
    
    if not found:
        print(f"{search_name} is not in the contacts list!")


def update_contact(contacts_list):
    print("---- Update contacts ----\n")

    if not display_all_contacts(contacts_list):
        return contacts_list

    user_input = input("Enter the number of the contact you want to update: ")

    if user_input == "<":
        return contacts_list

    try:
        contact_update = int(user_input)
    except ValueError:
        print("Invalid option! Returning to main menu.\n")
        return contacts_list

    actual_index = contact_update - 1 

    if 0 <= actual_index < len(contacts_list):
        name_update = input("Enter the updated name: ").capitalize()
        if name_update == "<": return contacts_list
        
        while True:
            number_update = input("Enter the updated number: ")
            if number_update == "<": return contacts_list
            if number_update.isdigit():
                break
            print("Invalid number! Please enter digits only.\n")
        
        while True:
            email_update = input("Enter the updated email (e.g., name@email.com): ")
            if email_update == "<": return contacts_list
            
            email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if re.match(email_pattern, email_update):
                break
            print("Invalid email format! Please try again.\n")

        contacts_list[actual_index]['name'] = name_update
        
        contacts_list[actual_index]['number'] = number_update
        contacts_list[actual_index]['email'] = email_update

        print("Contact updated successfully!")

        with open(JSON_FILE, "w") as file:
            json.dump(contacts_list, file, indent=4)
    else:
        print("Invalid contact number!")
    
    return contacts_list


def delete_contact(contacts_list):
    print("---- Delete contacts ----\n")

    if not display_all_contacts(contacts_list):
        return contacts_list
    
    user_input = input("Enter the number of the contact you want to delete: ")

    if user_input == "<":
        return contacts_list

    try:
        remove_contact = int(user_input)
    except ValueError:
        print("Invalid option! Returning to main menu.\n")
        return contacts_list

    actual_index = remove_contact - 1 

    if 0 <= actual_index < len(contacts_list):
        removed_contact = contacts_list.pop(actual_index)
        print(f"\nSuccessfully deleted: '{removed_contact['name']}'")

        with open(JSON_FILE, "w") as file:
            json.dump(contacts_list, file, indent=4)
    else:
        print("Invalid task number!")
    return contacts_list


def main(contacts_list):
    is_running = True

    while is_running:
        print("*************\nContact Book\n*************") 
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit\n") 
        print("IF YOU NEED TO GO BACK TYPE '<'\n")

        try:
            option_input = input("Enter an option: ")

            if option_input == "<":
                print("You are already on the main page!\n")
                continue
            option = int(option_input)

        except ValueError:
            print("Enter a number from the options!\n")
            continue

        if option == 1:
            contacts_list = add_contact(contacts_list)
        elif option == 2:
            view_contact(contacts_list)
        elif option == 3:
            search_contact(contacts_list)
        elif option == 4:
            contacts_list = update_contact(contacts_list)
        elif option == 5:
            contacts_list = delete_contact(contacts_list)
        elif option == 6:
            print("Goodbye!")
            is_running = False
        else:
            print("Invalid option please try again!\n")


if __name__ == "__main__":
    main(contacts_list)
