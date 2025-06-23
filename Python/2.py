def add_expense(expenses):
    description = input("Enter expense description: ").strip()
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive!")
            return
        expenses.append((description, amount))
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount! Must be a number.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("\nExpenses:")
    for desc, amt in expenses:
        print(f"Description: {desc}, Amount: ${amt:.2f}")

def calculate_total(expenses):
    total = sum(amount for _, amount in expenses)
    print(f"Total expenses: ${total:.2f}")

def main():
    expenses = []
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            calculate_total(expenses)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()