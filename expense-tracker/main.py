import json


def load_expenses():
    try:
        with open('expenses.json', 'r')as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)


def add_expense(amount, category, description):
    expenses = load_expenses()

    new_expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(new_expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("Your expense list is empty.")
        return False

    print("\n--- Tracked Expenses ---")

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Amount: ${expense['amount']} | Category: {expense['category']} | Description: {expense['description']}")
    print() 
    return True


def delete_expense(index_to_delete):
    expenses = load_expenses()

    if not expenses:
        print("No expenses to delete.")
        return
    
    if 0 <= index_to_delete < len(expenses):
        removed = expenses.pop(index_to_delete)
        
        save_expenses(expenses)
        
        print(f"Successfully deleted: {removed['description']} (${removed['amount']})")
    else:
        print("Invalid option. That expense number does not exist.")


def view_total_spending():
    expenses = load_expenses()

    if not expenses:
        print("Total Spending: $0.00")
        return
    
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Spending: ${total:.2f}")


def view_spending_by_category():
    expenses = load_expenses()

    if not expenses:
        print("No expenses tracked yet.")
        return
    
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\n--- Spending By Category ---")
    for category, total in category_totals.items():
         print(f"{category}: ${total:.2f}")
    print()


def main():
    while True:
        print("****************\nExpense Tracker\n***************\n")
        print("1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. View Total Spending\n5. View Spending By Category\n6. Exit\n")
            
        try:
            option = int(input("Enter an option from the given: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue
    
        if option == 1:
            try:
                amount = float(input("Enter expense amount: $"))
            except ValueError:
                print("Invalid amount. Please enter a valid number.\n")
                continue
            category = input("Enter expense category: ")
            description = input("Enter expense description: ")
            add_expense(amount, category, description)
            print()

        elif option == 2:
            view_expenses()

        elif option == 3:
            if view_expenses():
                try:
                    index_input = int(input("Enter the number of the expense to delete: "))
                    delete_expense(index_input)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            print()

        elif option == 4:
            view_total_spending()
            print()

        elif option == 5:
            view_spending_by_category()
            
        elif option == 6:
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
             print("Invalid option. Please choose between 1 and 6.\n")


if __name__ == "__main__":
    main()
