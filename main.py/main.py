import csv

def display_menu():
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Spending")
    print("4. Exit")

def add_expense():
    item = input("What did you buy? ")
    price = input("How much did it cost? ")
    category = input("Category (Food, Transport, Fun): ")
    
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([item, price, category])
    print("Expense saved!")

def view_expenses():
    print("\n--- Your Expenses ---")
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Item: {row[0]} | Price: ${row[1]} | Category: {row[2]}")
    except FileNotFoundError:
        print("No expenses found yet.")

def show_total():
    total = 0
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
        print(f"\nTotal Spending: ${total:.2f}")
    except FileNotFoundError:
        print("No data yet.")

while True:
    display_menu()
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        show_total()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
