import json
import os

JSON_FILE = "tasks.json"

if os.path.exists(JSON_FILE) and os.path.getsize(JSON_FILE) > 0:
    with open(JSON_FILE, "r") as file:
        tasks_list = json.load(file)
else:
    tasks_list = []


def add_task(tasks_list):
    print("\n--- Add a New Task ---")
    
    task_name = input("\n Enter the task: ")

    new_task = {
        "task": task_name,
        "status": "Incomplete"
    }

    tasks_list.append(new_task)
    print(f"'{task_name}' added to your list successfully!")

    with open(JSON_FILE, "w") as file:
        json.dump(tasks_list, file, indent=4)

    return tasks_list

def view_task(tasks_list):
    print("\n--- Your Tasks ---\n")

    if not tasks_list:
        print("No tasks found!")
        return
    
    for index, current_item in enumerate(tasks_list, start=1):
        if current_item["status"] == "Complete":
            checkbox = "[x]"
        else:
            checkbox = "[ ]"
        print(f"{index}. {checkbox} {current_item['task']}\n")


def complete_task(tasks_list):
    print("\n--- Complete Tasks ---\n")

    if not tasks_list:
        print("No tasks found!")
        return
    

    for index, current_item in enumerate(tasks_list, start=1):
        if current_item["status"] == "Incomplete":
            checkbox = "[ ]"
            print(f"{index}. {checkbox} {current_item['task']}\n")

    completed_task = int(input("Enter the number of the task you have completed: "))

    actual_index = completed_task - 1

    if 0 <= actual_index < len(tasks_list):
        tasks_list[actual_index]["status"] = "Complete"
        print(f"\nSuccess! Changed status to [x] for: '{tasks_list[actual_index]['task']}'")

        with open(JSON_FILE, "w") as file:
            json.dump(tasks_list, file, indent=4)
    else:
        print("Invalid task number!")
    return tasks_list


def delete_task(tasks_list):
    print("\n--- Delete Tasks ---\n")

    if not tasks_list:
        print("No tasks found!")
        return
    
    for index, current_item in enumerate(tasks_list, start=1):
        if current_item["status"] == "Complete":
            checkbox = "[x]"
        else:
            checkbox = "[ ]"
        print(f"{index}. {checkbox} {current_item['task']}\n")

    delete_a_task = int(input("\nEnter the number of the task you want to delete: "))

    actual_index = delete_a_task - 1

    if 0 <= actual_index < len(tasks_list):
        removed_task = tasks_list.pop(actual_index)
        print(f"\nSuccessfully deleted: '{removed_task['task']}'")

        with open (JSON_FILE, "w") as file:
            json.dump(tasks_list, file, indent=4)
    else:
        print("Invalid task number!")
    return tasks_list









def main():
    global tasks_list

    while True:
        print("**************")
        print("To Do List App")
        print("**************")

        print("1. Add Task \n2. View Tasks \n3. Complete Task \n4. Delete Task \n5. Exit\n")

        option = int(input("Choose an option: "))

        if option == 1:
            tasks_list = add_task(tasks_list)
        elif option == 2:
            view_task(tasks_list)
        elif option == 3:
            tasks_list = complete_task(tasks_list)
        elif option == 4:
            tasks_list= delete_task(tasks_list)
        elif option == 5:
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option!")











if __name__ == "__main__":
    main()




