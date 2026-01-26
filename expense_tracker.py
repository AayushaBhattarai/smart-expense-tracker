import csv
from datetime import date

while True:
    print("\n--- Smart Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        today = date.today()
        amount = input("Enter amount: ")
        category = input("Enter category: ")

        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([today, amount, category])

        print("Expense saved successfully with date!")

    elif choice == "2":
        print("\n--- Expenses ---")
        try:
            with open("expenses.csv", "r") as file:
                reader = csv.reader(file)
                found = False
                for row in reader:
                    if len(row) == 3:
                        print(f"Date: {row[0]} | Amount: {row[1]} | Category: {row[2]}")
                        found = True
                if not found:
                    print("No expenses recorded yet.")
        except FileNotFoundError:
            print("No expenses file found.")

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
