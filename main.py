import json
import os

JSON_FILE = "contacts.json"

if os.path.exists(JSON_FILE) and os.path.getsize(JSON_FILE) > 0:
    with open(JSON_FILE, "r") as file:
        contacts_list = json.load(file)
else:
    contacts_list = []



# Function for adding contact
def add_contact():
    pass


# Function for viewing contact
def view_contact():
    pass

# Function for seraching contact
def serach_contact():
    pass

# Function for updating contact
def update_contact():
    pass

# Function for deleting contact
def delete_contact():
    pass







# Main function to call all functions from it
def main():
    
    print("*************\nContact Book\n*************") 

    print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit\n") 

    option = int(input("Enter an option: "))


     
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        pass
       
    
    
    


if __name__ == "__main__":
    main()