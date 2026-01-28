import csv
from datetime import date
while True:
    print("\n--- Smart Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    # ================= ADD EXPENSE =================
    if choice == "1":
        today = date.today()
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        try:
            amount = int(amount)
        except ValueError:
            print("Amount must be a number.")
            continue
        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([today, amount, category])
        print("Expense saved successfully with date!")
    # ================= VIEW EXPENSES =================
    elif choice == "2":
        print("\n--- Expenses ---")
        total = 0
        found = False
        try:
            with open("expenses.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if len(row) != 3:
                        continue  # skip broken rows
                    date_val, amount_val, category = row
                    try:
                        amount_val = int(amount_val)
                    except ValueError:
                        continue  # skip invalid amount rows
                    print(f"Date: {date_val} | Amount: {amount_val} | Category: {category}")
                    total += amount_val
                    found = True
            if found:
                print(f"\nTotal Spent: {total}")
            else:
                print("No expenses recorded yet.")
        except FileNotFoundError:
            print("No expenses file found.")
    # ================= EXIT =================
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
