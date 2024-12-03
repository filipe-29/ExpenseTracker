import os
import json
from datetime import datetime


class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=2)

    def add_expense(self, amount, category, description):
        expense = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'amount': float(amount),
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self, category=None):
        filtered_expenses = self.expenses
        if category:
            filtered_expenses = [exp for exp in filtered_expenses if exp['category'].lower() == category.lower()]

        if not filtered_expenses:
            print("No expenses found.")
            return

        total = 0
        print("\n{:<12} {:<10} {:<15} {:<20}".format("Date", "Amount", "Category", "Description"))
        print("-" * 60)

        for expense in filtered_expenses:
            print("{:<12} ${:<9.2f} {:<15} {:<20}".format(
                expense['date'],
                expense['amount'],
                expense['category'],
                expense['description']
            ))
            total += expense['amount']

        print("-" * 60)
        print(f"Total Expenses: ${total:.2f}")

    def get_summary(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        # Category-wise summary
        category_totals = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            category_totals[category] = category_totals.get(category, 0) + amount

        print("\nCategory-wise Expense Summary:")
        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expense Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = input("Enter expense amount: ")
            category = input("Enter expense category: ")
            description = input("Enter expense description: ")
            tracker.add_expense(amount, category, description)

        elif choice == '2':
            category_filter = input("Enter category to filter (or press Enter for all): ")
            tracker.view_expenses(category_filter)

        elif choice == '3':
            tracker.get_summary()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()