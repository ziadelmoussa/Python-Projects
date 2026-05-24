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
        elif option == 5:
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option!")











if __name__ == "__main__":
    main()




