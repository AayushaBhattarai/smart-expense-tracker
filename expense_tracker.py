import csv

while True:
    print("\n--- Smart Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        amount = input("Enter amount: ")
        category = input("Enter category: ")

        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category])

        print("Expense saved successfully!")

    elif choice == "2":
        print("\n--- Expenses ---")
        try:
            with open("expenses.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(f"Amount: {row[0]} | Category: {row[1]}")
        except FileNotFoundError:
            print("No expenses found.")

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
