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

    if not contacts_list:
        print("There are no contacts!")
        return

    for index, current_contact in enumerate(contacts_list, start= 1):
        print(f"{index}. {current_contact['name']}: {current_contact['number']}\n")
       


def serach_contact(contacts_list):
    print("---- Serach contacts ----\n")

    if not contacts_list:
        print("There are no contacts!")
        return
    
    serach_name = input("Enter the contact you want to look up: ")
    found = False

    
    for index, contact in enumerate(contacts_list, start= 1):
        if serach_name in contact['name']:
            print(f"{index}. {contact['name']}: {contact['number']}\n")
            found = True
    
    if not found:
        print(f"{serach_name} is not in the contacts list!")



def update_contact(contacts_list):
    print("---- Update contacts ----\n")

    if not contacts_list:
        print("There are no contacts!")
        return

    for index, current_contact in enumerate(contacts_list, start= 1):
        print(f"{index}. {current_contact['name']}: {current_contact['number']}\n")

    contact_update = int(input("Enter the number of the contact you want to update: "))

    actual_index =  contact_update - 1 

    if 0<= actual_index < len(contacts_list):
        name_update = input("Enter the updated name: ")
        number_update = input("Enter the updated number: ")

        contacts_list[actual_index]['name'] = name_update
        contacts_list[actual_index]['number'] = number_update

        print("Contact updated successfully!")


        with open(JSON_FILE, "w") as file:
            json.dump(contacts_list, file, indent=4)
    else:
        print("Invalid contact number!")
    
    return contacts_list
    

       


def delete_contact(contacts_list):
    print("---- Delete contacts ----\n")

    if not contacts_list:
        print("There are no contacts!")
        return

    for index, current_contact in enumerate(contacts_list, start= 1):
        print(f"{index}. {current_contact['name']}: {current_contact['number']}\n")

    remove_contact = int(input("Enter the number of the contact you want to delete: "))

    actual_index =  remove_contact - 1 

    if 0<= actual_index < len(contacts_list):
        removed_contact = contacts_list.pop(actual_index)
        print(f"\nSuccessfully deleted: '{removed_contact['name']}'")

        with open (JSON_FILE, "w") as file:
            json.dump(contacts_list, file, indent=4)
    else:
        print("Invalid task number!")
    return contacts_list




    

    







def main(contacts_list):
    is_running = True

    
    print("*************\nContact Book\n*************") 

    print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit\n") 

    option = int(input("Enter an option: "))

    if option == 1:
        contacts_list = add_contact(contacts_list)
    elif option == 2:
        view_contact(contacts_list)
    elif option == 3:
        serach_contact(contacts_list)
    elif option == 4:
        contacts_list = update_contact(contacts_list)
    elif option == 5:
        contacts_list = delete_contact(contacts_list)
    elif option == 6:
        is_running = False



if __name__ == "__main__":
    main(contacts_list)
