# Personal Expense Tracker (Python Project)

##  Project Title
**Personal Expense Tracker using Python**

##  1. Introduction
This Python-based Expense Tracker helps users add, view, and manage daily expenses.  
It also provides total spending and category-wise summaries.  
The project demonstrates Python basics like lists, dictionaries, loops, and file handling.

##  2. Objectives
- Add daily expenses with date, amount, and category  
- View all recorded expenses  
- Calculate total amount spent  
- Display category-wise summary  
- Save and load data using CSV file  
- Learn Python file handling and modular programming  

## 3. Requirements

### Software Requirements
- Python 3.x  
- IDE (IDLE, VS Code, PyCharm)

### Hardware Requirements
- Laptop or PC  
- 2 GB RAM or above  

### Knowledge Requirements
- Basics of Python  
- Lists, loops, dictionaries  
- Functions and file handling  

##  4. Features
- Simple menu-driven interface  
- Add/View expenses  
- Total spent calculation  
- Category-wise summary  
- Save & load using CSV file  

##  5. Project Flow
Start → Load Data → Show Menu → User Choice → Execute Task → Back to Menu → Exit

##  6. Folder Structure
Expense-Tracker/  
│── main.py  
│── expenses.csv  
└── README.md  

##  7. How to Run
1. Install Python  
2. Save the code in `main.py`  
3. Open terminal and run:  
```
python main.py
```

##  8. Python Code
```
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
```

##  9. Sample Output
```
1. Add Expense
2. View Expenses
3. Total Spent
4. Category Summary
5. Save
6. Exit
Enter choice: 1
Enter date: 22-11-2025
Enter amount: 150
Enter category: Food
Expense added!
```
