import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    name = input("Enter expense name: ")
    category = input("Enter category: ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    expense = {
        "name": name,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.\\n")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.\\n")
        return

    print("\\nExpenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} | {expense['category']} | ${expense['amount']:.2f}")
    print()


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\\nTotal spent: ${total:.2f}\\n")


def main():
    expenses = load_expenses()

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.\\n")


if __name__ == "__main__":
    main()