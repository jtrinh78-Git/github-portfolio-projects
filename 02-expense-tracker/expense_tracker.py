expenses = []

while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        expense_name = input("Enter expense name: ")

        try:
            expense_amount = float(input("Enter expense amount: "))
            expense = {"name": expense_name, "amount": expense_amount}
            expenses.append(expense)

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        if expenses:
            for number, expense in enumerate(expenses, start=1):
                print(f'{number}. {expense["name"]} - ${expense["amount"]:.2f}')
        else:
            print("No expenses yet.")

    elif choice == "3":
        total = 0
        for expense in expenses:
            total = total + expense["amount"]

        print(f"Total: ${total:.2f}")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please choose 1-4.")