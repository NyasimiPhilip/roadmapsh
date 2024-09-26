# 🌟 Expense Tracker CLI 🌟[link](https://github.com/NyasimiPhilip/roadmapsh/tree/main/expense_tracker)

A simple command-line interface (CLI) tool to track your expenses, categorize them, and manage them across different currencies. This tracker stores all expenses in a local JSON file, allowing for easy data management and portability.

## ✨ Features

- **Add Expenses**: Track expenses with descriptions, categories, and amounts.
- **Expense Categories**: Group your expenses by categories (e.g., Food, Travel, Entertainment).
- **Currency Support**: Input expenses in different currencies with automatic conversion to your base currency.
- **Monthly Breakdown**: View a summary of your expenses and a detailed breakdown by category.
- **Edit Expenses**: Modify existing expenses easily using their ID.
- **Search Functionality**: Search for expenses by description or category.
- **Delete Expenses**: Remove expenses by their unique ID.

---

## 🛠️ Installation

1. **Ensure Python is installed**:
   - You’ll need Python 3.x installed on your system.

2. **Install necessary dependencies** (if any, for extended features):
   ```bash
   pip install argparse
   ```

3. **Make the script executable** (optional):
   ```bash
   chmod +x expense_tracker.py
   ```

---

## 🚀 Usage

You can interact with the expense tracker using various commands. Below is a guide on how to use them.

### 1. **Add an Expense**
```bash
python3 expense_tracker.py add --description "Lunch" --amount 20 --category "Food" --currency "USD" --conversion-rate 1.0
```

- Adds an expense with a description, amount, category, and currency. If the currency is different from the base currency, you can specify the `--conversion-rate`.

### 2. **List All Expenses**
```bash
python3 expense_tracker.py list
```

- Displays all the expenses in a neat table format, showing ID, date, description, category, amount, and currency.

### 3. **View Expense Summary**
```bash
python3 expense_tracker.py summary
```

- Shows the total expenses to date, with a breakdown by category.

#### **View Monthly Summary**
```bash
python3 expense_tracker.py summary --month 8
```

- Displays the total expenses for a given month, categorized by type.

### 4. **Delete an Expense**
```bash
python3 expense_tracker.py delete --id 1
```

- Deletes an expense by its unique ID.

### 5. **Edit an Expense**
```bash
python3 expense_tracker.py edit --id 1 --amount 30 --category "Dining"
```

- Updates an existing expense by specifying its ID and the fields you want to change (e.g., amount, category, description).

### 6. **Search for Expenses**
```bash
python3 expense_tracker.py search --keyword "Food"
```

- Finds expenses by keyword in the description or category.

---

## 📋 Example Workflow

Let’s go through a typical usage scenario:

1. **Add Expenses**:
   ```bash
   python3 expense_tracker.py add --description "Dinner" --amount 25 --category "Food" --currency "EUR" --conversion-rate 1.1
   python3 expense_tracker.py add --description "Uber" --amount 15 --category "Transport" --currency "USD" --conversion-rate 1.0
   ```

2. **List Your Expenses**:
   ```bash
   python3 expense_tracker.py list
   ```

   Output:
   ```bash
   ID   Date        Description    Category    Amount    Currency
   1    2024-09-25  Dinner         Food        $27.50    (EUR)
   2    2024-09-25  Uber           Transport   $15.00    (USD)
   ```

3. **View Summary**:
   ```bash
   python3 expense_tracker.py summary
   ```

   Output:
   ```bash
   Total expenses: $42.50
   
   Category breakdown:
   Food: $27.50
   Transport: $15.00
   ```

4. **Search for Expenses**:
   ```bash
   python3 expense_tracker.py search --keyword "Food"
   ```

   Output:
   ```bash
   ID   Date        Description    Category    Amount    Currency
   1    2024-09-25  Dinner         Food        $27.50    (EUR)
   ```

5. **Edit an Expense**:
   ```bash
   python3 expense_tracker.py edit --id 1 --amount 30 --category "Dining"
   ```

---

## 🛡️ Error Handling

- **Negative Amounts**: The tool prevents adding expenses with negative amounts.
- **Invalid IDs**: If you try to delete or edit an expense with an invalid ID, it will alert you.
- **File Not Found**: If the expenses file doesn't exist, it will create one automatically.

---

## 🧩 File Structure

```bash
expense_tracker/
│
├── expense_tracker.py  # Main script containing all logic
├── expenses.json       # File where all the expenses are stored
└── README.md           # This documentation
```

---

## 🎯 Future Enhancements

Some potential features to consider adding:

- **Recurring Expenses**: Ability to track recurring expenses (e.g., subscriptions).
- **Multi-User Support**: Allow multiple users to track their expenses independently.
- **Graphical Reports**: Generate graphs and charts for better visualization of expenses.

---


