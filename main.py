expenses = []

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expenses.append({"date": date, "amount": amount, "category": category})
    print("Expense added!")


def view_expenses():
    for e in expenses:
        print(e)


def total_spent():
    total = sum([e["amount"] for e in expenses])
    print("Total Spent =", total)


def summary_by_category():
    summary = {}
    for e in expenses:
        cat = e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]
    print(summary)


def save_to_file():
    with open("expenses.csv", "w") as f:
        for e in expenses:
            f.write(f'{e["date"]},{e["amount"]},{e["category"]}\n')
    print("Saved!")


def load_from_file():
    try:
        with open("expenses.csv", "r") as f:
            for line in f:
                date, amount, category = line.strip().split(",")
                expenses.append({"date": date, "amount": float(amount), "category": category})
    except FileNotFoundError:
        pass


load_from_file()

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Total Spent\n4. Category Summary\n5. Save\n6. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add_expense()
    elif ch == "2":
        view_expenses()
    elif ch == "3":
        total_spent()
    elif ch == "4":
        summary_by_category()
    elif ch == "5":
        save_to_file()
    elif ch == "6":
        break
    else:
        print("Invalid Input")
